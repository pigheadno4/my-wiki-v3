---
title: "Stripe Terminal: Provide Receipts"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
canonical_url: "https://docs.stripe.com/terminal/features/receipts"
original_format: webpage
raw_files:
  - "stripe-terminal-receipts-2025.md"
tags: [stripe, stripe-terminal, receipts, emv, compliance, card-networks]
---

## Summary

Stripe Terminal merchants must offer customers a physical or email receipt per card network rules and local regulations. Stripe supports two approaches: prebuilt email receipts and custom receipts.

## Prebuilt Email Receipts

- When you have the customer's email, set `receipt_email` when creating the live PaymentIntent. Stripe automatically emails a compliant receipt at capture.
- To trigger an automatic email after checkout, update the PaymentIntent's `receipt_email` with the customer's email.
- For Terminal payments created with test API keys, Stripe does not automatically send receipts. View or manually send a test receipt in the Dashboard.
- Available via server-side API (`receipt_email`) and client-side SDKs (`receiptEmail` on iOS, Android, React Native).
- Prebuilt receipts include the fields required by card networks.

## Custom Receipts

Merchants can use the Stripe API or Terminal SDKs to build branded emailed or printed receipts. Include the required fields for in-person EMV payments.

**Required EMV fields** (available on PaymentIntent after confirmation):

| Field | Name | Requirement |
| --- | --- | --- |
| `account_type` | Account Type | Required (optional in US) |
| `application_preferred_name` | Application name | Required |
| `dedicated_file_name` | AID | Required |

**Optional EMV fields**: `authorization_response_code` (ARC), `application_cryptogram`, `terminal_verification_results` (TVR), `transaction_status_information` (TSI).

- Server-side: access via the `receipt` object on `charge.payment_method_details.card_present`.
- Client-side: `ReceiptDetails` class on iOS, Android, React Native SDKs. The JavaScript SDK's PaymentIntent object matches the API object.
- If provided, `preferred_locales` on the PaymentMethod object gives the cardholder's preferred language from the presented card's settings.

## Related Pages

- [[stripe-terminal]] — in-person receipt workflows
- [[source-stripe-receipts]] — general Stripe email receipts. The May 11, 2026 general guide describes a verified-user testing exception. The November 7 general guide calls for manual test sends, and both Terminal captures document that test-key receipts are available to view or send manually in the Dashboard.

## Raw Sources

- [[stripe-terminal-receipts-2025]] — full Terminal guide captured May 1, 2025

## Related raw API references

- [[raw/stripe-terminal-features-receipts-2026-11-07]] — full November 7, 2026 Terminal guide documenting the same receipt behavior
