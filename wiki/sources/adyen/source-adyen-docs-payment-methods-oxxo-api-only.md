---
title: "OXXO API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/oxxo/api-only"
raw_files:
  - "adyen/docs/payment-methods/oxxo/api-only/2026-09-15.md"
tags: [adyen, oxxo, mexico, api-only, voucher]
---

## Overview

This 2026-09-15-captured Adyen guide adds **OXXO to an existing API-only integration**. It covers MX/MXN payment-method discovery, voucher action presentation, and the delayed offer-to-sale transition reported through webhooks. Voucher creation is an open offer, not a paid transaction. See [[adyen]], [[adyen-online-payments]], and the method overview [[source-adyen-docs-payment-methods-oxxo]] for the Mexican cash-voucher journey, unpaid expiry, and capability matrix.

## Key takeaways

- The guide requires an existing API-only Advanced flow, handling of `action.type: voucher`, and OXXO added in Customer Area (raw lines 23–29). The shopper selects OXXO, receives a voucher, then uses it in-store to finalize payment (raw lines 31–36).
- To discover OXXO through `/paymentMethods`, specify `countryCode: MX` and `amount.currency: MXN`. The sample response uses method `type: oxxo`; the request example is a **test** endpoint with placeholder credentials and a sample amount, not proof of present merchant availability (raw lines 46–85).
- The payment form section says no shopper information needs to be collected. The `/payments` section says no OXXO-specific additional parameters are needed, and its response contains a **voucher** action that must be shown to the shopper (raw lines 38–44, 87–91).
- **Source conflict:** the `## How it works` list says the payment request includes additional information about the items the shopper intends to purchase, but `## Add additional parameters to your /payments request` explicitly says no additional parameters are needed (raw lines 31–36 versus 87–91). The first list also says the shopper enters details in a payment form, while the form section says no information needs collection (raw lines 34 and 42). The captured guide does not resolve these statements; do not invent an item-field or shopper-detail requirement from the list.
- OXXO is offline. Creating the voucher produces an **Open** offer in Customer Area; method-specific **PENDING** webhooks are available if configured. After the shopper pays in-store, the offer becomes a sale with **Received** status, and the final result arrives via an **AUTHORISATION** webhook (raw lines 93–101). Payment is not established by voucher presentation or the pending webhook.
- In **test**, the page simulates payment by manually promoting the pending offer to a sale in test Customer Area; paid vouchers appear in **Payments > Payment list** and reconciliation should be tested. Live acceptance requires submitting an OXXO method request in live Customer Area (raw lines 103–114). The shown `/paymentMethods` curl example omits a line continuation after `-X POST` before `-d`, so it should not be copied as a complete shell command without checking syntax (raw lines 57–72).

> [!warning] Conflicting request-field guidance
> The high-level flow says to include item information and enter shopper details (raw lines 34–35), while the dedicated form and `/payments` sections say no shopper information or extra OXXO fields are needed (raw lines 42, 89). Treat the specific requirements as the guide's API instruction and verify any item-data need in the applicable API contract before implementation.

## Detail locators

- API-only, voucher-action and Customer Area prerequisites: raw `## Requirements`, lines 23–29.
- Shopper flow and internal field conflict: raw `## How it works` lines 31–36; `## Build your payment form` lines 38–44; `## Add additional parameters to your /payments request` lines 87–91.
- MX/MXN discovery and sample curl/response: raw lines 46–85.
- Offline status, webhook finality, test promotion and live request: raw `## Test and go live`, lines 93–114.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-oxxo]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/oxxo/api-only/2026-09-15|OXXO API-only guide, captured 2026-09-15]]
