<!-- Source URL: https://docs.stripe.com/payments/cards/surcharge -->
<!-- Fetched: 2026-05-11 -->

# Collect surcharges

Offset your card processing costs in the form of surcharges.

Surcharging allows you to offset some of the cost of accepting card payments. If you’re a platform that determines and collects payment fees from your connected accounts, surcharging allows your connected accounts to offset these costs.

## Compliance

If you impose a surcharge on your card payments, you must comply with all applicable laws, regulations, and card network rules. Surcharging requirements vary across regions and card types and might include obligations to:

- Accurately calculate permissible surcharge amounts so these amounts don’t exceed limits imposed by applicable law, card networks, or your cost of acceptance (which you must [determine](https://support.stripe.com/questions/exporting-payment-data)).
- Notify your acquirer or the card network of your intent to surcharge.
- Surcharge consistently across card networks or card products.
- Conspicuously disclose surcharge amounts that apply to each transaction and the total costs to the cardholder ahead of purchase, and reflect the surcharge separately on the transaction receipt.
- Provide the ability to cancel the transaction, or choose a different payment method after the surcharge amount is disclosed to the cardholder.

Even when surcharging functionality is available, you need to make sure that surcharging is permitted and that the surcharge you impose doesn’t exceed limitations set by applicable law, regulations, or the card networks. You’re responsible for understanding and complying with any country- or region-specific requirements or restrictions (including any state, province, or territory requirements or restrictions).

The information on this page relating to your compliance with these requirements is for your general guidance, and isn’t legal, tax, accounting, or other professional advice. Consult a professional if you’re unsure about your obligations.

> You’re fully responsible for any fines, penalties, or losses arising in connection with your failure to adhere to applicable surcharging requirements.

## Availability

Surcharging is available in the following countries and payment methods:

| Country       | Permitted payment methods | Maximum surcharge amount |
| ------------- | ------------------------- | ------------------------ |
| United States | Credit cards only         | 3%                       |
| Canada        | Credit cards only         | 2.4%                     |
| Australia     | All cards                 | 4%                       |
| New Zealand   | All cards                 | 4%                       |

## Before you begin

- Your integration must be on API version [2026-03-25.preview](https://docs.stripe.com/changelog.md?channel=preview#2026-03-25.preview). You must use the [public preview SDKs](https://docs.stripe.com/sdks/versioning.md?#public-preview-release-channel) or specify that [Stripe version](https://docs.stripe.com/api/versioning.md) in your request header to access preview features.
- See [API changes](https://docs.stripe.com/payments/cards/surcharge.md#migrate-to-public-preview) if you’re currently in the surcharging private preview.

## Determine surcharging availability

When you send either `surcharge.amount` or `surcharge.enforce_validation` and attach a payment method to your [PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md?api-version=preview#create_payment_intent-amount_details-surcharge), the response includes the following attributes to help you determine surcharge availability:

- `surcharge.status` indicates whether surcharging is available based on the country and the funding type of the payment method.
  - This returns `available` or `unavailable`.
- `surcharge.maximum_amount` indicates the maximum surcharge amount you can pass in. However, this value is a technical restriction, not a Stripe suggested amount. The surcharge limits imposed by laws or card network requirements in your jurisdiction might differ from the `surcharge.maximum_amount`. You’re responsible for making sure the surcharge you impose doesn’t exceed such limits.
- By default, Stripe validates the surcharge you apply to a given `PaymentIntent` against the maximum surcharge amount. If you attempt to surcharge in excess of the maximum surcharge amount, you get an error.

### Disable surcharge amount validations

- You can disable the maximum surcharge amount validation by passing in `enforce_validation: disabled`. If you disable validation by setting `enforce_validation: disabled`, Stripe doesn’t return the `maximum_amount` field and the default technical restriction on the surcharge amount doesn’t apply.
- You can disable the maximum surcharge amount validation at the time you create, update, or confirm a PaymentIntent. After you either enable or disable the maximum surcharge amount validation, you can no longer modify `surcharge.enforce_validation`.
- Passing in `enforce_validation: disabled` doesn’t disable any other restrictions on availability, including restrictions on card funding type and other regional restrictions. You must make sure that the surcharge you impose complies with all applicable laws and card network requirements whether or not you disable the maximum surcharge amount validation.
- You can also pass in `enforce_validation: enabled` to explicitly enable maximum surcharge amount technical validations. After you do so, you can no longer modify `surcharge.enforce_validation`.
- By default, Stripe enforces the maximum surcharge amount technical restrictions. If you don’t pass in any field in `surcharge.enforce_validation`, the response includes `enforce_validation: automatic` to signify this behavior.

#### Scenario 1: Enable validation and use `maximum_amount`

Create a `PaymentIntent` with validation enabled to receive the `maximum_amount`:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "usd",
  payment_method: "{{PAYMENTMETHOD_ID}}",
  payment_method_types: ["card"],
  amount_details: {
    surcharge: {
      enforce_validation: "enabled",
    },
  },
});
```

```json
{
  "id": "pi_123",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 0,
  "amount_details": {
    "surcharge": {
      "enforce_validation": "enabled",
      "maximum_amount": 24,
      "status": "available"
    }
  },
  "status": "requires_confirmation"
}
```

#### Scenario 2: Disable validation

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "usd",
  payment_method: "{{PAYMENTMETHOD_ID}}",
  payment_method_types: ["card"],
  amount_details: {
    surcharge: {
      enforce_validation: "disabled",
    },
  },
});
```

Stripe doesn’t return `maximum_amount` when you disable validation.

```json
{
  "id": "pi_123",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 0,
  "amount_details": {
    "surcharge": {
      "enforce_validation": "disabled",
      "status": "available"
    }
  },
  "status": "requires_confirmation"
}
```

## Calculate the surcharge amount

You must calculate surcharge amounts that comply with legal, regulatory, and card network requirements for each transaction. Your payment processing costs vary based on card brand, funding type, and the available networks.

If Stripe returns the maximum surcharge amount, always compare your calculated surcharge with the `surcharge.maximum_amount` returned in the PaymentIntent for the selected payment method to avoid errors. Card network and jurisdiction rules around surcharging might change over time. Stripe might modify the maximum surcharge amount. You’re responsible for consuming `surcharge.maximum_amount`. If you apply a surcharge in excess of the `surcharge.maximum_amount`, you might face validation errors.

## Confirm the payment with a surcharge

After calculating the surcharge and disclosing it to the customer, you can apply the surcharge when confirming or capturing the PaymentIntent.

> #### Specify the total amount inclusive of surcharge
>
> Stripe charges only the amount in the top-level `amount` field and doesn’t increment the amount with any additional values. So, you need to specify the total amount inclusive of the surcharge in the `amount` field. For example, for a 10.00 USD subtotal with a 0.20 USD surcharge, you’d pass in 10.20 USD in the top-level `amount` field. The surcharge amount of 0.20 USD would be specified separately in `amount_details[surcharge][amount]`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.confirm(
  "{{PAYMENTINTENT_ID}}",
  {
    amount_to_confirm: 1020,
    amount_details: {
      surcharge: {
        enforce_validation: "enabled",
        amount: 20,
      },
    },
  },
);
```

```json
{
  "id": "pi_123",
  "object": "payment_intent",
  "amount": 1020,
  "amount_capturable": 1020,
  "amount_details": {
    "surcharge": {
      "enforce_validation": "enabled",
      "amount": 20,
      "maximum_amount": 24,
      "status": "available"
    }
  },
  "status": "requires_capture"
}
```

## Apply surcharge when you create a PaymentIntent

Specify the top level `amount` field inclusive of the surcharge amount when creating a PaymentIntent:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1020,
  currency: "usd",
  payment_method: "{{PAYMENTMETHOD_ID}}",
  payment_method_types: ["card"],
  amount_details: {
    surcharge: {
      enforce_validation: "enabled",
      amount: 20,
    },
  },
});
```

## Apply surcharge on capture

You can also apply the surcharge when capturing. You can apply this behavior in various scenarios:

- **Adjust the surcharge post-confirmation**: If you need to modify the surcharge amount after confirmation, you can only reduce it. You can’t increase the surcharge amount during capture.
- **Multicapture scenarios**: When performing multiple captures on a single PaymentIntent, you can specify how much to surcharge for each individual capture. The sum of each surcharge amount passed during multicapture can’t exceed the surcharge amount passed upon confirmation.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{{PAYMENTINTENT_ID}}",
  {
    amount_to_capture: 1020,
    amount_details: {
      surcharge: {
        enforce_validation: "enabled",
        amount: 20,
      },
    },
  },
);
```

## Refunds

You must implement logic for returning surcharges to a customer when you issue a refund. Card network rules and certain laws and regulations require that you return the entire surcharge in the event of a full refund, and return a prorated surcharge in the case of a partial refund. For example, assume a customer returns an item with a value of 60.00 USD from a total order of 100.00 USD, where you applied a surcharge of 1.50 USD. To refund a prorated surcharge, you must refund 60.90 USD (60.00 USD, plus 60/100 of the 1.50 USD surcharge).

## Receipts

Stripe prebuilt receipts automatically display the surcharge. If you build custom receipts, show the applied surcharge amount separately. For example, for a purchase totaling 10.20 USD, where you applied a surcharge of 0.20 USD, you need to display 10.00 and 0.20 as separate line items in the receipt. Inspect the `amount_details.surcharge.amount` on the PaymentIntent to view the applied surcharge.

## Reporting

The `amount_details_surcharge_amount` field is available in the Sigma `payment_intents` table for your convenience. This field represents the surcharge amount applied on the transaction that you send to the card network.

## Feature interoperability

- You can use surcharging with [Payment Line Items](https://docs.stripe.com/payments/payment-line-items/flexible-payment-scenarios.md#add-a-surcharge).
- You can use surcharging with [Multicapture](https://docs.stripe.com/payments/multicapture.md), and you can specify different surcharge amounts on each capture.
  - You can’t capture a surcharge amount that’s greater than what was passed upon confirmation.
  - The sum of each surcharge amount passed during multicapture can’t exceed the surcharge amount passed upon confirmation.
- If you use surcharging with [Incremental Authorization](https://docs.stripe.com/payments/incremental-authorization.md), you can decrease the surcharge amount using the PaymentIntent capture endpoint if you capture less than you authorize. However, you can’t increase the surcharge amount regardless of how much the amount is increased during incremental authorization.
- Surcharging isn’t available when autocapturing with partial authorizations.

## Migration from private preview API changes

If you’re currently using the private preview version of surcharging, here are the key changes you need to make to access the public preview version behavior:

| Private Preview                                                         | Public Preview                                                          |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `amount_surcharge` (top-level)                                          | `amount_details[surcharge][amount]`                                     |
| Stripe automatically increments `amount`                                | You specify total `amount` inclusive of surcharge                       |
| Amount validation is always enforced                                    | `amount_details[surcharge][enforce_validation]`                         |
| Surcharge only on `/update` and `/confirm`                              | Surcharge available on `/create`, `/update`, `/confirm`, and `/capture` |
| `maximum_amount` and `status` returned in `payment_method_options` hash | `maximum_amount` and `status` returned in `amount_details` hash         |
