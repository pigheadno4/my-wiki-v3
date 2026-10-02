# Stripe iOS 26.12.1 review checkpoint

- Work item: `github-722f2ffc82b5d6e5375c`
- Boundary: `stripe-ios@26.12.0` -> `stripe-ios@26.12.1`
- SHA: `9f0d5aa20e6a690ff4d78b35c307f0fb88d6f36c`
- User approved focused reading for this release: changed retained files and affected prior code fully; unchanged cumulative history/inventories mechanically.
- Review completed on 2026-10-02; final recommendation below supersedes the chronological checkpoints. No ingest approval or lifecycle transition.

## Completed so far

Read release notes, comparison Markdown, required-reading inventory and complete 665-line retained patch. The new 90-line Pix QR model was read in full through the patch. Full reads of remaining changed files and integrity checks are still pending; these preliminary observations are not an ingestion receipt.

## Preliminary findings to verify in full context

- Pix adds an enum/type identifier, QR action decoding and a model with optional QR data/images/expiry but a required parseable hosted-instructions URL at decode time. Missing decoded details make the action unknown.
- Its handler requires PaymentSheetAuthenticationContext, redirects to hosted instructions and requests polling behind Safari; processing alone is not classified as success. Polling action parameters widen from PaymentIntent-specific to the shared type. Do not infer full SetupIntent behavior from this signature alone.
- PaymentIntent mandate inference adds Pix only for offSession future usage; SetupIntent adds Pix to its inference list. Explicit precedence still needs full-context confirmation.
- Financial Connections adds callback/async present and presentForToken overloads accepting preCollectedConsent and forwards it to the host. The consent type and downstream enforcement are excluded. Do not call this a general consent bypass.
- Checkout removes its new-method billing-email fallback from session email. No-method customerData email remains; an added upstream comment describes legacy requirements, not live API proof.
- CryptoOnramp routes failed post-authentication results through an excluded checkoutError helper. The newer changelog retrospectively adds error-detail preservation and StripeCore file-upload SPI notes under 26.12.0; preserve attribution separately from old raw evidence.

## Proposed bounded supplement

At the exact SHA above, collect only:

1. `StripeCore/StripeCore/Source/Connections Bindings/FinancialConnectionsPreCollectedConsent.swift` - determine the actual input contract of the new public overloads.
2. `StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/ViewControllers/PollingViewController.swift` - verify Pix polling presentation and result handling.
3. `StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/ViewControllers/PollingViewModel.swift` - verify Pix polling states and limits.

All three are listed as excluded upstream changes in the packet. This is a one-release evidence addition, not a collection-policy expansion. Publish immutable evidence and attach it to this work item only after user approval. The CryptoOnramp helper and Financial Connections event-emission internals can remain explicit evidence limits for the bounded review.

No wiki edits, ingest, commit, push or runtime testing. Next: obtain supplement approval, then finish the full changed-file review and integrity checks before recommending an ingest mode.

## Approved supplement completed

The user approved all three files. Collected at the exact release SHA under `raw/github/stripe/stripe-ios/supplements/2026-10-02-9f0d5aa-8ad0f8dd/`; read all three files and manifest fully. Published the canonical attachment and linked it through the existing work-item APIs, preserving awaiting_approval. Original snapshot and future policy are unchanged. Initial sandbox DNS failed; the approved network-enabled retry succeeded with no partial accepted evidence.

- Consent evidence contains the Stripe-issued consent object ID and Unix-seconds collectedAt. Capture affirmative acceptance of the complete issued text, preserve the timestamp across retries/reopening, and do not replace it with launch time. The SDK does not validate ID, expiry, clock skew or timestamp plausibility. Server evaluation determines whether the consent pane can be skipped; supplying evidence is not a guarantee.
- Pix polling has no displayed countdown, a configured two-second interval and an API expiresAt deadline when present; fallback is 24 hours. These are client settings, not a guaranteed backend expiry or precise network cadence.
- The controller schedules beginPolling five seconds after appearance or foregrounding; background/disappearance suspends it. This qualifies the handler comment about immediate polling. The generic IntentStatusPoller implementation is still excluded.
- At deadline, the controller suspends polling and schedules a final force poll three seconds later. A non-success result leads to the error UI. A failed polling result also enters that UI, dismisses Safari if present and completes the action as canceled, not failed. User cancellation also reports canceled; succeeded polling updates the action Intent, dismisses and reports succeeded. This UI result is not settlement proof.
- Shared polling-result mapping and request internals remain outside this supplement, so the shared action type alone does not prove every SetupIntent or Pix eligibility scenario.

