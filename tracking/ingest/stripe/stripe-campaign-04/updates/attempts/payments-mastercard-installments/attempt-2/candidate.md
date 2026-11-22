---
title: "Stripe: Mastercard Installments"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/mastercard-installments"
raw_files:
  - "stripe-payments-mastercard-installments-2026-11-07.md"
  - "stripe-mastercard-installments-2025.md"
tags: [stripe, mastercard, installments, bnpl, virtual-card]
---

## Summary

Mastercard Installments lets issuers and lenders offer four interest-free payments to customers who already hold a Mastercard Installments virtual card. The merchant uses its existing Mastercard relationship and is automatically enrolled when it starts accepting Mastercard payments. The virtual card works like a regular Mastercard transaction at checkout, with the regular Mastercard fee structure. A merchant cannot surcharge a Mastercard Installments payment.

## Key Details

- **Eligibility.** Customer locations are Australia, Canada, Germany, Malaysia, the United Arab Emirates, the United Kingdom and the United States. A separate Stripe business account list names the same seven jurisdictions (AU, CA, DE, MY, AE, GB and US). The presentment currency list is USD, CAD, GBP, AUD, AED, MYR and EUR. The two captures give no country-to-currency or customer-to-business pairing rules.
- **Features.** Stripe classifies this as Cards, with customer-initiated confirmation and standard payout timing. The properties list support for Connect, disputes, manual capture, and full and partial refunds. The four installments describe the buyer’s financing. The captures give no merchant capture sequence, exact payout schedule or eligible Connect charge types.
- **Recurring payment documentation.** The May and November properties say Yes for recurring payments (May lines 32–34 and November lines 33–35). Each capture’s dedicated recurring section explicitly says purchases of recurring products or subscriptions with this virtual card are declined (May lines 79–81 and November lines 80–82). The documentation does not reconcile the two statements.
- **Additional prohibited business categories.** On top of Stripe’s general restrictions, the captures prohibit money transfer, funding transactions, quasi cash, “Merchandise and services: Customer financial institution”, payment transaction and MoneySend. The captures give category names without numeric codes.
- **Opt-out.** Use the Stripe Support form with the subject `MC Installments Opt Out`. Stripe says the process can take 1–3 days. Submitting a request is separate from opt-out completion (May lines 83–87 and November lines 84–88).

## Related

- [[stripe-installments]] — Mastercard, Mexico and Japan installments
- [[stripe]] — Stripe company profile

## Raw Sources

- [[raw/stripe-payments-mastercard-installments-2026-11-07|Mastercard Installments, captured 2026-11-07]] — full captured page (88 lines); includes the same documented behavior as the May capture
- [[raw/stripe-mastercard-installments-2025|Mastercard Installments, captured 2026-05-01]] — verbatim webpage content
