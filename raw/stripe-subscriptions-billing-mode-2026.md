<!-- Source URL: https://docs.stripe.com/billing/subscriptions/billing-mode -->
<!-- Fetched: 2026-05-13 -->

# Enable increased flexibility for subscriptions

Use flexible billing mode for enhanced functionality and to access additional features.

You can set your preferred [billing mode](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-billing_mode) to orchestrate your invoices and subscriptions to meet your business requirements. You can configure each subscription to use one of two billing modes:

- **Flexible** (Recommended): Provides accurate and predictable billing behavior and new capabilities. To access these improvements, which are only available in flexible billing mode, you must create new subscriptions with flexible billing mode or migrate your existing subscriptions.
- **Classic**: Uses the existing Stripe subscription behavior. This setting is maintained for backward compatibility with older integrations.

You can [learn more](https://docs.stripe.com/billing/subscriptions/billing-mode/compare.md) about the detailed differences between classic and flexible billing mode and how to choose the billing mode that works best for you.

> You can’t migrate a subscription from flexible billing mode to classic billing mode.

## Why flexible billing mode

Flexible billing mode provides more accurate billing for prorations, usage-based pricing, flexible invoicing, and trial settings. It also unlocks new capabilities such as [mixed intervals on the same subscription](https://docs.stripe.com/billing/subscriptions/mixed-interval.md). These improvements are only available in flexible billing mode, which is why we recommend creating new subscriptions with flexible billing mode and [migrating](https://docs.stripe.com/billing/subscriptions/billing-mode.md#migrate-existing-subscriptions-to-flexible-billing-mode) your existing ones.

We recommend that new Billing users use flexible billing mode for subscriptions and invoices, although we don’t require it.

For existing users, your default billing mode is preserved as classic to maintain backward compatibility with your current integration. However, we recommend migrating to flexible billing mode to take advantage of the latest billing features and improvements. Learn more about the [differences between classic and flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode/compare.md).

## Get started with flexible billing mode

You can set or update the billing mode through the API or Dashboard when you create or migrate subscriptions. We apply a default billing mode if you don’t specify one.

- If you create or update a subscription through the API, the default billing mode depends on your [API integration version](https://docs.stripe.com/changelog.md). For API version `2025-09-30.clover` and later, the default is `flexible`. For earlier versions, the default is `classic`. If you [upgrade your API version](https://docs.stripe.com/upgrades.md#how-can-i-upgrade-my-api), the default billing mode for new subscriptions changes accordingly.
- If you create or update subscriptions through the Dashboard (including [Payment Links](https://docs.stripe.com/payment-links.md) and [Pricing Tables](https://docs.stripe.com/payments/checkout/pricing-table.md)), the default value depends on the [billing mode default setting](https://dashboard.stripe.com/settings/billing/subscriptions) you configure in **Settings** > **Billing** > **Subscriptions and emails**.

To use flexible billing mode, your integration must be on Stripe API version [2025-06-30.basil](https://docs.stripe.com/changelog/basil.md#2025-06-30.basil) or later. Learn how to [upgrade your API version](https://docs.stripe.com/upgrades.md#how-can-i-upgrade-my-api).

### Create a new subscription with flexible billing mode

#### Dashboard

You can create a flexible billing mode subscription or update a classic billing mode subscription to be flexible through the Dashboard, regardless of your integration’s API version. To fully modify these subscriptions in the Stripe API, your integration must be on [2025-06-30.basil](https://docs.stripe.com/changelog/basil.md#2025-06-30.basil) or later. To see what version you’re on, go to the [Workbench overview](https://dashboard.stripe.com/workbench/overview) and look at the API versions section. From there, click **Upgrade** to upgrade to a newer version.

Follow the steps below to create a flexible billing mode subscription through the subscription editor:

1. Go to the [Subscriptions](https://dashboard.stripe.com/subscriptions) page in the Dashboard.
1. Click **+Create Subscription**.
1. Scroll down to the **Advanced settings** section.
1. Set **Billing mode** to **Flexible**.

The default billing mode value depends on your account settings. You can customize both the available billing mode options and the default selection in the Subscription editor. To configure this, go to **Settings** > **Billing** > **Subscriptions and emails** > [Default billing mode](https://dashboard.stripe.com/settings/billing/subscriptions). In the subscription editor, you can choose to display billing mode options from the following:

- **Classic:** Both flexible and classic billing modes are displayed, with classic selected by default. This option is recommended if your integration depends on classic billing mode and you can’t migrate to flexible billing yet.
- **Flexible:** Both flexible and classic billing modes are displayed, with flexible selected by default. This option is recommended if you’re actively migrating to flexible billing mode.
- **Flexible and hide classic:** Only flexible billing mode is displayed in the subscription editor. This option is recommended for new Stripe Billing users and for existing users who exclusively use flexible billing mode.

The billing mode default setting also determines the billing mode for subscriptions created through Dashboard-generated Payment Links and Pricing Tables. For example, if you set the billing mode default to flexible and then create a Payment Link in the Dashboard, any subscription generated from that Payment Link uses flexible billing mode.

The billing mode default setting only applies to new subscriptions created in the Dashboard. It doesn’t affect subscriptions created using the API or subscriptions migrated to flexible mode.

#### API

You can provide the [billing_mode](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-billing_mode) parameter as `flexible` on API requests that create a subscription or preview an invoice for a subscription.

If you don’t provide this parameter, its default value depends on the API version you’re using:

- For API version `2025-08-27.preview` and any later preview version, and for `2025-09-30.clover` (GA) and any later GA version, the default is flexible.
- For all other API versions, the default is `classic`.

This API version logic also determines the billing mode for subscriptions generated by Payment Links and Pricing Tables.

> Upgrading your API version to `2025-09-30.clover` or later changes the default billing mode for new subscriptions from `classic` to `flexible`. Flexible billing mode changes how subscriptions calculate prorations, handle trials, and process cancellations. To continue using classic billing mode after upgrading, explicitly set `billing_mode` to `classic` when creating subscriptions. [Review the differences](https://docs.stripe.com/billing/subscriptions/billing-mode/compare.md) before upgrading.

Here’s an example when using the Subscriptions API:

Here’s the request:

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
  billing_mode: {
    type: "flexible",
  },
  payment_behavior: "default_incomplete",
  payment_settings: {
    save_default_payment_method: "on_subscription",
  },
});
```

Here’s the response:

```json
{
  "id": "sub_JgRjFjhKbtD2qz",
  "object": "subscription",
  "billing_mode": {
    "flexible": {
      "proration_discounts": "included"
    },
    "type": "flexible",
    "updated_at": 1751071020
  },
  "application_fee_percent": null,
  "automatic_tax": {
    "disabled_reason": null,
    "enabled": false,
    "liability": "null"
  },
  "billing_cycle_anchor": 1623873347,
  "billing_cycle_anchor_config": null,
  "cancel_at": null,
  "cancel_at_period_end": false,
  "canceled_at": null,
  "cancellation_details": {
    "comment": null,
    "feedback": null,
    "reason": null
  },
  "collection_method": "charge_automatically",
  "created": 1623873347,
  "currency": "usd",
  "customer": "cus_CMqDWO2xODTZqt",
  "days_until_due": null,
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "discounts": [],
  "ended_at": null,
  "invoice_customer_balance_settings": {
    "account_tax_ids": null,
    "issuer": {
      "type": "self"
    }
  },
  "items": {
    "object": "list",
    "data": [
      {
        "id": "si_JgRjmS4Ur1khEx",
        "object": "subscription_item",
        "created": 1623873347,
        "current_period_end": 1626465347,
        "current_period_start": 1623873347,
        "discounts": [],
        "metadata": {},
        "plan": {
          "id": "price_1J32RfGPZ1iASj5zHHp57z7C",
          "object": "plan",
          "active": true,
          "amount": 2000,
          "amount_decimal": "2000",
          "billing_scheme": "per_unit",
          "created": 1623864151,
          "currency": "usd",
          "interval": "month",
          "interval_count": 1,
          "livemode": false,
          "metadata": {},
          "nickname": null,
          "product": "prod_JgPF5xnq7qBun3",
          "tiers": null,
          "tiers_mode": null,
          "transform_usage": null,
          "trial_period_days": null,
          "usage_type": "licensed"
        },
        "price": {
          "id": "price_1J32RfGPZ1iASj5zHHp57z7C",
          "object": "price",
          "active": true,
          "billing_scheme": "per_unit",
          "created": 1623864151,
          "currency": "usd",
          "livemode": false,
          "lookup_key": null,
          "metadata": {},
          "nickname": null,
          "product": "prod_JgPF5xnq7qBun3",
          "recurring": {
            "interval": "month",
            "interval_count": 1,
            "trial_period_days": null,
            "usage_type": "licensed"
          },
          "tiers_mode": null,
          "transform_quantity": null,
          "type": "recurring",
          "unit_amount": 2000,
          "unit_amount_decimal": "2000"
        },
        "quantity": 1,
        "subscription": "sub_JgRjFjhKbtD2qz",
        "tax_rates": []
      }
    ],
    "has_more": false,
    "total_count": 1,
    "url": "/v1/subscription_items?subscription=sub_JgRjFjhKbtD2qz"
  },
  "latest_invoice": {
    "id": "in_1J34pzGPZ1iASj5zB87qdBNZ",
    "object": "invoice",
    "account_country": "US",
    "account_name": "Angelina's Store",
    "account_tax_ids": null,
    "amount_due": 2000,
    "amount_overpaid": 0,
    "amount_paid": 0,
    "amount_remaining": 2000,
    "amount_shipping": 0,
    "attempt_count": 0,
    "attempted": false,
    "auto_advance": false,
    "automatic_tax": {
      "disabled_reason": null,
      "enabled": false,
      "liability": null,
      "status": null
    },
    "automatically_finalizes_at": null,
    "billing_reason": "subscription_update",
    "collection_method": "charge_automatically",
    "created": 1623873347,
    "currency": "usd",
    "custom_fields": null,
    "customer": "cus_CMqDWO2xODTZqt",
    "customer_address": null,
    "customer_email": "angelina@stripe.com",
    "customer_name": null,
    "customer_phone": null,
    "customer_shipping": {
      "address": {
        "city": "",
        "country": "US",
        "line1": "Berry",
        "line2": "",
        "postal_code": "",
        "state": ""
      },
      "name": "",
      "phone": null
    },
    "customer_tax_exempt": "none",
    "customer_tax_ids": [],
    "default_payment_method": null,
    "default_source": null,
    "default_tax_rates": [],
    "description": null,
    "discounts": [],
    "due_date": null,
    "effective_at": "1623873347",
    "ending_balance": 0,
    "footer": null,
    "from_invoice": null,
    "hosted_invoice_url": "https://invoice.stripe.com/i/acct_1By64KGPZ1iASj5z/invst_JgRjzIOILGeq2MKC9T0KtyXnD5udsLp",
    "invoice_pdf": "https://pay.stripe.com/invoice/acct_1By64KGPZ1iASj5z/invst_JgRjzIOILGeq2MKC9T0KtyXnD5udsLp/pdf",
    "last_finalization_error": null,
    "latest_revision": null,
    "lines": {
      "object": "list",
      "data": [
        {
          "id": "il_1N2CjMBwKQ696a5NeOawRQP2",
          "object": "line_item",
          "amount": 2000,
          "currency": "usd",
          "description": "1 × Gold Special (at $20.00 / month)",
          "discount_amounts": [],
          "discountable": true,
          "discounts": [],
          "invoice": "in_1J34pzGPZ1iASj5zB87qdBNZ",
          "livemode": false,
          "metadata": {},
          "parent": {
            "invoice_item_details": null,
            "subscription_item_details": {
              "invoice_item": null,
              "proration": false,
              "proration_details": {
                "credited_items": null
              },
              "subscription": "sub_JgRjFjhKbtD2qz",
              "subscription_item": "si_JgRjmS4Ur1khEx"
            },
            "type": "subscription_item_details"
          },
          "period": {
            "end": 1626465347,
            "start": 1623873347
          },
          "plan": {
            "id": "price_1J32RfGPZ1iASj5zHHp57z7C",
            "object": "plan",
            "active": true,
            "amount": 2000,
            "amount_decimal": "2000",
            "billing_scheme": "per_unit",
            "created": 1623864151,
            "currency": "usd",
            "interval": "month",
            "interval_count": 1,
            "livemode": false,
            "metadata": {},
            "nickname": null,
            "product": "prod_JgPF5xnq7qBun3",
            "tiers": null,
            "tiers_mode": null,
            "transform_usage": null,
            "trial_period_days": null,
            "usage_type": "licensed"
          },
          "price": {
            "id": "price_1J32RfGPZ1iASj5zHHp57z7C",
            "object": "price",
            "active": true,
            "billing_scheme": "per_unit",
            "created": 1623864151,
            "currency": "usd",
            "livemode": false,
            "lookup_key": null,
            "metadata": {},
            "nickname": null,
            "product": "prod_JgPF5xnq7qBun3",
            "recurring": {
              "interval": "month",
              "interval_count": 1,
              "trial_period_days": null,
              "usage_type": "licensed"
            },
            "tiers_mode": null,
            "transform_quantity": null,
            "type": "recurring",
            "unit_amount": 2000,
            "unit_amount_decimal": "2000"
          },
          "quantity": 1,
          "taxes": []
        }
      ],
      "has_more": false,
      "total_count": 1,
      "url": "/v1/invoices/in_1J34pzGPZ1iASj5zB87qdBNZ/lines"
    },
    "livemode": false,
    "metadata": {},
    "next_payment_attempt": null,
    "number": "C008FC2-0354",
    "on_behalf_of": null,
    "parent": {
      "quote_details": null,
      "subscription_details": {
        "metadata": {},
        "pause_collection": null,
        "subscription": "sub_JgRjFjhKbtD2qz"
      }
    },
    "payment_intent": {
      "id": "pi_1J34pzGPZ1iASj5zI2nOAaE6",
      "object": "payment_intent",
      "allowed_source_types": ["card"],
      "amount": 2000,
      "amount_capturable": 0,
      "amount_received": 0,
      "application": null,
      "application_fee_amount": null,
      "canceled_at": null,
      "cancellation_reason": null,
      "capture_method": "automatic",
      "charges": {
        "object": "list",
        "data": [],
        "has_more": false,
        "total_count": 0,
        "url": "/v1/charges?payment_intent=pi_1J34pzGPZ1iASj5zI2nOAaE6"
      },
      "client_secret": "pi_1J34pzGPZ1iASj5zI2nOAaE6_secret_l7FN6ldFfXiFmJEumenJ2y2wu",
      "confirmation_method": "automatic",
      "created": 1623873347,
      "currency": "usd",
      "customer": "cus_CMqDWO2xODTZqt",
      "description": "Subscription creation",
      "invoice": "in_1J34pzGPZ1iASj5zB87qdBNZ",
      "last_payment_error": null,
      "livemode": false,
      "metadata": {},
      "next_action": null,
      "next_source_action": null,
      "on_behalf_of": null,
      "payment_method": null,
      "payment_method_options": {
        "card": {
          "installments": null,
          "network": null,
          "request_three_d_secure": "automatic"
        }
      },
      "payment_method_types": ["card"],
      "receipt_email": null,
      "review": null,
      "setup_future_usage": "off_session",
      "shipping": null,
      "source": "card_1By6iQGPZ1iASj5z7ijKBnXJ",
      "statement_descriptor": null,
      "statement_descriptor_suffix": null,
      "status": "requires_confirmation",
      "transfer_data": null,
      "transfer_group": null
    },
    "payment_settings": {
      "payment_method_options": null,
      "payment_method_types": null,
      "save_default_payment_method": "on_subscription"
    },
    "period_end": 1623873347,
    "period_start": 1623873347,
    "post_payment_credit_notes_amount": 0,
    "pre_payment_credit_notes_amount": 0,
    "receipt_number": null,
    "starting_balance": 0,
    "statement_descriptor": null,
    "status": "open",
    "status_transitions": {
      "finalized_at": 1623873347,
      "marked_uncollectible_at": null,
      "paid_at": null,
      "voided_at": null
    },
    "subscription": "sub_JgRjFjhKbtD2qz",
    "subtotal": 2000,
    "tax": null,
    "tax_percent": null,
    "total": 2000,
    "total_discount_amounts": [],
    "total_tax_amounts": [],
    "transfer_data": null,
    "webhooks_delivered_at": 1623873347
  },
  "livemode": false,
  "metadata": {},
  "next_pending_invoice_item_invoice": null,
  "pause_collection": null,
  "pending_invoice_item_interval": null,
  "pending_setup_intent": null,
  "pending_update": null,
  "plan": {
    "id": "price_1J32RfGPZ1iASj5zHHp57z7C",
    "object": "plan",
    "active": true,
    "amount": 2000,
    "amount_decimal": "2000",
    "billing_scheme": "per_unit",
    "created": 1623864151,
    "currency": "usd",
    "interval": "month",
    "interval_count": 1,
    "livemode": false,
    "metadata": {},
    "nickname": null,
    "product": "prod_JgPF5xnq7qBun3",
    "tiers": null,
    "tiers_mode": null,
    "transform_usage": null,
    "trial_period_days": null,
    "usage_type": "licensed"
  },
  "quantity": 1,
  "schedule": null,
  "start": 1623873347,
  "start_date": 1623873347,
  "status": "incomplete",
  "tax_percent": null,
  "transfer_data": null,
  "trial_end": null,
  "trial_start": null
}
```

Similarly, you can set `billing_mode` to `flexible` when creating a subscription from the following sources:

- A [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md?&rds=1#create_checkout_session-billing_mode)
- A [Subscription Schedule](https://docs.stripe.com/api/subscription_schedules/create.md?&rds=1#create_subscription_schedule-billing_mode)
- A [Quote](https://docs.stripe.com/api/quotes/create.md?&rds=1#create_quote-billing_mode)

### Migrate existing subscriptions to flexible billing mode

You can migrate your existing subscriptions to flexible billing mode. The flexible behaviors take effect for all new activity on the subscription after migration. However, Stripe doesn’t recalculate any resources created before migration, including pending proration `Invoice Items`.

#### Dashboard

To use flexible billing mode, your integration must be on Stripe API version [2025-06-30.basil](https://docs.stripe.com/changelog/basil.md#2025-06-30.basil) or later. To see what version you’re on, go to the Workbench overview and look at the **API versions** section. From there, click **Upgrade** to upgrade to a newer version.

1. On the [Subscriptions](https://dashboard.stripe.com/subscriptions) page in the Dashboard, select the subscription that you want to migrate.
1. Click **Update subscription**.
1. Expand the **Billing and payment collection** section.
1. Set **Billing mode** to **Flexible**, and click **Update subscription**.

#### API

To use flexible billing mode, you must [upgrade your API version](https://docs.stripe.com/upgrades.md#how-can-i-upgrade-my-api) to [2025-06-30.basil](https://docs.stripe.com/changelog/basil.md#2025-06-30.basil) or later.

Use the [migrate API](https://docs.stripe.com/api/subscriptions/migrate.md) to set `billing_mode` to `flexible` for an existing subscription. After the subscription is migrated to flexible billing mode, the `billing_mode.updated_at` timestamp reflects when the migration occurred. Here are an example request and response:

Here’s the request:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.migrate("sub_123", {
  billing_mode: {
    type: "flexible",
  },
});
```

Here’s the response:

The response shows the updated subscription with `billing_mode` set to `flexible` and the `billing_mode_details.updated_at` timestamp:

```json
{
  "id": "sub_123",
  "billing_mode": "flexible",
  "billing_mode_details": {
    "updated_at": 1716883200 // Example timestamp
  }
  // ... other subscription details
}
```

### Billing mode and subscription schedules

When you create a subscription schedule from an existing subscription, don’t set `billing_mode` if the subscription already has one. The schedule automatically inherits the `billing_mode` from the original subscription. If you set `billing_mode` when using `from_subscription`, Stripe returns an error. If you need a different `billing_mode`, create a new subscription.

### Itemize proration discounts

If you use flexible subscriptions, you can set your preferred behavior for [proration discounts](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-billing_mode-flexible-proration_discounts) on invoices and invoice items:

- **Itemized** (Recommended): Enables invoices and invoice items to show prorations with gross amounts and accurate discount amounts, consistent with non-prorations.
- **Included**: Uses the existing Stripe proration display behavior, with net amount and zero monetary discount amounts. This setting is maintained for backward compatibility with older integrations.

Learn more about the [differences between itemized and included](https://docs.stripe.com/billing/subscriptions/billing-mode/compare.md).

To enable itemized proration discounts, you must [upgrade your API version](https://docs.stripe.com/upgrades.md#how-can-i-upgrade-my-api) to [2025-06-30.basil](https://docs.stripe.com/changelog/basil.md#2025-06-30.basil) or later.

[Create](https://docs.stripe.com/api/subscriptions/create.md) or [migrate](https://docs.stripe.com/api/subscriptions/migrate.md) a subscription in order to set `proration_discounts` to `itemized`.

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
  billing_mode: {
    type: "flexible",
    flexible: {
      proration_discounts: "itemized",
    },
  },
  payment_behavior: "default_incomplete",
  payment_settings: {
    save_default_payment_method: "on_subscription",
  },
});
```

The code example above returns the following response:

```json
{
  "id": "sub_JgRjFjhKbtD2qz",
  "object": "subscription",
  "billing_mode": {
    "flexible": {
      "proration_discounts": "itemized"
    },
    "type": "flexible",
    "updated_at": 1751071020
  },
  "application_fee_percent": null,
  "automatic_tax": {
    "disabled_reason": null,
    "enabled": false,
    "liability": "null"
  },
  "billing_cycle_anchor": 1623873347,
  "billing_cycle_anchor_config": null,
  "cancel_at": null,
  "cancel_at_period_end": false,
  "canceled_at": null,
  "cancellation_details": {
    "comment": null,
    "feedback": null,
    "reason": null
  },
  "collection_method": "charge_automatically",
  "created": 1623873347,
  "currency": "usd",
  "customer": "cus_CMqDWO2xODTZqt",
  "days_until_due": null,
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "discounts": [],
  "ended_at": null,
  "invoice_customer_balance_settings": {
    "account_tax_ids": null,
    "issuer": {
      "type": "self"
    }
  },
  "items": {
    "object": "list",
    "data": [
      {
        "id": "si_JgRjmS4Ur1khEx",
        "object": "subscription_item",
        "created": 1623873347,
        "current_period_end": 1626465347,
        "current_period_start": 1623873347,
        "discounts": [],
        "metadata": {},
        "plan": {
          "id": "price_1J32RfGPZ1iASj5zHHp57z7C",
          "object": "plan",
          "active": true,
          "amount": 2000,
          "amount_decimal": "2000",
          "billing_scheme": "per_unit",
          "created": 1623864151,
          "currency": "usd",
          "interval": "month",
          "interval_count": 1,
          "livemode": false,
          "metadata": {},
          "nickname": null,
          "product": "prod_JgPF5xnq7qBun3",
          "tiers": null,
          "tiers_mode": null,
          "transform_usage": null,
          "trial_period_days": null,
          "usage_type": "licensed"
        },
        "price": {
          "id": "price_1J32RfGPZ1iASj5zHHp57z7C",
          "object": "price",
          "active": true,
          "billing_scheme": "per_unit",
          "created": 1623864151,
          "currency": "usd",
          "livemode": false,
          "lookup_key": null,
          "metadata": {},
          "nickname": null,
          "product": "prod_JgPF5xnq7qBun3",
          "recurring": {
            "interval": "month",
            "interval_count": 1,
            "trial_period_days": null,
            "usage_type": "licensed"
          },
          "tiers_mode": null,
          "transform_quantity": null,
          "type": "recurring",
          "unit_amount": 2000,
          "unit_amount_decimal": "2000"
        },
        "quantity": 1,
        "subscription": "sub_JgRjFjhKbtD2qz",
        "tax_rates": []
      }
    ],
    "has_more": false,
    "total_count": 1,
    "url": "/v1/subscription_items?subscription=sub_JgRjFjhKbtD2qz"
  },
  "latest_invoice": {
    "id": "in_1J34pzGPZ1iASj5zB87qdBNZ",
    "object": "invoice",
    "account_country": "US",
    "account_name": "Angelina's Store",
    "account_tax_ids": null,
    "amount_due": 2000,
    "amount_overpaid": 0,
    "amount_paid": 0,
    "amount_remaining": 2000,
    "amount_shipping": 0,
    "attempt_count": 0,
    "attempted": false,
    "auto_advance": false,
    "automatic_tax": {
      "disabled_reason": null,
      "enabled": false,
      "liability": null,
      "status": null
    },
    "automatically_finalizes_at": null,
    "billing_reason": "subscription_update",
    "collection_method": "charge_automatically",
    "created": 1623873347,
    "currency": "usd",
    "custom_fields": null,
    "customer": "cus_CMqDWO2xODTZqt",
    "customer_address": null,
    "customer_email": "angelina@stripe.com",
    "customer_name": null,
    "customer_phone": null,
    "customer_shipping": {
      "address": {
        "city": "",
        "country": "US",
        "line1": "Berry",
        "line2": "",
        "postal_code": "",
        "state": ""
      },
      "name": "",
      "phone": null
    },
    "customer_tax_exempt": "none",
    "customer_tax_ids": [],
    "default_payment_method": null,
    "default_source": null,
    "default_tax_rates": [],
    "description": null,
    "discounts": [],
    "due_date": null,
    "effective_at": "1623873347",
    "ending_balance": 0,
    "footer": null,
    "from_invoice": null,
    "hosted_invoice_url": "https://invoice.stripe.com/i/acct_1By64KGPZ1iASj5z/invst_JgRjzIOILGeq2MKC9T0KtyXnD5udsLp",
    "invoice_pdf": "https://pay.stripe.com/invoice/acct_1By64KGPZ1iASj5z/invst_JgRjzIOILGeq2MKC9T0KtyXnD5udsLp/pdf",
    "last_finalization_error": null,
    "latest_revision": null,
    "lines": {
      "object": "list",
      "data": [
        {
          "id": "il_1N2CjMBwKQ696a5NeOawRQP2",
          "object": "line_item",
          "amount": 2000,
          "currency": "usd",
          "description": "1 × Gold Special (at $20.00 / month)",
          "discount_amounts": [],
          "discountable": true,
          "discounts": [],
          "invoice": "in_1J34pzGPZ1iASj5zB87qdBNZ",
          "livemode": false,
          "metadata": {},
          "parent": {
            "invoice_item_details": null,
            "subscription_item_details": {
              "invoice_item": null,
              "proration": false,
              "proration_details": {
                "credited_items": null
              },
              "subscription": "sub_JgRjFjhKbtD2qz",
              "subscription_item": "si_JgRjmS4Ur1khEx"
            },
            "type": "subscription_item_details"
          },
          "period": {
            "end": 1626465347,
            "start": 1623873347
          },
          "plan": {
            "id": "price_1J32RfGPZ1iASj5zHHp57z7C",
            "object": "plan",
            "active": true,
            "amount": 2000,
            "amount_decimal": "2000",
            "billing_scheme": "per_unit",
            "created": 1623864151,
            "currency": "usd",
            "interval": "month",
            "interval_count": 1,
            "livemode": false,
            "metadata": {},
            "nickname": null,
            "product": "prod_JgPF5xnq7qBun3",
            "tiers": null,
            "tiers_mode": null,
            "transform_usage": null,
            "trial_period_days": null,
            "usage_type": "licensed"
          },
          "price": {
            "id": "price_1J32RfGPZ1iASj5zHHp57z7C",
            "object": "price",
            "active": true,
            "billing_scheme": "per_unit",
            "created": 1623864151,
            "currency": "usd",
            "livemode": false,
            "lookup_key": null,
            "metadata": {},
            "nickname": null,
            "product": "prod_JgPF5xnq7qBun3",
            "recurring": {
              "interval": "month",
              "interval_count": 1,
              "trial_period_days": null,
              "usage_type": "licensed"
            },
            "tiers_mode": null,
            "transform_quantity": null,
            "type": "recurring",
            "unit_amount": 2000,
            "unit_amount_decimal": "2000"
          },
          "quantity": 1,
          "taxes": []
        }
      ],
      "has_more": false,
      "total_count": 1,
      "url": "/v1/invoices/in_1J34pzGPZ1iASj5zB87qdBNZ/lines"
    },
    "livemode": false,
    "metadata": {},
    "next_payment_attempt": null,
    "number": "C008FC2-0354",
    "on_behalf_of": null,
    "parent": {
      "quote_details": null,
      "subscription_details": {
        "metadata": {},
        "pause_collection": null,
        "subscription": "sub_JgRjFjhKbtD2qz"
      }
    },
    "payment_intent": {
      "id": "pi_1J34pzGPZ1iASj5zI2nOAaE6",
      "object": "payment_intent",
      "allowed_source_types": ["card"],
      "amount": 2000,
      "amount_capturable": 0,
      "amount_received": 0,
      "application": null,
      "application_fee_amount": null,
      "canceled_at": null,
      "cancellation_reason": null,
      "capture_method": "automatic",
      "charges": {
        "object": "list",
        "data": [],
        "has_more": false,
        "total_count": 0,
        "url": "/v1/charges?payment_intent=pi_1J34pzGPZ1iASj5zI2nOAaE6"
      },
      "client_secret": "pi_1J34pzGPZ1iASj5zI2nOAaE6_secret_l7FN6ldFfXiFmJEumenJ2y2wu",
      "confirmation_method": "automatic",
      "created": 1623873347,
      "currency": "usd",
      "customer": "cus_CMqDWO2xODTZqt",
      "description": "Subscription creation",
      "invoice": "in_1J34pzGPZ1iASj5zB87qdBNZ",
      "last_payment_error": null,
      "livemode": false,
      "metadata": {},
      "next_action": null,
      "next_source_action": null,
      "on_behalf_of": null,
      "payment_method": null,
      "payment_method_options": {
        "card": {
          "installments": null,
          "network": null,
          "request_three_d_secure": "automatic"
        }
      },
      "payment_method_types": ["card"],
      "receipt_email": null,
      "review": null,
      "setup_future_usage": "off_session",
      "shipping": null,
      "source": "card_1By6iQGPZ1iASj5z7ijKBnXJ",
      "statement_descriptor": null,
      "statement_descriptor_suffix": null,
      "status": "requires_confirmation",
      "transfer_data": null,
      "transfer_group": null
    },
    "payment_settings": {
      "payment_method_options": null,
      "payment_method_types": null,
      "save_default_payment_method": "on_subscription"
    },
    "period_end": 1623873347,
    "period_start": 1623873347,
    "post_payment_credit_notes_amount": 0,
    "pre_payment_credit_notes_amount": 0,
    "receipt_number": null,
    "starting_balance": 0,
    "statement_descriptor": null,
    "status": "open",
    "status_transitions": {
      "finalized_at": 1623873347,
      "marked_uncollectible_at": null,
      "paid_at": null,
      "voided_at": null
    },
    "subscription": "sub_JgRjFjhKbtD2qz",
    "subtotal": 2000,
    "tax": null,
    "tax_percent": null,
    "total": 2000,
    "total_discount_amounts": [],
    "total_tax_amounts": [],
    "transfer_data": null,
    "webhooks_delivered_at": 1623873347
  },
  "livemode": false,
  "metadata": {},
  "next_pending_invoice_item_invoice": null,
  "pause_collection": null,
  "pending_invoice_item_interval": null,
  "pending_setup_intent": null,
  "pending_update": null,
  "plan": {
    "id": "price_1J32RfGPZ1iASj5zHHp57z7C",
    "object": "plan",
    "active": true,
    "amount": 2000,
    "amount_decimal": "2000",
    "billing_scheme": "per_unit",
    "created": 1623864151,
    "currency": "usd",
    "interval": "month",
    "interval_count": 1,
    "livemode": false,
    "metadata": {},
    "nickname": null,
    "product": "prod_JgPF5xnq7qBun3",
    "tiers": null,
    "tiers_mode": null,
    "transform_usage": null,
    "trial_period_days": null,
    "usage_type": "licensed"
  },
  "quantity": 1,
  "schedule": null,
  "start": 1623873347,
  "start_date": 1623873347,
  "status": "incomplete",
  "tax_percent": null,
  "transfer_data": null,
  "trial_end": null,
  "trial_start": null
}
```
