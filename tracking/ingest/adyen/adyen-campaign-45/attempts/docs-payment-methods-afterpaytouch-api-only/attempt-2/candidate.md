---
title: "Afterpay API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/afterpaytouch/api-only"
raw_files:
  - "adyen/docs/payment-methods/afterpaytouch/api-only/2026-09-15.md"
tags: [adyen, afterpay, api-only, redirect, capture, tokenization]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] guide adds Afterpay to an existing API-only online-payments integration. The merchant builds the form, collects shopper data, requests `afterpaytouch`, handles a redirect and captures payment. See [[adyen-online-payments]]. The captured API examples and sandbox instructions do not prove current merchant enablement, a completed redirect or successful settlement.

## Key takeaways

- Start with an existing API-only integration configured for `action.type: redirect`, and add Afterpay in Customer Area. The merchant form collects full name, email, billing and delivery addresses for Afterpay risk checks. The `/payments` table also marks shopper reference, country code and `lineItems` required; telephone number is optional. The AU/AUD TEST payment example uses Checkout API v68 and `paymentMethod.type: afterpaytouch`; a redirect action is shown, not final payment success.
- `/paymentMethods` discovery table pairs AU/AUD, NZ/NZD and CA/CAD. Its AU/AUD TEST example uses Checkout API v71. These captured combinations describe method discovery requests, not current account availability or all supported markets. The sandbox setup lists AU, NZ, US and Canada as test account choices; US in that list is not a discovery-table country/currency pair.
- Depending on account settings, capture follows authorisation automatically or manually. Shipping before capture calls for capture delay or manual capture; partial capture requires manual capture. Capture within 13 days, or Afterpay cancels and refunds the first installment charged at authorisation. TEST authorizations expire in one day. After one partial capture, the unclaimed amount is cancelled unless the account is enabled for multiple partial captures through Support; each capture then creates a new invoice. Cancel before capture and refund after capture.
- Recurring and on-file tokenization is explicitly limited to Australia and New Zealand. With shopper permission, the initial payment or zero-value authorization redirects the shopper to approve storage; enable tokenization webhooks and save `storedPaymentMethodId` with `shopperReference` from `recurring.token.created` (response additional data is an optional route). The guide's illustrated later on-file request uses `shopperInteraction: ContAuth` and `recurringProcessingModel: CardOnFile` (raw lines 1042–1108), and says no Afterpay redirect because prior approval was given. This example does not establish `CardOnFile` as the model for every recurring subscription, extend tokenization to Canada or prove that all future payments authorize.
- The discount section calls for a negative line-item amount, but its illustrative JSON has an empty currency and is not a complete validated payment request. Live acceptance requires a request for Afterpay in live Customer Area.

## Detail locators

- API-only/redirect prerequisites and method workflow: pinned raw lines 15–50. Discovery pairs and sample: lines 52–91. `/payments` fields, AU/AUD sample and redirect response: lines 93–171 and 822–836.
- Capture, cancellation/refund and discount example: lines 838–904. AU/NZ tokenization and initial/later payment examples: lines 906–1130. Sandbox/live setup: lines 1132–1151.

## Related

- [[adyen-online-payments]] — provider integration concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/afterpaytouch/api-only/2026-09-15|Afterpay API-only guide, captured 2026-09-15]]
