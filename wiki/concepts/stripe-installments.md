---
title: "Stripe: Installments"
type: concept
category: technology
tags: [installments, bnpl, mastercard, mexico, japan, cards, recurring-payments]
---

## Definition

Installments are credit card payments where customers split purchases across multiple billing statements. Stripe supports three distinct installment products across different markets.

## Products

### Mastercard Installments

A customer with a Mastercard Installments virtual card can pay in four interest-free installments at checkout. Businesses enroll automatically when they start accepting Mastercard. Regular Mastercard fees apply and surcharging is prohibited. Customer locations and eligible Stripe business-account jurisdictions are separate lists that name the same seven places (AE, AU, CA, DE, GB, MY and US). The May and November 2026 properties mark recurring payments Yes, and both dedicated sections say recurring or subscription purchases with this virtual card are declined. Stripe lists additional prohibited business categories by name. To request opt-out, use the Stripe Support form with subject `MC Installments Opt Out`. Stripe says it can take 1–3 days. See [[source-stripe-mastercard-installments]].

### Mexico — Meses Sin Intereses

Mexico installments require a Stripe Mexico account, payment in MXN above the plan minimum, and a Mexico-issued consumer credit card from a supported issuer. There are six plan lengths from 3 to 24 months, with 5%–22.5% added to the standard card fee. The customer repays the issuer over time, while the merchant receives proceeds net of fees on standard payout timing. Custom minimums and maximums are configurable in the Dashboard. Connect platforms set defaults, and Standard connected accounts can override them.

The May 2026 overview lists 32 issuers. The November overview lists 35 distinct names grouped by plan length, with Inbursa in both the 12- and 18-month groups. Its 18-month availability is unresolved. November adds Terminal at product level. The overview’s hosted and Direct API links lead to Japan. Use the separate [[source-stripe-mx-installments-accept-payment|Mexico guide]], which documents hosted Checkout in `payment` mode and Invoicing for individual invoices. Those May integration limits apply to their paths alongside the overview’s broad recurring-payments property. See [[source-stripe-mx-installments]] for dated issuer and fee details.

### Japan — 分割払い

Japan card installment feature for Japan Stripe accounts processing JPY on Japanese-issued credit cards. The merchant receives full transaction principal as with standard card payments, while the issuer extends credit and collects installments; funds become available on the ordinary card schedule, with standard payout timing.

**3 plan types**: fixed installments, revolving credit, bonus (paid at customer's company bonus cycle).

**Brand support**:

| Brand | Installments | Revolving | Bonus |
| --- | --- | --- | --- |
| Visa/Mastercard | Up to 60 | ✓ | ✓ |
| JCB | Up to 24 | ✓ | ✓ |
| Diners Club | ✗ | ✓ | ✓ |
| Amex | ✗ | ✗ | ✗ (stopped Dec 2022) |
| Discover | ✗ | ✗ | ✗ |

**Bonus windows**: Summer (Dec 16–Jun 15), Winter (Jul 16–Nov 15). Unavailable Jun 16–Jul 15 and Nov 16–Dec 15. Checkout-to-payment cutoff crossing causes payment failure.

**Restrictions**: Japan Stripe account, Japanese-issued credit card (no debit/prepaid) and JPY. Recurring installment payments are unsupported. For other off-session payments, the guide warns against use when the customer does not select the plan at payment; it does not affirm support in any other off-session case.

## Sources

- [[source-stripe-installments]] — installments overview: 3 products (Mastercard, Mexico, Japan)
- [[source-stripe-mastercard-installments]] — four interest-free virtual-card installments, separate customer and account locations, additional prohibited business categories, dated recurring-payment conflict and support-form opt-out
- [[source-stripe-mx-installments]] — Mexico meses sin intereses: 3–24-month plan fees, eligibility, Connect, dated issuer groups and the November Terminal listing
- [[source-stripe-mx-installments-accept-payment]] — May 2026 Mexico integration for Checkout, Elements, Direct API, Invoices and Payment Links, with a November variant index. Both Mexico product overviews list recurring payments as **Yes**. The May guide scopes Checkout to `payment` mode and Invoicing to individual `send_invoice` invoices. The overview property does not specify an eligible recurring integration or support for the excluded subscription and automatic collection routes.
- [[source-stripe-jp-installments]] — Japan installments detail: brand support table, bonus windows, requirements
- [[source-stripe-jp-installments-accept-payment]] — 2026-05-01 Japan installment integration guide for Checkout, Elements, Direct API, Invoices and Payment Links; the 2026-11-07 capture at its canonical URL supplies variant navigation only.
