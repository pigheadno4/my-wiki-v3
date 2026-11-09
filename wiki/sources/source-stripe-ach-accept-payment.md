---
title: "Stripe: Accept an ACH Direct Debit Payment"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment"
raw_files:
  - "stripe-ach-accept-payment-2025.md"
tags: [stripe, ach, us-bank-account, checkout, payment-element, payment-intents, financial-connections, verification]
---

## Summary

The guide captured 2026-05-02 at this URL covers ACH Direct Debit through Checkout, Elements with the Checkout Sessions API, Elements with the Payment Intents API, Direct API, iOS, Android, React Native, and Webview. The 2026-11-07 capture at the same base URL is a short index linking to those variants. It does not contain their integration instructions. The missing guide text in the November base-URL capture is not evidence that the older mechanics were deprecated or still describe current variant behavior. The integration details below are attributed to the May guide; the linked November variant pages require separate capture before making current-behavior claims.

## Key integration details from the 2026-05-02 guide

**Checkout scope and setup.** The Checkout variant says US Stripe users can accept ACH Direct Debit in payment mode, and its compatibility table lists US business location and USD supported and presentment currency. All line-item Prices must be in USD. Stripe describes dynamic payment methods as an option; the manual example uses `payment_method_types: ['card', 'us_bank_account']`. The guide recommends `payment_intent_data.setup_future_usage: 'off_session'` when saving for later use. These are Checkout-variant statements, not an eligibility finding for every platform or account.

**Account model.** The guide separately presents Accounts v2 and Customers v1 examples. It says Accounts v2 is generally available for Connect users and in public preview for other Stripe users, with a preview API version required for preview participants. An Account example uses `customer_account`; a Customer example uses `customer`. The examples do not establish this account's eligibility or make the preview generally available.

**Verification.** Automatic verification offers Financial Connections instant verification with manual entry and microdeposit fallback. The guide also shows instant-only `verification_method: 'instant'`, which makes an inability to verify instantly a `requires_payment_method` outcome, and a microdeposit-only option. The Checkout variant lists ten failed verification attempts. The Direct API variant is more precise: ten **failed descriptor-code** attempts versus three **failed amount-based** attempts; microdeposit verification times out after ten days, after which the PaymentIntent requires new payment-method details. A failed send, exceeded attempts, and timeout are distinct failure paths. Do not apply a universal ten-attempt limit.

**Financial Connections data.** When the bank account is successfully linked through Financial Connections, expanding the PaymentIntent's `payment_method` exposes `us_bank_account.financial_connections_account`. Accounts entered manually and verified through microdeposits do not have that Financial Connections account ID. Additional data such as balances requires requested permissions and customer authorization; `payment_method` permission alone is not a balance grant.

**Mandate and payment state.** In the Direct API flow the customer must see and accept mandate terms before the PaymentIntent is confirmed. A `processing` PaymentIntent means the debit was submitted, not that payment succeeded; the guide recommends using later webhook status to determine success or failure. ACH has delayed notification, which the guide says can take up to four business days. The guide's sandbox payments settle instantly, unlike live payments that can take multiple days. A bank-generated payment reference is unavailable on pending or failed Charges; after `charge.succeeded`, find it at `charge.payment_method_details.us_bank_account.payment_reference`.

**Target debit date.** The Checkout guide permits a target debit date at least three calendar days and no more than 15 days from the current date, and disallows `verification_method: 'microdeposits'` with it. The schedule is best effort: a weekend or bank holiday date, or fewer than three **business** days of lead time, can move the debit to the next available business day; the customer's bank may process on a different date.

**Disputes and reuse.** The guide says a dispute revokes authorization on the disputed **PaymentMethod**. Future payments reusing that PaymentMethod require resolving the dispute with the customer and obtaining authorization again; the example shows online mandate acknowledgement or offline acceptance via `mandate_data[customer_acceptance][type]=offline`. It separately says Stripe blocks the **same bank account** if the customer disputes **more than one payment from it**. This is not a generic first-dispute mandate deletion or any-account second-dispute rule.

**Sandbox email routing.** For test mandate and microdeposit emails, the guide gives `{username}+test_email@{domain}`, and says a Stripe account must be set up to trigger these emails while testing.

## Historical variant locators

- Checkout: [[raw/stripe-ach-accept-payment-2025|2026-05-02 guide]], lines 8–548; compatibility 18–41, verification 270–280, disputes 409–450, payment reference 452–462, target debit date 530–544.
- Elements with Checkout Sessions API: same guide, lines 549–1504.
- Elements with Payment Intents API: same guide, lines 1505–2512.
- Direct API: same guide, lines 2513–3330; mandate 2836–2842, verification limits 2904, payment status 2968–2984.
- iOS: same guide, lines 3331–4110; Android: 4111–4859; React Native: 4860–5694.
- Webview: same guide, lines 5695–6569; its beta-access notice and mobile OAuth handling are historical statements at lines 5722 and 5977–6127, not current access or implementation guarantees.

## Related raw API references

- [[raw/stripe-payments-ach-direct-debit-accept-a-payment-2026-11-07|2026-11-07 base-URL variant index]] — navigation to Checkout, both Elements variants, Direct API, iOS, Android, React Native, and Webview (lines 9–22). The linked variant contents were not captured in this unit.

## Raw Sources

- [[raw/stripe-ach-accept-payment-2025|Stripe ACH acceptance integration guide, captured 2026-05-02]] — historical multi-variant guide (6569 lines).
