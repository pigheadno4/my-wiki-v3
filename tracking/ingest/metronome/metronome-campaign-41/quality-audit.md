# Campaign 41 final retrieval audit

Final verdict: **PASS — 10/10 predetermined questions**. Zero retrieval failures, wrong-object answers or query-driven source repairs.

| Group | Object/action scope | Result | Evidence |
| --- | --- | --- | --- |
| A | Legacy grant list, credit edit, offset configuration edit | 6/6 pass | [Group A](query-audit-group-a.md) |
| B | Prepaid commit shortening, entity custom-field value setting | 4/4 pass | [Group B](query-audit-group-b.md) |

Each query used real root index → provider index → purpose-fit concept → source → exact raw navigation, with explicit object/action matching before the verdict. Detail questions used complete selected raw reads and the existing gap sweep. Group B additionally read the custom-fields overview and the two deletion references for action-boundary disambiguation; it distinguished overview wording and applicability tensions from the dedicated endpoint schema without requiring source expansion.

All required reciprocal routes were unique within their intended sections. The coordinator checked requested-versus-reached object/action and accepted both reports without a third full-content review. The single worker retry repaired receipt quote line locators only; source and shared content were unchanged and the retry was not a query-audit failure.

Final mechanical verification passed: five approved source/candidate/receipt matches, pinned hashes and raw provenance, six approved reciprocal concept updates, unique catalogs, 11 typed wiki files, provider-index links and capsule/count consistency. See [retrospective](retrospective.md) for overlapping stage timings and limitations.
