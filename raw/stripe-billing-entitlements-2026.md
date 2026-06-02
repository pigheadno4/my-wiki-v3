<!-- Source URL: https://docs.stripe.com/billing/entitlements -->
<!-- Fetched: 2026-05-13 -->

# Entitlements

Determine when you can grant or revoke product feature access to customers.

Entitlements enable you to map the features of your internal service to Stripe products. After you map your features, Stripe notifies you about when to provision or de-provision access (according to your customer’s subscription status), and to what features, based on your mapping choices.

Use Entitlements to:

- Launch, change, and experiment with your pricing without needing to change your codebase
- Grant, revoke, and manage your customer’s feature access
- Simplify your billing integration
  ![](https://d37ugbyn3rpeym.cloudfront.net/videos/entitlements-demo.mp4)

## Before you begin

This guide assumes that you’re already using Stripe [Subscriptions](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md) and [Customer](https://docs.stripe.com/invoicing/customer.md) resources.

# Dashboard

> This is a Dashboard for when dashboard-or-api is dashboard. View the full page at https://docs.stripe.com/billing/entitlements?dashboard-or-api=dashboard.

## Get started

To get started with Entitlements:

- **Set up your features**: Create each feature in Stripe Billing from the Dashboard. Here are some examples of features you can include:
  - API access
  - AI assistant
  - Premium support
  - Advanced reporting
  - Extended data retention
- **Add your features to products**: Attach features to corresponding Stripe Products. You can add a single feature to multiple products.
- **Manage your features**: Edit or archive each feature from the Dashboard.

## Set up your features

To create a feature in the Dashboard, do the following:

1. In the Dashboard, go to the [Product catalog](https://dashboard.stripe.com/products) and click **Features**.
1. Click **+ Create feature** and enter a Name and a Lookup Key for the feature. You can optionally also add Metadata.
1. Because the Lookup Key is unique to each feature, you can’t reuse it across different features unless you archive the feature associated with the Lookup Key.
1. Click **Create feature**.

## Add your features to products

To add a feature to a product in the Dashboard, do the following:

1. In the Dashboard, from the [Features](https://dashboard.stripe.com/features) tab, click the feature that you want to add.
1. Click **Attach to product** and select a product from the menu.
1. Click **Confirm**.

When a customer subscribes to the product, you can view what features they’re entitled to. To do this, go to the [Customers](https://dashboard.stripe.com/customers) page, select the customer, and review the Entitlements section.

> Existing subscriptions will create active entitlements for any product feature changes at the start of the next billing period.

## Manage features

You can manage features from the Dashboard.

### Edit a feature

To edit a feature’s Name or add Metadata, go to the [Features](https://dashboard.stripe.com/features) tab, click the overflow menu (⋯), and click **Edit feature**. You can’t edit a feature’s Lookup Key after the feature is created.

### Remove a feature from a product

To remove a feature from a product, go to the [Features](https://dashboard.stripe.com/features) tab and select the feature. Then click the overflow menu (⋯) next to the product name and click **Remove product**.

### Archive a feature

To archive a feature, go to the [Features](https://dashboard.stripe.com/features) tab, click the overflow menu (⋯), and click **Archive feature**.

Before you archive a feature, keep in mind the following:

- Archived features can’t be edited or added to any new products.
- Archived features still create entitlements if attached to existing products.
- An archived feature’s lookup key can be used again.
- You can’t unarchive a feature.

# API

> This is a API for when dashboard-or-api is api. View the full page at https://docs.stripe.com/billing/entitlements?dashboard-or-api=api.

## Get started

To get started with Entitlements:

- **Set up your features**: Create each feature in Stripe Billing using the [Feature API](https://docs.stripe.com/api/entitlements/feature/object.md). Here are some examples of features you can include:
  - API access
  - AI assistant
  - Premium support
  - Advanced reporting
  - Extended data retention
- **Add your features to products**: Attach Features to corresponding Stripe Products. You can add a single feature to multiple products.
- **Get customers’ active entitlements**: When customers subscribe to your products, Stripe Billing entitles the customer to the product’s features. Listen to the [Active Entitlement Summary webhook](https://docs.stripe.com/billing/entitlements.md#webhooks) and use the [List Active Entitlements API](https://docs.stripe.com/api/entitlements/active-entitlement/list.md) for a given customer to execute your feature provisioning process.
  ![Diagram with Entitlements and its relationship with a Customer and Product's features](assets/stripe-entitlements-diagram.png)

## Set up your features

Provide a name and a unique `lookup_key` for each feature you create. Because the `lookup_key` is unique to each feature, you can’t reuse it across different features.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const feature = await stripe.entitlements.features.create({
  name: "My feature",
  lookup_key: "myinternalfeaturecode",
});
```

## Add your features to products

Assign your feature to one or more products.

> Existing subscriptions will create active entitlements for any product feature changes at the start of the next billing period.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const productFeature = await stripe.products.createFeature("{{PRODUCT_ID}}", {
  entitlement_feature: "{{ENTITLEMENTSFEATURE_ID}}",
});
```

After you submit a request to attach your feature to your product, you receive a response similar to the following:

```json
{
  "id": "{{PRODUCT_FEATURE_ID}}",
  "object": "product_feature",
  "entitlement_feature": {
    "id": "{{ENTITLEMENTS_FEATURE_ID}}",
    "object": "entitlements.feature",
    "name": "My feature",
    "lookup_key": "myinternalfeaturecode"
  }
}
```

List the features attached to a product by paging through the list of product features:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const productFeatures = await stripe.products.listFeatures("{{PRODUCT_ID}}");
```

And remove a feature from a specific product by deleting the product feature attachment:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const deleted = await stripe.products.deleteFeature(
  "{{PRODUCT_ID}}",
  "{{PRODUCTFEATURE_ID}}",
);
```

## Get customers' active entitlements

During the lifecycle of a customer’s subscription, from activation, through upgrades, downgrades, and so on, Stripe updates the customer’s entitlements based on your mapped features.

When a customer’s subscription is first activated, Stripe creates entitlements for the features that they’re subscribed to.

As long as a customer maintains an active subscription for a feature, they retain an active entitlement. Make sure you provision access in your system for any users entitled to this feature.

### Listen for webhooks to grant or revoke access

When a customer’s entitlements change because they subscribe to a product, upgrade, downgrade, or cancel, Stripe fires the `entitlements.active_entitlement_summary.updated` webhook. Use this event to drive access provisioning in your own system.

**Grant access**: When a customer purchases a subscription that includes a product with attached features, Stripe fires `entitlements.active_entitlement_summary.updated`. The event payload contains the customer’s full, up-to-date entitlement summary. Your application should enable whichever features or services correspond to the features listed under `entitlements.data`.

**Revoke access**: When a customer cancels their subscription or their subscription is canceled automatically due to failed payments, Stripe fires `entitlements.active_entitlement_summary.updated` again. At this point, the revoked features no longer appear in `entitlements.data`. Your application needs to disable the associated features or services accordingly.

> #### Limited entitlements available in summary webhook
>
> The entitlement summary’s `entitlements.data` array contains a maximum of 10 entitlements. If a customer has more than 10 active entitlements, use the `entitlements.url` field in the payload to fetch the complete, paginated list.

| Event                                             | Description                                                                                                                 |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `entitlements.active_entitlement_summary.updated` | Occurs each time a customer’s active entitlements change, for example when a subscription is created, updated, or canceled. |

The `data.object` in the webhook payload is an `entitlements.active_entitlement_summary` object. Here is an example payload for a customer who has just subscribed to a product with two features:

```json
{
  "id": "evt_1OcCWTLkdIwHu7ixbUwdUFui",
  "object": "event",
  "created": 1706111369,
  "data": {
    "object": {
      "object": "entitlements.active_entitlement_summary",
      "customer": "cus_ABC123customer",
      "entitlements": {
        "object": "list",
        "data": [
          {
            "id": "ent_test_61QG5x2cU1GluFTYs41JqiESbLiX8C8O",
            "object": "entitlements.active_entitlement",
            "feature": "feat_test_61QGU1MWyFMSP9YBZ41ClCIKljWvsTgu",
            "livemode": false,
            "lookup_key": "premium-support"
          },
          {
            "id": "ent_test_72RH6y3dV2HmvGUZt52KrjFTcMjY9D9P",
            "object": "entitlements.active_entitlement",
            "feature": "feat_test_72RHV2NXzGNTP0ZCA52DmDJLkmXwtUhv",
            "livemode": false,
            "lookup_key": "advanced-reporting"
          }
        ],
        "has_more": false,
        "url": "/v1/customer/cus_ABC123customer/entitlements"
      },
      "livemode": false
    },
    "previous_attributes": {
      "entitlements": {
        "data": []
      }
    }
  },
  "livemode": false,
  "pending_webhooks": 0,
  "request": {
    "id": null,
    "idempotency_key": null
  },
  "type": "entitlements.active_entitlement_summary.updated"
}
```

When a customer’s subscription is canceled and a feature is revoked, Stripe fires the same event but `entitlements.data` no longer contains the revoked feature:

```json
{
  "id": "evt_1OcDYTLkdIwHu7ixcVxeVGvj",
  "object": "event",
  "created": 1706115012,
  "data": {
    "object": {
      "object": "entitlements.active_entitlement_summary",
      "customer": "cus_ABC123customer",
      "entitlements": {
        "object": "list",
        "data": [],
        "has_more": false,
        "url": "/v1/customer/cus_ABC123customer/entitlements"
      },
      "livemode": false
    },
    "previous_attributes": {
      "entitlements": {
        "data": [
          {
            "id": "ent_test_61QG5x2cU1GluFTYs41JqiESbLiX8C8O",
            "object": "entitlements.active_entitlement",
            "feature": "feat_test_61QGU1MWyFMSP9YBZ41ClCIKljWvsTgu",
            "livemode": false,
            "lookup_key": "premium-support"
          },
          {
            "id": "ent_test_72RH6y3dV2HmvGUZt52KrjFTcMjY9D9P",
            "object": "entitlements.active_entitlement",
            "feature": "feat_test_72RHV2NXzGNTP0ZCA52DmDJLkmXwtUhv",
            "livemode": false,
            "lookup_key": "advanced-reporting"
          }
        ]
      }
    }
  },
  "livemode": false,
  "pending_webhooks": 0,
  "request": {
    "id": null,
    "idempotency_key": null
  },
  "type": "entitlements.active_entitlement_summary.updated"
}
```

### Retrieve the list of all active entitlements for a customer

If your application needs to check a customer’s current entitlements at any time without waiting for a webhook, you can retrieve them directly using [List Active Entitlements](https://docs.stripe.com/api/entitlements/active-entitlement/list.md). This is useful on application startup, for authorization checks, or to reconcile state after a webhook delivery failure.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const activeEntitlements = await stripe.entitlements.activeEntitlements.list({
  customer: "{{CUSTOMER_ID}}",
});
```

The response returns a paginated list of `entitlements.active_entitlement` objects for the specified customer. Each object includes the `lookup_key` you defined when creating the feature, which you can use to gate access in your application. For example, if a customer has an active subscription to a product with features `premium-support` and `advanced-reporting`, the response looks like:

```json
{
  "object": "list",
  "url": "/v1/entitlements/active_entitlements",
  "has_more": false,
  "data": [
    {
      "id": "ent_test_61QG5x2cU1GluFTYs41JqiESbLiX8C8O",
      "object": "entitlements.active_entitlement",
      "feature": "feat_test_61QGU1MWyFMSP9YBZ41ClCIKljWvsTgu",
      "lookup_key": "premium-support",
      "livemode": false
    },
    {
      "id": "ent_test_72RH6y3dV2HmvGUZt52KrjFTcMjY9D9P",
      "object": "entitlements.active_entitlement",
      "feature": "feat_test_72RHV2NXzGNTP0ZCA52DmDJLkmXwtUhv",
      "lookup_key": "advanced-reporting",
      "livemode": false
    }
  ]
}
```

If the customer has no active entitlements (for example, their subscription has been canceled), the `data` array is empty.

> #### Recommendation
>
> We recommend you persist these entitlements internally for faster resolution.

> Subscription pricing, plan, and entitlement changes might be subject to certain legal requirements. Consult with your legal counsel for advice specific to your business.
