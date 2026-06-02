<!-- Source URL: https://developer.paypal.com/studio/checkout/standard/integrate (Recurring Payment tab) -->
<!-- Fetched: 2026-04-13 -->

Online / Checkout / PayPal / Integrate / Recurring Payment

# Recurring Payments

The Recurring payments module helps you display recurring payment information to the payer before they commit to the payment. Recurring payments are initiated by a merchant based on a schedule or other criteria. Examples include subscriptions and automatic bill payments.

Pay with PayPal supports saving payment methods so that you can charge payers on a recurring basis. To learn more about how to save payment methods, review the Save PayPal for purchase later with the JavaScript SDK guide.

## Eligibility

- Available for buyers and merchants in the United States.
- Must be integrated using the Payment Method Tokens v3 API for a Save for Purchase Later buyer experience.

## How it works

1. The buyer signs up for your service and adds PayPal as a payment method.
2. PayPal authenticates the buyer and creates a setup token.
3. The Recurring Payments module shows the buyer details about the recurring payment.
4. The buyer consents to the billing agreement.
5. PayPal creates a payment token that you can use to create and capture payments.

---

## 1. Recurring payments flow

### Step 1. Create setup token

To set up the recurring payment module, pass additional fields in the Create setup token request. The buyer reviews and agrees to the recurring billing terms to allow the merchant to charge their PayPal account for future payments.

There are two types of information that you need to provide:

#### Recurring payment type

Pass the recurring payment type in the `payment_source.paypal.usage_pattern` field of the Create setup token request when you set the payment method. This flags the payment method token for future recurring payments and tailors content in the PayPal flow to show the buyer that this will be a recurring payment.

Recurring payment options include subscriptions, unscheduled payments, and installments. Choose prepaid when the payments are upfront or postpaid when the payments come after the goods or services are delivered.

#### Recurring billing plan

This shows the buyer a summary of the recurring payment agreement in PayPal. The recurring billing plan details are passed in the `payment_source.paypal.billing_plan` object of the Create setup token request:

- `name`: The billing plan name is an optional description used to provide further information to the buyer about the service they are purchasing as part of a recurring payment arrangement. This is displayed within the PayPal flow.
- `billing_cycles`: The billing cycle is a set of attributes relating to the amount and duration of a billing agreement. Although most recurring payments consist of only one or two billing cycles, PayPal's recurring payments structure supports an array of up to 3 billing cycles to support more complex recurring payment arrangements. A billing cycle may either be a trial or a regular cycle. Trial cycles may be either chargeable or free.
- `one_time_charges`: Data that can be provided for a one-time fee that is not part of the ongoing recurring payment arrangement with the payer. Examples of this include setup fees and items ordered when establishing a recurring payment, such as a mobile phone purchased upon signing up for a service plan.

#### Customize your plan

Configure your `usage_pattern` and `billing_cycle` to match your needs. For more information on billing cycle customizations see the Create a setup token endpoint of the Payment Method Tokens v3 API.

- Use `paypal` as the `payment_source`. Pass additional parameters in the `paypal` object for your use case and business.
- Pass the `usage_pattern` and `billing_plan` details using the `payment_source.paypal` object. These are the details that the payer sees on the PayPal review page.
- Update the `return_url` value with the URL where the payer is redirected after they approve the flow.
- Update the `cancel_url` value with the URL where the payer is redirected after they cancel the flow.
- By default, the setup token expires after 3 days. After the payer completes the approval flow, you can upgrade the setup token to a full payment method token by calling the Create payment token for a given payment source endpoint of the Payment Method Tokens v3 API.

Interactive configuration options:
- Company: plan name
- usage_pattern: Subscription Prepaid (example)
- Pricing Model: Fixed
- Frequency: Monthly
- Duration of billing cycle: 1
- Total cycles: 1
- Start Date: 04/13/2026
- One time charges: Setup Fee, Shipping Amount, Taxes, Product Price
- Shipping information (optional): Full Name, Address Line 1, City, State, ZIP Code, Country Code

### Step 2. Get buyer approval

Get the buyer's approval for a recurring payment plan by sending a POST request to the Authorize payment for order endpoint of the Create Orders v2 API.

By default, the setup token expires after 3 days.

### Step 3. Create payment token

After the payer completes the approval flow, you can upgrade the setup token to a full payment method token by sending a POST call to the Create payment token for a given payment source endpoint of the Payment Method Tokens v3 API. The endpoint returns the payment source details, links, payment token ID, and customer details.

- Use `token` as the `payment_source` and complete the rest of the source objects for your use case and business.
- Pass your setup token ID in the `payment_source` parameter and set the type as `SETUP_TOKEN`.
- Store the merchant payer ID aligned with your system to simplify the mapping of payer information between your system and PayPal. This is an optional field that returns the value shared in the response.

---

## 2. Use payment method token with checkout

