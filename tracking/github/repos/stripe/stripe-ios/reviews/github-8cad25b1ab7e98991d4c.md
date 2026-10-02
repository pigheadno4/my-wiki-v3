# Stripe iOS 26.12.0 review

- Work item: `github-8cad25b1ab7e98991d4c`
- Boundary: `stripe-ios@26.11.0` -> `stripe-ios@26.12.0`
- SHA: `bc51b3323a06c029c561474547910bff0db82fc8`
- Review date: 2026-10-02
- State: user approved full additive ingest with focused reading; ingested on 2026-10-02.
- Recommendation: full additive with the approved release-specific focused-reading exception. Override generated delta because the release explicitly announces removal of public alpha CryptoOnramp image API exposure. Full mode preserves older history; it does not expand factual claims beyond retained evidence.

## Reading and integrity

Read both packet representations (JSON inventories inspected structurally), release manifest/notes, comparison and complete 592-line patch. Read all changed retained source/build/version content in full, except unchanged cumulative changelog history covered by the approved mechanical exception. Embedded output truncation was recovered with a bounded reread. Compared affected old code in the complete patch and the prior Link attestation method; inspected the current shared confirmation entry and async bridge for the changed callers. Existing source/changelog context is the just-completed 26.11.0 ingest, not permission to overwrite it.

Both 275-file snapshot inventories passed SHA-256 checks. Packet Markdown, comparison Markdown/patch and release-note hashes passed. The retained comparison has 16 modified and 259 unchanged files, no additions/removals. All 216 upstream entries have dispositions: 16 retained, 200 intentional exclusions. Empty automated API/gap arrays are not exhaustive Swift semantic review. All 2,159 prior changelog lines remain, with 12 insertions: eleven release-block lines and one historical annotation.

Release metadata records 2026-09-22T17:20:07Z publication, while the notes heading says 2026-09-21. Preserve both rather than silently equating them.

## Findings

### Partner terms: alpha coordinator and STP Link UI

The coordinator adds MainActor `presentTermsAndConditionsIfNeeded(from:)` and `presentTermsOfServiceIfNeeded(from:)`. They require available Link account information, retrieve terms for transactionTerms or termsOfService, and return notRequired without presenting UI when indicated. Required terms pass the returned HTML into the matching Link presenter. Acceptance calls and awaits `confirmPartnerTerms` with the declaration ID and Link account information; its response value is discarded. Accepted results alone log completion analytics. Cancellation is not acceptance; failures use existing error mapping.

Link adds a separate two-case STP `PartnerTermsResult` (accepted/canceled). Do not conflate this with the coordinator's accepted/canceled/notRequired result. Link's shared HTML confirmation helper awaits the async acceptance callback before dismissal and resumes only in the dismissal completion; callback failure dismisses and throws, while cancellation bypasses acceptance. User attestation now reuses this helper with equivalent retained callback ordering. The actual HTML controller, result/model declarations for CryptoOnramp, request serializers and backend persistence are excluded: do not infer sanitization, idempotency, complete compliance fulfillment or merchant eligibility.

### Checkout-related confirmation cleanup

Embedded `_confirm` and FlowController `confirm` remove their Checkout-specific pendingOperations rejection/enqueueSessionUpdate wrapper and call shared PaymentSheet.confirm directly. General latest-update guards remain; Embedded still prevents reconfirmation and manages disabled interaction/result state. FlowController retains its option and SEPA-mandate guards and Link-default persistence after completed results.

The current shared PaymentSheet.confirm entry still rejects Checkout intents and directs callers to CheckoutController.confirm; its async bridge delegates to that same entry. This does not establish an unguarded working Checkout route or removal of all concurrency protections. Checkout+Confirm.swift itself is unchanged by hash. Current CheckoutController and session internals changed upstream but are excluded; the 26.11.0 controller supplement must not be presented as current 26.12.0 caller evidence. No runtime safety claim or newly introduced free-order support follows.

### Other retained changes and announcements

- Identity adds STP `SecondaryButtonStyle`, default/custom background and text colors, with default property value. Documentation recommends dynamic colors, keeps disabled styling default, and says primary buttons are unaffected. Actual rendering changes are excluded.
- Package.swift adds CryptoOnramp localization resources. Eight retained podspecs only bump versions; no retained deployment-floor change or standalone Apple Pay integration change.
- Release notes announce removal of public `StripeCryptoOnramp.Image`, including linkIconSquare. The changed Image implementation is excluded. The retained coordinator still uses the image internally, which is consistent with removing public exposure rather than deleting the asset. Do not invent a replacement public API.
- StripeCore additionalHeaders for GET/POST/DELETE STP APIs and the card-scan funding-warning fix are release-note evidence only. Their implementations are outside the capsule; no header precedence, scanner mechanics or device verification claim.
- The new cumulative changelog retrospectively adds card-program-name support for saved methods with CustomerSessions under 26.11.0. It was absent in that earlier retained changelog. Preserve the later annotation separately from exact first implementation/version attribution; the changed display/category/form files are excluded.

## Grounding pointers

Current root: `raw/github/stripe/stripe-ios/snapshots/2026-09-30-bc51b33/files/`.

- `StripeCryptoOnramp/StripeCryptoOnramp/Source/Components/CryptoOnrampCoordinator.swift`: `case .notRequired:`, `declarationId: declaration.id`, `if result == .accepted`.
- `StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Link/LinkController.swift`: shared HTML helper `try await onConfirm()` before `dismissAndResumeWithResult(.success(result))`.
- `StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet+API.swift`: `Checkout Session confirmation must go through CheckoutController.confirm, not PaymentSheet.confirm.`
- `StripeIdentity/StripeIdentity/Source/IdentityVerificationSheet.swift`: `secondaryButtonStyle: SecondaryButtonStyle = .default`.
- Release manifest: `raw/github/stripe/stripe-ios/releases/stripe-ios/26.12.0/2026-09-30/manifest.json`.
- Comparison: `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.11.0--26.12.0/comparison.json` and adjacent diff.patch.

## Next action

Approve full additive ingest with focused reading, preserving earlier baselines and retrospective annotations. No further collection is needed for the bounded findings above; deeper questions about excluded functionality require separately approved exact-SHA evidence. No wiki edits, lifecycle approval/claim, SDK build, device/payment test, commit or push performed in this review.

## Subsequent ingest receipt

The user approved the recommendation. Claimed only this work item with full mode (284 effective reading paths), retaining the approved exception for unchanged content and inventories. Review-stage full changed-file reads and affected prior-code comparison ground the update; cumulative wiki history remains preserved. Verified three exact terms-flow excerpts before writing. Updated the existing iOS concept first, then source, changelog, company catalog, provider index and logs. No new source count or cross-company comparison was warranted.

Five frontmatter-bearing pages pass targeted wiki validation. The seven-page run reports only the previously confirmed missing frontmatter in wiki/stripe-index.md and wiki/log.md. GitHub collection validation and whitespace checks pass. Work item completed through the collector CLI. No additional collection, SDK/device/payment test, commit or push. Next candidate: 26.12.1, subject to separate review and approval.
