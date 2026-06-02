<!-- Source URL: https://docs.paypal.ai/growth/agentic-commerce/agent-ready -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Agent Ready

Agent Ready makes your business ready for agentic commerce by transforming your existing PayPal and Braintree integrations to work seamlessly with AI platforms, like ChatGPT.

## Agentic Commerce Protocol

The Agentic Commerce Protocol (ACP) is an open standard that OpenAI developed to enable AI agents to complete purchases on behalf of buyers. ACP consists of the specifications in the following table.

| Specification     | Description                                                     | Integration       |
| ----------------- | --------------------------------------------------------------- | ----------------- |
| Product feed      | How merchants expose their product catalog for AI discovery.    | OpenAI ↔ Merchant |
| Agentic checkout  | How AI agents create checkout sessions and complete orders.     | OpenAI ↔ Merchant |
| Delegated payment | How AI platforms securely obtain payment credentials from PSPs. | OpenAI ↔ PSP      |

To learn more about ACP, see the [OpenAI Agentic Commerce Protocol Documentation](https://developers.openai.com/commerce/specs/checkout).

## How Agent Ready works with ACP

Using ACP, an AI platform can discover your products (product feed), negotiate checkout with your server (agentic checkout), obtain a secure, one-time-use payment token from PayPal or Braintree (delegated payment), and send that token to you as part of checkout.

Agent Ready supports merchants who use Braintree as a payment provider and integrate using Braintree SDK and GraphQL.

## Enable Instant Checkout in a custom ChatGPT app

You can build a custom ChatGPT app that provides a tailored shopping experience while leveraging PayPal's Agent Ready capabilities for payment processing.

To build a custom ChatGPT app using the [ChatGPT Apps SDK](https://platform.openai.com/docs/guides/chatgpt/apps-sdk), complete the steps in this section.

### Prerequisites

- Build your app using the ChatGPT Apps SDK.
- Implement MCP server with the `complete_checkout` tool to receive tokens.
- Call `requestCheckout()` from the app to trigger Instant Checkout.
- Follow the ACP agentic checkout specification to manage checkout sessions.
- Specify `braintree` as your payment provider.
- Process payment tokens using your existing Braintree integration.

### Tips for building a ChatGPT app

This guide does not tell you how to build a ChatGPT app. The following tips and resources, however, could help.

- [ChatGPT Apps SDK documentation](https://platform.openai.com/docs/guides/chatgpt/apps-sdk)
- [Build your ChatGPT UI](https://developers.openai.com/apps-sdk/build/chatgpt-ui)
- [Example ChatGPT apps](https://github.com/openai/openai-apps-sdk-examples)

### Step 1: Specify Braintree as your payment provider

When your ChatGPT app widget calls `requestCheckout()`, you must construct a checkout session that specifies Braintree as the payment provider according to the ACP [Agentic Checkout Specification](https://developers.openai.com/commerce/specs/checkout#post-checkout_sessions).

#### Widget calls `requestCheckout()`

```javascript theme={null}
const checkoutRequest = {
  id: checkoutSessionId,
  payment_provider: {
    provider: "braintree",
    merchant_id: "your_braintree_merchant_id",
    supported_payment_methods: ["card", "applepay", "googlepay"],
  },
  status: "ready_for_payment",
  currency: "USD",
  totals: [
    {
      type: "total",
      display_text: "Total",
      amount: 330, // Amount in cents
    },
  ],
  links: [
    { type: "terms_of_use", url: "https://yoursite.com/terms" },
    { type: "privacy_policy", url: "https://yoursite.com/privacy" },
  ],
  payment_mode: "live", // Use "test" for testing with test cards
};

// Open Instant Checkout UI in ChatGPT
const order = await window.openai.requestCheckout(checkoutRequest);
```

| Parameter                                    | Description                                                                                                                                          |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                         | Unique checkout session identifier                                                                                                                   |
| `payment_provider.provider`                  | Identify Braintree as the payment provider (`braintree`).                                                                                            |
| `payment_provider.merchant_id`               | Your Braintree public [merchant ID](https://developer.paypal.com/braintree/articles/control-panel/important-gateway-credentials#merchant-id)         |
| `payment_provider.supported_payment_methods` | An array of payment methods that your Braintree integration supports. Current supported values are: <br /> `card` <br /> `applepay`<br />`googlepay` |
| `status`                                     | Set to `ready_for_payment` to indicate that the checkout session is ready to accept payment.                                                         |
| `currency`                                   | The [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) currency code for the transaction (for example, `USD`).                             |
| `totals`                                     | An array of line items for the transaction, showing the amounts in cents.                                                                            |
| `payment_mode`                               | Set to `live` for production environments or `test` for testing.                                                                                     |

For more information, see the [Apps SDK Monetization Guide](https://developers.openai.com/apps-sdk/build/monetization).

### Step 2: Complete checkout and process payments

To complete checkout, your MCP server must expose a `complete_checkout` tool that receives the token and processes it.

> **Note:** Use the payment method nonce exactly as you would use any payment method nonce in Braintree's [transaction.sale](https://developer.paypal.com/braintree/docs/reference/request/transaction/sale/php) method or [chargePaymentMethod](https://developer.paypal.com/braintree/graphql/reference/#Mutation--chargePaymentMethod) GraphQL mutation.

The following example uses Python.

```python theme={null}
@tool(description="Complete checkout and process payment")
async def complete_checkout(
    self,
    checkout_session_id: str,
    buyer: Buyer,
    payment_data: PaymentData,
) -> types.CallToolResult:

    # Extract the delegated payment token
    token = payment_data.token

    # Process payment using Braintree SDK
    result = gateway.transaction.sale({
        "amount": "10.00",
        "payment_method_nonce": token,
        "options": {
            "submit_for_settlement": True
        }
    })

    if result.is_success:
        return types.CallToolResult(
            content=[],
            structuredContent={
                "id": checkout_session_id,
                "status": "completed",
                "currency": "USD",
                "order": {
                    "id": result.transaction.id,
                    "checkout_session_id": checkout_session_id,
                    "permalink_url": f"https://yoursite.com/orders/{result.transaction.id}",
                },
            },
            isError=False,
        )
    else:
        # Return error response
        return types.CallToolResult(
            content=[{
                "type": "text",
                "text": f"Payment failed: {result.message}"
            }],
            isError=True,
        )
```

> **Note:** The payment token in `payment_data.token` (for example, `"tokencc_bf_abc123_456def_ghijkl_mno789_pqr"`) is a one-time-use token that you can process using your existing Braintree integration to complete the payment. In Braintree, this type of token is called a [payment method nonce](https://developer.paypal.com/braintree/docs/guides/payment-method-nonces). It serves as a secure, single-use reference to the buyer's payment information. It's bound to your merchant ID and includes amount and time restrictions that you can configure.

### Test your integration

To test Instant Checkout in a ChatGPT App, extend your MCP server to render a widget in the ChatGPT application by completing these steps.

#### 1. Register a resource in your MCP server

This step depends on your implementation. For example, if you want your application to display a Buy Now product card when someone prompts ChatGPT with something like "I want to buy wireless headphones," you build a front-end application that reads ChatGPT's input and renders the Buy Now product card. Then, you register that HTML as a resource for the `complete_checkout` tool in your [MCP server](#step-2-implement-the-complete-checkout-tool), as shown in the following example.

```javascript theme={null}
const widgetHTML = loadWidgetHTML();
const buyProductTemplateUri = "ui://widget/buy-product-template.html";

mcpServer.registerResource(
  "buy-product-widget",
  buyProductTemplateUri,
  {
    title: "Buy Product",
    description: "Buy Product Widget",
    mimeType: "text/html+skybridge",
  },
  async (uri) => ({
    contents: [
      {
        uri: uri.href,
        mimeType: "text/html+skybridge",
        text: widgetHTML,
      },
    ],
  }),
);
```

Your `widgetHTML` variable references the result of reading an HTML file. This guide does not require you to use any specific coding language or framework. These choices are up to you or your selected integrator.

#### 2. Register the tool to use the widget in your MCP server

After you register your tool, you must register the `complete_checkout` tool to use that resource. The following example is a tool that retrieves product information and returns it in the `structuredContent` field. ChatGPT attaches this response to `window.openapi.toolOutput` for your application to read and render.

```javascript theme={null}
mcpServer.registerTool(
  "show-buy-product-widget",
  {
    title: "Buy Product",
    description: "Shows the Buy Now Product Widget",
    inputSchema: {
      // Your integration should use a library like Zod or JSON Schema here.
      product_title: string,
    },
    _meta: { "openai/outputTemplate": buyProductTemplateUri },
    annotations: { readOnlyHint: true },
  },
  async (input) => {
    //This is just an example, your application can retrieve product information in anyway you see fit
    const product = await productService.findByTitle(input.product_title);
    return {
      content: [],
      structuredContent: {
        ...product,
      },
      _meta: {
        "openai/outputTemplate": widgetHTML,
      },
    };
  },
);
```

For more information about the `complete_checkout` tool, see [Step 2: Implement the `complete_checkout` tool](#step-2-implement-the-complete-checkout-tool).

#### 3. Initiate checkout from your ChatGPT app

To initiate checkout from your ChatGPT app, call `window.openai.requestCheckout`, typically using a button. When ChatGPT initiates checkout, your server's `/checkout_sessions` response must specify Braintree as the payment provider according to the [ACP agentic checkout specification](https://developers.openai.com/commerce/specs/checkout#agentic-checkout-specification), as shown in the following example.

```json theme={null}
{
  "payment_provider": {
    "provider": "braintree",
    "supported_payment_methods": ["card"],
    "merchant_id": "your_braintree_merchant_id"
  }
}
```

| Parameter                                    | Description                                                                                                                                                                                                                                        |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_provider.provider`                  | Payment provider. Set to `braintree`.                                                                                                                                                                                                              |
| `payment_provider.supported_payment_methods` | An array of payment methods that your Braintree integration supports. Available values are: <br /> `card`<br />`applepay`<br />`googlepay` <br /> <br />Other options, including these, are coming soon: <br />`paypal_wallet`<br />`venmo_wallet` |
| `merchant_id`                                | Your Braintree [merchant ID](https://developer.paypal.com/braintree/articles/control-panel/important-gateway-credentials#merchant-id), which identifies your Braintree account.                                                                    |

> **Note:** OpenAI uses the `merchant_id` that you provide here in the `allowance.merchant_id` field when it requests delegated payment tokens.

#### 4. Register your app in ChatGPT

After you host your MCP server with a publicly available URL, test your application in ChatGPT's developer mode.

1. Enable developer mode by navigating to **ChatGPT → Settings → Apps → Advanced Settings**, and use the toggle to turn on developer mode.
2. Register your application by navigating to **ChatGPT → Settings → Apps → Create App** and entering your application URL.

Now you can go to the ChatGPT prompt screen, click the plus (+) symbol, select your application, and enter the prompt to display your widget.

## Allowance validation

Braintree validates the following fields in the allowance when issuing a delegated payment token.

### `merchant_id`

The `merchant_id` must match the Braintree [public merchant ID](https://developer.paypal.com/braintree/articles/control-panel/important-gateway-credentials#merchant-id) that processes the transaction.

```json theme={null}
{
  "message": "Unknown or expired single-use payment method.",
  "path": ["chargePaymentMethod"],
  "extensions": {
    "errorClass": "VALIDATION",
    "errorType": "user_error",
    "inputPath": ["input", "paymentMethodId"],
    "legacyCode": "91565"
  }
}
```

### `max_amount`

The `max_amount` must be greater than or equal to the transaction amount.

```json theme={null}
{
  "message": "Transaction amount exceeds the payment method maximum amount.",
  "path": ["chargePaymentMethod"],
  "extensions": {
    "errorClass": "VALIDATION",
    "errorType": "user_error",
    "inputPath": ["input", "transaction", "amount"],
    "legacyCode": "915266"
  }
}
```

### `currency`

The currency on the transaction must match the configured currency for the transacting merchant.

```json theme={null}
{
  "message": "Transaction currency does not match the payment method currency.",
  "path": ["chargePaymentMethod"],
  "extensions": {
    "errorClass": "VALIDATION",
    "errorType": "user_error",
    "inputPath": ["input", "transaction", "merchantAccountId"],
    "legacyCode": "915267"
  }
}
```

### `expires_at`

```json theme={null}
{
  "message": "Unknown or expired single-use payment method.",
  "path": ["chargePaymentMethod"],
  "extensions": {
    "errorClass": "VALIDATION",
    "errorType": "user_error",
    "inputPath": ["input", "paymentMethodId"],
    "legacyCode": "91565"
  }
}
```

## Track AI-initiated transactions

PayPal and Braintree provide the following ways to track AI-initiated transactions.

### Transaction facilitator details

When you process a transaction with a delegated payment token, it includes the following fields in the transaction response.

```bash theme={null}
transaction.facilitator_details.oauth_application_client_id
transaction.facilitator_details.oauth_application_name # "ChatGPT"
```

For example, your transaction response might look similar to this one.

```bash theme={null}
result = gateway.transaction.find("transaction_id")
puts result.transaction.facilitator_details.oauth_application_name
# => "ChatGPT"
puts result.transaction.facilitator_details.oauth_application_client_id
# => "oauth_client_abc123"
```

### Search for AI-initiated transactions

You can search for transactions by AI platform using the Braintree Control Panel or API.

#### Braintree Control Panel

- Navigate to the [Braintree Control Panel](https://www.braintreegateway.com/).
- Use the search filter for `facilitator_details.oauth_application_name`.
- Select `ChatGPT` to view all ChatGPT-initiated transactions.

#### API

<CodeGroup>
  ```javascript Query theme={null}
    query($input: TransactionSearchInput!) {
      search {
        transactions(input: $input) {
          edges {
            node {
              id
              amount { value }
            }
          }
        }
      }
    }
  ```

```json Input theme={null}
{
  "input": {
    "facilitatorOAuthApplicationClientId": {
      "is": "ChatGPT"
    }
  }
}
```

```json Success response theme={null}
{
  "data": {
    "search": {
      "transactions": {
        "edges": [
          {
            "node": {
              "id": "dHJhbnNhY3Rpb25fN3gybWJlcHg",
              "amount": {
                "value": "7.50"
              }
            }
          },
          {
            "node": {
              "id": "dHJhbnNhY3Rpb25fMjlxMXYwNjQ",
              "amount": {
                "value": "10.00"
              }
            }
          }
        ]
      }
    }
  },
  "extensions": {
    "requestId": "f9773cbb-5994-4c04-a55b-ccb20d496a18"
  }
}
```

</CodeGroup>