After you create a payment method token, use the token instead of the payment method to create a purchase and capture the payment with the Create orders endpoint of the Orders v2 API. Use this to charge your buyers for their recurring payments.

- Use the ID of your payment method token as the `vault_id`.
- Specify intent to indicate whether to capture a payment immediately or authorize it for a payment later. Use `AUTHORIZE` for Auth-Capture.
- Add amount for the total order.
- Update `stored_credential` as the payment source for a vaulted payment method token to provide additional details for recurring transactions that include `usage_pattern`, `payment_initiator`, and `usage`.

Configuration options:
- Intent: CAPTURE
- Currency Code: USD
- Amount: 100
- Payment Tokens: (select a payment token)

---

## 3. Configure your integration

### Step 1. Configure your script parameters

Country and currency:
- The Buyer Country field is intended solely for sandbox testing purposes and should not be utilized in production environments.
- Buyer Country: United States Of America
- Currency: USD

### Step 2. Configure the layout of the Buttons component (OPTIONAL)

Depending on where you want these buttons to show up on your website, you can lay out the buttons in a horizontal or vertical stack. You can also customize the buttons with different colors and shapes.

To override the default style settings for your page, use a `style` object inside the `Buttons` component.

Options:
- Button Shape: Rectangle | Pill
- Button Color: Gold (default) | others
- Button Layout: Vertical | Horizontal
- Button Label Text: PayPal (default) | others
- Button Message: Enable | Disable

---

## Code Samples

### index.html (front end)

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>PayPal JS SDK Standard Integration</title>
    </head>
    <body>
        <div id="paypal-button-container"></div>
        <p id="result-message"></p>

        <!-- Initialize the JS-SDK -->
        <script
            src="https://www.paypal.com/sdk/js?client-id=test&buyer-country=US&currency=USD&components=buttons"
            data-sdk-integration-source="developer-studio"
        ></script>
        <script src="app.js"></script>
    </body>
</html>
```

### app.js (front end)

```javascript
const paypalButtons = window.paypal.Buttons({
    style: {
        shape: "rect",
        layout: "vertical",
        color: "gold",
        label: "paypal",
    },
    async createVaultSetupToken() {
        try {
            const response = await fetch("/api/vault", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                // use the "body" param to optionally pass additional token information
                body: JSON.stringify({
                    payment_source: {
                        paypal: {
                            usage_type: "MERCHANT",
                            experience_context: {
                                return_url: "https://example.com/returnUrl",
                                cancel_url: "https://example.com/cancelUrl",
                            },
                        },
                    },
                }),
            });

            const setupTokenData = await response.json();

            if (setupTokenData.id) {
                return setupTokenData.id;
            }
            const errorDetail = setupTokenData?.details?.[0];
            const errorMessage = errorDetail
                ? `${errorDetail.issue} ${errorDetail.description} (${setupTokenData.debug_id})`
                : JSON.stringify(setupTokenData);

            throw new Error(errorMessage);
        } catch (error) {
            console.error(error);
            // resultMessage(`Could not create Setup token...<br><br>${error}`);
        }
    },
    async onApprove(data, actions) {
        try {
            const response = await fetch(`/api/vault/payment-tokens`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: {
                    payment_source: {
                        token: {
                            id: data.vaultSetupToken,
                            type: "SETUP_TOKEN",
                        },
                    },
                },
            });

            const paymentTokenData = await response.json();
            const errorDetail = paymentTokenData?.details?.[0];

            if (errorDetail) {
                throw new Error(
                    `${errorDetail.description} (${paymentTokenData.debug_id})`
                );
            } else {
                console.log(
                    "Payment Token",
                    paymentTokenData,
                    JSON.stringify(paymentTokenData, null, 2)
                );
            }
        } catch (error) {
            console.error(error);
            resultMessage(
                `Sorry, could not create tokenized payment source...<br><br>${error}`
            );
        }
    },
});

// Example function to show a result to the user. Your site's UI library can be used instead.
function resultMessage(message) {
    const container = document.querySelector("#result-message");
    container.innerHTML = message;
}
```

### server.js (Node.js backend)

```javascript
import express from "express";
import "dotenv/config";
import {
    ApiError,
    CheckoutPaymentIntent,
    Client,
    Environment,
    LogLevel,
    OrdersController,
    VaultController,
} from "@paypal/paypal-server-sdk";
import bodyParser from "body-parser";

const app = express();
app.use(bodyParser.json());

const {
    PAYPAL_CLIENT_ID,
    PAYPAL_CLIENT_SECRET,
    PORT = 8080,
} = process.env;

const client = new Client({
    clientCredentialsAuthCredentials: {
        oAuthClientId: PAYPAL_CLIENT_ID,
        oAuthClientSecret: PAYPAL_CLIENT_SECRET,
    },
    timeout: 0,
    environment: Environment.Sandbox,
    logging: {
        logLevel: LogLevel.Info,
        logRequest: { logBody: true },
        logResponse: { logHeaders: true },
    },
});

