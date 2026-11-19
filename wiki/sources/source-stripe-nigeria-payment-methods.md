---
title: "Stripe Docs — Nigerian payment methods"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/countries/nigeria"
raw_files:
  - "stripe-payments-countries-nigeria-2026-11-07.md"
  - "stripe-nigeria-payment-methods-2025.md"
tags: [stripe, nigeria, naira, local-payment-methods, merchant-of-record, bank-transfer, wallets]
---

## Overview

[[stripe]] describes Nigerian local payments through a **Nigerian partner acting as merchant of record**, so a business using this route does not need a local Nigerian entity. A customer starts on Stripe's checkout page, then clicks Pay and is redirected to the partner and its local processor's localized checkout to complete payment. This partner-MoR route is distinct from [[stripe-managed-payments]], where Stripe is the merchant of record. See [[stripe-nigeria-payment-methods]]. [May raw lines 4-14; November raw lines 5-15]

## Scope and access

- The captured page identifies Nigerian customers, NGN presentment, and **US Stripe accounts** accepting Naira payments with USD settlement. It lists customer-authenticated confirmation, standard payout timing, Connect support, manual capture, and full/partial refunds at the family-property level. These statements do not establish a particular account's entitlement or a transaction outcome. [May raw lines 27-73; November raw lines 28-74]
- The November capture adds an **invite-request** section. Its example posts a business email to a preview registration endpoint; this is an invitation request, not proof of invitation, activation or approval. Dashboard payment-method enablement, Checkout/Elements/Payment Links navigation and Payment Intents API navigation are separate integration surfaces, not substitutes for access approval. No registration request was made here. [November raw lines 76-103]
- When the Nigerian merchant-of-record provider processes a local transaction, the page says that provider remits customer VAT and that presentment pricing should include VAT. This condition belongs to this partner-MoR route; it is not a blanket claim about every Nigeria transaction or Stripe Managed Payments. [May raw lines 23-25; November raw lines 24-26]
- The customer is redirected to the partner's localized experience. **After authorization and approval**, the guide says funds become available in the Stripe account after three days. This is distinct from its separate standard-payout-timing property; initiating a redirect does not prove approval, funds availability or payout. [May raw lines 49-51, 92-94; November raw lines 50-52, 105-107]

## Dated payment-method matrix

| Method | May 2026 one-time / recurring | November 2026 one-time / recurring |
| --- | --- | --- |
| Naira card | Yes / Yes | Yes / Yes |
| Naira bank transfer | Yes / Coming soon | Yes / No |
| Naira wallet | Coming soon / No | No / No |

The November overview prose nevertheless says businesses can accept a selection of local wallets and cards, while its specific Naira wallet matrix cell says No for both one-time and recurring. The exact wallet route or availability is unresolved in this capture. “Coming soon” is May's historical wording; November's “No” is the captured table status, not evidence that a live wallet or recurring bank-transfer feature was withdrawn or will never launch. The generic “Recurring payments: Yes” property applies at the family level and is narrowed by the card Yes/Yes versus transfer/wallet cells. [May raw lines 45-47, 96-104; November raw lines 9-11, 46-48, 109-117]

## Refund and dispute boundaries

The page allows full and partial refunds and says they can only be **submitted** within 365 calendar days of the original charge. Some Nigerian method transactions can take up to seven calendar days from purchase to return a refund status; submission is not a completed refund. Customer-initiated disputes cannot be challenged through this route. Funds are removed immediately **when Stripe is notified that the relevant payment service provider has accepted a request** to return customer funds, not merely when a customer complains; resolve directly with the customer. These conditions persist across both captures. [May raw lines 65-67, 106-114; November raw lines 66-68, 119-127]

## Related

- [[stripe-nigeria-payment-methods]] — method scope, dated matrix and integration routes
- [[stripe-managed-payments]] — distinct Stripe-as-MoR product
- [[source-stripe-local-payment-methods-by-country]] — country-method hub
- [[source-stripe-ng-card-accept-payment]] — card integration guide
- [[source-stripe-ng-bank-transfer-accept-payment]] — bank-transfer integration guide

## Raw Sources

- [[raw/stripe-payments-countries-nigeria-2026-11-07|2026-11-07 full Nigeria methods overview]] — 127 lines; invite request and revised method matrix
- [[raw/stripe-nigeria-payment-methods-2025|2026-05-08 Nigeria methods overview]] — 114 lines; earlier “Coming soon” table statuses
