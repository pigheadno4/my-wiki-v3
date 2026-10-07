# Braintree C44 fixed-query audit — group A

- Scope: first four approved C44 jobs only; eight predetermined queries.
- Result: **PASS — 8/8 queries**.
- Completed UTC: `2026-10-07T12:30:02Z`

## Shared checks

- Manifest/job state: all four jobs are `approved` at attempt 1 and map to the canonical source targets audited below.
- Integrity/provenance: all four computed SHA-256 values exactly match the manifest. Each raw begins with the same canonical `Source URL` as the manifest/source frontmatter, a `Fetched: 2026-09-16` marker, and `Discovery: llms.txt,sitemap.xml`.
- Primary ownership: each exact `raw_files` path occurs in exactly one `wiki/sources/` page; each canonical URL also occurs in exactly one source page. `## Raw Sources` points to the same pinned primary raw. Related/supporting raw references do not claim primary ownership.
- Retrieval closure: `wiki/index.md:11` routes to `[[braintree-index]]`; the provider index routes to `[[paypal-fastlane]]` (`wiki/braintree-index.md:793`), `[[braintree-payment-methods]]` (`:813`), and `[[braintree-webhooks]]` (`:818`). Those concepts reciprocally list the four sources at `wiki/concepts/braintree-payment-methods.md:31,66`, `wiki/concepts/paypal-fastlane.md:99`, and `wiki/concepts/braintree-webhooks.md:22`. Direct provider-catalog source rows are absent, but this is the explicitly deferred shared-catalog close and is not a failure while the concept routes work.
- Bounded gap sweep: one filename/topic sweep covered network tokens, SEPA Direct Debit, Fastlane, reports/webhooks, and linked webhook references. No secondary raw was needed to answer the fixed queries; no unrelated fan-out was performed.

## 1. Network Tokens Overview

Source: `wiki/sources/braintree/source-braintree-docs-guides-network-tokens-overview.md`; primary raw: `raw/braintree/docs/guides/network-tokens/overview-2026-09-16.md` (`b5176ff1c0e3239e5922468794194fcae5241f0ceddfed7b4b68cb0a1d5670af`).

**Q1 — exact scope. PASS.** Braintree's unversioned **Network Tokens Overview** webpage covers ordinary Braintree Vault card tokenization versus merchant-specific network tokenization. Its objects are the card/PAN, a Braintree Vault token, and a network token; its action scope is definitional/product framing only. It names no SDK family/package/version, client/server procedure, environment, enrollment state, merchant eligibility, or executable create/refresh/payment action, so none may be inferred. Locators: source `:14-16`; raw `:1-9,14,19,22-29`.

**Q2 — purpose, action, conditions/warnings, detail route. PASS.** The page's central purpose is to explain replacement of a PAN with a merchant-specific cryptographic token: one merchant's network token cannot transact at another merchant, and the page says it can refresh in real time when a card is lost, stolen, or expires. Authorization/expense/fraud/revenue are stated benefits, not measured outcomes; the absolute “cannot be used fraudulently” wording has no supplied threat model and must not become a universal guarantee. Exact detail routes: source `:27-29`; raw `:19` (benefits), `:24` (ordinary tokenization and security wording), `:29` (merchant binding and refresh conditions).

## 2. SEPA Direct Debit Vaulting — Node route

Source: `wiki/sources/braintree/source-braintree-docs-guides-sepa-direct-debit-vaulting-node.md`; primary raw: `raw/braintree/docs/guides/sepa-direct-debit/vaulting/node-2026-09-16.md` (`c87122babc300bf4f03db0e7916a15b36b0663ed0f021a2f5aa847c0a25f0ff5`).

**Q1 — exact scope. PASS.** This is Braintree's unversioned, Node.js-routed server webpage for a customer-owned SEPA Direct Debit Vault `PaymentMethod`. It covers create from a client nonce (or create a customer plus method), later `Transaction: Sale` by `payment_method_token`, find by token, and delete by token. No exact Node package/version, Sandbox/Production environment, account enablement, or successful transaction is identified; the route must not be promoted to current package/runtime or execution proof. Locators: source `:14,18-22,31-35`; raw `:14-16,17-50,51-82,85-118`.

