---
title: "Adyen MoMo API-only integration guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/momo-wallet/api-only"
raw_files:
  - "adyen/docs/payment-methods/momo-wallet/api-only/2026-09-15.md"
tags: [adyen, momo, api-only, wallets, online-payments, tokenization]
---

## Overview

This [[adyen]] MoMo method add-on for an **existing API-only Advanced Web integration**, captured 2026-09-15, covers MoMo method discovery, a merchant-owned payment form, redirect prerequisites, and a separate recurring-token route. See [[adyen-online-payments]] and [[adyen-tokenization]]. It is not a standalone checkout implementation, proof that MoMo is enabled for an account, or evidence of authorization, settlement or order fulfillment. See raw lines 15–29 and 31–46.

## Key takeaways

- **Base flow and form:** The integration must already handle an `action.type: redirect`, and MoMo must be added in Customer Area. The page's short flow says the shopper enters details in the merchant-built form, but the form section expressly says **no information needs to be collected from the shopper** for MoMo. Read the latter as the method-specific form instruction and do not infer required shopper input from the generic flow sentence. The flow list also puts “fulfill the order” after the payment request without explaining status checks; this is not a verified authorization or fulfillment trigger. See raw lines 23–42.
- **Discovery and ordinary payment:** For `/paymentMethods`, the guide specifies `countryCode: VN`, `amount.currency: VND`, an amount value, and a channel such as Web, iOS or Android to include MoMo; the sample response identifies `momo_wallet`. The ordinary `/payments` add-on says no extra MoMo-specific parameters. These VN/VND discovery parameters are scoped to this API-only guide and do not alone establish account eligibility. The `/paymentMethods` curl sample uses a v72 TEST URL while later recurring samples use v68; its displayed `-X POST` line lacks a continuation before `-d`, and its example omits the table's channel field. Treat samples as illustrative rather than a verified executable recipe. See raw lines 44–89 and 128–325.
- **Recurring:** The guide says MoMo supports recurring transactions. Token creation adds `storePaymentMethod: true` and a shopper-unique `shopperReference` to `/payments`. It describes `recurring.token.created`, with `storedPaymentMethodId`, **after the initial payment has settled** and requires the server to receive token-lifecycle webhooks. Later token payments use the stored ID, matching shopper reference, `shopperInteraction: ContAuth`, and `Subscription` for fixed intervals or `UnscheduledCardOnFile` for nonfixed intervals. The base no-extra-parameters statement does not apply to these token requests. See raw lines 87–126.
- **Example and environment limits:** The Java recurring sample calls `setRecurringDetailReference` while the prose and other examples specify `paymentMethod.storedPaymentMethodId`; this field-mapping difference is unresolved on the page. For TEST, it directs use of the MoMo test app and scenario-specific credentials, with status checked in test Customer Area. Live acceptance separately requires a MoMo request in live Customer Area. Neither an app handoff nor a setup request proves payment success or live enablement. See raw lines 128–325 and 327–336, especially 169–171.

## Detail locators

- API-only prerequisites, generic flow and form discrepancy: raw lines 23–42.
- `/paymentMethods` parameters, v72 example and `momo_wallet` response: raw lines 44–85.
- Ordinary `/payments` statement and recurring-token prerequisites: raw lines 87–126.
- Later-payment v68 examples and Java field mismatch: raw lines 128–325.
- TEST app, status checking and live request: raw lines 327–336.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/momo-wallet/api-only/2026-09-15|MoMo API only — captured 2026-09-15]]
