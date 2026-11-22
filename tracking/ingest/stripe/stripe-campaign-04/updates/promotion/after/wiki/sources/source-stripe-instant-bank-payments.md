---
title: "Stripe Docs — Instant Bank Payments"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/link/instant-bank-payments"
raw_files:
  - "stripe-payments-link-instant-bank-payments-2026-11-07.md"
  - "stripe-instant-bank-payments-2025.md"
tags: [stripe, instant-bank-payments, link, ach, bank-debit, us-only, recurring, guaranteed-settlement, cash-back]
---

## Summary

The May 8 and November 7, 2026 guides describe Instant Bank Payments as a Link option for eligible US customers using a US bank account in USD. Enabling Link also enables this method subject to business, session and transaction eligibility. Confirmation is immediate. Authorized payments settle to the Stripe balance on the documented two-day card timeline.

## Eligibility and supported integrations

- Stripe dynamically sets a risk threshold per eligible transaction. The May guide gives a default of **under 5,000 USD** and the November guide gives **under 7,500 USD**. Onboarding criteria include being a US business and having Stripe usage history. These are neither exhaustive criteria nor an individual account's guaranteed amount limit.
- Both dedicated guides list Checkout, Payment Links, hosted invoice page, Payment Element and Mobile Payment Element, and mark Connect, manual capture and full or partial refunds supported.
- **Dated mobile disagreement.** The May 2 [[source-stripe-bank-debits|bank-debits overview]] marks the combined Instant Bank Payments-or-ACH row supported for Mobile Payment Element. The November 7 overview marks that combined row unsupported, while both dedicated Instant Bank Payments guides still list Mobile Payment Element. The combined row does not isolate the method or client route. Current SDK-specific support, account eligibility and runtime removal remain unverified.

## Checkout, reuse and settlement

A new Link customer selects a bank, accepts the Link terms, signs up or in with email, and authenticates with the bank. A returning customer authenticates with Link 2FA and can select a saved account. Returning from bank linking precedes completing the transaction. After the customer authenticates and **completes their first Link transaction**, the guides describe charging the saved bank account for future recurring or off-session payments without reauthentication.

The settlement guarantee applies to an authorized Instant Bank Payment when the bank initiates an ACH return. If the customer disputes through their bank, Stripe debits the payment amount and dispute fee from the Stripe balance. The guide routes responses through the same Dashboard workflow used for cardholder disputes. The November capture adds navigation to [dispute evidence by return code](https://docs.stripe.com/payments/link/instant-bank-payments/disputed-payments). Payment confirmation, settlement to Stripe balance and external payout are separate events.

## ACH Direct Debit precedence

[ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit) takes precedence when both options would be offered for the same transaction. The explicit request input is the ACH enum `us_bank_account`.

- **May 8 guide.** The dedicated instructions name `payment_method_types` for Checkout Session, PaymentIntent and SetupIntent.
- **November 7 guide.** The dedicated instructions still name `payment_method_types` for Checkout Session and use `allowed_payment_method_types` for PaymentIntent and SetupIntent.
- **Dynamic payment methods.** When a transaction qualifies for ACH, Link suppresses Instant Bank Payments. A payment-method rule can narrow ACH eligibility. Transactions outside that ACH rule can show Instant Bank Payments if they independently qualify. The guides recommend ACH Direct Debit for businesses that can wait up to four business days for confirmation.

**Separate Endive request rules.** The [Checkout Session changelog](https://docs.stripe.com/changelog/endive/2026-09-30/remove-payment-method-types-checkout-sessions) documents HTTP 400 for the writable `payment_method_types` field on Checkout Session Create in `2026-09-30.endive`, despite the dedicated November guide's Checkout wording. Its alternatives are dynamic methods and `allowed_payment_method_types` or `excluded_payment_method_types`. The compatible subset appears in the computed response property. The changelog leaves ACH precedence with a Checkout Session Endive allowlist unverified.

The separate [Intents changelog](https://docs.stripe.com/changelog/endive/2026-09-30/removes-the-payment-method-types-parameter-from-payment-intents-and-setup-intents) documents HTTP 400 with `payment_method_types_no_longer_supported` for writable use on the listed Endive PaymentIntent create/update/confirm and SetupIntent create/update REST endpoints. The computed response property remains readable. Its Impact paragraph separately names `2026-08-26.preview`; the endpoint links and REST table identify `2026-09-30.endive`. Allowed lists filter incompatible methods.

## Link route selection and PaymentMethod responses

The separate [[source-stripe-link-payment-integrations|Link integration guide]] describes both Instant Bank Payments representations. Link as a payment method returns `PaymentMethod.type=link` without the underlying funding method. The card-specific route returns `PaymentMethod.type=card` and `card.wallet.type=link`, with `card.brand=link` for non-card funding such as Instant Bank Payments.

The May Link integration guide uses `payment_method_types` for explicit `link` or `card` route selection. The November Link integration guide names `allowed_payment_method_types`. That selection is distinct from the dedicated guide's `us_bank_account` ACH precedence input and from the versioned Endive request limits. The resulting response representation leaves eligibility and payment status to separate checks.

## Stripe-funded promotions

Stripe can show qualifying US customers cash back or promotional credits according to Link settings. The customer pays the full amount and the business receives the full amount. Stripe separately deposits the promotional amount to the customer's bank account within seven business days.

## Sandbox tests

- **Success, Disputed and Blocked** simulate a successful bank connection with authorization, a subsequent customer-initiated dispute, or a risk decline, respectively.
- The non-OAuth test institution's initial login accepts any input, with sandbox prompts `options`, `mfa`, `confirm_mfa`, `security_question`, `error` and `incorrect`. The OAuth test institution uses a popup to select accounts.
- **Down (Scheduled), Down (Unscheduled) and Down (Error)** simulate unavailable institutions or an unknown communication error.

## May 8, 2026 capture assets (9 screenshots)

- `raw/assets/stripe-ibp-bank-tab.png` — bank selection tab (93 KB)
- `raw/assets/stripe-ibp-consent.png` — Link agreement page (78 KB)
- `raw/assets/stripe-ibp-sign-up.png` — Link sign-up (64 KB)
- `raw/assets/stripe-ibp-oauth.png` — bank OAuth login (132 KB)
- `raw/assets/stripe-ibp-success.png` — success page (29 KB)
- `raw/assets/stripe-ibp-returning.png` — returning customer welcome back (77 KB)
- `raw/assets/stripe-ibp-otp.png` — 2FA code entry (55 KB)
- `raw/assets/stripe-ibp-saved.png` — saved account selection (73 KB)
- `raw/assets/stripe-ibp-settlement-timing.png` — 2-day settlement diagram (13 KB)

## Related Pages

- [[stripe-instant-bank-payments]]
- [[stripe-link]]
- [[stripe-ach-direct-debit]] and [[source-stripe-ach-direct-debit]]
- [[stripe-payment-method-rules]]
- [[stripe]]

## Raw Sources

- [[raw/stripe-payments-link-instant-bank-payments-2026-11-07|November 7, 2026 full Instant Bank Payments guide]] — 185 lines. Checkout and returns at lines 61–117, eligibility and products at 119–137, promotions and ACH precedence at 139–157, and tests at 159–178.
- [[raw/stripe-instant-bank-payments-2025|May 8, 2026 full Instant Bank Payments guide]] — verbatim webpage content, 185 lines, with local checkout screenshots and settlement diagram.
