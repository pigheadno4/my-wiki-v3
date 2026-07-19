import errno
import importlib
import inspect
import os
import stat
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Optional, Sequence, get_type_hints
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_durable_io import (  # noqa: E402
    DurableIO,
    FailpointController,
    InjectedCrash,
)
import github_durable_io  # noqa: E402


class DurableIOPublicApiTests(unittest.TestCase):
    def test_public_api_has_the_fixed_descriptor_signatures(self):
        try:
            module = importlib.import_module("github_durable_io")
        except ModuleNotFoundError:
            self.fail("github_durable_io module is missing")

        self.assertTrue(issubclass(module.InjectedCrash, BaseException))
        controller_signature = inspect.signature(module.FailpointController)
        self.assertEqual(
            tuple(controller_signature.parameters),
            ("target_site", "target_occurrence"),
        )
        self.assertTrue(
            all(
                parameter.default is None
                for parameter in controller_signature.parameters.values()
            )
        )
        durable_signature = inspect.signature(module.DurableIO)
        self.assertEqual(tuple(durable_signature.parameters), ("failpoints",))
        self.assertIsNone(durable_signature.parameters["failpoints"].default)
        self.assertEqual(
            get_type_hints(module.FailpointController.__init__),
            {
                "target_site": Optional[str],
                "target_occurrence": Optional[int],
                "return": type(None),
            },
        )
        self.assertEqual(
            get_type_hints(module.DurableIO.__init__),
            {
                "failpoints": Optional[module.FailpointController],
                "return": type(None),
            },
        )
        expected = {
            "bootstrap_directory_at": (
                ("self", "parent_fd", "components"),
                {"parent_fd": int, "components": Sequence[str], "return": int},
            ),
            "write_fsync_at": (
                ("self", "parent_fd", "name", "content"),
                {
                    "parent_fd": int,
                    "name": str,
                    "content": bytes,
                    "return": os.stat_result,
                },
            ),
            "fsync_directory": (
                ("self", "descriptor", "site"),
                {"descriptor": int, "site": str, "return": type(None)},
            ),
            "link_no_replace_at": (
                (
                    "self",
                    "source_parent_fd",
                    "source_name",
                    "destination_parent_fd",
                    "destination_name",
                ),
                {
                    "source_parent_fd": int,
                    "source_name": str,
                    "destination_parent_fd": int,
                    "destination_name": str,
                    "return": type(None),
                },
            ),
            "rename_fsync_both_at": (
                (
                    "self",
                    "source_parent_fd",
                    "source_name",
                    "destination_parent_fd",
                    "destination_name",
                ),
                {
                    "source_parent_fd": int,
                    "source_name": str,
                    "destination_parent_fd": int,
                    "destination_name": str,
                    "return": type(None),
                },
            ),
            "unlink_fsync_parent_at": (
                ("self", "parent_fd", "name"),
                {"parent_fd": int, "name": str, "return": type(None)},
            ),
        }
        actual = {}
        for name in expected:
            method = getattr(module.DurableIO, name)
            actual[name] = (
                tuple(inspect.signature(method).parameters),
                get_type_hints(method),
            )
        self.assertEqual(actual, expected)


class FailpointControllerTests(unittest.TestCase):
    def test_records_ordered_occurrences_per_site(self):
        controller = FailpointController()

        controller.checkpoint("file-write-before")
        controller.checkpoint("file-write-after")
        controller.checkpoint("file-write-before")

        self.assertEqual(
            controller.trace,
            (
                ("file-write-before", 1),
                ("file-write-after", 1),
                ("file-write-before", 2),
            ),
        )

    def test_crashes_only_at_the_selected_site_occurrence(self):
        controller = FailpointController("file-write-before", 2)

        controller.checkpoint("file-write-before")
        controller.checkpoint("file-write-after")
        with self.assertRaises(InjectedCrash) as raised:
            controller.checkpoint("file-write-before")

        self.assertEqual(raised.exception.site, "file-write-before")
        self.assertEqual(raised.exception.occurrence, 2)
        self.assertLessEqual(len(str(raised.exception)), 160)
        self.assertEqual(controller.trace[-1], ("file-write-before", 2))

    def test_rejects_partial_or_unsafe_targets(self):
        invalid = (
            ("file-write-before", None),
            (None, 1),
            ("file-write-before", 0),
            ("file-write-before", True),
            ("contains/slash", 1),
            ("x" * 97, 1),
        )
        for site, occurrence in invalid:
            with self.subTest(site=site, occurrence=occurrence):
                with self.assertRaisesRegex(ValueError, r"^invalid failpoint target$"):
                    FailpointController(site, occurrence)

    def test_checkpoint_rejects_unbounded_or_untrusted_site_names(self):
        controller = FailpointController()
        for site in ("", "UPPER", "contains/slash", "contains space", "x" * 97):
            with self.subTest(site=site):
                with self.assertRaisesRegex(ValueError, r"^invalid failpoint site$"):
                    controller.checkpoint(site)

        self.assertEqual(controller.trace, ())

    def test_production_default_has_no_controller(self):
        self.assertIsNone(DurableIO().failpoints)


class DurableIOFilesystemTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.root_fd = os.open(
            str(self.root), os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
        )
        self.addCleanup(os.close, self.root_fd)

    def open_directory(self, path):
        descriptor = os.open(
            str(path), os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
        )
        self.addCleanup(os.close, descriptor)
        return descriptor

    def test_bootstrap_creates_each_component_and_fsyncs_its_parent(self):
        controller = FailpointController()
        descriptor = DurableIO(controller).bootstrap_directory_at(
            self.root_fd, ("transactions", "transaction-1")
        )
        self.addCleanup(os.close, descriptor)

        self.assertTrue(stat.S_ISDIR(os.fstat(descriptor).st_mode))
        self.assertTrue((self.root / "transactions" / "transaction-1").is_dir())
        self.assertEqual(
            controller.trace,
            (
                ("namespace-mkdir-before", 1),
                ("namespace-mkdir-after", 1),
                ("namespace-parent-fsync-before", 1),
                ("namespace-parent-fsync-after", 1),
                ("namespace-mkdir-before", 2),
                ("namespace-mkdir-after", 2),
                ("namespace-parent-fsync-before", 2),
                ("namespace-parent-fsync-after", 2),
            ),
        )

    def test_bootstrap_refsyncs_existing_components_for_crash_recovery(self):
        (self.root / "transactions" / "transaction-1").mkdir(parents=True)
        controller = FailpointController()
        descriptor = DurableIO(controller).bootstrap_directory_at(
            self.root_fd, ("transactions", "transaction-1")
        )
        self.addCleanup(os.close, descriptor)

        self.assertEqual(
            controller.trace,
            (
                ("namespace-parent-fsync-before", 1),
                ("namespace-parent-fsync-after", 1),
                ("namespace-parent-fsync-before", 2),
                ("namespace-parent-fsync-after", 2),
            ),
        )

    def test_bootstrap_empty_sequence_returns_an_independent_descriptor(self):
        descriptor = DurableIO().bootstrap_directory_at(self.root_fd, ())
        os.close(descriptor)

        self.assertTrue(stat.S_ISDIR(os.fstat(self.root_fd).st_mode))

    def test_bootstrap_rejects_unsafe_components_without_creating_any_path(self):
        invalid = (
            "",
            ".",
            "..",
            "nested/path",
            "windows\\path",
            "nul\0byte",
            "line\nbreak",
            "x" * 256,
        )
        for component in invalid:
            with self.subTest(component=repr(component)):
                with self.assertRaisesRegex(ValueError, r"^unsafe path component$"):
                    DurableIO().bootstrap_directory_at(self.root_fd, (component,))

        with self.assertRaisesRegex(ValueError, r"^unsafe component sequence$"):
            DurableIO().bootstrap_directory_at(self.root_fd, "child")
        self.assertEqual(tuple(self.root.iterdir()), ())

    def test_bootstrap_prevalidates_every_component_before_mutation(self):
        with self.assertRaisesRegex(ValueError, r"^unsafe path component$"):
            DurableIO().bootstrap_directory_at(
                self.root_fd, ("must-not-be-created", "../unsafe")
            )

        self.assertEqual(tuple(self.root.iterdir()), ())

    def test_bootstrap_rejects_symlink_and_non_directory_components(self):
        outside = self.root / "outside"
        outside.mkdir()
        (self.root / "regular-secret-name").write_text("not a directory")
        (self.root / "link-secret-name").symlink_to(outside, target_is_directory=True)

        for component in ("regular-secret-name", "link-secret-name"):
            with self.subTest(component=component):
                with self.assertRaises(github_durable_io.DurableIOError) as raised:
                    DurableIO().bootstrap_directory_at(self.root_fd, (component,))
                self.assertLessEqual(len(str(raised.exception)), 200)
                self.assertNotIn(component, str(raised.exception))

        self.assertEqual(tuple(outside.iterdir()), ())

    def test_bootstrap_rejects_component_replaced_by_symlink_after_mkdir(self):
        outside = self.root / "outside"
        outside.mkdir()
        real_mkdir = os.mkdir

        def replace_after_mkdir(name, mode=0o777, *, dir_fd=None):
            real_mkdir(name, mode, dir_fd=dir_fd)
            os.rmdir(name, dir_fd=dir_fd)
            (self.root / name).symlink_to(outside, target_is_directory=True)

        with mock.patch("github_durable_io.os.mkdir", side_effect=replace_after_mkdir):
            with self.assertRaises(github_durable_io.DurableIOError):
                DurableIO().bootstrap_directory_at(self.root_fd, ("created",))

        self.assertTrue((self.root / "created").is_symlink())
        self.assertEqual(tuple(outside.iterdir()), ())

    def test_bootstrap_closes_internal_descriptors_when_crash_is_injected(self):
        opened = []
        real_open = os.open

        def recording_open(*args, **kwargs):
            descriptor = real_open(*args, **kwargs)
            opened.append(descriptor)
            return descriptor

        controller = FailpointController("namespace-parent-fsync-before", 1)
        with mock.patch("github_durable_io.os.open", side_effect=recording_open):
            with self.assertRaises(InjectedCrash):
                DurableIO(controller).bootstrap_directory_at(
                    self.root_fd, ("transactions",)
                )

        self.assertGreaterEqual(len(opened), 1)
        for descriptor in opened:
            with self.subTest(descriptor=descriptor):
                with self.assertRaises(OSError):
                    os.fstat(descriptor)

    def test_bootstrap_rejects_existing_component_swapped_during_parent_fsync(self):
        existing = self.root / "existing"
        attacker = self.root / "attacker-existing"
        existing.mkdir()
        attacker.mkdir()
        (existing / "identity").write_bytes(b"intended")
        (attacker / "identity").write_bytes(b"replacement")
        real_fsync_directory = DurableIO.fsync_directory
        real_open = os.open
        real_dup = os.dup
        captured = []
        swapped = False

        def recording_open(*args, **kwargs):
            descriptor = real_open(*args, **kwargs)
            captured.append(descriptor)
            return descriptor

        def recording_dup(descriptor):
            duplicate = real_dup(descriptor)
            captured.append(duplicate)
            return duplicate

        def swap_after_fsync(instance, descriptor, site):
            nonlocal swapped
            real_fsync_directory(instance, descriptor, site)
            if not swapped and site == "namespace-parent-fsync":
                swapped = True
                os.rename(
                    "existing",
                    "preserved-existing",
                    src_dir_fd=descriptor,
                    dst_dir_fd=descriptor,
                )
                os.rename(
                    "attacker-existing",
                    "existing",
                    src_dir_fd=descriptor,
                    dst_dir_fd=descriptor,
                )

        def close_captured():
            for descriptor in set(captured):
                try:
                    os.close(descriptor)
                except OSError:
                    pass

        self.addCleanup(close_captured)
        with mock.patch("github_durable_io.os.open", side_effect=recording_open):
            with mock.patch("github_durable_io.os.dup", side_effect=recording_dup):
                with mock.patch.object(
                    DurableIO, "fsync_directory", new=swap_after_fsync
                ):
                    with self.assertRaisesRegex(
                        github_durable_io.DurableIOError,
                        r"^bootstrap component identity changed$",
                    ):
                        DurableIO().bootstrap_directory_at(self.root_fd, ("existing",))

        self.assertEqual((self.root / "existing" / "identity").read_bytes(), b"replacement")
        self.assertEqual(
            (self.root / "preserved-existing" / "identity").read_bytes(),
            b"intended",
        )
        self.assertGreaterEqual(len(captured), 2)
        for descriptor in set(captured):
            with self.assertRaises(OSError):
                os.fstat(descriptor)

    def test_bootstrap_rejects_new_component_swapped_during_parent_fsync(self):
        real_fsync_directory = DurableIO.fsync_directory
        real_open = os.open
        real_dup = os.dup
        captured = []
        swapped = False

        def recording_open(*args, **kwargs):
            descriptor = real_open(*args, **kwargs)
            captured.append(descriptor)
            return descriptor

        def recording_dup(descriptor):
            duplicate = real_dup(descriptor)
            captured.append(duplicate)
            return duplicate

        def swap_after_fsync(instance, descriptor, site):
            nonlocal swapped
            real_fsync_directory(instance, descriptor, site)
            if not swapped and site == "namespace-parent-fsync":
                swapped = True
                os.rename(
                    "created",
                    "preserved-created",
                    src_dir_fd=descriptor,
                    dst_dir_fd=descriptor,
                )
                os.mkdir("created", 0o700, dir_fd=descriptor)

        def close_captured():
            for descriptor in set(captured):
                try:
                    os.close(descriptor)
                except OSError:
                    pass

        self.addCleanup(close_captured)
        with mock.patch("github_durable_io.os.open", side_effect=recording_open):
            with mock.patch("github_durable_io.os.dup", side_effect=recording_dup):
                with mock.patch.object(
                    DurableIO, "fsync_directory", new=swap_after_fsync
                ):
                    with self.assertRaisesRegex(
                        github_durable_io.DurableIOError,
                        r"^bootstrap component identity changed$",
                    ):
                        DurableIO().bootstrap_directory_at(self.root_fd, ("created",))

        self.assertTrue((self.root / "created").is_dir())
        self.assertTrue((self.root / "preserved-created").is_dir())
        self.assertGreaterEqual(len(captured), 2)
        for descriptor in set(captured):
            with self.assertRaises(OSError):
                os.fstat(descriptor)

    def test_write_fsync_creates_exclusive_regular_file_and_returns_identity(self):
        controller = FailpointController()

        result = DurableIO(controller).write_fsync_at(
            self.root_fd, "terminal-event.json", b'{"state":"done"}'
        )

        path = self.root / "terminal-event.json"
        observed = path.stat()
        self.assertEqual(path.read_bytes(), b'{"state":"done"}')
        self.assertTrue(stat.S_ISREG(result.st_mode))
        self.assertEqual((result.st_dev, result.st_ino), (observed.st_dev, observed.st_ino))
        self.assertEqual(result.st_size, len(b'{"state":"done"}'))
        self.assertEqual(stat.S_IMODE(result.st_mode), 0o600)
        self.assertEqual(
            controller.trace,
            (
                ("file-create-before", 1),
                ("file-create-after", 1),
                ("file-write-before", 1),
                ("file-write-after", 1),
                ("file-fsync-before", 1),
                ("file-fsync-after", 1),
            ),
        )

    def test_write_fsync_accepts_empty_content_without_fake_write_site(self):
        controller = FailpointController()

        result = DurableIO(controller).write_fsync_at(self.root_fd, "COMMITTED", b"")

        self.assertEqual(result.st_size, 0)
        self.assertEqual(
            controller.trace,
            (
                ("file-create-before", 1),
                ("file-create-after", 1),
                ("file-fsync-before", 1),
                ("file-fsync-after", 1),
            ),
        )

    def test_write_fsync_never_replaces_existing_entry(self):
        outside = self.root / "outside"
        outside.write_bytes(b"outside")
        (self.root / "existing").write_bytes(b"original")
        (self.root / "link").symlink_to(outside)
        (self.root / "directory").mkdir()

        for name in ("existing", "link", "directory"):
            with self.subTest(name=name):
                with self.assertRaises(github_durable_io.DurableIOError):
                    DurableIO().write_fsync_at(self.root_fd, name, b"replacement")

        self.assertEqual((self.root / "existing").read_bytes(), b"original")
        self.assertEqual(outside.read_bytes(), b"outside")
        self.assertTrue((self.root / "directory").is_dir())

    def test_write_fsync_retries_interrupted_and_short_writes_and_fsync(self):
        real_write = os.write
        real_fsync = os.fsync
        write_calls = 0
        fsync_calls = 0

        def interrupted_short_write(descriptor, content):
            nonlocal write_calls
            write_calls += 1
            if write_calls == 1:
                raise InterruptedError(errno.EINTR, "interrupted secret")
            if write_calls == 2:
                return real_write(descriptor, content[:2])
            return real_write(descriptor, content)

        def interrupted_fsync(descriptor):
            nonlocal fsync_calls
            fsync_calls += 1
            if fsync_calls == 1:
                raise InterruptedError(errno.EINTR, "interrupted secret")
            return real_fsync(descriptor)

        controller = FailpointController()
        with mock.patch("github_durable_io.os.write", side_effect=interrupted_short_write):
            with mock.patch("github_durable_io.os.fsync", side_effect=interrupted_fsync):
                DurableIO(controller).write_fsync_at(
                    self.root_fd, "short-write", b"abcdef"
                )

        self.assertEqual((self.root / "short-write").read_bytes(), b"abcdef")
        self.assertEqual(write_calls, 3)
        self.assertEqual(fsync_calls, 2)
        self.assertEqual(
            [entry for entry in controller.trace if entry[0] == "file-write-before"],
            [("file-write-before", 1), ("file-write-before", 2), ("file-write-before", 3)],
        )
        self.assertEqual(
            [entry for entry in controller.trace if entry[0] == "file-write-after"],
            [("file-write-after", 1), ("file-write-after", 2)],
        )
        self.assertEqual(
            [entry for entry in controller.trace if entry[0] == "file-fsync-before"],
            [("file-fsync-before", 1), ("file-fsync-before", 2)],
        )

    def test_write_fsync_rejects_namespace_replacement_after_open(self):
        outside = self.root / "outside"
        outside.write_bytes(b"outside")
        real_write = os.write
        replaced = False

        def replacing_write(descriptor, content):
            nonlocal replaced
            written = real_write(descriptor, content)
            if not replaced:
                replaced = True
                os.unlink("staged", dir_fd=self.root_fd)
                (self.root / "staged").symlink_to(outside)
            return written

        with mock.patch("github_durable_io.os.write", side_effect=replacing_write):
            with self.assertRaises(github_durable_io.DurableIOError):
                DurableIO().write_fsync_at(self.root_fd, "staged", b"payload")

        self.assertTrue((self.root / "staged").is_symlink())
        self.assertEqual(outside.read_bytes(), b"outside")

    def test_write_fsync_closes_descriptor_at_every_post_open_crash_phase(self):
        real_open = os.open
        cases = (
            ("file-create-after", b""),
            ("file-write-after", b"payload"),
            ("file-fsync-after", b"payload"),
        )
        for index, (site, expected) in enumerate(cases):
            with self.subTest(site=site):
                opened = []

                def recording_open(*args, **kwargs):
                    descriptor = real_open(*args, **kwargs)
                    opened.append(descriptor)
                    return descriptor

                name = "staged-" + str(index)
                controller = FailpointController(site, 1)
                with mock.patch("github_durable_io.os.open", side_effect=recording_open):
                    with self.assertRaises(InjectedCrash):
                        DurableIO(controller).write_fsync_at(
                            self.root_fd, name, b"payload"
                        )

                self.assertEqual(len(opened), 1)
                with self.assertRaises(OSError):
                    os.fstat(opened[0])
                self.assertEqual((self.root / name).read_bytes(), expected)

    def test_write_fsync_errors_are_bounded_and_do_not_echo_names_or_os_text(self):
        secret_name = "merchant-production-secret"
        error = OSError(errno.EACCES, "credential=do-not-report", secret_name)
        with mock.patch("github_durable_io.os.open", side_effect=error):
            with self.assertRaises(github_durable_io.DurableIOError) as raised:
                DurableIO().write_fsync_at(self.root_fd, secret_name, b"secret bytes")

        message = str(raised.exception)
        self.assertLessEqual(len(message), 200)
        self.assertNotIn(secret_name, message)
        self.assertNotIn("credential", message)
        self.assertNotIn("secret bytes", message)

    def test_write_fsync_rejects_invalid_names_and_content_types(self):
        with self.assertRaisesRegex(ValueError, r"^unsafe path component$"):
            DurableIO().write_fsync_at(self.root_fd, "nested/file", b"content")
        with self.assertRaisesRegex(ValueError, r"^file content must be bytes$"):
            DurableIO().write_fsync_at(self.root_fd, "file", bytearray(b"content"))
        self.assertEqual(tuple(self.root.iterdir()), ())

    def test_fsync_directory_retries_eintr_and_traces_each_attempt(self):
        real_fsync = os.fsync
        calls = 0

        def interrupted_once(descriptor):
            nonlocal calls
            calls += 1
            if calls == 1:
                raise InterruptedError(errno.EINTR, "secret")
            return real_fsync(descriptor)

        controller = FailpointController()
        with mock.patch("github_durable_io.os.fsync", side_effect=interrupted_once):
            DurableIO(controller).fsync_directory(self.root_fd, "source-parent-fsync")

        self.assertEqual(
            controller.trace,
            (
                ("source-parent-fsync-before", 1),
                ("source-parent-fsync-before", 2),
                ("source-parent-fsync-after", 1),
            ),
        )

    def test_fsync_directory_rejects_file_descriptors_and_unsafe_sites(self):
        path = self.root / "file"
        path.write_bytes(b"content")
        descriptor = os.open(str(path), os.O_RDONLY)
        self.addCleanup(os.close, descriptor)

        with self.assertRaises(github_durable_io.DurableIOError):
            DurableIO().fsync_directory(descriptor, "source-parent-fsync")
        with self.assertRaisesRegex(ValueError, r"^invalid fsync site$"):
            DurableIO().fsync_directory(self.root_fd, "contains/slash")

    def test_link_no_replace_creates_same_inode_without_implicit_parent_fsync(self):
        source = self.root / "staging"
        destination = self.root / "history"
        source.mkdir()
        destination.mkdir()
        source_fd = self.open_directory(source)
        destination_fd = self.open_directory(destination)
        DurableIO().write_fsync_at(source_fd, "event.staged", b"event")
        controller = FailpointController()

        DurableIO(controller).link_no_replace_at(
            source_fd, "event.staged", destination_fd, "event.json"
        )

        source_stat = (source / "event.staged").stat()
        destination_stat = (destination / "event.json").stat()
        self.assertEqual(
            (source_stat.st_dev, source_stat.st_ino),
            (destination_stat.st_dev, destination_stat.st_ino),
        )
        self.assertEqual((destination / "event.json").read_bytes(), b"event")
        self.assertEqual(
            controller.trace,
            (("hard-link-before", 1), ("hard-link-after", 1)),
        )

    def test_link_no_replace_rejects_existing_destinations_and_unsafe_sources(self):
        source = self.root / "staging"
        destination = self.root / "history"
        outside = self.root / "outside"
        source.mkdir()
        destination.mkdir()
        outside.write_bytes(b"outside")
        (source / "event.staged").write_bytes(b"event")
        (source / "link-source").symlink_to(outside)
        (source / "directory-source").mkdir()
        (destination / "existing").write_bytes(b"existing")
        (destination / "link").symlink_to(outside)
        (destination / "directory").mkdir()
        source_fd = self.open_directory(source)
        destination_fd = self.open_directory(destination)

        for name in ("existing", "link", "directory"):
            with self.subTest(destination=name):
                with self.assertRaises(github_durable_io.DurableIOError):
                    DurableIO().link_no_replace_at(
                        source_fd, "event.staged", destination_fd, name
                    )
        for name in ("link-source", "directory-source"):
            with self.subTest(source=name):
                with self.assertRaises(github_durable_io.DurableIOError):
                    DurableIO().link_no_replace_at(
                        source_fd, name, destination_fd, "new-" + name
                    )

        self.assertEqual((destination / "existing").read_bytes(), b"existing")
        self.assertEqual(outside.read_bytes(), b"outside")

    def test_link_no_replace_preflights_same_filesystem(self):
        source = self.root / "staging"
        destination = self.root / "history"
        source.mkdir()
        destination.mkdir()
        (source / "event.staged").write_bytes(b"event")
        source_fd = self.open_directory(source)
        destination_fd = self.open_directory(destination)
        real_fstat = os.fstat

        def different_device(descriptor):
            observed = real_fstat(descriptor)
            if descriptor != destination_fd:
                return observed
            values = list(observed)
            values[2] = observed.st_dev + 1
            return os.stat_result(values)

        with mock.patch("github_durable_io.os.fstat", side_effect=different_device):
            with mock.patch("github_durable_io.os.link") as link:
                with self.assertRaisesRegex(
                    github_durable_io.DurableIOError,
                    r"^hard-link parents are on different filesystems$",
                ):
                    DurableIO().link_no_replace_at(
                        source_fd, "event.staged", destination_fd, "event.json"
                    )
                link.assert_not_called()

    def test_link_no_replace_detects_source_replacement_during_operation(self):
        source = self.root / "staging"
        destination = self.root / "history"
        source.mkdir()
        destination.mkdir()
        (source / "event.staged").write_bytes(b"intended")
        (source / "attacker").write_bytes(b"attacker")
        source_fd = self.open_directory(source)
        destination_fd = self.open_directory(destination)
        real_link = os.link

        def replacing_link(*args, **kwargs):
            os.unlink("event.staged", dir_fd=source_fd)
            os.rename("attacker", "event.staged", src_dir_fd=source_fd, dst_dir_fd=source_fd)
            return real_link(*args, **kwargs)

        with mock.patch("github_durable_io.os.link", side_effect=replacing_link):
            with self.assertRaisesRegex(
                github_durable_io.DurableIOError,
                r"^hard-link identity verification failed$",
            ):
                DurableIO().link_no_replace_at(
                    source_fd, "event.staged", destination_fd, "event.json"
                )

        self.assertEqual((destination / "event.json").read_bytes(), b"attacker")

    def test_rename_fsync_both_replaces_destination_and_fsyncs_both_roles(self):
        source = self.root / "staging"
        destination = self.root / "published"
        source.mkdir()
        destination.mkdir()
        (source / "after-index.json").write_bytes(b"after")
        (destination / "index.json").write_bytes(b"before")
        source_fd = self.open_directory(source)
        destination_fd = self.open_directory(destination)
        controller = FailpointController()

        DurableIO(controller).rename_fsync_both_at(
            source_fd, "after-index.json", destination_fd, "index.json"
        )

        self.assertFalse((source / "after-index.json").exists())
        self.assertEqual((destination / "index.json").read_bytes(), b"after")
        self.assertEqual(
            controller.trace,
            (
                ("rename-before", 1),
                ("rename-after", 1),
                ("destination-parent-fsync-before", 1),
                ("destination-parent-fsync-after", 1),
                ("source-parent-fsync-before", 1),
                ("source-parent-fsync-after", 1),
            ),
        )

    def test_rename_fsync_both_supports_owned_directories(self):
        source = self.root / "staging"
        destination = self.root / "published"
        source.mkdir()
        destination.mkdir()
        artifact = source / "artifact"
        artifact.mkdir()
        (artifact / "snapshot.md").write_bytes(b"snapshot")
        original = artifact.stat()
        source_fd = self.open_directory(source)
        destination_fd = self.open_directory(destination)

        DurableIO().rename_fsync_both_at(
            source_fd, "artifact", destination_fd, "artifact-final"
        )

        observed = (destination / "artifact-final").stat()
        self.assertEqual((observed.st_dev, observed.st_ino), (original.st_dev, original.st_ino))
        self.assertEqual(
            (destination / "artifact-final" / "snapshot.md").read_bytes(),
            b"snapshot",
        )

    def test_rename_fsync_both_fsyncs_twice_for_one_parent_descriptor(self):
        (self.root / "source").write_bytes(b"content")
        controller = FailpointController()

        DurableIO(controller).rename_fsync_both_at(
            self.root_fd, "source", self.root_fd, "destination"
        )

        self.assertEqual((self.root / "destination").read_bytes(), b"content")
        self.assertEqual(
            controller.trace,
            (
                ("rename-before", 1),
                ("rename-after", 1),
                ("destination-parent-fsync-before", 1),
                ("destination-parent-fsync-after", 1),
                ("source-parent-fsync-before", 1),
                ("source-parent-fsync-after", 1),
            ),
        )

    def test_rename_fsync_both_rejects_cross_filesystem_before_mutation(self):
        source = self.root / "staging"
        destination = self.root / "published"
        source.mkdir()
        destination.mkdir()
        (source / "artifact").write_bytes(b"content")
        source_fd = self.open_directory(source)
        destination_fd = self.open_directory(destination)
        real_fstat = os.fstat

        def different_device(descriptor):
            observed = real_fstat(descriptor)
            if descriptor != destination_fd:
                return observed
            values = list(observed)
            values[2] = observed.st_dev + 1
            return os.stat_result(values)

        with mock.patch("github_durable_io.os.fstat", side_effect=different_device):
            with mock.patch("github_durable_io.os.rename") as rename:
                with self.assertRaisesRegex(
                    github_durable_io.DurableIOError,
                    r"^rename parents are on different filesystems$",
                ):
                    DurableIO().rename_fsync_both_at(
                        source_fd, "artifact", destination_fd, "artifact"
                    )
                rename.assert_not_called()

        self.assertEqual((source / "artifact").read_bytes(), b"content")

    def test_rename_fsync_both_rejects_symlink_source_and_equal_endpoint(self):
        outside = self.root / "outside"
        outside.write_bytes(b"outside")
        (self.root / "link").symlink_to(outside)
        second_root_fd = self.open_directory(self.root)

        with self.assertRaises(github_durable_io.DurableIOError):
            DurableIO().rename_fsync_both_at(
                self.root_fd, "link", self.root_fd, "destination"
            )
        with self.assertRaisesRegex(ValueError, r"^rename endpoints must differ$"):
            DurableIO().rename_fsync_both_at(
                self.root_fd, "outside", second_root_fd, "outside"
            )
        self.assertEqual(outside.read_bytes(), b"outside")

    def test_unlink_fsync_parent_removes_regular_file_and_syncs_parent(self):
        (self.root / "staged-link").write_bytes(b"event")
        controller = FailpointController()

        DurableIO(controller).unlink_fsync_parent_at(self.root_fd, "staged-link")

        self.assertFalse((self.root / "staged-link").exists())
        self.assertEqual(
            controller.trace,
            (
                ("unlink-before", 1),
                ("unlink-after", 1),
                ("source-parent-fsync-before", 1),
                ("source-parent-fsync-after", 1),
            ),
        )

    def test_unlink_revalidates_name_after_the_before_failpoint(self):
        (self.root / "intended").write_bytes(b"intended")
        (self.root / "replacement").write_bytes(b"replacement")
        controller = FailpointController()
        real_checkpoint = controller.checkpoint
        swapped = False

        def swap_at_before_site(site):
            nonlocal swapped
            real_checkpoint(site)
            if not swapped and site == "unlink-before":
                swapped = True
                os.rename(
                    "intended",
                    "preserved-intended",
                    src_dir_fd=self.root_fd,
                    dst_dir_fd=self.root_fd,
                )
                os.rename(
                    "replacement",
                    "intended",
                    src_dir_fd=self.root_fd,
                    dst_dir_fd=self.root_fd,
                )

        with mock.patch.object(controller, "checkpoint", side_effect=swap_at_before_site):
            with self.assertRaisesRegex(
                github_durable_io.DurableIOError,
                r"^unlink source identity changed$",
            ):
                DurableIO(controller).unlink_fsync_parent_at(
                    self.root_fd, "intended"
                )

        self.assertEqual((self.root / "preserved-intended").read_bytes(), b"intended")
        self.assertEqual((self.root / "intended").read_bytes(), b"replacement")

    def test_unlink_detects_name_swap_inside_unlink_from_intended_link_count(self):
        (self.root / "intended").write_bytes(b"intended")
        (self.root / "replacement").write_bytes(b"replacement")
        real_unlink = os.unlink
        swapped = False

        def swap_then_unlink(name, *, dir_fd=None):
            nonlocal swapped
            if not swapped:
                swapped = True
                os.rename(
                    name,
                    "preserved-intended",
                    src_dir_fd=dir_fd,
                    dst_dir_fd=dir_fd,
                )
                os.rename(
                    "replacement",
                    name,
                    src_dir_fd=dir_fd,
                    dst_dir_fd=dir_fd,
                )
            return real_unlink(name, dir_fd=dir_fd)

        with mock.patch("github_durable_io.os.unlink", side_effect=swap_then_unlink):
            with self.assertRaisesRegex(
                github_durable_io.DurableIOError,
                r"^unlink source link count did not decrease$",
            ) as raised:
                DurableIO().unlink_fsync_parent_at(self.root_fd, "intended")

        self.assertLessEqual(len(str(raised.exception)), 200)
        self.assertEqual((self.root / "preserved-intended").read_bytes(), b"intended")
        self.assertFalse((self.root / "intended").exists())

    def test_unlink_normal_hard_link_cleanup_decrements_link_count_from_two_to_one(self):
        (self.root / "retained").write_bytes(b"event")
        os.link(self.root / "retained", self.root / "staged-link")
        self.assertEqual((self.root / "retained").stat().st_nlink, 2)

        DurableIO().unlink_fsync_parent_at(self.root_fd, "staged-link")

        self.assertFalse((self.root / "staged-link").exists())
        self.assertEqual((self.root / "retained").read_bytes(), b"event")
        self.assertEqual((self.root / "retained").stat().st_nlink, 1)

    def test_unlink_fsync_parent_rejects_symlink_directory_and_missing_entry(self):
        outside = self.root / "outside"
        outside.write_bytes(b"outside")
        (self.root / "link").symlink_to(outside)
        (self.root / "directory").mkdir()

        for name in ("link", "directory", "missing"):
            with self.subTest(name=name):
                with self.assertRaises(github_durable_io.DurableIOError) as raised:
                    DurableIO().unlink_fsync_parent_at(self.root_fd, name)
                self.assertNotIn(name, str(raised.exception))

        self.assertTrue((self.root / "link").is_symlink())
        self.assertTrue((self.root / "directory").is_dir())
        self.assertEqual(outside.read_bytes(), b"outside")

    def test_link_rename_and_unlink_reject_unsafe_names(self):
        (self.root / "source").write_bytes(b"content")
        operations = (
            lambda: DurableIO().link_no_replace_at(
                self.root_fd, "source", self.root_fd, "../destination"
            ),
            lambda: DurableIO().rename_fsync_both_at(
                self.root_fd, "../source", self.root_fd, "destination"
            ),
            lambda: DurableIO().unlink_fsync_parent_at(self.root_fd, "../source"),
        )
        for operation in operations:
            with self.assertRaisesRegex(ValueError, r"^unsafe path component$"):
                operation()

    def test_mutating_operations_close_owned_descriptors_on_injected_crash(self):
        source = self.root / "source"
        destination = self.root / "destination"
        source.mkdir()
        destination.mkdir()
        source_fd = self.open_directory(source)
        destination_fd = self.open_directory(destination)
        real_open = os.open

        cases = (
            (
                "hard-link-after",
                "link-source",
                lambda io: io.link_no_replace_at(
                    source_fd, "link-source", destination_fd, "link-destination"
                ),
            ),
            (
                "rename-after",
                "rename-source",
                lambda io: io.rename_fsync_both_at(
                    source_fd, "rename-source", destination_fd, "rename-destination"
                ),
            ),
            (
                "unlink-after",
                "unlink-source",
                lambda io: io.unlink_fsync_parent_at(source_fd, "unlink-source"),
            ),
        )
        for site, name, operation in cases:
            with self.subTest(site=site):
                (source / name).write_bytes(b"content")
                opened = []

                def recording_open(*args, **kwargs):
                    descriptor = real_open(*args, **kwargs)
                    opened.append(descriptor)
                    return descriptor

                controller = FailpointController(site, 1)
                with mock.patch("github_durable_io.os.open", side_effect=recording_open):
                    with self.assertRaises(InjectedCrash):
                        operation(DurableIO(controller))

                self.assertEqual(len(opened), 1)
                with self.assertRaises(OSError):
                    os.fstat(opened[0])


