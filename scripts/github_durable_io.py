"""Descriptor-relative durable filesystem primitives for GitHub publication."""

import os
import re
import stat
from collections.abc import Sequence as SequenceABC
from typing import Dict, List, Optional, Sequence, Tuple


_SITE_PATTERN = re.compile(r"[a-z][a-z0-9._-]{0,95}")
_OPEN_SUPPORTS_DIR_FD = os.open in os.supports_dir_fd
_STAT_SUPPORTS_DIR_FD = os.stat in os.supports_dir_fd
_STAT_SUPPORTS_NOFOLLOW = os.stat in os.supports_follow_symlinks
_LINK_SUPPORTS_DIR_FD = os.link in os.supports_dir_fd
_LINK_SUPPORTS_NOFOLLOW = os.link in os.supports_follow_symlinks
_RENAME_SUPPORTS_DIR_FD = os.rename in os.supports_dir_fd
_UNLINK_SUPPORTS_DIR_FD = os.unlink in os.supports_dir_fd


class InjectedCrash(BaseException):
    """Simulate abrupt process termination at a named durability boundary."""

    def __init__(self, site: str, occurrence: int) -> None:
        self.site = site
        self.occurrence = occurrence
        super().__init__("injected crash at " + site + " #" + str(occurrence))


class DurableIOError(RuntimeError):
    """A bounded, path-redacted durable filesystem failure."""


class FailpointController:
    def __init__(
        self,
        target_site: Optional[str] = None,
        target_occurrence: Optional[int] = None,
    ) -> None:
        if (target_site is None) != (target_occurrence is None):
            raise ValueError("invalid failpoint target")
        if target_site is not None and not _is_valid_site(target_site):
            raise ValueError("invalid failpoint target")
        if target_occurrence is not None and (
            type(target_occurrence) is not int or target_occurrence <= 0
        ):
            raise ValueError("invalid failpoint target")
        self._target_site = target_site
        self._target_occurrence = target_occurrence
        self._counts: Dict[str, int] = {}
        self._trace: List[Tuple[str, int]] = []

    @property
    def trace(self) -> Tuple[Tuple[str, int], ...]:
        return tuple(self._trace)

    def checkpoint(self, site: str) -> None:
        if not _is_valid_site(site):
            raise ValueError("invalid failpoint site")
        occurrence = self._counts.get(site, 0) + 1
        self._counts[site] = occurrence
        self._trace.append((site, occurrence))
        if site == self._target_site and occurrence == self._target_occurrence:
            raise InjectedCrash(site, occurrence)


def _is_valid_site(site: object) -> bool:
    return type(site) is str and _SITE_PATTERN.fullmatch(site) is not None


