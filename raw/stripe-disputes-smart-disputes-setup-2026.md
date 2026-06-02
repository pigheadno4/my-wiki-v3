<!-- Source URL: https://docs.stripe.com/disputes/set-up-smart-disputes -->
<!-- Fetched: 2026-05-10 -->

# Set up and configure Smart Disputes

Automatically fight disputes and improve your dispute win rates.

Smart Disputes automatically compiles and submits high-quality evidence packets on your behalf before the dispute deadline. This helps you recover revenue you might otherwise lose to timeouts or incomplete submissions, while still giving you full control to review, edit, or submit your own evidence.

No additional setup is required after you enroll your account in Smart Disputes. Stripe builds and submits evidence packets automatically when enough data is available. You can also manually enhance these packets to improve performance.

## How it works

After you’re notified of a dispute:

- Stripe automatically builds evidence packets for every eligible dispute.
- You retain full control, and you can:
  - Submit your own evidence or the Smart Dispute packet manually.
  - Accept the dispute.
  - Rely on Smart Disputes to submit evidence automatically before the dispute deadline.
  - Improve your odds of winning by adding evidence to a Smart Disputes packet.

If you take no action, Smart Disputes submits the packet automatically to make sure you don’t miss the opportunity to contest a dispute. If you prefer, you can engage manually by submitting it before the deadline or adding more evidence to improve your likelihood of a win:

- For disputes with a packet already available, Stripe might recommend adding additional evidence (for example, fulfillment details or communication logs) to increase your chances of winning. However, this isn’t required.
- For other disputes, adding the recommended evidence might make them eligible for Smart Disputes submission. See more below on availability status.

## Use the Disputes API

If you manage disputes programmatically, update your integration to take advantage of Smart Disputes.

### Intended submission method

