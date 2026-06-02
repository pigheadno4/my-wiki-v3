<!-- Source URL: https://docs.stripe.com/payments/klarna/disputes -->
<!-- Fetched: 2026-05-06 -->

# Respond to disputes

The lifecycle of Klarna disputes and how to respond to them.

> This guide is specific to Klarna payment disputes. Learn [how card disputes work](https://docs.stripe.com/disputes/how-disputes-work.md).

A dispute occurs when the Klarna customer files a complaint or return request for a specific order using the Klarna consumer app. Customers have up to 180 calendar days to file a dispute from the date of capture.
(See full diagram at https://docs.stripe.com/payments/klarna/disputes)

> #### Chargeback dispute outcomes
>
> Learn more about [chargeback disputes outcomes and their financial impact](https://docs.stripe.com/payments/klarna/disputes.md#chargeback-disputes)

These complaints and return requests correspond to specific [reason codes](https://docs.stripe.com/disputes/categories.md) that Stripe shares back with you. When someone files a Klarna dispute, the process varies slightly by reason code, but typically follows a standard pattern.

> #### Dispute-raising exceptions
>
> In some exceptional cases, Klarna must raise a dispute outside of the dispute limitations after 180 days of transaction. These exceptions include fraudulent disputes reported by the customers, legal claims raised through an external authority, local legal consumer protection rules, and debt collection.

## Comparison to card disputes

There are a few key similarities and differences between how Klarna and card disputes work.

|                                              | Card disputes                                                                                                                                                                                                                                                                                                  | Klarna disputes                                                                                                                                                                                                        |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inquiry support                              | Select card networks support inquiries, also known as a “retrieval” or “request for information”.                                                                                                                                                                                                              | All Klarna disputes, except for fraudulent disputes start as inquiries. *Unlike cards, businesses aren’t expected to submit evidence at this stage, and are expected to resolve the issue directly with the customer.* |
| Responding to disputes                       | Businesses can use the [Stripe Dashboard](https://dashboard.stripe.com/dashboard) or [Disputes API](https://docs.stripe.com/api/disputes.md) to manage and respond to disputes.                                                                                                                                | Same as cards.                                                                                                                                                                                                         |
| Dispute fees                                 | There are [separate fees](https://support.stripe.com/questions/june-2025-pricing-updates-for-disputes#fee-details) for receiving a dispute, in addition to countering a dispute. Dispute fees are assessed when the dispute is created and apply regardless of whether you ultimately win or lose the dispute. | There is only a [single fee](https://stripe.com/pricing/local-payment-methods#klarna) for losing a dispute. Dispute fees are assessed when the dispute is created, but are reversed if you ultimately win the dispute. |
| Partial disputes                             | Partial disputes are supported.                                                                                                                                                                                                                                                                                | Same as cards.                                                                                                                                                                                                         |
| Credit not processed Stripe dispute category | This [dispute category](https://docs.stripe.com/disputes/categories.md?card-network=visa#network-code-map) can refer to several card network reason codes, although the most common reason is when a customer has made a return and hasn’t yet received a refund.                                              | For Klarna, this dispute category refers to two distinct scenarios, although both reasons share the same reason code.                                                                                                  |

- **Return**: The most common scenario where a customer requests to initiate a return using the Klarna app.
- **Credit not processed**: The customer has already completed the return but hasn’t yet received a refund. |

## Inquiries

Inquiry disputes are an opportunity to resolve a customer’s issue before the dispute escalates to a chargeback and carries a fee. Stripe notifies you of an inquiry as soon as Klarna opens one. Inquiry creation is triggered by the customer taking action on the Klarna app, either by filing a complaint or requesting to return the purchase. When a customer files an inquiry, Klarna pauses any outstanding repayments from the customer until the dispute is resolved.

Almost all Klarna disputes start as inquiry disputes, which have a 21-calendar-day timeframe before they escalate. However, there are [specific exceptions documented by Klarna](https://docs.klarna.com/payments/after-payments/disputes/disputes-management-v1-v2/dispute-management-overview/#disputes-time-and-amount-limitations-limit-on-number-of-disputes-for-a-single-order) where disputes escalate directly to a chargeback. Fraudulent transactions are one example of this immediate escalation, but there are also other scenarios.

The intent of an inquiry is to give you early notice that the customer has an issue with the order so that you can proactively address the customer’s concern and potentially avoid chargeback disputes. During this stage, you can perform one of the following actions:

- **Contact your customer** to understand the reason for raising the dispute, and try to mutually find a resolution before the inquiry escalates to a chargeback. Customers have the ability to withdraw their inquiry using the Klarna app.
- **Accept the dispute** by issuing a refund of the full disputed amount. Refunding during the inquiry dispute period avoids a dispute fee and prevents the inquiry from being escalated to a chargeback dispute. Refunds can no longer be performed after the inquiry escalates to a chargeback dispute.
- **Allow the dispute to escalate**. If you ignore the inquiry or are unable to resolve the issue, it will automatically escalate to a chargeback. At this point you can submit evidence to challenge the dispute.

> #### Evidence submission during inquiry phase
>
> Klarna doesn’t accept evidence during the inquiry stage. You can only [submit evidence](https://docs.stripe.com/payments/klarna/disputes.md#submit-evidence) after a dispute escalates to a chargeback.

### Partial disputes

If a partial dispute is created, you can issue a partial refund. As long as the return amount is the same as the disputed amount, the inquiry will be resolved and won’t escalate to a chargeback dispute.

If a full-amount dispute is created for what should actually be a partial dispute, you can issue a partial refund for the returned item. However, this won’t resolve the inquiry because the disputed amount is for the entire order. After 21 calendar days (from return registration), the inquiry automatically escalates to a chargeback. At this point, you can contest the dispute with evidence (for example, only one item was returned and the order was already partially refunded).

### Responding to return inquiries

Customers paying with Klarna use inquiry disputes as a means to pause repayments while they’re in the process of completing a return for physical goods purchases. Klarna allows customers to file an inquiry and pause repayments before they’ve completed their return, but ask customers to provide proof of return, such as the return tracking ID.

Stripe only notifies you of a return inquiry when the customer provides the necessary information. This means return inquiries are visible in the Stripe Dashboard, the API, or events only when the customer provides return proof.

If you receive an inquiry dispute with the [Return](https://docs.stripe.com/disputes/categories.md?card-network=klarna) Klarna dispute code, make sure to handle these appropriately:

- Click into the dispute object view in your Stripe Dashboard for details on the return dispute.
- Select **Issuer evidence**. This provides the return tracking details.
- After you’ve verified that the return is in transit or has already been returned to you, process a refund within the 21-day inquiry period.

## Chargeback disputes

If an inquiry dispute remains unresolved after the 21 calendar day timeframe, the dispute automatically escalates to a chargeback dispute. At this point, Stripe withholds the disputed funds and the associated [dispute fee](https://stripe.com/pricing/local-payment-methods#klarna) from your account for this payment until the dispute is resolved.

During the chargeback dispute stage, you can counter disputes by [submitting evidence](https://docs.stripe.com/payments/klarna/disputes.md#submit-evidence) to Klarna, either in the Dashboard or with the API. You need to submit evidence by the deadline displayed in the Dashboard or [evidence_due_by](https://docs.stripe.com/api/disputes/evidence_object.md#dispute_evidence_object-evidence_due_by) for API users.

If you counter the dispute by submitting evidence, Klarna evaluates your response to decide the outcome.

- If you win the dispute, Stripe releases the withheld funds to your account, including the associated [dispute fee](https://stripe.com/pricing/local-payment-methods#klarna).
- If you lose the dispute, Stripe debits the withheld funds, including the associated [dispute fee](https://stripe.com/pricing/local-payment-methods#klarna). Klarna then returns the disputed amount to the customer.

### Submit evidence for chargeback disputes

You can only submit evidence after a dispute gets escalated to a chargeback. Use the Dashboard or the API to submit evidence against a chargeback dispute. If you fail to submit evidence, Klarna rules the dispute in favor of the customer.

Businesses have 12 calendar days from chargeback escalation to provide evidence, except for fraud disputes, which have a 5 day timeframe.

It’s only possible to submit a single round of evidence for Klarna disputes. Therefore, it’s important to ensure that all necessary evidence is gathered and submitted during the evidence submission window. Below we provide recommended guidelines based on dispute reasons below. For additional best practices, refer to [Klarna’s guide](https://docs.klarna.com/payments/after-payments/disputes/evidence-gathering/merchant-evidence-gathering/).

| Stripe dispute reason | Klarna dispute reason | Suggested evidence fields                                                                                                              | Description |
| --------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Product not received  | Goods not received    | - [shipping_tracking_number](https://docs.stripe.com/api/disputes/evidence_object.md#dispute_evidence_object-shipping_tracking_number) |

- [shipping_carrier](https://docs.stripe.com/api/disputes/evidence_object.md#dispute_evidence_object-shipping_carrier)
- [shipping_date](https://docs.stripe.com/api/disputes/evidence_object.md#dispute_evidence_object-shipping_date)
- [customer_communication](https://docs.stripe.com/api/disputes/evidence_object.md#dispute_evidence_object-customer_communication) | - All shipping related information |
  | Credit not processed | Return | - [uncategorized_file](https://docs.stripe.com/api/disputes/evidence_object.md#dispute_evidence_object-uncategorized_file)
- [refund_refusal_explanation](https://docs.stripe.com/api/disputes/evidence_object.md#dispute_evidence_object-refund_refusal_explanation) | |
  | Duplicate | Already paid | - [uncategorized_file](https://docs.stripe.com/api/disputes/evidence_object.md#dispute_evidence_object-uncategorized_file)
- [customer_communication](https://docs.stripe.com/api/disputes/evidence_object.md#dispute_evidence_object-customer_communication) | - Supporting evidence for your case in an attachment
- Any communication with the customer |
  | Fraudulent | Unauthorized | - [customer_communication](https://docs.stripe.com/api/disputes/evidence_object.md#dispute_evidence_object-customer_communication)
- [shipping_tracking_number](https://docs.stripe.com/api/disputes/evidence_object.md#dispute_evidence_object-shipping_tracking_number)
- [shipping_address](https://docs.stripe.com/api/disputes/evidence_object.md#dispute_evidence_object-shipping_address)
- [shipping_documentation](https://docs.stripe.com/api/disputes/evidence_object.md#dispute_evidence_object-shipping_documentation) | - All shipping related information
- Communication with the customer |
  | General | - Incorrect invoice
- High risk order | - [shipping_documentation](https://docs.stripe.com/api/disputes/evidence_object.md#dispute_evidence_object-shipping_documentation) | |
  | Product unacceptable | Faulty goods | - [customer_communication](https://docs.stripe.com/api/disputes/evidence_object.md#dispute_evidence_object-customer_communication) | |

Use the Dashboard or the API to submit evidence against a chargeback dispute. You can’t submit evidence to disputes that are still in the [inquiry](https://docs.stripe.com/payments/klarna/disputes.md#inquiries) stage.

#### Dashboard

1. Navigate to the [Disputes Dashboard](https://dashboard.stripe.com/disputes), and click the **Needs Response** tab.
1. Click the disputed payment. If you want to counter the dispute, click **Counter dispute**.
1. Select the reason why you should win the dispute, and click **Next**.
1. Enter and attach all the applicable supporting evidence. The `recommended` label indicates the best documents for the type of dispute.
1. After entering all the evidence, verify the information is correct by selecting the checkbox.
1. Click **Submit Evidence**.

> #### Submit evidence on time
>
> If you fail to submit evidence, Klarna rules the dispute in favor of the customer. See [Respond to disputes](https://docs.stripe.com/disputes/responding.md) for more information.

Alternatively, you can accept a dispute loss from the [Disputes Dashboard](https://dashboard.stripe.com/disputes) by clicking **Accept Dispute**.

#### API

You can counter a chargeback dispute using the [Dispute Evidence object](https://docs.stripe.com/api/disputes/evidence_object.md). Stripe sends a webhook [event](https://docs.stripe.com/api/events/types.md) for each stage of the dispute lifecycle. Use the [charge.dispute.funds_withdrawn](https://docs.stripe.com/api/events/types.md#event_types-charge.dispute.funds_withdrawn) event to track when an inquiry dispute escalates to a chargeback dispute.

Upload the file, and then use the file ID in the subsequent requests:

```node
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const fp = fs.readFileSync("@/path/to/a/file.jpg");
const upload = await stripe.files.create({
  file: {
    data: fp,
    name: "file.jpg",
    type: "application.octet-stream",
  },
  purpose: "dispute_evidence",
});
```

You must use the uploaded file only for a single dispute. You must upload another file for another dispute. The following code examples demonstrate how to submit evidence for different dispute reasons:

#### Product not received

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const dispute = await stripe.disputes.update("{{DISPUTE_ID}}", {
  evidence: {
    shipping_date: "6/28/2023",
    shipping_carrier: "dhl",
    shipping_tracking_number: "456789",
    customer_communication: "<file_id_from_the_upload_response>",
  },
  submit: true,
});
```

#### Credit not processed

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const dispute = await stripe.disputes.update("{{DISPUTE_ID}}", {
  evidence: {
    refund_refusal_explanation: "Reason why you can't issue refund",
    uncategorized_file: "<file_id_from_the_upload_response>",
  },
  submit: true,
});
```

#### Duplicate

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const dispute = await stripe.disputes.update("{{DISPUTE_ID}}", {
  evidence: {
    customer_communication: "<file_id_from_the_upload_response>",
    uncategorized_file: "<file_id_from_the_upload_response>",
  },
  submit: true,
});
```

#### Fraudulent

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const dispute = await stripe.disputes.update("{{DISPUTE_ID}}", {
  evidence: {
    shipping_date: "6/28/2023",
    shipping_carrier: "dhl",
    shipping_tracking_number: "456789",
    customer_communication: "<file_id_from_the_upload_response>",
  },
  submit: true,
});
```

If you want to submit extra evidence in the form of an attachment, use [uncategorized_file](https://docs.stripe.com/api/disputes/evidence_object.md#dispute_evidence_object-uncategorized_file). Combine all the attachments into a single document to improve your chances of winning the dispute. For example:

#### Upload the attachment

```node
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const fp = fs.readFileSync("@/path/to/a/file.jpg");
const upload = await stripe.files.create({
  file: {
    data: fp,
    name: "file.jpg",
    type: "application.octet-stream",
  },
  purpose: "dispute_evidence",
});
```

#### Set uncategorized_file during evidence submission

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const dispute = await stripe.disputes.update("{{DISPUTE_ID}}", {
  evidence: {
    shipping_date: "6/28/2023",
    shipping_carrier: "dhl",
    shipping_tracking_number: "456789",
    uncategorized_file: "<file_id_from_the_upload_response>",
  },
  submit: true,
});
```

#### Accept dispute loss

Accept a dispute loss by [closing the dispute](https://docs.stripe.com/api/disputes/close.md).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const dispute = await stripe.disputes.close("{{DISPUTE_ID}}");
```

### Guidelines

Follow [these guidelines](https://docs.klarna.com/payments/after-payments/disputes/evidence-gathering/merchant-evidence-gathering/) to submit the most relevant evidence for both Dashboard and API disputes.

## Create test disputes

You can simulate dispute creation by creating a transaction in a sandbox using the following email addresses and phone numbers in the given Klarna checkout region. A dispute automatically opens on the transaction. You can submit evidence on the dispute, but you can’t simulate the final dispute outcome in a testing environment.

Below, we have specially selected test data for the currently supported customer countries.

#### Australia

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number   |
| --------------------- | --------------------- | -------------------------------------------------- | -------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.au`                | `+61491574118` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.au`    | `+61491574632` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.au`          | `+61491575254` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.au`          | `+61491575789` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.au`     | `+61491575789` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.au`       | `+61491576801` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.au` | `+61491577426` |

#### Austria

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number     |
| --------------------- | --------------------- | -------------------------------------------------- | ---------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.at`                | `+4306762600762` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.at`    | `+4306762600763` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.at`          | `+4306762600764` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.at`          | `+4306762600765` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.at`     | `+4306762600766` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.at`       | `+4306762600767` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.at` | `+4306762600768` |

#### Belgium

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number   |
| --------------------- | --------------------- | -------------------------------------------------- | -------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.be`                | `+32485212140` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.be`    | `+32485212141` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.be`          | `+32485212142` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.be`          | `+32485212143` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.be`     | `+32485212144` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.be`       | `+32485212145` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.be` | `+32485212146` |

#### Canada

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number   |
| --------------------- | --------------------- | -------------------------------------------------- | -------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.ca`                | `+15195550116` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.ca`    | `+15195550117` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.ca`          | `+15195550118` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.ca`          | `+15195550119` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.ca`     | `+15195550120` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.ca`       | `+15195550121` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.ca` | `+15195550122` |

#### Czechia

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number    |
| --------------------- | --------------------- | -------------------------------------------------- | --------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.cz`                | `+420771623708` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.cz`    | `+420771623709` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.cz`          | `+420771623710` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.cz`          | `+420771623711` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.cz`     | `+420771623712` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.cz`       | `+420771623713` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.cz` | `+420771623714` |

#### Denmark

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number  |
| --------------------- | --------------------- | -------------------------------------------------- | ------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.dk`                | `+4561555921` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.dk`    | `+4531555956` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.dk`          | `+4571555576` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.dk`          | `+4561555601` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.dk`     | `+4571555705` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.dk`       | `+4541555404` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.dk` | `+4525558959` |

#### Finland

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number     |
| --------------------- | --------------------- | -------------------------------------------------- | ---------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.fi`                | `+3580401234585` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.fi`    | `+3580401234586` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.fi`          | `+3580401234587` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.fi`          | `+3580401234588` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.fi`     | `+3580401234589` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.fi`       | `+3580401234590` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.fi` | `+3580401234591` |

#### France

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number   |
| --------------------- | --------------------- | -------------------------------------------------- | -------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.fr`                | `+33656194339` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.fr`    | `+33656194340` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.fr`          | `+33656194341` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.fr`          | `+33656194342` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.fr`     | `+33656194343` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.fr`       | `+33656194344` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.fr` | `+33656194345` |

#### Germany

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number    |
| --------------------- | --------------------- | -------------------------------------------------- | --------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.de`                | `+491713920016` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.de`    | `+491713920017` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.de`          | `+491713920018` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.de`          | `+491713920019` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.de`     | `+491713920020` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.de`       | `+491713920021` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.de` | `+491713920022` |

#### Greece

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number    |
| --------------------- | --------------------- | -------------------------------------------------- | --------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.gr`                | `+306945553642` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.gr`    | `+306945553643` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.gr`          | `+306945553644` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.gr`          | `+306945553645` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.gr`     | `+306945553646` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.gr`       | `+306945553647` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.gr` | `+306945553648` |

#### Ireland

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number    |
| --------------------- | --------------------- | -------------------------------------------------- | --------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.ie`                | `+353855351418` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.ie`    | `+353855351419` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.ie`          | `+353855351420` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.ie`          | `+353855351421` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.ie`     | `+353855351422` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.ie`       | `+353855351423` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.ie` | `+353855351424` |

#### Italy

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number    |
| --------------------- | --------------------- | -------------------------------------------------- | --------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.it`                | `+393312232406` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.it`    | `+393312232407` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.it`          | `+393312232408` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.it`          | `+393312232409` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.it`     | `+393312232410` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.it`       | `+393312232411` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.it` | `+393312232412` |

#### Netherlands

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number   |
| --------------------- | --------------------- | -------------------------------------------------- | -------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.nl`                | `+31632167695` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.nl`    | `+31632167696` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.nl`          | `+31632167697` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.nl`          | `+31632167698` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.nl`     | `+31632167699` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.nl`       | `+31632167700` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.nl` | `+31632167701` |

#### New Zealand

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number    |
| --------------------- | --------------------- | -------------------------------------------------- | --------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.nz`                | `+642862276120` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.nz`    | `+648596357854` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.nz`          | `+642838916248` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.nz`          | `+64265615253`  |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.nz`     | `+648597431043` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.nz`       | `+64217249819`  |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.nz` | `+642293258935` |

#### Norway

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number  |
| --------------------- | --------------------- | -------------------------------------------------- | ------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.no`                | `+4740123474` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.no`    | `+4740123475` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.no`          | `+4740123476` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.no`          | `+4740123477` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.no`     | `+4740123478` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.no`       | `+4740123479` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.no` | `+4740123480` |

#### Poland

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number   |
| --------------------- | --------------------- | -------------------------------------------------- | -------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.pl`                | `+48795223342` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.pl`    | `+48795223343` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.pl`          | `+48795223344` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.pl`          | `+48795223345` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.pl`     | `+48795223346` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.pl`       | `+48795223347` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.pl` | `+48795223348` |

#### Portugal

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number    |
| --------------------- | --------------------- | -------------------------------------------------- | --------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.pt`                | `+351808151188` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.pt`    | `+351760715143` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.pt`          | `+351762748941` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.pt`          | `+351302066842` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.pt`     | `+351926839015` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.pt`       | `+351301381736` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.pt` | `+351937416657` |

#### Romania

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number   |
| --------------------- | --------------------- | -------------------------------------------------- | -------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.ro`                | `+40707129331` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.ro`    | `+40707129442` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.ro`          | `+40707129553` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.ro`          | `+40707129664` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.ro`     | `+40707129775` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.ro`       | `+40707129886` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.ro` | `+40707129997` |

#### Spain

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number   |
| --------------------- | --------------------- | -------------------------------------------------- | -------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.es`                | `+34670097138` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.es`    | `+34680859660` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.es`          | `+34735215817` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.es`          | `+34782234072` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.es`     | `+34699002829` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.es`       | `+34782153382` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.es` | `+34670369667` |

#### Sweden

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number   |
| --------------------- | --------------------- | -------------------------------------------------- | -------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.se`                | `+46701740637` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.se`    | `+46701740638` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.se`          | `+46701740639` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.se`          | `+46701740640` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.se`     | `+46701740641` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.se`       | `+46701740642` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.se` | `+46701740643` |

#### Switzerland

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number   |
| --------------------- | --------------------- | -------------------------------------------------- | -------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.ch`                | `+41618680018` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.ch`    | `+41618680019` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.ch`          | `+41618680020` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.ch`          | `+41618680021` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.ch`     | `+41618680022` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.ch`       | `+41618680023` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.ch` | `+41618680024` |

#### United Kingdom

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number    |
| --------------------- | --------------------- | -------------------------------------------------- | --------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.uk`                | `+445674519807` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.uk`    | `+447455511475` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.uk`          | `+447755535234` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.uk`          | `+443794116227` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.uk`     | `+443012348266` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.uk`       | `+447555529984` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.uk` | `+447555595216` |

#### United States

| Stripe dispute reason | Klarna dispute reason | Email                                              | Phone number   |
| --------------------- | --------------------- | -------------------------------------------------- | -------------- |
| Credit not processed  | Return                | `customer+disputed-return@email.us`                | `+13105550116` |
| Product not received  | Goods not received    | `customer+disputed-goods_not_received@email.us`    | `+13105550117` |
| Duplicate             | Already paid          | `customer+disputed-already_paid@email.us`          | `+13105550118` |
| Product unacceptable  | Faulty goods          | `customer+disputed-faulty_goods@email.us`          | `+13105550119` |
| General               | Incorrect invoice     | `customer+disputed-incorrect_invoice@email.us`     | `+13105550120` |
| General               | High risk order       | `customer+disputed-high_risk_order@email.us`       | `+13105550121` |
| Fraudulent            | Unauthorized purchase | `customer+disputed-unauthorized_purchase@email.us` | `+13105550122` |

## Dispute API

A [Dispute object](https://docs.stripe.com/api/issuing/disputes/object.md) contains a dispute type and Klarna dispute reason. These parameters are useful for countering a dispute.

### Type

The [Status](https://docs.stripe.com/api/disputes/object.md#dispute_object-status) parameter indicates the dispute type. The following table explains the dispute status and the state of the dispute.

| Status                   | Dispute type | Description                                                     |
| ------------------------ | ------------ | --------------------------------------------------------------- |
| `warning_needs_response` | Inquiry      | The inquiry is open and the business can issue a refund.        |
| `warning_closed`         | Inquiry      | The inquiry is closed.                                          |
| `needs_response`         | Chargeback   | The chargeback is open and the business can submit evidence.    |
| `under_review`           | Chargeback   | The chargeback is open and the evidence is submitted to Klarna. |
| `lost`                   | Chargeback   | The chargeback is closed and the business lost the dispute.     |
| `won`                    | Chargeback   | The Chargeback is closed and the business won the dispute.      |

### Klarna reason

The Klarna reason is mapped to [Stripe dispute reason](https://docs.stripe.com/disputes/categories.md?card-network=klarna) and displayed in the Dashboard as `Network Reason Code`.

The Stripe reason is available in the Dispute object as [reason](https://docs.stripe.com/api/disputes/object.md#dispute_object-reason) and the Klarna reason is available in [payment_method_details.klarna.reason_code](https://docs.stripe.com/api/disputes/object.md#dispute_object-payment_method_details-klarna-reason_code). The data is available in the API and webhook.

### Klarna chargeback loss reason code

When a business loses a chargeback, Klarna sends the loss reason which tells you why the dispute was unsuccessful. We map the Klarna chargeback loss reason to the Stripe chargeback loss reason code and display it in the Dashboard as `Chargeback Loss Reason Code`.

The Stripe chargeback loss reason is available in the `Dispute` object as [payment_method_details.klarna.chargeback_loss_reason_code](https://docs.stripe.com/api/disputes/object.md#dispute_object-payment_method_details-klarna-chargeback_loss_reason_code). The data is available in the API and webhook.

[Download Klarna’s merchant protection terms](https://docs.stripecdn.com/6bdb10db38769886e89f72d8c202c56368d50ac9fc9d90d04253594e6254e908.pdf)

| Chargeback loss reason code        | Description                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Shipping policy violated           | This reason indicates that the business didn’t adhere to the stated Klarna shipping policy. To prevent this, review and update shipping policies regularly and provide clear tracking information to customers. Review the [Submit evidence for chargeback disputes](https://docs.stripe.com/payments/klarna/disputes.md#submit-evidence) section for how to submit evidence for chargeback disputes. |
| Proof of delivery inadequate       | This signifies that the evidence provided to prove delivery of the product was insufficient. Review the [Submit evidence for chargeback disputes](https://docs.stripe.com/payments/klarna/disputes.md#submit-evidence) section for how to submit evidence for chargeback disputes.                                                                                                                    |
| Evidence missing proof of delivery | This reason indicates that the merchant didn’t provide any proof of delivery when required. Review the [Submit evidence for chargeback disputes](https://docs.stripe.com/payments/klarna/disputes.md#submit-evidence) section for how to submit evidence for chargeback disputes.                                                                                                                     |
| Evidence missing customer details  | This occurs when the business fails to provide necessary details about the customer that verify the legitimacy of the transaction.                                                                                                                                                                                                                                                                    |
| Merchant loss accepted             | This indicates that the business has accepted the financial loss from the transaction.                                                                                                                                                                                                                                                                                                                |
| Merchant didn’t counter dispute    | This reason signifies that the business didn’t counter the dispute with evidence submission in stipulated time.                                                                                                                                                                                                                                                                                       |
| Merchant didn’t issue refund       | This reason indicates that the business didn’t process a refund or issued a partial refund for a transaction.                                                                                                                                                                                                                                                                                         |
| Reason unspecified                 | You see this when we can’t clearly define the loss reason or when Klarna didn’t provide it.                                                                                                                                                                                                                                                                                                           |

> This field is available in the webhook only when Klarna closed the dispute. When the business didn’t counter the dispute or accept the loss, the field won’t be available in the webhook but will eventually be available in the API. The business needs to fetch the dispute object to get the field data. The value eventually displays in the Stripe Dashboard and embedded component as well.

## See also

- [Respond to disputes](https://docs.stripe.com/disputes/responding.md)
- [Dispute categories](https://docs.stripe.com/disputes/categories.md?card-network=klarna)
- [Dispute evidence object](https://docs.stripe.com/api/disputes/evidence_object.md)
