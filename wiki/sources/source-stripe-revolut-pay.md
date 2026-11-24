---
title: "Stripe: Revolut Pay Payments"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/payments/revolut-pay
raw_files:
  - "stripe-payments-revolut-pay-2026-11-07.md"
  - "stripe-revolut-pay-2025.md"
tags: [stripe, wallets, revolut-pay, uk, eu, gbp, eur, ron, huf, pln, dkk, recurring, disputes, manual-capture]
---

## Summary

Revolut Pay (`revolut_pay`) is a wallet with customer-initiated confirmation, support for one-time and recurring payments, Connect, disputes, manual capture and full and partial refunds. Both overviews list standard payout timing. The November 7, 2026 overview describes Revolut account holders paying with their balance or a linked card. On mobile Stripe opens the Revolut app for authentication and confirmation. On desktop the customer scans a QR code with the app and returns to the merchant after confirming.

## Dated customer and authorization scope

The May 7, 2026 opening describes redirection to Revolut's website, with account authentication or first-time checkout, and says non-Revolut customers could save details after their first purchase. The Disputes section on both dates says customers must authenticate by logging in to a Revolut account. The May opening and Disputes section leave the exact guest scope unclear. November's account-holder description leaves subsequent availability of the May option unresolved (May lines 6–10 and 126–130, November lines 7–11 and 126–130).

The separate May acceptance guide already describes mobile redirect and desktop QR authentication after `confirmPayment`. Its Elements testing subsections also describe live-mode automatic approval after mobile redirect or desktop QR scan, in tension with the guide's customer authorization instructions and the November overview. The November acceptance capture lists implementation variants. The browser return alone serves customer navigation. See [[source-stripe-revolut-pay-accept-payment|May acceptance authentication and testing and November selector]] for these scopes (May acceptance raw lines 607–625 and 691–701, November selector raw lines 9–21).

## Locations, currencies and integration

- **Customer locations** in both properties tables are the UK and EU. The 30 separately listed **Stripe-account business locations** are AT, BE, BG, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI and SK. The November opening's EU/UK shorthand sits alongside the detailed table, which includes Liechtenstein and Norway. The November support matrix repeats the distinct account and customer scopes. [[raw/stripe-payments-payment-methods-payment-method-support-2026-11-07|November support matrix, line 69]]
- **Currencies.** Both overviews list EUR, GBP, RON, HUF, PLN and DKK as presentment currencies and describe those six for settlement across the listed accounts, subject to the country table. That table maps GBP to the UK and EUR, RON, HUF, PLN and DKK to the other listed business countries. It gives GBP as the default for UK customers and EUR for other EU customers (May lines 12–97 and 147–154, November lines 13–98 and 148–155).
- **Products.** Both list Connect, Checkout, Payment Links, Elements, Subscriptions and Invoicing. Enable Revolut Pay in Dashboard payment settings for supported Stripe-managed flows. The manual integration has its own acceptance guide. November changes the Elements quickstart destination and switches the demo from the local May video reference to a CDN URL (May lines 89–120, November lines 90–120).

## Refunds and disputes

- **Refunds.** Full and partial refunds are available up to 180 days after purchase. The overviews describe asynchronous refunds taking up to five minutes and a final status event, `refund.updated` or `refund.failed`. The Refund object moves to `succeeded` or `failed`. On failure Stripe returns the funds to the Stripe balance and the merchant must arrange another refund method (both captures line 124).
- **Disputes.** Under Revolut's Buyer Protection Policy, customers have up to 120 calendar days from purchase to file. Stripe notifies the merchant by email and Dashboard, and sends `charge.dispute.created` when webhooks are configured. Stripe holds the disputed amount until Revolut resolves the dispute. Merchants have 14 calendar days to submit requested evidence through Dashboard or can respond via API. Evidence examples include return confirmation, tracking ID, shipping date, purchase IP or receipt for intangible items, and phone number or proof of receipt for services or physical goods. Revolut decides within 35 calendar days **of evidence submission**. Stripe returns the disputed amount to the Stripe balance if the merchant wins, or makes the debit permanent if the customer wins (May lines 126–145, November lines 126–146).

## Related Pages

- [[stripe]]
- [[stripe-wallets]]
- [[stripe-revolut-pay]]
- [[source-stripe-revolut-pay-accept-payment]] — acceptance variants and dated implementation guidance
- [[source-stripe-revolut-pay-set-up-future-payments]] — separate future-payment setup guide
- [[source-stripe-subscriptions-revolut-pay]] — separate subscription integration

## Raw Sources

- [[raw/stripe-payments-revolut-pay-2026-11-07|Revolut Pay overview, captured 2026-11-07]] — full 155-line overview with the hosted demo reference.
- [[raw/stripe-revolut-pay-2025|Revolut Pay overview, captured 2026-05-07]] — full 154-line overview with one italic fix for “webhook” and demo saved to `assets/stripe-revolut-pay-flow.mp4`.
