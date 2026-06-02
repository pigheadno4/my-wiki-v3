<!-- Source URL: https://docs.stripe.com/radar/risk-evaluation -->
<!-- Fetched: 2026-05-10 -->

# Risk evaluations

Review the outcomes of Stripe Radar risk evaluations.

While Stripe Radar offers a greater ability to monitor your payments and protect your business from disputes, you’re [ultimately responsible](https://stripe.com/us/legal#processing-transactions-disputes) for payments you choose to accept, including those that are later disputed or found to be fraudulent.

Stripe Radar includes an adaptive [AI model](https://stripe.com/radar/guide) that uses a risk score to evaluate the risk level for each payment in real time. The model uses hundreds of risk factors about each payment and data across our network of businesses to predict whether a payment is likely to be fraudulent. It learns from new customer purchase patterns and transaction features, and incorporates feedback from you whenever payments are marked as fraudulent.

Risk settings and the risk controls for fraudulent disputes and early fraud warnings don’t use this AI model. They use more specialized models that can balance the tradeoffs between authorization and fraud.

> When a business using Stripe sees a card, a SEPA Direct Debit account, or an ACH account, Stripe has likely processed payments for that payment method in the past:
>
> - 92% chance we’ve seen the card

- 82% chance we’ve seen the SEPA account
- 71% chance we’ve seen the ACH account

## When to use Radar

Radar evaluates risk and runs rules for three Stripe API objects: [Charges](https://docs.stripe.com/api/charges.md), [PaymentIntents](https://docs.stripe.com/api/payment_intents.md) and [SetupIntents](https://docs.stripe.com/api/setup_intents.md). Stripe designed the Radar rules to take four actions:

- Request 3DS authentication
- Allow the creation of the object
- Block the creation of the object
- Review the creation of a charge

The following table illustrates which rules Radar runs for each type of API object:

| Transaction type | Request 3DS   | Allow and Block | Review        |
| ---------------- | ------------- | --------------- | ------------- |
| Charge           | - Unsupported | ✓ Supported     | ✓ Supported   |
| PaymentIntent    | ✓ Supported   | ✓ Supported     | ✓ Supported   |
| SetupIntent      | ✓ Supported   | ✓ Supported     | - Unsupported |

If you use card payments, you can enable Radar for SetupIntents in your [Radar settings](https://dashboard.stripe.com/test/radar/settings).

### Use Radar with Stripe Checkout or Stripe Billing

This information also applies to payments created using Stripe Checkout and Stripe Billing. To provide a seamless flow for your _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) customers, the Radar fraud models only score the initial payment of a recurring Stripe Billing subscription, but evaluate rules for all payments.

## Risk outcomes

With Stripe Radar for Fraud Teams, each payment also includes a risk score that ranges from 0–99 to indicate the risk level on a more granular level. By default, a score of 65 or above indicates elevated risk, while a score of 75 or above indicates high risk.

The Stripe AI model evaluates the likelihood that a payment is fraudulent, and provides an assessment of one of the following values:

- [High risk](https://docs.stripe.com/radar/risk-evaluation.md#high-risk)
- [Elevated risk](https://docs.stripe.com/radar/risk-evaluation.md#elevated-risk)
- [Normal risk](https://docs.stripe.com/radar/risk-evaluation.md#normal-risk)
- [Not evaluated](https://docs.stripe.com/radar/risk-evaluation.md#not-evaluated)
- [Unknown risk](https://docs.stripe.com/radar/risk-evaluation.md#unknown-risk)

Each payment includes information on the _outcome_ of our risk evaluation.

Radar for Fraud Teams lets you see a [risk insights](https://docs.stripe.com/radar/reviews/risk-insights.md) section on the payment page that provides more details about why we assigned a payment a particular risk level and score.

If a financial institution (such as a card issuer or bank) [declines](https://docs.stripe.com/declines.md) a payment, Stripe also includes any information we receive from them as part of the outcome. You can see the outcome for each payment in the [Dashboard](https://dashboard.stripe.com/), or through the API in the [Outcome](https://docs.stripe.com/api.md#charge_object-outcome) attribute of the [Charge](https://docs.stripe.com/api.md#charge_object) object.

### High risk payments

Stripe reports payments as high risk when we believe they’re likely to be fraudulent. Payments of this risk level are [blocked](https://docs.stripe.com/radar/rules.md#built-in-rules) by default.

On the `Charge` object of a high risk payment, the `risk_level` is set to `highest`.

```json
...
"outcome":
{
  "network_status": "not_sent_to_network",
  "reason": "highest_risk_level",
  "risk_level": "highest",
  "risk_score": 92, // Provided only with Stripe Radar for Fraud Teams
  "seller_message": "Stripe blocked this charge as too risky.",
  "type": "blocked"
}
...
```

If Stripe Radar blocks a payment that you know is legitimate, you can remove the block by viewing the payment in the Dashboard and clicking **Add to allow list**. Adding a payment to the allow list doesn’t retry the payment, but it does prevent Stripe Radar from blocking future payment attempts with that payment method or email address.

> If you don’t see **Add to allow list**, you can [contact us](https://support.stripe.com/email) to add this feature to your Radar account.

### Elevated risk payments

Elevated risk payments have an increased chance of being fraudulent. Stripe Radar allows payments of this risk level by default. Stripe Radar for Fraud Teams automatically places elevated risk payments into your [review](https://docs.stripe.com/radar/reviews.md) queue so you can look at them more closely.

On the `Charge` object of an elevated risk payment, the `risk_level` is set to `elevated`.

```json
...
"outcome": {
  "network_status": "approved_by_network",
  "reason": "elevated_risk_level",
  "risk_level": "elevated",
  "risk_score": 68, // Provided only with Stripe Radar for Fraud Teams
  "seller_message": "Stripe evaluated this charge as having elevated risk, and placed it in your manual review queue.",
  "type": "manual_review"
}
...
```

### Normal risk payments

Payments with a normal risk evaluation have fewer characteristics that indicate fraud than payments with elevated or high risk levels. However, we recommend that you continue to be vigilant when fulfilling these orders. Payments that have normal risk can still turn out to be fraudulent, and there are other possible [types of fraud](https://docs.stripe.com/disputes/prevention/identifying-fraud.md) that can occur later in the order process.

On the `Charge` object of a successful payment with normal risk, the `risk_level` is set to `normal`.

```json
...
"outcome":
{
  "network_status": "approved_by_network",
  "reason": null,
  "seller_message": "The charge was authorized.",
  "risk_level": "normal",
  "risk_score": 23, // Provided only with Stripe Radar for Fraud Teams
  "type": "authorized"
}
...
```

### Not evaluated

Radar assesses the risk level for card, ACH, and SEPA Direct Debit payments, and sets the risk level to `not_assessed` for:

- All other non-card payments
- Card-based payments predating the public assignment of risk levels
- Payments where the business opts out of Radar fraud risk assessment

On the `Charge` object of an unevaluated payment, the `risk_level` is set to `not_assessed`.

```json
...
"outcome": {
  "network_status": "approved_by_network",
  "reason": "not_assessed_risk_level",
  "risk_level": "not_assessed",
  "seller_message": "Your business has opted out of Radar fraud risk assessments.",
  "type": "authorized"
}
...
```

### Unknown risk payments

In unusual cases, an error might cause risk evaluation to fail. If this happens, Stripe reports the payment as having unknown risk.

On the `Charge` object of an unknown risk payment, the `risk_level` is set to `unknown`.

```json
...
"outcome": {
  "network_status": "approved_by_network",
  "reason": "unknown_risk_level",
  "risk_level": "unknown",
  "seller_message": "Something went wrong while evaluating this payment. Our engineers have been notified and we’ll look into this as soon as possible.",
  "type": "authorized"
}
...
```

## Search for a specific risk level in the Dashboard

You can search for payments with a specific risk level using the **risk_level** search term and the desired risk level. For example, a search for [risk_level:highest](https://dashboard.stripe.com/test/search?query=risk_level%3Ahighest) returns a list of all payments with a high risk level. A search for [risk_level:elevated](https://dashboard.stripe.com/test/search?query=risk_level%3Aelevated) returns a list of all payments with an elevated risk level.

## Provide feedback on risk evaluations

While we use information across our network to evaluate a payment, you might have additional information about a payment as a result of a customer interaction. Our AI model responds to feedback you share with us, and you can help improve our fraud detection algorithms and the accuracy of our risk evaluations by [refunding](https://docs.stripe.com/refunds.md) and reporting payments that you believe are fraudulent.

To refund a payment and mark it as fraudulent, do the following:

1. View the payment in the Dashboard.
1. Click **Refund**.
1. Select **Fraudulent** as the **Reason**.
1. Provide a brief explanation.

You can also indicate that a payment is fraudulent when you [create a refund](https://docs.stripe.com/api.md#create_refund) using the API by providing `fraudulent` as the value for `reason`. This adds the email address and card fingerprint associated with the payment to the default email address and card fingerprint [block lists](https://docs.stripe.com/radar/lists.md#default-lists).

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// If you haven't refunded the charge, you can do so and let Stripe
// know it was fraudulent in one step.
var refund = await stripe.refunds.create({
  charge: "{{CHARGE_ID}}",
  reason: "fraudulent",
});

// If you already refunded the charge (without specifying the
// 'fraudulent' reason), you can still let us know it was fraudulent.
var charge = await stripe.charges.update(charge_id, {
  fraud_details: {
    user_report: "fraudulent",
  },
});
```

For a small subset of payments, Stripe modifies the reported risk score so we can measure the performance of our models and obtain data for subsequent model development. This allows us to make sure key metrics, such as false positive rate and recall, remain within desirable ranges, and that model performance continues to improve.

You can opt out of using the Stripe Radar API model by [contacting support](https://stripe.com/contact).