class DurableIOCrashMatrixTests(unittest.TestCase):
    def open_descriptor_count(self):
        for directory in ("/proc/self/fd", "/dev/fd"):
            try:
                return len(os.listdir(directory))
            except OSError:
                continue
        self.skipTest("open descriptor inventory is unavailable")

    def run_workflow(self, root, controller):
        real_write = os.write
        real_fsync = os.fsync
        write_calls = 0
        regular_fsync_interrupted = False

        def interrupted_short_write(descriptor, content):
            nonlocal write_calls
            write_calls += 1
            if write_calls == 1:
                raise InterruptedError(errno.EINTR, "deterministic write interruption")
            if write_calls == 2:
                return real_write(descriptor, content[:2])
            return real_write(descriptor, content)

        def interrupted_file_fsync(descriptor):
            nonlocal regular_fsync_interrupted
            if (
                stat.S_ISREG(os.fstat(descriptor).st_mode)
                and not regular_fsync_interrupted
            ):
                regular_fsync_interrupted = True
                raise InterruptedError(errno.EINTR, "deterministic fsync interruption")
            return real_fsync(descriptor)

        with mock.patch(
            "github_durable_io.os.write", side_effect=interrupted_short_write
        ):
            with mock.patch(
                "github_durable_io.os.fsync", side_effect=interrupted_file_fsync
            ):
                root_fd = os.open(
                    str(root), os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
                )
                stage_fd = None
                published_fd = None
                try:
                    io = DurableIO(controller)
                    stage_fd = io.bootstrap_directory_at(
                        root_fd,
                        ("transactions", "transaction-1", "staged-artifacts"),
                    )
                    io.write_fsync_at(stage_fd, "ZERO", b"")
                    io.write_fsync_at(stage_fd, "event.staged", b"event")
                    io.fsync_directory(stage_fd, "source-parent-fsync")
                    published_fd = io.bootstrap_directory_at(root_fd, ("published",))
                    io.link_no_replace_at(
                        stage_fd, "event.staged", published_fd, "event.json"
                    )
                    io.fsync_directory(published_fd, "destination-parent-fsync")
                    io.unlink_fsync_parent_at(stage_fd, "event.staged")
                    io.write_fsync_at(stage_fd, "index.next", b"after")
                    io.fsync_directory(stage_fd, "source-parent-fsync")
                    io.rename_fsync_both_at(
                        stage_fd, "index.next", root_fd, "index.json"
                    )
                finally:
                    # Simulate process descriptor teardown only. No crashed
                    # namespace is cleaned or recovered before fresh reopen.
                    if published_fd is not None:
                        os.close(published_fd)
                    if stage_fd is not None:
                        os.close(stage_fd)
                    os.close(root_fd)

    def reopen_state(self, root):
        initial_fd = os.open(
            str(root), os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
        )
        root_fd = DurableIO().bootstrap_directory_at(initial_fd, ())
        os.close(initial_fd)
        descriptors = [root_fd]

        def directory(parent_fd, name):
            try:
                descriptor = os.open(
                    name,
                    os.O_RDONLY
                    | getattr(os, "O_DIRECTORY", 0)
                    | getattr(os, "O_NOFOLLOW", 0),
                    dir_fd=parent_fd,
                )
            except FileNotFoundError:
                return None
            descriptors.append(descriptor)
            self.assertTrue(stat.S_ISDIR(os.fstat(descriptor).st_mode))
            return descriptor

        def regular(parent_fd, name):
            if parent_fd is None:
                return None
            try:
                descriptor = os.open(
                    name,
                    os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0),
                    dir_fd=parent_fd,
                )
            except FileNotFoundError:
                return None
            try:
                observed = os.fstat(descriptor)
                self.assertTrue(stat.S_ISREG(observed.st_mode))
                chunks = []
                while True:
                    chunk = os.read(descriptor, 4096)
                    if not chunk:
                        break
                    chunks.append(chunk)
                return (b"".join(chunks), observed.st_dev, observed.st_ino)
            finally:
                os.close(descriptor)

        try:
            transactions_fd = directory(root_fd, "transactions")
            transaction_fd = (
                directory(transactions_fd, "transaction-1")
                if transactions_fd is not None
                else None
            )
            stage_fd = (
                directory(transaction_fd, "staged-artifacts")
                if transaction_fd is not None
                else None
            )
            published_fd = directory(root_fd, "published")
            return {
                "transactions": transactions_fd is not None,
                "transaction": transaction_fd is not None,
                "stage": stage_fd is not None,
                "published": published_fd is not None,
                "zero": regular(stage_fd, "ZERO"),
                "event_source": regular(stage_fd, "event.staged"),
                "event_destination": regular(published_fd, "event.json"),
                "index_source": regular(stage_fd, "index.next"),
                "index_destination": regular(root_fd, "index.json"),
            }
        finally:
            for descriptor in reversed(descriptors):
                os.close(descriptor)

    def project_state(self, state):
        if not state["transactions"]:
            depth = 0
        elif not state["transaction"]:
            depth = 1
        elif not state["stage"]:
            depth = 2
        else:
            depth = 3

        event_source = state["event_source"]
        event_destination = state["event_destination"]
        if event_source is None and event_destination is None:
            relation = "absent"
        elif event_source is not None and event_destination is None:
            relation = "source-only"
        elif event_source is None and event_destination is not None:
            relation = "destination-only"
        elif event_source[1:] == event_destination[1:]:
            relation = "same-inode"
        else:
            relation = "different-inode"

        def content(record):
            return None if record is None else record[0]

        return (
            depth,
            state["published"],
            content(state["zero"]),
            content(event_source),
            content(event_destination),
            relation,
            content(state["index_source"]),
            content(state["index_destination"]),
        )

    def assert_global_invariants(self, state):
        self.assertFalse(state["transaction"] and not state["transactions"])
        self.assertFalse(state["stage"] and not state["transaction"])
        if state["published"]:
            self.assertTrue(state["stage"])
        if state["zero"] is not None:
            self.assertEqual(state["zero"][0], b"")

        event_source = state["event_source"]
        event_destination = state["event_destination"]
        if event_source is not None:
            self.assertIn(event_source[0], (b"", b"ev", b"event"))
        if event_destination is not None:
            self.assertEqual(event_destination[0], b"event")
        if event_source is not None and event_destination is not None:
            self.assertEqual(event_source[1:], event_destination[1:])
        if event_destination is not None:
            self.assertIsNotNone(state["zero"])

        index_source = state["index_source"]
        index_destination = state["index_destination"]
        self.assertIsNotNone(index_destination)
        self.assertIn(index_destination[0], (b"before", b"after"))
        if index_source is not None:
            self.assertIn(index_source[0], (b"", b"after"))
            self.assertEqual(index_destination[0], b"before")
        if index_destination[0] == b"after":
            self.assertIsNone(index_source)

        if index_source is not None or index_destination[0] == b"after":
            self.assertIsNotNone(event_destination)
            self.assertIsNone(event_source)

    def expected_trace(self):
        return (
            ("namespace-mkdir-before", 1),
            ("namespace-mkdir-after", 1),
            ("namespace-parent-fsync-before", 1),
            ("namespace-parent-fsync-after", 1),
            ("namespace-mkdir-before", 2),
            ("namespace-mkdir-after", 2),
            ("namespace-parent-fsync-before", 2),
            ("namespace-parent-fsync-after", 2),
            ("namespace-mkdir-before", 3),
            ("namespace-mkdir-after", 3),
            ("namespace-parent-fsync-before", 3),
            ("namespace-parent-fsync-after", 3),
            ("file-create-before", 1),
            ("file-create-after", 1),
            ("file-fsync-before", 1),
            ("file-fsync-before", 2),
            ("file-fsync-after", 1),
            ("file-create-before", 2),
            ("file-create-after", 2),
            ("file-write-before", 1),
            ("file-write-before", 2),
            ("file-write-after", 1),
            ("file-write-before", 3),
            ("file-write-after", 2),
            ("file-fsync-before", 3),
            ("file-fsync-after", 2),
            ("source-parent-fsync-before", 1),
            ("source-parent-fsync-after", 1),
            ("namespace-mkdir-before", 4),
            ("namespace-mkdir-after", 4),
            ("namespace-parent-fsync-before", 4),
            ("namespace-parent-fsync-after", 4),
            ("hard-link-before", 1),
            ("hard-link-after", 1),
            ("destination-parent-fsync-before", 1),
            ("destination-parent-fsync-after", 1),
            ("unlink-before", 1),
            ("unlink-after", 1),
            ("source-parent-fsync-before", 2),
            ("source-parent-fsync-after", 2),
            ("file-create-before", 3),
            ("file-create-after", 3),
            ("file-write-before", 4),
            ("file-write-after", 3),
            ("file-fsync-before", 4),
            ("file-fsync-after", 3),
            ("source-parent-fsync-before", 3),
            ("source-parent-fsync-after", 3),
            ("rename-before", 1),
            ("rename-after", 1),
            ("destination-parent-fsync-before", 2),
            ("destination-parent-fsync-after", 2),
            ("source-parent-fsync-before", 4),
            ("source-parent-fsync-after", 4),
        )

    def allowed_pre_post_states(self, expected_trace):
        fields = (
            "depth",
            "published",
            "zero",
            "event_source",
            "event_destination",
            "event_relation",
            "index_source",
            "index_destination",
        )
        state = {
            "depth": 0,
            "published": False,
            "zero": None,
            "event_source": None,
            "event_destination": None,
            "event_relation": "absent",
            "index_source": None,
            "index_destination": b"before",
        }
        transitions = {
            ("namespace-mkdir-after", 1): {"depth": 1},
            ("namespace-mkdir-after", 2): {"depth": 2},
            ("namespace-mkdir-after", 3): {"depth": 3},
            ("file-create-after", 1): {"zero": b""},
            ("file-create-after", 2): {
                "event_source": b"",
                "event_relation": "source-only",
            },
            ("file-write-after", 1): {"event_source": b"ev"},
            ("file-write-after", 2): {"event_source": b"event"},
            ("namespace-mkdir-after", 4): {"published": True},
            ("hard-link-after", 1): {
                "event_destination": b"event",
                "event_relation": "same-inode",
            },
            ("unlink-after", 1): {
                "event_source": None,
                "event_relation": "destination-only",
            },
            ("file-create-after", 3): {"index_source": b""},
            ("file-write-after", 3): {"index_source": b"after"},
            ("rename-after", 1): {
                "index_source": None,
                "index_destination": b"after",
            },
        }
        allowed = {}
        for target in expected_trace:
            state.update(transitions.get(target, {}))
            allowed[target] = (tuple(state[field] for field in fields),)
        return allowed

    def test_baseline_trace_and_every_independent_crash_reopen_safely(self):
        expected_trace = self.expected_trace()
        allowed_states = self.allowed_pre_post_states(expected_trace)
        self.assertEqual(set(allowed_states), set(expected_trace))

        with tempfile.TemporaryDirectory() as baseline_name:
            baseline_root = Path(baseline_name)
            (baseline_root / "index.json").write_bytes(b"before")
            baseline = FailpointController()
            self.run_workflow(baseline_root, baseline)
            self.assertEqual(baseline.trace, expected_trace)
            final_state = self.reopen_state(baseline_root)
            self.assert_global_invariants(final_state)
            self.assertEqual(final_state["zero"][0], b"")
            self.assertEqual(final_state["event_destination"][0], b"event")
            self.assertIsNone(final_state["event_source"])
            self.assertEqual(final_state["index_destination"][0], b"after")
            self.assertIsNone(final_state["index_source"])

        for position, target in enumerate(expected_trace):
            site, occurrence = target
            with self.subTest(site=site, occurrence=occurrence):
                with tempfile.TemporaryDirectory() as crash_name:
                    crash_root = Path(crash_name)
                    (crash_root / "index.json").write_bytes(b"before")
                    descriptors_before = self.open_descriptor_count()
                    controller = FailpointController(site, occurrence)
                    with self.assertRaises(InjectedCrash) as raised:
                        self.run_workflow(crash_root, controller)
                    self.assertEqual(
                        (raised.exception.site, raised.exception.occurrence),
                        target,
                    )
                    self.assertEqual(
                        controller.trace, expected_trace[: position + 1]
                    )
                    del controller
                    reopened = self.reopen_state(crash_root)
                    self.assert_global_invariants(reopened)
                    self.assertIn(
                        self.project_state(reopened), allowed_states[target]
                    )
                    self.assertEqual(
                        self.open_descriptor_count(), descriptors_before
                    )


if __name__ == "__main__":
    unittest.main()