class DurableIO:
    def __init__(self, failpoints: Optional[FailpointController] = None) -> None:
        self.failpoints = failpoints

    def bootstrap_directory_at(
        self, parent_fd: int, components: Sequence[str]
    ) -> int:
        safe_components = _validated_components(components)
        _require_directory_descriptor(parent_fd)
        current_descriptor = _duplicate_descriptor(parent_fd)
        next_descriptor: Optional[int] = None
        try:
            for component in safe_components:
                next_descriptor = _open_existing_directory_at(
                    current_descriptor, component
                )
                if next_descriptor is None:
                    self._checkpoint("namespace-mkdir-before")
                    try:
                        os.mkdir(component, 0o700, dir_fd=current_descriptor)
                    except OSError as error:
                        _raise_io_error("namespace mkdir", error)
                    self._checkpoint("namespace-mkdir-after")
                    next_descriptor = _open_required_directory_at(
                        current_descriptor, component
                    )

                # A prior crash can leave a visible component whose parent was
                # never synced, so existing components are re-synced as well.
                self.fsync_directory(current_descriptor, "namespace-parent-fsync")
                opened_stat = _require_directory_descriptor(next_descriptor)
                if not _entry_identity_matches(
                    current_descriptor,
                    component,
                    opened_stat,
                    directory_only=True,
                ):
                    raise DurableIOError("bootstrap component identity changed")
                os.close(current_descriptor)
                current_descriptor = next_descriptor
                next_descriptor = None

            result = current_descriptor
            current_descriptor = -1
            return result
        finally:
            if next_descriptor is not None:
                os.close(next_descriptor)
            if current_descriptor >= 0:
                os.close(current_descriptor)

    def write_fsync_at(
        self, parent_fd: int, name: str, content: bytes
    ) -> os.stat_result:
        _require_directory_descriptor(parent_fd)
        _require_safe_component(name)
        if type(content) is not bytes:
            raise ValueError("file content must be bytes")

        descriptor: Optional[int] = None
        self._checkpoint("file-create-before")
        try:
            descriptor = os.open(
                name, _exclusive_file_open_flags(), 0o600, dir_fd=parent_fd
            )
        except OSError as error:
            _raise_io_error("exclusive file creation", error)

        try:
            self._checkpoint("file-create-after")
            created_stat = _require_regular_descriptor(descriptor, "created file")
            if created_stat.st_nlink != 1:
                raise DurableIOError("created file has unexpected link count")

            offset = 0
            while offset < len(content):
                self._checkpoint("file-write-before")
                try:
                    written = os.write(descriptor, content[offset:])
                except InterruptedError:
                    continue
                except OSError as error:
                    _raise_io_error("file write", error)
                if written <= 0 or written > len(content) - offset:
                    raise DurableIOError("file write made invalid progress")
                offset += written
                self._checkpoint("file-write-after")

            while True:
                self._checkpoint("file-fsync-before")
                try:
                    os.fsync(descriptor)
                except InterruptedError:
                    continue
                except OSError as error:
                    _raise_io_error("file fsync", error)
                self._checkpoint("file-fsync-after")
                break

            result = _require_regular_descriptor(descriptor, "created file")
            if result.st_size != len(content) or result.st_nlink != 1:
                raise DurableIOError("created file identity is invalid")
            _require_name_matches_descriptor(parent_fd, name, result)
            return result
        finally:
            os.close(descriptor)

    def fsync_directory(self, descriptor: int, site: str) -> None:
        _require_directory_descriptor(descriptor)
        _require_fsync_site(site)
        while True:
            self._checkpoint(site + "-before")
            try:
                os.fsync(descriptor)
            except InterruptedError:
                continue
            except OSError as error:
                _raise_io_error("directory fsync", error)
            self._checkpoint(site + "-after")
            return

    def link_no_replace_at(
        self,
        source_parent_fd: int,
        source_name: str,
        destination_parent_fd: int,
        destination_name: str,
    ) -> None:
        _require_safe_component(source_name)
        _require_safe_component(destination_name)
        source_parent_stat = _require_directory_descriptor(source_parent_fd)
        destination_parent_stat = _require_directory_descriptor(destination_parent_fd)
        if source_parent_stat.st_dev != destination_parent_stat.st_dev:
            raise DurableIOError("hard-link parents are on different filesystems")
        if not _LINK_SUPPORTS_DIR_FD or not _LINK_SUPPORTS_NOFOLLOW:
            raise DurableIOError("required descriptor operations are unavailable")

        source_descriptor = _open_owned_entry_at(
            source_parent_fd, source_name, allow_directory=False
        )
        try:
            source_stat = _require_regular_descriptor(
                source_descriptor, "hard-link source"
            )
            if source_stat.st_dev != source_parent_stat.st_dev:
                raise DurableIOError("hard-link source is on a different filesystem")
            self._checkpoint("hard-link-before")
            try:
                os.link(
                    source_name,
                    destination_name,
                    src_dir_fd=source_parent_fd,
                    dst_dir_fd=destination_parent_fd,
                    follow_symlinks=False,
                )
            except OSError as error:
                _raise_io_error("no-replace hard link", error)
            self._checkpoint("hard-link-after")
            if not _entry_identity_matches(
                source_parent_fd, source_name, source_stat, regular_only=True
            ) or not _entry_identity_matches(
                destination_parent_fd,
                destination_name,
                source_stat,
                regular_only=True,
            ):
                raise DurableIOError("hard-link identity verification failed")
        finally:
            os.close(source_descriptor)

    def rename_fsync_both_at(
        self,
        source_parent_fd: int,
        source_name: str,
        destination_parent_fd: int,
        destination_name: str,
    ) -> None:
        _require_safe_component(source_name)
        _require_safe_component(destination_name)
        source_parent_stat = _require_directory_descriptor(source_parent_fd)
        destination_parent_stat = _require_directory_descriptor(destination_parent_fd)
        if source_name == destination_name and (
            source_parent_stat.st_dev,
            source_parent_stat.st_ino,
        ) == (
            destination_parent_stat.st_dev,
            destination_parent_stat.st_ino,
        ):
            raise ValueError("rename endpoints must differ")
        if source_parent_stat.st_dev != destination_parent_stat.st_dev:
            raise DurableIOError("rename parents are on different filesystems")
        if not _RENAME_SUPPORTS_DIR_FD:
            raise DurableIOError("required descriptor operations are unavailable")

        source_descriptor = _open_owned_entry_at(
            source_parent_fd, source_name, allow_directory=True
        )
        try:
            source_stat = _require_publishable_descriptor(
                source_descriptor, "rename source"
            )
            if source_stat.st_dev != source_parent_stat.st_dev:
                raise DurableIOError("rename source is on a different filesystem")
            self._checkpoint("rename-before")
            try:
                os.rename(
                    source_name,
                    destination_name,
                    src_dir_fd=source_parent_fd,
                    dst_dir_fd=destination_parent_fd,
                )
            except OSError as error:
                _raise_io_error("same-filesystem rename", error)
            self._checkpoint("rename-after")
            if not _entry_identity_matches(
                destination_parent_fd,
                destination_name,
                source_stat,
                regular_only=stat.S_ISREG(source_stat.st_mode),
                directory_only=stat.S_ISDIR(source_stat.st_mode),
            ):
                raise DurableIOError("rename identity verification failed")
            if _lstat_optional(source_parent_fd, source_name) is not None:
                raise DurableIOError("rename source namespace was replaced")
            self.fsync_directory(destination_parent_fd, "destination-parent-fsync")
            self.fsync_directory(source_parent_fd, "source-parent-fsync")
        finally:
            os.close(source_descriptor)

    def unlink_fsync_parent_at(self, parent_fd: int, name: str) -> None:
        _require_safe_component(name)
        _require_directory_descriptor(parent_fd)
        if not _UNLINK_SUPPORTS_DIR_FD:
            raise DurableIOError("required descriptor operations are unavailable")
        source_descriptor = _open_owned_entry_at(
            parent_fd, name, allow_directory=False
        )
        try:
            source_stat = _require_regular_descriptor(
                source_descriptor, "unlink source"
            )
            if not _entry_identity_matches(
                parent_fd, name, source_stat, regular_only=True
            ):
                raise DurableIOError("unlink source identity changed")
            self._checkpoint("unlink-before")
            if not _entry_identity_matches(
                parent_fd, name, source_stat, regular_only=True
            ):
                raise DurableIOError("unlink source identity changed")
            try:
                os.unlink(name, dir_fd=parent_fd)
            except OSError as error:
                _raise_io_error("unlink", error)
            self._checkpoint("unlink-after")
            unlinked_stat = _require_regular_descriptor(
                source_descriptor, "unlinked source"
            )
            if unlinked_stat.st_nlink != source_stat.st_nlink - 1:
                raise DurableIOError("unlink source link count did not decrease")
            if _lstat_optional(parent_fd, name) is not None:
                raise DurableIOError("unlink namespace was replaced")
            self.fsync_directory(parent_fd, "source-parent-fsync")
        finally:
            os.close(source_descriptor)

    def _checkpoint(self, site: str) -> None:
        if self.failpoints is not None:
            self.failpoints.checkpoint(site)


