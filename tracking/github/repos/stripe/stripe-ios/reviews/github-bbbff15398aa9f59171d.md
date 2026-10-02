# Stripe iOS 26.9.0 review checkpoint

## Identity and authorization

- Item: `github-bbbff15398aa9f59171d`
- Boundary: `stripe-ios@26.8.0` -> `stripe-ios@26.9.0`
- Prior SHA: `844404116961cb66eb8d67253386b4d564c66e87`
- Current SHA: `841b697a9c45a97a36ade02d9184c7d11b927e82`
- User approved review with a release-specific focused-reading exception:
  changed/new retained files read fully, affected prior code compared, unchanged
  history and manifest inventories checked mechanically. Not ingest approval.

## Checks and reading progress

Both snapshots pass file-size and SHA-256 checks: 263 prior and 273 current
files. Retained comparison counts are ten additions, 31 modifications, zero
removals and 232 unchanged files. The cumulative changelog preserves all 2,131
prior lines and inserts only four lines (2,135 current). The packet assigns
50 paths totaling 1,238,792 bytes; its complete semantic review is not finished.

Release notes and comparison Markdown were read. Current Checkout+Confirm.swift
and Checkout+Confirm+Link.swift were read fully. Packet JSON inventories were
inspected structurally. Remaining assigned implementation and prior comparisons
still need review; do not describe this checkpoint as completed review.

## Material finding requiring bounded evidence

Release notes announce API bindings for Kakao Pay, SeQura, Korean cards, Naver
Pay and PAYCO. Retained Checkout source exposes broader confirmation changes:

- The core result mapping returns `.completed(paymentStatus:)`, unlike the
  prior `.succeeded(paymentStatus:)` mapping.
- Confirmation handles a returned PaymentIntent before SetupIntent and rejects
  missing returned Intents. It explicitly rejects manual-approval and
  orchestration responses.
- An open session is passed to a new CheckoutSessionPoller. Completed and
  timed-out outcomes both proceed to client-side response reconstruction;
  payment-method-required, failed asynchronous payment, invalid/expired
  outcomes instead retrieve the session and return failure.
- Reconstruction marks a succeeded PaymentIntent complete/paid; processing
  marks the session complete without forcing paid. A succeeded SetupIntent
  marks complete. Do not turn client completion into settlement proof or claim
  timeout itself establishes payment success.
- Link-produced methods now use the shared request-construction/confirmation
  flow; a completed Link result without a returned session still fails.

Evidence prefix:
`raw/github/stripe/stripe-ios/snapshots/2026-09-30-841b697/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/`.
Key locations in Checkout+Confirm.swift: result mapping line 270, poller
construction line 405, Intent dispatch lines 434/460, timeout continuation
line 497 and response reconstruction lines 545-559.

The packet classifies the newly added CheckoutSessionPoller.swift and modified
CheckoutController.swift as intentional policy exclusions. The prior release's
controller supplement is not evidence of their current implementations.
Timing, retry/termination rules and the complete current result contract remain
unverified. Apple Pay wrapper/context changes also remain excluded; do not
reuse the prior supplement as current proof.

## Proposed next step (approval required)

Collect exactly these two files at the current SHA as an immutable supplement:

1. `StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/CheckoutSessionPoller.swift`
2. `StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/CheckoutController.swift`

Read them fully, attach them to this item, and finish the remaining focused
review before recommending ingest mode. Do not change snapshot contents or
future capsule policy. No additional Apple Pay collection is proposed.
The retained confirmation changes suggest a full-additive signal, but mode
recommendation is pending review completion. No wiki ingest, commit, push,
SDK build or runtime payment verification.

## Approved supplement collected and read (2026-09-30)

Exactly the two approved files were collected at the current SHA, totaling
27,225 bytes, and read fully with their manifest and canonical attachment.
The first sandbox attempt failed DNS resolution; the same collector succeeded
with network permission. No accepted snapshot or future capsule policy changed.

- Supplement: `raw/github/stripe/stripe-ios/supplements/2026-09-30-841b697-f58a4b7c/manifest.json`
- Attachment: `tracking/github/repos/stripe/stripe-ios/evidence-attachments/github-bbbff15398aa9f59171d/attachment.json`
- Queue linkage preserves `awaiting_approval` and no approved ingest mode.

The poller uses a 30-second elapsed-time budget, passing remaining time to each
request. Normal minimum spacing is 0.5 seconds between request starts. Request
failures retry until the budget expires; HTTP 429 increases minimum spacing to
2, 4 and then at most 8 seconds. A successful request resets that spacing and
rate-limit counter. The delegated API client's timeout enforcement is not
verified, so do not promise a strict observed wall-clock bound.

