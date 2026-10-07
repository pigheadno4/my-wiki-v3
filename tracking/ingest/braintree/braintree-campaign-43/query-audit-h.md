# Braintree C43 query audit H — positions 29–32

- Audit start (UTC): `2026-10-07T11:45:57Z`
- Audit end (UTC): `2026-10-07T11:46:58Z`
- Result: **PASS 8/8**, first pass
- Corrections: none
- Repository changes: none; this report is the only write

## Shared evidence and routing checks

- Exact allocation confirmed at `tracking/ingest/braintree/braintree-campaign-43/selection-review.md:55-58,89`; the predetermined question wording is at lines 95-96.
- Manifest pins are at `tracking/ingest/braintree/braintree-campaign-43/manifest.json:269-305`. Recalculated SHA-256 values match all four pins:
  - Masterpass: `0d1fb939534c9194af9fde96a1449516f328ce24fd61ac9696e2c3b026783c41`
  - PayPal Commerce iOS: `509c2bf61072c37c66d03c55037cbfe0decc8c9e39d8fc2b3ec9c81cb27519da`
  - Disputes: `f6f2c1739b8a2904ee7063fbe9ad895a7c293c053b698ec2eee70a053819e951`
  - PINless ODR: `ede7798e520c57e223c3ea38ecd7b7b7a3028605de204487ac70c699c611f8d0`
- Manifest-wide uniqueness check: 50 jobs, 50 unique raw paths, 50 unique hashes, 50 unique source targets, and 50 unique canonical URLs.
- Each selected raw pin and canonical URL resolves to exactly one source file under `wiki/sources/`; each source has one factual `raw_files` pin and a reciprocal `## Raw Sources` link.
- Actual route is valid: root `wiki/index.md:11` → provider `wiki/braintree-index.md` → main concepts at provider lines 760 (`braintree-payment-methods`), 772 (`braintree-ios-sdk`), and 778 (`disputes`) → reciprocal source entries at `wiki/concepts/braintree-payment-methods.md:32,34`, `wiki/concepts/braintree-ios-sdk.md:90`, and `wiki/concepts/disputes.md:335` → canonical source → pinned raw.
- The four direct source rows are not yet in `wiki/braintree-index.md` or `wiki/companies/braintree.md`; per the campaign contract this is deferred shared close work, not a content failure.
- Bounded gap sweep retained only claim-relevant supporting authority: the Masterpass/SRC conflict was fully checked against `wiki/sources/braintree/source-braintree-payment-methods-secure-remote-commerce.md` and its pinned raw, especially raw lines 14-15 and 21-48. Companion setup/client pages, dispute workflow/support routes, PINless code samples/response-code material, and other nearby raws remained navigation-only because no audited answer relies on their content.

## Position 29 — Masterpass server-side Node

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-methods]]` → `[[source-braintree-docs-guides-masterpass-server-side-node]]` → `[[raw/braintree/docs/guides/masterpass/server-side/node-2026-09-16]]`.

### Q57 — established scope and non-inferences — PASS

Braintree's captured, unversioned historical Masterpass **server-side Node.js route** covers transaction requests made from a client-produced payment-method nonce plus client-collected device data, and approval-gated Vault storage for recurring use. It does not identify an exact Node package/version or environment. Do not infer current Masterpass or SRC availability, merchant approval/eligibility, client-side nonce or device-data behavior, exact SDK/runtime behavior, a safe executable SRC migration, or successful vaulting, authorization, submission, settlement, or funding. Evidence: source lines 14-17, 27-30, 43-50; raw lines 17-24, 63-71, 91-99; SRC support conflict authority raw lines 14-15 and 21-48.

### Q58 — central purpose, conditions, warnings, and detail retrieval — PASS

The page's central action is to submit a Masterpass nonce transaction with `gateway.transaction.sale()`; its examples include amount, nonce, device data, and `submitForSettlement: true` (raw 21-61). Vaulting is recurring-only and requires Masterpass approval; without approval the documented error is `Nonce is not vaultable.` Storage routes through `gateway.paymentMethod.create()` or transaction-time Vault options, while vaulted Masterpass excludes split shipments and one-off transactions (raw 63-95). Gateway card verification is unsupported; the page says the wallet verifies the card (raw 96-99). The source preserves the consequential conditions and routes routine syntax/options to exact raw locators without claiming runnable code or payment outcome proof (source 21-39).

## Position 30 — PayPal Commerce iOS overview

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-ios-sdk]]` → `[[source-braintree-docs-guides-paypal-commerce-ios-overview]]` → `[[raw/braintree/docs/guides/paypal-commerce-ios/overview-2026-09-16]]`.

### Q59 — established scope and non-inferences — PASS

