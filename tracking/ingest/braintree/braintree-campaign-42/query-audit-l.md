# Braintree campaign 42 query audit L

- Scope: manifest entries 45–48 only; exactly two questions per canonical source page.
- UTC start: `2026-10-07T01:21:31Z`
- UTC end: `2026-10-07T01:22:54Z`
- Overall verdict: **PASS — 8/8 queries passed.**
- Extra authority reads: none.

## Shared checks

All four pinned raw files were read in full. Their computed SHA-256 values exactly match the campaign manifest: `1703115f…8989`, `65a367c…aa9`, `fcad7616…da36`, and `55abe90c…587a`. Answers below stay within each assigned Braintree website snapshot and its canonical source page; they make no current-state, sibling-page, GitHub, provider-wide, account-eligibility, or successful-execution inference.

The required main-concept reciprocity exists now for every page. New company-page work and the provider source-catalog additions are deferred closeout concerns, not per-page content failures. Damaged captured prose or illustrative request/result syntax is nonblocking where the source preserves the gap and does not turn an example into a runnable or successful-operation guarantee. No source-to-raw material conflict was found; the bounded capture gaps are called out below.

## Manifest 45 — PayPal Order payment method with payee email

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:729` → `wiki/concepts/paypal-braintree-integration.md:54` → `wiki/sources/braintree/source-braintree-docs-reference-general-paypal-advanced-options-paypal-order-payee-email-node.md:12-40` → `raw/braintree/docs/reference/general/paypal-advanced-options/paypal-order/payee-email/node-2026-09-16.md`.

1. **PASS — What is the central action and who may receive the funds?** In this captured Braintree-hosted Node.js PayPal Order reference, the merchant places `payeeEmail` under `options.paypal` while creating or updating a customer payment method. Transactions against that payment method route all funds to the specified PayPal account, which must be owned by the merchant; the PayPal account linked in the Braintree Control Panel does not see those transactions or reporting. This is request-shape and snapshot evidence, not proof of configuration, eligibility, or successful execution. Evidence: source `Overview`, `Key takeaways`, and `Detail locators`; raw lines 14–38, 42–123.

2. **PASS — Does `payee_email` select currency, and what are the refund/reporting conditions?** No. The snapshot separately requires a currency-configured Braintree item and a `merchant_account_id` with PayPal payments enabled, but the captured noun after “Braintree” is missing and must not be reconstructed. Receiving accounts may need additional configuration. Refunds omit `payee_email` and draw from the PayPal account that received the original transaction; `payee_email` is absent from Control Panel transaction reporting, with a unique `merchant_account_id` offered for separate reporting. Evidence: source `Key takeaways` and `Detail locators`; raw lines 125–147.

## Manifest 46 — PayPal transaction-sale payee advanced options

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:729` → `wiki/concepts/paypal-braintree-integration.md:133` → `wiki/sources/braintree/source-braintree-docs-reference-general-paypal-advanced-options-payee-node.md:12-42` → `raw/braintree/docs/reference/general/paypal-advanced-options/payee/node-2026-09-16.md`.

3. **PASS — How does this Node-routed website reference dynamically change the receiving account?** A PayPal `gateway.transaction.sale` request may carry `payeeId` or `payeeEmail` under `options.paypal`; either routes the transaction funds to a different merchant-owned PayPal account and removes that transaction from the linked Control Panel PayPal account’s account/reporting view. The page describes `payee_id` as preferable because the Merchant account ID cannot be changed, while `payee_email` uses the receiving account email. Evidence: source `Overview`, `Key takeaways`, and `Detail locators`; raw lines 14–60, 61–128.

4. **PASS — What material setup, currency, refund, reporting, and damaged-note boundaries apply?** Receiving PayPal accounts may need additional configuration. Neither payee field selects currency; use a currency-configured Braintree `merchant_account_id` with PayPal payments enabled. Refunds use the ordinary Braintree path and withdraw from the original receiving PayPal account. Neither payee field appears in Control Panel transaction reporting; separate reporting is routed to unique `merchant_account_id` values. The restriction note at raw line 92 has missing identifiers, so its parameter/method restrictions cannot be recovered from this snapshot. Evidence: source `Key takeaways` and `Detail locators`; raw lines 91–99, 130–184.

## Manifest 47 — Venmo server-side Node guide

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:707` → `wiki/concepts/braintree-payment-methods.md:25` → `wiki/sources/braintree/source-braintree-docs-guides-venmo-server-side-node.md:12-61` → `raw/braintree/docs/guides/venmo/server-side/node-2026-09-16.md`.

5. **PASS — How is a Venmo account vaulted, and what are the deletion consequences?** This unversioned Braintree website guide uses the client-supplied nonce with `gateway.paymentMethod.create()` and a customer ID. Deleting the vaulted method also deletes the Venmo merchant connection, except that duplicate vaulted methods postpone connection deletion until the last is removed; customer-side revocation removes the method from the merchant Vault and is routed to `PaymentMethodRevokedByCustomer`. The transaction-time vaulting sentence is damaged, so the missing option names and conditions are not asserted. Evidence: source `Key takeaways`, `Material boundaries`, and `Detail locators`; raw lines 21–44, 115–119.

6. **PASS — What is required for transaction creation and a non-default business profile, and how narrow is the retry instruction?** The shown `gateway.transaction.sale()` request uses a client nonce, `submitForSettlement: true`, and client-collected device data; the page limits the device-data requirement to transaction creation. A non-default Venmo business profile requires the same profile ID used during client tokenization, while omission selects the default profile. Multiple partial capture is navigation only. In production, only the documented inability to obtain the transactable token yields `token_issuance` and the page-directed retry; this is not a general retry policy or proof of authorization, settlement, or funding. Evidence: source `Key takeaways`, `Material boundaries`, and `Detail locators`; raw lines 47–75, 78–112, 122–132.

## Manifest 48 — In-Person Configure Sandbox

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:685` → `wiki/concepts/braintree-in-person.md:14` → `wiki/sources/braintree/source-braintree-in-person-get-started-1-configure-sandbox.md:12-61` → `raw/braintree/in-person/get-started-1/configure-sandbox-2026-09-16.md`.

7. **PASS — What must be understood before preparing the Dev Kit P400 Sandbox account?** This unversioned Braintree In-Person website guide recommends preparing the Sandbox account before the kit arrives. The Dev Kit P400 is designed for one Braintree Sandbox account and, after pairing, cannot be used with another; the captured guide limits the kit to United States Sandbox accounts. These statements are setup conditions, not proof of current availability, eligibility, pairing, reader-online state, or production enablement. Evidence: source `Overview`, `Key takeaways`, `Material warnings`, and `Detail locators`; raw lines 14–26.

8. **PASS — What does the authentication/connectivity sequence establish, and what remains only routed detail?** The merchant or its integrator chooses an authentication approach; static first-party Public/Private API keys are described as the fastest option, not the only one. The Postman sequence maps the Sandbox public key to Basic Auth username and private key to password, then makes a first GraphQL request to check connectivity. Custom fields are optional. Transaction creation, reversal/refund, and search are only linked exercises whose operational detail belongs to unread authorities, so this page does not prove any payment, refund, search, settlement, or funding outcome. Evidence: source `Key takeaways`, `Material warnings`, `Detail locators`, and navigation labels; raw lines 29–65.
