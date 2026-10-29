---
title: "Adyen PaySafeCard recurring payments"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paysafecard/recurring"
raw_files:
  - "adyen/docs/payment-methods/paysafecard/recurring/2026-09-15.md"
tags: [adyen, paysafecard, recurring, tokenization, online-payments]
---

## Overview

This 2026-09-15-captured Adyen guide describes tokenization and subsequent recurring payments for PaySafeCard with a myPaysafeCard wallet. It covers the listed country scope, transaction flags, token creation and reuse, data exchange, test setup, and two refusal cases. Its statement that an existing PaySafeCard account needs no extra setup does not mean every payment funding source can yield a token. This is a method-specific supplement to [[adyen-online-payments]]. [[adyen]]

## Key takeaways

- **Country and account scope:** The page lists Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lichtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, and United Kingdom for PaySafeCard recurring tokenization. It says the existing PaySafeCard account works with no extra setup, and strongly recommends explicit shopper permission and schedule/amount transparency. The captured country list is not proof of current account eligibility. [Raw: lines 19–28]
- **Wallet-only token condition:** PaySafeCard can be funded by myPaysafeCard wallet or Voucher/PIN card, but only wallet payments are eligible for tokenization. A Voucher/PIN payment on a tokenization request can still process with no token generated. The merchant cannot control the funding source, and the payment response does not identify it; receipt of a payment response alone therefore cannot establish token creation. The `CardOnFile` wording in the recurring model names does not extend recurring support to Voucher/PIN cards. [Raw: lines 36–45]
- **Initial request and token retrieval:** For a token-creation `/payments` request, the guide calls for `recurringProcessingModel`, `shopperInteraction` (online `Ecommerce`), a case-sensitive `shopperReference` of at least three characters without PII, and `storePaymentMethod: true`. Models are `CardOnFile` for stored one-click/omnichannel use, `UnscheduledCardOnFile` for non-fixed schedule and/or variable amounts, and `Subscription` for fixed schedule with fixed or variable amount. It shows zero-value authorization through `/sessions` or `/payments`, or with-purchase tokenization using the purchase amount. Obtain the shopper reference and actual token from webhooks after the initial flow; the zero-EUR sample is illustrative, not evidence of a token. [Raw: lines 30–39, 47–84]
- **Subsequent payment:** Send `storedPaymentMethodId` from the webhook as the Adyen reference to the token/myPaysafeCard account, plus `shopperInteraction: ContAuth` and the applicable `recurringProcessingModel` (the example uses `Subscription`). `storePaymentMethod` is not required on later payments. The EUR 20 example is a sample request, not an acceptance guarantee. [Raw: lines 39, 86–114]
- **Data exchange and testing:** After wallet confirmation, Customer Data Exchange can return customer data for positive-amount payments but not the zero-amount transaction establishing the recurring relationship. Testing calls for a myPaysafeCard test wallet requested from Paysafe technical support with country and test-user birth date, then token creation, webhook confirmation, model and error scenarios in Adyen test. The page also instructs the same scenarios live; that is a provider procedure, not evidence they were performed. [Raw: lines 116–134]
- **Refusal handling:** Error 2004 means insufficient wallet balance; the page suggests a lower-amount retry or shopper top-up then retry. Error 10033 means an invalid token, possibly after more than one year of inactivity or failed creation; ask the shopper to approve recurring again through a new zero-value authorization request. The captured table has a line-wrap break in its 2004 row, so read the adjacent lines together. [Raw: lines 136–144]

> [!WARNING] Payment success does not prove recurring readiness
> Voucher/PIN payments can process but yield no token, and their funding source is absent from the payment response. Confirm token creation through the documented webhook before storing or reusing `storedPaymentMethodId`. [Raw: lines 43–45, 84–90]

## Detail locators

- Listed countries, no-extra-setup statement and permission recommendation: pinned raw lines 19–28.
- Recurring flags and wallet-only limitation: pinned raw lines 30–45.
- Zero-value or with-purchase token request and webhook token retrieval: pinned raw lines 47–84.
- Subsequent token payment: pinned raw lines 86–114.
- Data exchange, test wallet and refusal handling: pinned raw lines 116–144.

## Related

- [[adyen-online-payments]] — provider integration and method routes.
- [[source-adyen-docs-payment-methods-paysafecard]] — approved method overview; consult its captured capability matrix separately from this wallet-only recurring guide.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paysafecard/recurring/2026-09-15|PaySafeCard recurring guide, captured 2026-09-15]]
