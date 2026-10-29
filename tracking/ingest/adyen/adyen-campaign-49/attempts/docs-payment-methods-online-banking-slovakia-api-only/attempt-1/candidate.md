---
title: "Online banking Slovakia API-only add-on"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-slovakia/api-only"
raw_files:
  - "adyen/docs/payment-methods/online-banking-slovakia/api-only/2026-09-15.md"
tags: [adyen, online-banking-slovakia, api-only, bank-redirect, payments]
---

## Overview

This 2026-09-15-captured [[adyen]] page adds Online banking Slovakia to an existing API-only online-payment integration. A merchant-built form offers issuing banks, sends the chosen issuer to the server, and handles a `redirect` action through the existing integration. It is a method add-on rather than a standalone payment recipe or proof of current merchant eligibility or payment completion. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-online-banking-slovakia|the method overview]] for broader SK/EUR and capability context.

## Key takeaways

- **Prerequisites:** The page requires an existing API-only integration with redirect handling (`action.type: redirect`) and Online banking Slovakia added in Customer Area. It does not state a minimum Checkout API version; the test `/v72/payments` examples do not create one (raw lines 23–29, 73–92).
- **Discovery and UI:** For `/paymentMethods`, the page specifies `countryCode: SK` and `amount.currency: EUR`. The form should obtain issuing-bank options from the returned `onlineBanking_SK` object, show them to the shopper, pass the selected Issuer ID to the server, and ask the shopper to accept the linked terms and conditions. The captured bank table lists BLIK SK (`bliksk`), ePlatby VÚB (`vub`), Poštová banka (`posta`), Sporopay (`sporo`), TatraPay (`tatra`), and Viamo (`viamo`). This is a snapshot list within Online banking Slovakia; `BLIK SK` here is an issuer option, not proof of eligibility for a separate BLIK integration. Use the actual discovery response for available choices (raw lines 31–61).
- **Payment request:** The method-specific `/payments` addition is required `paymentMethod.issuer`, the issuing bank selected by the shopper. The examples also show `paymentMethod.type: onlineBanking_SK`, EUR amount and a `returnUrl` in a server-side test request; those samples supplement the base API-only request, not an executable or live-success guarantee (raw lines 63–92 and 218–245).
- **Action and testing:** The page reiterates that the additional action has type `redirect`, but does not itself give a complete returned-action or post-return status sequence. It says to test with real payment details and small amounts, inspect test payments in Customer Area, and add the method in Customer Area to accept live payments. These are documented steps, not evidence that a particular merchant is enabled or that a payment succeeded (raw lines 383–399).

## Detail locators

- Requirements and method-specific discovery: raw lines 23–39.
- Issuer choice, table and terms: raw lines 40–61. Bank names and IDs are captured values; check the `/paymentMethods` response for current available options.
- `/payments` issuer field and language-specific test examples: raw lines 63–381. The examples use a test endpoint, EUR 1000 minor-unit value and `vub` issuer; no minimum API/library version follows from those examples.
- Action type and test/live steps: raw lines 383–399.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-slovakia]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-slovakia/api-only/2026-09-15|Online banking Slovakia API-only, captured 2026-09-15]]
