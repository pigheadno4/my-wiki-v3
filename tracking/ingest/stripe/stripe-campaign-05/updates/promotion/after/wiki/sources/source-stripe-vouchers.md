---
title: "Stripe: Vouchers Overview"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-22
canonical_url: "https://docs.stripe.com/payments/vouchers"
original_format: webpage
raw_files:
  - "stripe-payments-vouchers-2026-11-07.md"
  - "stripe-vouchers-2025.md"
tags: [stripe, vouchers, boleto, konbini, multibanco, oxxo, cash, in-person, brazil, japan, portugal, mexico]
---

## Summary

The May 7 and November 7, 2026 captures of [[stripe]]'s voucher hub describe Boleto, Konbini, Multibanco and OXXO. A customer selects a voucher method, receives a digital code with transaction details by email or in an app, and pays through a channel supported by the method. Cash payment at an authorized location is common. [[source-stripe-multibanco|Multibanco's method guide]] documents payment by bank transfer through online banking or at an ATM. See [[stripe-vouchers]] for method-specific channels, eligibility, confirmation, and refunds.

## Payment and Fulfillment

The customer can leave a voucher unpaid. Wait for confirmed payment before fulfilling an order. Both captures give one business day as a possible confirmation delay. Consult each method's documentation for its timing and refund support. Some businesses credit customers through a separate process when their voucher method lacks refund support. Vouchers can reach customers without cards or bank accounts and serve as a fallback where card authorization rates are low. For gift vouchers, the hub points to Checkout promotions and discounts.

## Product and API Support

| Method | API enum | SetupIntents | `setup_future_usage` | Subscriptions | Invoicing |
| --- | --- | --- | --- | --- | --- |
| Boleto | `boleto` | Yes | Yes | Yes | Yes |
| Konbini | `konbini` | No | No | `send_invoice` only | `send_invoice` only |
| Multibanco | `multibanco` | No | No | `send_invoice` only | `send_invoice` only |
| OXXO | `oxxo` | No | No | No | No |

- All four methods list Connect, Checkout, Payment Links, Payment Element and Mobile Payment Element. The hub excludes Express Checkout Element for all four. Boleto alone lists Customer Portal. Konbini and OXXO exclude Checkout subscription and setup modes. The November [[source-stripe-boleto|Boleto method guide]] lists setup support and excludes off-session payments.
- The hub's API matrix lists PaymentIntents for all four, excludes manual capture, and marks all four “No” in its “Requires redirect” column. Its generic footnote says some PaymentIntent confirmations may require a `return_url`. Voucher presentation depends on the integration. The May [[source-stripe-boleto-accept-payment|Boleto Checkout guide]] sends the customer to `hosted_voucher_url` after form submission, when Stripe has created the voucher and still requires customer action.
- Both hub captures scope the Konbini Connect invite to charges made `on_behalf_of` other accounts. The November [[source-stripe-konbini|Konbini method guide]] separately documents a Japanese platform settling destination charges or separate charges and transfers on its own account with its own Konbini activation and without `on_behalf_of`. The connected account does not need its own activation in that flow.
- Use method-specific eligibility and account requirements alongside the hub tables. The separate [payment-method support matrix](https://docs.stripe.com/payments/payment-methods/payment-method-support) gives business location and customer country independently.

For Sources or Tokens integrations, both captures point to [migration to PaymentIntents](https://docs.stripe.com/payments/payment-intents/migration.md).

## Raw Sources

- [[raw/stripe-payments-vouchers-2026-11-07|2026-11-07 vouchers overview]] — full capture with flow, product and API matrices, and migration reference.
- [[raw/stripe-vouchers-2025|2026-05-07 vouchers overview]] — full capture with the same lifecycle and matrix content and a locally captured SVG flow diagram.
