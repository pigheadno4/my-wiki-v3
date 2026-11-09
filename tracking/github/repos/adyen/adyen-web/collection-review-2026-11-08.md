# Adyen Web Collection Review - 2026-11-08

## Approval Boundary

This initial collection review is followed by the separately approved supplement review at the end of this file. Statements about supplements not yet being collected describe the initial review stage, not the completed follow-up.

User approved rechecking and collection, with findings before ingestion. The existing registry scope and budgets were used unchanged. Both new work items stop at `awaiting_approval`, with no approved mode. No ingest approval/claim, wiki edit, supplement collection, install/build/browser/payment test, commit or push was performed.

The latest canonical wiki ingest remains `@adyen/adyen-web@6.47.0` on 2026-10-19, SHA `6068f43579dfbf50bad7505113b369e4e0d4df54`. Earlier history and the 6.45.1 do-not-use warning remain unchanged.

## Collected Releases

| Package release | Published UTC | Exact SHA | Work item | Retained change counts |
| --- | --- | --- | --- | --- |
| `@adyen/adyen-web@6.48.0` | 2026-10-28T10:26:57Z | `a05c1184195fa73ce7dc9e956fa080cb40638209` | `github-7af6b1df429e8b0d75bf` | 10 modified / 212 unchanged; no added/removed |
| `@adyen/adyen-web@6.48.1` | 2026-11-05T10:51:46Z | `6ccc03f83b064c2171bc836edd9b35444e582823` | `github-63a67800194fcf63cd6f` | 2 modified / 220 unchanged; no added/removed |

Latest stable on the official GitHub releases listing at this check is 6.48.1. Prereleases were not selected; the collector's newer-major guard did not report an untracked stable major.

## Findings Before Ingestion

### 6.48.0

- The public callback payload becomes `OrderUpdatedData`, retaining `order` and adding optional `sessionData?: string`. Retained `Core.processPayment` forwards its current Session data on the remaining-order branch, only when truthy. This is optional client-state restoration information, not final payment/fulfillment evidence. Its ordinary UIElement path also changes in the generated comparison but is outside the retained capsule; collect the proposed supplement before grounding that path in a full file.
- Both 3DS2 Challenge and DeviceFingerprint implementations remove their message listener when the promise settles, then skip the completion/error callback when `!base?.isConnected`. Normal Preact unmount cancellation/cleanup still exists. This suppresses stale callbacks after raw DOM removal; it does not establish immediate listener cleanup at the moment of removal or cancellation of server-side payment work. `Node.isConnected` avoids treating attached shadow-tree content as detached. The new retained TwoInstances story illustrates sibling Drop-ins sharing one Checkout/Session; it is not an executed regression test or production integration recommendation.
- Retained analytics enum adds invalid-hosting/insecure-merchant-domain codes 501/502. The actual message handling and hosted secured-fields selection sit outside the capsule. Previewed comparison hunks show SecuredField event-to-analytics wiring and SF_VERSION 6.3.0 -> 6.4.0, but those hunks are not a full-file implementation read or proof of hosted enforcement/security guarantees.
- Release notes announce Apple Pay completion/merchant-validation rejection handling, address-query preservation and Click to Pay/shared Modal null-safety. ApplePayService's authored change is visible in the comparison, but its complete file is not retained. Those fixes remain announcement/diff-preview qualified until separately collected/read.
- Runtime PayPal JS dependency advances 11.1.0 -> 11.2.0. This is a dependency pin, not independently verified PayPal behavior. Development tooling also changes; no package manager/build was run.

### 6.48.1

- Release notes announce IRIS bank-list-only mobile presentation, UPI regulatory-related changes and checkoutshopper-beta compatibility in secured-fields URL validation. They do not prove merchant eligibility, regulatory compliance or payment success.
- Only root/library package manifests change in this retained capsule. The library runtime PayPal JS pin advances 11.2.0 -> 11.2.1; tooling/build-size configuration changes are not merchant-facing runtime evidence.
- The generated comparison shows SF_VERSION 6.4.0 -> 6.4.1 in excluded SecuredFields constants; collect that exact file to preserve the hosted-version selection boundary. The remote hosted runtime's URL-validation implementation is not established by this constant.
- IRIS/UPI and shared QR implementation remain intentionally outside the configured capsule. Do not describe the two modified retained files as the whole upstream release or as verification of those payment-method implementations.

## Proposed Bounded Supplements - Not Collected

Recommend six UTF-8 file captures, without modifying snapshots or future registry policy:

At 6.48.0 SHA `a05c1184195fa73ce7dc9e956fa080cb40638209`:

