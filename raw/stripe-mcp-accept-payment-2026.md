<!-- Source URL: https://docs.stripe.com/agentic-commerce/apps/accept-payment -->
<!-- Fetched: 2026-05-12 -->

# Accept a payment

Securely accept payments with your MCP App.

# Redirect

> This is a Redirect for when platform is web and ui is stripe-hosted. View the full page at https://docs.stripe.com/agentic-commerce/apps/accept-payment?platform=web&ui=stripe-hosted.

You can collect payments outside your app with a prebuilt Stripe-hosted Checkout page. This guide shows how to:

- Define Model Context Protocol (MCP) tools to display products and let customers select items to buy
- Collect payment details with [a prebuilt Stripe-hosted Checkout page](https://docs.stripe.com/payments/checkout.md)
- Monitor webhooks after a successful payment

## Set up Stripe

To set up Stripe, add the Stripe API library to your back end.

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create products and prices

In this example, you can display a group of products in the MCP app. Learn how to [create products and prices in the Dashboard or with the Stripe CLI](https://docs.stripe.com/products-prices/manage-prices.md).

## Register a Checkout MCP tool

Register an MCP tool that creates a [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) for a set of _Prices_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions). You call this tool from the MCP app in a later step.

```javascript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import {
  registerAppTool,
  registerAppResource,
  RESOURCE_MIME_TYPE,
} from "@modelcontextprotocol/ext-apps/server";
import { readFileSync } from "node:fs";
import Stripe from "stripe";
import { z } from "zod";

// Follow https://docs.stripe.com/keys-best-practices to protect your Stripe API keys.
const stripe = new Stripe(process.env.STRIPE_API_KEY);
const server = new McpServer({ name: "my-mcp-server", version: "1.0.0" });
const resourceUri = "ui://list-products.html";
async function createCheckoutSession(priceIds) {
  const lineItems = priceIds.map((price) => ({ price, quantity: 1 }));

  const session = await stripe.checkout.sessions.create({
    mode: "payment",
    line_items: lineItems,
    success_url: "https://example.com/checkout/success",
  });

  return session;
}

// Register the tool that creates a checkout session
server.registerTool(
  "buy-products",
  {
    title: "Buy products",
    description:
      "Create a checkout page link for purchasing the selected products",
    inputSchema: { priceIds: z.array(z.string()) },
  },
  async ({ priceIds }) => {
    const session = await createCheckoutSession(priceIds);

    return {
      content: [
        {
          type: "text",
          text: `[Complete your purchase here](${session.url})`,
        },
      ],
      structuredContent: {
        checkoutSessionId: session.id,
        checkoutSessionUrl: session.url,
      },
    };
  },
);
```

## Register a UI tool and resource

Set up the UI for your MCP app by registering an MCP tool and resource. This UI:

1. Displays a list of products
1. Lets the customer select products to buy
1. Redirects to Stripe Checkout to complete payment

### Register a list products MCP tool

Create a list products MCP tool. Its callback returns the price IDs for the products to display in the UI.

```javascript
registerAppTool(
  server,
  "list-products",
  {
    title: "List products",
    description: "List the products available for purchase",
    _meta: { ui: { resourceUri } },
  },
  async () => {
    const suggestedProducts = [
      // The price IDs from the earlier step
      { priceId: "{{PRICE_ID}}", name: "Test product 1" },
      { priceId: "{{PRICE_ID}}", name: "Test product 2" },
    ];

    return {
      structuredContent: { products: suggestedProducts },
      content: [],
    };
  },
);
```

### Register a list products UI resource

Create an MCP resource for the product list widget. It defines the UI code that displays the products.

```javascript
// Register the resource that serves the bundled HTML
registerAppResource(
  server,
  "list-products-widget",
  resourceUri,
  { mimeType: RESOURCE_MIME_TYPE },
  async () => {
    const html = readFileSync("dist/ui/list-products.html", "utf8");

    return {
      contents: [
        {
          uri: resourceUri,
          mimeType: RESOURCE_MIME_TYPE,
          text: html,
        },
      ],
    };
  },
);
```

This example uses minimal markup. In a production app, you can use a framework such as React. See the [MCP Apps documentation](https://modelcontextprotocol.github.io/ext-apps/) for additional examples.

```html
<div id="root"></div>
<script type="module" src="/ui/mcp-app.js"></script>
```

```js
import { App } from "@modelcontextprotocol/ext-apps";

const app = new App({ name: "ProductList", version: "1.0.0" });

// Establish communication with the host
await app.connect();

/**
 * UI markup and event handlers
 */
const renderProduct = (product) => {
  return `
    <label>
      <input type="checkbox" name="cart[]" value="${product.priceId}">
      ${product.name}
    </label>
  `;
};

const handleSubmit = async (event) => {
  // We'll fill this in next
};

const renderApp = (products) => {
  const root = document.querySelector("#root");

  root.innerHTML = `
    <h1>Select products to purchase</h1>
    <form id="product-form">
      ${products.map(renderProduct).join("")}
      <button type="submit">Buy</button>
    </form>
  `;

  document
    .querySelector("#product-form")
    ?.addEventListener("submit", handleSubmit);
};

/**
 * Render the list of products from the tool's structuredContent
 */
app.ontoolresult = (params) => {
  const { products } = params.structuredContent ?? {};
  if (products) {
    renderApp(products);
  }
};
```

## Redirect to Checkout

When the customer clicks **Buy** in the MCP app:

1. Call the tool that you created that buys product to create a Checkout Session URL.
1. Open the Checkout Session URL.

Update the `handleSubmit` function:

```javascript
const handleSubmit = async (event) => {
  event.preventDefault();
  const formData = new FormData(event.target);
  const priceIds = Array.from(formData.values());
  // Call the buy-products tool to create a Checkout Session
  const { structuredContent } = await app.callServerTool({
    name: "buy-products",
    arguments: { priceIds },
  });

  if (typeof structuredContent?.checkoutSessionUrl === "string") {
    await app.openLink({ url: structuredContent.checkoutSessionUrl });
  }
};
```

## Handle successful orders

You can handle successful orders by listening to `checkout.session.completed` (and `checkout.session.async_payment_succeeded` for delayed methods) and calling an idempotent fulfillment function that retrieves the Checkout Session (expand `line_items`), verifies payment_status, and fulfills the items.

Use a `success_url` landing page to trigger fulfillment immediately after redirecting, but rely on webhooks to make sure that every payment is fulfilled.

Then, you can test locally with the Stripe CLI, and deploy your webhook endpoint.

Learn more about how to [fulfill payments received with the Checkout Sessions API](https://docs.stripe.com/checkout/fulfillment.md?payment-ui=stripe-hosted).

## See also

- [Collect taxes](https://docs.stripe.com/payments/checkout/taxes.md)
- [Collect shipping and other customer info](https://docs.stripe.com/payments/checkout/collect-additional-info.md)
- [Customize your branding](https://docs.stripe.com/payments/checkout/customization.md)
- [Customize your success page](https://docs.stripe.com/payments/checkout/custom-success-page.md)

# Instant Checkout

> This is a Instant Checkout for when platform is web and ui is direct-api. View the full page at https://docs.stripe.com/agentic-commerce/apps/accept-payment?platform=web&ui=direct-api.

> - Accepting payments in ChatGPT apps is available to OpenAI-approved businesses in the United States.

- Payment methods supported on ChatGPT instant checkout are Cards, Apple Pay, Google Pay, and [Link](https://docs.stripe.com/payments/link.md).

This guide demonstrates how to accept a payment within your ChatGPT app using Instant Checkout and Stripe. To learn more about this framework, see the [ChatGPT Instant Checkout documentation](https://openai.com/index/buy-it-in-chatgpt/).

## Transaction diagram

Diagram for the ChatGPT Instant Checkout Flow (See full diagram at https://docs.stripe.com/agentic-commerce/apps/accept-payment)

## Create a Stripe profile and connect your ChatGPT app

Create a Stripe profile and authorize OpenAI to connect to your Stripe account. This lets ChatGPT securely provide a [shared payment token (SPT)](https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens.md) that represents the customer’s payment details.

1. Create your [Stripe profile](https://docs.stripe.com/get-started/account/profile.md) in the Stripe Dashboard.
1. Accept Stripe’s agentic seller terms and click **Authorize to enable OpenAI** to connect to your profile.
1. Copy your Network ID. You’ll need this when building your checkout requests in your ChatGPT app.

## Set up Stripe

First, add the Stripe API library to your back end:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Build a buy widget with Stripe

Set up the UI for your ChatGPT app by creating a buy product MCP tool and UI resource. This flow:

- Takes a product from chat context.
- Shows product information and collects the shipping address from the customer.
- Calls `window.openai.requestCheckout` when the customer is ready to proceed.

### Create products and prices

In this example, you can display a checkout flow for a product in the ChatGPT app. Learn how to [create products and prices in the Dashboard or with the Stripe CLI](https://docs.stripe.com/products-prices/manage-prices.md).

> If you have your own bespoke product logic, you don’t have to create Stripe Products. Instead, replace the Stripe Product API calls in the following sections with your own product logic.

### Register a buy product resource and tool in your MCP Server

Configure ChatGPT to render your checkout widget when customers prompt chat to buy a specific product.

```javascript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import {
  registerAppTool,
  registerAppResource,
  RESOURCE_MIME_TYPE,
} from "@modelcontextprotocol/ext-apps/server";
import { readFileSync } from "node:fs";
import Stripe from "stripe";
import { z } from "zod";

// Follow https://docs.stripe.com/keys-best-practices to protect your Stripe API keys.
const stripe = new Stripe(process.env.STRIPE_API_KEY);
const server = new McpServer({ name: "my-mcp-server", version: "1.0.0" });
const resourceUri = "ui://widget/buy-product-template.html";

registerAppResource(
  server,
  "buy-product-widget",
  resourceUri,
  {
    title: "Buy Product",
    description: "Buy Product widget",
    mimeType: RESOURCE_MIME_TYPE,
  },
  async () => {
    const html = readFileSync("dist/ui/buy-product.html", "utf8");

    return {
      contents: [
        {
          uri: resourceUri,
          mimeType: RESOURCE_MIME_TYPE,
          text: html,
        },
      ],
    };
  }
);

registerAppTool(
  server,
  "show-buy-product-widget",
  {
    title: "Buy Product",
    description: "Kickstart a checkout flow for a specific product.",
    // Add inputs here to help you find the product id
    inputSchema: { product_name: z.string() },
    _meta: { ui: { resourceUri } },
    annotations: { readOnlyHint: true }
  },
  async () => {
    // Add logic here to get product id from input schema

    const product = await stripe.products.retrieve('prod_123456');
    const amount = (await stripe.prices.retrieve(product.default_price as string)).unit_amount;

    return {
      content: [],
      structuredContent: {
        productName: product.name,
        amount: amount,
        priceID: product.default_price,
      },
    };
  }
);
```

### Create the buy product UI with the Apps SDK

This UI appears when the tool from the previous step runs. The following example uses minimal markup. In a production app, you can use a framework such as React. See the [ChatGPT Apps SDK documentation](https://developers.openai.com/apps-sdk) for more examples.

```html
<div id="root"></div>
<script type="module" src="/ui/mcp-app.js"></script>
```

```js
import { App } from "@modelcontextprotocol/ext-apps";

const app = new App({ name: "BuyProduct", version: "1.0.0" });
await app.connect();

if (!window.openai?.requestCheckout) {
  throw new Error("requestCheckout is not available in this host");
}

const root = document.getElementById("root");
let product = { name: "", amount: 0, priceID: "" };

const render = () => {
  root.innerHTML = `
    <h1>${product.name || "Loading..."}</h1>
    <p>$${(product.amount / 100).toFixed(2)}</p>
    <form onsubmit="handleSubmit(event)">
      <button type="submit">Proceed</button>
    </form>
  `;
};

app.ontoolresult = (params) => {
  const { productName, amount, priceID } = params.structuredContent ?? {};
  product = { name: productName ?? "", amount: amount ?? 0, priceID: priceID ?? "" };
  render();
};

render();
</script>

```

### Collect the shipping address and tax with Stripe

You can use the Stripe Tax API to calculate taxes used in the next step. For more information, see [Use the standalone Tax API](https://docs.stripe.com/tax/standalone-tax-api.md).

### Open the ChatGPT Instant Checkout modal

This prompts customers to select a payment method. Add logic to create a checkout session that maps to the price ID from the previous step. The following code snippet appends a UUID to the price ID to create a Checkout Session ID.

```javascript
const getTax = (priceID) => {
  // Add your tax integration
};

const createCheckoutSession = (priceID) => {
  const uuid = crypto.randomUUID();
  return `${priceID}::${uuid}`;
};

const handleSubmit = (e) => {
  e.preventDefault();
  const { name, amount, priceID } = product;
  const tax = getTax(priceID);
  window.openai.requestCheckout({
    // This is priceID passed in from the MCP buy product tool
    id: createCheckoutSession(priceID),
    // remove this when you are ready for live mode
    payment_mode: "test",
    payment_provider: {
      provider: "stripe", // Insert your Network ID from the Stripe dashboard
      merchant_id: networkID,
      supported_payment_methods: ["card"],
    },
    status: "ready_for_payment",
    currency: "USD",
    line_items: [
      {
        id: "line_items_123",
        item: {
          id: priceID,
          quantity: 1,
        },
        base_amount: product.amount,
        subtotal: product.amount,
        tax: tax,
        total: product.amount + tax,
      },
    ],
    totals: [
      {
        type: "items_base_amount",
        display_text: product.name,
        amount: product.amount,
      },
      {
        type: "subtotal",
        display_text: "Subtotal",
        amount: product.amount,
      },
      {
        type: "tax",
        display_text: "Tax",
        amount: tax,
      },
      {
        type: "total",
        display_text: "Total",
        amount: product.amount + tax,
      },
    ],
    fulfillment_options: [],
    fulfillment_address: null,
    messages: [],
    links: [
      {
        type: "terms_of_service",
        url: "https://example.com/terms",
      },
    ],
  });
};
```

## Register MCP tool to complete checkout

When the customer selects a payment method in the ChatGPT payment UI and selects **Pay**, ChatGPT calls your `complete_checkout` tool and returns the SPT that you use to create a `PaymentIntent`.

Register a `complete_checkout` MCP tool that takes a Shared Payment Granted Token as input and passes it to the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) for processing.

```javascript

const retrievePriceID = (checkout_session_id: string) => {
  const [priceID, uuid] = checkout_session_id.split('::');
  return priceID;
};

server.registerTool(
  "complete_checkout",
  {
    description: "Complete the checkout and process the payment",
    inputSchema: {
      checkout_session_id: z.string(),
      buyer: z
        .object({
          name: z.string().nullable(),
          email: z.string().nullable(),
          phone_number: z.string().nullable(),
        })
        .nullable(),
      payment_data: z.object({
        token: z.string(),
        provider: z.string(),
        billing_address: z
          .object({
            name: z.string(),
            line_one: z.string(),
            line_two: z.string().nullable(),
            city: z.string(),
            state: z.string(),
            country: z.string(),
            postal_code: z.string(),
            phone_number: z.string().nullable(),
          })
          .nullable(),
      }),
    },
  },
  async ({checkout_session_id, buyer, payment_data}) => {
    const price = (await stripe.prices.retrieve(retrievePriceID(checkout_session_id as string)))

    // Add your tax logic
    const tax = getTax()
// confirms the SPT
    stripe.paymentIntents.create({
      amount: price.unit_amount + tax,
      currency:  price.currency,
      shared_payment_granted_token: payment_data.token,
      confirm: true,
    });

    return {
      content: [],
      structuredContent: {
        id: checkout_session_id,
        status: "completed",
        currency:  price.currency,
        buyer,
        line_items: [],
        order: {
          id: "123",
          checkout_session_id,
          permalink_url: "",
        },
      },
    };
  }
);

```

## Testing

Use ChatGPT’s payments test mode with a Stripe testing environment to test your app without moving real money.

1. Enter a [sandbox](https://docs.stripe.com/sandboxes.md) in the Stripe Dashboard.
1. Create a test Stripe profile and connect to ChatGPT within the test environment, and copy your test Network ID.
1. Update your ChatGPT app settings to use payments test mode so it expects test cards and generates test SPTs.
1. When you request a checkout, provide your test profile ID and set `payment_mode` to `test` so ChatGPT expects test cards and generates test SPTs.
   ```javascript
     window.openai.requestCheckout({
         id: priceID,payment_mode: "test",
         payment_provider: {
           provider: "stripe",merchant_id: "profile_test",
           supported_payment_methods: ["card"],
         },
   ```
1. Use your test Stripe API key in your MCP tool implementation to handle test SPTs from ChatGPT. Follow [best practices](https://docs.stripe.com/keys-best-practices.md) to use the key safely: don’t embed it directly in your code, and use a secrets manager if your platform provides one.
1. Set up identical webhook configurations in your live and test environments, and make sure test webhook handlers can’t affect your production systems. For example, if your live webhook triggers shipping, the test endpoint should only log that it would have shipped in live mode.

After you complete these steps, evaluate the payments flow in your app without moving real money.

### Publish your app to live mode

When you’re ready to promote your app to live mode:

1. Create a live [restricted API key](https://docs.stripe.com/keys-best-practices.md#limit-access) (`rk_live_...`) with **Payment Intents: Write** permissions. Using a restricted key lets you give your MCP tool exactly the permissions it needs.
1. Update your MCP tool to use the live restricted API key.
1. Update your app’s checkout request with your live profile ID and remove the test `payment_mode` option.

Your app is then ready to handle live payments, which is required before submitting for ChatGPT app review.

> After you submit your ChatGPT app, don’t use test payment mode because it’s exposed to live customers.

## See also

- [Model Context Protocol](https://modelcontextprotocol.io/)
- [ChatGPT AppSDK](https://developers.openai.com/apps-sdk)
