---
title: "Stripe: MB WAY Payments"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/mb-way"
raw_files:
  - "stripe-payments-mb-way-2026-11-07.md"
  - "stripe-mb-way-2025.md"
tags: [stripe, wallets, mb-way, portugal, eur, phone-number, disputes, connect, refunds]
---

## Summary and eligibility

[[stripe|Stripe]] documents MB WAY (`mb_way`) as a phone-number-based [[stripe-wallets|wallet]] for customers in Portugal, with EUR presentment. International numbers can be linked to the wallet, and most customers use a Portuguese +351 number. The May 7 and November 7, 2026 captures list the same 40 business locations, including Mexico, Hong Kong, Japan, New Zealand and the United States. The November overview qualifies those locations by supported settlement currency and marks domestic and cross-border payments and B2C supported, with B2B unsupported.

Both captures document EUR 0.50–5,000 per payment and a EUR 1,000 default daily cumulative user limit, adjustable in the app up to EUR 10,000. November describes single use, instant access and immediate confirmation with the standard payout schedule. These are documented properties, with account eligibility and actual payout separate.

## App authorization and payment status

The customer enters the linked phone number and receives a push in the MB WAY app. November specifies approval within four minutes. The merchant page remains open and polls payment state without a browser redirect or return URL. Desktop customers approve on their phone. Mobile customers switch to the app and then back to the merchant page. The captured flow describes Stripe updating the page upon confirmation. Check payment status separately from app approval or a customer's return to the page.

The [[raw/stripe-changelog-endive-2026-09-30-handle-next-action-mb-way-bizum-ui-2026-11-07|Endive Stripe.js changelog]] separately documents pending authorization instructions in `stripe.handleNextAction`. Previous Stripe.js major versions retain the earlier wait behavior. The modal is a version-qualified client change, separate from the overview's merchant-page polling and payment result.

## Product, capture and Connect boundaries

- The May overview specifically excludes Mobile Payment Element and Checkout subscription/setup mode and saved details during payment (`setup_future_usage`). November lists Checkout for one-time payments, with setup mode unsupported, and supports Checkout Sessions and PaymentIntents while excluding SetupIntents, `setup_future_usage` and off-session payments. Both rule out automatic recurring payments.
- November marks Billing and Invoicing supported through `send_invoice` only. Customers authorize each hosted invoice payment, including invoices on subscriptions. The separate [[raw/stripe-changelog-dahlia-2026-07-29-hosted-invoice-page-mb-way-support-2026-11-07|2026-07-29.dahlia changelog]] documents Dashboard enablement or the Invoice and Subscription `payment_settings.payment_method_types` field, with `collection_method=send_invoice`.
- The November matrix lists in-app payments as supported. Its broader category leaves individual SDKs, variants and account availability unresolved. See [[stripe-ios-sdk]] for the separate iOS `26.6.0` PaymentSheet evidence. The November base [[source-stripe-mb-way-accept-payment|acceptance guide]] only routes to Checkout, Elements and Direct API variants. Its navigation neither extends the May web Elements beta wording nor resolves the mobile scopes.
- Manual capture remains unsupported. The November matrix also excludes partial, multi and over-capture and lists unsupported authorization variations under **Capabilities**.
- Stripe front-end integrations can enable MB WAY in Dashboard payment settings. Stripe then selects relevant methods to display. For manually configured methods, see [[source-stripe-mb-way-accept-payment]]. Both captures say a Connect platform supports all charge types. Connected accounts with full Dashboard access can enable MB WAY there. For Express Dashboard or a dashboard hosted outside Stripe, request `mb_way_payments` through the Capabilities API. Check that the account's capability is `active` in the account API or webhooks.

## Disputes, refunds and statement text

**Disputes.** November supports full disputes and excludes partial disputes. A customer can dispute suspected fraud, duplicate payments or order-to-charge differences. Stripe notifies via email, Dashboard and `charge.dispute.created`, and holds the disputed amount until resolution. Submit evidence within seven calendar days. Stripe returns the held amount if the merchant wins. If the customer wins, the balance charge becomes permanent.

**Refunds.** Issue full or partial refunds up to 365 days after the payment completes. Multiple partial refunds cannot total more than the original payment. Processing typically takes minutes. November documents return to the original method and tracking through the Dashboard or the Refund object's `status`, with `refund.updated` or `refund.failed` events for final status. Failed refunds return the amount to the Stripe balance, and the merchant must refund the customer another way.

**Statement descriptors.** In May, `statement_descriptor` is ignored and the guide says `Stripe Inc` appears with the amount. November says Stripe's name appears and that PaymentIntent, account and Connect descriptors do not override it.

## Raw Sources

- [[raw/stripe-payments-mb-way-2026-11-07|MB WAY payments, November 7, 2026 full capture]]
- [[raw/stripe-mb-way-2025|MB WAY payments, May 7, 2026 capture]] — 177 lines of webpage content, with `*sandbox*` corrected ×1. One stripecdn `.mp4` video was skipped for download and its link was retained.