const ordersController = new OrdersController(client);
const paymentsController = new PaymentsController(client);
const vaultController = new VaultController(client);

/**
 * Create a setup token from the given payment source and adds it to the Vault of the associated customer.
 * @see https://developer.paypal.com/docs/api/payment-tokens/v3/#setup-tokens_create
 */
const createVaultSetupToken = async () => {
    const collect = {
        /* Unique identifier for your request to maintain idempotency */
        paypalRequestId: uuidv4(),
        body: {
            paymentSource: {
                paypal: {
                    usage_type: "MERCHANT",
                    usage_pattern: "SUBSCRIPTION_PREPAID",
                    billing_plan: {
                        billing_cycles: [
                            {
                                tenure_type: "REGULAR",
                                pricing_scheme: {
                                    pricing_model: "FIXED",
                                    price: {
                                        value: "100",
                                        currency_code: "USD",
                                    },
                                },
                                frequency: {
                                    interval_unit: "MONTH",
                                    interval_count: "1",
                                },
                                total_cycles: "1",
                                start_date: "2026-04-13",
                            },
                        ],
                        one_time_charges: {
                            product_price: {
                                value: "10",
                                currency_code: "USD",
                            },
                            total_amount: {
                                value: 10,
                                currency_code: "USD",
                            },
                        },
                        product: {
                            description: "Yearly Membership",
                            quantity: "1",
                        },
                        name: "Company",
                    },
                    experience_context: {
                        return_url: "https://example.com/returnUrl",
                        cancel_url: "https://example.com/cancelUrl",
                    },
                },
            },
        },
    };
    try {
        const { result, ...httpResponse } =
            await vaultController.setupTokensCreate(collect);
        return {
            jsonResponse: JSON.parse(body),
            httpStatusCode: httpResponse.statusCode,
        };
    } catch (error) {
        if (error instanceof ApiError) {
            throw new Error(error.message);
        }
    }
};

// setupTokensCreate route
app.post("/api/vault", async (req, res) => {
    try {
        const { jsonResponse, httpStatusCode } = await createVaultSetupToken();
        res.status(httpStatusCode).json(jsonResponse);
    } catch (error) {
        console.error("Failed to set up vault token:", error);
        res.status(500).json({ error: "Failed to set up vault token." });
    }
});

/**
 * Creates a Payment Token from the given payment source and adds it to the Vault of the associated customer.
 * @see https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_create
 */
const createPaymentToken = async () => {
    const collect = {
        /* Unique identifier for your request to maintain idempotency */
        paypalRequestId: uuidv4(),
        body: {
            paymentSource: {},
        },
    };
    try {
        const { result, ...httpResponse } =
            await vaultController.paymentTokensCreate(collect);
        return {
            jsonResponse: JSON.parse(body),
            httpStatusCode: httpResponse.statusCode,
        };
    } catch (error) {
        if (error instanceof ApiError) {
            throw new Error(error.message);
        }
    }
};

// paymentTokensCreate route
app.post("/api/vault/payment-tokens", async (req, res) => {
    try {
        const { jsonResponse, httpStatusCode } = await createPaymentToken();
        res.status(httpStatusCode).json(jsonResponse);
    } catch (error) {
        console.error("Failed to create payment token:", error);
        res.status(500).json({ error: "Failed to create payment token." });
    }
});

/**
 * Create an order utilizing the payment token.
 * @see https://developer.paypal.com/docs/api/orders/v2/#orders_create
 */
const createOrder = async (cart) => {
    const collect = {
        body: {
            intent: "CAPTURE",
            purchaseUnits: [
                {
                    amount: {
                        currencyCode: "USD",
                        value: "100",
                    },
                },
            ],
            payment_source: {
                paypal: {
                    vault_id: "PAYMENT-TOKEN-ID",
                    stored_credential: {
                        payment_initiator: "MERCHANT",
                        usage: "SUBSEQUENT",
                        usage_pattern: "RECURRING_POSTPAID",
                    },
                },
            },
        },
        prefer: "return=minimal",
    };

    try {
        const { body, ...httpResponse } = await ordersController.ordersCreate(
            collect
        );
        return {
            jsonResponse: JSON.parse(body),
            httpStatusCode: httpResponse.statusCode,
        };
    } catch (error) {
        if (error instanceof ApiError) {
            throw new Error(error.message);
        }
    }
};

// createOrder route
app.post("/api/orders", async (req, res) => {
    try {
        const { cart } = req.body;
        const { jsonResponse, httpStatusCode } = await createOrder(cart);
        res.status(httpStatusCode).json(jsonResponse);
    } catch (error) {
        console.error("Failed to create order:", error);
        res.status(500).json({ error: "Failed to create order." });
    }
});

app.listen(PORT, () => {
    console.log(`Node server listening at http://localhost:${PORT}/`);
});
```
