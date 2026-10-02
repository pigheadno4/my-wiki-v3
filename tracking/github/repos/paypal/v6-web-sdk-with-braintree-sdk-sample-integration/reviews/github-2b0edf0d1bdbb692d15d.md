# PayPal V6 Braintree Sample Collection Review

- Date: 2026-10-02. Work item: github-2b0edf0d1bdbb692d15d.
- Prior accepted SHA: f1c712374f674ce6f0b2683f105871dcb969d2d7. Current SHA: 06bc2de96264a29f33ff7b6eb0d566c1cd162b0a, commit date 2026-10-01.
- Collection contains 68 retained snapshot files and an explicitly approved two-file supplement. Both supplemental frontend files and their manifest were read completely. Backend GraphQL/auth/transaction handlers and affected route/server/customer/error context were read; complete scoped comparison patch and cumulative source/changelog context reviewed. This is a collection/mode review, not completion of full-mode assigned reading or wiki ingest.
- The supplement is immutable and linked through the canonical work-item evidence attachment. Snapshot and future collection policy remain unchanged. Work item remains awaiting_approval.

## Integration Findings

1. The saved-payment page loads Braintree Web 3.146.0, with the saved-payment custom element present before SDK loading. It requests a client token using a vault token or customer ID, creates fresh Braintree client/paypalCheckoutV6 instances, calls loadPayPalSDK, and creates an edit session with amount/currency, authorize intent and commit false.
2. The server gives an explicit preferred token precedence over customer lookup. Customer lookup selects the default vaulted PayPal account or the first account. The GraphQL helper maps the resolved token to input.clientToken.paymentMethodId; credentials remain server-side in this sample, unlike browser-only SDK story tooling. This sample's direct API request is not live API acceptance proof.
3. Clicking the saved-payment element starts the edit session with auto presentation. Approval is tokenized from orderId/payerId into a nonce. Submit Order sends that nonce when present, otherwise the retained vault token. The transaction route requires exactly one truthy nonce/token and requests submitForSettlement. Tokenization and submission do not prove settlement or a durable change to the default vaulted funding instrument.
4. The basic billing-agreement page now displays customerId and vaultId for the new example. This is debugging/demo output, not production identity management. Existing React helpers still submit nonces and request ordinary client tokens; the new static example does not establish a dedicated React edit wrapper or a PayPal JS package update.

## Production Caveats

- The server routes accept browser-supplied customer IDs and vault tokens without authenticated ownership checks in the retained server/route wiring. Production must resolve permitted payment methods from authenticated server-side buyer identity, not copy these inputs as an authorization boundary.
- Client amount remains fixed/browser-supplied demonstration data. Rebuild trusted order totals server-side and persist authoritative transaction state/idempotency.
- The frontend fetch helpers do not check HTTP status, and its submit handler unconditionally displays captured/success wording after JSON completion without checking transactionResult.success or transaction state. The label is not evidence of authorization, capture or settlement. Avoid raw payload/token/error display in production.
- The submit button is disabled only during its fetch, not while editing. Setup resets the approved nonce, but cancellation/error callbacks do not clear a previous approval. No teardown or durable edit-result reconciliation is demonstrated. These are code-review caveats, not reproduced browser defects.
- No build, SDK test, browser, wallet runtime or payment request executed. No merchant/region eligibility claim derived from the sample. Independent Braintree Web 3.146.0 source already documents the adapter; repository histories remain separate.

## Grounding

- app.js: `editPaypalCheckoutV6Instance.createEditSavedPaymentSession({`
- app.js: `intent: "authorize",` and `commit: false,`
- app.js: `? { paymentMethodNonce: approvedNonce }` and `: { paymentMethodToken: vaultConfig.vaultId },`
- index.html: `src="https://js.braintreegateway.com/web/3.146.0/js/paypal-checkout-v6.min.js"`

These excerpts are in raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/supplements/2026-10-02-06bc2de-9592883c/files/client/paypalEditSavedPayment/src/.

## Recommended Next Step

Additive full ingest is appropriate for the server authentication/payment-flow change, keeping all older commit knowledge. Recommend a one-item focused-reading exception: fully read all changed retained files, both supplements and affected prior/dependency context; mechanically verify unchanged files and manifest inventories. Do not approve or claim until the user authorizes that ingest scope. No wiki edit, commit or push performed during this review.

## Approved Ingest Receipt - 2026-10-02

The user subsequently approved additive full ingest and the one-item focused-reading exception. The collection-review status and recommendation above are historical, superseded by this approved ingest.

- Claimed this exact work item in full mode; no other item started. Effective packet inventory: 143 existing paths. Fully read all eight changed/newly retained files, both saved-payment frontend files, affected prior auth/transaction/billing/navigation context, current React/server dependencies and route/customer/error wiring, and cumulative source/changelog/concept context. Read the complete selected comparison patch. Unchanged source and manifest inventories were checked mechanically, not claimed as full rereads.
- SHA-256 and size checks passed for all 64 prior and 68 current snapshot files, all three prior linked supplement files and both current supplement files. Also checked the older duplicate two-file supplement without adopting it as new evidence. Sixty snapshot paths are unchanged. Three newly retained files match the prior linked supplement exactly; five selected upstream patch paths carry actual changes.
- Packet Markdown/snapshot hashes, comparison Markdown/patch hashes, attachment SHA/repository identity and both attachment file hashes passed. All packet paths exist; new source/changelog Markdown evidence links resolve.
- Concept audit/update completed before cumulative source edits. Added exact-commit saved-payment integration and illustrative JavaScript; preserved old baseline content mechanically, including the complete earlier changelog section. Updated existing company/provider catalog entries and logs; no new comparison page or registry policy change.
- Mirrored the unchecked captured-label contradiction in source and concept; distinguished static Braintree 3.146.0 from unchanged React 3.142.0 and independent PayPal JS package history. No eligibility, durable vault mutation or successful payment claim follows.
- `validate_wiki.py`: five frontmatter pages passed. `validate_github_collection.py`: 150 snapshots, 134 release records, 92 comparisons, 149 work items; no structural errors. `git diff --check` passed.
- Existing PayPal company metadata remains source_count 177; its source catalog has 183 unique bullet entries both before and after this change. No source was added or removed here. This pre-existing count discrepancy is recorded for separate reconciliation, not silently presented as a validated count.
- `complete-ingest` succeeded: this exact work item is now `ingested`. No build, runtime, sandbox/payment test, commit or push performed. Unrelated session edits remain untouched. Next: review and commit this bounded update after explicit approval.
- Post-completion validation caught a missing root-qualified comparison JSON reference in the changelog (the navigable Markdown comparison link was already present). Added the exact comparison manifest reference; no raw evidence or implementation claim changed.
