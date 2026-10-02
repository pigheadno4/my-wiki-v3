# Stripe iOS 26.11.0 review checkpoint

- Work item: `github-266fd96ba1fdc3d98b71`
- Review date: 2026-10-02
- Boundary: `stripe-ios@26.10.0` -> `stripe-ios@26.11.0`
- Current SHA: `70378192e4b345bd4283511e1f6a3151591ebecf`
- State: user approved full additive mode with the focused-reading exception; serial ingest completed on 2026-10-02.
- Reading authorization: user approved focused reading for this release. Changed retained files and affected prior code require full reading; unchanged history/inventories may be checked mechanically.

## Verified so far

Both retained snapshot file inventories pass SHA-256 checks: 273 prior files, 275 current files. Packet Markdown hash matches. Retained counts: two added, 19 modified, 254 unchanged. Upstream dispositions: 21 retained, 459 intentional policy exclusions. These classifications do not establish complete semantic coverage.

Read release notes, the complete retained diff, all changed retained implementation, README, eight podspecs, VERSION and changed changelog content. Recovered truncated output using bounded reads, including payment-handler, configuration and parameter-file sections. Both new Scalapay files were read in full in the patch. Read the supplemental controller and attachment in full. Packet/comparison inventories were inspected structurally under the approved exception; cumulative source/changelog context remains at the completed 26.10.0 ingest. This is a review receipt, not an ingestion receipt.

Comparison Markdown/patch and release-note hashes match their records. The cumulative changelog preserves all 2,148 prior lines with eleven insertions: ten for 26.11.0 and one retrospective Kakao Pay bullet under 26.10.0. The automated empty public-API/gap arrays are not exhaustive Swift semantic analysis.

## Findings

1. Checkout confirmation introduces `withoutPaymentMethod` when `session.paymentOption == nil`, before requiring a PaymentElement. Request construction supplies nil method ID/type, session amount, return URL, attribution and optional session email. The branch does not itself check for a zero amount or establish general free-order/subscription support.
2. A confirm response with neither PaymentIntent nor SetupIntent now proceeds instead of failing immediately. Completed polling sets the reconstructed session status to complete in the nil-Intent branch; timeout does not. Both can still reach `.completed(updatedResponse)` if decoding succeeds. Payment status is not forced to paid. SDK completion is not backend settlement or confirmed session completion.
3. The approved exact-SHA controller supplement closes current caller reachability: `confirm(from:)` forwards its optional PaymentElement into the reviewed flow builder. Prior-release controller evidence is not substituted for current code. This remains SPI, not a generally available free-order or subscription integration recipe.
4. Link `walletButtonHidden` documentation now says existing Link users see its button/row; the old unconditional `shouldShowButton` property is removed. Downstream behavior must remain qualified until reviewed.
5. Scalapay gains typed API bindings and a PaymentSheet release announcement. Its processing state enters the handler's false classification; model/parameter files are not merchant-eligibility proof.
6. PaymentIntent inferred-mandate handling removes Kakao Pay. The cumulative changelog retrospectively inserts Kakao Pay PaymentSheet support under 26.10.0. Preserve that as a later annotation, not evidence that the old retained notes announced it or proof of old implementation.
7. Release notes add Welsh. Identity configuration adds SPI primary-button styling, with default/custom colors and documented disabled/secondary-button limits. Downstream UI implementation remains excluded.

## Grounding pointers

Current snapshot root: `raw/github/stripe/stripe-ios/snapshots/2026-09-30-7037819/files/`.

- `StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm.swift`: `if session.paymentOption == nil`, `case withoutPaymentMethod(STPAuthenticationContext)`, `clientCompletedIntent = nil`, `if didPollToCompletion`, `return .completed(updatedResponse)`.
- `StripeIdentity/StripeIdentity/Source/IdentityVerificationSheet.swift`: `case custom(backgroundColor: UIColor, textColor: UIColor)`.
- Comparison: `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.10.0--26.11.0/diff.patch`.

## Supplement history

### Approved supplement collected and read, 2026-10-02

User approved the single current controller file. Collected it at the exact release SHA under `raw/github/stripe/stripe-ios/supplements/2026-10-02-7037819-bd3ee3a4/`; read its manifest and full 20,093-byte source. File SHA-256: `aca8c0a711f90996cc605bc78f510b7548dc1e38d75d42e66451a9160f400e4f`. The canonical attachment is `tracking/github/repos/stripe/stripe-ios/evidence-attachments/github-266fd96ba1fdc3d98b71/attachment.json`, linked from this pending work item. Original snapshot and future policy are unchanged.

