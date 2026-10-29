---
title: "Adyen PaySafeCard Customer Data Exchange"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paysafecard/customer-data-exchange"
raw_files:
  - "adyen/docs/payment-methods/paysafecard/customer-data-exchange/2026-09-15.md"
tags: [adyen, paysafecard, customer-data-exchange, auth-flow, capture, online-payments]
---

## Overview

This 2026-09-15-captured Adyen guide describes PaySafeCard Customer Data Exchange for MyPaySafeCard account payments. It frames the feature for a merchant whose business type and location legally require excluding anonymous payment methods, then describes owner-data delivery, merchant comparison, and a conditional cancel or capture decision. This is a provider procedure, not a legal determination or proof of a configured account or executed transaction. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Conditional purpose and data:** The guide says that when the merchant's business type and location legally require excluding anonymous methods, MyPaySafeCard is the checkout option. It says PaySafeCard verifies the shopper's first name, last name, and date of birth; after a completed MyPaySafeCard payment, those data are sent to Adyen. The merchant is expected to hold comparable information for verification. The returned account-owner fields also include an account ID. This statement does not decide whether a particular merchant has that legal obligation. [Raw: lines 19–23, 46–50]
- **Authorization and capture configuration:** For an account currently set to automatic capture, the guide says it must be changed to an **Auth. flow** for this verification process. In that flow the transaction stays **Authorised**, with funds reserved but not yet debited, until the merchant sends capture. It says the authorized amount remains frozen for **24 hours** before release to the shopper's MyPaySafeCard account and recommends prompt comparison and capture. An authorization or data receipt is not a capture. [Raw: lines 25, 29–35]
- **Data-return routes:** After redirect, send `redirectResult` to `/payments/details` to check authorization and receive data. Alternatively, after authorization the standard webhook can deliver the same format even if the shopper does not return to the frontend. Configure “payment account owner data” in Customer Area under **Developer > Additional Data** for details responses, or under **Developer > Webhooks** for the standard webhook. The page says this feature can be configured for any currency account via Adyen; it does not establish acceptance of every currency for every payment. [Raw: lines 37–50, 56–69, 87–89]
- **Merchant decision:** Compare the returned owner information with the merchant's user record. If the comparison fails the merchant's criteria, the documented flow sends `/payments/{paymentPspReference}/cancels` to remove the reservation; otherwise it sends `/payments/{paymentPspReference}/captures`. The source does not define the merchant's identity-match policy or legal standard, and neither the sample `Authorised` response nor sample `AUTHORISATION` webhook is evidence that capture occurred. [Raw: lines 52–54, 71–85, 89–126]

> [!WARNING] Captured example boundary
> The examples show `additionalData.paymentAccountOwner.firstName`, `lastName`, `dateOfBirth`, and `accountId`, with `Authorised`/`AUTHORISATION` status. These are illustrative payloads. The guide requires a separate merchant comparison and cancel or capture request; do not infer verification or captured funds from the examples. [Raw: lines 69–85, 89–126]

## Detail locators

- Conditional use case, verified shopper attributes, 24-hour authorization hold: pinned raw lines 19–25.
- Actor sequence, delivery paths, owner fields, comparison and cancel/capture: pinned raw lines 27–54.
- Customer Area configuration and currency-account statement: pinned raw lines 56–63.
- Details and webhook example fields: pinned raw lines 65–126.

## Related

- [[adyen-online-payments]] — provider integration and method routes.
- [[source-adyen-docs-payment-methods-paysafecard-recurring]] — recurring-tokenization guide; its positive-amount versus zero-amount customer-data distinction is separate from this page's Auth.-flow use case.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paysafecard/customer-data-exchange/2026-09-15|PaySafeCard Customer Data Exchange guide, captured 2026-09-15]]
