---
title: "Dynamic Currency Conversion for Adyen for Platforms in-person payments | Adyen Docs"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/in-person-payments/dynamic-currency-conversion"
raw_files:
  - "adyen/docs/platforms/in-person-payments/dynamic-currency-conversion/2026-09-15.md"
tags: [adyen, platforms, in-person-payments, dynamic-currency-conversion, terminal-api]
---

## Overview

Adyen's Adyen for Platforms in-person Dynamic Currency Conversion (DCC) guide describes a terminal choice for an eligible user's customer between local/settlement currency and the card's billing currency. If the customer accepts the billing-currency option, Adyen applies conversion and a markup; declining continues in local currency. This is a 2026-09-15 webpage snapshot whose metadata says last modified 2026-08-10. The Platforms feature is described as a pilot with limited availability and changing processes/documentation. [[adyen]] [[adyen-platforms]] [[adyen-currencies-and-fx]]

## Key takeaways

- The page requires an Adyen for Platforms in-person setup using Terminal API with payment terminals or standalone terminals. It calls for an account-manager-signed DCC addendum with an agreed markup rate, scheme-rule compliance, and enablement in Customer Area or via Management API terminal settings. For API enablement the credential needs the Management API—Terminal settings read and write role; Customer Area and reporting each have specified POS roles. Check the Visa/Mastercard/Maestro configured currencies for `ANY`; Support enables DCC reporting per merchant account and optionally pre-authorization/authorization-adjustment DCC. The guide says DCC is certified for Visa, Mastercard and Maestro, while its later supported-card list also includes VPay; treat that discrepancy and its dated currency/region lists as eligibility requiring account-level confirmation.
- The terminal must give the cardholder a real choice and disclose exchange rate and markup. Scheme requirements in the snapshot prohibit forcing DCC. An integration-defined receipt must show the rate, rate source, markup, billing-currency amount, local-currency amount and acceptance statement. For DCC with pre-authorization/authorization adjustment, the guide calls for standard webhooks and final `CAPTURE` details on receipt or invoice. It forbids combining surcharge and DCC on one transaction and does not support DCC for offline POS.
- After Adyen's share of the markup, the remaining markup can be allocated between the platform's liable balance account and its user's balance account. A split profile rule or per-payment `platformDccLogic` instructions can determine this; per-payment instructions override the profile. `targetAccount` identifies the user's balance account and `accountHolderPercentage` gives the user's share in basis points. The guide's defaults book the remaining markup to the platform's liable balance account. Adyen books it as `DCCMarkup` with the balance account's default settlement delay. This is separate from the payment's ordinary amount/fee splits and from generic FX management fees.
- In the Terminal API request, the payment split instructions and DCC markup instructions go in `SaleData.SaleToAcquirerData` as form-encoded key-value pairs or Base64-encoded JSON. Provide payment splits in settlement currency. The response's `AdditionalResponse` can report converted currency/amount, rate and markup. Funds settle in settlement currency: the original pre-DCC transaction amount is paid to the user's balance account, while the post-Adyen-share markup follows the DCC allocation. The example percentages and amounts are illustrative, not a merchant-specific return. DCC can change automated reconciliation; the `DCCMarkup` split type is described as visible in reports/webhooks but unavailable on the Customer Area Transfers page.
- Standalone terminals cannot carry split instructions on individual authorization requests. The snapshot says enabling DCC for one platform store can make all standalone terminals support it regardless of linked store, except terminals on version 1.120 or 1.122 and later. The exact version and account behavior needs verification before rollout.

## Detail locators

- Pilot status, scope, Terminal API/role requirements, methods, surcharge/offline/standalone limits and addendum: pinned raw lines 15–47 (`## Requirements`).
- Customer choice, disclosure and receipt content, authorization-adjustment webhook/CAPTURE path: pinned raw lines 49–112 (`## How it works`; `## Complying with regulations`).
- Markup shares, `DCCMarkup`, split-profile versus request precedence, default and settings steps: pinned raw lines 114–177 (`## DCC markup`; `## Enable DCC for your platform`).
- Settlement-currency split instructions, `platformDccLogic` fields/basis points, encoding formats, request/response examples: pinned raw lines 179–370 (`## Make a payment with DCC`).
- Settlement/reconciliation, report/webhook visibility, dated card/currency/region lists: pinned raw lines 372–470 (`## Reconciling payments`; `## Availability`).

## Related

- [[adyen-currencies-and-fx]] — provider FX concept; this Platforms pilot has its own DCC markup and balance-account allocation rules.
- [[adyen-platforms]] — platform/user and liable-account context.
- [[source-adyen-docs-point-of-sale-currency-conversion]] — broader POS DCC guide; its dated no-extra-contract statement differs from this Platforms guide's addendum requirement, so do not transfer that contract claim across scopes.

## Raw Sources

- [[raw/adyen/docs/platforms/in-person-payments/dynamic-currency-conversion/2026-09-15|Adyen for Platforms in-person DCC — 2026-09-15 snapshot]]
