# Braintree C20 close audit

## Outcome

**PASS.** All ten exact-manifest jobs are approved; none is failed or rejected.
Eight first reviews approved. Chargeback Protection and Effortless Chargeback
Protection each needed one bounded correction and targeted re-review on an
unchanged pinned raw. There were 12 worker attempts, ten initial full reviews,
two targeted reviews and one post-promotion concept/index repair.

The five fixed query groups in `query-audit-a.md` through `query-audit-e.md`
passed **20/20** navigation/detail questions with complete pinned-raw reads,
object/action checks, exact locators, bounded gap sweeps and reciprocal routes.
Group E's extra full read of the Premium Fraud Management Tools overview found
a material upstream conflict: its no-bypass statement disagrees with the
Chargeback Protection article's bypass statement. An independent bounded
review confirmed the unresolved warning now in
`wiki/concepts/braintree-chargeback-protection.md`; the provider index exposes
that route. No claim of current bypass support or indemnity direction is made.
The missing Eligible Chargeback Types section remains an evidence gap.

## Mechanical close evidence

- `validate_wiki.py` passed all **21** touched typed pages: ten sources, nine
  concepts (seven new plus Control Panel and Disputes), company and provider
  log. The provider index is a frontmatter-free router.
- All ten promoted sources are byte-equal to their latest independently
  approved `candidate.md`. Pinned raw SHA-256 values, embedded source URLs,
  source frontmatter raw paths and path-qualified `## Raw Sources` links match
  the manifest.
- Every new source has a purpose-fit reciprocal main-concept route. The
  provider index and company page each contain exactly one entry per new
  source. The provider has **171** source pages = **155** website + **16**
  GitHub, matching company `source_count`; changelogs are excluded.
- Scoped `git diff --check` and new-file trailing-whitespace checks found no
  issue. `raw/braintree/` is unchanged. No code, rules, GitHub work items,
  root index or root log were edited by C20.

The campaign monitor and receipts retain per-job evidence. This close records
local wiki promotion only; it does not authorize commit, push or C21.
