---
title: "Stripe: Bacs Direct Debit Payments"
type: source
date_ingested: 2026-05-02
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/bacs-debit"
raw_files:
  - "stripe-payments-bacs-debit-2026-11-07.md"
  - "stripe-bacs-direct-debit-2025.md"
tags: [stripe, bacs, bank-debit, uk, gbp, mandates, disputes, connect, custom-branding]
---

## Summary

[[stripe]] Bacs Direct Debit is a reusable, delayed GBP debit from a customer's UK bank account, authorized by a Direct Debit Instruction (DDI) mandate. The 2026-11-07 guide lists many supported merchant business locations, including cross-border business-to-GB-customer coverage, while the 2026-05-02 guide described UK business accounts and outside-UK platforms acting for UK connected accounts. Access requires Stripe approval and additional identity verification; neither a supported location nor enabled UI proves a particular merchant is approved. See [[stripe-bacs-direct-debit]].

## Geography, eligibility, and limits

The November guide lists business locations in the Americas (CA, US), APAC (AU, SG), and multiple EMEA countries, while customer location remains **GB** and presentment currency **GBP**. Its matrix permits merchants and Connect platforms, B2B and B2C, with domestic or cross-border coverage. Stripe may review the account after activation and has prohibited and restricted MCC rows; a restricted MCC may need more account information. The exact location and MCC inventory is at `raw/stripe-payments-bacs-debit-2026-11-07.md:22-80`.

> [!warning] Dated transaction-limit and location change
> May described UK Stripe business accounts, an outside-UK platform path for UK connected accounts, and **100,000 GBP per transaction**. November lists broader merchant locations and a **default 10,000 GBP per transaction**. The separate **10,000 GBP weekly limit for new users** remains; it can increase with processing, and support can consider higher limits. Do not conflate that weekly limit with the default transaction limit or infer account-specific access.

## Mandate and notification boundaries

A debit needs customer mandate acceptance with sort code, account number, name, email, and full address. The Mandate object records business name, acceptance and Bacs reference; `Mandate.payment_method_details.bacs_debit.reference` is a **mandate-level** identifier, not a transaction descriptor. `mandate.updated` requires inspecting `mandate.status` (usable when active); `payment_method.automatically_updated` reports bank-detail changes. A customer can cancel through the business or bank; cancellation invalidates future debits, so a new mandate and details are needed for later payments.

Checkout collects bank details and mandate acceptance; Payment Element cannot create Bacs SetupIntents, for which the guide gives Checkout setup mode as an alternative. **Custom API mandate collection separately requires Stripe approval** and compliance with the exact prescribed checkbox and form requirements, including advance notice and Direct Debit Guarantee content. A mandate/setup confirmation authorizes future debits; it is not payment success.

Bacs requires customer notice when details are collected and confirmed and before each debit. May says Stripe sends both email types by default. November expressly excepts **enterprise accounts with a custom service user number (SUN)** from Stripe's default sending; merchant-sent notices need eligibility and approval. The exception does not remove notification duties or imply every Stripe email is suppressed. Mandate and advance-debit notices are not payment-success receipts.

## Payment processing and outcome

An existing-mandate payment typically takes four business days to confirm; a new-mandate payment can take seven. T+x is measured from submission, which can differ from creation. With an existing mandate, customer debit is typically T+2, **PaymentIntent success** T+3 at 21:00 UTC, and funds available in the Stripe balance T+4 at 00:00 UTC, with a 20:00 London-time cutoff. With a new mandate: mandate submitted T+0, active and payment submitted T+3, customer debit T+5, and funds available T+7. `Charge.payment_method_details` can provide `expected_debit_date`, an estimate rather than a guarantee. A later bank failure can be reported as a dispute even after Stripe marked payment successful.

Use integration-specific events: PaymentIntents have `payment_intent.processing` then `payment_intent.succeeded` or `payment_intent.payment_failed`; Checkout has `checkout.session.completed` then `checkout.session.async_payment_succeeded` or `checkout.session.async_payment_failed`. `checkout.session.completed` means the customer submitted and authorized the form, **not** that the delayed debit succeeded. A Checkout return page should say processing until the success event. Checkout Session expiration defaults to 24 hours and can be configured from 30 minutes to 24 hours; it is separate from the four-to-seven-business-day processing period. The overview gives no distinct custom-integration authorization timeout. These timelines do not prove a specific debit, funds arrival, or native mobile SDK support.

