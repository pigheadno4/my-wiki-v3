<!-- Source URL: https://docs.stripe.com/payments/customer-balance/reconciliation -->
<!-- Fetched: 2026-05-05 -->

# Reconciliation

Learn about how Stripe reconciles the customer balance to payments and invoices.

Stripe offers the `automatic` or `manual` reconciliation behavior for funds in the cash balance.

By default, Stripe applies the automatic reconciliation mode to the cash balance of all of your customers. You can use the Bank Transfers [reconciliation settings](https://dashboard.stripe.com/settings/bank_transfers) to change the reconciliation behavior for everyone.
![Bank Transfer reconciliation settings](assets/stripe-reconciliation-settings.png)

Bank Transfer reconciliation settings

## Override reconciliation behavior

You can use the Dashboard or API to override the Bank Transfers reconciliation settings for a specific customer.

To override a customer’s reconciliation behavior in the Dashboard:

1. Select the customer, then find **Cash Balance** in the **Payment methods** section.
1. Expand the overflow menu (⋯) next to the cash balance details.
1. From the expanded options, select **Change reconciliation mode**. This displays a modal that allows you to change the reconciliation behavior for the customer.
   ![Cash Balance section on the Customer page](assets/stripe-cash-balance-settings.png)

The Cash Balance section on the Customer page

To override a customer’s reconciliation behavior using the API, set the customer’s [reconciliation mode](https://docs.stripe.com/api/customers/object.md#customer_object-balance_settings-reconciliation_mode) to `manual`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.update("{{CUSTOMER_ID}}", {
  cash_balance: {
    settings: {
      reconciliation_mode: "manual",
    },
  },
});
```

To point the reconciliation mode for an overridden customer back to the user’s default, you can do so in the Dashboard. You can also use the API to set the [reconciliation mode](https://docs.stripe.com/api/customers/object.md#customer_object-balance_settings-reconciliation_mode) on the customer to `merchant_default`.

To manage the cash balance settings, including reconciliation mode, for a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer), use the Customers API endpoint with the Account ID as the path parameter, for example `v1/customers/acct_xxxxx`.

## Automatic cash balance reconciliation

#### US

By default, Stripe automatically applies any available cash balance to PaymentIntents and *invoices* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) that are awaiting funding. A PaymentIntent is awaiting funding if it’s incomplete. An invoice is awaiting funding if it’s `open` and either hasn’t passed its due date or became overdue within the last 30 days.

Stripe applies funds in the following order:

1. Stripe initially attempts to match a bank transfer reference with a single invoice that has a matching [invoice number](https://docs.stripe.com/api/invoices/object.md#invoice_object-number).
1. If the first attempt is unsuccessful, Stripe attempts to match the bank transfer reference with a single incomplete PaymentIntent that has a matching reference stored in the PaymentIntent’s [display_bank_transfer_instructions](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-reference) field.
1. If Stripe doesn’t receive a bank transfer reference or can’t match the reference with a single invoice or PaymentIntent, we search for a group of between one and five invoices and PaymentIntents awaiting the exact amount the user sent. For multiple valid combinations, Stripe prioritizes as follows:
   - We filter for the smallest group. If there’s two groups of invoices or PaymentIntents that can both receive the funds, we select the one with fewer objects.
   - If there are multiple smallest-sized groups, we select the smallest group that contains the most invoices.
   - If multiple groups contain the same number of invoices, we select the group with the oldest PaymentIntents.
1. If we can’t find a group that equals the exact funds available, we fund as many invoices that can be fully funded, starting with the oldest finalized ones first.
1. If any funds remain, we apply the remaining funds to incomplete PaymentIntents, starting with the oldest ones first.

#### UK

By default, Stripe automatically applies any available cash balance to PaymentIntents and *invoices* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) that are awaiting funding. A PaymentIntent is awaiting funding if it’s incomplete. An invoice is awaiting funding if it’s `open` and either hasn’t passed its due date or became overdue within the last 30 days.

Stripe applies funds in the following order:

1. Stripe initially attempts to match a bank transfer reference with a single invoice that has a matching [invoice number](https://docs.stripe.com/api/invoices/object.md#invoice_object-number).
1. If the first attempt is unsuccessful, Stripe attempts to match the bank transfer reference with a single incomplete PaymentIntent that has a matching reference stored in the PaymentIntent’s [display_bank_transfer_instructions](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-reference) field.
1. If Stripe doesn’t receive a bank transfer reference or can’t match the reference with a single invoice or PaymentIntent, we search for a group of between one and five invoices and PaymentIntents awaiting the exact amount the user sent. For multiple valid combinations, Stripe prioritizes as follows:
   - We filter for the smallest group. If there’s two groups of invoices or PaymentIntents that can both receive the funds, we select the one with fewer objects.
   - If there are multiple smallest-sized groups, we select the smallest group that contains the most invoices.
   - If multiple groups contain the same number of invoices, we select the group with the oldest PaymentIntents.
1. If we can’t find a group that equals the exact funds available, we fund as many invoices that can be fully funded, starting with the oldest finalized ones first.
1. If any funds remain, we apply the remaining funds to incomplete PaymentIntents, starting with the oldest ones first.

#### EU

By default, Stripe automatically applies any available cash balance to PaymentIntents and *invoices* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) that are awaiting funding. A PaymentIntent is awaiting funding if it’s incomplete. An invoice is awaiting funding if it’s `open` and has either not exceeded its due date or has become past due within the last thirty days.

Stripe applies funds in the following order:

1. Stripe initially attempts to match a bank transfer reference with a single invoice that has a matching [invoice number](https://docs.stripe.com/api/invoices/object.md#invoice_object-number).
1. If the first attempt is unsuccessful, Stripe attempts to match the bank transfer reference with a single incomplete PaymentIntent that has a matching reference stored in the PaymentIntent’s [display_bank_transfer_instructions](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-reference) field.
1. If Stripe doesn’t receive a bank transfer reference or can’t match the reference with a single invoice or PaymentIntent, we search for a group of between one and five invoices and PaymentIntents awaiting the exact amount the user sent. For multiple valid combinations, Stripe prioritizes as follows:
   - We filter for the smallest group. If there’s two groups of invoices or PaymentIntents that can both receive the funds, we select the one with fewer objects.
   - If there are multiple smallest-sized groups, we select the smallest group that contains the most invoices.
   - If multiple groups contain the same number of invoices, we select the group with the oldest PaymentIntents.
1. If we can’t find a group that equals the exact funds available, we fund as many invoices that can be fully funded, starting with the oldest finalized ones first.
1. If any funds remain, we apply the remaining funds to incomplete PaymentIntents, starting with the oldest ones first.

#### JP

By default, Stripe automatically applies any available cash balance to PaymentIntents and *invoices* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) that are awaiting funding. A PaymentIntent is awaiting funding if it’s incomplete. An invoice is awaiting funding if it’s `open` and has either not exceeded its due date or has become past due within the last thirty days.

Stripe applies funds in the following order:

1. We try to find a group of between one and five invoices and PaymentIntents that are waiting for the exact amount sent by the user. If there are multiple valid combinations, we prioritize as follows:
   - We filter for the smallest group. If there’s two groups of invoices or PaymentIntents that can both receive the funds, we select the one with fewer objects.
   - If there are multiple smallest-sized groups, we select the smallest group that contains the most invoices.
   - If multiple groups contain the same number of invoices, we select the group with the oldest PaymentIntents.
1. If we’re unsuccessful in finding a group that sums to the exact funding available, we fund as many invoices that can be fully funded in order of finalization time, oldest first.
1. If any funding remains, Stripe applies funds to incomplete PaymentIntents in order of confirmation time, oldest first.

#### MX

By default, Stripe automatically applies any available cash balance to PaymentIntents and *invoices* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) that are awaiting funding. A PaymentIntent is awaiting funding if it’s incomplete. An invoice is awaiting funding if it’s `open` and either hasn’t passed its due date or became overdue within the last 30 days.

Stripe applies funds in the following order:

1. Stripe initially attempts to match a bank transfer reference with a single invoice that has a matching [invoice number](https://docs.stripe.com/api/invoices/object.md#invoice_object-number).
1. If the first attempt is unsuccessful, Stripe attempts to match the bank transfer reference with a single incomplete PaymentIntent that has a matching reference stored in the PaymentIntent’s [display_bank_transfer_instructions](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-reference) field.
1. If Stripe doesn’t receive a bank transfer reference or can’t match the reference with a single invoice or PaymentIntent, we search for a group of between one and five invoices and PaymentIntents awaiting the exact amount the user sent. For multiple valid combinations, Stripe prioritizes as follows:
   - We filter for the smallest group. If there’s two groups of invoices or PaymentIntents that can both receive the funds, we select the one with fewer objects.
   - If there are multiple smallest-sized groups, we select the smallest group that contains the most invoices.
   - If multiple groups contain the same number of invoices, we select the group with the oldest PaymentIntents.
1. If we can’t find a group that equals the exact funds available, we fund as many invoices that can be fully funded, starting with the oldest finalized ones first.
1. If any funds remain, we apply the remaining funds to incomplete PaymentIntents, starting with the oldest ones first.

## Manual cash balance reconciliation

When manual reconciliation is enabled on a customer, Stripe doesn’t automatically apply any funds from the customer balance.

You can apply funds from the customer balance manually using either the API or the Dashboard.

For both the API and the Dashboard, you can apply funds to an incomplete or partially funded PaymentIntent, or an open Invoice. You can also fund Invoices that are still open but marked overdue with this method.

In the Dashboard, you can apply funds to a PaymentIntent on the Payments page or on the page for the individual payment.

To fund a PaymentIntent from the Payments page, find the payment you want to fund, select the overflow menu (⋯), then click **Fund from cash balance**.
![The overflow menu for a single Payment on the Stripe Dashboard Payments page](assets/stripe-fund-from-cash-balance-payments-list.png)

To fund a PaymentIntent from the page for the individual payment, click the **Fund from cash balance** button.

In both cases, selecting the **Fund from cash balance** button prompts you to confirm the payment. This button doesn’t appear on either page if the customer doesn’t have any funds available on their cash balance.

To apply funds to an invoice, go to the **Invoice** page, click the **Charge customer** button, and then select **Cash Balance** as the payment method.

You can partially or fully fund an invoice using the Dashboard. This option allows you to pay a portion of the invoice, if the customer doesn’t have sufficient funds on their cash balance to fully pay the invoice.

To apply funds using the API:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.applyCustomerBalance(
  "{{PAYMENTINTENT_ID}}",
  {
    amount: 1500,
    currency: "usd",
  },
);
```