1. `packages/lib/src/components/internal/UIElement/UIElement.tsx` - complete ordinary onOrderUpdated Session-refresh path, alongside retained Core review flow.
2. `packages/lib/src/components/ApplePay/services/ApplePayService.ts` - complete completion/abort error handling and callback ownership.
3. `packages/lib/src/components/internal/SecuredFields/lib/CSF/extensions/handleConfig.ts` - hosted iframe URL/version construction versus development override.
4. `packages/lib/src/components/internal/SecuredFields/lib/constants.ts` - exact SF_VERSION 6.4.0 selection.
5. `packages/lib/src/components/internal/SecuredFields/lib/securedField/SecuredField.ts` - complete message guards and invalid-hosting/insecure-domain analytics wiring.

At 6.48.1 SHA `6ccc03f83b064c2171bc836edd9b35444e582823`:

6. `packages/lib/src/components/internal/SecuredFields/lib/constants.ts` - exact SF_VERSION 6.4.1 selection.

IRIS/UPI, Click to Pay/Modal and address-lookup implementation can stay release-note-only at this stage; approve a separate exact-source deep dive if a query requires it. No invisible scope widening or claim that supplements cover the remote hosted secured-fields implementation.

## Evidence and Validation

- Snapshots: `raw/github/adyen/adyen-web/snapshots/2026-11-08-a05c118/manifest.json` (222 files / 673,061 bytes), and `2026-11-08-6ccc03f/manifest.json` (222 files / 673,140 bytes).
- Release records: `raw/github/adyen/adyen-web/releases/adyen-web/6.48.0/2026-11-08/` and `6.48.1/2026-11-08/`, each containing manifest and release notes.
- Comparisons: `tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.47.0--6.48.0/` and `6.48.0--6.48.1/`.
- Packets: `tracking/github/repos/adyen/adyen-web/ingest-packets/<work-item-id>/packet.json` and `packet.md` for each item above.
- All 666 prior/current snapshot files pass size/SHA-256/Git blob identity checks. Release-note, packet and comparison identities/hashes pass. No packet evidence gaps or unclassified changes under the existing policy.
- Repository-wide dispositions: 6.48.0 has 75 changes = 10 retained + 65 intentional exclusions; 6.48.1 has 81 = 2 retained + 79 intentional exclusions. Policy coverage is not whole-repository semantic verification.
- Collection-time reading assignments: 6.48.0 has 19 paths / 512,643 bytes; 6.48.1 has 11 paths / 332,948 bytes. This collection review is not a complete pre-ingest reading of every assigned file.
- Seeded 222 hash-verified prior raw blobs into the collector's temporary Git object store to avoid redundant network fetches. No raw evidence, selection, policy or collector code changed. Collector and seeding helper finished.
- Offline validator reports exactly the same 13 unrelated historical errors (six packet-budget rebuild failures plus six resulting invalid-packet reports and the Adyen PHP ledger alias mismatch), none for either new item. Pending work items: 2. No global all-green claim.
- Final state checks confirm both items remain awaiting approval with approved mode null. Canonical Adyen Web source/changelog and registry remain byte-identical to HEAD. No supplement was collected, and no ingest was started. Scoped whitespace check passes.

## Recommendation and Next Step

Both packets recommend delta/high. Preliminary recommendation is serial additive delta for 6.48.0, then 6.48.1, after separately approved supplement collection/review closes the targeted implementation coverage. Optional callback data and bounded lifecycle/error-handling changes do not currently establish a full-mode signal; reconsider if complete supplemental source exposes a broader incompatible or security impact.

Next approval requested: collect the six exact-SHA supplemental files and share findings before any ingest approval. Preserve all 6.47.0 and earlier history. No ingestion or publication is authorized by this collection review.

## Approved Supplement Follow-Up - 2026-11-08

User approved the six-file proposal above. Both supplement collectors completed, and all six complete files were read serially. No additional file, snapshot mutation or future-policy expansion was made. This approval did not authorize ingestion or publication.

### Identity and Attachments

- 6.48.0 supplement: `raw/github/adyen/adyen-web/supplements/2026-11-08-a05c118-97e12dcc/manifest.json`, five files / 70,075 bytes, exact SHA `a05c1184195fa73ce7dc9e956fa080cb40638209`.
- 6.48.1 supplement: `raw/github/adyen/adyen-web/supplements/2026-11-08-6ccc03f-543c5280/manifest.json`, one file / 3,424 bytes, exact SHA `6ccc03f83b064c2171bc836edd9b35444e582823`.
- Canonical attachments: `tracking/github/repos/adyen/adyen-web/evidence-attachments/github-7af6b1df429e8b0d75bf/attachment.json` and `github-63a67800194fcf63cd6f/attachment.json`. Each is linked through its work item's `evidence_attachments`, preserving the original packet and required-reading list while extending effective reading.
- Combined delta reading now validates 26 paths for 6.48.0 and 14 for 6.48.1. Both remain `awaiting_approval` with approved mode null.

