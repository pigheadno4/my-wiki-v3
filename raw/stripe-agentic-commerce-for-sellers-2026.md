<!-- Source URL: https://docs.stripe.com/agentic-commerce/for-sellers -->
<!-- Fetched: 2026-05-12 -->

# Sell through agents

Learn how to sell your products through agents.

> Agentic Commerce Suite is available in the US.

Use Agentic Commerce Suite (ACS) to start selling through agents with a single integration. ACS helps you make your products discoverable and accept agentic payments across multiple commerce protocols. It lets you share product, price, and availability information with agents while minimizing changes to your existing commerce systems.

If you operate a platform, see the [guide for platforms](https://docs.stripe.com/connect/saas/tasks/enable-in-context-selling-on-ai-agents.md).

## Set up your Stripe account

If you don’t already have a Stripe account, [create one](https://stripe.com/register). After you verify your email, activate payments by providing business and personal information, linking a bank account for payouts, and setting up two-step authentication. Then, go to [Agentic commerce onboarding](https://dashboard.stripe.com/agentic-commerce) in the Stripe Dashboard. This guides you through creating a [Stripe Profile](https://docs.stripe.com/get-started/account/profile.md) and configuring settings for agentic commerce.

## Configure taxes

Use [Stripe Tax](https://docs.stripe.com/tax.md) to manage taxes and apply configurations to individual products. Follow the [tax setup guide](https://docs.stripe.com/tax/set-up.md?dashboard-or-api=api) to configure Stripe Tax. When you [create a catalog feed](https://docs.stripe.com/agentic-commerce/for-sellers.md#upload-feed), set the `stripe_product_tax_code` column to associate a product with a tax treatment. If you use [Anrok](https://www.anrok.com) for tax calculation, set the `third_party_tax_code` column in your catalog feed instead. See the [price and promotions field reference](https://docs.stripe.com/agentic-commerce/product-feed.md#price-and-promotions) for details on these fields.

## Configure support and legal policies

From [Agentic commerce settings](https://dashboard.stripe.com/settings/agentic-commerce) page, add links to your **Refund and return policy**, **Terms of service**, and **Privacy policy**. You can optionally provide a link to your **Store policy**.

## Create a catalog feed

Create a [catalog feed](https://docs.stripe.com/agentic-commerce/product-feed.md) to share your product and inventory data with agents. You can send your data using the Stripe Dashboard or API. To keep data current, we recommend uploading product data once per day and send more frequent incremental updates for inventory and pricing.

> Feed uploads are processed as independent, asynchronous tasks. We don’t guarantee uploads are processed or completed in the order you submit them. If you upload multiple files in quick succession, a later upload can finish before an earlier one.

#### API

Use Stripe APIs to upload your product data CSV. We recommend using the sandbox to validate parsing, field mappings, and data quality before enabling live updates.

> If you use a [restricted API key](https://docs.stripe.com/keys.md#create-restricted-api-secret-key), it must have **Product Catalog Import** write permission. Without this permission, API requests return a `403` error.

### Create an import

Create a `ProductCatalogImport` object using the [Product Catalog Import API](https://docs.stripe.com/api/v2/commerce/product-catalog-imports.md). A successful request returns a [ProductCatalogImport object](https://docs.stripe.com/api/v2/commerce/product-catalog-imports/object.md) in the `awaiting_upload` state. The `status_details.awaiting_upload.upload_url.url` field in the response contains the presigned URL for your file upload.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const productCatalogImport =
  await stripe.v2.commerce.productCatalog.imports.create({
    feed_type: "product",
    mode: "upsert",
    metadata: {
      file_name: "march_11_2026_product_upload.csv",
    },
  });
```

```json
{
  "id": "pcimprt_xxx",
  "object": "v2.commerce.product_catalog_import",
  "created": "2026-03-26T00:35:01.000Z",
  "feed_type": "product",
  "status": "awaiting_upload",
  "status_details": {
    "awaiting_upload": {
      "upload_url": {
        "expires_at": "2026-03-26T00:40:02.000Z",
        "url": "https://stripeusercontent.com/files/us-west-2/upload/wksp_xxx"
      }
    }
  },
  "livemode": true
}
```

### Upload your CSV

Upload your CSV to the presigned URL. The file must be in CSV or TSV format, where each row represents one product or variant. The maximum file size is 4 GB.

```curl
curl -X PUT \
  -H "Content-Type: text/csv" \
  --data-binary @"/path/to/your/file.csv" \
  "{{PRESIGNED_URL}}"
```

After Stripe receives the file, the import transitions from `awaiting_upload` to `processing`. Stripe validates the file and ingests the items.

### Monitor feed status and resolve errors

Stripe processes your product data, validates and cleans it, then indexes it in a format you can send to AI agents. You can monitor indexing progress in two ways:

#### API

Use a `GET` request to poll the import object and check the `status` field. Continue polling until the object reaches a terminal state: `succeeded`, `succeeded_with_errors`, or `failed`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const productCatalogImport =
  await stripe.v2.commerce.productCatalog.imports.retrieve(
    "{{PRODUCTCATALOGIMPORT_ID}}",
  );
```

If the import completes without errors, it reaches `succeeded`. If the file is structurally valid but contains row-level errors, it reaches `succeeded_with_errors`. If the import can’t complete (for example, because the file was never uploaded, is unreadable, or an internal error occurs), it reaches `failed`.

If your import status is `succeeded_with_errors`, you can download the error file:

1. Look for the `status_details.succeeded_with_errors.error_file.url` field in the response.
1. Download the CSV directly from that URL before it expires.
1. The CSV contains only the rows that failed, with a leading `stripe_error_message` column describing each error.

> Error file URLs expire after 5 minutes. To get a new URL, call the [retrieve endpoint](https://docs.stripe.com/api/v2/commerce/product-catalog-imports/retrieve.md) again.

#### Webhooks

Stripe sends terminal webhook events after product data indexing completes. Set up an endpoint to listen for `v2.commerce.product_catalog.imports.succeeded`, `v2.commerce.product_catalog.imports.succeeded_with_errors`, and `v2.commerce.product_catalog.imports.failed` events. Each event includes the `v2.commerce.product_catalog_import` object. See the [webhooks guide](https://docs.stripe.com/webhooks.md) for step-by-step instructions.

Here’s an example of the `v2.commerce.product_catalog.imports.succeeded` webhook payload:

```javascript
{
  "id": "evt_65THl3VA5Zt5cTqbP16T9R4DRrSQbEWmWeLUx7WmOR8B",
  "object": "v2.core.event",
  "type": "v2.commerce.product_catalog.imports.succeeded",
  "created": "2026-03-26T00:40:00.000Z",
  "livemode": true,
  "reason": null,
  "related_object": {
    "id": "pcimprt_61THl3VA5Zt5cTqbP16T9R4DRrSQbEWmWeLUx7WmOR8K",
    "type": "v2.commerce.product_catalog.imports",
    "url": "/v2/commerce/product_catalog/imports/pcimprt_61THl3VA5Zt5cTqbP16T9R4DRrSQbEWmWeLUx7WmOR8K"
  },
  "changes": {
    "before": {"status": "PROCESSING"},
    "after": {"status": "SUCCEEDED"}
  },
  "data": {}
}
```

The webhook doesn’t include the full import object. Use the `related_object.url` to retrieve it:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const productCatalogImport =
  await stripe.v2.commerce.productCatalog.imports.retrieve(
    "{{PRODUCTCATALOGIMPORT_ID}}",
  );
```

If your import status is `succeeded_with_errors`, you can download the error file:

1. Look for the `status_details.succeeded_with_errors.error_file.url` field in the response.
1. Download the CSV directly from that URL before it expires.
1. The CSV contains only the rows that failed, with a leading `stripe_error_message` column describing each error.

> Error file URLs expire after 5 minutes. To get a new URL, call the retrieve endpoint again.

#### Dashboard

Go to the [Feed history](https://dashboard.stripe.com/agentic-commerce/feed-history) page in the Dashboard and upload your product data CSV.

## Set up custom order URL

By default, Stripe returns a [payment receipt](https://docs.stripe.com/receipts.md) to a customer after you confirm the order. To provide your self-hosted order URL:

1. On the [Agentic commerce settings](https://dashboard.stripe.com/settings/agentic-commerce) page in the Dashboard, select **Custom page** in the **Receipt type** dropdown.
1. Enter your order URL in the **Custom page URL** field. Your URL must include the `{CHECKOUT_SESSION_ID}` template variable. After you confirm the order, Stripe automatically replaces it with a Checkout Session ID. You can use the ID to look up the Checkout Session and display the order information.

## Respond to purchases and fulfill orders

Monitor orders placed through AI chat agents in three ways.

#### Dashboard

View orders on the [Transactions page](https://dashboard.stripe.com/payments) in the Dashboard—they’re tagged with the originating agent. You can also filter transactions by agent names.

#### Webhooks

Stripe sends `checkout.session.completed` after the agent completes an order. Each order generates a unique `checkout.session.completed` event. The webhook includes the [CheckoutSession](https://docs.stripe.com/api/checkout/sessions/object.md) object. Set up an endpoint to listen for `checkout.session.completed` events. See the [webhooks guide](https://docs.stripe.com/webhooks.md) for step-by-step instructions.

```javascript
const stripe = require("stripe")(process.env.STRIPE_SECRET_KEY);

// Use the secret provided by Stripe CLI for local testing
// or your webhook endpoint's secret
const endpointSecret = "whsec_...";

app.post("/webhook", (request, response) => {
  const sig = request.headers["stripe-signature"];
  let event;

  try {
    event = stripe.webhooks.constructEvent(request.body, sig, endpointSecret);
  } catch (err) {
    response.status(400).send(`Webhook Error: ${err.message}`);
    return;
  }

  if (event.type === "checkout.session.completed") {
    const session = event.data.object;
    // Fulfill the order using the session data
    fulfillCheckout(session.id);
  }

  response.status(200).send();
});
```

Here’s an example of the `checkout.session.completed` webhook payload:

```javascript
{
  "id": "evt_1SUz6YRhxngcl2jFHhAi1Wiu",
  "object": "event",
  "api_version": "2025-10-29.clover",
  "created": 1763511518,
  "data": {
    "object": {
      "id": "cs_test_a1exHOZ77Pg40P1hPtcWe2oT2xI8G9ruoQohXq6jkKldIPQaGsNSPQmOGZ",
      "object": "checkout.session",
       ...
      "total_details": {
        "amount_discount": 0,
        "amount_shipping": 0,
        "amount_tax": 0
      }
    }
  },
  "livemode": false,
  ...
  "type": "checkout.session.completed"
}
```

After you receive the webhook, retrieve all required fields with a single API call. To avoid multiple requests, expand sub-resources using the [expand](https://docs.stripe.com/api/expanding_objects.md) request parameter with the preview header `Stripe-Version: 2025-12-15.preview`.

```curl
curl https://api.stripe.com/v1/checkout/sessions/{{SESSION_ID}}?expand[]=line_items.data.price.product&expand[]=line_items.data.taxes&expand[]=payment_intent.latest_charge \
  -u <<YOUR_SECRET_KEY>>: \
  -H "Stripe-Version: 2025-12-15.preview"
```

See fields in the expanded [CheckoutSession](https://docs.stripe.com/api/checkout/sessions/object.md), such as `amount_total`, quantity, and SKU ID.

### Checkout session field reference

| Order field                         | Available resource                            | API path                                                                            |
| ----------------------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Order date**                      | `CheckoutSession.PaymentIntent.LatestCharge`  | `CheckoutSessions.PaymentIntent.LatestCharge.created`                               |
| **Order quantity**                  | `CheckoutSessions`                            | `CheckoutSession.LineItems.Data[].quantity`                                         |
| **SKU**                             | `CheckoutSessions`                            | `CheckoutSession.LineItems.Data[].price.external_reference`                         |
| **Product description**             | `CheckoutSessions`                            | `CheckoutSession.LineItems.Data[].price.product.description`                        |
| **Unit price**                      | `CheckoutSessions`                            | `CheckoutSession.LineItems.Data[].price.unit_amount`                                |
| **Tax amount**                      | `CheckoutSessions`                            | `CheckoutSession.LineItems.Data[].Taxes[].amount`                                   |
| **Tax type**                        | `CheckoutSessions`                            | `CheckoutSession.LineItems.Data[].Taxes[].Rate.tax_type`                            |
| **Tax rate**                        | `CheckoutSessions`                            | `CheckoutSession.LineItems.Data[].Taxes[].Rate.percentage`                          |
| **ShippingAddress**                 | `CheckoutSessions`                            | `CheckoutSessions.CollectedInformation.shipping_details`                            |
| **BillingAddress**                  | `CheckoutSessions.PaymentIntent.LatestCharge` | `CheckoutSessions.PaymentIntent.LatestCharge.billing_details`                       |
| **Last4**                           | `CheckoutSessions.PaymentIntent.LatestCharge` | `CheckoutSessions.PaymentIntent.LatestCharge.payment_method_details.card.last4`     |
| **ExpMonth**                        | `CheckoutSessions.PaymentIntent.LatestCharge` | `CheckoutSessions.PaymentIntent.LatestCharge.payment_method_details.card.exp_month` |
| **ExpYear**                         | `CheckoutSessions.PaymentIntent.LatestCharge` | `CheckoutSessions.PaymentIntent.LatestCharge.payment_method_details.card.exp_year`  |
| **CreditCardType**                  | `CheckoutSessions.PaymentIntent.LatestCharge` | `CheckoutSessions.PaymentIntent.LatestCharge.payment_method_details.card.brand`     |
| **Final amount**                    | `CheckoutSessions`                            | `CheckoutSessions.amount_total`                                                     |
| **GTIN** (Private preview)          | `CheckoutSessions`                            | `CheckoutSession.LineItems.Data[].price.product.identifiers.gtin`                   |
| **MPN** (Private preview)           | `CheckoutSessions`                            | `CheckoutSession.LineItems.Data[].price.product.identifiers.mpn`                    |
| **Agent details** (Private preview) | `CheckoutSession.PaymentIntent`               | `CheckoutSessions.PaymentIntent.agent_details`                                      |
| **OrderNo**                         | `CheckoutSession.PaymentIntent.LatestCharge`  | `CheckoutSessions.PaymentIntent.LatestCharge.receipt_number`                        |

#### Batch processing

Instead of fulfilling each order individually, bulk fulfill orders using the [List CheckoutSessions endpoint](https://docs.stripe.com/api/checkout/sessions/list.md).

```curl
# List all successful CheckoutSessions in the last hour
curl https://api.stripe.com/v1/checkout/sessions?created[gt]={{TIMESTAMP}}&status=complete \
  -u <<YOUR_SECRET_KEY>>:
```

To prevent duplicate fulfillments, use the `starting_after` parameter.

```curl
curl https://api.stripe.com/v1/checkout/sessions?created[gt]={{TIMESTAMP}}&status=complete&starting_after={{LAST_SESSION_ID}} \
  -u <<YOUR_SECRET_KEY>>:
```

## Test your integration

You can test your integration directly from the Dashboard in a [sandbox](https://docs.stripe.com/sandboxes.md):

1. Go to the [Agentic Commerce](https://dashboard.stripe.com/agentic-commerce) page, then click **View catalog**.
1. Hover over the product you want to test, then click **Test in Workbench**.

## Enable sales on an AI chat agent

When you’re ready to sell through an AI interface, review the agent terms and enable the agent in the Stripe Dashboard. Stripe sends the agent an approval request that the agent must accept. To pause or stop selling on an AI chat agent, disable the agent in the Dashboard.

## Optional: Set up manual capture

By default, Stripe captures payments immediately after purchase. To use manual capture, open the [Agentic commerce settings](https://dashboard.stripe.com/settings/agentic-commerce) page in the Dashboard and set capture mode to manual. When you enable manual capture, call the `capture` method on the `PaymentIntent`:

```curl
curl -X POST https://api.stripe.com/v1/payment_intents/pi_3MrPBM2eZvKYlo2C1TEMacFD/capture \
  -u "<secret_key>:" \
  -H "Stripe-Version: 2025-09-30.preview"
```

## Optional: Set up an order approval hook

Before we confirm a payment, we check inventory based on your product catalog data and might run fraud checks depending on your [Radar](https://docs.stripe.com/radar.md) setup. To control whether we complete a purchase, configure an order approval hook. Before we complete the checkout flow, we send an approval request to your service. You must approve or decline the request.

Stripe enforces a four-second timeout for your hook. If your hook doesn’t respond within this time, Stripe declines the payment.

To set up an order approval hook:

1. Specify the endpoint on the [Agentic Commerce settings](https://dashboard.stripe.com/settings/agentic-commerce) page in the Dashboard.
1. Enable **Order approvals**.
1. Implement your logic at the endpoint and use the request and response formats below.

> Stripe returns a `424` status code to agents if your endpoint returns a non-`2xx` status code. Some agents might retry these API requests, so you must make sure that your endpoint is idempotent.

### Request format

Stripe sends the following request to your endpoint:

```typescript
{
  type: "v1.delegated_checkout.finalize_checkout",
  id: string,
  livemode: boolean,
  // account ID
  context?: string,
  // request specific data
  data: {
    amount_subtotal?: number,
    amount_total?: number,
    billing_details?: {
      name?: string,
      address?: {
        line1?: string,
        line2?: string,
        city?: string,
        state?: string,
        postal_code?: string,
        country?: string
      }
    },
    currency: string,
    email?: string,
    line_items_details: Array<{
      id: string,
      unit_amount: number,
      quantity: number,
      name: string
    }>,
    payment_method_details?: {
      type: "card" | ...,
      card?: {
        brand: "amex" | "visa" | "master_card" | ...,
        country?: string,
        exp_month: number,
        exp_year: number,
        fingerprint?: string,
        funding: "credit" | "debit" | "prepaid" | "unknown",
        iin?: string,
        last4: string,
        wallet?: {
          type: "apple_pay" | "google_pay" | ...
        }
      }
    },
    phone?: string,
    shipping_details?: {
      name?: string,
      address?: {
        line1?: string,
        line2?: string,
        city?: string,
        state?: string,
        postal_code?: string,
        country?: string
      },
    },
    total_details?: {
      amount_discount?: number,
      amount_shipping?: number,
      amount_tax?: number
    }
  }
}
```

### Response format

Your endpoint must return `200` HTTP responses with the following format:

```typescript
{
  manual_approval_details: {
    type: "approved" | "declined",
    declined?: {
      reason: string
    }
  },
  // Connect only: set an application fee for the transaction
  application_fee_details?: {
    application_fee_amount: number,
    transfer_data?: {
      amount?: number,
    }
  }
}
```

## Optional: Set up a checkout customization hook

By default, Stripe calculates taxes and shipping options for your products based on the options defined in your [product catalog](https://docs.stripe.com/agentic-commerce/product-feed.md).

To calculate taxes or shipping options and costs dynamically with your logic:

1. Specify the endpoint on the [Agentic Commerce settings](https://dashboard.stripe.com/settings/agentic-commerce) page in the Dashboard.
1. Enable **Custom tax rates** or **Custom shipping options**.
1. Implement your logic at the endpoint and use the request and response formats below.

> Stripe returns a `424` status code to agents if your endpoint returns a non-`2xx` status code. Some agents might retry these API requests, so you must make sure that your endpoint is idempotent.

### Request format

Stripe sends the following request to your endpoint:

```typescript
{
  type: "v1.delegated_checkout.customize_checkout",
  id: string,
  livemode: boolean,
  // Connected account ID
  context?: string,
  // Request specific data
  data: {
    // Used by the seller to determine whether they can set manual tax rates on line items
    automatic_tax: {
      enabled: boolean,
    },
    currency: string,
    line_item_details?: Array<{
      id: string,
      sku_id: string,
      unit_amount: number,
      amount_discount: number,
      amount_subtotal: number,
      amount_tax: number,
      amount_total: number,
      quantity: number,
      name: string,
      tax_rates: Array<{
        rate: {
          id: string,
          display_name: string,
          percentage: number,
          inclusive: boolean,
        }
        // Amount of tax applied for this rate.
        amount: number
      }>
    }>,
    shipping_details?: {
      // Same as the shipping rate object described at https://docs.stripe.com/api/shipping_rates/object#shipping_rate_object
      shipping_rate?: {
        id: string,
        display_name?: string,
        metadata?: Map<string,string>,
        tax_code?: string ,
        tax_behavior: 'unspecified' | 'inclusive' | 'exclusive',
        fixed_amount: {
          amount: number,
          currency: 'usd' | 'cad' | etc.,
          currency_options.<currency>: {
            amount: number,
            tax_behavior: 'unspecified' | 'inclusive' | 'exclusive',
          }
        },
        delivery_estimate?: {
          maximum: { unit: 'business_day' | 'day' | 'hour' | 'month' | 'year', value: number },
          minimum: { unit: 'business_day' | 'day' | 'hour' | 'month' | 'year', value: number }
        }
      },
      // Same as the shipping rate object described at https://docs.stripe.com/api/shipping_rates/object#shipping_rate_object
      shipping_rates?: Array<{
        id: string,
        display_name?: string,
        metadata?: Map<string,string>,
        tax_code?: string,
        tax_behavior: 'unspecified' | 'inclusive' | 'exclusive',
        fixed_amount: {
          amount: number,
          currency: 'usd' | 'cad' | etc.,
          currency_options.<currency>: {
            amount: number,
            tax_behavior: 'unspecified' | 'inclusive' | 'exclusive',
          }
        },
        delivery_estimate?: {
          maximum: { unit: 'business_day' | 'day' | 'hour' | 'month' | 'year', value: number },
          minimum: { unit: 'business_day' | 'day' | 'hour' | 'month' | 'year', value: number }
        }
      },
      address?: {
        line1?: string,
        line2?: string,
        city?: string,
        state?: string,
        postal_code?: string,
        country?: string
      }
    },
    amount_total?: number,
    amount_subtotal?: number,
    total_details?: {
      amount_discount?: number,
      amount_shipping?: number,
      amount_tax?: number
    }
  }
}
```

### Response format

Your endpoint must return a `200` HTTP response with the following format:

```typescript
{
  shipping_options?: Array<{
    // ID of the shipping rate, or data provided to create the shipping rate. Only provide one; not both
    shipping_rate?: string,
    shipping_rate_data: {
      display_name?: string,
      fixed_amount: {
        amount: number,
        currency: 'usd' | 'cad' | etc.,
      },
      metadata?: Map<string,string>,
      tax_code?: string ,
      tax_behavior?: 'unspecified' | 'inclusive' | 'exclusive',
      // Same as the shipping rate object described at https://docs.stripe.com/api/shipping_rates/create#create_shipping_rate-delivery_estimate
      delivery_estimate?: {
        maximum: { unit: 'business_day' | 'day' | 'hour' | 'month' | 'year', value: number },
        minimum: { unit: 'business_day' | 'day' | 'hour' | 'month' | 'year', value: number }
      }
    },
  }>,
  line_items?: Array<{
    // Corresponding ID of the line item to update
    id: string,
    // List of tax rates to apply to this line item
    // Provide either `rate` or `rate_data`
    tax_rates: Array<{
      // ID of a v1 tax rate
      rate?: string,
      // Or `rate_data`.
      // This will use an existing tax rate that matches the params or will create one if a matching rate does not exist
      rate_data?: {
        display_name: string,
        inclusive: boolean,
        // percentage out of 100
        percentage: number,
      }
    },
  }>
}
```

## Optional: Test your hooks

You can test your order approval or checkout customization hook by providing a publicly accessible endpoint that can accept hook requests with a `POST` method. Set up your endpoint function so that it:

1. Handles `POST` requests with a JSON payload
1. Returns a successful status code (`200`)

For local development, use a tunneling tool such as [ngrok](https://ngrok.com/) to expose your local endpoint.

### Example endpoint

This code snippet shows an endpoint function that receives `v1.delegated_checkout.finalize_checkout` requests and returns a `200` response. You can find the signing secret under the **Agentic Commerce Extension** event destination in your webhook settings in the [Developer Dashboard](https://docs.stripe.com/development/dashboard.md).

#### Node.js

```javascript
// Using Express
const express = require("express");
const stripe = require("stripe")(process.env.STRIPE_SECRET_KEY);
const app = express();

// Replace with your endpoint's secret from your webhook settings
const endpointSecret = "whsec_...";

app.post(
  "/hooks",
  express.raw({ type: "application/json" }),
  (request, response) => {
    const sig = request.headers["stripe-signature"];

    // Verify the webhook signature
    try {
      stripe.webhooks.signature.verifyHeader(
        request.body.toString(),
        sig,
        endpointSecret,
      );
    } catch (err) {
      return response.status(400).send(`Webhook Error: ${err.message}`);
    }

    // Handle the payload
    const payload = JSON.parse(request.body);
    if (payload.type === "v1.delegated_checkout.finalize_checkout") {
      // Check inventory and accept payment
      const data = { manual_approval_details: { type: "approved" } };
      return response.status(200).json(data);
    }

    response.status(200).end();
  },
);

app.listen(4242, () => console.log("Node server listening on port 4242!"));
```

## Optional: Send incremental inventory updates

In addition to uploading your product data, send individual product inventory updates through the [Imports API](https://docs.stripe.com/api/v2/commerce/product-catalog-imports.md). Use the same upload process as product data uploads, but set `feed_type` to `inventory`. Inventory feeds support only `upsert` mode.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const productCatalogImport =
  await stripe.v2.commerce.productCatalog.imports.create({
    feed_type: "inventory",
    mode: "upsert",
    metadata: {
      file_name: "march_11_2026_inventory_upload.csv",
    },
  });
```

## Optional: Send incremental price updates

Upload your product data, then send individual price updates through the [Imports API](https://docs.stripe.com/api/v2/commerce/product-catalog-imports.md). Use the same upload process as product data uploads and set `feed_type` to `pricing`. Price feeds support only `upsert` mode.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const productCatalogImport =
  await stripe.v2.commerce.productCatalog.imports.create({
    feed_type: "pricing",
    mode: "upsert",
    metadata: {
      file_name: "march_11_2026_pricing_upload.csv",
    },
  });
```

## Optional: Handle refunds and disputes

If a customer cancels the order on your website or through customer service after checkout succeeds, initiate a refund. If you already use the Checkout Sessions or PaymentIntents API, your existing refund flow works without changes for agentic checkouts. You can manage refunds and disputes in the Dashboard on the [Transactions page](https://dashboard.stripe.com/payments), or use the [Refunds API](https://docs.stripe.com/api/refunds.md) to handle cancellations and refunds programmatically.

## See also

- [Shared Payment Tokens](https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens.md)
