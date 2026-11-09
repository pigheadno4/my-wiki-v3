# Adyen Web Serial Delta Ingest Review - 2026-11-08

## Authorization

User explicitly approved delta ingestion of 6.48.0, then 6.48.1, with focused reading, exact-SHA supplements and preservation of all history. Each item must complete its entire ingest/validation cycle before the next is claimed. No additional collection, runtime/build/test/payment operation, commit or push is authorized.

Focused reading fully covers changed retained authored source, supplements, affected prior/dependency context, release evidence and complete cumulative source/changelog. Generated inventories, unchanged historical evidence and duplicated diffs are mechanically verified. This does not claim a complete upstream-tree read or audit of excluded/hosted implementations.

## 6.48.0 - `github-7af6b1df429e8b0d75bf`

- SHA `a05c1184195fa73ce7dc9e956fa080cb40638209`, from 6.47.0, published 2026-10-28. Approved/claimed in delta mode, separately from 6.48.1.
- Standard capsule 222 files: 10 modified, 212 unchanged, no additions/removals. Five-file supplement `2026-11-08-a05c118-97e12dcc` (70,075 bytes) is linked through the canonical attachment. Effective assignment: 26 paths / 587,140 bytes.
- All 444 current/prior snapshot sizes, SHA-256 and Git blob identities pass; five supplemental identities and packet/attachment/comparison hashes validated. All 75 upstream changes have policy dispositions: 10 retained and 65 intentional exclusions; no gaps/unclassified changes.
- Complete changed source and five supplemental files read during collection review/ingest, with hashes revalidated. Read affected prior Core/3DS2 and comparison contexts plus the current complete Session dependency. Session already stores refreshed blobs; the new callback is not first-time persistence support. Excluded message-helper/hosted runtime internals remain outside scope.

### Grounding Gate

1. Current snapshot `packages/lib/src/types/global-types.ts:247`: `sessionData?: string;` in `OrderUpdatedData`.
2. Current snapshot `packages/lib/src/components/ThreeDS2/components/utils.ts:192`: `return !base?.isConnected;`
3. Supplement `packages/lib/src/components/internal/UIElement/UIElement.tsx:483`: `this.props.onOrderUpdated?.({ order, ...(session?.data && { sessionData: session.data }) });`
4. Supplement `packages/lib/src/components/ApplePay/services/ApplePayService.ts:141`: `console.warn('ApplePayService: onpaymentauthorized session.completePayment() failed', error);`
5. Supplement `packages/lib/src/components/internal/SecuredFields/lib/constants.ts:18`: `export const SF_VERSION = '6.4.0';`

### Workflow Checklist

- [x] 1. Focused reading, identities, required list and located grounding excerpts.
- [x] 2. Concept audit: updated existing online-payments, review-page checkout and 3D Secure concepts before source edits; no new concept needed.
- [x] 3. Cumulative source/changelog with all older history retained.
- [x] 4. Company summary; source_count unchanged at 3206, repository-release count 32 (reconcile at close).
- [x] 5. Durable concept and reciprocal-citation completion.
- [x] 6. No substantive cross-company comparison; no new comparison page.
- [x] 7. Version-scope check: distinct callback refresh paths and historical ADR contradiction preserved; no first-persistence, hosted-enforcement or universal wallet-error-safety claim.
- [x] 8. Provider index; root cross-provider index unchanged.
- [x] 9. Provider/root logs; unrelated work preserved.
- [x] 10. Seven typed pages pass; scoped whitespace, local evidence links, unique catalog, 3206 source / 32 release counts and full historical-body/raw-list preservation checks pass. Item completed as ingested/delta before any 6.48.1 claim.

## 6.48.1 - `github-63a67800194fcf63cd6f`

Approved and claimed only after 6.48.0 reached ingested. SHA `6ccc03f83b064c2171bc836edd9b35444e582823`, from 6.48.0, published 2026-11-05. Delta effective assignment now 14 paths / 353,098 bytes, reflecting the newly cumulative wiki context. Standard capsule 222 files: two modified manifests / 220 unchanged. One-file supplement `2026-11-08-6ccc03f-543c5280` retains constants.ts (3,424 bytes). All 444 current/prior snapshot identities and supplemental/attachment checks pass.

