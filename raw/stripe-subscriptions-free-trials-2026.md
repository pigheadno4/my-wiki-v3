<!-- Source URL: https://docs.stripe.com/billing/subscriptions/trials/free-trials -->
<!-- Fetched: 2026-05-12 -->

# Use free trial periods on subscriptions

Offer free trial periods on subscriptions using the legacy trial_end parameter.

> #### Legacy
>
> The content below describes a _Legacy_ (Technology that's no longer recommended) integration path for offering free trials.
>
> If you’re building a new integration, we recommend that you [Configure trial offers on subscriptions](https://docs.stripe.com/billing/subscriptions/trials.md).

You can start a customer’s _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) with a free trial period by providing a `trial_end` argument when [creating the subscription](https://docs.stripe.com/api.md#create_subscription):

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
  trial_end: 1610403705,
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
  trial_end: 1610403705,
});
```

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

The `trial_end` parameter takes a timestamp indicating the exact moment the trial ends. When creating a subscription, you can alternatively use the [trial_period_days](https://docs.stripe.com/api.md#create_subscription-trial_period_days) parameter: an integer representing the number of days the trial lasts, from the current moment. The trial period must be 730 days (2 years) or less. Trial periods are normally applied at the start of a subscription, but you can also use a trial period on an existing subscription to [change the subscription’s billing period (cycle)](https://docs.stripe.com/billing/subscriptions/billing-cycle.md).

When creating a subscription with a trial period, you don’t need to add a payment method. An immediate _invoice_ (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) is still created, but the amount is 0 and the [Invoice Line descriptions](https://docs.stripe.com/api/invoices/object.md#invoice_object-lines-data-description) include “Free trial” verbiage.

When the trial ends, if the subscription `status` isn’t `paused`, we generate an invoice and send an `invoice.created` event notification. Approximately 1 hour later, we attempt to charge that invoice. A new billing period also begins for the customer when the trial ends.

To end a trial early, make an [update subscription](https://docs.stripe.com/api.md#update_subscription) API call, setting the `trial_end` value to a new timestamp, or **now** to end immediately:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.update("{{SUBSCRIPTION_ID}}", {
  trial_end: "now",
});
```

## Trials with usage-based billing

