---
title: "Adyen manage payments in Customer Area"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/account/manage-payments"
raw_files:
  - "adyen/docs/account/manage-payments/2026-09-15.md"
tags: [adyen, customer-area, payment-management, refund, capture, reauthorisation]
---

## Overview

This Adyen Customer Area guide (2023-05-02 last-modified metadata; captured 2026-09-15) explains how to find payment details and submit refund, cancellation, capture, or re-authorization actions. It points to APIs as another route. It is an interface and eligibility guide, not evidence that a submitted action succeeded, funds moved, or a particular payment is safe to retry. See [[adyen-online-payments]], [[adyen-payment-capture]], [[adyen-refunds]], and [[adyen]].

## Key takeaways

- The company-account **Payments > Payment list** covers payments across regions and currencies and shows PSP reference, merchant reference, merchant account, date, amount, method, status, and risk score. Payment details include lifecycle, events/ARN, processing and transaction costs. `Export Payments` is needed to export CSV, and `Merchant view PII` is needed to unmask default-masked shopper details. [Raw lines 27–57]
- Customer Area **Refund payment** requires `Merchant manage payments` or `Refund payments` role and appears only after capture, with `SentForSettle` or `Settled` status. The requested refund amount must equal or, for a partial refund, be less than the captured amount; the form accepts a refund request reference. This action initiates a request, not documented bank or shopper receipt here. [Raw lines 59–81]
- For payment methods supporting separate capture, **Cancel payment** is available only before capture at `Authorised` status, with `Merchant manage payments` or `Cancel payments` role and a confirmation code. **Capture payment** likewise appears only at `Authorised`, requires `Merchant manage payments` or `Capture payments`, and accepts amount and request reference. Availability of a UI action does not by itself establish successful modification or final funds transfer. [Raw lines 83–128]
- Refusal detail appears in **Processing > Acquirer response**; a `FRAUD` response has a risk-results drilldown, while a bare `Refused` directs the shopper to their bank for the reason. The guide says fraud score 100 or more is automatically refused in this Customer Area account context. [Raw lines 130–139]
- Re-authorization is a separate merchant-initiated action for specific latest journal types (`Cancelled`, `Expired`, `Refunded`, `RefundedBulk`, `RefundedExternally`) and listed cards or SEPA Direct Debit, requiring `Merchant re-authorise payments` role. It can still be issuer-refused, may create a new chargeback, and Adyen says the merchant bears that chargeback liability because it initiated the payment. Optional amount, reference, and capture delay fields alter the request; blank delay follows account capture settings. Adyen does not proactively re-authorize. [Raw lines 141–190]

## Detail locators

- Payment-list fields, detail tabs, export/PII roles: raw lines 27–57. Refund roles, captured-state gate, amount/ref: raw lines 59–81. Cancel/capture eligibility, roles, confirmation and submit steps: raw lines 83–128.
- Refusal investigation: raw lines 130–139. Re-authorization eligibility, risk and optional fields: raw lines 141–190.
- This page specifies Customer Area conditions and submissions; track subsequent lifecycle and operation outcomes in the payment journal/events and applicable webhook or provider result evidence before claiming success.

## Related

- [[adyen-online-payments]]
- [[adyen-payment-capture]]
- [[adyen-refunds]]
- [[adyen]]
- [[source-adyen-docs-account-payments-lifecycle]]

## Raw Sources

- [[raw/adyen/docs/account/manage-payments/2026-09-15|Adyen manage payments, 2026-09-15 snapshot]]
