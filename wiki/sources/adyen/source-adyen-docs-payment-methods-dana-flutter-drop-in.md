---
title: "Adyen DANA Flutter Drop-in guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/dana/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/dana/flutter-drop-in/2026-09-15.md"
tags: [adyen, dana, flutter, drop-in, wallets, tokenization]
---

## Overview

This [[adyen]] DANA Flutter Drop-in add-on, captured 2026-09-15, describes method-specific steps for **existing** Sessions or Advanced Flutter Drop-in integrations and a separate recurring-token route. See [[adyen-online-payments]] and [[adyen-tokenization]]. It is not a standalone Flutter integration, evidence of merchant enablement, or proof that a payment or refund completed. See raw lines 15–23, 25–48 and 298–320.

## Key takeaways

- **Sessions:** The prose requires an existing Sessions Flutter Drop-in integration, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and DANA setup. Its setup row says to contact Adyen Support to add DANA. The base `/sessions` request and DANA configuration need no additional method-specific parameters. The integration-type link labeled Sessions actually points to an **Advanced** Flutter Drop-in URL, so use the flow-specific prose and verify the main Sessions guide. See raw lines 25–48.
- **Advanced:** The prose requires an existing Advanced Flutter Drop-in integration and redirect handling. Its setup row says to add DANA in Customer Area, unlike the Sessions row's Support-contact wording; the guide does not resolve the difference. It says no additional DANA configuration or ordinary `/payments` request parameters are needed. These no-extra-fields claims do not cover the separate recurring request. See raw lines 298–320.
- **Recurring:** The guide states DANA supports recurring transactions. Token creation adds `storePaymentMethod: true` and a unique `shopperReference` to `/payments`. It says the `recurring.token.created` webhook, carrying `storedPaymentMethodId`, arrives **when the initial payment has settled**, and the server must receive token-lifecycle webhooks. Later token payments use that stored ID, the matching shopper reference, `shopperInteraction: ContAuth`, and `Subscription` for fixed intervals or `UnscheduledCardOnFile` for nonfixed intervals. Request submission or redirect alone does not prove settlement or token creation. See raw lines 50–87 and 322–359.
- **Examples and environments:** The later-payment samples use `type: dana`, IDR amounts and TEST endpoints; they are example server requests rather than a full Flutter client implementation or country/account eligibility matrix. Under **Test and go live**, the page says a real mobile number registered with a DANA account is needed to test successful DANA **live** payments, yet also tells readers to check **test** payment status in test Customer Area. Keep this live/test wording tension and verify the intended environment before operational use. It separately requires a DANA request in live Customer Area before live acceptance. See raw lines 89–286, 288–296, 361–558 and 560–568.

## Detail locators

- Sessions prerequisites, setup, request and configuration: raw lines 25–48.
- Sessions recurring-token fields and examples: raw lines 50–286.
- Advanced prerequisites, setup, request and configuration: raw lines 298–320.
- Advanced recurring-token fields and examples: raw lines 322–558.
- Testing, status check and live request: raw lines 288–296 and 560–568.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/dana/flutter-drop-in/2026-09-15|DANA Flutter Drop-in — captured 2026-09-15]]
