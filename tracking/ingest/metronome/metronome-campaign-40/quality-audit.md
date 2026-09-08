# Campaign 40 final retrieval audit

Final verdict: **PASS — 10/10 predetermined questions**, after correcting one auditor wrong-object error. Zero source retrieval failures, zero source or concept repairs required by the query audit.

| Group | Scope | Final result | Evidence |
| --- | --- | --- | --- |
| A | Rate-card rates, commit archival, threshold notifications; six questions | 6/6 pass | [Group A report](query-audit-group-a.md) |
| B | Legacy Plan customers and Avalara credentials; four questions | 4/4 pass | [Group B report](query-audit-group-b.md) |

Both auditors used actual root index → provider index → concept → source → exact raw navigation, with complete selected-raw reads for detail questions and the existing gap sweep. Two additional needed raw authorities were read: contract-specific rate schedule for the override branch, and account-level billing-provider enumeration for delivery-method IDs. No broad new source audit was added.

The initial Group A Q3/Q4 incorrectly selected credit archival instead of the assigned commit archival. The coordinator invalidated those two verdicts and requested only their correction. Corrected evidence uses the exact commit source/raw, including finalized usage and commit-payment invoice prerequisites. Four other valid answers were preserved without reread. The error was in audit execution, not the source, and must not be hidden in the final pass count.

All five final sources remain the independently approved candidates. One final mechanical check verified exact raw hashes/provenance, all nine approved concept updates and reciprocal routes, unique company/provider catalog entries, thirteen typed wiki files, provider-index links, capsule consistency and reconciled counts. See [retrospective](retrospective.md) for stage timings and limitations.