The amount is optional. When omitted, the amount defaults to the remaining amount requested on the PaymentIntent.

The following code is an example of a full pass of manual reconciliation. You receive the `cash_balance.funds_available` webhook, find PaymentIntents that are awaiting funding, and use the funds available to reconcile the open PaymentIntents.

The object sent in the `cash_balance.funds_available` message always contains a representation of the customer’s full cash balance, regardless of the event triggering the webhook. This means that the cash balance might contain funds that were previously added to the customer’s cash balance, not just those added immediately before the triggering event.

#### Node.js

```node
// This example uses Express to receive webhooks
const express = require("express");
const app = express();
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const isPiEligible = (paymentIntent, currencies) => {
  // PaymentIntents are only fundable if they're both not yet fully-funded and have
  // customer_balance as an allowed payment type.

  const awaitingFurtherFunding = [
    "requires_payment_method",
    "requires_action",
  ].includes(paymentIntent.status);
  const paymentMethodEligible =
    paymentIntent["payment_method_types"].includes("customer_balance");
  const currencyEligible = currencies.includes(paymentIntent.currency);

  return awaitingFurtherFunding && paymentMethodEligible && currencyEligible;
};

// You can use webhooks to receive information about asynchronous payment events. For more about our
// webhook events check out https://stripe.com/docs/webhooks.
//
// To follow our webhook best practices, you should aim to return a response as soon as possible after
// parsing the event received.
app.post(
  "/webhook",
  express.raw({ type: "application/json" }),
  async (request, response) => {
    const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;

    let event;
    let signature = request.headers["stripe-signature"];

    try {
      event = stripe.webhooks.constructEvent(
        request.body,
        signature,
        webhookSecret,
      );
    } catch (err) {
      console.log(`⚠️  Webhook signature verification failed.`);
      return response.sendStatus(400);
    }

    data = event.data;
    eventType = event.type;

    // Get the type of webhook event sent. If it isn't cash_balance.funds_available, we don't want
    // to process it.
    if (eventType === "cash_balance.funds_available") {
      // The cash_balance.funds_available webhook always contains a complete Cash Balance,
      // regardless of the event triggering the webhook.
      //
      // This means that the Cash Balance may contain funds that were previously added to
      // the customer's Cash Balance, not just those added immediately before the triggering event.
      let cashBalance = data.object;
      const customerId = cashBalance.customer;

      // Cash balances may contain multiple currencies.
      const currenciesAvailable = Object.keys(cashBalance.available);

      await stripe.paymentIntents
        .list({
          customer: customerId,
        })
        .then(async (paymentIntents) => {
          const fundablePaymentIntents = paymentIntents.data.filter(
            (paymentIntent) => isPiEligible(paymentIntent, currenciesAvailable),
          );

          // We can order the funding of PaymentIntents in whichever order we like - here we'd
          // like to pay the oldest first.
          fundablePaymentIntents.sort((a, b) => a.created - b.created);

          const intentsForCurrency = currenciesAvailable.reduce(
            (result, currency) => {
              result[currency] = fundablePaymentIntents.filter(
                (pi) => pi.currency == currency,
              );
              return result;
            },
            {},
          );

          for (let i = 0; i < currenciesAvailable.length; i++) {
            // If a customer has balances in multiple currencies, we only allow reconciliation using
            // the balance that matches the currency of the PaymentIntent.
            const currency = currenciesAvailable[i];
            const paymentIntents = intentsForCurrency[currency];

            for (let j = 0; j < paymentIntents.length; j++) {
              const paymentIntent = paymentIntents[j];

              if (cashBalance.available[currency] == 0) {
                break;
              }

              await stripe.paymentIntents.applyCustomerBalance(
                paymentIntent.id,
              );
              await stripe.customers
                .retrieveCashBalance(customerId)
                .then((result) => {
                  cashBalance = result;
                });
            }
          }
        });
    } else {
      console.log(`Unhandled event type ${event.type}`);
    }

    response.json({ received: true });
  },
);

app.listen(3000, () => console.log("Running on port 3000"));
```