The controller's `confirm(from:)` requires a presenter, passes its optional `paymentElement` to `makeConfirmationFlow`, rejects an invalid returned flow and otherwise calls `confirm(flow)`. This closes the current caller-reachability gap for the new no-payment-method branch. The controller remains STP/ReactNativeSDK SPI. Its result documents completed/canceled/failed and payment statuses paid/unpaid/no_payment_required; the retained engine's nil-Intent timeout path means the completed label must not be treated as proof that the session status became complete or funds moved.

The full controller additionally exposes serialized session updates, server-update timeout handling and element propagation. These are current supplemental observations, not all proven newly introduced at 26.11.0 because the immediate prior controller was not collected. No additional gaps are silently filled by this file; request serialization, backend behavior and other delegated internals remain outside this supplement.

Collection initially failed on sandbox DNS resolution, then succeeded with approved network access. No partial accepted evidence was used. The original one-file supplement request is fulfilled; no additional collection is proposed.

## Final mode recommendation and ingest guidance

Recommend **full additive**, overriding the generated delta recommendation because Checkout adds a new confirmation flow and changes missing-Intent and polling-result semantics. Keep the approved release-specific focused-reading exception: changed retained content and current supplement read fully, affected prior code compared, unchanged evidence checked mechanically. Full mode is not permission to overwrite older knowledge or claim full-repository coverage.

- Scalapay has response decoding, parameter initialization/serialization and a type identifier; its enum case precedes unknown. Params expose no typed method-specific fields but retain additional API parameters. Optional billing parameters do not prove backend billing is optional. Processing is not classified as completed for this method. PaymentSheet support remains a release announcement without retained availability/form-factory implementation.
- Explicit PaymentIntent mandate data still wins over inference. SetupIntent confirmation params are not in the changed retained list; do not generalize Kakao Pay's PaymentIntent change to setup flows.
- Preserve walletButtonHidden's older documented semantics under their versions; label the new recognized-user behavior as current configuration documentation, not end-to-end UI verification.
- ApplePayConfirmationParameters stops accepting billingDetailsCollectionConfiguration. This does not prove that Apple Pay stops requesting billing information: current delegated wallet context is excluded.
- Identity primary styling is SPI, with documented default disabled styling and unaffected secondary buttons. Actual changed Identity rendering remains excluded.
- Checkout's no-Intent timeout path can return completed while retaining the original open session status and payment status if response decoding succeeds. Preserve this as a code-level warning; no runtime reproduction or backend acceptance test was performed. Successful polling alone changes status, not payment_status, in the nil-Intent branch.

Remaining gaps: request serializer/API implementation, current poller implementation, wallet context, Link visibility consumers, payment-method availability/form factories and Identity rendering. No more collection is needed for these bounded claims. Do not infer merchant eligibility, general availability, complete free-order support, settlement or exact first introduction dates for newly supplemented controller behavior.

Next: user approval of full additive ingest with focused reading, then one serial work item preserving historical source/changelog sections, updating the existing iOS concept first, and recording the retrospective Kakao Pay annotation. No wiki edits, ingest transition, commit, push or SDK/runtime tests during this review.

## Ingest receipt, 2026-10-02

The review-stage next action above was subsequently approved. Claimed only `github-266fd96ba1fdc3d98b71` in full mode. The effective full list expands to current retained evidence plus packet/attachment context; the approved exception permits mechanical treatment of unchanged files/history rather than a fresh full read. Review-stage changed-source and supplement reads remain the grounding evidence; cumulative source/changelog were reread before writing, with truncated output recovered in bounded sections. Four exact confirmation-code excerpts were verified before edits.

Updated the existing iOS concept first, then cumulative source and changelog, company catalog, Stripe index and both logs. Preserved all earlier release sections and raw pointers. Version-qualified differences resolve the old missing-Intent failure and Link documentation without overwriting them; the Kakao Pay note is explicitly retrospective. No new source count, unrelated concept or cross-company comparison was warranted.

Five frontmatter-bearing pages pass targeted wiki validation. The seven-page run reports only the existing missing frontmatter in `wiki/stripe-index.md` and `wiki/log.md`, confirmed in HEAD and left outside scope. GitHub collection validation passes (148 snapshots, 133 release records, 90 comparisons, 147 work items); whitespace diff check passes. The work item is marked ingested through the collector CLI. No SDK/runtime/payment tests, commit or push. Next candidate is 26.12.0, subject to separate review and approval.
