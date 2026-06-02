<!-- Source URL: https://docs.stripe.com/payments/paypal/choose-settlement-preference -->
<!-- Fetched: 2026-05-07 -->

# Choose settlement preference

Learn about settlement modes for PayPal payments.

Settlement choice determines how you access and manage funds, use the Dashboard, perform reconciliation, and so on.

## Getting started

If you’re a Connect user, your funds always settle on Stripe, similar to other payment methods. If you operate as a direct business, when you [connect your PayPal and Stripe accounts](https://docs.stripe.com/payments/paypal/activate.md) you can set the funds settlement preference for your PayPal payments. Read this guide to learn more about differences between PayPal and Stripe settlement options.

If you already use PayPal through Stripe, you can check your current settlement preference on the [Payment Methods Settings](https://dashboard.stripe.com/settings/payment_methods) page in the Stripe Dashboard.

## Money flow and payouts

If you settle funds from the PayPal payments on Stripe, you can access the money from your Stripe balance according to your [payouts](https://docs.stripe.com/payouts.md) schedule, similar to other payment methods at Stripe. The funds from the payments you receive are immediately transferred from PayPal to your Stripe balance, without the need for you to take any action.

If you settle PayPal payments to PayPal, you’ll need to manage payouts on PayPal.

## Refunds and disputes

Settlement on Stripe uses the funds available in your Stripe account if you want to refund a payment or need to cover the funds from a dispute, similarly to other payment methods on Stripe. If PayPal charges a fee when a dispute closes, it’s withdrawn from your Stripe balance through a [Balance Transaction](https://docs.stripe.com/reports/balance-transaction-types.md) of type `adjustment`.

For settlement on PayPal, you can still manage refunds and disputes from your Stripe Dashboard, but the relevant funds are the funds on your PayPal account. If you settle on PayPal, Stripe doesn’t transfer any funds from your PayPal account to your Stripe account or vice-versa. Make sure there is always a positive balance in both accounts to cover expected refund amounts or disputes, and fees that PayPal might charge when the dispute closes.

## Dashboard

If you settle your funds from PayPal payments on Stripe, the Stripe Dashboard functionality is the same as with other payment methods on Stripe.

If you settle your PayPal funds on a PayPal account, the [balance transaction](https://docs.stripe.com/api.md#balance_transaction_object) linked to the corresponding payment has a zero amount regardless of the payment, because funds settle in your PayPal balance, and no money goes to your Stripe balance.

Additionally, the Gross and Net volume charts won’t reflect your sales volume from PayPal if you settle your funds on a PayPal account. In this case, we recommend using the Payment methods report to track the volume from PayPal sales.

The payment details view is also different if you settle your PayPal funds to your PayPal account. The **Net** value reflects the change on the net volume of your Stripe balance. This is a negative value of the fee amount that Stripe takes for the payment.

## Reconciliation impact

Reconciliation is the process of matching and verifying payments that have been received and processed with the corresponding PayPal orders.

When settling your funds on Stripe, you get automatic transactions reconciliation.

If you settle on PayPal, you need to manually reconcile the transactions. Learn about how Stripe provides support for PayPal [transaction reconciliation](https://docs.stripe.com/payments/paypal/payout-reconciliation.md).

## Changing your settlement preference

If for any reason you need to change your current settlement mode, you can initiate the process from the Stripe Dashboard.

1. Go to the [Payment Methods Settings page](https://dashboard.stripe.com/settings/payment_methods).
1. Find PayPal settings.
1. Click **Contact Support to change**. You’ll be redirected to the FAQ page where you can file a support ticket.
1. File a support ticket to request a change.

The change shows up in the PayPal settings accordingly.

## Currency conversions

A currency conversion occurs when the *presentment currency* (The presentment currency is the currency the customer uses to make a payment) differs from the *settlement currency* (The settlement currency is the currency your bank account uses). See [currency conversions](https://docs.stripe.com/connect/currencies/fx-quotes-api.md#currency-conversions) for more information. Prevent currency conversions by adding a [settlement currency](https://docs.stripe.com/payouts/multicurrency-settlement.md#enable-multi-currency-settlement) for every currency you present to your customers.
