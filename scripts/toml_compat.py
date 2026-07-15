"""Python 3.9-compatible TOML loading for local configuration files."""

import json
from pathlib import Path
from typing import Dict, List, Set


def load_toml(path: Path) -> Dict[str, object]:
    try:
        import tomllib
    except ModuleNotFoundError:
        try:
            import tomli as tomllib
        except ModuleNotFoundError:
            return _load_toml_subset(path)
    with path.open("rb") as handle:
        return tomllib.load(handle)


def _load_toml_subset(path: Path) -> Dict[str, object]:
    """Load the JSON-compatible TOML subset used by the local registries."""
    root: Dict[str, object] = {}
    context: Dict[str, object] = root
    pending: List[str] = []
    pending_line = 0
    bracket_depth = 0
    declared_tables: Set[int] = set()

    for current_line, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = _strip_comment(raw).strip()
        if not line and not pending:
            continue

        if pending:
            pending.append(line)
            bracket_depth += _bracket_delta(line)
            if bracket_depth < 0:
                raise _source_error(path, current_line, "unexpected closing bracket")
            if bracket_depth > 0:
                continue
            line = "\n".join(pending)
            line_number = pending_line
            pending = []
        else:
            line_number = current_line
            if line.startswith("[") and "=" not in line:
                context = _set_table(root, line, path, line_number, declared_tables)
                continue

        if "=" not in line:
            raise _source_error(path, line_number, "expected key = value")
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not key or not value:
            raise _source_error(path, line_number, "expected key = value")

        bracket_depth = _bracket_delta(value)
        if bracket_depth < 0:
            raise _source_error(path, line_number, "unexpected closing bracket")
        if bracket_depth > 0:
            pending = [line]
            pending_line = line_number
            continue
        if key in context:
            raise _source_error(path, line_number, "duplicate key " + key)
        context[key] = _parse_value(value, path, line_number)

    if pending:
        raise _source_error(path, pending_line, "unterminated array")
    return root


def _strip_comment(line: str) -> str:
    in_string = False
    escaped = False
    for index, character in enumerate(line):
        if escaped:
            escaped = False
        elif character == "\\" and in_string:
            escaped = True
        elif character == '"':
            in_string = not in_string
        elif character == "#" and not in_string:
            return line[:index]
    return line


def _bracket_delta(value: str) -> int:
    in_string = False
    escaped = False
    depth = 0
    for character in value:
        if escaped:
            escaped = False
        elif character == "\\" and in_string:
            escaped = True
        elif character == '"':
            in_string = not in_string
        elif not in_string and character == "[":
            depth += 1
        elif not in_string and character == "]":
            depth -= 1
    return depth


def _set_table(
    root: Dict[str, object],
    header: str,
    path: Path,
    line_number: int,
    declared_tables: Set[int],
) -> Dict[str, object]:
    if header.startswith("[["):
        is_array = True
        if not header.endswith("]]"):
            raise _source_error(path, line_number, "malformed table header")
        name = header[2:-2]
    elif header.startswith("["):
        is_array = False
        if not header.endswith("]"):
            raise _source_error(path, line_number, "malformed table header")
        name = header[1:-1]
    else:
        raise _source_error(path, line_number, "malformed table header")
    if "[" in name or "]" in name:
        raise _source_error(path, line_number, "malformed table header")
    keys = [key.strip() for key in name.split(".")]
    if not keys or any(not key for key in keys):
        raise _source_error(path, line_number, "malformed table header")

    context = root
    for key in keys[:-1]:
        current = context.setdefault(key, {})
        if isinstance(current, list):
            if not current or not isinstance(current[-1], dict):
                raise _source_error(path, line_number, "invalid table path")
            context = current[-1]
        elif isinstance(current, dict):
            context = current
        else:
            raise _source_error(path, line_number, "invalid table path")

    final_key = keys[-1]
    if is_array:
        rows = context.setdefault(final_key, [])
        if not isinstance(rows, list):
            raise _source_error(path, line_number, "table conflicts with value")
        row: Dict[str, object] = {}
        rows.append(row)
        return row

    table = context.setdefault(final_key, {})
    if not isinstance(table, dict):
        raise _source_error(path, line_number, "table conflicts with value")
    if id(table) in declared_tables:
        raise _source_error(path, line_number, "duplicate table " + name)
    declared_tables.add(id(table))
    return table


def _parse_value(value: str, path: Path, line_number: int) -> object:
    try:
        return json.loads(_remove_trailing_array_commas(value))
    except json.JSONDecodeError as error:
        raise _source_error(
            path,
            line_number + error.lineno - 1,
            "invalid JSON-compatible value: " + error.msg,
        ) from error


def _remove_trailing_array_commas(value: str) -> str:
    output = []
    in_string = False
    escaped = False
    for index, character in enumerate(value):
        if escaped:
            escaped = False
        elif character == "\\" and in_string:
            escaped = True
        elif character == '"':
            in_string = not in_string
        elif character == "," and not in_string:
            remainder = value[index + 1:].lstrip()
            if remainder.startswith("]"):
                continue
        output.append(character)
    return "".join(output)


def _source_error(path: Path, line_number: int, message: str) -> ValueError:
    return ValueError(str(path) + ": line " + str(line_number) + ": " + message)