`requiresPaymentMethod` takes priority over session-state classification.
Active, processing-sync-payment and processing-subscription continue polling;
succeeded, processing-async-payment and pending-async-customer-action return
`completed`. Failed asynchronous payment and invalid/expired return distinct
outcomes. The previously read caller permits both completed and timed-out
outcomes to proceed to response reconstruction using the client-completed
Intent; neither outcome independently establishes settlement. Source comments
link to internal web implementations, which were not accessed and do not prove
cross-platform parity. No runtime test was performed.

The controller confirms the SPI enum rename from `succeeded` to `completed`
against the fully read 26.8.0 supplemental controller. PaymentElement becomes
optional and is initialized only when configured; `confirm(from:)` fails if
it is absent, while `getPaymentElement()` asserts configuration/presence and
force-unwraps. Adaptive-pricing allowance now follows whether a currency
selector is configured rather than the old adaptive-pricing flag.

`updateShippingAddress` now requires an explicit name argument and accepts a
nil address to clear shipping. Clearing retains the previous country for tax
region updates when shipping is the tax source, because the comment says the
endpoint does not support clearing tax_region. Otherwise the caller updates
local shipping without sending a tax-region update. Excluded performUpdate
internals limit broader persistence claims. The 20-second merchant update
timeout and multi-scene presenter warning remain.

The two-file supplement task is complete. Remaining original packet files
still require focused review before a final ingest recommendation. No further
collection, wiki ingest, commit or push.

## Focused review completed (2026-10-02)

This section supersedes the pending-review status above, not the historical
record of collection or authorization. Recommendation: **full additive** for
`stripe-ios@26.9.0`, retaining the release-specific focused-reading exception.
The generated packet's `delta` recommendation remains unchanged; this is a
human-review recommendation, not an approved mode or queue transition.

### Reading and integrity

All 40 changed/new retained files other than the cumulative CHANGELOG were
read fully: ten new payment-method model/parameter files, 21 other Swift files,
eight podspecs and VERSION. The two attached current-SHA supplemental Swift
files were also read fully. The complete retained diff was reviewed against
affected prior code, including the prior supplemental controller comparison.
Both packet representations, release record/notes, comparison prose and the
cumulative wiki source/changelog were reviewed. Manifest inventories and
unchanged source/history used the approved mechanical checks rather than a
claim of a fresh full read.

Fresh checks confirm all 263 prior and 273 current snapshot file sizes and
SHA-256 values; 10 added, 31 modified, zero removed and 232 unchanged files.
The packet Markdown/current manifest, comparison Markdown/patch and release
notes match their recorded hashes. All 50 original required paths exist.
CHANGELOG adds four lines after its opening metadata; all 2,131 historical
lines remain unchanged. The original packet is format 1; the snapshots and
comparison are format 2. Empty automated public-API/gap arrays are not proof
of complete Swift API compatibility or complete repository coverage.

### Findings to preserve during ingest

- New API bindings cover `kakao_pay`, `kr_card`, `naver_pay`, `payco` and
  `sequra`: type identifiers, response properties/decoding, parameter factories,
  convenience initializers and serialization mappings. Korean cards expose
  brand and optional last4; Naver Pay exposes buyer ID and card/points funding.
  Unknown funding maps to no typed serialized value. These types do not prove
  PaymentSheet availability, merchant eligibility, supported currencies or
  preview access. New cases precede `unknown`; do not claim every existing
  numeric enum value is preserved.
- PaymentIntent and SetupIntent mandate-inference lists add Kakao Pay, Korean
  cards and Naver Pay, not PAYCO or SeQura. All five enter the payment handler's
  group where processing alone is not a successful completed Intent.
- Checkout uses shared request construction and confirmation, handles a
  PaymentIntent before a SetupIntent, checks unsupported manual approval and
  orchestration, and polls open sessions. The detailed outcome, retry and
  client-completion limits recorded above remain essential. The internal
  `completed` result and timeout continuation do not prove funds moved.
- Link wallet callbacks now require a Link option and recurse through
  `confirmLink`; resulting new/saved methods use the shared Checkout path.
  The earlier route accepted new/saved options directly. New-method request
  construction schedules challenge completion in a deferred Task; do not
  describe that scheduling as awaited end-to-end challenge completion.
- Checkout's SPI result case changes from `succeeded` to `completed`.
  Checkout-specific Embedded and FlowController creation overloads become
  internal (including the async FlowController overload); ordinary public
  Intent-based creation remains. Embedded Checkout creation accepts an initial
  payment option and maps it into the initial row selection. The changed row
  conversion helper is excluded, so preservation of every option's details
  is not established.
