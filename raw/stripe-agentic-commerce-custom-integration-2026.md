<!-- Source URL: https://docs.stripe.com/agentic-commerce/for-sellers/custom -->
<!-- Fetched: 2026-05-12 -->

# Build a custom integration

Learn how to use ACS with a third-party processor.

> Agentic Commerce Suite (ACS) is available in the US. Use this integration if you want to build your own checkout API endpoints and process agentic payments with a third-party payment processor. To request access and onboard your endpoint, [join the waitlist](https://go.stripe.global/agentic-commerce-contact-sales).

Use Agentic Commerce Suite (ACS) to sell your products through agents with a single integration. To build a custom integration with ACS and process payments with a third-party processor, implement a reverse API that defines the requests Stripe sends to your commerce backend and the response shapes your backend returns. When an agent routes a checkout request through Stripe, Stripe calls these endpoints on your behalf.

This lets you sell products through agents with a single integration and avoid per-agent configuration. After the agent finalizes the checkout flow, resolve the shared payment token (SPT) that you received from the agent into credentials and process the payment with your third-party processor.
ACS Seller API (See full diagram at https://docs.stripe.com/agentic-commerce/for-sellers/custom)

## Before you begin

After Stripe onboards your custom endpoint, go to [Agentic Commerce](https://dashboard.stripe.com/agentic-commerce) in the Stripe Dashboard. This flow guides you through creating a [Stripe profile](https://docs.stripe.com/get-started/account/profile.md) and requesting onboarding for the agents you want to use.

We recommend that you use Blueprints in [Workbench](https://docs.stripe.com/workbench.md) to test receiving reverse API requests in your [sandbox](https://docs.stripe.com/sandboxes.md):

- Test an `UpdateSession` reverse API request with an invalid shipping address to verify that your error validation messages display correctly.
- Test a `CompleteSession` reverse API request with specific payment data to verify your order creation logic.

You can configure request payloads, including custom line items, buyer details, fulfillment addresses, and other fields, to match your test cases. Before you go live, confirm that your checkout flow updates as expected, your shipping calculations are accurat e, and payment confirmation completes successfully. When you’re ready to sell your products through an agent, review the [agent terms](https://stripe.com/legal/ssa-services-terms#stripe-agentic-commerce-seller-services-preview) and request onboarding for the agent in the Dashboard. Stripe sends the agent an approval request that the agent must accept. To pause or stop selling through the agent, disable the agent in the Dashboard.

## Optional: Share your product data with agents

To share product data across agents through Stripe, you can upload your product data to Stripe and have Stripe forward your product details to the agents that you approve.

Create a CSV file that follows the [Stripe product feed spec](https://docs.stripe.com/agentic-commerce/product-feed.md).

### Upload product data to Stripe

You can upload your product data in the Dashboard or through the API. You can upload product data at any interval. To keep data current, upload product data once per day and send more frequent incremental updates for inventory and pricing.

> Stripe processes feed uploads as independent, asynchronous tasks. We don’t guarantee that uploads are processed or completed in the order that you submit them. If you upload multiple files in quick succession, a later upload can finish before an earlier one.

#### API

Use Stripe APIs to upload your product data CSV. We recommend using the sandbox to validate parsing, field mappings, and data quality before enabling live updates.

> If you use a [restricted API key](https://docs.stripe.com/keys.md#create-restricted-api-secret-key), it must have **Product Catalog Import** write permission. Without this permission, API requests return a `403` error.

### Create an import

Create a `ProductCatalogImport` using the [Product Catalog Import API](https://docs.stripe.com/api/v2/commerce/product-catalog-imports.md). A successful request returns a [ProductCatalogImport object](https://docs.stripe.com/api/v2/commerce/product-catalog-imports/object.md) in the `awaiting_upload` state. The `status_details.awaiting_upload.upload_url.url` field in the response contains the presigned URL for your file upload.

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

If the import completes without errors, it reaches `succeeded`. If the file is structurally valid but contains row-level validation issues, the import reaches `succeeded_with_errors`. If the import can’t complete (for example, because the file was never uploaded, is unreadable, or an internal error occurs), it reaches `failed`.

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
    "pcimprt_61THl3VA5Zt5cTqbP16T9R4DRrSQbEWmWeLUx7WmOR8K",
  );
```

If your import status is `succeeded_with_errors`, you can download the error file:

1. Look for the `status_details.succeeded_with_errors.error_file.url` field in the response.
1. Download the CSV directly from that URL before it expires.
1. The CSV contains only the rows that failed, with a leading `stripe_error_message` column describing each error.

> Error file URLs expire after 5 minutes. To get a new URL, call the retrieve endpoint again.

#### Dashboard

To upload your product data CSV, go to the [Feed history](https://dashboard.stripe.com/agentic-commerce/feed-history) page in the Stripe Dashboard.

## Set up a checkout creation hook

When a customer indicates that they want to place an order, the agent sends you a checkout request. Process the request and return the current checkout flow so the agent can show the customer details such as the total and available options such as shipping methods. If any required information is missing, the checkout flow remains incomplete.

#### Request

```json
POST api.seller.com/agentic/checkouts
{
  created: Timestamp,
  currency: "usd",
  // currently limited to single item checkouts
  line_items: [
    {
      sku_id: "sku_123",
      quantity: 2
    }
  ],
  buyer: {
    first_name: "John",
    last_name: "Doe",
    email: "john.doe@example.com",
    phone_number: "+1234567890"
  },
  fulfillment_details: {
     contact: {
        name: "Jane Doe",
        email: "jane.doe@example.com",
        phone_number: "+14155552671"
      },
      address: {
        "line_one": "123 Main St",
        "line_two": "Apt 4B",
        "city": "San Francisco",
        "state": "CA",
        "country": "US",
        "postal_code": "94105"
      }
  },
  agent_details: {
     network_profile: "profile_agent", // agent's Stripe provided unique id
     display_name: "Agent"
  }
}

```

#### Response

```json
{
  id: "checkout_123", // unique checkout identifier
  currency: "usd",
  status: "incomplete" (Enum: "incomplete | ready_for_payment | requires_escalation | processing | completed | canceled"),
  buyer: {
    first_name: "John",
    last_name: "Doe",
    email: "john.doe@example.com",
    phone_number: "+1234567890"
  },
  fulfillment_details: {
    contact: {
        name: "Jane Doe",
        email: "jane.doe@example.com",
        phone_number: "+14155552671"
      },
    address: {
      "line_one": "123 Main St",
      "line_two": "Apt 4B",
      "city": "San Francisco",
      "state": "CA",
      "country": "US",
      "postal_code": "94105"
    }
  },
  line_items: [
    {
      id: "sku_123",
      item: {
        id: "prod_abc123",
        name: "Shampoo",
        description: "Shampoo for curly hair",
        images: ["https://seller.com/images/shampoo.jpg"],
        unit_amount: 5000
      },
      quantity: 2,
      base_amount: 10000,  // pre-discount amount in cents
      discount: 1000,      // total discount applied
      subtotal: 9000,      // after discount, before tax
      tax: 720,            // tax amount
      total: 9720          // final line item total
    }
  ],
  fulfillment_options: [  // available shipping or delivery methods
    {
      type: "shipping",
      id: "ship_standard_001",
      title: "Standard Shipping",
      subtitle: "5-7 business days",
      carrier: "USPS",
      earliest_delivery_time: "2026-01-20T00:00:00Z",  // ISO 8601
      latest_delivery_time: "2026-01-22T23:59:59Z",
      subtotal: 500,
      tax: 40,
      total: 540
    },
    {
      type: "shipping",
      id: "ship_express_001",
      title: "Express Shipping",
      subtitle: "2-3 business days",
      carrier: "FedEx",
      earliest_delivery_time: "2026-01-15T00:00:00Z",
      latest_delivery_time: "2026-01-16T23:59:59Z",
      subtotal: 1500,
      tax: 0,
      total: 1500
    },
  ],
  fulfillment_option_id?: "ship_standard_001", // Implement default selected shipping option, if any
  totals: [  // itemized cost breakdown
    {
      type: "items_base_amount",
      display_text: "Items",
      amount: 10000
    },
    {
      type: "discount",
      display_text: "Discount",
      amount: -1000
    },
    {
      type: "subtotal",
      display_text: "Subtotal",
      amount: 9000
    },
    {
      type: "fulfillment",
      display_text: "Shipping",
      amount: 0  // at this step, if shipping option is not yet selected, no shipping cost to show
    },
    {
      type: "tax",
      display_text: "Sales Tax",
      amount: 720
    },
    {
      type: "total",
      display_text: "Total",
      amount: 9720
    },
    {
      type: "packing_fee",
      display_text: "Gift Wrap",
      amount: 100
    },
  ],
}
```

## Set up a checkout updated hook

Agents can update a checkout flow to change items, select fulfillment options, or update addresses. After each update, recalculate totals and confirm inventory availability. When the checkout includes all required information, mark it as `ready_for_payment`.

#### Request

```json
POST api.seller.com/agentic/checkouts/:id
{
    fulfillment_option_id?: "ship_express_001", // updated shipping option
}

```

#### Response

```json
{
  id: "checkout_123", // unique checkout identifier
  currency: "usd",status: "ready_for_payment" (Enum: "incomplete | ready_for_payment | requires_escalation | processing | completed | canceled"),
  buyer: {
    first_name: "John",
    last_name: "Doe",
    email: "john.doe@example.com",
    phone_number: "+1234567890"
  },
  fulfillment_details: {
    contact: {
        name: "Jane Doe",
        email: "jane.doe@example.com",
        phone_number: "+14155552671"
      },
    address: {
      "line_one": "123 Main St",
      "line_two": "Apt 4B",
      "city": "San Francisco",
      "state": "CA",
      "country": "US",
      "postal_code": "94105"
    }
  },
  line_items: [
    {
      id: "sku_123",
      item: {
        id: "prod_abc123",
        name: "Shampoo",
        description: "Shampoo for curly hair",
        images: ["https://seller.com/images/shampoo.jpg"],
        unit_amount: 5000
      },
      quantity: 2,
      base_amount: 10000,  // pre-discount amount in cents
      discount: 1000,      // total discount applied
      subtotal: 9000,      // after discount, before tax
      tax: 720,            // tax amount
      total: 9720          // final line item total
    }
  ],
  fulfillment_options: [  // available shipping or delivery methods
    {
      type: "shipping",
      id: "ship_standard_001",
      title: "Standard Shipping",
      subtitle: "5-7 business days",
      carrier: "USPS",
      earliest_delivery_time: "2026-01-20T00:00:00Z",  // ISO 8601
      latest_delivery_time: "2026-01-22T23:59:59Z",
      subtotal: 500,
      tax: 40,
      total: 540
    },
    {
      type: "shipping",
      id: "ship_express_001",
      title: "Express Shipping",
      subtitle: "2-3 business days",
      carrier: "FedEx",
      earliest_delivery_time: "2026-01-15T00:00:00Z",
      latest_delivery_time: "2026-01-16T23:59:59Z",
      subtotal: 1500,
      tax: 0,
      total: 1500
    },
  ],fulfillment_option_id?: "ship_express_001", // Implement default selected shipping option, if any
  totals: [  // itemized cost breakdown
    {
      type: "items_base_amount",
      display_text: "Items",
      amount: 10000
    },
    {
      type: "discount",
      display_text: "Discount",
      amount: -1000
    },
    {
      type: "subtotal",
      display_text: "Subtotal",
      amount: 9000
    },
    {
      type: "fulfillment",
      display_text: "Shipping",amount: 1500  // updated shipping cost
    },
    {
      type: "tax",
      display_text: "Sales Tax",
      amount: 720
    },
    {
      type: "total",
      display_text: "Total",
      amount: 9720
    },
    {
      type: "packing_fee",
      display_text: "Gift Wrap",
      amount: 100
    },
  ],
}
```

## Set up a checkout confirmed hook

### Receive an SPT

When the agent collects the buyer’s payment information and confirms the checkout, your confirmation hook receives an [SPT](https://docs.stripe.com/api/shared-payment/granted-token.md). The SPT is a scoped grant of the customer’s payment method from the agent to your [Stripe profile](https://docs.stripe.com/get-started/account/profile.md) with specific usage and expiration limits.

```json
POST api.seller.com/agentic/checkouts/:id/confirm
{
  payment_data: {
    token: "spt_123",  // Stripe SharedPaymentToken ID
    provider: "stripe",
    billing_address?: {  // optional
      line1?: string,
      city?: string,
      state?: string,
      postal_code?: string,
      country?: string
    }
  },
  risk_details: {
    client_device_metadata_details: {
      user_agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
      ip_address: 1.2.3.4
    }
  }
}
```

### Use an SPT

Use [SPT resolve](https://docs.stripe.com/api/v1/shared_payment/granted_tokens/resolve.md) to retrieve network credentials and submit them to your payment processor.

```bash
curl --request POST \
  --url https://api.stripe.com/v1/shared_payment/granted_tokens/:id/resolve \
  --header 'Authorization: Bearer sk_XXX' \
  --header 'Content-Type: application/x-www-form-urlencoded'
```

> The credential type appears in `payment_method_details.credentials.type` and is either `agentic_token` or `dpan`.
>
> In collaboration with the card networks, Stripe might use tokens issued through network programs such as Mastercard’s Agent Pay and Visa’s Intelligent Commerce programs on your behalf. Stripe submits the requested data to the card networks to provision and process those tokens for related transactions.

```json
{
  id: "spt_123",
  object: "shared_payment.granted_token",
  created: 1234567890,
  deactivated_at: null,
  deactivated_reason: null,
  livemode: true,
  shared_metadata: {},
  payment_method_details: {
    type: "card",
    card: {
      credentials?: {
        type: "dpan" || "agentic_token",
        // if type is agentic_token
        agentic_token?: {
          number?: string,
          exp_month?: string,
          exp_year?: string,
          cryptogram?: {
            value: string,
            type: "CAVV" | "TAVV" | "DCVV",
            eci?: string
          },
          encrypted?: {
            encryption_type: "RSA",
            encryption_block: string,
            encryption_block_fields: string,
            key_id: string
          }
        },
        // if type is dpan
        dpan?: {
          number?: string,
          exp_month?: string,
          exp_year?: string,
          cryptogram?: {
            value: string,
            type: "CAVV" | "TAVV" | "DCVV",
            eci?: string
          },
          encrypted?: {
            encryption_type: "RSA",
            encryption_block: string,
            encryption_block_fields: string,
            key_id: string
          }
        }
      },
      brand: "visa",
      country: "US",
      display_brand: "visa",
      exp_month: 9,
      exp_year: 2029,
      fingerprint: "dyRcYjZNxnHpC51l",
      funding: "credit",
      last4: "5627",
      networks: {
        available: ["visa"],
        preferred: null
      },
      wallet: null
    }
  },
  usage_details: {
    amount_captured: {
      value: 1000,
      currency: "usd"
    }
  },
  usage_limits: {
    currency: "usd",
    expires_at: 1234567890,
    max_amount: 10000
  },
  agent_details: {
    name: string,
    network_business_profile: "profile_1234"
  }
}
```

### Record a payment

After you capture the payment with your processor, record a [payment](https://docs.stripe.com/api/payment-record/report.md) and confirm the checkout flow.

```curl
curl https://api.stripe.comv1/payment_records/report_payment \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "payment_method_details[shared_payment_granted_token]=spt_123" \
  -d "amount_requested[value]=1000" \
  -d "amount_requested[currency]=usd" \
  -d initiated_at=54646747 \
  -d outcome=guaranteed \
  -d "guaranteed[amount][value]=1000" \
  -d "guaranteed[amount][currency]=usd" \
  -d "guaranteed[final_capture]=true" \
  -d "guaranteed[guaranteed_at]=54646747" \
  -d "processor_details[type]=custom" \
  -d "processor_details[custom][payment_reference]=auth_order_id_1"
```

### Respond to confirm checkout and fulfill orders

```json
{
    // status must be in_progress or completed, or you must return an error
    status: "in_progress" | "completed",
    order: {
      id: string,
      permalink_url: string,
    },
    metadata?: Hash
}
```

## Set up a checkout retrieve hook

When an agent retrieves the latest checkout state, Stripe sends you the full current checkout state, and you respond with any changes to that state. If nothing has changed, you can return the current state without making any updates.

#### Request

```bash
GET api.seller.com/agentic/checkouts/:id
```

#### Response

```json
{
  "status": "in_progress"
}
```

## See also

- [Shared Payment Tokens](https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens.md)
