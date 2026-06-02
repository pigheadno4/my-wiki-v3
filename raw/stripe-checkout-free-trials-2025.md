<!-- Source: Stripe Checkout — Configure free trials -->
<!-- Fetched: 2026-04-20 -->

# Configure free trials

Delay payments on subscriptions using free trial periods.

You can set up free trials with Stripe Checkout. The maximum free trial length is 2 years (730 days), but most businesses use shorter trials, such as 30 days. Some issues that can affect longer trials include:

- Payment methods expiring before the first charge
- Lower conversion rates

# Hosted page

> This is a Hosted page for when payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/checkout/free-trials?payment-ui=stripe-hosted.

You can configure a Checkout Session to start a customer’s subscription with a free trial by passing one of the following parameters:

- [subscription_data.trial_period_days](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-trial_period_days), the length (in days) of your free trial.
- [subscription_data.trial_end](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-trial_end), a Unix timestamp representing the end of the trial period.

```node
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "subscription",
  success_url: "https://example.com/success",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  subscription_data: {
    trial_period_days: 30,
  },
});
```

## Free trials without collecting a payment method

By default, Checkout Sessions collect a payment method to use after the trial ends. You can sign customers up for free trials without collecting payment details by passing [payment_method_collection=if_required](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_collection).

Choose whether to cancel or pause the subscription if the customer doesn’t provide a payment method before the trial ends by passing [trial_settings.end_behavior.missing_payment_method](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-trial_settings-end_behavior-missing_payment_method).

