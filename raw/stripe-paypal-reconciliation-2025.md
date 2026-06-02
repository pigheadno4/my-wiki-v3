<!-- Source URL: https://docs.stripe.com/payments/paypal/payout-reconciliation -->
<!-- Fetched: 2026-05-07 -->

# PayPal payout reconciliation

Learn how to reconcile payments made through PayPal, a common payment method in Europe.

Reconciliation is the process of matching and verifying payments that have been received and processed with the corresponding PayPal orders. It only applies to customers receiving their funds on PayPal, and not on Stripe. Stripe automatically [reconciles](https://docs.stripe.com/reports/payout-reconciliation.md) PayPal transactions before the payout, whereas this can’t be done if transactions *settle* (When funds are available in your Stripe balance) outside of Stripe’s platform. When transactions settle outside of Stripe’s platform, you’ll use PayPal reporting available on your PayPal account or with sFTP for reconciliation.

Stripe provides two ways of supporting PayPal transaction reconciliation:

- (Recommended) Using the [reference](https://docs.stripe.com/payments/paypal/payout-reconciliation.md#use-reference) field. This is the preferred option if you have a businesses-generated order or invoice ID, which you can put in the reference field. After the payment is made and processed, `my_order_id` appears as `Invoice ID` in the PayPal settlement report.
- Using the [transaction_id](https://docs.stripe.com/payments/paypal/payout-reconciliation.md#use-transaction-id) from the [Charge](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-paypal-transaction_id) object. When the payment is processed, `paypal_capture_id` appears as `Transaction ID` in the PayPal settlement report. This is recommended only if you don’t have a business-generated order ID.

## Use Reference

Use the [reference](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-paypal-reference) field to populate your own reference for an order on a PayPal payment. One example of this is an Order ID from PayPal. This reference is visible to the buyer and also in the [settlement report](https://developer.paypal.com/docs/reports/sftp-reports/settlement-report/) on your PayPal account. To reconcile funds using a `reference`, you can include it as part of the [payment_method_options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-paypal) parameter when creating a PaymentIntent. You can use this `reference` to match payments made through Stripe with corresponding transactions in the [PayPal settlement report](https://developer.paypal.com/docs/reports/sftp-reports/settlement-report/). Any subsequent transactions derived from the original Payment transaction, such as refunds and disputes, are associated with the given `reference`.

The following code sample shows the creation of a PaymentIntent with the `reference` set in `payment_method_options`:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["paypal"],
  payment_method_options: {
    paypal: {
      reference: "my_order_id",
    },
  },
});
```

After the payment is made and processed, `my_order_id` is reflected as Invoice ID in the [PayPal settlement report](https://developer.paypal.com/docs/reports/sftp-reports/settlement-report/).

## Use the Charge object’s transaction ID

The [transaction_id](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-paypal-transaction_id) field contains the ID used by PayPal to identify a transaction. To reconcile funds using a `transaction_id`, retrieve the `transaction_id` from the [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-paypal) field in the Charge object. The `transaction_id` is present only if the payment has been captured. It’s used to match payments made through Stripe with corresponding transactions in the [PayPal settlement report](https://developer.paypal.com/docs/reports/sftp-reports/settlement-report/).

For example, here’s how you can retrieve the `transaction_id` from the Charge object:

#### Json

```json
{
  "amount": 1099,
  "amount_captured": 1099,
  "payment_method_details": {
    "paypal": {
      "transaction_id": "paypal_capture_id",
      "payer_id": "ZA889USQQDD37",
      "payer_email": "jenny@example.com",
      "payer_name": "Jenny Rosen"
    },
    "type": "paypal"
  },
  "balance_transaction": "txn_3MrOPxGsnWT9WMaQ19vg30v3",
  "billing_details": {
    "address": {
      "city": "Co. Kerry",
      "country": "IE",
      "line1": "Skellig Michael",
      "line2": "Great Skellig",
      "postal_code": "12345",
      "state": "Munster"
    },
    "email": "jenny@example.com",
    "name": null,
    "phone": null
  },
  "calculated_statement_descriptor": null,
  "captured": true,
  "created": 1680194094,
  "currency": "eur",
  "fraud_details": {},
  "id": "py_3MrOPxGsnWT9WMaQ1gwt6RSD",
  "invoice": null,
  "livemode": true,
  "metadata": {},
  "object": "charge",
  "on_behalf_of": null,
  "order": null,
  "outcome": {
    "network_status": "approved_by_network",
    "reason": null,
    "risk_level": "not_assessed",
    "seller_message": "Payment complete.",
    "type": "authorized"
  },
  "paid": true,
  "payment_intent": "pi_3MrOPxGsnWT9WMaQ1IrNlTiZ",
  "payment_method": "pm_1MrOPxGsnWT9WMaQ3XBSs7eY",
  "receipt_email": null,
  "receipt_number": null,
  "refunded": false
}
```

When the payment is processed, `paypal_capture_id` is appears as `Transaction ID` in the [PayPal settlement report](https://developer.paypal.com/docs/reports/sftp-reports/settlement-report/).

## Access your PayPal reports

You can download your PayPal Settlement Report and other reports from paypal.com, or you can enable sFTP reporting by contacting PayPal.

The Settlement Report provides an end-to-end view of all balance-impacting transactions within a 24-hour period. This report is used to reconcile money moving events in a PayPal account with monies that are moved to a linked bank account.

To access the Settlement report:

1. [Log in](https://www.paypal.com/signin) to your PayPal business account.
1. Under **Activity**, select **All Reports**.
1. Select **Transactions > Settlement**.

Read more about [PayPal reports and how to download them](https://www.paypal.com/us/cshelp/article/how-do-i-view-and-download-statements-and-reports-help145).
