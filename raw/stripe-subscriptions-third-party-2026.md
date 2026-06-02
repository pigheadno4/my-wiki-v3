<!-- Source URL: https://docs.stripe.com/billing/subscriptions/third-party-payment-processing -->
<!-- Fetched: 2026-05-13 -->

# Integrate with third-party payment processors

Learn how to use Stripe subscriptions and invoices with third party payment processors.

To process payments for your Billing _subscriptions_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) and _invoices_ (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) with a third-party processor, you have the following options:

# Integrate your own processor

> This is a Integrate your own processor for when process-payments-third-party is own-processor. View the full page at https://docs.stripe.com/billing/subscriptions/third-party-payment-processing?process-payments-third-party=own-processor.

Use Stripe Billing to manage subscription payments made with off-Stripe payment processors. With this integration, you can:

- Make requests for payments linked to a subscription with your off-Stripe payment processor
- Create and manage [charge automatically](https://docs.stripe.com/billing/collection-method.md#automatic-charging-versus-manual-payments) subscriptions with off-Stripe payments using [custom payment methods](https://docs.stripe.com/payments/payment-methods/custom-payment-methods.md) that reference off-Stripe payment methods
- Create [payment records](https://docs.stripe.com/payments/payment-records.md) to capture payment details of off-Stripe transactions, such as payment type and reference ID
- Use webhooks and record off-Stripe payment results to manage the subscription lifecycle
- Use [Connect](https://docs.stripe.com/connect/authentication.md) with the `Stripe-Account` header to perform operations on behalf of connected accounts

If you set up this integration, you no longer need to mark invoices as paid [out-of-band](https://support.stripe.com/questions/marking-an-invoice-paid-out-of-band) or rely on the [send_invoice](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method) method to accept off-Stripe payments.

> When integrating with a third-party payment processor, you’re responsible for complying with [applicable legal requirements](https://docs.stripe.com/payments/payment-methods/custom-payment-methods.md#compliance), including your agreement with your PSP, applicable laws, and so on.
>
> Additionally, you’re responsible for limiting your integration to [supported locations](https://docs.stripe.com/billing/subscriptions/third-party-payment-processing.md#supported-countries).

## Limitations

Make sure that the following limitations don’t conflict with your use case:

- You must build and maintain direct integrations with non-Stripe payment processors.
- If your integration uses the [Payment Element](https://docs.stripe.com/payments/elements.md) or a custom non-Stripe checkout flow, you can use Billing with non-Stripe payment processors. However, you can’t use Billing with [Checkout](https://docs.stripe.com/payments/checkout.md), because Checkout can’t capture details for off-Stripe payments.
- You can’t manage [disputes](https://docs.stripe.com/disputes.md) of off-Stripe payments in Stripe.
- You can’t initiate refunds from Stripe for payments processed through your third-party processor. You must process the refund directly with your third-party processor, then [report the refund to Stripe](https://docs.stripe.com/billing/subscriptions/third-party-payment-processing.md#handle-refunds) to maintain accurate payment records.
- Off-Stripe payments have limited support for [revenue recovery](https://docs.stripe.com/billing/revenue-recovery.md). They support [automations](https://docs.stripe.com/billing/automations.md) and [scheduled retries on failed payments](https://docs.stripe.com/billing/revenue-recovery/smart-retries.md), and are included in [revenue recovery analytics](https://docs.stripe.com/billing/revenue-recovery/recovery-analytics.md). However, they don’t support [revenue recovery emails](https://docs.stripe.com/billing/revenue-recovery/customer-emails.md) or [Smart Retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries.md#smart-retries).
- Off-Stripe payments are only available to businesses in the [specified countries](https://docs.stripe.com/billing/subscriptions/third-party-payment-processing.md#supported-business-countries), and you can only use them with payment processors operating in [certain countries](https://docs.stripe.com/billing/subscriptions/third-party-payment-processing.md#supported-payment-processor-countries).
- In the [customer portal](https://docs.stripe.com/customer-management.md), you can’t add discounts to subscriptions that use custom payment methods, if the session configuration’s [subscription update proration behavior](https://docs.stripe.com/api/customer_portal/configurations/object.md#portal_configuration_object-features-subscription_update-proration_behavior) is set to `always_invoice`.
- The [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page.md) doesn’t support invoices paid through a third-party processor. You must build your own payment page or use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) to collect payments outside of Stripe.

## Integration flow

You can integrate your custom payment page or Payment Element with Stripe Billing to process payments off-Stripe. This payment flow relies on two Stripe concepts that enable off-Stripe payments:

- **[Custom payment methods](https://docs.stripe.com/payments/payment-methods/custom-payment-methods.md)**: Enables you to create a reference to a non-Stripe payment method (such as a non-Stripe card or bank account) as a Stripe object. Custom payment methods used with the `charge_automatically` collection method allow you to receive webhooks for future subscription charges, and to apply off-Stripe payments to associated invoices.
- **[Payment records](https://docs.stripe.com/payments/payment-records.md)**: Records indicating successful off-Stripe payments to Stripe, along with associated structured metadata such as payment type, date, and external payment ID.

### Prerequisites

To use Stripe Billing with off-Stripe payment processors, you must:

- Set up a subscription integration for your off-Stripe payments.
- Renew subscriptions after you set up a subscription integration.

#### Subscription setup flow

To set up your off-Stripe subscriptions:

1. Configure a custom payment method type in the Dashboard.
1. Register customer information needed for subscriptions.
1. Collect payment information for payment methods not supported on Stripe.
1. Create subscriptions with payment information and payment records that occurred off-Stripe.
1. Record payments regardless of where they were processed.
   Steps in a checkout flow to set up a subscription while a customer is on-session (See full diagram at https://docs.stripe.com/billing/subscriptions/third-party-payment-processing)

#### Subscription renewal flow

In the subscription renewals and updates flow, you can:

- Process payments automatically when subscriptions are updated or renewed
- Create records of payment attempts for unified reporting and invoice management
  Steps to process off-session payments for a subscription (See full diagram at https://docs.stripe.com/billing/subscriptions/third-party-payment-processing)

## Configure custom payment method types

In the Dashboard, create the custom payment method type your customers will pay with. Custom payment method types allow you to specify branding for the custom payment methods you define for each customer. For example, if you’re using `SamplePay` as another processor, you might want to create a `SamplePayCard` to represent cards that you process with `SamplePay`.

Go to [Custom payment method types](https://dashboard.stripe.com/settings/custom_payment_methods) in the Dashboard. At the end of these steps, you’ll have one or more custom payment method types defined that you can offer your customers when they checkout.

1. Create a custom payment method type.
1. Set the display name and logo for the custom payment method type.

> Make sure your custom payment method aligns with our [marks policy](https://docs.stripe.com/payments/payment-methods/custom-payment-methods.md#marks-requirements) on the usage of display name and logo.

1. Click **Create** to make a new payment method type, `SamplePayCard`, which you can then use to set up a custom payment method.
1. You can see the created custom payment method type details in the Dashboard.
1. Custom payment method types aren’t retrievable through the API. We recommend storing the ID in your database and retrieving it during payment method creation.
1. After you configure custom payment methods, you can add them in either the [Payment Element](https://docs.stripe.com/payments/payment-element/custom-payment-methods.md) or directly to your custom payment page.

## Collect customer information and create subscription [Server]

Collect customer information (email address, billing address, and shipping address) and the [price](https://docs.stripe.com/api/prices/object.md) your customer selected. Create a new `Customer` or customer-configured `Account` with that information, then use it and the selected price to create a [Subscription](https://docs.stripe.com/api/subscriptions/object.md).

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  payment_behavior: "default_incomplete",
  payment_settings: {
    save_default_payment_method: "on_subscription",
  },
  expand: ["latest_invoice"],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  payment_behavior: "default_incomplete",
  payment_settings: {
    save_default_payment_method: "on_subscription",
  },
  expand: ["latest_invoice"],
});
```

At this point the subscription is `incomplete` with an open invoice.

## Collect payment [Client and Server]

Redirect the customer to your payment form to collect payment. Collect payment details for the payment method selected, and send a request to your server to initiate a payment session:

```javascript
const response = await fetch("/create_payment_session", {
  method: "POST",
  data: {
    // If needed, include an identifier for the processor selected by the customer
  },
});
// Redirect customer to processor to complete payment
window.location.href = response.redirectUrl;
```

Create a server-side handler to start a new payment session on your third-party processor. Then, send a return URL to redirect your customer to where they can complete payment.

#### Node.js

```javascript
app.post("/create_payment_session", async (req, res) => {
  const paymentSession = processorSdk.createPaymentSession({
    amount: invoice.amount_due,
    currency: invoice.currency,
    return_url: "/payment_session_completed",
  }); // Replace with code specific to your third-party processor. Invoice details should be retrieved from your server or Stripe, not passed from the client.
  return {
    redirectUrl: paymentSession.redirectUrl,
  };
});
```

## Record payment [Server]

When Stripe creates an invoice for a `charge_automatically` subscription, it automatically creates a default [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) object to attempt payment collection. Because you’re processing payments through your own processor and reporting the outcome with a `PaymentRecord`, Stripe cancels this default `PaymentIntent`. As a result, you see a **Canceled** payment entry next to your reported payment on each invoice. This is expected behavior and doesn’t affect the invoice or subscription status.

#### Synchronous payment outcome

After the customer completes their checkout session on the payment processor, [create a record of payment](https://docs.stripe.com/payments/payment-records.md#create-and-manage-paymentrecords) on Stripe:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = new Stripe('<<YOUR_SECRET_KEY>>', {
  apiVersion: '2026-04-22.dahlia'
});

app.post('/payment_session_completed', async (req, res) => {
  // `paymentReference` refers to the response object provided by your third-party processor
  // to indicate completion of payment. The exact contents vary based on the third-party processor.
  const paymentMethod = await stripe.paymentMethods.create({
    type: 'custom',
    custom: {
      // Set to the ID of the custom payment method type created in Step 1
      type: '{{CUSTOM_PAYMENT_METHOD_TYPE_ID}}', // Identifier of the custom payment method type created in the Dashboard.
    },
    metadata: {
      // Store any information specific to your third-party processor
      // that's needed to perform off-session payments
      {{PROCESSOR_AGREEMENT_ID_KEY}}: '{{PROCESSOR_AGREEMENT_ID}}',
    }
  });

  // Attach custom payment method to customer
  await stripe.paymentMethods.attach(paymentMethod.id, {
    customer: customer.id
  });

  // Set the payment method as the default for the subscription
  await stripe.subscriptions.update(subscription.id, {
    default_payment_method: paymentMethod.id
  });

  // Report payment
  const paymentRecord = await stripe.paymentRecords.reportPayment({
    amount_requested: {
      value: paymentReference.amount,
      currency: paymentReference.currency
    },
    payment_method_details: {
      payment_method: paymentMethod.id
    },
    customer_details: {
      customer: customer.id
    },
    initiated_at: paymentReference.initiated_at,
    customer_presence: 'on_session',
    processor_details: {
      type: 'custom',
      custom: {
        payment_reference: paymentReference.id
      }
    },
    outcome: paymentReference.success ? 'guaranteed' : 'failed',
    guaranteed: paymentReference.success
      ? { guaranteed_at: paymentResult.completed_at }
      : undefined,
    failed: !paymentReference.success
      ? { failed_at: paymentResult.completed_at }
      : undefined
  });

  // Attach the payment record to the invoice
  await stripe.invoices.attachPayment(subscription.latest_invoice.id, {
    payment_record: paymentRecord.id
  });
});
```

#### Asynchronous payment outcome

After the customer completes their checkout session on the payment processor, create a record of payment on Stripe to indicate that the payment is initiated.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = new Stripe('<<YOUR_SECRET_KEY>>', {
  apiVersion: '2026-04-22.dahlia'
});

app.post('/payment_session_initiated', async (req, res) => {
  // `paymentReference` refers to the response object provided by your third-party processor
  // to indicate completion of payment. The exact contents vary based on the third-party processor.
  const paymentMethod = await stripe.paymentMethods.create({
    type: 'custom',
    custom: {
      // Set to the ID of the custom payment method type created in Step 1
      type: '{{CUSTOM_PAYMENT_METHOD_TYPE_ID}}', // Identifier of the custom payment method type created in the Dashboard.
    },
    metadata: {
      // Store any information specific to your third-party processor
      // that's needed to perform off-session payments
      {{PROCESSOR_AGREEMENT_ID_KEY}}: '{{PROCESSOR_AGREEMENT_ID}}',
    }
  });

  // Attach custom payment method to customer
  await stripe.paymentMethods.attach(paymentMethod.id, {
    customer: customer.id
  });

  // Set the payment method as the default for the subscription
  await stripe.subscriptions.update(subscription.id, {
    default_payment_method: paymentMethod.id
  });

  // Report initiated payment
  const paymentRecord = await stripe.paymentRecords.reportPayment({
    amount_requested: {
      value: paymentReference.amount,
      currency: paymentReference.currency
    },
    payment_method_details: {
      payment_method: paymentMethod.id
    },
    customer_details: {
      customer: customer.id
    },
    initiated_at: paymentReference.initiated_at,
    customer_presence: 'on_session',
    processor_details: {
      type: 'custom',
      custom: {
        payment_reference: paymentReference.id
      }
    },
  });

  // Attach the payment record to the invoice
  await stripe.invoices.attachPayment(subscription.latest_invoice.id, {
    payment_record: paymentRecord.id
  });
});
```

After your third-party processor responds with the payment result, report the outcome of the payment attempt to Stripe.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = new Stripe("<<YOUR_SECRET_KEY>>", {
  apiVersion: "2026-04-22.dahlia;",
});

app.post("/payment_session_completed", async (req, res) => {
  await stripe.paymentRecords.reportPaymentAttemptGuaranteed(paymentRecord.id, {
    guaranteed_at: Date.now(),
  });
  // or, if payment failed
  await stripe.paymentRecords.reportPaymentAttemptFailed(paymentRecord.id, {
    failed_at: Date.now(),
  });
});
```

> When setting up your custom payment method and integration, don’t save any sensitive payment credentials with Stripe, including PANs.

Attaching a payment record to the invoice marks it as `paid` and transitions the associated subscription to `active`. You must [report a payment](https://docs.stripe.com/payments/payment-records.md#report-a-new-payment) within 23 hours of creating the subscription, or the subscription transitions to `incomplete_expired` and you need to recreate it.

## Configure the webhook handler

To process future payments for a `charge_automatically` subscription, configure a handler to receive webhook events. Specifically, you’ll handle the [invoice.payment_attempt_required](https://docs.stripe.com/api/events/types.md#event_types-invoice.payment_attempt_required) webhook, which Stripe sends when a new invoice is finalized and requires payment through your custom payment method:

> Most integrations don’t need to set `auto_advance: false` on an invoice. However, if your integration requires it for any reason, Stripe won’t attempt payment on the invoice while `auto_advance` is set to `false`, and the `invoice.payment_attempt_required` webhook won’t be sent. To resume normal payment collection and trigger the webhook, update the invoice to set `auto_advance` back to `true`.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = new Stripe("<<YOUR_SECRET_KEY>>", {
  apiVersion: "2026-04-22.dahlia",
});

app.post("/webhook", async (request, response) => {
  const payload = request.body;
  const sig = request.headers["stripe-signature"];

  let event;

  try {
    event = stripe.webhooks.constructEvent(payload, sig, endpointSecret);
  } catch (err) {
    return response.status(400).send(`Webhook Error: ${err.message}`);
  }

  switch (event.type) {
    case "invoice.payment_attempt_required":
      const invoiceId = event.data.object.id;
      // Validate that the invoice still has an outstanding balance
      const invoice = await stripe.invoices.retrieve(invoiceId);
      if (invoice.amount_remaining > 0) {
        // Asynchronously schedule payment collection
        processOffSessionPayment(invoice);
      }
      break;
  }
  response.send(200);
});

async function processOffSessionPayment(invoice) {
  // Fetch payment method details from the invoice
  // to complete off-session payment
  const customPaymentMethod = await stripe.paymentMethods.retrieve(
    invoice.defaultPaymentMethod,
  );
  // Collect payment from the third-party processor
  const paymentReference = await processorSdk.collectPayment({
    amount: invoice.amount_remaining,
    agreement_id:
      customPaymentMethod.metadata["{{PROCESSOR_AGREEMENT_ID_KEY}}"],
  }); // Replace with code specific to your third-party processor.

  // Report payment
  const paymentRecord = await stripe.paymentRecords.reportPayment({
    amount_requested: {
      value: invoice.amount_remaining,
      currency: invoice.currency,
    },
    payment_method_details: {
      payment_method: customPaymentMethod.id,
    },
    customer_details: {
      customer: invoice.customer,
    },
    initiated_at: paymentReference.initiated_at,
    customer_presence: "off_session",
    processor_details: {
      type: "custom",
      custom: {
        payment_reference: paymentReference.id,
      },
    },
    outcome: paymentReference.success ? "guaranteed" : "failed",
    guaranteed:
      paymentReference.success ?
        { guaranteed_at: paymentResult.completed_at }
      : undefined,
    failed:
      !paymentReference.success ?
        { failed_at: paymentResult.completed_at }
      : undefined,
  });

  // Attach the payment record to the invoice
  await stripe.invoices.attachPayment(invoice.id, {
    payment_record: paymentRecord.id,
  });
}
```

## Retry failed payments

When a failed payment is reported, the invoice remains open. If the Subscription was created in an `incomplete` status, it remains `incomplete` until successful payment is reported, or it expires.

If the Subscription was previously `active`, it transitions to `past_due`. If retries are configured, then the Subscription moves into dunning and we send subsequent [invoice.payment_attempt_required](https://docs.stripe.com/api/events/types.md#event_types-invoice.payment_attempt_required) webhook events when retries are attempted.

You can configure retries using custom retry schedules or [automations](https://docs.stripe.com/billing/automations.md). We don’t support [Smart Retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries.md#smart-retries).

For custom retry schedules, if you exhaust all retries, the invoice and subscription might transition depending on your [configured retry settings](https://dashboard.stripe.com/revenue-recovery/retries). You can also manually cancel the subscription earlier if you can’t collect payment.

When retrying a failed payment, report the new attempt against the existing `PaymentRecord` object using [report_payment_attempt](https://docs.stripe.com/api/payment_records/report_payment_attempt.md) or [report_payment_attempt_guaranteed](https://docs.stripe.com/api/payment_records/report_payment_attempt_guaranteed.md). Don’t create a new `PaymentRecord` with [report_payment](https://docs.stripe.com/api/payment_records/report_payment.md). Creating a separate `PaymentRecord` for each attempt results in multiple distinct payment entries on the invoice (for example, one **Failed** and one **Succeeded**), rather than a single payment with a consolidated history of attempts.

To handle payment retries, extend the handler implemented in the [Configure webhook handler](https://docs.stripe.com/billing/subscriptions/third-party-payment-processing.md#configure-webhook) section:

#### Node.js

```javascript
async function processOffSessionPayment(invoice) {
  const customPaymentMethod = await stripe.paymentMethods.retrieve(
    invoice.defaultPaymentMethod,
  );

  // No changes needed, collect payment as before from the third-party processor
  const paymentResult = await processorSdk.collectPayment({
    amount: invoice.amount_remaining,
    agreement_id:
      customPaymentMethod.metadata["{{PROCESSOR_AGREEMENT_ID_KEY}}"],
  });
  // Query for any existing payment records, which indicate a prior payment attempt
  const invoicePayments = await stripe.invoicePayments.list({
    invoice: invoice.id,
    payment: { type: "payment_record" },
  });

  if (invoicePayments.data.length) {
    // If there's an existing payment record, report a new attempt against that record
    await stripe.paymentRecords.reportPaymentAttempt({
      id: invoicePayments.data[0].payment.id,
      initiated_at: Date.now(),
      payment_method_details: {
        payment_method: customPaymentMethod.id,
      },
      outcome: paymentResult.success ? "guaranteed" : "failed",
      guaranteed:
        paymentResult.success ?
          { guaranteed_at: paymentResult.completed_at }
        : undefined,
      failed:
        !paymentResult.success ?
          { failed_at: paymentResult.completed_at }
        : undefined,
    });
  } else {
    // Otherwise, report a new payment and attach it to the invoice
    const paymentRecord = await stripe.paymentRecords.reportPayment({
      amount_requested: {
        value: invoice.amount_remaining,
        currency: invoice.currency,
      },
      payment_method_details: {
        payment_method: customPaymentMethod.id,
      },
      customer_details: {
        customer: invoice.customer,
      },
      initiated_at: paymentResult.initiated_at,
      customer_presence: "off_session",
      processor_details: {
        type: "custom",
        custom: {
          payment_reference: paymentResult.id,
        },
      },
      outcome: paymentResult.success ? "guaranteed" : "failed",
      guaranteed:
        paymentResult.success ?
          { guaranteed_at: paymentResult.completed_at }
        : undefined,
      failed:
        !paymentResult.success ?
          { failed_at: paymentResult.completed_at }
        : undefined,
    });

    // Attach the payment record to the invoice
    await stripe.invoices.attachPayment(invoice.id, {
      payment_record: paymentRecord.id,
    });
  }
}
```

## Handle canceled payments

You can report canceled payments to Stripe when using the asynchronous payment flow. Use this option when a payment is initiated but later canceled.

To report a canceled payment, first create a payment record indicating the payment is initiated (as shown in [Record payment](https://docs.stripe.com/billing/subscriptions/third-party-payment-processing.md#record-payment)).

When the payment is canceled, report the cancellation to Stripe:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = new Stripe("<<YOUR_SECRET_KEY>>", {
  apiVersion: "2026-04-22.dahlia",
});

app.post("/payment_session_canceled", async (req, res) => {
  await stripe.paymentRecords.reportPaymentAttemptCanceled(paymentRecord.id, {
    canceled_at: Date.now(),
  });
});
```

## Handle refunds

When your third-party processor processes a refund, you can report it to Stripe to maintain accurate payment records. You can report both full and partial refunds, but only after the original payment is [successfully recorded](https://docs.stripe.com/billing/subscriptions/third-party-payment-processing.md#record-payment) in Stripe.

To report a refund, you need to provide the refund reference from your third-party processor, which must be unique for each Payment Record. For a partial refund, specify the [amount](https://docs.stripe.com/api/payment-record/report-refund/report.md#report_payment_records_report_refund-amount) parameter.

To maintain accurate accounting data, log refunds on issued invoices by using [Credit Notes](https://docs.stripe.com/api/credit_notes/object.md) to adjust the invoice amounts.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = new Stripe("<<YOUR_SECRET_KEY>>", {
  apiVersion: "2026-04-22.dahlia",
});

app.post("/payment_refunded", async (req, res) => {
  const paymentRecordRefund = await stripe.paymentRecords.reportRefund(
    paymentRecord.id,
    {
      // `refundReference` refers to the response object provided by your third-party processor
      // when the refund is issued. The exact contents vary based on the third-party processor.
      processor_details: {
        type: "custom",
        custom: {
          refund_reference: refundReference.id,
        },
      },
      outcome: "refunded",
      refunded: {
        refunded_at: Date.now(),
      },
    },
  );

  const invoicePayments = await stripe.invoicePayments.list({
    payment: {
      type: "payment_record",
      payment_record: paymentRecordId,
    },
  });

  // Create a credit note to reflect the refund on the invoice
  await stripe.creditNotes.create({
    invoice: invoicePayments.data[0].invoice,
    refunds: [
      {
        type: "payment_record_refund",
        // amount_refunded is an optional field. If not provided, the credit note is created for the full amount of the PaymentRecord refund.
        amount_refunded:
          paymentRecordRefund.refund_details[0].amount_refunded.value,
        payment_record_refund: {
          payment_record: paymentRecordRefund.id,
          refund_group: refundReference.id,
        },
      },
    ],
  });
});
```

## Allow management of subscriptions with custom payment methods in the customer portal

Customers can use the customer portal to manage their own subscriptions that use custom payment methods, which reduces their need for interaction with your support team. The customer portal supports the following functionality for subscriptions with custom payment methods:

- **Update subscription**: Modify subscription details such as quantities and pricing
- **Switch payment methods**: Change the payment method to another custom payment method or to a Stripe-supported payment method
- **Set default payment method**: Mark a custom payment method as the default for future charges
- **Cancel subscription**: Cancel an active subscription that uses a custom payment method

## Fees for using third-party payment processors

Billing volume from third-party processors is considered part of your total billing volume, which includes transactions both on and off Stripe that use Stripe Billing functionality. The standard fee structure applies based on your billing contract, either pay-as-you-go or a subscription plan. For more information, see [Billing pricing](https://stripe.com/billing/pricing) and [how Stripe charges for Billing](https://support.stripe.com/questions/july-2024-changes-to-stripe-billing).

In addition, one-off invoices that are paid through a third-party payment processor are monetized under [Invoicing pricing](https://stripe.com/invoicing/pricing). Invoices [marked as paid out-of-band](https://docs.stripe.com/api/invoices/pay.md#pay_invoice-paid_out_of_band) aren’t charged as usual.

## Supported countries

This feature is available to businesses located in:

### Countries where businesses can be located

- AE
- AT
- AU
- BE
- BG
- BR
- CA
- CH
- CY
- CZ
- DE
- DK
- EE
- ES
- FI
- FR
- GB
- GR
- HK
- HR
- HU
- IE
- IN
- IT
- JP
- LI
- LT
- LU
- LV
- MT
- MX
- NL
- NO
- NZ
- PL
- PT
- RO
- SE
- SG
- SI
- SK
- TH
- US

This feature is available to use with payment processors located in:

### Countries where payment processors can be located

- AE
- AG
- AL
- AM
- AO
- AR
- AT
- AU
- AZ
- BA
- BD
- BE
- BG
- BH
- BJ
- BN
- BO
- BR
- BS
- BT
- BW
- CA
- CH
- CI
- CL
- CN
- CO
- CR
- CY
- CZ
- DE
- DK
- DO
- DZ
- EC
- EE
- EG
- ES
- ET
- FI
- FR
- GB
- GH
- GR
- GT
- GY
- HK
- HR
- HU
- ID
- IE
- IN
- IT
- JM
- JO
- JP
- KH
- KR
- KW
- KZ
- LA
- LI
- LT
- LU
- LV
- MA
- MC
- MD
- MG
- MK
- MN
- MO
- MT
- MU
- MX
- MY
- MZ
- NA
- NE
- NG
- NL
- NO
- NZ
- OM
- PA
- PE
- PH
- PK
- PL
- PT
- PY
- QA
- RO
- RS
- RW
- SA
- SE
- SG
- SI
- SK
- SM
- SN
- SV
- TH
- TN
- TR
- TT
- TW
- US
- UY
- UZ
- VN
- ZA

# Use out-of-band invoices

> This is a Use out-of-band invoices for when process-payments-third-party is out-of-band. View the full page at https://docs.stripe.com/billing/subscriptions/third-party-payment-processing?process-payments-third-party=out-of-band.

When you submit payments for Stripe invoices to a third-party processor, your system records the invoices as `paid_out_of_band`. The remaining subscription service period continues normally. To use out-of-band invoices, you need to customize two key Stripe Billing workflows:

- Collecting customers’ payment method details
- Paying invoices

## Request flow

The following diagrams illustrate the high-level request flows of a multiprocessor integration.

### Collecting and storing customers’ payment method details

(See full diagram at https://docs.stripe.com/billing/subscriptions/third-party-payment-processing)

### Paying invoices

(See full diagram at https://docs.stripe.com/billing/subscriptions/third-party-payment-processing)

## Configure Stripe

To set up a multiprocessor integration, you must make some configuration changes to Stripe.

### Disable invoice emails

To prevent customers from paying directly on Stripe, disable automatic emails for any customer who processes payments on a third-party processor. To disable automatic emails:

- From the [automatic billing settings](https://dashboard.stripe.com/settings/billing/automatic) in the Dashboard, disable **Send finalized invoices and credit notes to customers**. After you change this setting, changes to any subscription with [collection_method](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-collection_method) set to `send_invoice` won’t trigger customer emails. Only use this if all of your emailed subscription invoices are paid with a third-party processor.

### Configure the customer portal

If you use the [customer portal](https://docs.stripe.com/customer-management.md#customer-portal-features), disable **Allow customers to view and update payment methods** in the [customer portal settings](https://dashboard.stripe.com/settings/billing/portal). You must also disable the **Customers can switch plans** setting. You need to build custom flows to allow users to self-serve updates to their payment method on a third-party processor.

## Sign up new customers

### Create a Stripe customer

#### Accounts v2

First, create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts.md) object on Stripe.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const account = await stripe.v2.core.accounts.create({
  configuration: {
    customer: {},
  },
});
```

#### Customers v1

First, create a blank [Customer](https://docs.stripe.com/api/customers.md) object on Stripe.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

### Create a subscription

Next, create a [Subscription](https://docs.stripe.com/api/subscription.md) and set the `collection_method` to `send_invoice`. This setting doesn’t require a Stripe payment method and generates [Invoices](https://docs.stripe.com/api/invoice.md) that must be paid directly instead. Set the `days_until_due` parameter to the number of days an unpaid invoice remains open before your [failed payment logic](https://dashboard.stripe.com/settings/billing/automatic) activates. You’re responsible for retrying failed payments on the third-party processor, and you must set a long enough time for `days_until_due` so that any recovery workflows you implement have time to complete.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  collection_method: "send_invoice",
  days_until_due: 30,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  customer: "{{CUSTOMER_ID}}",
  collection_method: "send_invoice",
  days_until_due: 30,
});
```

### Present the amount to the user for payment

Third-party payments don’t work with _Stripe Checkout_ (A low-code payment integration that creates a customizable form for collecting payments. You can embed Checkout directly in your website, redirect customers to a Stripe-hosted payment page, or create a customized checkout page with Stripe Elements) or _Elements_ (A set of UI components for building a web checkout flow. They adapt to your customer's locale, validate input, and use tokenization, keeping sensitive customer data from touching your server). You must build a checkout flow that uses the third party to create a valid payment method, but uses Stripe to determine billable amounts. To determine the amount to charge in the checkout flow, [retrieve the initial invoice](https://docs.stripe.com/api/invoices/retrieve.md) generated by the subscription.

### Collect payment method details (Third party)

Follow the instructions from the third-party processor to collect payment method details from customers. Make sure to set up payment methods for use in future or off-session transactions.

The output of this step varies by processor. Some third-party processors provide a payment method token that you use to generate payments on that processor.

### Update the `Customer` or `Account` object

#### Accounts v2

Update the `Account` object created in the [first step](https://docs.stripe.com/billing/subscriptions/third-party-payment-processing.md#create-customer) of the subscription creation flow. For convenience, store non-sensitive third-party tokens as [metadata](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-metadata) on the `Account` object.

Remember to disable the **Send finalized invoices and credit notes to customers** option before setting the `email` property on the `Account`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const account = await stripe.v2.core.accounts.update("{{CUSTOMERACCOUNT_ID}}", {
  metadata: {
    description: "Third-party payment customer",
    third_party_customer_id: "{{THIRD_PARTY_CUSTOMER_ID}}",
    third_party_payment_method_id: "{{THIRD_PARTY_PAYMENT_METHOD_ID}}",
  },
});
```

#### Customers v1

Update the `Customer` object created in the [first step](https://docs.stripe.com/billing/subscriptions/third-party-payment-processing.md#create-customer) of the subscription creation flow. For convenience, store non-sensitive third-party tokens as [metadata](https://docs.stripe.com/api/customers/object.md#customer_object-metadata) on the `Customer` object.

Remember to disable the **Send finalized invoices and credit notes to customers** option before setting the `email` property on the `Customer`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.update("{{CUSTOMER_ID}}", {
  description: "Third-party payment customer",
  metadata: {
    third_party_customer_id: "{{THIRD_PARTY_CUSTOMER_ID}}",
    third_party_payment_method_id: "{{THIRD_PARTY_PAYMENT_METHOD_ID}}",
  },
});
```

## Collect payment

### Listen for invoice.created webhook events

All invoices (including the first invoice created from a subscription) start in a draft status and trigger [invoice.created](https://docs.stripe.com/api/events/types.md#event_types-invoice.created) webhooks. Invoices created by a subscription are automatically finalized after 1 hour to allow time for integrations to modify the draft invoice. You can [finalize the invoice manually](https://docs.stripe.com/api/invoices/finalize.md) if you want to skip this delay.

Invoice finalization triggers an [invoice.finalized](https://docs.stripe.com/api/events/types.md#event_types-invoice.finalized) event, which you should [listen for](https://docs.stripe.com/billing/subscriptions/webhooks.md) to trigger payments on the third-party processor.

### Process payments (Third party)

Follow the instructions from the third-party processor to collect payments for the amounts represented on each invoice using the tokens stored on the associated Customer object. This might include listening to webhooks from the third party for notifications of successful payments.

### Mark the Stripe invoice as paid out-of-band

When payment on the third party processor is successful, mark the corresponding invoice as `paid_out_of_band`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const invoice = await stripe.invoices.pay("{{INVOICE_ID}}", {
  paid_out_of_band: true,
});
```

Mark the invoice as `paid` before the subscription’s payment due date to keep the subscription operating normally. The Subscription object’s [days_until_due](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-days_until_due) attribute defines the payment due date.

## Handle status changes

### Cancel subscriptions

#### Accounts v2

To cancel a subscription, remove the third-party payment method details from the Stripe `Account` object and your database. Listen for the [customer.subscription.deleted](https://docs.stripe.com/api/events/types.md#event_types-customer.subscription.deleted) event and delete any tokens related to the canceled subscription.

#### Customers v1

To cancel a subscription, remove the third-party payment method details from the Stripe `Customer` object and your database. Listen for the [customer.subscription.deleted](https://docs.stripe.com/api/events/types.md#event_types-customer.subscription.deleted) event and delete any tokens related to the canceled subscription.

### Third-party payment cancellation (Third party)

Some third-party processors allow end customers to cancel billing agreements directly. If the processor allows this, listen for any associated events and then [cancel the subscription](https://docs.stripe.com/api/subscriptions/cancel.md) on Stripe.

### Refunds and disputes (Third party)

You’re responsible for processing refunds and disputes originating from the third-party processor. To maintain accurate accounting data, log refunds on issued invoices by using [Credit Notes](https://docs.stripe.com/api/credit_notes/object.md) to adjust the invoice amounts. Create a Credit Note, and set the [out_of_band_amount](https://docs.stripe.com/api/credit_notes/create.md#create_credit_note-out_of_band_amount) to the refunded amount.

## Other considerations

### Switch between third-party payments and Stripe

To switch a customer from a third-party processor to Stripe:

1. Collect a new payment method for the customer by [setting up future payments](https://docs.stripe.com/payments/save-and-reuse.md?platform=checkout) or using the [customer portal](https://docs.stripe.com/no-code/customer-portal.md).
1. Update the subscription [collection_method](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-collection_method) from `send_invoice` to `charge_automatically` and set the new payment method as the `default_payment_method`.
1. Delete any existing third-party payment method tokens.

### Retries

You must handle any recovery of failed third-party payments yourself. Stripe doesn’t have any visibility into the status of third-party payments until you mark an invoice as `paid`.

### Taxes

#### Accounts v2

Stripe Tax automatically adds the correct tax amounts to invoices as long as you set a billing postal code or IP address when [updating the `Account` object after checkout](https://docs.stripe.com/billing/subscriptions/third-party-payment-processing.md#update-customer).

#### Customers v1

Stripe Tax automatically adds the correct tax amounts to invoices as long as you set a billing postal code or IP address when [updating the `Customer` object after checkout](https://docs.stripe.com/billing/subscriptions/third-party-payment-processing.md#update-customer).

### Partial payments

We don’t support partial payments on `out_of_band` invoices. In the event of a partial payment, use a Credit Note to adjust the original invoice, and then manually generate a new invoice for any remaining balance.
