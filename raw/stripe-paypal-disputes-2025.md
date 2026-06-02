<!-- Source URL: https://docs.stripe.com/payments/paypal/disputed-payments -->
<!-- Fetched: 2026-05-07 -->

# Disputed PayPal payments

Learn how dispute management works for PayPal, a digital wallet popular with businesses in Europe.

The risk of fraud or unrecognized PayPal payments is low because the customer must authenticate the payment with their PayPal account.

## Overview

Customers must authenticate any payment with their PayPal account to decrease the risk of fraud. However, customers can dispute PayPal payments if for example:

- They don’t receive the goods they paid for
- The received goods don’t match their description

Your settlement choice when activating PayPal affects the funds flow for PayPal disputes. See [Choose settlement preference](https://docs.stripe.com/payments/paypal/choose-settlement-preference.md#refunds-and-disputes) for more context.

## Dispute process

Customers can file a dispute on PayPal up to 180 calendar days from the date of purchase. They can also file a dispute through the payment method they used to complete the PayPal purchase (such as their bank).

After the customer initiates a dispute, Stripe notifies you through:

- Email
- The [Stripe Dashboard](https://dashboard.stripe.com/disputes)
- An API `charge.dispute.created` event (if your integration is set up to receive [webhooks](https://docs.stripe.com/webhooks.md))
- Push notification (if you’ve subscribed)

Depending on the type of dispute and where it was filed, PayPal might offer the ability for you to communicate directly with the customer in an attempt to resolve the dispute before countering it. Currently, Stripe doesn’t offer this functionality and requests that you turn to PayPal to contact the customer.

If no agreement is reached, you can either accept or counter the dispute. If you choose to counter, Stripe requests that you [submit evidence](https://docs.stripe.com/disputes/responding.md#respond) that you fulfilled the purchase order in the [Stripe Dashboard](https://docs.stripe.com/disputes/responding.md#respond). This evidence helps PayPal determine if a dispute is valid or if they should reject it. The evidence you provide must contain as much detail as possible from what the customer provided at checkout. You must submit the requested information within 2 to 19 calendar days, depending on the category of the dispute. PayPal aims to make a decision within 30 calendar days of evidence submission.

If you prefer to handle disputes programmatically, you can [respond to disputes using the API](https://docs.stripe.com/disputes/api.md).

## Dispute resolution

If PayPal resolves the dispute with you winning, the disputed amount will be returned to your balance.

If PayPal rules in favor of the customer, the dispute is lost and the balance charge becomes permanent.

In some cases, PayPal allows a lost dispute to be appealed. Currently, Stripe doesn’t support appeals and requests that you turn to PayPal to file an appeal. In these cases, the dispute remains open on Stripe until a final resolution has been reached by PayPal. Refer to PayPal to be notified on when a dispute becomes appealable.

Read more about disputes on [how disputes work](https://docs.stripe.com/disputes/how-disputes-work.md) and [best practices for responding to disputes](https://docs.stripe.com/disputes/best-practices.md).

## Fees

PayPal might charge fees for disputes. The terms and amount of PayPal dispute fees are set by PayPal. Stripe doesn’t charge any additional fees for PayPal disputes.

## Multiple disputes per payment

A buyer can reopen a dispute on PayPal if there are subsequent issues with an order. For example, the buyer might create a dispute because they haven’t received their goods (`product_not_received`). After you counter and win the case, the buyer can change the category of the dispute on PayPal by claiming that the product they received isn’t what they ordered (`product_unacceptable`). This action causes the dispute to reopen on PayPal.

On Stripe, each claim in a specific category is represented by a separate dispute. In contrast, on PayPal, the original dispute is reopened under a different category. This means you might have multiple disputes for a single payment. In the example above, there are two disputes on Stripe: the first one for `product_not_received` and the second one for `product_unacceptable`. Both of these disputes link to the same dispute on PayPal.

In rare cases, you might see two disputes with the same category for the same payment on Stripe. This happens when the buyer first files a dispute on PayPal, loses it, then files the same dispute with their bank.

## Testing your integration

Stripe allows you to simulate a [disputed transaction](https://docs.stripe.com/disputes.md) by specifying `email` values that match the patterns described in [test scenarios](https://docs.stripe.com/payments/paypal/disputed-payments.md#scenarios) when you create a PaymentIntent (as part of the [billing details](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_data-billing_details)). You can choose from the different test scenarios to simulate disputes of all relevant categories.

For example, creating the PaymentIntent server-side and simulating a disputed transaction where the buyer claims they didn’t receive the product looks like:

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1099 \
  -d currency=eur \
  -d "payment_method_types[]=paypal" \
  -d "payment_method_data[type]=paypal" \
  --data-urlencode "payment_method_data[billing_details][email]=dispute_not_received@example.com"
```

If using [Checkout](https://docs.stripe.com/payments/checkout.md) or [Payment Links](https://docs.stripe.com/no-code/payment-links.md), you can enter the email in the checkout form. Shortly after the payment has been completed, it will be disputed as `product_not_received`.

### Test scenarios

The table below displays the scenarios available to test. Each scenario produces a dispute shortly after a payment has been completed.

`.*` represents any valid character in an email. For example, the pattern `.*dispute_duplicate@.*` is matched by an email such as `my_dispute_duplicate@mycompany.com`.

| Email pattern                         | Scenario                                                                                                                                                                                                                                                                                    |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.*dispute_credit_not_processed@.*`   | Tests a dispute for a payment where the customer claims they’re entitled to a full or partial refund because they returned the purchased product or didn’t fully use it, or the transaction was otherwise canceled or not fully fulfilled, but you haven’t yet provided a refund or credit. |
| `.*dispute_duplicate@.*`              | The customer claims they were charged multiple times for the same product or service.                                                                                                                                                                                                       |
| `.*dispute_fraudulent@.*`             | The customer claims that the transaction is fraudulent and they didn’t authorize the transaction.                                                                                                                                                                                           |
| `.*dispute_general@.*`                | Tests a dispute for a payment where an uncategorized dispute has been opened.                                                                                                                                                                                                               |
| `.*dispute_not_received@.*`           | The customer claims that they have not received the product or service they purchased.                                                                                                                                                                                                      |
| `.*dispute_product_unacceptable@.*`   | The customer claims that the product or service they purchased was unacceptable or otherwise not as described.                                                                                                                                                                              |
| `.*dispute_subscription_cancelled@.*` | The customer claims that they were charged for a subscription after it was canceled.                                                                                                                                                                                                        |

### Evidence

To simulate winning or losing the dispute, respond with one of the evidence values from the table below.

- If you [respond using the API](https://docs.stripe.com/disputes/api.md), pass the value from the table as [uncategorized_text](https://docs.stripe.com/api/disputes/update.md#update_dispute-evidence-uncategorized_text).
- If you [respond in the Dashboard](https://docs.stripe.com/disputes/responding.md), enter the value from the table in the **Additional information** field. Then, click **Submit evidence**.

| Evidence           | Description                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------- |
| `winning_evidence` | The dispute is closed and marked as won. Your account is credited the amount of the charge. |
| `losing_evidence`  | The dispute is closed and marked as lost. Your account isn’t credited.                      |
