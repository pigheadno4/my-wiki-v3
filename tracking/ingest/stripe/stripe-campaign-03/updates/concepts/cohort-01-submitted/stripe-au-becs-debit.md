---
title: "AU BECS Direct Debit (Stripe)"
type: concept
category: technology
tags: [stripe, au-becs, becs, australia, aud, bank-debit, mandates, disputes]
---

## Definition

Australia BECS Direct Debit lets AU businesses pull funds from customers' Australian bank accounts. API enum: `au_becs_debit`. Business-initiated, delayed notification, reusable. Disputes are final and uncontestable.

**Currency**: AUD only. **Country**: AU customers; AU business accounts only.

## Limits

- November 7, 2026 scheme range: 0.50–99,000,000 AUD; the scheme maximum is not an account processing limit.
- Default account limits: 10,000 AUD per transaction and 10,000 AUD per week across AU BECS debits. Actual limits vary with approval and increases; both scheme and account limits apply.
- Contact Stripe support to request higher account limits.

## Settlement

| Settlement | Payment Success | Funds Available | Cutoff |
| --- | --- | --- | --- |
| Standard | T+2 at 00:00 UTC | T+2 at 00:00 UTC | 18:30 Australia/Melbourne |

The May 2, 2026 capture shows customer debit at T+0 only in a sample timeline. Submission can occur after creation when a cutoff or non-business day intervenes. Standard payment success and funds availability are listed at T+2 after submission; the expected debit date is an estimate, not a guarantee. November's final success/failure notification bound is up to 2 business days, versus May's up to 3.

`expected_debit_date` available on `payment_method_details` for Charges (estimated, not guaranteed).

## Mandates (DDR)

Called Direct Debit Requests (DDRs). Require: account holder name, BSB number, account number, mandate Service Agreement acceptance.

Customers can cancel at any time via bank or merchant. Cancellation invalidates future debits — must collect new DDR.

Mandate event: `mandate.updated` fires when mandate is canceled or permanently failed → `status` becomes `inactive`.

## Debit Notification Emails

BECS scheme advises (not mandatory) notifying customers:

1. When mandate is established
2. Before each debit

Stripe sends automatically. Pre-debit email sent day before account is debited. Custom emails: turn off Stripe emails, trigger on `payment_intent.processing`. Suggested 14-day lead time (not mandatory).

Custom email should include: last 4 digits of bank account, amount, contact info, planned debit date.

## Disputes

- **7-year** dispute window, "no questions asked"
- **Final and uncontestable** — must resolve directly with customer
- Stripe sends both `charge.dispute.created` and `charge.dispute.closed`; neither dated overview specifies that the events are simultaneous. Disputes have no inquiry/evidence counter, are final, and the dispute fee is not refunded.
- Risk of double-credit if refund issued while dispute in flight

## Refunds

- Max 90 days from original payment
- May 2, 2026 overview: typically 3–5 business days; November 7, 2026 overview: typically 5 business days. A pending refund begins only after its Charge succeeds and is canceled if the Charge fails. Track final Refund status; a failed refund returns funds to the Stripe balance and requires another customer refund method.
- Full and partial refunds supported
- Labeled as credit (not refund) on bank statement

## Statement Descriptors

Two fields on customer's bank statement:

- **Business name**: comes from the account selected by Connect charge type and `on_behalf_of`; `PaymentIntent.statement_descriptor` changes the payment-specific lodgement reference, not this business name.
- **Lodgement reference**: first 9 alphanumeric chars of descriptor + unique ID (e.g., `RocketRid_AB1234CD`)

Connect `on_behalf_of` changes descriptor source to connected account.

## Product Support

November 7 overview lists full-page and embedded Checkout, Payment Links, Payment Element, in-app payments, Billing, Invoicing, Customer Portal, Radar, and Connect as supported; Express Checkout Element, Payment Method Messaging Element, Managed Payments, and Terminal as unsupported. Its API matrix lists Checkout Sessions, PaymentIntents with or without `setup_future_usage`, and SetupIntents as supported, while also labeling “Off-session payments” unsupported. The scope of that last label is unresolved here; it does not independently override the separate setup and subscription guides.

## Billing Retries

