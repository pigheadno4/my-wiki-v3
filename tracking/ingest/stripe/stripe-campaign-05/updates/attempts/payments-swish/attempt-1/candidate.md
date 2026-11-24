---
title: "Stripe: Swish Payments"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/payments/swish
raw_files:
  - "stripe-payments-swish-2026-11-07.md"
  - "stripe-swish-2025.md"
tags: [stripe, real-time-payments, swish, sweden, sek, redirect, qr-code, connect, merchant-of-record]
---

## Summary

The May 6 and November 7, 2026 overviews describe Swish as a single-use real-time method for Swedish customers paying in SEK. Customers open the Swish app through a mobile redirect or scan a desktop QR code, then approve using Swedish BankID. Stripe reports payment success or failure immediately and follows its standard payout schedule. Stripe acts as merchant of record under the factoring addendum. The November overview adds explicit eligibility, authorization, refund tracking and transaction identifier details.

## Access and eligibility

- The November overview lists merchant and Connect platform or marketplace accounts, B2C only, and domestic and cross-border customer payments in the documented locations. The customer must be in Sweden and the amount must be SEK 3.00–150,000.00. Both captures list the same 27 business-account countries: AT, BE, BG, CY, CZ, DE, DK, EE, ES, FI, FR, GR, HR, IE, IS, IT, LI, LT, LU, LV, NL, NO, PL, RO, SE, SI, SK.
- The November overview labels access “Instant provisional access” and also shows an email access request and the identifier `swish_beta_preview`. It directs merchants to Dashboard Payment methods settings for account eligibility. Merchants using Stripe front-end products enable Swish there and Stripe selects relevant methods. See [[source-stripe-swish-accept-payment]] for manual configuration.
- The November MCC table distinguishes prohibited codes from restricted codes that require more information at account creation (new raw lines 41–78). Both captures also list prohibited categories in addition to Stripe's general restricted-business rules (old raw lines 137–152, new raw lines 95–110). These include wine and Champagne producers, alcoholic beverage wholesalers and package stores, pawn shops and salvage yards, art dealers and galleries, real estate rental agents and managers, legal services and attorneys, precious stones and metals, watches and jewelry, and digital wallet top-ups. The broader category list still applies where a category does not appear by name in the MCC table.

## Authorization and outcome

The November overview gives customers three minutes to authorize. On expiration the PaymentIntent returns to `requires_payment_method`. A successful payment reaches `succeeded`. A mobile redirect back to the merchant is part of the customer flow. For fulfillment, the May acceptance guide documents server-side payment outcome events and detachment of the PaymentMethod when a `requires_action` payment expires. Its allowance of up to 20 QR refreshes applies to the May Elements desktop flow. See [[source-stripe-swish-accept-payment]] for those scoped conditions.

## Merchant of record and identifiers

Both captures say Stripe is the payment recipient shown in the Swish app and describe Stripe's name as the bank statement descriptor under the [Swish factoring terms](https://stripe.com/legal/swish). The November overview also documents the following distinct mappings (new raw lines 229–243).

- The Swish **Message** field uses the merchant's legal entity name, falling back to the displayable business name. For destination charges with `on_behalf_of`, it uses the connected account's business name. Stripe removes unsupported characters and truncates the value to 50 characters.
- Set a custom reference via `payment_method_options[swish][reference]` with 1–35 letters, numbers or hyphens. The May acceptance guide describes an order reference shown in the Swish app. For payments processed through PPRO, the November overview says Stripe sends this custom reference as the statement descriptor. PPRO or the customer's bank may display a different value.
- On completed payments, the provider returns a distinct bank reference at `latest_charge.payment_method_details.swish.payment_reference` when the PaymentIntent's `latest_charge` is expanded.
- Both captures list Connect direct charges, destination charges, and separate charges and transfers. November describes general descriptor ownership as connected-account for direct charges. Destination charges and separate charges and transfers use the connected account with `on_behalf_of` and the platform otherwise. Those general settings do not control the Swish Message or PPRO reference mapping.

## Refunds and disputes

Both overviews document full and partial refunds up to 365 days after payment completes, with multiple partial refunds capped at the original amount. A refund usually takes a few minutes. The November matrix labels the window “1 year” and leaves processing time blank. Its prose retains the precise 365-day window and the usual timing estimate.

November describes asynchronous refunds. Stripe tracks the provider outcome, which merchants can inspect in the Dashboard or the Refund object's `status`. Stripe reports the final status through `refund.updated` or `refund.failed`. On failure the amount returns to the merchant's Stripe balance and the merchant must refund through another method. Swish lacks standard disputes, so customers with concerns contact the merchant.

## Product and API scope

Both Swish overviews list Payment Links alongside Checkout and Elements, and both exclude Checkout subscription/setup modes and Express Checkout Element. The November method matrix lists full-page Checkout, Payment Links, embedded form, Payment Element, in-app payments and Connect, with Checkout Sessions recommended and PaymentIntents supported. It excludes Managed Payments, Billing, Invoicing, Customer Portal, Radar, Terminal, PaymentIntents with `setup_future_usage`, and SetupIntents. November also lists no recurring payments, manual or partial capture, multi-capture, over-capture or the listed authorization adjustments.

The May and November cross-method tables instead mark Payment Links unsupported and list Subscriptions as supported only with `send_invoice`, while listing Invoicing as unsupported. The November Swish method page explicitly excludes Billing and Invoicing. Treat the subscription cell as a dated cross-method label. Both method captures exclude recurring payments. See [[source-stripe-real-time-payments]] for the separate comparison and the Swish cells at [[raw/stripe-real-time-payments-2025|May raw lines 24–32]] and [[raw/stripe-payments-real-time-2026-11-07|November raw lines 25–34]].

## Related

- [[stripe]]
- [[stripe-real-time-payments]]
- [[source-stripe-swish-accept-payment]]
- [[source-stripe-real-time-payments]]

## Raw Sources

- [[raw/stripe-payments-swish-2026-11-07]] — November 7, 2026 method overview (249 lines). Flow diagrams use CDN links.
- [[raw/stripe-swish-2025]] — May 6, 2026 method overview (164 lines). No italic fixes. Both PNG flow diagrams were downloaded from CloudFront to `assets/`.