## Refunds and disputes

Submit full or partial refunds within **180 days** of the original payment. They usually take 3–4 business days. Stripe issues a separate credit outside the Bacs scheme, not a debit reversal; if the original Charge is still processing, the refund waits for success or is canceled on Charge failure. A bank dispute after refund can produce a double loss, so avoid simultaneous refund and bank-dispute credits. `refund.failed` with Refund `status`/`failure_reason` is a webhook failure route, not guaranteed email; `refund.updated` with `status=succeeded` or a retrieved Refund status establishes Stripe's refund outcome. `refund.created` and `charge.refunded` alone do not prove success or bank posting. Stripe says it does not emit `refund.succeeded`.

Customers have **no fixed time limit** to dispute, but one Bacs payment can be disputed only once. Stripe gives no fixed lag from bank contact to Stripe dispute creation. On creation, `charge.dispute.created` reports the dispute and Stripe deducts amount plus applicable fee; Dashboard and Dispute `reason` show a reported category, not necessarily detailed customer facts. The business cannot submit evidence, counter, or appeal; the bank's decision is final and the fee is not refunded. A customer who agrees to return funds must make a new payment.

## Product, Connect, branding, and retries

The November matrix lists recurring payments, Billing, Invoicing, Customer Portal, Connect, Checkout Sessions, PaymentIntents, and PaymentIntents with `setup_future_usage`; it excludes SetupIntents and off-session payments, as well as Express Checkout Element, native in-app payments, manual/partial/multi/over-capture, and partial disputes. **Scope tension:** this same page describes recurring mandates, Checkout setup mode, and Subscriptions while its API matrix marks off-session payments and SetupIntents unsupported. Preserve the API/UI distinctions and do not infer that recurring Bacs or the Checkout setup path has been removed, or that Payment Element can create a Bacs SetupIntent.

For Stripe front-end products, the November guide separately directs merchants to **enable Bacs Direct Debit in Payment methods settings**. An integration that manually lists payment methods can configure Bacs as an accepted method. This settings step is scoped to those front-end products; it does not replace platform enablement for Connect or Stripe approval and identity verification for the account.

The **November Connect** description permits supported-location platforms to use destination charges with or without `on_behalf_of`, but says to **enable Bacs Direct Debit on the platform before accepting payments**. Without `on_behalf_of`, the platform is settlement merchant; with it, the connected account must be in a supported business location and have `bacs_debit_payments` capability. Platform enablement, connected-account capability, and Stripe's account approval/identity verification are distinct conditions; satisfying one does not prove the others. The **May guide** separately says UK platforms did not need that capability for UK connected-account destination charges, while outside-UK platforms did, and either needed it with `on_behalf_of`. These are dated, differently scoped statements, not a universal present-day exemption.

Custom Branding shows a business name on bank statements, Checkout and customer emails, and costs **50 GBP per active month**. On Connect, `settings.bacs_debit_payments.display_name` enables it; omitting the display name or using `Stripe` retains Stripe branding. May said new mandates showed the name five business days after request. November says activation **typically takes ten business days** and new mandates after activation show the name. A request is not proof of activation. Bacs has no transaction-level statement descriptor.

The **May** Billing retries section was labeled private preview. The **November** section has no preview label and describes automatic insufficient-funds retries for subscription and/or one-off invoices: at most **two retries within 30 days** of the original attempt, with no debit-failure fee for Stripe-initiated retries. Omission of the old preview label does not prove access for an account. The separate **Pay by Bank Recurring** initial Pay by Bank payment plus Bacs mandate is explicitly **private preview** for Elements/PaymentIntents users; its claimed instant first payment does not change ordinary Bacs confirmation timing.

## Raw Sources

- [[raw/stripe-payments-bacs-debit-2026-11-07|2026-11-07 Bacs overview]] — full newer guide capture (364 lines).
- [[raw/stripe-bacs-direct-debit-2025|2026-05-02 Bacs overview]] — prior full guide capture (218 lines); historical limit, location, Connect, branding and retry claims retained.