The supplement request is fulfilled. Remaining task: fully read the original changed retained files and affected prior code, finish integrity/history checks and recommend ingest mode. No ingest, wiki edits, commit, push or SDK/device testing.

## Final Review - 2026-10-02

### Reading and Integrity Receipt

- Completed full reads of all changed retained implementation, eight podspecs and VERSION. The added Pix model was read fully through the patch; the changed cumulative changelog's inserted sections were read, with unchanged history checked mechanically under the approved exception.
- Read all three approved supplemental files and their manifest/attachment fully. Also fully read the retained, unchanged PollingBudget.swift as an affected dependency. Affected prior code was reviewed against the complete retained patch and prior baseline reads, with targeted rechecks of the old email fallback, mandate getter and redirect-retrieval branch.
- Read the complete current cumulative wiki source and separate changelog. Read packet narrative/required-reading metadata and comparison content; large generated path inventories were checked structurally/mechanically under the inventory exception rather than claimed as fresh semantic source reads.
- Independently matched 551 current/prior retained file hashes: 276 current and 275 prior. Counts: one added, 22 modified, 253 unchanged, no retained removals. No hash mismatches.
- Upstream inventory has 6,623 dispositions: 23 retained and 6,600 intentional policy exclusions. Exclusions are inventory evidence, not semantic review of all upstream changes. Inspected excluded implementation paths to identify the bounded gaps below; no unclassified changes reported.
- All 2,171 prior cumulative changelog lines survive byte-identically in equal diff segments; 13 lines are inserted (the new release block plus two retrospective 26.12.0 annotations). Packet Markdown hash matches its JSON authority.
- Offline validator passed: 148 snapshots, 133 release records, 90 comparisons, 147 work items, no structural errors. It validates evidence/lifecycle structure, not runtime payment behavior.

### Confirmed Findings and Qualifications

1. Pix API bindings and announced PaymentSheet support: identifier pix, next action pix_display_qr_code, optional QR data/image URLs/expiry, required parseable hosted-instructions URL when decoding. Missing decoded details downgrade the next action to unknown. URL parsing alone is not an HTTPS/absolute-URL safety guarantee. The handler requires PaymentSheetAuthenticationContext; ordinary authentication contexts fail as unsupported. It attempts native URL opening with a Safari fallback and requests polling. The QR action and Pix processing state are not classified as client success merely because they are pending.
2. Supplemental polling contract: Pix hides its countdown, configures a two-second retry interval and uses the API expiry when available, otherwise a 24-hour fallback. Polling is scheduled five seconds after appearance/foregrounding and suspended on background/disappearance. Deadline handling schedules a final force poll three seconds later. Failed/non-success timeout UI completes the action as canceled; succeeded results update the action Intent before completing. These are client settings/callback semantics, not network-cadence or settlement guarantees. Generic IntentStatusPoller and action-result mapping remain excluded.
3. Pix redirect-return caveat: STPPaymentHandler.swift:1696 excludes only PayNow and PromptPay from cancellation when a retrieved Intent still requires action. The fully read PollingBudget initializer returns nil for Pix. Consequently this path can call complete(canceled) for still-pending Pix after redirect return/dismissal rather than leaving completion solely to the polling controller. This is a code-path risk, not a device reproduction; concurrency/UI consequences remain unverified. Do not equate canceled with no payment.
4. Mandate inference: explicit mandate data still takes precedence. PaymentIntent adds inferred values for Pix only with offSession future usage and a known method type; the static general PaymentIntent inference list does not add Pix. SetupIntent adds Pix to its inference list. This does not prove every Pix setup/recurring/account-eligibility scenario.
5. Financial Connections adds callback/async present and presentForToken overloads with optional preCollectedConsent. The supplemental type represents a Stripe-issued consent ID plus the actual Unix-seconds acceptance timestamp for the complete issued text. Server evaluation controls whether the pane is skipped. The sheet stores the value; its original overloads and dismissal path do not clear it. On a reused instance, explicitly passing nil resets the stored evidence; merely calling an older overload does not. This is retained state behavior, not proof of backend acceptance of stale consent. no_eligible_accounts preservation and session-context event diagnostics are release-note findings because the changed event/host internals remain excluded.
6. Checkout no longer fills a new method's missing billing email from session.email before PaymentMethod creation. The no-method customerData email branch remains, as do the general confirmation guards and nil-Intent/poll-timeout completion caveat. Do not infer a global email requirement change or complete public Checkout support.
7. CryptoOnramp failed post-auth handling now passes the available PaymentIntent and error into checkoutError; the helper is excluded, so exact field preservation is announced rather than independently verified. The cumulative changelog retrospectively attributes error/decline/type preservation and uploadFile SPI to 26.12.0; do not rewrite the older raw notes or claim first implementation at that earlier SHA. Legacy StripeFile purpose conversion maps cryptoOnrampKYCDocument to unknown, not new legacy-upload support.
8. Eight podspecs are version-only changes, retaining iOS 15 and Swift 5 declarations. No standalone Apple Pay integration or general deployment-floor change is established. Availability/form factories, current Checkout controller/API/Apple Pay context, Financial Connections enforcement/event internals, generic poller/action mapping and CryptoOnramp error/upload helpers remain explicit evidence gaps. No SDK build, simulator/device, eligibility or payment testing.

