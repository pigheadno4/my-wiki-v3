---
title: "Nigerian Payment Methods (Stripe)"
type: concept
category: technology
tags: [stripe, nigeria, naira, local-payment-methods, merchant-of-record, wallets, bank-transfer]
---

## Definition

Stripe describes acceptance of Nigerian local methods through a **Nigerian partner as merchant of record**, without a local Nigerian entity. The November 2026 matrix lists Naira cards and one-time bank transfers; it marks Naira wallet No/No, despite overview prose mentioning local wallets. The May 2026 matrix instead said wallet one-time was “Coming soon.” Treat wallet availability as unresolved in this capture; see [[source-stripe-nigeria-payment-methods]]. This partner-MoR route is distinct from [[stripe-managed-payments]], where Stripe is MoR.

## How It Works

Customers begin checkout on Stripe's page, then are redirected to the Nigerian partner's localized checkout and their local processor. Payment happens there — Stripe acts as the conduit to the MoR partner.

- **No local entity required**: US-based Stripe accounts can accept NGN payments with USD settlement
- **3-day funding** after payment approval
- **VAT**: The MoR partner remits buyer VAT for Nigerian transactions — merchants should include VAT in presentment pricing

## Payment Methods

| Method | May 2026 one-time / recurring | November 2026 one-time / recurring |
| --- | --- | --- |
| Naira cards | Yes / Yes | Yes / Yes |
| Naira bank transfer | Yes / Coming soon | Yes / No |
| Naira wallet | Coming soon / No | No / No |

The November overview also mentions local wallets in prose; its wallet matrix says No/No. This is an unresolved within-page discrepancy, not proof of current wallet availability or a prior live withdrawal. See [[source-stripe-nigeria-payment-methods]].

## Key Properties

- **Currency**: NGN only
- **Business locations**: US only (USD settlement)
- **Recurring**: Yes (Naira cards)
- **Manual capture**: Yes
- **Connect**: Yes
- **Disputes**: Cannot challenge — funds removed immediately when PSP accepts dispute; merchant must contact customer directly
- **Refunds**: Full + partial, 365-day window; up to 7 calendar days to return status for some transactions

## Integration

The November 2026 overview includes an invite-request step. Requesting an invite or enabling a method in the Dashboard does not establish approval or account eligibility. For an eligible account, the guide routes Stripe front-end products through Dashboard payment-method settings, links Checkout/Elements and Payment Links, and points to the Payment Intents API; see [[source-stripe-nigeria-payment-methods]] for the dated access boundary.

### Naira Card (`ng_card`)