### Findings After Full Supplemental Reads

1. **Ordinary Sessions partial-payment path:** `UIElement.handleOrder` waits for `core.update({ order })`, then emits `onOrderUpdated` with the resolved Core Session's truthy `data`. Retained Core.update reinitializes Checkout before resolving. The authored comment identifies this as the newer post-setup blob rather than the earlier payments response. Advanced handling also resolves through Core.update, but absent Session data does not gain a field. Persist callback-provided optional data rather than synthesizing it. This is a continuation/restoration payload, not payment-finality proof.
2. **Review-page path remains distinct:** retained `Core.processPayment` directly forwards `this.session?.data` on the remaining-amount branch; it does not perform the same Core.update in that branch. Do not claim every callback path performs an identical post-setup refresh. Existing merchant review/action/error and backend verification responsibilities remain.
3. **Apple Pay completion:** success/rejection completion calls use a helper that catches and warns on `session.completePayment` exceptions. A rejection value with numeric `status` remains an authorization-result payload; other rejection reasons become `STATUS_FAILURE`. That numeric-status check is not exhaustive result validation, and a sheet completion is not backend authorization/capture proof.
4. **Apple Pay merchant validation:** errors from merchant validation/completion attempt abort inside try/catch. If abort throws, the code warns and returns without the extra `onError` call (the upstream comment attributes this to prior cancellation); if abort succeeds, it invokes `onError(error)`. Do not claim onError always fires or all Apple Pay selection/coupon/shipping promises are newly protected; those handlers retain their existing direct completion calls. No browser/cancellation race was executed here.
5. **Secured-fields diagnostics:** the complete message path first invokes its existing origin-check helper, parses feedback and checks action/numKey plus matching per-field numKey before dispatch. `invalidHosting` and `insecureMerchantDomain` create internal analytics error events using supplied codes or 501/502 fallbacks and optional `submitAnalytics`. These branches do not directly invoke merchant validation callbacks, display a shopper error or independently reject a payment. The imported origin-check helper itself was not newly collected, so no broader security audit is claimed.
6. **Hosted runtime selection:** 6.48.0 constants select SF_VERSION 6.4.0, and handleConfig builds `${loadingContext}securedfields/${clientKey}/${SF_VERSION}/securedFields.html` with bundle/origin query data. The development override separately uses `vn=${SF_VERSION}`. 6.48.1 constants select 6.4.1. The hosted validation implementation is not in these files; checkoutshopper-beta support remains an upstream announcement associated with the version selection, not an independently verified allowlist or production deployment.

IRIS/UPI, address lookup and Click to Pay/shared Modal remain release-note-qualified. No further source is silently inferred from their announcements, no complete upstream-source read is claimed, and no SDK install/build/test/browser/payment execution occurred.

### Follow-Up Validation and Decision

All six supplemental sizes, SHA-256 hashes and Git blob identities pass; exact work-item SHA/supplement identity and canonical attachment links validate through the existing APIs. The attachment extends immutable source evidence, not version history or workflow approval. An initial local helper referenced a nonexistent attachment `.path` attribute after publishing the first record; it was corrected to the actual `.relative_path` field, safely reused the identical record and linked both attachments. No collector code or accepted evidence changed.

Final offline validator reports the same 13 unrelated historical structural errors, none for either item or attachment, and two pending work items. Both effective reading lists validate, both items remain awaiting approval with approved mode null, all current snapshot content hashes pass, and canonical source/changelog/registry are byte-identical to HEAD. Scoped whitespace check passes. No global all-green claim. Recommended mode remains delta for both releases: optional additive callback data, bounded lifecycle/error handling and diagnostics/version selection do not establish a broader incompatible API or unbounded security change in the reviewed evidence.

**Next approval:** serial additive delta ingestion of 6.48.0 including its five-file supplement, then 6.48.1 including its one-file supplement, preserving all prior history. Recommend focused reading: fully read changed authored source, supplemental files, affected prior/dependency code, release notes and cumulative wiki source/changelog; mechanically verify generated manifests/inventories, unchanged history and duplicated diff. Neither ingest is approved or started yet; commit/push remain a separate gate.
