---
title: "Adyen GrabPay API-only integration guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/grabpay/api-only"
raw_files:
  - "adyen/docs/payment-methods/grabpay/api-only/2026-09-15.md"
tags: [adyen, grabpay, api-only, wallets, paylater, redirects]
---

## Overview

This [[adyen]] GrabPay API-only guide, captured 2026-09-15 (page metadata last modified 2019-09-06), describes a merchant-built Web form, country-qualified Wallet versus PayLater requests, redirect handling and payment-result checks. It names existing **Web API-only Sessions and Advanced** integrations as prerequisites, while the detailed example sequence uses `/payments` and `/payments/details`. See [[adyen-online-payments]]. This historical guide does not prove current merchant enablement, PayLater eligibility, a completed payment, capture or settlement. See raw lines 15–37, 39–67 and 897–985.

## Key takeaways

- **Country and method scope:** After the shopper selects GrabPay, the merchant passes `grabpay_MY` for Malaysia/MYR, `grabpay_PH` for the Philippines/PHP, or `grabpay_SG` for Singapore/SGD; the `/paymentMethods` response can also supply the type. The page expressly says **GrabPay PayLater is unavailable in the Philippines**. These mappings and that exclusion are source-snapshot scope, not proof a merchant account is enabled. The requirements say to add GrabPay in Customer Area for both Sessions and Advanced. See raw lines 21–63.
- **Wallet versus PayLater requests:** Both paths send `/payments` with `grabpay_XX`, a return URL, merchant reference and amount. Wallet prose limits the reference to 32 alphanumeric/dash/underscore characters; PayLater prose states the 32-character maximum but does not repeat that character-set rule. PayLater, whether postpaid or installment, additionally calls for `deliveryAddress` and `lineItems`; its `amountIncludingTax` cannot be zero. Do not extend PayLater to PH. The `grabpay_SG` TEST samples illustrate requests; `/payments` v68 and `/payments/details` v72 examples are mixed, so API/version compatibility needs separate verification. See raw lines 65–79, 397–409, 410–445 and 897–922.
- **Redirect and result:** The `/payments` response example has `resultCode: RedirectShopper` and an `action.url`; this is a redirect instruction, not final authorization. After the shopper returns, the guide says to POST URL-decoded `redirectResult` in `/payments/details`, then use its `resultCode` to display the result. For mobile integrations it recommends the device default browser; for GET redirects shown in-app it recommends SFSafariViewController or Chrome Custom Tabs rather than WebView. These are redirect recommendations inside this Web API-only guide, not a complete native-integration specification. See raw lines 381–395 and 881–957.
- **Asynchronous outcomes:** `Authorised`, `Cancelled` and `Refused` are documented result codes. `Pending` or `Received` means final status is not yet known and the guide says an **AUTHORISATION webhook** supplies the final result. If the shopper closes the browser without returning, it says to wait for webhooks. The webhook table distinguishes AUTHORISATION success true/false and OFFER_CLOSED success true. A shopper return or sample `Authorised` response does not prove an actual capture, settlement or merchant payout. See raw lines 955–974. The PayLater details response may include `additionalData.paymentMethodVariant`, with wallet and PayLater subvariants listed at raw lines 938–953; that field is not the initial `paymentMethod.type`.
- **Testing and live:** Testing requires Support-provided test-wallet credentials and a simulator login using a registered phone number and its one-time password; test payment status is checked in Customer Area. Live acceptance requires a separate GrabPay request in live Customer Area. The page's See also tokenization link is navigation, not an on-page recurring-payment procedure. See raw lines 976–992.

## Detail locators

- Prerequisites, country/currency/type mapping and PH PayLater exclusion: raw lines 21–63.
- Wallet request, examples and redirect action: raw lines 65–395.
- PayLater request, item constraint and examples: raw lines 397–895.
- Redirect return, details, result codes and webhook outcomes: raw lines 897–974.
- TEST and live setup: raw lines 976–985.

## Related

- [[adyen-online-payments]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/grabpay/api-only/2026-09-15|GrabPay API only — captured 2026-09-15]]
