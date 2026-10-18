---
title: "Adyen for Platforms in-person configuration-based surcharge"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/in-person-payments/surcharge/configuration"
raw_files:
  - "adyen/docs/platforms/in-person-payments/surcharge/configuration/2026-09-15.md"
tags: [adyen, platforms, in-person-payments, surcharge, terminal-api]
---

## Overview

This 2026-09-15 Adyen for Platforms guide explains automatic configuration-based surcharges for in-person payments and, separately, how a platform can request booking of the calculated surcharge to one of its user's balance accounts. Management API rules can be set for a company or merchant account, store, or terminal. A terminal or Mobile SDK calculates the surcharge after card presentation; the ordinary payment request needs no special surcharge trigger. A Terminal API payment request can carry a `Surcharge` split item for allocation. This is distinct from a merchant-calculated dynamic surcharge and the online API-only card surcharge pilot. The snapshot describes configuration and requests, not current legal permission, account enablement, completed booking or payout.

## Key takeaways

- The guide adds to the general Platforms in-person and surcharge requirements. It lists Terminal API with payment terminals or Tap to Pay Mobile, plus standalone solutions, while excluding SFO1 terminals and NYC1 Mobile readers. Configuration needs an API key with Management API Terminal settings read and read/write roles. For payment terminals, software v1.108 enables per-transaction caps, v1.112 commercial/consumer distinction, v1.115 tip exclusion, and v1.117 MOTO/MKE application. Live terminal-settings Management API endpoints are rate-limited. Tap to Pay surcharge use requires Adyen Support-enabled single tap. These snapshot prerequisites do not prove device, account, or live eligibility.
- GET and PATCH `/terminalSettings` at company, merchant, store, or terminal level. Rules must account for applicable compliance requirements and brand, funding source, issuer country and currency. Each `configurations` item requires a brand and currency entry with `currencyCode` plus percentage and/or fixed amount; fixed amount and cap are in minor units. Optional `sources`, `country`, and `commercial` narrow a match. The first matching configuration executes, so order matters. The commercial-card check is unsupported on Mobile devices and on payment terminals when offline; a rule relying on it cannot be assumed to enforce a consumer-card prohibition in those conditions.
- Rules can combine fixed and percentage surcharge, cap the amount, exclude tips, and ask for terminal confirmation. The confirmation screen depends on configuration and solution; Tap to Pay has no surcharge confirmation screen. In Mobile or when confirmation is skipped, the guide requires another form of disclosure. The configured surcharge is calculated after card presentation, and the payment response reports it in `TotalFeesAmount`; this field is not settlement evidence. Adyen recommends Standard webhooks with surcharge amount in AUTHORISATION messages.
- For a Terminal API payment, the guide's booking route adds one `Surcharge` item, increments `split.nrOfItems`, and sets `split.item[...].account` to one of the user's balance account IDs; it says the surcharge cannot be divided among multiple balance accounts. Because the amount is calculated after card presentation, the split omits a surcharge item amount and excludes it from `split.totalAmount`. Send the form-encoded or Base64 JSON split instructions in `PaymentRequest.SaleData.SaleToAcquirerData`. The payment response describes `TotalFeesAmount`, `AuthorizedAmount`, `posAuthAmountValue` and `surchargeAmount`; request and response examples are illustrative, not proof of booking or payout. The printed Base64 example contains a currency value that differs from the adjacent USD JSON example, so do not treat that encoded blob as an authoritative payload.
- From terminal software v1.117, configured surcharges also apply to MOTO and MKE payments. Existing custom MOTO/MKE surcharging may therefore charge twice. The guide says an opt-out can be set at company, merchant, store or terminal level through an Adyen account manager or technical contact. Configuration-based surcharge may be combined with dynamic surcharge depending on use case; this page does not specify their precedence.

## Detail locators

- `Requirements` — integration and device support, software gates, credential roles, webhook recommendation, live API rate limits and Tap to Pay single tap.
- `How it works` — card-present calculation, conditional confirmation, alternative disclosure and response field.
- `Configure surcharges` — GET/PATCH scope, rule dimensions, first-match precedence, currency and minor-unit fields, offline/Mobile commercial-card limit; the country table and request body are examples.
- `Book the surcharge to your user` — one user balance account, `Surcharge` split item, amount omission, both encoding formats, `SaleToAcquirerData` and response locators. The Base64 string at line 328 encodes `split.currencyCode` as EUR while the adjacent JSON and prose use USD.
- `Opting out for MOTO and MKE` — v1.117 coverage, double-surcharge risk and Adyen-contact opt-out route.

## Related

- Company: [[adyen]]
- Concepts: [[adyen-platforms]], [[adyen-surcharging]]
- Related source: [[source-adyen-docs-platforms-in-person-payments-split-transactions-split-payments-at-authorization]]

## Raw Sources

- [[raw/adyen/docs/platforms/in-person-payments/surcharge/configuration/2026-09-15|2026-09-15 Platforms in-person surcharge configuration guide]]
