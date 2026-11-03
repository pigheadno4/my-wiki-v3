# Checkout Components exact-ref ingest review

- Work item: `github-7eb03c30a9c79e1870cd`.
- Ingest date: 2026-11-03 (Asia/Shanghai).
- Approved mode: full additive, with explicit focused-reading exception.
- Boundary: `294b50a11d61ccb458877776e5ba8d481781014b` to `dcd6abfc340371666a0428d7292a2cab32c2bbca`.
- Current identity: `default-branch@dcd6abf`, not a package release.
- Accepted release identity remains `@paypal/checkout-components@5.0.438`.

## Reading and grounding

Complete cumulative wiki source and changelog read, including all older release
sections, warnings and evidence links. All 16 changed retained files read fully
(5,914 lines): helper, lib export, 13 component files and Vitest configuration.
Affected prior source read with surrounding context; complete comparison read.
Current package metadata read and verified byte-identical. Relevant company,
provider catalog/log and root-log sections read. Existing Checkout concept read
fully and audited before canonical edits. No new concept or cross-company
comparison warranted; this is internal runtime knowledge for an existing topic.

User-approved mechanical checks cover unchanged retained files, generated
manifests/inventories, historical changelog/generated evidence and duplicated
comparison content. This is not a whole-repository or complete semantic read of
the 439-path full packet. External SDK-client/logger and Zoid implementations,
hosted child event emitters and server-side masking remain unverified.

Five verbatim excerpts extracted before edits, all from
`raw/github/paypal/paypal-checkout-components/snapshots/2026-11-02-dcd6abf/files/src/lib/fpti-ip-masking.js`:

1. Line 32: `getLogger().addMetaBuilder(() => (hasInteracted ? {} : { maskIP: true }));`
2. Line 43: `  if (hasInteracted || isFlushing) {`
3. Line 49: `    .immediateFlush()`
4. Line 51: `      hasInteracted = true;`
5. Line 56: `            instance.updateProps({ hasInteracted: true }).catch(() => {`

## Evidence verification

- Both snapshot inventories: 214 files each, all 428 file sizes, SHA-256 values
  and Git blob IDs verified. Current total: 665,938 bytes.
- 198 common files verified byte-equal; 14 modified retained files, two newly
  retained paths. The helper is upstream-added; Vitest configuration was
  previously outside the capsule, not newly introduced upstream.
- Prior `CHANGELOG.md` and `dist/button.js` remain in immutable prior evidence;
  their omission now is selection scope, not an upstream deletion.
- All 26 upstream file changes disposed: 16 retained, 10 excluded tests.
- Comparison JSON identifies exact from/to SHAs; patch/Markdown hashes verified.
- Full packet rebuilt identically from retained evidence; packet Markdown hash
  verified; 439 paths, no evidence gaps or unclassified changes.
- Budget: 450 files / 4,500,000 bytes; previous policy hash registered to preserve
  historical packet rebuilds. No raw snapshot or release record rewritten.

## Findings and limits

Metadata builder initially returns `{ maskIP: true }`, later `{}`. Notification
sets a flushing guard and waits for external `immediateFlush()` fulfillment
before changing module-local interaction state and relaying it to live instances
of 13 registered factories. No local order/session reset is present. Buttons,
Card Fields and Saved Payment Methods supply the notification callback; Card
Fields child props derive the parent interaction value.

Instance update rejection and per-factory exceptions are isolated without retry.
The flush has no local catch/reset; a rejection would prevent this fulfillment
path and leave the guard set. External promise rejection/recovery behavior is
unverified, so this is a conditional source limitation, not a reproduced bug.
The metadata flag itself does not anonymize an IP or establish server behavior,
consent compliance, complete interaction detection, delivery or hosted rollout.

Vitest switches to a one-to-four-worker fork pool; its memory rationale is an
upstream comment, not a measured result here. No net fallback-transport feature
is present in the comparison. Package version/dependencies and retained public
interface files are unchanged. Internal props/helper exports do change, but no
new merchant payment method, React integration, saved-method editing flow or
documented merchant migration is established. Independent repository histories
remain separate.

## Output scope

Checkout concept first; cumulative source/changelog, company, provider index and
provider/root logs updated additively. All older source/changelog body lines and
raw references must remain; company source_count stays 177. Existing documented
contradictions remain unchanged. No upstream build/test, browser, privacy/network
or payment execution. No commit/push in this approval.

## Ingest checklist and scoped validation

- [x] Focused source/prior-code reading and five grounding excerpts.
- [x] Existing-concept audit; Checkout concept updated before source promotion.
- [x] Additive source summary with newest raw-manifest reference.
- [x] Company update; source_count remains 177.
- [x] Concept linkage and version-qualified evidence limits.
- [x] Cross-company comparison assessed; not warranted.
- [x] Contradiction check; prior warnings retained, new masking limits reciprocal.
- [x] Provider catalog updated once per source/changelog, no duplicate entries.
- [x] Provider and root log entries added; unrelated work preserved.
- [x] Four touched typed pages pass `validate_wiki.py`; whitespace checks pass.

History preservation verified against HEAD: all 459 prior source-body lines and
344 prior changelog-body lines retained without deletion/replacement. Both
15-entry historical raw lists remain in order behind the new manifest. Local
source/changelog evidence links resolve; all five quote locations match exactly.
Work item completed as `ingested`, approved mode full, with zero pending queue
items. Generated index preserves the accepted `5.0.438` release and returns to
`wait`. No automatic next collection/ingest or publication was started.

Post-completion `validate_github_collection.py` reports zero pending items and
only the same 13 historical unrelated structural errors: six older packet-byte
budget rebuild failures, their six invalid-packet consequences, and the existing
Adyen PHP 30.1.0 changelog omission. No Checkout Components errors. No full unit
suite rerun for this documentation-only ingest; the preceding collector/budget
change's test results remain separately reported, not a fresh claim here.

## Publication preflight (2026-11-03)

User separately approved commit/push and an inventory refresh. Fresh full unit
suite: 820 tests, 816 pass and four unchanged registry-expectation failures:
Adyen Postman packet count, Braintree GraphQL packet count, PayPal Messages iOS
v2 track and Metronome Terraform on-demand cadence. Four typed wiki pages pass;
scoped whitespace passes. Cleared only the recovered packet error through the
generated-index API; the last online check remains November 2. Day-rollover due
actions in the generated November 3 index do not mean new collection/ingestion.
Isolated staging excludes unrelated Adyen/BYD work and includes only this
checkpoint's root-log entry and two provider-catalog rows from shared files.
