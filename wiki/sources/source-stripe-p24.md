---
title: "Stripe: Przelewy24 Payments"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/p24"
raw_files:
  - "stripe-payments-p24-2026-11-07.md"
  - "stripe-p24-2025.md"
tags: [stripe, p24, przelewy24, poland, eur, pln, bank-redirect, authenticated, prohibited-categories]
---

## Summary

[[stripe|Stripe]] describes [[stripe-p24|Przelewy24 (P24)]] as a Poland-based aggregator of bank transfers and other payment methods. Both captures limit customer location to Poland, list EUR and PLN as presentment currencies and list 40 business locations. The November 7, 2026 capture separately lists local-currency settlement geographies in AMER, EMEA and APAC, domestic and cross-border coverage and a EUR 0.50 minimum. It supplies no PLN minimum.

## Eligibility and website requirements

The May 3, 2026 capture requires a publicly accessible website or app with priced products or services, business address, tax and registration numbers, and links to refund and privacy policies. It warns that P24 can suspend or terminate access for breaching prohibited categories or the site/app requirements.

The November 7, 2026 capture lists merchant and Connect platform or marketplace account types and B2B and B2C models. It requires a website with address, tax ID, registration number, return and refund policy, privacy policy and terms of service, in addition to Stripe's activation requirements. Stripe may review eligibility after activation and accepts appeals of P24 capability restrictions through support. The November page omits May's public-access and priced-list wording without expressly withdrawing it.

Both captures list ten broadly prohibited categories in addition to Stripe's general restrictions. These cover dropshipping, automotive sales/services/rentals, specialty food retail, pawn shops, higher education/vocational training, healthcare providers/medical services, entertainment/event promotion, IT/telecom, advertising/marketing, and real estate management/brokerage.

November also lists prohibited merchant category codes (MCCs) as unsupported and restricted MCCs as potentially supported with additional information at account creation. Pawn shops (MCC 5933) and new/used car and truck dealers (MCC 5511) illustrate overlaps with the broad prohibition list. The page leaves precedence unresolved. Connect marketplace is a listed account type while marketplaces (MCC 5262) are prohibited at the business-code level. Those labels leave individual eligibility unresolved. The full MCC table and location lists are under **Eligibility and availability** in the November capture.

## Authorization, confirmation and settlement

May labels the family authenticated bank debit and says standard payout timing applies. November labels it a single-use bank redirect and lists immediate payment confirmation, instant provisional access and settlement up to T+2 business days. These describe distinct stages and leave the external merchant payout schedule unspecified. Both captures describe customer bank authorization, a payment notification and no disputes that become chargebacks.

In November's flow the customer is redirected to P24, chooses a bank and completes authorization within one hour of checkout. May explicitly calls the customer's return to the merchant site optional. November lists browser return after the customer is notified of payment completion and leaves optionality unstated. The wording leaves the return requirement unresolved. Verify payment outcome separately from browser return before fulfillment.

## Refunds and payment references

Both captures support full or partial refunds submitted within 180 days of the original payment. The submission window is the payment method maximum, and the merchant return policy determines what it offers. November describes asynchronous, noncancelable processing of up to three business days as a separate bank credit referencing the original statement descriptor. Check the Dashboard or the Refund object's `status` and use refund status events (`refund.updated` or `refund.failed`) for final status. If a refund fails, Stripe returns the amount to the merchant's Stripe balance and the merchant must arrange an alternative refund. Once the Refund succeeds, the merchant can share its `destination_details.p24.reference` when available.

For the original payment, the November **Transaction Identifiers** section says to set a custom statement descriptor on the PaymentIntent before confirmation or use the account-level default. The bank statement shows a unique P24 payment reference followed by the descriptor. After payment completion, expand the PaymentIntent's `latest_charge` and retrieve `latest_charge.payment_method_details.p24.reference`. The separate May 3, 2026 [[source-stripe-p24-accept-payment|acceptance guide]] specifies a 14-character descriptor limit. The November overview gives no length.

## Product support and enablement

The November matrix marks full-page and embedded checkout, Payment Links, Payment Element and in-app payments supported. Express Checkout Element is unsupported. It lists Checkout Sessions and PaymentIntents for payments and excludes SetupIntents, `setup_future_usage`, recurring payments and manual capture.

May excludes Checkout subscription and setup modes and lists Invoicing as invite-only. The November method overview marks Billing and Invoicing supported with a `send_invoice`-only collection note after the matrix whose attachment is unclear. The same-date [[source-stripe-bank-redirects|Bank Redirects matrix]] retains invite-only Invoicing and excludes Checkout subscription and setup modes. It scopes invoice/subscription collection to `send_invoice` and excludes SetupIntents, future usage and manual capture. These captures leave account-level Invoicing access unresolved and document no automatic recurring P24 path.

Use Dashboard payment method settings for Stripe front-end products, where Stripe determines which relevant methods to display. The separate [[source-stripe-p24-accept-payment|acceptance guide]] covers manual configuration. For connected accounts using the Express Dashboard or no Stripe-hosted Dashboard, November directs platforms to request `p24_payments` and verify it is `active` before accepting P24. Enablement and matrix support do not establish an account's or transaction's eligibility.

## Raw Sources

- [[raw/stripe-payments-p24-2026-11-07|Przelewy24 payments, November 7, 2026 full capture]]
- [[raw/stripe-p24-2025|Przelewy24 payments, May 3, 2026 capture]] — verbatim webpage content with six reused flow diagrams from `raw/assets/`.
