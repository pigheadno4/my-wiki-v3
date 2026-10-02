# Stripe iOS 26.8.0 review checkpoint

## Identity and authorization

- Work item: `github-4ef7ad96d01f40cfff58`
- Boundary: `stripe-ios@26.7.0` -> `stripe-ios@26.8.0`
- Prior SHA: `62c2070c57f20b4d632b25fc62780841f8883cc8`
- Current SHA: `844404116961cb66eb8d67253386b4d564c66e87`
- User authorized review and focused reading for this release only, not ingest.
- Queue remains awaiting approval. No collection, wiki edit, commit or push.

## Progress and verified limits

Prior/current snapshot manifests were checked mechanically: every retained file
size and SHA-256 matches (262 prior, 263 current). Packet Markdown hash matches
its JSON. The format-1 packet assigns 40 paths totaling 1,089,905 bytes; semantic
review of that complete assignment is NOT finished.

Release notes and comparison summary were read. Current `Checkout+Confirm.swift`
and `Checkout+Confirm+Link.swift`, and prior `Checkout+Confirm.swift`, were read
fully. The changed payment-error branch was inspected but the complete current
payment handler has not yet been read. Packet inventory was inspected as
structured data; its long Markdown rendering was truncated, not fully read.

## Important finding before further review

The current `Checkout+Confirm.swift` extends `CheckoutController` and constructs
typed Apple Pay, Link and conventional payment-method flows. Confirmation guards
reject a closed session, concurrent confirmation and pending session updates.
The queued operation commits a returned response and maps the internal result:

> `return .succeeded(paymentStatus: response.paymentStatus)`

The retained Link helper requires a returned session to represent completion;
completion without one becomes an error:

> `Link completed Checkout confirmation without returning the confirmed session.`

The prior retained conventional confirmation helper had an Apple Pay TODO that
returned canceled. Current dispatch instead calls:

> `result = await Self.confirmApplePay(checkoutSession: self.session, parameters: parameters)`

These are material payment-confirmation changes, not merely the three release
announcements (FPX banks, 3DS decline-message fix, preview Link permissions).
They suggest full additive ingest may be appropriate under the common rule;
the automated delta recommendation is not a completed semantic decision.

The upstream inventory explicitly excludes the newly added Apple Pay helper
and renamed controller. Retained callers cannot establish complete Apple Pay
behavior, public availability or readiness. Do not repeat the 26.6.0 unfinished
result mapping as a current finding, and do not claim end-to-end resolution.

Evidence prefix:
`raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/`.

## Proposed bounded supplement (approval required)

At the current exact SHA, collect and read only:

1. `StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/CheckoutController.swift`
2. `StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm+ApplePay.swift`

Purpose: verify the controller entry-point/result contract and the new delegated
Apple Pay confirmation implementation. Publish immutable supplemental evidence
and link it to this work item; do not change the existing snapshot or future
registry policy. Then finish the remaining focused review, report verified
findings and recommend ingest mode. This checkpoint is not ingest approval or
a claim of full review completion. No SDK build or runtime payment test.

## Approved supplement collected and reviewed (2026-09-30)

Both requested files were collected at the approved SHA and read fully (452
lines, 19,144 bytes). The initial sandbox attempt failed DNS resolution; the
same command succeeded with network permission. No partial snapshot was used.

- Supplement: `raw/github/stripe/stripe-ios/supplements/2026-09-30-8444041-bea35b75/manifest.json`
- Canonical attachment: `tracking/github/repos/stripe/stripe-ios/evidence-attachments/github-4ef7ad96d01f40cfff58/attachment.json`
- Attachment linked to this item while preserving `awaiting_approval` and no
  approved mode. Existing snapshot and registry policy were not changed.

The controller is explicitly STP/ReactNativeSDK SPI. Its public-on-SPI
`confirm(from:)` resolves a presenter and flow, then returns `await confirm(flow)`.
The retained confirmation engine therefore maps its outcome rather than the
old historical always-canceled mapping. `succeeded(paymentStatus:)` may carry
paid, unpaid or no-payment-required status; it is not settlement proof.

The nil-presenter fallback uses the key-window visible controller and explicitly
documents that it is not compatible with multi-scene apps. Initialization orders
shipping normalization/default application before PaymentElement, then creates
the remaining session-observing elements. Server updates document a 20-second
timeout and refresh the session after the merchant callback; delegated timeout
and queue implementations were not added by this supplement.

The 28-line Apple Pay helper creates `CheckoutApplePayContext`, awaits
`presentApplePay()`, and maps thrown errors to failure. The context itself remains
excluded, so actual wallet authorization, request construction and result
handling are not verified. Do not silently collect further dependencies or
claim complete Apple Pay support from this wrapper.

Collection validation passed with 148 snapshots, 133 release records,
90 comparisons and 147 work items, no structural errors. The two-file supplement
task is complete; the remaining original 26.8.0 focused review is still pending.
Next: finish that review and report the ingest-mode recommendation. No wiki
ingest, commit or push.

## Focused review completed (2026-09-30)

This entry supersedes the pending-reading statements above. The approved
focused review covered all changed retained Swift implementations in full,
README, eight podspecs, VERSION, release notes, the two approved supplemental
files, and affected prior code/comparison hunks. Manifest inventories and
unchanged cumulative history were checked mechanically, not claimed as fresh
full semantic reads. The packet Markdown inventory was inspected through its
structured JSON counterpart; its previously truncated rendering is not claimed
as a full read. No additional collection or wiki ingest was performed.

