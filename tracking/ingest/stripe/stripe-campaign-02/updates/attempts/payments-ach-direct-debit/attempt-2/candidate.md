---
title: "Stripe: ACH Direct Debit"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/ach-direct-debit"
raw_files:
  - "stripe-payments-ach-direct-debit-2026-11-07.md"
  - "stripe-ach-direct-debit-2025.md"
tags: [stripe, ach, us-bank-account, bank-debit, mandates, disputes, refunds, financial-connections, connect]
---

## Summary

ACH Direct Debit is a reusable, delayed-notification, nonguaranteed debit from a customer's US bank account, presented in USD. A bank-account verification or the page's “instant provisional access” label is not final debit confirmation or funds settlement. The 2026-11-07 capture lists US customers and bank accounts, but eligible merchant locations include listed European countries and the US, with Canada in private preview; it also lists crossborder coverage and local-currency settlement for eligible Stripe accounts. This is a dated product and eligibility statement, not proof of access for an individual account.

## Eligibility, billing details, and support

- **Customer and transaction scope:** US customer location and bank account, USD presentment, domestic or crossborder coverage, minimum 0.50 USD (new raw lines 58–98). The page lists restrictions for some UK and EU business categories and says accounts might be reviewed after activation. Canadian business location is labeled private preview.
- **Billing details:** `billing_details` must include the account holder's name. Include a complete address when the merchant of record is outside the US; that address condition is not unconditional (new raw line 15).
- **Captured product support:** The page lists full-page Checkout, Payment Links, embedded Checkout, Payment Element, Billing, Invoicing, Radar and Connect, with Checkout Sessions and Payment Intents/Setup Intents API paths. It marks Express Checkout Element, in-app payments, Managed Payments, Customer Portal and Terminal unsupported in this capture (new raw lines 340–362). This does not establish a particular account's entitlement.
- **Comparison:** Instant Bank Payments is a separate Link-only route with instant confirmation and Stripe-guaranteed bank-initiated returns; ACH Direct Debit can take up to four business days to acknowledge success or failure (new raw lines 9, 22–27).

## Timing and verification

- Standard settlement is T+4 business days from payment creation, with a 21:00 US/Eastern cutoff. Faster T+2 uses a 14:00 US/Eastern cutoff and is available only to eligible US users; eligibility and activation are checked in Payment method settings. Settlement means funds become available in the Stripe balance; bank payout then follows the account's payout schedule (new raw lines 29–40). The `expected_debit_date` is an estimate, and temporary Financial Connections account numbers may delay initial settlement (new raw lines 33–35).
- The bank account must be verified before use. Financial Connections can link an account; manual entry may use hosted microdeposit verification. The customer has 10 days to verify microdeposits, after which the PaymentIntent or SetupIntent needs new payment-method details (new raw lines 330–338). Neither verification nor provisional access guarantees the subsequent debit.
- ACH transactions can fail during processing; a rare late bank failure can occur even after a PaymentIntent reaches `succeeded`. Stripe describes specific failure reasons and a fee in that situation (new raw lines 312–328).

## Mandates and blocked accounts

Customer authorization through a mandate is required before debit. Checkout, Payment Element and the hosted invoice page display the online mandate and record acceptance. A custom Payment Intents form must display mandate terms before confirming the PaymentIntent or SetupIntent. For recurring preauthorized debits, the capture requires amount disclosure or an expected range and at least seven calendar days' notice when timing changes (new raw lines 211–265).

Nacha requires an electronic or hard copy of the mandate. When a billing email is provided, Stripe defaults to sending mandate confirmation; it also sends a microdeposit notification if microdeposit verification is needed. If the merchant sends custom notifications, the guide calls for mandate confirmation and separate microdeposit reminder emails (new raw lines 267–306). It does not require every customer to have an email address.

Mandates can become inactive after disputes, some failures or blocked bank-account status. A `payment_method.automatically_updated` event can expose `us_bank_account.status_details.blocked`; reuse after the block lifts still requires an active or newly collected mandate (new raw lines 99–107, 308–310).