### Recommendation and Next Action

Recommend **full additive ingest with the already approved release-specific focused-reading exception**, overriding the generated delta. The STP SPI PaymentSheetAuthenticationContext polling requirement changes from PaymentIntent-specific parameters to shared STPPaymentHandlerActionParams (STPPaymentHandler.swift:2761), an incompatible signature for conformers, alongside the new Pix flow and consent/confirmation behavior. Full is an additive knowledge baseline, not replacement of older knowledge and not a claim to have reread all 253 unchanged source files.

No further collection or policy expansion is needed for this bounded ingest; preserve the listed gaps. Next: obtain user approval for this concrete mode, approve only github-722f2ffc82b5d6e5375c, claim it through next-ingest, then update the existing iOS concept, cumulative source/changelog, Stripe catalog/index and logs serially. Preserve every older version and validate before completing the item. Commit/push remain separate authorization boundaries.

State remains awaiting_approval with approved_mode null. No wiki edits, ingest, staging, commit or push occurred during this review.

## Approved Ingest Receipt - 2026-10-02

The user approved the final full-additive recommendation. Approved only this work item through the existing CLI and claimed it serially; next-ingest returned this exact ID/SHA in full mode with 290 effective required-reading paths. Applied the already approved release-specific focused-reading exception and completed review reads above, not a fresh semantic read of all 253 unchanged files. Original snapshots, packet and future collection policy remain unchanged.

Concept audit: updated the existing stripe-ios-sdk and stripe-pix concepts first. Pix's web subscription guidance is explicitly distinguished from bounded native evidence; Financial Accounts disclosures is a separate domain and was left untouched. No redundant concept, cross-company comparison or contradiction entry was created: version changes are recorded as qualified history, not replacement claims.

Added five verbatim grounding excerpts with exact raw locations, the version-qualified baseline, package status, history and raw references. Updated cumulative changelog, company catalog, provider index and provider/root logs. No new source count. Preserved all previous section headings; the complete earlier 26.5.0-through-26.12.0 source knowledge block and older changelog entries are byte-identical to the pre-ingest working copy. Unrelated dirty work remains untouched.

Fresh validation before completion: six frontmatter-bearing edited wiki pages passed with no issues. Provider index and root log retain their pre-existing missing-frontmatter errors (also present at HEAD); no unrelated format migration performed. GitHub validation passed with 148 snapshots, 133 release records, 90 comparisons and 147 work items, no structural errors. git diff --check passed.

No SDK build, simulator/device, runtime payment, settlement or eligibility testing; no staging, commit or push. Next: complete this exact work item, revalidate lifecycle, then seek separate approval to review/commit the pending Stripe iOS changes without unrelated work.

Lifecycle completion: complete-ingest returned this exact work item as ingested with approved_mode full. No other work item was claimed. Next user action remains separate review/commit approval; push is not authorized.
