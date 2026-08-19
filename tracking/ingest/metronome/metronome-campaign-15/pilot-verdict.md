# Metronome Campaign 15 Pilot Verdict

- Verdict: **retain independent review; retain targeted retry; do not scale or
  promote this campaign**
- Result: **2/3 approved**
- Runtime: **890 seconds (14 minutes 50 seconds)**
- Canonical promotion: **none**

## What the pilot established

The dynamic three-slot workflow completed the three short guides much faster
than earlier ten-page campaigns. Workers finished independently, each completed
worker slot moved directly to a reviewer, and the coordinator performed no
third full-source read or candidate repair.

The narrowed reviewer role was still necessary. On `manage-seats`, deterministic
checks and a Sol worker were insufficient: the independent complete-source
review found a material error about unassigned-seat removal and several concept
signals whose cited quotes did not support their claims. That page was rejected
without a retry because a renewed semantic interpretation would have been needed.

The bounded retry path worked as intended on `guarantee-zero-overages`. Its
first review found the source interpretation materially accurate but the
evidence incomplete. The same worker changed only the requested quote ranges
and USD-scaling links, and the same reviewer approved only that diff with the
raw hash unchanged. A second full-page review was not performed.

## Production decision

Do not remove the independent strong-model reviewer, even for short guide pages.
The coordinator may continue to avoid a default third full-source read and may
derive mechanical company, index, and log entries at campaign close. Reviewers
should continue to focus on source correctness, important omissions,
contradictions, raw links, and the factual validity and completeness of concept
signals rather than polishing final shared-page prose.

Keep targeted diff review for unchanged-hash corrections limited to evidence,
links, frontmatter, formatting, wording, or an already identified field. A
factual error, important omission, or new interpretation still requires a full
review or terminal rejection under the approved campaign gate.

The approved shared-update plan remains evidence only. Because the exact `3/3`
gate failed, do not promote the two approved candidates or their grouped concept
signals, do not repair and promote `manage-seats`, and do not treat this result
as authorization for a larger Metronome or cross-PSP campaign.

## Minimal next decision

No scheduler, schema, registry, monitoring, or provider-rule change is needed.
The next user decision is whether to keep Campaign 15 only as calibration
evidence or authorize a separate, exact manifest using the same independent
review gate. Campaign 15 itself must not be resumed.
