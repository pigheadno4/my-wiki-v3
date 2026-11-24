---
title: "Stripe: Satispay Payments"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/payments/satispay
raw_files:
  - "stripe-payments-satispay-2026-11-07.md"
  - "stripe-satispay-2025.md"
tags: [stripe, wallets, satispay, italy, eur, disputes, refunds, connect]
---

## Summary

Satispay is a stored-value wallet on [[stripe|Stripe]] for customers in Italy, with EUR presentment. The November 7, 2026 guide describes selection at checkout, a redirect to a Satispay-hosted page, identification by phone request or QR code, in-app approval, immediate confirmation and return to the merchant site. Stripe gives immediate outcome notification and pays out on its standard schedule. In a manual-capture integration, verify capture separately from app approval.

## Account and payment eligibility

- **May 8, 2026.** The method guide lists 20 business account locations in the euro area: AT, BE, CY, DE, EE, ES, FI, FR, GR, HR, IE, IT, LT, LU, LV, MT, NL, PT, SI and SK.
- **November 7, 2026.** The listing adds AU, BG, CA, CH, CZ, DK, GB, HK, HU, JP, LI, NO, PL, RO, SE, SG and US, for 37 locations. The guide lists merchant and Connect platform or marketplace accounts, B2C only, and instant provisional access. It lists domestic and cross-border payments with EUR 0.50 to EUR 999,999.99 limits. Customer location remains Italy. See May lines 12–38 and 52–75, and November lines 9–21 and 64–82 for eligibility and geography.

The May guide lists 13 named prohibited categories and a discretion catch-all (lines 107–124). The November guide distinguishes prohibited and restricted MCC categories and lists 33 codes, all marked prohibited in the captured table (lines 22–62). The change from labels to codes leaves the current eligibility of omitted May labels, such as Automobile Associations, unresolved.

## Capture and product support

Both guides list manual capture. November also lists partial capture and excludes multicapture, overcapture, extended and flexible extended authorizations, incremental and decremental authorizations, and reauthorizations (lines 86–97). The November table lists full-page and embedded Checkout, Payment Links, Payment Element and in-app payments. It excludes Express Checkout Element, Payment Method Messaging Element, Managed Payments and Terminal (lines 184–201). Enable Satispay in Stripe payment method settings for Stripe front ends. Use the [[source-stripe-satispay-accept-payment|acceptance guide]] for the separate integration routes.

## Recurring payments and mandates

The May method guide marked recurring payments unsupported and listed Subscriptions among products where Satispay could be added through the Dashboard (lines 28–30 and 98–105). The May 8 wallet product matrix separately marks Subscriptions, Invoicing and Customer Portal unsupported (header line 184 and Satispay row 199). The May acceptance guide's Checkout and Elements with Checkout Sessions tables specify payment mode and exclude setup and subscription modes (lines 18–32 and 95–109). The November acceptance root lists variants.

The November 7 method guide lists reusable and recurring support, PaymentIntents with `setup_future_usage`, SetupIntents, off-session payments, Billing, Invoicing and Customer Portal (lines 11, 84 and 194–208). The November 7 wallet product matrix still marks Subscriptions, Invoicing and Customer Portal unsupported (header line 188 and Satispay row 203). Separately, the [[raw/stripe-changelog-dahlia-2026-06-24-satispay-recurring-payments-2026-11-07|2026-06-24.dahlia changelog]] documents on- and off-session saving with Intent APIs and Satispay under Subscription and Invoice `payment_settings.payment_method_types`. Specific Checkout variant modes, Customer Portal behavior and individual account eligibility remain unresolved.

In the November method guide, the customer authorizes future payments in Satispay. Stripe records the authorization automatically in Checkout or Payment Element and stores a Mandate associated with the PaymentMethod. Satispay collects the authorization directly, and the guide says custom payment flows need no additional mandate language for this method. After a SetupIntent, use its `mandate` ID to retrieve mandate details. After saving through a PaymentIntent, use its `payment_method` ID for future payments. Customer revocation triggers `mandate.updated` and blocks future use of that method. A merchant can instead detach the PaymentMethod to stop future payments. A later charge has its own outcome. See November lines 164–182 and the separate [[raw/stripe-payments-satispay-set-up-future-payments-2026-11-07|future-payment setup routes]].

## Disputes

The May guide gives merchants 12 calendar days to provide evidence and describes cases such as suspected fraud, duplicate payments and order or amount mismatch. The November guide describes full disputes only. Customers have 120 calendar days from purchase to file. Stripe immediately withholds the disputed amount. Merchants have 15 calendar days from dispute creation to provide evidence, and Satispay makes its final decision within 25 calendar days of creation.

Stripe notifies via email, Dashboard and `charge.dispute.created`. Use the Dashboard or the Dispute object's `reason` and `evidence_details.due_by`. Submit evidence through the Dashboard or Disputes API, with supporting files as needed. Examples include shipping and tracking information, proof of purchase and prior refund records. When the merchant wins, Stripe returns the amount to its Stripe balance. A customer win makes the balance charge permanent. See May lines 126–148 and November lines 105–108 and 125–162.

## Refunds

Both guides describe asynchronous full and partial refunds within 180 days, with processing up to five minutes. The November guide says Satispay refunds cannot be canceled, are never processed as reversals and return to the customer's Satispay wallet balance. Track the result in the Dashboard or on the Refund object's `status`; Stripe sends `refund.updated` or `refund.failed` notifications. A failed refund returns the amount to the merchant's Stripe balance and requires another way to refund the customer. See May lines 150–157 and November lines 99–123.

## Connect

The May guide requires `satispay_payments` active on the platform and the connected accounts where Satispay is enabled. For direct charges and destination or separate charges using `on_behalf_of`, it identifies the connected account descriptor. For ordinary destination and separate charges and transfers, it identifies the platform descriptor.

November ties the descriptor in the Satispay app to charge type and describes overriding the account default using `statement_descriptor` when creating a PaymentIntent or `payment_intent_data.statement_descriptor` for Payment Links and Checkout. The May capability and charge-type table remain dated guidance. See May lines 159–179 and November lines 231–237.

## Related Pages

- [[stripe]] — provider overview
- [[stripe-wallets#Satispay Details|Satispay in Stripe Wallets]]
- [[source-stripe-satispay-accept-payment]] — May implementation examples and November variant selector
- [[source-stripe-payment-method-support]] — dated cross-method wallet product matrices

## Raw Sources

- [[raw/stripe-payments-satispay-2026-11-07]] — November 7, 2026 full Satispay method guide
- [[raw/stripe-satispay-2025]] — May 8, 2026 full Satispay method guide and captured demonstration