To retrieve the cash balance for a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer), pass the `Account` ID instead of the `Customer` ID.

## Unreconciled cash balance funds

Sometimes funds in the customer balance remain unreconciled—for example, when a customer sends too much money and you haven’t created any more PaymentIntents or Invoices for that customer.

To reconcile outstanding funds in the customer cash balance, you can either create a new PaymentIntent or invoice to accept a payment, or return the funds to the customer.

> You’re responsible for making sure that you reconcile customer cash balances promptly and accurately. Reconcile outstanding customer balances quickly, rather than leaving them in your account for an extended period.

Stripe periodically sends a reminder email when you have unreconciled balances in your account to make sure that you can review these unreconciled funds. If a customer balance remains unreconciled for 75 days, Stripe automatically attempts to return the funds to the customer’s bank account. When Stripe doesn’t have the customer’s account information, Stripe might reach out to the customer directly to initiate a refund of unreconciled funds. If Stripe is unable to determine the customer’s account information by the 90 day mark, we sweep the unreconciled funds to your Stripe account balance. Coordinate directly with the customer to make sure they receive the returned funds.

You can see the full list of customers who have unreconciled cash balances and the date that we’ll return them to the customer in your [Dashboard](https://dashboard.stripe.com/test/customers?tab=remaining_balance).
![Remaining customer balances filter](assets/stripe-remaining-customer-balances-filter.png)

Remaining customer balances filter

## Credit balance

*Credit balance* is handled differently from cash balance. Customer credit balance is an *Invoices* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice)-only feature which represents liability between you and the customer. When an invoice is finalized, the customer’s credit balance is applied to the invoice, decreasing the amount due.

For more information on credit balances, see [Customer Credit Balance](https://docs.stripe.com/invoicing/customer/balance.md).