def _require_fsync_site(site: object) -> None:
    if (
        type(site) is not str
        or len(site) > 89
        or _SITE_PATTERN.fullmatch(site) is None
    ):
        raise ValueError("invalid fsync site")


def _validated_components(components: object) -> Tuple[str, ...]:
    if isinstance(components, (str, bytes)) or not isinstance(
        components, SequenceABC
    ):
        raise ValueError("unsafe component sequence")
    result = tuple(components)
    for component in result:
        _require_safe_component(component)
    return result


def _require_safe_component(component: object) -> None:
    if type(component) is not str or component in ("", ".", ".."):
        raise ValueError("unsafe path component")
    try:
        encoded = component.encode("utf-8")
    except UnicodeEncodeError:
        raise ValueError("unsafe path component") from None
    if (
        len(encoded) > 255
        or "/" in component
        or "\\" in component
        or "\0" in component
        or any(ord(character) < 32 or ord(character) == 127 for character in component)
    ):
        raise ValueError("unsafe path component")


def _require_directory_descriptor(descriptor: object) -> os.stat_result:
    if type(descriptor) is not int or descriptor < 0:
        raise ValueError("invalid directory descriptor")
    try:
        result = os.fstat(descriptor)
    except OSError as error:
        _raise_io_error("directory descriptor validation", error)
    if not stat.S_ISDIR(result.st_mode):
        raise DurableIOError("directory descriptor is not a directory")
    return result


def _duplicate_descriptor(descriptor: int) -> int:
    try:
        return os.dup(descriptor)
    except OSError as error:
        _raise_io_error("directory descriptor duplication", error)


def _directory_open_flags() -> int:
    directory = getattr(os, "O_DIRECTORY", None)
    no_follow = getattr(os, "O_NOFOLLOW", None)
    if (
        directory is None
        or no_follow is None
        or not _OPEN_SUPPORTS_DIR_FD
    ):
        raise DurableIOError("required descriptor operations are unavailable")
    return os.O_RDONLY | directory | no_follow | getattr(os, "O_CLOEXEC", 0)


def _exclusive_file_open_flags() -> int:
    no_follow = getattr(os, "O_NOFOLLOW", None)
    if no_follow is None or not _OPEN_SUPPORTS_DIR_FD:
        raise DurableIOError("required descriptor operations are unavailable")
    return (
        os.O_WRONLY
        | os.O_CREAT
        | os.O_EXCL
        | no_follow
        | getattr(os, "O_CLOEXEC", 0)
    )


