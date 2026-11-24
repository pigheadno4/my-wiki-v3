---
title: "Stripe: TWINT Payments"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/payments/twint
raw_files:
  - "stripe-payments-twint-2026-11-07.md"
  - "stripe-twint-2025.md"
tags: [stripe, twint, switzerland, chf, wallet, bank-redirect, recurring, disputes, connect, onboarding]
---

## Summary

[[stripe]] supports TWINT for Swiss customers paying in CHF through a TWINT app. The November 7, 2026 overview classifies TWINT under Wallets, lists the same 35 eligible business locations as the May 3, 2026 capture, and documents domestic and cross-border business acceptance for B2C transactions with approval. The transaction range is CHF 0.50 to CHF 5,000. Stripe lists immediate payment outcome notification, its standard payout timing, and support for recurring payments.

## Eligibility and onboarding

Before requesting access in the Dashboard or through the Capabilities API, meet the account and website requirements. The business needs a working, public website with its legal name and form, physical address, terms and conditions, and email or phone contact. Sole proprietors must provide the owner's full name. The address must include the street, house number, postal code, and city. Show CHF by checkout, including when using Adaptive Pricing. If you sell physical goods, make Switzerland available as a shipping destination. The website must avoid deceptive marketing. The `twint_payments` capability stays `pending` until verified. The account may be reviewed after activation to confirm eligibility. TWINT can suspend or terminate access for noncompliance. Contact Stripe Support to appeal capability restrictions.

The November overview groups prohibited and restricted merchant category codes by business country. Restricted categories require additional information. Iceland, Monaco, and San Marino appear in the 35 locations, and the guide directs businesses there to Stripe Support for MCC requirements.

## Payment flow and result

In November both mobile and desktop buyers first reach a TWINT-hosted page. On mobile the buyer selects their TWINT app, and on desktop the buyer scans the page's QR code. The buyer approves in the app. The PaymentIntent stays `requires_action` while approval is pending, moves to `succeeded` after success, or returns to `requires_payment_method` after a decline or failure. The latter leaves an incomplete Intent that can be retried. Use the PaymentIntent status to establish the outcome after the browser returns.

The May 3, 2026 capture classified TWINT as a bank redirect and described the merchant website displaying the desktop QR code. See [[source-stripe-twint-accept-payment]] for the separate acceptance guide.

## Mandates and recurring payments

One-time payments require no mandate. The customer can authorize a mandate with a SetupIntent or with a PaymentIntent set up for future use. The mandate allows ad hoc off-session payments without a fixed amount or schedule. One active mandate applies per business and customer. For indirect Connect charges using the platform as merchant of record without `on_behalf_of`, a new mandate for that customer revokes the earlier mandate, including across connected accounts.

Use the customer's saved payment methods in the Dashboard to find active mandates. For a specific payment, read `charge.payment_method_details.twint.mandate` on the Charge. The merchant can detach the saved PaymentMethod, the customer can revoke authorization in the app, and TWINT can revoke it. Stripe updates the Mandate status. See [[source-stripe-twint-save-during-payment]], [[source-stripe-twint-set-up-future-payments]], and [[source-stripe-subscriptions-twint]] for the separate implementation guides.

## Refunds and disputes

Full or partial refunds are available for up to 180 days after completion. Multiple partial refunds can total up to the original payment amount, return to the original payment source, and usually complete within a few minutes. The November guide excludes cancellation and reversals. Check the Refund status or `refund.updated` and `refund.failed` for final status. A failed refund returns funds to the Stripe balance, and the merchant needs another method to refund the customer.

Customers file disputes through their bank. Stripe debits the disputed amount on receipt. The Dashboard provides the reason, evidence deadline, and options to accept or respond. Acceptance or a missed deadline loses the dispute. A win returns the funds to the Stripe balance, while a loss makes the debit permanent. The November matrix supports full disputes and excludes partial disputes. The May capture reported 25–50 disputes per million transactions.

## Products and Connect

The November matrix lists Stripe-hosted and embedded Checkout, Payment Links, Payment Element and in-app integrations, Billing, Invoicing, Customer Portal, Radar, and Connect. It excludes Express Checkout Element, Payment Method Messaging Element, Managed Payments, and Terminal. It lists Checkout Sessions, PaymentIntents, future use, SetupIntents, and off-session payments, with manual capture, partial capture, multicapture, overcapture, and authorization adjustments unsupported.

The May overview named direct charges, destination charges, and separate charges and transfers and described self-service enablement for connected accounts with a full Stripe Dashboard. Check the active capability in the API or a webhook. The November guide says to request `twint_payments` for accounts with an Express Dashboard or without a Stripe-hosted Dashboard and confirm that it is active before accepting payments.

Stripe forwards a custom `statement_descriptor` to TWINT, which may choose whether to display it. The default name is the connected account for direct charges and charges using `on_behalf_of`, or the platform for destination charges and separate charges and transfers without `on_behalf_of`.

## Related Concepts

- [[stripe-twint]]

## Raw Sources

- [[raw/stripe-payments-twint-2026-11-07|November 7, 2026 TWINT overview]]
- [[raw/stripe-twint-2025|May 3, 2026 TWINT overview]]