May 2, 2026 overview labeled Billing Retries a private preview. The November 7 overview describes opt-in Direct Debit retries for insufficient-funds failures on recurring subscription or one-off invoices, at most four retries within 30 days of the original attempt, with no debit-failure fee for Stripe-initiated attempts. Neither capture establishes access or enabled status for a particular account. The subscription-guide contradiction below remains unresolved.

## Integration

**Checkout (2026-05-02 full guide)**: Australian customer geography and `aud` prices for every line item; payment, setup, and subscription modes. The guide shows manual `payment_method_types: ['au_becs_debit']` as well as a dynamic-payment-method route. Optional `target_date` is 3–15 days ahead and best effort; nonbusiness dates or dates fewer than three business days out can shift the debit. See [[source-stripe-au-becs-accept-payment]].

**Web Elements (2026-05-02 full guide)**: Two distinct routes are documented: Checkout Sessions API with a server-created Session, client secret and Checkout Elements confirmation; and Payment Intents API with a server-created PaymentIntent, Payment Element and client `stripe.confirmPayment`.

**iOS (2026-05-02 full guide)**: The form collects name, email, BSB and account number and displays BECS Terms; the prose names `STPAUBECSFormView`, while Swift code/delegate name `STPAUBECSDebitFormView`. The guide uses `STPPaymentHandler.confirmPayment` and says to share the mandate URL after confirmation. Verify the SDK symbol before implementation.

**Android (2026-05-02 full guide)**: Prose/layout name `BecsDebitWidget`. The prose names `PaymentLauncher.confirm`, but the Kotlin example passes SetupIntent parameters inside a PaymentIntent section and testing text names `Stripe#confirmPayment()`. The guide does not establish a consistent executable call; see [[source-stripe-au-becs-accept-payment]].

**React Native (2026-05-02 full guide)**: `AuBECSDebitForm` collects details and mandate acknowledgement; its shown client path calls `useConfirmPayment().confirmPayment` using a server-created PaymentIntent client secret. `processing` is distinct from final `succeeded`.

**Test BSB `000000`**: 10 test accounts covering success, delayed success, closed account, no account, refer-to-customer, debit-not-authorized, dispute, weekly/transaction limit.

## Subscription integration

Flow: server SetupIntent → `auBankAccount` Element or React `AuBankAccountElement` and DDR acceptance → `confirmAuBecsDebitSetup()` → share Mandate URL → store the payment method as default on a customer-configured Account v2 or Customer v1 → create subscription. The May 2026 Node.js SetupIntent example selects `au_becs_debit` explicitly; the November 2026 guide enables it in the Dashboard and uses `automatic_payment_methods` for eligible methods. After setup, share the Mandate URL; the guide recommends adding the business name, applicable amount/schedule and DDR link. The accepted DDR and service agreement must remain shareable at all times. Before fulfilling the first payment, require `invoice.paid` or a `succeeded` underlying PaymentIntent **and** an `active` related subscription; `active` alone can precede payment success.

> [!warning] Contradiction
> The May 2026 subscription guide says BECS payments are never automatically retried. The November 2026 guide says Stripe can retry an insufficient-funds AU BECS payment when Direct Debit retries is enabled. The adjacent Billing Retries section records private-preview availability from separate evidence. Do not infer that any account has access or that other BECS failure reasons are retried. See [[source-stripe-subscriptions-becs-debit]].

## Sources

- [[source-stripe-au-becs-debit]] — May 2 and November 7, 2026 full overviews: AU/AUD eligibility, account versus scheme limits, DDR and Connect mandate ownership, processing versus T+2 success, refund/dispute outcomes, debit notices, conditional retries, and descriptor identities; dated differences and off-session matrix ambiguity are qualified there.
- [[source-stripe-au-becs-accept-payment]] — 2026-05-02 full accept-payment guide: Checkout, Elements via Checkout Sessions or Payment Intents, iOS, Android, React Native, test accounts and target_date; 2026-11-07 capture provides variant navigation only
- [[source-stripe-au-becs-set-up-payment]] — 2026-05-02 full save-for-future guide: SetupIntent with DDR, Elements, iOS, Android and React Native; a later separate PaymentIntent attempts a debit. The 2026-11-07 capture adds Direct API navigation without inspected instructions.
- [[source-stripe-subscriptions-becs-debit]] — May and November 2026 AU BECS subscription guide: SetupIntent and DDR, first-payment check, conditional insufficient-funds retry, anchor and trial
