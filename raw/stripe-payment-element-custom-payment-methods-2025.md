<!-- Source URL: https://docs.stripe.com/payments/payment-element/custom-payment-methods -->
<!-- Fetched: 2026-04-21 -->

# Add custom payment methods

Learn how to add custom payment methods to the Payment Element.

# Checkout Sessions API

> This is a Checkout Sessions API for when payment-ui is embedded-components. View the full page at https://docs.stripe.com/payments/payment-element/custom-payment-methods?payment-ui=embedded-components.

Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) with [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions.md) to enable merchant-instructed payments.

# Payment Intents API

> This is a Payment Intents API for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/payment-element/custom-payment-methods?payment-ui=elements.

Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) with the Payment Intents API to display over 50 preset [payment methods](https://docs.stripe.com/payments/payment-methods/payment-method-support.md), as well as your custom payment methods, through a single integration. After creating your custom payment method in the Dashboard, configure the Payment Element to make sure these transactions process and finalize correctly outside of Stripe. You can record these transactions to your Stripe account for reporting purposes.

> When integrating with a third-party payment processor, you’re responsible for complying with [applicable legal requirements](https://docs.stripe.com/payments/payment-methods/custom-payment-methods.md#compliance), including your agreement with your PSP, applicable laws, and so on.

## Before you begin

1. [Create a Stripe account](https://dashboard.stripe.com/register) or [sign in](https://dashboard.stripe.com/login) with your existing account.
1. Follow [this guide](https://docs.stripe.com/payments/accept-a-payment-deferred.md) to complete a payments integration.

## Create your custom payment method [Dashboard]

You can create a custom payment method in the Dashboard by going to **Settings** > **Payments** > [Custom Payment Methods](https://dashboard.stripe.com/settings/custom_payment_methods). Provide the name and logo for the Payment Element to display.

#### Choose the right logo

- For logos with a transparent background, consider the background color of the Payment Element on your page and make sure that it stands out.
- For logos with a background fill, include rounded corners in your file, if needed.
- Choose a logo variant that can scale down to 16x16 pixels. This is often the standalone logo mark for a brand.

After creating the custom payment method, the Dashboard displays the custom payment method ID (beginning with `cpmt_`) that you need for the next step.

## Add the custom payment method type [Client-side]

Next, add the custom payment method type to your Stripe Elements configuration. In your `checkout.js` file where you initialize Stripe Elements, specify the [customPaymentMethods](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-customPaymentMethods) to add to the Payment Element. Provide the custom payment method ID from the previous step, the `options.type`, and an optional subtitle.

```javascript
const elements = stripe.elements({
  // ...
  customPaymentMethods: [
    {
      id: "{{CUSTOM_PAYMENT_METHOD_TYPE_ID}}", // Identifier of the custom payment method type created in the Dashboard.
      options: {
        type: "static",
        subtitle: "Optional subtitle",
      },
    },
  ],
});
```

After loading, the Payment Element shows your custom payment method.
![Stripe Payment Element showing a custom payment method called PM Name.](assets/stripe-payment-element-custom-pm-static.png)

## Optional: Display embedded custom content (Preview) [Client-side]

Use the `embedded` type to display the content for your custom payment method in the Payment Element.
![Stripe Payment Element showing a custom payment method called PM Name, with custom content overlayed in the form container.](assets/stripe-payment-element-custom-pm-embedded.png)

Manage your custom content using these callbacks:

- [handleRender](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-customPaymentMethods-options-embedded-handleRender): Called when a payment method is selected, and contains a reference to a container DOM node that you can render your content in.
- [handleDestroy](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-customPaymentMethods-options-embedded-handleDestroy): Called when a payment method is deselected and the Payment Element is unmounted. Performs cleanup, such as removing event listeners or a custom SDK.

> Only render trusted content within the `container` that’s provided by `handleEmbed`. Rendering markup that you don’t control, especially from a user or an unsanitized source, can introduce a [cross-site scripting vulnerability (XSS)](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting).

```javascript
const elements = stripe.elements({
  // ...
  customPaymentMethods: [
    {
      id: '{{CUSTOM_PAYMENT_METHOD_TYPE_ID}}',
      options: {type: 'embedded',
        subtitle: 'Embedded payment method',
        embedded: {
          handleRender: (container) => {
            // Render markup in the embedded content container
            // using the templating system or JavaScript framework
            // of your choice
          }
          handleDestroy: () => {
            // Handle any needed cleanup, like removing SDKs
            // or event listeners
          }
        }
      }
    }
  ]
});
```

Tools like [React Portals](https://react.dev/reference/react-dom/createPortal) allow you to integrate your rendering logic with your application code:

```javascript
import { Elements } from "@stripe/react-stripe-js";
import { loadStripe } from "@stripe/stripe-js";

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

export default function App() {
  const [embedContainer, setEmbedContainer] = useState();

  const options = {
    customPaymentMethods: [
      {
        id: "{{CUSTOM_PAYMENT_METHOD_TYPE_ID}}",
        options: {
          type: "embedded",
          subtitle: "Embedded payment method",
          embedded: {
            handleRender: (container) => {
              setEmbedContainer(container);
            },
            handleDestroy: () => {
              setEmbedContainer(null);
            },
          },
        },
      },
    ],
  };

  return (
    <Elements stripe={stripePromise} options={options}>
      <CheckoutFormWithPaymentElement />
      {embedContainer && createPortal(<EmbeddedCpmContent />, embedContainer)}
    </Elements>
  );
}
```

## Handle payment method submission [Client-side]

To process custom payment method transactions outside of Stripe, update the `handleSubmit` function that’s called when users click the pay button on your website.

The [elements.submit()](https://docs.stripe.com/js/elements/submit) function retrieves the selected payment method type. For example, you might show a modal, and then either process the payment on your own server or redirect your customer to an external payment page.

```javascript

async function handleSubmit(e) {const { submitError, selectedPaymentMethod } = await elements.submit();

  if (selectedPaymentMethod === '{{CUSTOM_PAYMENT_METHOD_TYPE_ID}}') { // Identifier of the custom payment method type created in the Dashboard.
    // Process CPM payment on merchant server and handle redirect
    const res = await fetch("/process-cpm-payment", { method: 'post' });
    ...
  } else {
    // Process Stripe payment methods
    ...
  }
}

```

## Optional: Specify the order of custom payment methods [Client-side]

By default, the Payment Element shows custom payment methods last. To manually specify the order of payment methods, set the [paymentMethodOrder](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-paymentMethodOrder) property on the options configuration when creating your Payment Element instance.

```javascript

const paymentElement = elements.create('payment', {
  // an array of payment method types, including custom payment method types
  paymentMethodOrder: [...]
});

```

## Optional: Record the payment to your Stripe account [Server-side]

While you handle custom payment method transactions outside of Stripe, you can still [record the transaction details](https://docs.stripe.com/api/payment-record/report.md) to your Stripe account. This can help with unified reporting and building back-office workflows, such as issuing receipts or creating reports.

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = new Stripe('<<YOUR_SECRET_KEY>>', {
  apiVersion: '2026-03-25.dahlia; invoice_partial_payments_beta=v3'
});

app.get('/process-cpm-payment', async (req, res) => {
  const paymentResult = processMyCustomPayment(...)

  // Create an instance of a custom payment method
  const paymentMethod = await stripe.paymentMethods.create({
    type: 'custom',
    custom: {
      type: '{{CUSTOM_PAYMENT_METHOD_TYPE_ID}}', // Identifier of the custom payment method type created in the Dashboard.
    }
  });

  // Report successful payment
  const paymentRecord = await stripe.paymentRecords.reportPayment({
    amount_requested: {
      value: paymentResult.amount,
      currency: paymentResult.currency
    },
    payment_method_details: {
      payment_method: paymentMethod.id
    },
    customer_details: {
      customer: paymentResult.customer.id
    },
    processor_details: {
      type: 'custom',
      custom: {
        payment_reference: paymentResult.id
      }
    },
    initiated_at: paymentResult.initiated_at,
    customer_presence: 'on_session',
    outcome: 'guaranteed',
    guaranteed: {
      guaranteed_at: paymentResult.completed_at
    }
  });

  // Respond to frontend to finish buying experience
  return res.json(...)
});
```
