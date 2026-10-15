---
title: "Testing result codes and refusal reasons | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/testing/result-codes"
raw_files:
  - "adyen/docs/development-resources/testing/result-codes/2026-09-15.md"
tags: [adyen, payment-testing, result-codes, refusal-reasons, checkout-api]
---

## Overview

This 2026-09-15 Adyen Docs snapshot shows how an **online Checkout API test integration** can trigger result codes and refusal reasons in a `/payments` response to exercise failure handling before go-live. It points in-person integrations to a separate POS decline-simulation guide. See [[adyen]] and [[adyen-payment-testing]].

## Key takeaways

- To select a test response, set either `paymentMethod.holderName` to a table value or `additionalData.RequestedTestAcquirerResponseCode` to its numeric code in a `/payments` request. The shown `CARD_EXPIRED` or code `6` example yields `Refused` with an expired-card refusal in the illustrated response. Its USD 10.00 amount is example payment data, not the documented trigger for that refusal.
- Some card-related payment methods redirect to a simulator to choose the result; in that case the supplied holder name is ignored. The table must be used with that method-specific qualification, not as a guarantee that every trigger works for every payment method.
- The mapping table covers more than refusals: `APPROVED` / code `1` maps to `Authorised`, and `PENDING` / code `13` maps to `Received`; it also includes `Error`, `Cancelled`, and many `Refused` cases. A test `Authorised` response is a simulated result, while `Received` is a distinct intermediate result; neither fixture proves a production authorization or final settlement.
- The guide asks implementers to verify the triggered `resultCode` and `refusalReason` and check their integration's response handling. It motivates shopper messages, retry logic, and order-management handling as examples of uses, not mandatory policy for each refusal. Its sample `/payments` URL is Checkout v72 test, while API Explorer links use `latest`; do not transfer the table into an unverified production or fixed-version guarantee.

## Detail locators

- Test purpose and separate in-person route: lines 15–25.
- Suggested reasons for testing unhappy flows: `Benefits of testing refusal reasons`, lines 27–33.
- Two trigger fields, simulator exception, expired-card example, and response verification: `Trigger a refusal reason in a payment request`, lines 35–119.
- Full result/refusal trigger table, including `Authorised`, `Received`, `Error`, `Cancelled`, and `Refused`: `Values for testing refusal reasons`, lines 121–176.
- Related refusal, result-code, and response-handling navigation: `See also`, lines 178–182.

## Related

- [[adyen-payment-testing]] — test integration scope and simulation outcome boundary.
- [[source-adyen-docs-online-payments-build-your-integration-payment-result-codes]] — payment result-code interpretation.

## Raw Sources

- [[raw/adyen/docs/development-resources/testing/result-codes/2026-09-15|Testing result codes and refusal reasons (2026-09-15)]]