## Refunds

The 2026-11-07 capture marks full refunds supported and **partial refunds unsupported**, with a 180-day submission window. Its prose says ACH refunds are asynchronous and take **up to three business days** to complete, cannot be canceled, and are submitted only after the original payment succeeds (new raw lines 125–150). Refunds are a separate credit, not a reversal or explicitly labeled refund on the bank statement. Track the Refund status and `refund.updated` or `refund.failed`; if a refund fails, arrange another way to return funds. A refund does not prevent a dispute and can create a double credit if a bank dispute proceeds.

> [!warning] Contradiction
> The 2026-05-02 capture listed “Refunds / Partial refunds” as “Yes / Yes” and said refunds require **at least three business days** (old raw lines 57–59, 383–385). The 2026-11-07 capture instead marks partial refunds unsupported and says **up to three business days** (new raw lines 125–138). The captures do not establish the effective change date or the behavior of an individual historical transaction; verify the relevant account and payment before promising refund options or timing.

## Disputes and proof-of-authorization inquiries

A customer can generally dispute a personal-account debit within 60 calendar days or a business-account debit within two business days. A final ACH dispute in these windows cannot be contested or appealed through the ACH network; rare late returns are managed and decided by the banks. A dispute invalidates that payment method's mandate; collect new authorization before another charge. If a subsequent payment from the same bank account is disputed, Stripe blocks that bank account from further reuse (new raw lines 154–182; same-account scope also stated in the 2026-05-02 [[source-stripe-ach-accept-payment]] guide).

**A requested proof-of-authorization inquiry is a separate predecision process.** For some late returns, Stripe can request evidence with `warning_needs_response` and a deadline. Stripe-hosted mandates are answered by Stripe; custom Payment Intents mandates may require the merchant to provide authorization proof. Submit evidence only when requested, and only once; the bank determines the outcome. Evidence for an inquiry is not a way to appeal a final dispute (new raw lines 174–209). [[source-stripe-ach-accept-payment]] also routes the ACH integration context.

## Connect, retries, and descriptors

Connect requires `us_bank_account_ach_payments` active on the platform and relevant connected accounts. Charge type can change merchant of record, mandate and email identity, and which account's statement descriptor appears. Cloning a bank PaymentMethod duplicates the mandate but sends no new confirmation email; disclose that authorization extends to connected accounts. A mandate authorized `on_behalf_of` one connected account cannot be reused with another (new raw lines 365–387, 421–444). Settlement speed control also differs by account and charge type (new raw lines 47–56).

Stripe Billing's enabled insufficient-funds Direct Debit retries can run at most twice within 40 days of the original attempt; the new capture says Stripe-initiated automatic retry attempts incur no debit-failure fee (new raw lines 395–401). This does not waive the separate late-failure fee described above.

The merchant's statement descriptor appears on the bank statement and may be set dynamically per PaymentIntent. The capture describes first-16-alphanumeric-character truncation and disallows `<`, `>`, `'`, and `"`; Connect charge type determines which account's descriptor appears (new raw lines 421–444).

## Historical testing details

The 2026-05-02 capture includes sandbox transaction-email addressing, manually entered bank-account test numbers, microdeposit values and descriptor codes, and the distinction that test transactions settle instantly while live transactions can take days (old raw lines 455–502). These are sandbox examples, not live settlement evidence.

## Related

- [[stripe-ach-direct-debit]] — ACH concept and reciprocal source route
- [[source-stripe-ach-accept-payment]] — ACH acceptance integration guide
- [[source-stripe-ach-set-up-payment]] — saving a bank account for future payments

## Raw Sources

- [[raw/stripe-payments-ach-direct-debit-2026-11-07|2026-11-07 ACH Direct Debit capture]]
- [[raw/stripe-ach-direct-debit-2025|2026-05-02 earlier ACH Direct Debit capture]]