You can use trial periods for subscriptions with usage-based billing. Stripe doesn’t bill for usage recorded during the trial period, but you can view the usage in the [meter event summary](https://docs.stripe.com/api/billing/meter-event-summary.md) for the trial period. After the trial period ends, billing resumes for recorded usage.

Make sure your integration properly monitors and handles [webhook events](https://docs.stripe.com/billing/subscriptions/webhooks.md) related to trial status changes. A few days before a trial ends and the subscription moves from `trialing` to `active`, you receive a `customer.subscription.trial_will_end` event. When you receive this event, make sure you have a payment method on the customer account to bill them. Optionally, provide advance notification to the customer about the upcoming charge.

### Usage-based billing with paused subscriptions

You can send [meter events](https://docs.stripe.com/api/billing/meter-event.md) associated with a price on a subscription even while it’s paused, but that usage isn’t invoiced. Future invoices only include meter events that occur after the resume date. If you use [legacy usage records](https://docs.stripe.com/billing/subscriptions/usage-based-legacy.md), you can’t create new usage records while a subscription is paused.

## Adding a new trial to a subscription previously in a trial

You can add a new trial on a non-trialing subscription by updating the subscription while specifying [`trial_end`](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-trial_end) or updating its associated subscription schedule. You need to specify [`phases.trial_end`](https://docs.stripe.com/api/subscription_schedules/create.md?#create_subscription_schedule-phases-trial_end) for subscriptions.

For most subscriptions that enter a new trial after a previous trial ends, the `trial_start` field remains set to the start of the first trial. As of [API version 2025-04-30](https://docs.stripe.com/changelog/basil.md#2025-04-30.preview), for subscriptions with [billing_mode](https://docs.stripe.com/api/subscription_schedules/create.md#create_subscription_schedule-billing_mode) set to `flexible`, `trial_start` reflects the beginning of the most recent trial.

## Update a subscription in a trial

You can update subscriptions in a trial normally. Adding items to a `billing_mode=flexible` or `billing_mode=classic` subscription in a trial generates an invoice for those items with an amount of 0. For `billing_mode=classic`, the 0-amount invoice might include items that were previously invoiced.

## Combining trials with add_invoice_items

You can combine trial periods for subscriptions with one time prices and `add_invoice_items`. This is useful when you want to charge a one-time fee or add-on at the same time you start a trial. When you do this, Stripe automatically generates an invoice for the one-time charge, even though the trial hasn’t ended yet. The customer pays the one-time amount upfront, while the recurring subscription billing begins after the trial period ends.

## Create free trials without collecting payment method

> While starting a free trial without a payment method lets your potential customers try your product or service faster, it can also allow spammers to create lots of fake customers, usage, and subscriptions. We recommend carefully considering the signup flow here to balance making it easy for real customers and difficult for spam bots to abuse (for example, requiring customers to create a user account and complete a captcha before starting their free trial subscription).

You can sign customers up for a free trial of a subscription without collecting their payment details in the Dashboard, the API, and Checkout. When you create the subscription, you can specify whether to cancel or pause the subscription if the customer didn’t provide a payment method during the trial period. To cancel or pause the subscription, set the `trial_settings.end_behavior.missing_payment_method` parameter when you create or update the subscription:

- **Cancel subscription**-If the free trial subscription ends without a payment method, it cancels immediately. You can create another subscription if the customer decides to subscribe to a paid plan in the future. Set `missing_payment_method=cancel` to cancel the subscription when it reaches the end of a trial without an available payment method.
- **Pause subscription**-If the free trial subscription ends without a payment method, it pauses and doesn’t cycle until it’s resumed. When a subscription is paused, it doesn’t generate invoices (unlike when a subscription’s [payment collection](https://docs.stripe.com/billing/subscriptions/pause-payment.md) is paused). When your customer adds their payment method after the subscription has paused, you can resume the same subscription. The subscription can remain paused indefinitely. Set `missing_payment_method=pause` to pause the subscription when it reaches the end of a trial without an available payment method.

Alternatively, set `missing_payment_method=create_invoice` to invoice at the end of the trial if no payment method is present. If a payment method isn’t provided when the invoice finalizes, the subscription moves into `past_due`.

Configure reminder emails to collect customer payment details in your [free trial messaging settings](https://dashboard.stripe.com/settings/billing/automatic).

### Configure free trials without payment methods to cancel

Use the Dashboard, the API, or Checkout to create free trials of a subscription without collecting payment details from your customers, and to configure your subscription to cancel if the trial ends without a payment method.

#### Dashboard

Use the Dashboard to sign customers up for a free trial of a subscription without collecting their payment details:

1. On the [Subscriptions](https://dashboard.stripe.com/subscriptions) page in the Dashboard, select **+Create subscription**.
1. After adding your customer, product, and service period information, expand **Subscription options**.
1. Click **Trial period** to give the customer free access to this subscription. Set the trial end date.
1. Under **When trial ends without a payment method…**, click **Cancel subscription**. If you’re using [test clocks](https://docs.stripe.com/billing/testing/test-clocks.md), advance to the end of the trial. You won’t see an upcoming invoice for the subscription.
1. Listen to the `customer.subscription.deleted` event that informs you when a subscription cancels at the end of a trial without a payment method.

#### API

Use the following API calls to sign up customers for a free trial of a subscription without collecting their payment details. If no payment method is provided at the end of the trial, the subscription cancels.

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
  trial_period_days: 30,
  payment_settings: {
    save_default_payment_method: "on_subscription",
  },
  trial_settings: {
    end_behavior: {
      missing_payment_method: "cancel",
    },
  },
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
  trial_period_days: 30,
  payment_settings: {
    save_default_payment_method: "on_subscription",
  },
  trial_settings: {
    end_behavior: {
      missing_payment_method: "cancel",
    },
  },
});
```

To update existing subscriptions, use the following API call:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.update("{{SUBSCRIPTION_ID}}", {
  trial_settings: {
    end_behavior: {
      missing_payment_method: "cancel",
    },
  },
});
```

#### Checkout

You can use Stripe Checkout to sign customers up for a free trial of a subscription without collecting their payment details.

Create a Checkout Session with the following:

- A `subscription_data` dictionary with:
  - The `trial_period_days` field set to the length (in days) of your free trial. In this example, the trial period is 30 days.
  - The `trial_settings[end_behavior]` parameter set to `cancel` to make sure that the subscription cancels if the free trial ends without a payment method attached.
- The `payment_method_collection` field with a value of `if_required`. This tells Stripe that collecting payment information at checkout is optional.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "subscription",
  line_items: [
    {
      price: "price_abc",
      quantity: 1,
    },
  ],
  subscription_data: {
    trial_settings: {
      end_behavior: {
        missing_payment_method: "cancel",
      },
    },
    trial_period_days: 30,
  },
  payment_method_collection: "if_required",
  success_url: "https://example.com/success",
});
```

If you set the `trial_settings.end_behavior.missing_payment_method=cancel` field on the subscription or set the subscription in the `subscription_data` field when creating a Checkout session, the subscription cancels if a payment method isn’t provided before the trial ends.

### Configure free trials without payment methods to pause

Use the Dashboard, the API, or Checkout to create free trials of a subscription without collecting payment details from your customers, and to configure your subscription to pause if the trial ends without a payment method.

#### Dashboard

You can use the Dashboard to sign customers up for a free trial of a subscription without collecting their payment details:

1. On the [Subscriptions](https://dashboard.stripe.com/subscriptions) page in the Dashboard, select **+Create subscription**.
1. After adding your customer, product, and service period information, expand **Subscription options**.
1. Click **Trial period** to give the customer free access to this subscription. Set the trial end date.
1. Under **When trial ends without a payment method…**, click **Cancel subscription**. If you’re using [test clocks](https://docs.stripe.com/billing/testing/test-clocks.md), advance to the end of the trial. You won’t see an upcoming invoice for the subscription.
1. Listen to the `customer.subscription.paused` event that informs you when a subscription pauses at the end of trials without a payment method.

#### API

Use the following API calls to sign up customers for a free trial of a subscription without collecting their payment details. If no payment method is provided at the end of the trial, the subscription pauses.

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
  trial_period_days: 30,
  payment_settings: {
    save_default_payment_method: "on_subscription",
  },
  trial_settings: {
    end_behavior: {
      missing_payment_method: "pause",
    },
  },
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
  trial_period_days: 30,
  payment_settings: {
    save_default_payment_method: "on_subscription",
  },
  trial_settings: {
    end_behavior: {
      missing_payment_method: "pause",
    },
  },
});
```

To update existing subscriptions, use the following API call:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.update("{{SUBSCRIPTION_ID}}", {
  trial_settings: {
    end_behavior: {
      missing_payment_method: "pause",
    },
  },
});
```

#### Checkout

You can use Stripe Checkout to sign customers up for a free trial of a subscription without collecting their payment details.

Create a Checkout Session with the following:

- A `subscription_data` dictionary with:
  - The `trial_period_days` field set to the length (in days) of your free trial. In this example, the trial period is 30 days.
  - The `trial_settings[end_behavior]` parameter set to `pause` to make sure that the subscription pauses if the free trial ends without a payment method attached.
- The `payment_method_collection` field with a value of `if_required`. This tells Stripe that collecting payment information at checkout is optional.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "subscription",
  line_items: [
    {
      price: "price_abc",
      quantity: 1,
    },
  ],
  subscription_data: {
    trial_settings: {
      end_behavior: {
        missing_payment_method: "pause",
      },
    },
    trial_period_days: 30,
  },
  payment_method_collection: "if_required",
  success_url: "https://example.com/success",
});
```

If you set the `trial_settings.end_behavior.missing_payment_method=pause` field on the subscription or set the subscription in the `subscription_data` field when creating a Checkout session, the subscription pauses if you don’t add a payment method before the trial ends.

### Collect payment details from your customer before their trial ends

Configure your subscription to automatically send a reminder email when the customer’s trial is about to expire. You must comply with the card network requirements when offering trials. Learn more about [compliance requirements for trials and promotions](https://docs.stripe.com/billing/subscriptions/trials/manage-trial-compliance.md).

### Use the customer portal to collect payment

After you create a subscription for a customer without collecting a payment method, you can redirect them to the Billing customer portal to add their payment details.

First, configure the [Billing customer portal](https://docs.stripe.com/customer-management.md) to enable your customers to manage their subscriptions.

Next, collect billing information from your customers:

1. Listen to the [`customer.subscription.trial_will_end` event](https://docs.stripe.com/api/events/types.md#event_types-customer.subscription.trial_will_end).
1. If the subscription doesn’t have a [default payment method](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-default_payment_method), get the customer’s email from the associated customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/retrieve.md) or [Customer](https://docs.stripe.com/api/customers/retrieve.md). Send the customer a message with a link to your site. Embed the customer ID in the email, for example **https://example.com?..&customer={{CUSTOMER\_ID}}**.
1. When the customer enters your site, create a customer portal session using the customer ID from the previous step.
1. Redirect the customer to the customer portal, where they can update their subscription with payment details.

### Allow customers to reactivate their subscriptions in the customer portal

To enable the subscription of a customer whose trial ended in a `paused` subscription through the customer portal, enable the free trial without payment method feature when creating a new subscription in the Dashboard.

### Convert a trial if customers provide payment information before the trial ends

Subscriptions and upcoming invoices are created at the start of the trial and become active at the end of the trial if the customer provides a payment method.

### Configure pausing when a payment method isn’t provided

After a free trial ends, you can configure subscriptions to pause if no default payment method is available for a subscription on a per-subscription basis.

You can update subscriptions while they’re paused. Updates that typically generate prorations (adding items, changing price or plan, changing quantity, and so on) won’t generate proration line items because the customer isn’t being charged while the subscription is paused. If you want to extend a trial after a subscription transitions into a `paused` status, you must resume the subscription before configuring a trial.

We check `default_source` and `default_payment_method` on the subscription and customer to determine whether a subscription is missing a payment method at the end of a trial.

### Resume a paused subscription

Use the Dashboard, API, customer portal, or Hosted Invoice Page to resume a paused subscription.

#### Dashboard

To resume a paused subscription in the Dashboard:

1. Go to the subscription, click the overflow menu (⋯), and select **Resume Subscription**.
1. Click the overflow menu (⋯), and select **Update Subscription**.
1. Expand the **Billing and payment collection** section, and click **Bill today instead** to charge the customer immediately.

#### API

When a paused subscription resumes, resumption of the subscription begins immediately. The `resume` endpoint enables you to resume a subscription and optionally change the `billing_cycle_anchor` date or create prorations.

For a `billing_cycle_anchor` value of `unchanged`, we create a debit proration for the partial period between `proration_date` (the default is `now`) and the end of the current billing period (unless `proration_behavior=none`). This also creates an invoice for the current period if `proration_behavior=always_invoice`.

Use the `resume` endpoint to resume a paused subscription. A payment method doesn’t need to be supplied on the subscription before you can resume (for example, if you want to generate or view the invoice before a customer provides payment), but the invoice needs to be paid before the subscription is reactivated. The invoice becomes automatically void after 23 hours if the associated payment intent doesn’t have a payment method attached and isn’t confirmed.

When you reactivate a subscription, the `items.current_period_start` and `items.current_period_end` timestamps advance to surround the current time. If `billing_cycle_anchor=now`, then `items.current_period_start == now`, which starts a new cycle, similar to converting after the trial ends.

#### Customer portal

Use the [customer portal to collect payment](https://docs.stripe.com/billing/subscriptions/trials/free-trials.md#use-the-customer-portal-to-collect-payment), then [redirect](https://docs.stripe.com/customer-management/integrate-customer-portal.md#redirect) the customer to the customer portal. The customer can select **Start subscription**, then add a payment method to resume their subscription.

#### Hosted Invoice Page

To resume a paused subscription in the [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page.md), provide a payment method, then select **Authorize and pay**.

### Invoicing a subscription

While paused, a subscription won’t create an invoice. If you want to continue creating invoices, use `pause_collection` to stop collecting payments while continuing to invoice and advance billing periods.

To preview the invoice that’s generated when a paused subscription is resumed, specify [subscription_details.resume_at](https://docs.stripe.com/api/invoices/create_preview.md#create_create_preview-subscription_details-resume_at).

## Combine trials with a specific billing cycle anchor

You can combine trials with `billing_cycle_anchor`, resulting in a free period followed by a prorated period, leading into a fixed billing period. This capability is available through the API.

For example, if you give a customer a 7 day free trial starting on July 15 and want to start normal billing on August 1:

- On July 15, you give the customer a 7 day free trial (until July 22).
- The customer gets an invoice for a prorated amount on July 22, for the period until August 1.
- The customer is billed for the full amount on August 1, then on September 1, and so on.

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
  trial_end: 1753170047,
  billing_cycle_anchor: 1627801200,
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
  trial_end: 1753170047,
  billing_cycle_anchor: 1627801200,
});
```

You can also use `trial_end` to change the billing period for an existing subscription. To learn more, see [Change the billing period on existing subscriptions](https://docs.stripe.com/billing/subscriptions/billing-cycle.md#changing).

## See also

- [Products and prices](https://docs.stripe.com/products-prices/overview.md)
- [Prices](https://docs.stripe.com/api.md#prices)
- [Subscriptions](https://docs.stripe.com/api.md#subscriptions)
- [Managing subscription billing periods](https://docs.stripe.com/billing/subscriptions/billing-cycle.md)