The capsule has 232 unchanged files, 30 modified files and one added file.
Changelog comparison preserves all 2,118 prior lines and inserts 13 lines
(2,131 current lines); there are no replacements or deletions. Collection
validation passed: 148 snapshots, 133 release records, 90 comparisons and
147 work items, with no structural errors. These are evidence checks, not
an SDK build or runtime payment test.

### Findings and attribution

- **Checkout confirmation architecture:** the retained engine now uses typed
  Apple Pay, Link and conventional payment-method flows under
  `CheckoutController`, guards concurrent/pending confirmation, commits returned
  session responses and maps their result. Link completion without a returned
  session fails explicitly. The supplemental controller confirms the entry
  point reaches this engine. This is a broad SPI payment-behavior change, not
  merely a symbol rename. Standard `PaymentSheet.confirm` still rejects Checkout
  sessions; its error directs callers to `CheckoutController.confirm`.
- **Apple Pay evidence boundary:** the prior retained helper's TODO/canceled
  path is replaced by delegation to the newly retained wrapper. The wrapper
  awaits `CheckoutApplePayContext`, whose implementation is still excluded.
  Do not claim end-to-end wallet support, authorization correctness, merchant
  eligibility, or general availability. The controller is STP/ReactNativeSDK
  SPI, and `succeeded(paymentStatus:)` is not settlement proof. The old 26.6.0
  always-canceled outer mapping must remain historical, not a current claim;
  the exact first fixed release is not established by the missing prior outer
  controller evidence.
- **Post-3DS decline messages:** `STPPaymentHandler._error` now prioritizes an
  existing localized description over generic API-code localization. This
  preserves supplied decline text; it does not change payment approval rules.
- **FPX:** adds Agrobank, Bank of China and MBSB Bank and converts bank mappings
  to dictionaries. Added status codes are Agrobank AGRO02/AGRO01
  (business/individual), Bank of China nil/BOCM01 and MBSB MBSB001/MBSB001.
  Existing enum cases retain their order; the new cases follow `unknown`.
  SDK mappings alone do not prove live bank availability.
- **Link private preview:** top-level `LinkConfiguration` gains optional
  `financialConnectionsPermissions`; `LinkController` copies it into deferred
  setup configuration before loading. This is not the nested
  `PaymentSheet.LinkConfiguration`, nor proof that permissions were granted.
  `LinkSettings` also decodes a bank-account data-consent string from
  `link_payment_session_context`; consent UI/backend behavior remains outside
  this retained evidence.
- **Alipay/Klarna low-level options:** Alipay gains currency and future-usage
  fields, and inferred SetupIntent mandate handling. Klarna private-preview
  options distinguish interoperability tokens (PaymentIntent/SetupIntent)
  from partner confirmation tokens (PaymentIntent only). SetupIntent params
  gain private-preview payment-method options, including encoding/copying.
  The retained `PaymentSheet.makeSetupIntentParams` does not forward the
  incoming payment options automatically; do not advertise automatic
  PaymentSheet integration from these low-level additions.
- **Historical annotations:** this changelog adds horizontal-layout Link and
  Alipay notes under 26.7.0, and a Klarna note under 26.5.0. Record their stated
  historical attribution separately from implementation observed changing at
  the retained 26.7.0 -> 26.8.0 boundary. Those headings do not prove the added
  code existed in the older retained SHA. The horizontal-layout fix is not
  established by the retained controller changes alone.
- **Maintenance:** mandate providers gain MainActor isolation; podspec changes
  are version bumps, not new platform floors. README describes pinned cached
  SwiftLint use; excluded scripts were not executed or verified.

### Recommendation and next gate

Recommend **full additive ingest**, overriding the automated delta suggestion
because the Checkout confirmation architecture/payment behavior changed broadly.
Add a version-qualified 26.8.0 baseline to the cumulative source and append its
changelog entry; preserve all validated older knowledge and evidence gaps.

Request explicit user approval for that ingest **using this release's focused
reading exception**, with unchanged current files checked mechanically rather
than claiming a new full read of the entire capsule. Full mode otherwise expands
the effective reading assignment. This checkpoint does not approve or start
ingest. No commit, push, SDK build, or runtime payment verification.

## Approved ingest executed (2026-09-30)

The user approved the full additive ingest and release-specific focused-reading
exception. The CLI approved full mode, claimed this item and completed it as
`ingested`. The expanded full-mode reading list is subject to that explicit
exception; unchanged files were not claimed as freshly read. The preceding
review's complete changed-source reads and two supplemental reads support this
ingest. Four exact grounding excerpts were verified before writing.

The existing iOS concept was updated first, followed by cumulative source,
changelog, company, provider index and logs. Older sections remain intact;
the latest-ingested row is 26.8.0, not a claim about latest upstream publication.
The Checkout result change is version-qualified and the excluded Apple Pay
context remains explicit. No new source page, source-count increment or
cross-company comparison was needed.

Focused wiki validation passed for source, changelog, concept, company and
provider log (five files). Including the provider index and root log reports
their two pre-existing missing-frontmatter findings, confirmed in HEAD; their
established format was left unchanged. `git diff --check` passed. No commit,
push, SDK build or runtime payment test. Next candidate is 26.9.0, subject to
separate review and approval.