- **Cancel subscription**-If the free trial subscription ends without a payment method, it cancels immediately. You can create another subscription if the customer decides to subscribe to a paid plan in the future.
- **Pause subscription**-If the free trial subscription ends without a payment method, it pauses and doesn’t cycle until it’s resumed. When a subscription is paused, it doesn’t generate invoices (unlike when a subscription’s [payment collection](https://docs.stripe.com/billing/subscriptions/pause-payment.md) is paused). When your customer adds their payment method after the subscription has paused, you can resume the same subscription. The subscription can remain paused indefinitely.

```node
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "subscription",
  success_url: "https://example.com/success",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  subscription_data: {
    trial_period_days: 30,
    trial_settings: {
      end_behavior: {
        missing_payment_method: "cancel",
      },
    },
  },
  payment_method_collection: "if_required",
});
```

### Collect payment details automatically

Before the trial expires, collect payment details from your customer.

Under **Manage free trial messaging** in your [Subscriptions and emails settings](https://dashboard.stripe.com/settings/billing/automatic), you can choose to automatically send a reminder email when a customer’s trial is about to expire.

Next, select the **Link to a Stripe-hosted page** option so the reminder email contains a link for the customer to add or update their payment details. We don’t send free trial reminder emails in a sandbox. Learn more about how to [set up free trial reminders](https://docs.stripe.com/billing/revenue-recovery/customer-emails.md#trial-ending-reminders).

You must comply with card network requirements when offering trials. Learn more about [compliance requirements for trials and promotions](https://docs.stripe.com/billing/subscriptions/trials/manage-trial-compliance.md).

### Collect payment details in the Billing customer portal

You can also send the reminder email yourself, and redirect customers to the Billing customer portal to add their payment details.

First, configure the [Billing customer portal](https://docs.stripe.com/customer-management.md) to enable your customers to manage their subscriptions.

Next, collect billing information from your customers:

1. Listen to the `customer.subscription.trial_will_end` [event](https://docs.stripe.com/api/events/types.md#event_types-customer.subscription.trial_will_end).
1. If the subscription doesn’t have a [default payment method](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-default_payment_method), get the customer’s email using the [Customers API](https://docs.stripe.com/api/customers/retrieve.md) and send them a message with a link to your site. It’s helpful to embed the customer ID in the email, for example `https://example.com?...&customer={{CUSTOMER_ID}}`.
1. When the customer lands on your site, create a customer portal session using the customer ID from the previous step.
1. [Redirect](https://docs.stripe.com/customer-management/integrate-customer-portal.md#redirect) the customer to the customer portal, where they can update their subscription with payment details.

Your customers can also [resume their paused subscription](https://docs.stripe.com/billing/subscriptions/trials/free-trials.md#resume-a-paused-subscription) in the customer portal by selecting **Start subscription**, then adding a payment method. View [free trial periods](https://docs.stripe.com/billing/subscriptions/trials/free-trials.md#create-free-trials-without-payment) to learn how to configure a subscription to pause or cancel when a free trial ends without a payment method attached.

# Embedded page

> This is a Embedded page for when payment-ui is embedded-form. View the full page at https://docs.stripe.com/payments/checkout/free-trials?payment-ui=embedded-form.

You can configure a Checkout Session to start a customer’s subscription with a free trial by passing one of the following parameters:

- [subscription_data.trial_period_days](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-trial_period_days), the length (in days) of your free trial.
- [subscription_data.trial_end](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-trial_end), a Unix timestamp representing the end of the trial period.

```node
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "subscription",
  ui_mode: "embedded_page",
  return_url: "https://example.com/return",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  subscription_data: {
    trial_period_days: 30,
  },
});
```

## Free trials without collecting a payment method

By default, Checkout Sessions collect a payment method to use after the trial ends. You can sign customers up for free trials without collecting payment details by passing [payment_method_collection=if_required](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_collection).

Choose whether to cancel or pause the subscription if the customer doesn’t provide a payment method before the trial ends by passing [trial_settings.end_behavior.missing_payment_method](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-trial_settings-end_behavior-missing_payment_method).

- **Cancel subscription**-If the free trial subscription ends without a payment method, it cancels immediately. You can create another subscription if the customer decides to subscribe to a paid plan in the future.
- **Pause subscription**-If the free trial subscription ends without a payment method, it pauses and doesn’t cycle until it’s resumed. When a subscription is paused, it doesn’t generate invoices (unlike when a subscription’s [payment collection](https://docs.stripe.com/billing/subscriptions/pause-payment.md) is paused). When your customer adds their payment method after the subscription has paused, you can resume the same subscription. The subscription can remain paused indefinitely.

```node
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "subscription",
  ui_mode: "embedded_page",
  return_url: "https://example.com/return",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  subscription_data: {
    trial_period_days: 30,
    trial_settings: {
      end_behavior: {
        missing_payment_method: "cancel",
      },
    },
  },
  payment_method_collection: "if_required",
});
```

### Collect payment details automatically

Before the trial expires, collect payment details from your customer.

Under **Manage free trial messaging** in your [Subscriptions and emails settings](https://dashboard.stripe.com/settings/billing/automatic), you can choose to automatically send a reminder email when a customer’s trial is about to expire.

Next, select the **Link to a Stripe-hosted page** option so the reminder email contains a link for the customer to add or update their payment details. We don’t send free trial reminder emails in a sandbox. Learn more about how to [set up free trial reminders](https://docs.stripe.com/billing/revenue-recovery/customer-emails.md#trial-ending-reminders).

You must comply with card network requirements when offering trials. Learn more about [compliance requirements for trials and promotions](https://docs.stripe.com/billing/subscriptions/trials/manage-trial-compliance.md).

### Collect payment details in the Billing customer portal

You can also send the reminder email yourself, and redirect customers to the Billing customer portal to add their payment details.

First, configure the [Billing customer portal](https://docs.stripe.com/customer-management.md) to enable your customers to manage their subscriptions.

Next, collect billing information from your customers:

1. Listen to the `customer.subscription.trial_will_end` [event](https://docs.stripe.com/api/events/types.md#event_types-customer.subscription.trial_will_end).
1. If the subscription doesn’t have a [default payment method](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-default_payment_method), get the customer’s email using the [Customers API](https://docs.stripe.com/api/customers/retrieve.md) and send them a message with a link to your site. It’s helpful to embed the customer ID in the email, for example `https://example.com?...&customer={{CUSTOMER_ID}}`.
1. When the customer lands on your site, create a customer portal session using the customer ID from the previous step.
1. [Redirect](https://docs.stripe.com/customer-management/integrate-customer-portal.md#redirect) the customer to the customer portal, where they can update their subscription with payment details.

Your customers can also [resume their paused subscription](https://docs.stripe.com/billing/subscriptions/trials/free-trials.md#resume-a-paused-subscription) in the customer portal by selecting **Start subscription**, then adding a payment method. View [free trial periods](https://docs.stripe.com/billing/subscriptions/trials/free-trials.md#create-free-trials-without-payment) to learn how to configure a subscription to pause or cancel when a free trial ends without a payment method attached.

## See also

- [Using trial periods on subscriptions](https://docs.stripe.com/billing/subscriptions/trials/free-trials.md)
- [Send an email reminder before the trial ends](https://docs.stripe.com/billing/subscriptions/trials/manage-trial-compliance.md#notify-customers-with-trial-end-reminder-emails)
- [Combine trials with usage-based billing](https://docs.stripe.com/billing/subscriptions/trials/free-trials.md#trials-usage-based-billing)
