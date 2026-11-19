---
title: "Stripe: Buy Now, Pay Later Overview"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/buy-now-pay-later"
raw_files:
  - "stripe-payments-buy-now-pay-later-2026-11-07.md"
  - "stripe-bnpl-overview-2025.md"
tags: [stripe, bnpl, buy-now-pay-later, klarna, affirm, afterpay, installments, payments]
---

## Overview

Stripe's 7 November 2026 overview describes buy now, pay later (BNPL) methods that let a buyer repay a provider in installments while the merchant is described as paid immediately and in full. The buyer chooses a BNPL service, creates or logs into its account, accepts or declines the repayment terms, then returns to the merchant site. This is a documented checkout flow, not evidence of an individual buyer's approval, a successful payment, or a merchant payout. Subscription-schedule installment plans are a separate option mentioned by the page.

## Key takeaways

- Dynamic payment methods are enabled by default and configured in Dashboard. Stripe displays relevant *eligible* methods for the buyer through standard Checkout, including Stripe-hosted or embedded pages, Elements checkout, and a hosted invoice page. A custom payments form can list methods manually using the method-specific guides. Display does not establish account access or buyer approval.
- The **product support** matrix has eleven named BNPL methods: Affirm, Afterpay/Clearpay, Alma, Billie, Klarna, Kriya, Mondu, Scalapay, SeQura, Sunbit, and Zip. Its Connect column says Supported for all eleven. The separate May 2026 Kriya, Mondu, SeQura, and Scalapay method captures say Connect **No**. The captures do not reconcile this scope conflict; do not treat the overview cell as universal Connect eligibility.
- The **API support** matrix has only ten rows; Scalapay is absent. All *listed* methods show PaymentIntents support and a redirect requirement. Only Klarna shows SetupIntents support. Manual capture is unsupported for Sunbit and Zip; the other listed rows show support. This matrix alone establishes no Scalapay PaymentIntent, setup, manual capture, or redirect behavior.
- The November API matrix marks `setup_future_usage` supported for Billie, Klarna, Kriya, Mondu, and Sunbit. It marks SeQura unsupported, whereas the May matrix marked SeQura supported. Sunbit was supported in both snapshots but was omitted from this source's former summary. The table footnote says non-card/bank-debit methods either do not support this parameter or support only `off_session`; the matrix does not promise every session mode.
- The November product matrix changes Affirm Subscriptions from May's supported-with-`send_invoice` to Unsupported, and Customer Portal from Unsupported to Supported. Affirm Invoicing remains `send_invoice` only; Terminal remains Supported. The prior May Subscriptions cell is dated history, not a November entitlement.
- Klarna Checkout now has a buyer-country/payment-option qualification instead of the former generic Checkout subscription/setup footnotes. Klarna Subscriptions remains Supported, while Terminal is **Private preview** rather than May's Unsupported. Its prior Subscriptions `send_invoice` marker disappears; that omission does not prove automatic collection or any recurring option for every country/buyer. Express Checkout Element support excludes saving during payment via `setup_future_usage`.
- Mondu, Scalapay, and SeQura gain Mobile Payment Element support in the November product table. SeQura Invoicing becomes Supported only for `send_invoice`. Afterpay/Clearpay Invoicing remains Private preview. Matrix labels describe the captured documentation, not a merchant account's activation.

## Detail locators

- November product rows and footnotes: new raw lines 39-55. May product rows and footnotes: old raw lines 38-54. Checkout footnotes 1 and 2 still exclude subscription and setup modes for methods carrying them; Klarna uses November footnote 5 instead.
- November API rows and footnotes: new raw lines 57-72. May API rows and footnotes: old raw lines 56-71. The redirect column covers its ten rows; confirmation may require `return_url`.
- The transaction table separately lists Affirm (Canada/US; 50 USD minimum and up to 30,000 USD or local equivalent), Afterpay/Clearpay (five countries; 1–4,000 USD or local equivalent), Klarna (country and option dependent, 10 USD minimum or local equivalent and variable maximum), Meses sin intereses (Mexico, 3–24 billing cycles, 100 MXN per month minimum), and Zip (AU/US with product-specific limits). Affirm's credit limit is 20,000 USD/CAD; a transaction up to 30,000 USD/CAD requires a buyer down payment. These are table terms, not an offer to a particular buyer. New raw lines 74-91; old raw lines 73-91.
- The Payment Method Messaging Element can present BNPL messaging on product and cart pages. It does not prove the buyer can select or complete a method. New raw lines 93-95; old raw lines 93-95.

## Related

- [[stripe]] — company
- [[stripe-bnpl]] — BNPL concept and method-specific routes

## Raw Sources

- [[raw/stripe-payments-buy-now-pay-later-2026-11-07|Stripe BNPL overview, captured 2026-11-07]] — full current captured page
- [[raw/stripe-bnpl-overview-2025|Stripe BNPL overview, captured 2026-05-06]] — prior matched capture
- [[raw/stripe-kriya-2025|Kriya method capture, 2026-05-06]]; [[raw/stripe-mondu-2025|Mondu method capture, 2026-05-06]]; [[raw/stripe-sequra-2025|SeQura method capture, 2026-05-06]]; [[raw/stripe-scalapay-2025|Scalapay method capture, 2026-05-06]] — method-specific Connect-No conflict at lines 36-38
