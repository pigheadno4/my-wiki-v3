"""Append-only state events and deterministic GitHub collection dashboards."""

from collections import Counter
import json
from pathlib import Path
from typing import Dict, Mapping, Sequence, Tuple

from github_packets import PacketRecord
from github_registry import RepoConfig


COLLECTION_TERMINAL = {
    "unchanged",
    "collected-baseline",
    "collected-change",
    "retry-pending",
    "failed",
}
PACKET_TRANSITIONS = {
    "awaiting-review": {"approved", "rejected"},
    "approved": {"ingesting", "rejected"},
    "ingesting": {"ingested", "validation-failed"},
    "validation-failed": {"approved", "rejected"},
    "ingested": set(),
    "rejected": set(),
}


class StateTransitionError(ValueError):
    """A packet lifecycle request is not allowed by the public state machine."""


class CollectionReconciliationError(ValueError):
    """A selected repository/ref does not have exactly one terminal event."""


def append_event(path: Path, event: Mapping[str, object]) -> None:
    """Append one deterministic JSON object without replacing existing history."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(dict(event), sort_keys=True) + "\n")


def validate_collection_run(events: Sequence[Mapping[str, object]]) -> int:
    """Require exactly one terminal event for every selected repository/ref."""
    selected = []
    terminals: Dict[Tuple[str, str], int] = Counter()
    for event in events:
        key = _collection_key(event)
        if event.get("selected") is True:
            selected.append(key)
        if event.get("state") in COLLECTION_TERMINAL:
            terminals[key] += 1

    for key in selected:
        count = terminals.get(key, 0)
        if count != 1:
            raise CollectionReconciliationError(
                key[0] + " " + key[1] + " must have exactly one terminal event; found " + str(count)
            )
    return len(selected)


def transition_packet(current: str, requested: str) -> str:
    """Validate and return one explicit packet lifecycle transition."""
    if current not in PACKET_TRANSITIONS or requested not in PACKET_TRANSITIONS[current]:
        raise StateTransitionError(
            "invalid packet state transition from " + str(current) + " to " + str(requested)
        )
    return requested


def validate_packet_history(
    packet_id: str,
    initial_state: str,
    events: Sequence[Mapping[str, object]],
) -> str:
    """Validate one complete packet history and return its current state."""
    if initial_state != "awaiting-review":
        raise StateTransitionError("packet initial state must be awaiting-review")
    if not events:
        raise StateTransitionError("packet has no initial state event")
    if dict(events[0]) != {"packet_id": packet_id, "state": "awaiting-review"}:
        raise StateTransitionError("packet initial state event is invalid")

    current = initial_state
    for event in events[1:]:
        if set(event) != {"from_state", "packet_id", "state"}:
            raise StateTransitionError("packet transition event has an invalid shape")
        if (
            type(event.get("from_state")) is not str
            or type(event.get("packet_id")) is not str
            or type(event.get("state")) is not str
            or event["packet_id"] != packet_id
            or event["from_state"] != current
        ):
            raise StateTransitionError("packet transition event does not match its history")
        current = transition_packet(current, str(event["state"]))
    return current


def packet_state_key(repo_id: str, packet_id: str) -> str:
    """Return a collision-free string key for one repository-local packet ID."""
    return json.dumps((repo_id, packet_id), separators=(",", ":"))


def render_collection_status(
    repos: Sequence[RepoConfig], events: Sequence[Mapping[str, object]]
) -> str:
    """Render the latest collection state for every registered repository."""
    latest: Dict[str, Mapping[str, object]] = {}
    for event in events:
        repo_id = event.get("repo_id")
        if isinstance(repo_id, str) and event.get("state") in COLLECTION_TERMINAL:
            latest[repo_id] = event

    lines = [
        "# GitHub Collection Status",
        "",
        "| Company | Repository | Enabled | Priority | Track | Latest ref | Latest version | State | Error |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for repo in repos:
        event = latest.get(repo.id, {})
        lines.append(
            "| "
            + " | ".join(
                _markdown_cell(value)
                for value in (
                    repo.company,
                    repo.id,
                    "yes" if repo.enabled else "no",
                    repo.priority,
                    repo.track,
                    event.get("ref_name") or event.get("selector") or "-",
                    event.get("version") or "-",
                    event.get("state") or "not-collected",
                    event.get("error") or "-",
                )
            )
            + " |"
        )

    counts = Counter(str(event.get("state")) for event in latest.values())
    lines.extend(["", "## Latest terminal states", "", "| State | Count |", "| --- | ---: |"])
    if counts:
        lines.extend("| " + state + " | " + str(counts[state]) + " |" for state in sorted(counts))
    else:
        lines.append("| not-collected | " + str(len(repos)) + " |")
    return "\n".join(lines).rstrip() + "\n"


def render_ingest_status(
    packets: Sequence[PacketRecord], states: Mapping[str, str]
) -> str:
    """Render one row per immutable packet contract using its latest valid state."""
    lines = [
        "# GitHub Ingest Status",
        "",
        "| Repository | Packet | Type | From snapshot | To snapshot | State |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for packet in sorted(packets, key=lambda item: (item.repo_id, item.packet_id)):
        lines.append(
            "| "
            + " | ".join(
                _markdown_cell(value)
                for value in (
                    packet.repo_id,
                    packet.packet_id,
                    packet.packet_type,
                    packet.from_snapshot or "-",
                    packet.to_snapshot,
                    states.get(
                        packet_state_key(packet.repo_id, packet.packet_id),
                        packet.initial_state,
                    ),
                )
            )
            + " |"
        )
    if not packets:
        lines.append("| - | - | - | - | - | no-packets |")
    return "\n".join(lines).rstrip() + "\n"


def _collection_key(event: Mapping[str, object]) -> Tuple[str, str]:
    repo_id = event.get("repo_id")
    selector = event.get("selector", event.get("ref"))
    if not isinstance(repo_id, str) or not repo_id:
        raise CollectionReconciliationError("collection event has no repository identity")
    if not isinstance(selector, str) or not selector:
        raise CollectionReconciliationError("collection event for " + repo_id + " has no ref selector")
    return repo_id, selector


def _markdown_cell(value: object) -> str:
    return str(value).replace("\\", "\\\\").replace("|", "\\|").replace("\n", "<br>")