Both complete changed package manifests, release notes, the complete constants supplement and affected prior package/constants context read. Cumulative history just read/updated in the preceding cycle remains intact and is checked for exact preservation; generated inventories and duplicated/excluded comparison material checked mechanically under the approved focus exception. All 81 upstream changes have dispositions: two retained and 79 intentional exclusions, with no gaps/unclassified changes. This is not a semantic read of IRIS/UPI or a hosted-runtime audit.

### Grounding Gate

1. Current snapshot `packages/lib/package.json:3`: `"version": "6.48.1",`
2. Current snapshot `packages/lib/package.json:142`: `"@paypal/paypal-js": "11.2.1",`
3. Supplement `packages/lib/src/components/internal/SecuredFields/lib/constants.ts:18`: `export const SF_VERSION = '6.4.1';`
4. Release notes line 3: "Improved: Display only the bank list for IRIS on mobile, without the QR code option."
5. Release notes line 9: "Fixed: new securedFields url validation also allows checkoutshopper-beta environments"

### Workflow Checklist

- [x] 1. Focused reading, identities, effective list and grounding excerpts.
- [x] 2. Existing online-payments concept updated before source; no new topic/concept, no new 3DS/review lifecycle facts in the retained 6.48.1 delta.
- [x] 3. Source/changelog additive delta; all 6.48.0 and earlier release sections retained.
- [x] 4. Company/counts: source_count unchanged at 3206; repository-release count 33, verify at close.
- [x] 5. Concept/citation completion; earlier 3DS/review concept findings retained.
- [x] 6. No substantive cross-company comparison; no new comparison page.
- [x] 7. Scope check: announcement-only IRIS/UPI/hosted implementation clearly distinguished from package/constants evidence; no new contradiction, old warning/ADR history preserved.
- [x] 8. Provider index only; unrelated root index left untouched.
- [x] 9. Provider/root logs, preserving other work.
- [x] 10. Seven typed pages pass; history/raw-list/link/catalog/count and whitespace checks pass; item completed as ingested/delta after the independently completed 6.48.0 cycle.

## Final Validation and Outcome

- Both work items are ingested in delta mode, in the approved 6.48.0 -> 6.48.1 sequence. No pending ingest items remain. Collector-generated index accepts `@adyen/adyen-web@6.48.1`, action wait, next due 2026-11-15.
- All 672 distinct prior/current snapshot and supplemental files pass size, SHA-256 and Git blob identity checks. Both canonical attachments and effective reading lists validate; original packets/accepted raw/registry remain unchanged. Release-note and comparison/packet hashes pass.
- Seven typed pages pass `validate_wiki.py` after each cycle. The existing untyped provider index/root log are checked separately for catalog/links/whitespace rather than mixing a schema migration into this ingest. Provider source/changelog entries remain unique.
- Complete pre-existing source release-body history and changelog chronology are preserved, including the 6.45.1 warning and ADR/code discrepancy. Every older raw frontmatter reference remains in its original order after the six new manifest entries. The 6.48.0 section is retained after adding 6.48.1. Exact evidence links resolve.
- Source_count reconciles to 3206 unchanged source summaries, including 16 cumulative GitHub repository sources. Distinct ingested repository/package release identities reconcile to 33; no new source page or cross-company comparison was created.
- Final offline GitHub validator reports exactly 13 historical unrelated structural errors, none for either item/attachment: six packet-budget rebuild failures, six resulting invalid-packet reports and the existing Adyen PHP package-alias ledger mismatch. Pending count zero. No global all-green claim.
- Scoped whitespace checks pass. No collector/validator code, registry, rules or upstream tests changed; full unit suite not rerun for documentation/tracking-only work. No extra collection, install/build, browser/issuer/device/compliance/payment execution, commit or push. Unrelated checkout edits remain preserved.

Next step: request a scoped commit and push for the approved collection/supplement/ingest work. Publication remains a separate user approval gate.
