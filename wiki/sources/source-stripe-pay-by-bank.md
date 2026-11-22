---
title: "Stripe: Pay by Bank Payments"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/pay-by-bank"
raw_files:
  - "stripe-payments-pay-by-bank-2026-11-07.md"
  - "stripe-pay-by-bank-2025.md"
tags: [stripe, real-time-payments, pay-by-bank, open-banking, uk, europe, eur, gbp, connect]
---

## Summary

The May 6 and November 7, 2026 method overviews describe Pay by Bank (`pay_by_bank`) as a single-use open-banking payment. Customers choose their bank and authorize in its app or web portal before returning to the merchant. The regular one-off path lists GBP and EUR presentment, no manual capture and standard payout timing. The default GBP range is £0.50–£10,000. Stripe directs merchants to contact support for larger amounts.

## Bank-account and business eligibility

- **May customer scope.** The overview lists Finland, France, Germany, Ireland and the UK, with France, Germany and Ireland in private preview.
- **November customer scope.** Bank accounts in Finland, Ireland and the UK are generally available. Belgium, France and Germany require private-preview access. UK bank accounts pay in GBP and accounts in the listed European countries pay in EUR. Availability depends on where the account is held and which banks the checkout provides. An account at the same bank in a different country does not qualify under that listing. The November interest-form heading names France and Germany, leaving Belgium's request route unresolved.
- **Merchant scope.** Both snapshots list the same 35 Stripe business locations (AT, AU, BE, BG, CA, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SG, SI, SK, US). This product list is separate from customer bank location, Checkout route eligibility and account activation.
- Enable Pay by Bank in Dashboard **Payment methods** for front-end products. Stripe dynamically selects relevant methods. The separate [[source-stripe-pay-by-bank-accept-payment|acceptance guide]] covers manual configuration with date and route qualifications.

## Product, API and recurring scope

- The product overviews list Connect, Payment Links, Checkout and Elements. Both exclude Checkout subscription mode and Express Checkout Element. The May method overview also excludes Mobile Payment Element. The November method overview omits that exclusion. The separate [[source-stripe-real-time-payments|real-time methods matrix]] changes the Mobile Payment Element cell from unsupported in May to supported in November. Neither the matrix nor the [[source-stripe-pay-by-bank-accept-payment|November acceptance selector]] establishes an SDK version or individual account eligibility.
- The May method overview lists recurring payments as unsupported. The November overview separately describes a request-access **private preview** for Elements with the Payment Intents API. It combines an initial Pay by Bank payment with a Bacs Direct Debit mandate for subsequent payments. For this preview, the guide describes immediate initial confirmation and an initial payout within three business days. It describes the strongly authenticated initial payment as non-disputable and says the preview verifies account ownership and the account holder’s name immediately. These are preview claims for the initial Pay by Bank step. The one-off product and subsequent Bacs debits have separate terms.
- In the separate November real-time matrix, Pay by Bank supports Invoicing and Subscriptions via `send_invoice` and does not support Setup Intents or Payment Intents `setup_future_usage`. The [Clover Billing changelog](https://docs.stripe.com/changelog/clover/2026-02-25/billing-api-pay-by-bank) adds the `pay_by_bank` enum to Billing operations, with REST examples on `2026-02-25.clover` and a separate preview reference for quotes. Enum availability establishes neither automatic collection on a one-off Pay by Bank method nor access to the Bacs-backed preview.

## Notification, transfer and refund outcomes

- **Timing disagreement.** The May 6 [[source-stripe-pay-by-bank-accept-payment|acceptance guide]] describes immediate notification of Pay by Bank success or failure. The April 20 [[source-stripe-checkout-dashboard-payment-methods|Dashboard-managed Checkout migration guide]] lists Pay by Bank among delayed notifications and advises waiting for success or failure when Checkout completion records authorization. Its 2–14 day illustration is generic. Keep bank authorization, browser return, verified success, available funds and merchant payout separate.
- **Late bank funds.** November says an authorized payment can fail with `payment_method_provider_timeout` if the bank funds miss the expected settlement window. Stripe automatically returns funds that arrive after the failure. That return is separate from a merchant-initiated refund or payout.
- **Refunds.** Both captures allow full or partial refunds to the original bank account for up to 730 days. Stripe charges no refund fee and does not return the original processing fee. Check the Refund object and `refund.updated` or `refund.failed` for `succeeded` or `failed`. Failure returns the amount to the Stripe balance and requires arranging an alternative refund.
- **Disputes.** May broadly describes no chargeback process. November specifies that ordinary inadequate-goods or services claims do not lead to a chargeback debiting the Stripe account through this process. The wording gives no general guarantee against all recourse and does not scope later Bacs debits.

## Connect

Both overviews list direct charges, destination charges, and separate charges and transfers. Connected accounts using the Stripe Dashboard can enable the method in Payment methods. For Express or non-Stripe-hosted dashboards, request `pay_by_bank_payments` through the Capabilities API. Check the Accounts API or account webhooks for `capabilities.pay_by_bank_payments` set to `active`. A capability request is separate from approval and activation.

## Detail locators

- November raw lines 17–27, 61–117 and 119–217 cover geography, business locations, preview and the country-specific bank directory. Lines 219–246 cover the customer flow and front-end enablement.
- November raw lines 248–277 cover the Refund object, dispute scope, late transfer and the separate Bacs-backed preview. Lines 279–293 cover Connect charge types and capability.
- May raw lines 14–54, 56–108 and 131–166 cover the historical availability, mobile and recurring exclusions, enablement, refunds and Connect.
- The April Dashboard-managed Checkout raw lines 66–84 and May acceptance raw lines 12 and 139 give the different notification statements. The separate November real-time matrix lines 25–40 and Clover Billing changelog lines 7–23 and 63–74 give product, API and version scope.

## Related

- [[stripe]] — Stripe company and source routes.
- [[stripe-real-time-payments]] — Pay by Bank and other real-time methods.
- [[source-stripe-pay-by-bank-accept-payment]] — May implementation and November variant selector.

## Raw Sources

- [[raw/stripe-payments-pay-by-bank-2026-11-07|Pay by Bank overview captured 2026-11-07]] — full overview with country-specific bank list, timeout, recurring preview and Connect.
- [[raw/stripe-pay-by-bank-2025|Pay by Bank overview captured 2026-05-06]] — verbatim webpage content (166 lines); fixed `*webhook*` ×1; 6 SVG flow diagrams downloaded to assets/