def _open_existing_directory_at(parent_fd: int, component: str) -> Optional[int]:
    try:
        descriptor = os.open(component, _directory_open_flags(), dir_fd=parent_fd)
    except FileNotFoundError:
        return None
    except OSError as error:
        _raise_io_error("directory component open", error)
    try:
        _require_directory_descriptor(descriptor)
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _open_required_directory_at(parent_fd: int, component: str) -> int:
    descriptor = _open_existing_directory_at(parent_fd, component)
    if descriptor is None:
        raise DurableIOError("created directory component is missing")
    return descriptor


def _require_regular_descriptor(descriptor: int, label: str) -> os.stat_result:
    try:
        result = os.fstat(descriptor)
    except OSError as error:
        _raise_io_error(label + " validation", error)
    if not stat.S_ISREG(result.st_mode):
        raise DurableIOError(label + " is not a regular file")
    return result


def _require_publishable_descriptor(descriptor: int, label: str) -> os.stat_result:
    try:
        result = os.fstat(descriptor)
    except OSError as error:
        _raise_io_error(label + " validation", error)
    if not (stat.S_ISREG(result.st_mode) or stat.S_ISDIR(result.st_mode)):
        raise DurableIOError(label + " is not a regular file or directory")
    return result


def _open_owned_entry_at(
    parent_fd: int, name: str, allow_directory: bool
) -> int:
    observed = _lstat_at(parent_fd, name)
    if stat.S_ISREG(observed.st_mode):
        flags = (
            os.O_RDONLY
            | getattr(os, "O_NONBLOCK", 0)
            | getattr(os, "O_NOFOLLOW", 0)
            | getattr(os, "O_CLOEXEC", 0)
        )
    elif allow_directory and stat.S_ISDIR(observed.st_mode):
        flags = _directory_open_flags()
    else:
        raise DurableIOError("owned source type is invalid")
    if getattr(os, "O_NOFOLLOW", None) is None or not _OPEN_SUPPORTS_DIR_FD:
        raise DurableIOError("required descriptor operations are unavailable")
    try:
        descriptor = os.open(name, flags, dir_fd=parent_fd)
    except OSError as error:
        _raise_io_error("owned source open", error)
    try:
        opened = _require_publishable_descriptor(descriptor, "owned source")
        if (
            (opened.st_dev, opened.st_ino) != (observed.st_dev, observed.st_ino)
            or stat.S_IFMT(opened.st_mode) != stat.S_IFMT(observed.st_mode)
        ):
            raise DurableIOError("owned source identity changed")
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _lstat_at(parent_fd: int, name: str) -> os.stat_result:
    if not _STAT_SUPPORTS_DIR_FD or not _STAT_SUPPORTS_NOFOLLOW:
        raise DurableIOError("required descriptor operations are unavailable")
    try:
        return os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except OSError as error:
        _raise_io_error("namespace entry validation", error)


def _lstat_optional(parent_fd: int, name: str) -> Optional[os.stat_result]:
    if not _STAT_SUPPORTS_DIR_FD or not _STAT_SUPPORTS_NOFOLLOW:
        raise DurableIOError("required descriptor operations are unavailable")
    try:
        return os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except FileNotFoundError:
        return None
    except OSError as error:
        _raise_io_error("namespace entry validation", error)


def _entry_identity_matches(
    parent_fd: int,
    name: str,
    expected: os.stat_result,
    regular_only: bool = False,
    directory_only: bool = False,
) -> bool:
    observed = _lstat_optional(parent_fd, name)
    if observed is None:
        return False
    if regular_only and not stat.S_ISREG(observed.st_mode):
        return False
    if directory_only and not stat.S_ISDIR(observed.st_mode):
        return False
    return (observed.st_dev, observed.st_ino) == (expected.st_dev, expected.st_ino)


def _require_name_matches_descriptor(
    parent_fd: int, name: str, expected: os.stat_result
) -> None:
    if not _STAT_SUPPORTS_DIR_FD or not _STAT_SUPPORTS_NOFOLLOW:
        raise DurableIOError("required descriptor operations are unavailable")
    try:
        observed = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except OSError as error:
        _raise_io_error("created file namespace validation", error)
    if (
        not stat.S_ISREG(observed.st_mode)
        or (observed.st_dev, observed.st_ino) != (expected.st_dev, expected.st_ino)
    ):
        raise DurableIOError("created file namespace identity changed")


def _raise_io_error(operation: str, error: OSError) -> None:
    error_number = error.errno
    suffix = "unknown" if error_number is None else str(error_number)
    raise DurableIOError(operation + " failed (errno=" + suffix + ")") from None


__all__ = [
    "DurableIO",
    "DurableIOError",
    "FailpointController",
    "InjectedCrash",
]
