---
title: "Adyen Payment Result Codes"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/build-your-integration/payment-result-codes"
raw_files:
  - "adyen/docs/online-payments/build-your-integration/payment-result-codes/2026-09-15.md"
tags: [adyen, online-payments, result-codes, webhooks]
---

## Overview

This unversioned [[adyen]] website-guide snapshot explains how an online-payment integration receives a `resultCode`, uses that current-state signal to inform the shopper, and distinguishes it from later payment-status updates. It explicitly warns that a result code can change and should not be used to update the order management system. See [[adyen-online-payments]].

## Key takeaways

- The retrieval point depends on the server-side flow: Sessions returns the result through Drop-in or a Component when the flow finishes; Advanced returns it from `/payments` when no additional action is required or from `/payments/details` after an additional action.
- Authentication-only and 3D Secure 2 result codes describe the next authentication or authorization action. They are not themselves proof of payment authorization, capture, or settlement.
- Intermediate result codes mean the payment has not reached a final state. The guide says successful completion is reported through an `AUTHORISATION` webhook and notes that completion can take minutes, hours, or days. Keep this asynchronous webhook lifecycle distinct from the synchronous result shown to the shopper.
- The guide separately documents partial authorization for merchants that accept it and final-state result codes. An `Authorised` result tells the merchant to inform the shopper of success, but manual-capture integrations still need to capture the payment; the updated webhook status is the route the guide identifies for order-management updates.
- For a non-`Authorised` result, the response includes a `refusalReason`; Adyen recommends not disclosing that reason to the shopper.
- This dated documentation snapshot is not evidence of current account or payment-method eligibility, successful execution, webhook delivery, authorization, capture, or settlement. Its API Explorer links use `latest`, so it does not establish a fixed Checkout API version.

## Detail locators

- Purpose and warning against order-management updates from the synchronous result: raw line 19.
- Required online-payments integration and API credential roles: raw lines 21–29.
- Sessions and Advanced result-code retrieval points: raw lines 31–38.
- Standalone-authentication and 3D Secure 2 action groups: raw lines 40–57.
- Intermediate states, successful `AUTHORISATION` webhook, and potentially long completion time: raw lines 59–71.
- Partial authorization scope and documented follow-up choices: raw lines 73–82.
- Final states, manual-capture qualification, and refusal-reason disclosure warning: raw lines 84–95.

## Related

- [[adyen]] — provider page.
- [[adyen-online-payments]] — provider-level online-payments architecture and lifecycle route.
- [[source-adyen-docs-online-payments-build-your-integration]] — server-side flow selection guide.

## Raw Sources

- [[raw/adyen/docs/online-payments/build-your-integration/payment-result-codes/2026-09-15|Adyen payment result codes — collected 2026-09-15]]