- **May 2026 Checkout compatibility** — US businesses accepting Nigerian-issued cards from Nigerian customers, all line items in `ngn`, and 500–100,000,000 NGN per Checkout transaction. The guide lists payment, setup and subscription compatibility. Both hosted and embedded samples use payment mode.
- **May 2026 selection** — Stripe evaluates dynamic method applicability. The historical manual Checkout examples add `ng_card` to `payment_method_types`. For the separate Endive request contract, see [[source-stripe-ng-card-accept-payment]].
- **May 2026 Direct API** — the server example includes amount, `ngn`, `ng_card` in `payment_method_types`, and `payment_method_data.type: 'ng_card'`. The browser sample uses the PaymentIntent client secret, `payment_method_data.type: 'ng_card'` and `return_url` in `stripe.confirmPayment`. The extra create field is example-specific.
- **Version boundary** — Checkout Session Create and PaymentIntent Create in `2026-09-30.endive` reject writable `payment_method_types` with HTTP 400 and retain their computed response properties. The documented alternatives are dynamic methods with an optional exclusion or a compatibility-filtered allowlist. For each endpoint’s changelog and the separate PaymentIntent Impact preview label, see [[source-stripe-ng-card-accept-payment#API Version Boundary — Endive Create Requests|the Naira card guide’s Endive warning]].
- **Return and verification** — the Nigerian partner handles authentication and authorization. Stripe returns `payment_intent` and `payment_intent_client_secret` for status lookup. A return or authentication alone does not verify payment. The guide recommends `payment_intent.succeeded` events for post-payment actions.
- **Sandbox tests** — simulated authorization moves `requires_action` to `succeeded`, and a simulated failure moves it to `requires_payment_method`. Live payment and payout are separate outcomes.

### Naira Card — Save / Recurring (`ng_card`)

The May 8, 2026 guide describes written opt-in for future use, including off-session terms where applicable. Its Checkout setup branch also requires the customer's authorization of the local merchant-of-record provider for future payments. See [[source-stripe-ng-card-set-up-future-payments]].

- **Checkout setup**: The May example creates a setup-mode Session for the Stripe Customer. In the successful test, authentication moves the SetupIntent from `requires_action` to `succeeded`.
- **Direct API**: May's no-charge setup creates a Customer-linked SetupIntent and shows browser `stripe.confirmNgCardSetup()` with online `infer_from_client`. Stripe.js handles authorization navigation and the May guide uses `return_url` after SetupIntent success. Verify setup status separately from browser return and the outcome of any later payment. Its separate PaymentIntent charge-and-save example uses `setup_future_usage=off_session` and shows explicit IP address and user agent when supplying optional `mandate_data`. The November Billing subscription sample also shows explicit IP and user agent on a server-confirmed SetupIntent. Written permission remains separate from those API fields.
- **Standalone manual redirect**: May's standalone PaymentIntent payment example shows no future-use attachment. Redirect only for `requires_action` plus `next_action.type=redirect_to_url`. Use server webhooks to verify payment status after browser return.
- **Reuse and detach**: Confirm a new PaymentIntent for the Customer and saved PaymentMethod, with `off_session=true` when the customer is absent. Server detach deactivates the saved method and sends `mandate.updated` and `payment_method.detached`.

The May requests with writable `payment_method_types` are historical. The November-captured Endive changelogs warn of HTTP 400 at their linked `2026-09-30.endive` Checkout Session Create, SetupIntent Create and PaymentIntent Create endpoints while preserving readable response properties. The Intent changelog's Impact section names `2026-08-26.preview` separately. The November Naira setup index links two variants and supplies no migrated flow. See [[source-stripe-ng-card-set-up-future-payments#API version boundary for the May requests]].

### Naira Bank Transfer (`ng_bank_transfer`)

- **Checkout (May 2026)**: US businesses, 500–100,000,000 NGN, all line items in NGN and payment mode only. Use dynamic selection or the historical `ng_bank_transfer` list. The hosted example uses `success_url`; the embedded example uses `return_url` and `ui_mode: embedded_page`.
- **Direct API (May 2026)**: The server creates an NGN PaymentIntent and passes its client secret to the browser. The creation example includes `payment_method_data.type`; the stated creation prerequisites list amount, currency and the historical method list. Browser `stripe.confirmPayment` uses the transfer type and `return_url`. The return identifiers let the merchant verify Intent status, and business actions follow verified `payment_intent.succeeded`. Test-key transitions describe sandbox outcomes.
- **API version**: The separate Endive changelogs remove writable `payment_method_types` in the documented `2026-09-30.endive` Checkout Session create and PaymentIntent create/update/confirm endpoints. Dynamic methods and compatibility filters are distinct from the computed response property. See [[source-stripe-ng-bank-transfer-accept-payment]] for the endpoint version, example defect, test paths and November navigation boundary.
- **Access and recurring**: The country overview's May “Coming soon” recurring cell is historical. The November bank-transfer row is Yes for one-time and No for recurring; the preview invite request leaves approval unverified. See [[source-stripe-nigeria-payment-methods]].

## Sources

- [[source-stripe-local-payment-methods-by-country]] — hub page: Nigeria + South Korea local payment methods
- [[source-stripe-nigeria-payment-methods]] — May and November 2026 Nigeria partner-MoR overview: card/bank-transfer matrix, unresolved wallet prose versus No/No table, invite request, conditional VAT, disputes and refunds
- [[source-stripe-ng-bank-transfer-accept-payment]] — May Naira bank-transfer Checkout and Direct API guide, including dated request fields, Endive warning and verification after partner redirect. The November capture is variant navigation.
- [[source-stripe-ng-card-accept-payment]] — May 2026 Checkout and Direct API guide, November variant index and separate Endive Create request warning.
- [[source-stripe-ng-card-set-up-future-payments]] — Naira card save/recurring: SetupIntent + confirmNgCardSetup(), PaymentIntent setup_future_usage, off_session reuse, detach events
