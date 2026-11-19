---
title: "Stripe: Alma Payments"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/alma"
raw_files:
  - "stripe-payments-alma-2026-11-07.md"
  - "stripe-alma-2025.md"
tags: [stripe, bnpl, alma, buy-now-pay-later, europe, installments, connect, disputes]
---

## Overview

Stripe's Alma overview describes a single-use buy now, pay later method for eligible European B2C purchases. Customers are redirected to Alma to select two, three, or four installments. Stripe describes immediate payment confirmation and upfront availability of the amount minus fees, while the 2026-11-07 property matrix separately labels settlement as **up to three business days (T+3)**. The 2026-05-06 page instead labeled T+3 as **payout timing**. These date-specific terms should not be collapsed into instant settlement or a guaranteed payout arrival. See [[stripe]] and [[stripe-bnpl]]. (New raw lines 5-16, 650-653; old raw lines 4-12, 36-38, 87-91.)

## Eligibility and payment choices

- The November matrix lists business and customer locations BE, ES, FR, IT, LU, NL; B2C rather than B2B; domestic rather than cross-border; EUR presentment; and a EUR 50–5,000 transaction range. The old capture already listed these six countries, EUR and amount range, and prohibited B2B services. Alma determines cart ranges and geographic option availability and can vary them. Pay in 2, 3, or 4 is described as interest-free; the first installment may be higher based on customer credit factors. Country, range and configuration alone do not establish a particular merchant or buyer's approval. (New raw lines 17-23, 636-703; old raw lines 12-22, 56-65, 87-112.)
- The November page defines **Prohibited** MCCs as unusable and **Restricted** MCCs as potentially usable with additional account information. Its visible MCC table, including many rows labeled “Software,” enumerates **Prohibited** rows only; it shows no Restricted row. Match a business to its actual MCC and account circumstances rather than generalizing a row description to all software businesses. Risk may also make an unlisted business ineligible. The older prohibited-category list includes sole proprietorships, B2B, education, professional services, transportation, travel, telecom/utilities, and veterinary services. (New raw lines 24-42, 44-634; old raw lines 101-114.)
- The account-type checkmark for platforms/marketplaces does not mean all Connect platforms are eligible. Both captures restrict Alma to online marketplaces such as Deliveroo or ManoMano and exclude platforms that merely onboard other businesses to accept payments directly, such as Shopify or Squarespace. Online marketplaces must request onboarding in Dashboard. Destination, separate charges and transfers, direct charges, and `on_behalf_of` appear in the Connect charge table for eligible marketplace businesses. (New raw lines 19-22, 827-837; old raw lines 152-162.)

## Product and transaction boundaries

- The November matrix lists full-page Checkout, Payment Links, embedded form, Payment Element, and in-app payments as supported; Checkout Sessions are the recommended API and PaymentIntents are supported. It marks Express Checkout Element, Payment Method Messaging Element, Billing, Invoicing, Customer Portal, Terminal, SetupIntents, PaymentIntents with `setup_future_usage`, and off-session payments unsupported. The method is single-use with no recurring payments. The old page already listed no recurring payments, manual capture, Connect and Dashboard-enabled Checkout/Elements/Payment Links. The accept-a-payment link is a route to a separate guide, not proof of a completed integration. (New raw lines 12-16, 705-730, 793-817, 861-865; old raw lines 24-54, 72-85.)
- Manual and partial capture are supported; multi-capture, over-capture, extended and incremental authorization variants are marked unsupported in the November matrix. The overview does not specify the separate integration guide's timing or execution steps. (New raw lines 705-719.)
- Alma payment-method details include `transaction_id` and `installments.count`. Use `transaction_id` to cross-reference Alma records. To reference the underlying Charge, expand `latest_charge` on the PaymentIntent; these are different identifiers and objects. A redirect, installment selection or product-support checkmark does not establish payment success. (New raw lines 839-859.)

## Refunds, disputes, and customer terms

- Full and partial refunds must be submitted within 180 days of the original payment. Processing is asynchronous and can take up to five minutes; Alma refunds cannot be canceled. Check the Refund object's `status` or `refund.updated`/`refund.failed` events for final outcome. A failed refund returns the amount to the Stripe balance and requires another way to refund the customer. The old capture already stated the window, asynchronous timing and events; the no-cancel rule and explicit retrieve route appear in November. Submission itself does not prove a refund succeeded. (New raw lines 721-741; old raw lines 125-127.)
- Customers have up to 120 calendar days from purchase to dispute. The merchant has 14 calendar days to submit evidence; Alma decides within 25 calendar days after evidence submission. The old guide already described email, Dashboard and `charge.dispute.created` notifications, Dashboard evidence, and an API response route. November adds detailed Dashboard/Disputes API/File API submission steps, a refund-record evidence example, and says dispute fees are nonrefundable regardless of outcome. Stripe holds the disputed amount until decision. (New raw lines 743-783; old raw lines 129-148.)
- Alma's fraud-loss coverage is specifically for **customer fraud**. Alma may ask the merchant to stop or pause shipment, and elevated fraud or dispute rates may cost access. This qualification was present in May and remains in November. It does not guarantee a merchant's outcome in a particular dispute. (New raw lines 785-791; old raw lines 131, 150.)
- Alma requires four clauses in merchants' general terms of sale: installment availability, Alma terms, possible cancellation on non-approval, and a 14-day withdrawal period. This was already in the May page. (New raw lines 818-825; old raw lines 116-123.)

## Raw Sources

- [[raw/stripe-payments-alma-2026-11-07|Alma payments, 2026-11-07]] — full November overview with eligibility, MCC, capability, product, refund, dispute and identifier sections.
- [[raw/stripe-alma-2025|Alma payments, 2026-05-06]] — retained earlier overview and original historical wording.