This is a Braintree-hosted overview of the historical **PayPal Commerce iOS SDK**, not the modern modular `braintree-ios` SDK or ordinary Braintree checkout/Drop-in. It is labeled closed beta, is unversioned, names no exact package/commit or runtime environment, and records historical iOS 8.0–10.0/device requirements. Do not infer current beta access, merchant/buyer eligibility, enablement, exact-package compatibility, runtime behavior, or successful payment processing. Evidence: source lines 14-16, 23-24, 38-44; raw lines 17-18, 25-29, 36-39, 62-64.

### Q60 — central purpose, conditions, warnings, and detail retrieval — PASS

The central purpose is a PayPal Commerce-powered mobile store offered as a standalone app, embedded modally or more deeply in an existing app, or as embedded products/buy buttons (raw 20-32). Merchants connect an ecommerce platform; the historical snapshot names Magento, Bigcommerce, and Demandware. PayPal Commerce Panel manages stores, credentials, and backends, while the merchant continues product, inventory, order-processing, and fulfillment work in its ecommerce platform (raw 23-35). Closed-beta access, historical requirements, advertised features, live-store examples, and repository/release routes remain precisely locatable at raw 17-18, 36-51, and 54-64; none is treated as current/runtime/payment proof (source 20-34).

## Position 31 — disputes overview

Route: `[[index]]` → `[[braintree-index]]` → `[[disputes]]` → `[[source-braintree-docs-guides-disputes-overview]]` → `[[raw/braintree/docs/guides/disputes/overview-2026-09-16]]`.

### Q61 — established scope and non-inferences — PASS

This unversioned Braintree webpage covers API dispute management only for merchant accounts already able to access disputes in the Braintree Control Panel. Its objects are chargebacks, retrievals, and pre-arbitrations; its page-level actions are find/search, status check, evidence submission, and acceptance. It states no SDK family/version or runtime environment. Do not infer current merchant eligibility, successful API execution, evidence acceptance, a bank decision, settlement, or recovered funds. Evidence: source lines 14, 18-22, 34-44; raw lines 16-27 and 47-57.

### Q62 — central purpose, conditions, warnings, and detail retrieval — PASS

The central flow is merchant review and an accept-or-respond decision: acceptance ends the merchant flow; response adds text/file evidence and requires finalization before Braintree sends it to the cardholder's bank (raw 30-40). Account setup controls eligibility; merchants using another chargeback process cannot use this API route, and an unsupported implementation may cause a missed recovery opportunity (raw 47-57). The source keeps exact actions and warnings at raw locators (source 18-30). The support-article and next-page API routes remain explicitly unread navigation, not evidence (source 38-40).

## Position 32 — PINless Debit optimized routing integration

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-methods]]` → `[[source-braintree-docs-guides-pinless-debit-optimized-debit-routing-integration]]` → `[[raw/braintree/docs/guides/pinless-debit/optimized-debit-routing/integration-2026-09-16]]`.

### Q63 — established scope and non-inferences — PASS

This unversioned Braintree website integration page covers merchant enablement of PINless Debit Optimized Debit Routing, routed-network visibility, NTI behavior for stored credentials, and the split between Braintree Vault and external-vault/orchestration merchants. Base enablement requires contacting PayPal and is distinct from the SDK/version floor for seeing the routed low-cost network without waiting for a report: GraphQL latest, Java `>=3.32.0`, Ruby `>=4.18.0`, Node.js `>=3.21.0`, PHP `>=6.17.0`, .NET `>=5.24.0`, Python `>=4.26.0` (raw 20-32). No environment is established. Do not infer current availability, merchant eligibility/enablement, installed-package/runtime behavior, authorization success, payment execution, settlement, or funding. Evidence: source lines 14, 18-22, 34-40.

### Q64 — central purpose, conditions, warnings, and detail retrieval — PASS

The page says basic PINless enablement requires no integration modification, but immediate routed-network visibility requires the listed versions (raw 20-32). It defines a network-generated NTI as a signature-network CoF value; PINless networks do not participate in CoF or issue such NTIs, so a successful PINless authorization may lack one (raw 35-43). A later section nevertheless says Braintree returns an NTI value for PINless transactions subject to network/CoF rules (raw 46-57); the source correctly retains this unresolved network-generated-versus-Braintree-returned distinction rather than guaranteeing population. Braintree Vault merchants need no change; external-vault merchants must pass the original CIT NTI in `previous_network_transaction_id` for linked recurring transactions where applicable (raw 60-68). Routine procedures and code-sample routes remain raw navigation, not runnable-code obligations (source 18-30).

## Closure

- First-pass result: `Q57 PASS`, `Q58 PASS`, `Q59 PASS`, `Q60 PASS`, `Q61 PASS`, `Q62 PASS`, `Q63 PASS`, `Q64 PASS`.
- Material content failures: none.
- Corrections/rechecks: none.
- Deferred catalog edges: provider/company direct rows only; close-stage work, not a query failure.