- Supplemental controller changes include optional PaymentElement, a guarded
  confirm path when absent, currency-selector-based adaptive-pricing allowance,
  and a nullable shipping address with explicit name argument. These are SPI
  compatibility notes, not a generally available Checkout integration recipe.
- Financial Connections adds the STP SPI `hasRequestedDataPermissions` flag,
  default false, and forwards it to its API client. LinkAccountSession decodes
  permissions with an empty-array fallback. Public FinancialConnectionsSheet
  presentation treats a payment-details host result as unsupported, not a new
  successful public result. Excluded API/host internals prevent consent or
  actual data-access claims.
- Link preview rendering switches from `unparsable` to `generic`, using a Link
  icon and a card-category preview for that case. The excluded decoder and UI
  internals prevent claiming that every unknown payment method is accepted.
  Several confirmation/UI helpers gain MainActor isolation.
- New internal Apple Pay contact-field helpers map automatic/full address to
  billing postal address, always-name to billing name, and always-email/phone
  to shipping contact fields. Changed callers, wallet context and wrapper are
  excluded at this SHA; these helpers do not establish actual wallet request
  behavior or a new public Apple Pay integration contract.
- Retained podspec changes only bump versions. Release notes are dated
  2026-08-31; this review does not claim 26.9.0 is latest upstream.

### Grounding locations

Paths below are relative to the current snapshot's `files/`, except the
controller, which is relative to the attached supplement's `files/`.

- `StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm.swift:434`:
  `if let paymentIntent = response.paymentIntent {`
- `StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/CheckoutController.swift:379`:
  `case completed(paymentStatus: Session.Status.PaymentStatus)`
- `StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedPaymentElement.swift:134`:
  `initialSelection: initialPaymentOption.map(RowButtonType.init)`
- `StripePayments/StripePayments/Source/API Bindings/Models/ACH/LinkAccountSession.swift:51`:
  `permissions: response["permissions"] as? [String] ?? [],`
- `StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetConfiguration.swift:796`
  and `:807`: internal Apple Pay billing/shipping contact-field helpers.

### Recommendation and next boundary

Full mode is justified by broad confirmation/polling and SPI compatibility
changes, despite the minor release number and automated delta recommendation.
It means adding a version-qualified baseline and changelog entry, not replacing
older knowledge or claiming a complete repository review. In particular, keep
26.8.0's SetupIntent-first dispatch and `succeeded` result as historical facts;
record 26.9.0's opposite dispatch order and renamed result alongside them.
Do not carry forward the old no-payment-required save suppression as a verified
26.9.0 fact: request serialization moved into excluded implementation.

Await user approval of full additive ingest with focused reading. Then process
only this work item, run the normal concept/contradiction/index/log workflow,
and preserve all earlier version sections. Current Apple Pay internals,
request serialization, poll-response decoding and backend timeout enforcement
remain bounded evidence gaps, not reasons to infer behavior from old snapshots.
No SDK build, simulator, live payment, settlement or eligibility verification
was performed. No wiki pages, queue state, commit or remote were changed by
this review-completion step.

Validation on 2026-10-02: `validate_github_collection.py` passed with 148
snapshots, 133 release records, 90 comparisons and 147 work items, with no
structural errors. `git diff --check` passed. These are evidence-structure and
whitespace checks, not SDK runtime tests.

## Approved ingest completed (2026-10-02)

The user approved the full-additive recommendation with focused reading.
The normal approve/next-ingest commands claimed only this work item in full
mode. Its effective reading list contains 286 paths; the approved exception
retains full reads of changed/new implementation and the two supplements,
with unchanged evidence checked mechanically as documented above.

Updated the existing Stripe iOS concept first, then the cumulative source and
changelog, company catalog, provider index and provider/root logs. All previous
version sections remain; no new source count or cross-company comparison was
introduced. Version-qualified differences are recorded alongside older facts,
and delegated implementation gaps remain explicit. Raw evidence was unchanged.

The five frontmatter-bearing touched pages pass validate_wiki. The seven-page
run reports only missing frontmatter in stripe-index.md and log.md, both
confirmed present in HEAD before this work; those unrelated schema issues were
not changed. Collection validation passes (148 snapshots, 133 release records,
90 comparisons, 147 work items); git diff --check passes. The normal
complete-ingest command marked the item ingested. No commit or push.

Next candidate: stripe-ios@26.10.0, requiring separate review and approval.