The Disputes API includes an `intended_submission_method` field to determine whether you or Stripe submits the dispute evidence. See the [Update a dispute API](https://docs.stripe.com/api/disputes/update.md?api-version=2025-10-29.preview) for more information.

| Field                 | Description                                                                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| prefer_manual         | Default setting. Stripe submits your evidence if you’ve added any. If you haven’t, Stripe submits a Smart Disputes packet (if available).              |
| prefer_smart_disputes | Stripe combines your evidence with Smart Disputes’ generated evidence and submits the strongest possible packet. Recommended for maximizing win rates. |

To get the best results, set `intended_submission_method` to `prefer_smart_disputes` when updating a dispute. When you add evidence, Stripe merges it with the Smart Disputes automatically-generated data to create a single, comprehensive packet.

## Improve performance

Smart Disputes relies on data quality. The more transaction and customer data available to Stripe, the stronger your evidence packets are.

### Provide more data at charge time

Smart Disputes uses an AI rules engine to extract evidence from your transaction data, Stripe internal data, historical win performances, and cardholder data. Adding more data when creating charges helps Stripe generate more complete and compelling evidence packets.

To collect fraud signals at charge time, make sure your integration includes [stripe.js](https://docs.stripe.com/js.md), or uses [Radar Sessions](https://docs.stripe.com/js/payment_intents/create_radar_session) to send browser information to Stripe.

#### Dashboard

If you use Stripe-hosted products such as Checkout, Payment Links, or Billing, you can collect key data fields automatically at checkout. Enable the following fields in your Dashboard settings:

- [Cardholder name](https://docs.stripe.com/payments/checkout/name-collection.md)
- Cardholder phone number
- Billing address
- Email address
- Terms of service acceptance
- Provide customers with an [email receipt](https://docs.stripe.com/receipts.md) by toggling **Successful payments** in [Customer Email](https://dashboard.stripe.com/settings/emails) settings.

We also recommend that you add your business URL to your [business profile](https://dashboard.stripe.com/settings/business-details).

#### API

If you create payments through the API, include as many of the following fields as possible:

| Object                                     | Field                                                                                                               | Description                                                                                |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| payment_intent, charge, customer           | payment_intent.customer[email], charge.billing_details[email], charge.customer[email]                               | Customer’s email address                                                                   |
| payment_intent, charge, customer           | payment_intent.customer[phone], charge.billing_details[phone], charge.customer[phone]                               | Customer’s phone number                                                                    |
| payment_intent, charge, card               | payment*intent.customer[address], charge.customer[address], charge.billing_details[address], card[address*\*]       | Customer’s billing address                                                                 |
| payment_intent, charge, card               | payment_intent.customer[name], charge.billing_details[name], charge.customer[name], card[name], card.customer[name] | Customer’s name                                                                            |
| payment_intent, checkout, product          | payment_intent.amount_details[line_items], checkout[line_items]                                                     | Provide detailed line item details on each transaction                                     |
| checkout, product                          | checkout.line_items.data.price[product], product[images], product[url], product[description]                        | Product information, including images and descriptions                                     |
| payment_intent, charge, customer, shipping | payment_intent.shipping[address], charge.shipping[address], customer.shipping[address]                              | Shipping address for a physical product                                                    |
| payment_intent, charge, customer, shipping | payment_intent.shipping[tracking_number], charge.shipping[tracking_number], customer.shipping[tracking_number]      | The tracking number for a physical product                                                 |
| payment_intent, charge, customer, shipping | payment_intent.shipping[carrier], charge.shipping[carrier], customer.shipping[carrier]                              | The delivery service that shipped a physical product, such as Fedex, UPS, USPS, and so on. |
| payment_intent, charge, customer, shipping | payment_intent.shipping[phone], charge.shipping[phone], customer.shipping[phone]                                    | Phone number of package recipient                                                          |
| payment_intent, charge                     | payment_intent[receipt_email], charge[receipt_email]                                                                | Email address that the receipt for this charge was sent to.                                |

Providing this data helps Stripe build evidence that supports cardholder identity and transaction legitimacy and is combined with other data throughout the Stripe network.

### Provide more data at dispute time

Even after a dispute is created, you can enhance the effectiveness of Smart Disputes by providing additional evidence.

#### Dashboard

Each Smart Dispute in the Dashboard includes:

- **Recommended evidence fields**: Adding data here lets Smart Disputes automatically assemble the packet, and run automations on your behalf tailored to the specific reason code.

- **Example**: Adding a tracking ID enables Stripe to automatically pull fulfillment data such as delivery history, proof of delivery, and shipping confirmation from several fulfillment providers.

- **Additional evidence field**: Use this for any information that doesn’t fit a recommended field but could still support your case (for example, screenshots or unique order context).

Adding this information can increase your win rate, and make previously ineligible disputes eligible for Smart Disputes.

#### API

If you manage disputes through the API, Stripe exposes two pieces of information that help you understand and influence Smart Disputes eligibility:

- **Recommended evidence fields**: The [Dispute](https://docs.stripe.com/api/disputes/object.md?api-version=2025-10-29.preview) object includes a `smart_disputes.recommended_evidence` array that lists which fields (or groups of fields) would strengthen the packet or make the dispute eligible for Smart Disputes. These fields are dynamically generated based on the dispute reason and network rules.

- **Availability (packet status)**: The dispute includes a `smart_disputes.status` value that signals whether a Smart Disputes packet currently exists for the dispute:

| Field             | Description                                                                                                                                                                          |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| available         | A Smart Disputes packet is ready and can be submitted automatically.                                                                                                                 |
| requires_evidence | A Smart Disputes packet becomes available if you provide the required evidence listed in the `recommended_evidence`. Supplying the required fields moves the dispute to `available`. |
| unavailable       | The dispute isn’t available for Smart Disputes. Supplying additional fields won’t change this status.                                                                                |

If `smart_disputes.status` isn’t `available` and you have `intended_submission_method` set to `prefer_smart_disputes`, Stripe falls back to submitting any manual evidence you’ve provided (such as a manual packet) until `smart_disputes.status` becomes `available`.

You can also add any custom evidence fields as you do today using the [Update Dispute](https://docs.stripe.com/api/disputes/update.md?api-version=2025-10-29.preview) endpoint, even if they aren’t a part of the `recommended_evidence` array. Make sure `intended_submission_method` is set to `prefer_smart_disputes`.

For example, to read recommended evidence and status:

`GET /v1/disputes/{dispute_id}` returns both the recommended fields and the current packet status:

```json
{
  "id": "dp_123",
  "amount": 1000,
  "reason": "fraudulent",
  "smart_disputes": {
    "status": "requires_evidence",
    "recommended_evidence": [
      ["shipping_carrier", "tracking_number"], // group — both required together
      ["customer_email"] // single required field
    ]
  }
}
```

In this example:

- The smart dispute status is `requires_evidence`.
- Supplying _either_ `customer_email` _or both_ `shipping_carrier` and `tracking_number` causes Stripe to re-evaluate the dispute and (if scoped rules are satisfied) update `smart_disputes.status` to `available`.

For example, to set `intended_submission_method` and submit recommended evidence:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const dispute = await stripe.disputes.update("{{DISPUTE_ID}}", {
  evidence: {
    shipping_tracking_number: "123",
    shipping_carrier: "ups",
  },
  intended_submission_method: "prefer_smart_disputes",
  submit: true,
});
```

In this example:

- `intended_submission_method` is set to `prefer_smart_disputes` selecting smart disputes as the preferred packet.
- Both recommended evidence fields (`shipping_tracking_number` and `shipping_carrier`) are provided.
- Supplying the recommended evidence causes Stripe to re-evaluate the dispute and update `smart_disputes.status` to `available` (if scoped rules are satisfied).

After you submit a dispute, you can view the submission method through the [`evidence_details.submission_method`](https://docs.stripe.com/api/disputes/object.md?api-version=2025-10-29.clover#dispute_object-evidence_details-submission_method) parameter on the `Dispute` object.