**Q2 — purpose, action, conditions/warnings, detail route. PASS.** The purpose is to store a customer's SEPA debit authorization as a Vault payment method for later transaction use. `find` returns a `PaymentMethod` plus a link to the associated mandate, and a missing method follows the linked not-found route. Deletion is consequential: it also revokes the associated mandate; restoration or replacement is not documented. Exact detail routes: source `:26-27,31-35`; raw `:16` (identity/ownership), `:22-50` (create and later sale), `:56-82` (find/mandate), `:90-118` (delete/not-found/mandate revocation).

## 3. Fastlane Appendix

Source: `wiki/sources/braintree/source-braintree-docs-guides-fastlane-appendix.md`; primary raw: `raw/braintree/docs/guides/fastlane/appendix-2026-09-16.md` (`49967b89dd65a3bf7422c3b1d967b13bb53bc23ffd515603cd23369290667bf9`).

**Q1 — exact scope. PASS.** This is Braintree's unversioned **Fastlane Appendix** webpage (`updateTime` 2026-08-26), not a package-qualified implementation. It names browser calls `braintree.fastlane.create()` and `triggerAuthenticationFlow()` and server `transaction.sale()`, with `paymentToken`, Fastlane profile/address data, `addressOptions`, and `authenticatedCustomerResult` in scope. It provides no exact SDK/package version, environment, merchant/payer eligibility, or hosted/runtime/payment/Vault outcome; none may be inferred. Locators: source `:14`; raw `:1-9,17-29,35-46`.

**Q2 — purpose, action, conditions/warnings, detail route. PASS.** The appendix records profile-data precedence (phone/email UI-only; billing/shipping API before UI tokenization; names derived from billing), a three-hour `paymentToken` lifetime, allowed shipping locations via initial-call `addressOptions`, and reload guidance to call `triggerAuthenticationFlow()` again; SDK logic then chooses OTP or session restoration and returns a new token. Preserve the raw's vault-ordering conflict: it first says the client token can be vaulted before a server transaction, then says vaulting is supported only through `store_in_vault_on_success` in `transaction.sale()` and explicitly rejects pre-transaction `customer`/`payment_method` creation. Exact detail routes: source `:18-24,28-32`; raw `:17-29` (priority), `:35-40` (vaulting conflict/lifetime), `:41-46` (shipping/reload authentication).

## 4. Webhook Reports — Node route

Source: `wiki/sources/braintree/source-braintree-docs-guides-reports-webhooks-node.md`; primary raw: `raw/braintree/docs/guides/reports/webhooks/node-2026-09-16.md` (`df50a6ebaf5f174c7fd1886526532666b12320718afd97a32b574d4a19f3ed7f`).

**Q1 — exact scope. PASS.** This is Braintree's unversioned, Node.js-routed webpage for merchant-built reports from webhook notifications. The account condition is explicit: the feature is available only when Braintree manages funding for the merchant account. The objects/actions are `WebhookNotification` storage, disbursement payloads and transaction IDs, destination setup, webhook parsing, and transaction search. No exact Node package/version or production delivery/report completion is proven; Sandbox appears only as a linked disbursement-exception test route. Locators: source `:14,18-22,26-30`; raw `:14-20,28-42,45-81`.

**Q2 — purpose, action, conditions/warnings, detail route. PASS.** The workflow is: configure at least one destination, parse notifications, and store selected trigger details for merchant reporting. A disbursement or disbursement-exception webhook carries the disbursement object, for which the page says no alternative gateway retrieval exists. To find associated transactions, parse incoming `bt_signature` plus `bt_payload`, take `webhookNotification.disbursement.transactionIds`, and search with `search.ids().in(...)`; callback and Promise examples are retained. Treat the named report types as examples, not guaranteed outputs. Exact detail routes: source `:18-22,26-30`; raw `:17-25` (eligibility/examples), `:28-33` (workflow), `:36-42` (unique disbursement retrieval and Sandbox route), `:45-81` (POST fields and searches).

## Query tally

| Page | Q1 exact scope | Q2 purpose/actions/conditions/detail route |
| --- | --- | --- |
| Network Tokens Overview | PASS | PASS |
| SEPA Direct Debit Vaulting (Node) | PASS | PASS |
| Fastlane Appendix | PASS | PASS |
| Webhook Reports (Node) | PASS | PASS |

Concrete uncertainty retained: only the Fastlane primary raw's internally inconsistent vault-ordering prose; the source and concept preserve it without inventing a pre-transaction vault flow. No query fails for missing material fact or insufficient raw routing.
