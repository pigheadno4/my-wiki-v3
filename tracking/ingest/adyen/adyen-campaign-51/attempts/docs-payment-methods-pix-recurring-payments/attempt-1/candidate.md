---
title: "Recurring payments with Pix Automático"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pix/recurring-payments"
raw_files:
  - "adyen/docs/payment-methods/pix/recurring-payments/2026-09-15.md"
tags: [adyen, pix, pix-automatico, recurring-payments, tokenization, webhooks]
---

## Overview

This Adyen Pix Automático guide, last modified 2024-03-25 and captured 2026-09-15, describes setting up a subscription billing plan with shopper QR confirmation, receiving a stored payment token, scheduling later charges, interpreting webhooks, retrying failures and ending a plan. It is for an API-only Checkout integration, not evidence of a created mandate, live enablement or successful charge. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-pix]] for Pix method context.

## Key takeaways

- Prerequisites are API-only Checkout API v49 or later, Standard and recurring-token lifecycle webhooks, Pix setup in Customer Area, and the Pix API-only integration. The page limits recurring Pix to the Subscription recurring processing model. It strongly recommends explicit shopper permission for future recurring charges; that advice is not itself stated as a required API field. See raw lines 23–36 and 65–69.
- Journey 2 authorizes a subscription by QR code without an initial payment, using amount.value 0 for zero-value validation. Journey 3 combines QR authorization with an initial payment, using the immediate payment amount. Both create a billing plan and show action.qrCodeData for shopper confirmation. The page says recurring.token.created confirms token creation and supplies shopperReference/storedPaymentMethodId; Journey 3 also has an AUTHORISATION webhook for the immediate transaction. These are separate events. See raw lines 38–63 and 71–83, 138–153.
- Initial /payments setup marks pix type, shopperReference (case-sensitive, at least three characters, no PII), shopperInteraction Ecommerce, recurringProcessingModel Subscription, storePaymentMethod true and amount required. Pix-specific required fields are shopperName, CPF/CNPJ socialSecurityNumber and pixRecurring.frequency; the listed fixed recurringAmount or variable minAmount, dates, statement and retryPolicy are unmarked optional/conditional. Frequency choices are weekly, monthly, quarterly, half-yearly and yearly. Plan changes require cancelling and creating a new plan. See raw lines 71–97 and 155.
- Schedule a later /payments charge ten to two days before its billing date. Use the webhook-supplied storedPaymentMethodId, the same shopperReference, shopperInteraction ContAuth, model Subscription, billingDate and amount. A fixed recurringAmount must match; a plan with minAmount can use a new amount. The request resultCode Pending is not charge success. AUTHORISATION success true confirms scheduling only; after the billing date CAPTURE success true confirms a charge, while CAPTURE success false or EXPIRE success true signals failure/no capture. See raw lines 157–173 and 201–222.
- Retry is limited to three attempts after the specified failure webhooks and only when retryPolicy was enabled at plan setup. Keep the failed amount, choose a new billingDate at least 24 hours ahead and within seven days of the failed billing date, and pass originalPspReference from the failure webhook's originalReference. To end a plan, delete the stored token; bank-initiated cancellation can cause Adyen to delete it and emit recurring.token.disabled, while merchant-side shopper data cleanup remains the merchant's responsibility. Refund is described within 90 days after capture; an uncaptured scheduled payment may be cancelled before 10 PM on the day before its scheduled date. The source does not state a timezone for that cutoff. See raw lines 224–287.

> [!warning] Example request inconsistency
> The fixed plan example sets recurringAmount.value to 10000 (raw lines 116–120), while the later recurring-charge example sends amount.value 100000 (lines 183–185), despite the stated fixed-amount match rule (lines 166–168). The retry sample also has a malformed storedPaymentMethodId key and incomplete nesting (lines 256–266); do not treat it as copy-ready JSON. Example 2025 billing dates precede the 2026 capture.

## Detail locators

- Scope, setup, model and two QR authorization journeys: raw lines 23–43.
- QR presentation, token and transaction webhook sequence: raw lines 45–63 and 138–153.
- Initial token/billing-plan fields and consent advice: raw lines 65–97.
- Schedule window, stored token and later charge fields: raw lines 157–173.
- Pending, scheduled-authorisation and final charge/failure webhook meanings: raw lines 201–222.
- Retry limits, dates and original reference: raw lines 224–242.
- Token deletion, refund/cancel and cutoff: raw lines 269–287.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-pix]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pix/recurring-payments/2026-09-15|Pix Automático recurring payments, captured 2026-09-15]]
