# Braintree Web Drop-in 1.48.0 delta ingest

- Work item: `github-d83a391d04b7021d0ef7`
- Approved mode: delta, inline; no focused-reading exception.
- Boundary: `braintree-web-drop-in@1.47.0` (`ec1c7c533c2e878545f2b25505c56b7e22dc1c17`) to `braintree-web-drop-in@1.48.0` (`5e6de786a463598b4583a657acbd5cafee72dbf9`).

## Checklist

- [x] Read both packet files and all 13 required paths completely, including cumulative history; also read prior payment-method implementation and current sanitizer/template.
- [x] Concept audit and update before source edits.
- [x] Add cumulative source and changelog findings without removing the baseline.
- [x] Update company context; preserve source count for a version-only ingest.
- [x] Check concept citations.
- [x] Assess cross-company comparison need: none, single-repository delta.
- [x] Record contradictions without resolving unsupported lifecycle claims; reciprocal website warning updated without changing its other content.
- [x] Update provider index.
- [x] Update provider and root logs.
- [x] Validate and complete the work item.

## Grounding

Locations below are relative to `raw/github/braintree/braintree-web-drop-in/snapshots/2026-09-20-5e6de78/files/` unless otherwise stated.

1. Release notes: "feat: sanitize `lastFour` card digits" (`raw/github/braintree/braintree-web-drop-in/releases/braintree-web-drop-in/1.48.0/2026-09-20/release-notes.md`).
2. `CHANGELOG.md`, 1.48.0: "fix: tighten `lastFour` innerHtml usage".
3. `CHANGELOG.md`, revised 1.47.0 entry: "fix: stop using innerHtml in favor of textContent (where possible)".
4. `src/views/payment-method-view.js`, card branch: `Number(this.paymentMethod.details.lastFour)` followed by `.toString()`, `.slice(0, 4)`, `.padStart(4, '0')`.
5. Same implementation after the switch: `this.element.innerHTML = html;`.

## Evidence Checks and Boundaries

Both snapshots' 86 file sizes and SHA-256 hashes passed. Packet Markdown, current snapshot manifest, comparison Markdown/patch, and release-note hashes passed. Four retained files changed; 82 are unchanged. All six upstream changes have dispositions, including excluded lockfile and unit-test paths whose changed hunks were read in the comparison. No changed retained path is unclassified; the unchanged LESS classifications do not constitute unclassified changes.

`policy-history-bootstrap` is comparison metadata, not evidence of a newly broadened capsule: both inventories retain the same 86 paths. Packet high priority is not a vulnerability severity rating. No public API or runtime dependency changes are identified. The card label still uses an HTML template; this is neither a universal textContent migration nor a digits-only validator. Do not claim a CVE, exploit, browser verification, or upstream test execution.

Preserve the September repository versus October website lifecycle conflict already recorded by the website task. The September 10 release also follows the unchanged README's September 1 no-updates milestone; it does not prove a support extension. No other repository or raw file is modified by this ingest.

## Verification

- Targeted wiki validation: six schema-bearing pages, no issues.
- GitHub validator: 116 snapshots, 101 release records, 58 comparisons, 115 work items; no structural errors before completion.
- `git diff --check` passed. Provider/root log links and source/changelog evidence paths resolve. The initial ad hoc path check treated line suffixes as filename characters; rerunning with line-qualified citation handling passed.
- Baseline architecture through 1.47.0 findings and the entire original 1.47.0 changelog entry remain verbatim.
- Six standalone Node expression assertions passed for the documented examples. This checks only expression results, not Drop-in rendering or upstream tests.
- CLI completed this work item as ingested. No commit or push performed.
