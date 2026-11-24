---
title: "Stripe: Disputed PayPal Payments"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/payments/paypal/disputed-payments
raw_files:
  - "stripe-payments-paypal-disputed-payments-2026-11-07.md"
  - "stripe-paypal-disputes-2025.md"
tags: [stripe, wallets, paypal, disputes, chargebacks, evidence, testing]
---

## Summary

The May 7 and November 7, 2026 [[stripe]] guides describe PayPal dispute management, settlement, and test scenarios. Authenticating with a PayPal account reduces fraud and unrecognized-payment risk. Customers can still dispute a purchase, including when goods do not arrive or do not match their description.

## Dispute process

- **Filing window** — customers have up to 180 calendar days from purchase to file on PayPal. They can also file through the original funding provider, such as their bank. The guides give no deadline for that separate route.
- **Notifications** — Stripe provides email and Dashboard notifications, `charge.dispute.created` if the integration is configured to receive webhooks, and push notifications if subscribed.
- **Contact and response** — depending on the dispute type and where it was filed, PayPal may let the merchant contact the customer directly. Use PayPal for that contact. If the parties do not reach agreement, the merchant can accept or counter through the Dashboard or API. To counter, submit detailed fulfillment and checkout evidence within 2–19 calendar days, depending on the category.
- **Outcome** — PayPal aims to decide within 30 calendar days of evidence submission. A merchant win returns the disputed amount, and a loss makes the balance charge permanent. The merchant's settlement preference determines whether dispute funding uses the Stripe or PayPal balance. See [[source-stripe-paypal-settlement]].
- **Appeals and fees** — PayPal permits some lost disputes to be appealed directly with PayPal. Stripe keeps those cases open until PayPal's final resolution. PayPal sets and may charge a dispute fee. Stripe adds no PayPal dispute fee.

A customer can reopen a PayPal dispute under a new category, such as changing `product_not_received` to `product_unacceptable`. Stripe creates separate dispute records for each category and links them to the same PayPal case. Two same-category Stripe records can also occur if the customer first loses at PayPal and then files through their bank.

## Test scenarios

The guides show how to simulate disputes by supplying a matching billing email when creating a test PaymentIntent. For the `product_not_received` example, both use `amount=1099`, `currency=eur`, `payment_method_data[type]=paypal`, and `payment_method_data[billing_details][email]=dispute_not_received@example.com`. The request amount is 1,099 euro cents (€10.99). The May 7, 2026 example sends `payment_method_types[]=paypal`. The November 7, 2026 example instead sends `automatic_payment_methods[enabled]=true`.

Both samples omit an API version header. The separate November-captured [Endive changelog](../../raw/stripe-changelog-endive-2026-09-30-removes-the-payment-method-types-parameter-from-payment-intents-and-setup-intents-2026-11-07.md#L7-L28) describes removing writable `payment_method_types` on the linked `2026-09-30.endive` PaymentIntent Create endpoint, while its Impact section names `2026-08-26.preview`. The test request comparison establishes the sample change and leaves the first affected version and account eligibility unresolved.

For Checkout or Payment Links, enter the matching test email in the form. The simulated dispute is created shortly after the test payment completes.

| Email pattern | Dispute category |
| --- | --- |
| `.*dispute_credit_not_processed@.*` | Credit not processed |
| `.*dispute_duplicate@.*` | Duplicate charge |
| `.*dispute_fraudulent@.*` | Fraudulent transaction |
| `.*dispute_general@.*` | Uncategorized |
| `.*dispute_not_received@.*` | Product not received |
| `.*dispute_product_unacceptable@.*` | Product unacceptable |
| `.*dispute_subscription_cancelled@.*` | Subscription cancelled |

For a simulated resolution, use `winning_evidence` to close as won and credit the charge amount, or `losing_evidence` to close as lost without a credit. With the Disputes update API, pass the value in the evidence field `uncategorized_text`. In the Dashboard, enter the value in **Additional information** and click **Submit evidence**.

## Related Pages

- [[stripe-wallets]] — PayPal as a Stripe wallet
- [[source-stripe-paypal-settlement]] — settlement and the balance used for refunds and disputes

## Raw Sources

- [[raw/stripe-payments-paypal-disputed-payments-2026-11-07|November 7, 2026 Disputed PayPal Payments guide]]
- [[raw/stripe-paypal-disputes-2025|May 7, 2026 Disputed PayPal Payments guide]] — verbatim dispute management guide (102 lines)
