---
title: "Stripe Terminal: Provide Receipts"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-receipts-2025.md"
tags: [stripe, stripe-terminal, receipts, emv, compliance, card-networks]
---

## Summary

Stripe Terminal merchants must offer customers a physical or email receipt per card network rules and local regulations. Stripe supports two approaches: prebuilt email receipts and custom receipts.

## Prebuilt Email Receipts

- Set `receipt_email` on the PaymentIntent at creation (or update it after checkout).
- Stripe automatically emails a compliant receipt when the PaymentIntent is captured.
- Available via server-side API (`receipt_email`) and client-side SDKs (`receiptEmail` on iOS, Android, React Native).
- Prebuilt receipts already include all card network-required fields — no extra work needed.

## Custom Receipts

For branded or printed receipts, merchants can build their own using EMV fields from the Stripe API or Terminal SDKs.

**Required EMV fields** (available on PaymentIntent after confirmation):

| Field | Name | Requirement |
| --- | --- | --- |
| `account_type` | Account Type | Required (optional in US) |
| `application_preferred_name` | Application name | Required |
| `dedicated_file_name` | AID | Required |

**Optional EMV fields**: `authorization_response_code` (ARC), `application_cryptogram`, `terminal_verification_results` (TVR), `transaction_status_information` (TSI).

- Server-side: access via the `receipt` object on `charge.payment_method_details.card_present`.
- Client-side: `ReceiptDetails` class on iOS, Android, React Native SDKs. JS SDK returns the API PaymentIntent object directly.
- `preferred_locales` on the PaymentMethod object provides the cardholder's preferred language from the card.

## Sources

- [[source-stripe-terminal-receipts]] — this page

## Raw Sources

- [[stripe-terminal-receipts-2025]] — verbatim webpage content
