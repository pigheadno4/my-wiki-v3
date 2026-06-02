<!-- Source URL: https://developer.paypal.com/docs/checkout/expanded/integrate/ -->
<!-- Fetched: 2026-04-13 -->

Online / Checkout / Expanded / Integrate

# Integrate Expanded PayPal Checkout

Important: These are the integration instructions for the JavaScript SDK component **CardFields**. If your integration uses the HostedFields component, see Integrate PayPal buttons and Hosted Fields instead.

Before beginning your integration, you need to set up your development environment. You can refer to this flow diagram, and watch a video demonstrating how to integrate PayPal Expanded Checkout.

---

## 1. Integrate front end (CLIENT)

### Front-end process

- Your app shows the PayPal card fields and payment buttons
- Your app calls server endpoints to create the order and capture the payment. The request details depend on a number of factors, such as the type of payment method, and SDK component.

### Front-end code

The `/src/index.html` and `/src/app.js` files handle the client-side logic and define how the PayPal front-end components connect with the back end.

You'll need to:
- Save the `index.html` file in a folder named `/src`.
- Save the `app.js` file in a folder named `/src`.

### Step 1. Initialize JavaScript SDK

Add the JavaScript SDK to your web page and include the following:
- Your app's client ID.
- A `<div>` to render the PayPal buttons.
- A `<div>` to render each of the card fields.

Pass a `client-id` and specify which components you want to use. This sample includes `buttons,card-fields` in the `components` parameter.

### Step 2: Render Card fields and PayPal buttons

#### Card Fields

The `paypal` namespace has a `CardFields` component to accept and save cards without handling card information. PayPal handles all security and compliance.

- Set up `cardField.isEligible()` for each card field to determine if a payment is eligible.
- Render each card field by declaring it as an object in `cardField` and applying a `.render()` function.
- Create the order by calling the `createOrder` function.
- Add an event listener for when the payer submits an eligible card payment.
- Pass the card field values (cardholder name, billing address) to the submit function. Anything passed into `submit()` is sent to the iframe that communicates with the Orders API.

#### PayPal Buttons

The `paypal` namespace has a `Buttons` function that initiates the callbacks needed to set up a payment.

- Declare a `createOrder` callback that returns an order ID.
- Completing the payment launches an `onApprove` callback.
- Handle the payment capture response (success, `INSTRUMENT_DECLINED`, error).

### Step 3: Customize the Card Fields (OPTIONAL)

- Configure the layout of the card fields.
- Include required card form elements: card number, security code, expiration date.
- Add your own fields to accept billing address information.
- Optional: Change layout, width, height, and outer styling.

### Step 4. Configure the layout of the Buttons component (OPTIONAL)

Button Shape: Rectangle | Pill
Button Color: Gold (default)
Button Layout: Vertical | Horizontal
Button Label: PayPal (default)
Button Message: Enable | Disable

### Integrate 3D Secure using JavaScript SDK

To trigger 3D Secure authentication, pass the verification method in the Create order payload:

- `SCA_ALWAYS` — trigger authentication for every transaction
- `SCA_WHEN_REQUIRED` — trigger only when required by regional compliance (e.g. PSD2; supported only in PSD2 mandate countries)

---

## 2. Integrate back end (SERVER)

### Backend process

- Your app creates an order on the backend by calling `ordersCreate` in the Orders Controller.
- Your app calls `ordersCapture` in the Orders Controller to move money when the payer confirms.

### Backend Code

- Server runs on port 8080
- `PAYPAL_CLIENT_ID` and `PAYPAL_CLIENT_SECRET` as environment variables
- By default the server SDK connects to PayPal's sandbox API

---

## 3. Custom Integration

### Handle buyer checkout errors (optional)

Use `onError` callbacks and alternate checkout pages. `onError` is a catch-all handler.

### Handle funding failures (optional)

If the Orders API returns `INSTRUMENT_DECLINED`, restart the payment so the payer can select a different payment option.

### Refund a captured payment

Refund a captured payment from a seller back to a buyer.

---

## 4. Test integration

Before going live, test in the sandbox environment:
- Use test card numbers to simulate successful payments.
- Use rejection triggers to simulate card error scenarios.
- Test 3D Secure authentication scenarios.

---

## 5. Go live

- Log into the PayPal Developer Dashboard with your PayPal business account.
- Complete production onboarding to process card payments.
- Request Expanded Credit and Debit Card Payments for your business account.

---

## Code Samples

### index.html (front end)

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link
            rel="stylesheet"
            type="text/css"
            href="https://www.paypalobjects.com/webstatic/en_US/developer/docs/css/cardfields.css"
        />
        <title>PayPal JS SDK Advanced Integration - Checkout Flow</title>
        <script
            src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&buyer-country=US&currency=USD&components=buttons,card-fields&enable-funding=venmo"
            data-sdk-integration-source="developer-studio"
        ></script>
    </head>
    <body>
        <div id="paypal-button-container" class="paypal-button-container"></div>
        <!-- Containers for Card Fields hosted by PayPal -->
        <div id="card-form" class="card_container">
            <div id="card-name-field-container"></div>
            <div id="card-number-field-container"></div>
            <div id="card-expiry-field-container"></div>
            <div id="card-cvv-field-container"></div>

            <div>
                <label for="card-billing-address-line-1">Billing Address</label>
                <input type="text" id="card-billing-address-line-1" name="card-billing-address-line-1" autocomplete="off" placeholder="Address line 1" />
            </div>
            <div>
                <input type="text" id="card-billing-address-line-2" name="card-billing-address-line-2" autocomplete="off" placeholder="Address line 2" />
            </div>
            <div>
                <input type="text" id="card-billing-address-admin-area-line-1" name="card-billing-address-admin-area-line-1" autocomplete="off" placeholder="Admin area line 1" />
            </div>
            <div>
                <input type="text" id="card-billing-address-admin-area-line-2" name="card-billing-address-admin-area-line-2" autocomplete="off" placeholder="Admin area line 2" />
            </div>
            <div>
                <input type="text" id="card-billing-address-country-code" name="card-billing-address-country-code" autocomplete="off" placeholder="Country code" />
            </div>
            <div>
                <input type="text" id="card-billing-address-postal-code" name="card-billing-address-postal-code" autocomplete="off" placeholder="Postal/zip code" />
            </div>

            <br /><br />
            <button id="card-field-submit-button" type="button">Pay now with Card</button>
        </div>
        <p id="result-message"></p>
        <script src="app.js"></script>
    </body>
</html>
```

### app.js (front end)

```javascript
// Render the button component
paypal
    .Buttons({
        createOrder: createOrderCallback,
        onApprove: onApproveCallback,
        onError: function (error) {
            // Do something with the error from the SDK
        },
        style: {
            shape: "rect",
            layout: "vertical",
            color: "gold",
            label: "paypal",
        },
        message: {
            amount: 100,
        },
    })
    .render("#paypal-button-container");

// Render each field after checking for eligibility
const cardField = window.paypal.CardFields({
    createOrder: createOrderCallback,
    onApprove: onApproveCallback,
    style: {
        input: {
            "font-size": "16px",
            "font-family": "courier, monospace",
            "font-weight": "lighter",
            color: "#ccc",
        },
        ".invalid": { color: "purple" },
    },
    onError: (err) => {
        window.location.assign("/your-error-page-here");
    },
});

if (cardField.isEligible()) {
    const nameField = cardField.NameField({
        style: { input: { color: "blue" }, ".invalid": { color: "purple" } },
    });
    nameField.render("#card-name-field-container");

    const numberField = cardField.NumberField({
        style: { input: { color: "blue" } },
    });
    numberField.render("#card-number-field-container");

    const cvvField = cardField.CVVField({
        style: { input: { color: "blue" } },
    });
    cvvField.render("#card-cvv-field-container");

    const expiryField = cardField.ExpiryField({
        style: { input: { color: "blue" } },
    });
    expiryField.render("#card-expiry-field-container");

    // Add click listener to submit button
    document
        .getElementById("card-field-submit-button")
        .addEventListener("click", () => {
            cardField
                .submit({
                    billingAddress: {
                        addressLine1: document.getElementById("card-billing-address-line-1").value,
                        addressLine2: document.getElementById("card-billing-address-line-2").value,
                        adminArea1: document.getElementById("card-billing-address-admin-area-line-1").value,
                        adminArea2: document.getElementById("card-billing-address-admin-area-line-2").value,
                        countryCode: document.getElementById("card-billing-address-country-code").value,
                        postalCode: document.getElementById("card-billing-address-postal-code").value,
                    },
                })
                .then(() => {
                    // submit successful
                });
        });
}

async function createOrderCallback() {
    resultMessage("");
    try {
        const response = await fetch("/api/orders", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                cart: [{ id: "YOUR_PRODUCT_ID", quantity: "YOUR_PRODUCT_QUANTITY" }],
            }),
        });

        const orderData = await response.json();

        if (orderData.id) {
            return orderData.id;
        } else {
            const errorDetail = orderData?.details?.[0];
            const errorMessage = errorDetail
                ? `${errorDetail.issue} ${errorDetail.description} (${orderData.debug_id})`
                : JSON.stringify(orderData);
            throw new Error(errorMessage);
        }
    } catch (error) {
        console.error(error);
        resultMessage(`Could not initiate PayPal Checkout...<br><br>${error}`);
    }
}

async function onApproveCallback(data, actions) {
    try {
        const response = await fetch(`/api/orders/${data.orderID}/capture`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
        });

        const orderData = await response.json();

        const transaction =
            orderData?.purchase_units?.[0]?.payments?.captures?.[0] ||
            orderData?.purchase_units?.[0]?.payments?.authorizations?.[0];
        const errorDetail = orderData?.details?.[0];

        // NOTE: actions.restart() only applies to Buttons component, NOT card payments
        if (errorDetail?.issue === "INSTRUMENT_DECLINED" && !data.card && actions) {
            // (1) Recoverable INSTRUMENT_DECLINED for Buttons -> restart()
            return actions.restart();
        } else if (errorDetail || !transaction || transaction.status === "DECLINED") {
            // (2) Non-recoverable errors
            let errorMessage;
            if (transaction) {
                errorMessage = `Transaction ${transaction.status}: ${transaction.id}`;
            } else if (errorDetail) {
                errorMessage = `${errorDetail.description} (${orderData.debug_id})`;
            } else {
                errorMessage = JSON.stringify(orderData);
            }
            throw new Error(errorMessage);
        } else {
            // (3) Successful transaction
            resultMessage(
                `Transaction ${transaction.status}: ${transaction.id}<br><br>See console for all available details`
            );
            console.log("Capture result", orderData, JSON.stringify(orderData, null, 2));
        }
    } catch (error) {
        console.error(error);
        resultMessage(`Sorry, your transaction could not be processed...<br><br>${error}`);
    }
}

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
    Client,
    Environment,
    LogLevel,
    OrdersController,
    PaymentsController,
} from "@paypal/paypal-server-sdk";
import bodyParser from "body-parser";

const app = express();
app.use(bodyParser.json());

const { PAYPAL_CLIENT_ID, PAYPAL_CLIENT_SECRET, PORT = 8080 } = process.env;

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

/**
 * Create an order to start the transaction.
 * @see https://developer.paypal.com/docs/api/orders/v2/#orders_create
 */
const createOrder = async (cart) => {
    const payload = {
        body: {
            intent: "CAPTURE",
            purchaseUnits: [{
                amount: { currencyCode: "USD", value: "100" },
            }],
            paymentSource: {
                card: {
                    attributes: {
                        verification: {
                            method: "SCA_ALWAYS",
                        },
                    },
                },
            },
        },
        prefer: "return=minimal",
    };

    try {
        const { body, ...httpResponse } = await ordersController.createOrder(payload);
        return { jsonResponse: JSON.parse(body), httpStatusCode: httpResponse.statusCode };
    } catch (error) {
        if (error instanceof ApiError) throw new Error(error.message);
    }
};

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

/**
 * Capture payment for the created order.
 * @see https://developer.paypal.com/docs/api/orders/v2/#orders_capture
 */
const captureOrder = async (orderID) => {
    const collect = { id: orderID, prefer: "return=minimal" };
    try {
        const { body, ...httpResponse } = await ordersController.captureOrder(collect);
        return { jsonResponse: JSON.parse(body), httpStatusCode: httpResponse.statusCode };
    } catch (error) {
        if (error instanceof ApiError) throw new Error(error.message);
    }
};

app.post("/api/orders/:orderID/capture", async (req, res) => {
    try {
        const { orderID } = req.params;
        const { jsonResponse, httpStatusCode } = await captureOrder(orderID);
        res.status(httpStatusCode).json(jsonResponse);
    } catch (error) {
        console.error("Failed to create order:", error);
        res.status(500).json({ error: "Failed to capture order." });
    }
});

/**
 * Authorize payment for the created order.
 * @see https://developer.paypal.com/docs/api/orders/v2/#orders_authorize
 */
const authorizeOrder = async (orderID) => {
    const collect = { id: orderID, prefer: "return=minimal" };
    try {
        const { body, ...httpResponse } = await ordersController.authorizeOrder(collect);
        return { jsonResponse: JSON.parse(body), httpStatusCode: httpResponse.statusCode };
    } catch (error) {
        if (error instanceof ApiError) throw new Error(error.message);
    }
};

app.post("/api/orders/:orderID/authorize", async (req, res) => {
    try {
        const { orderID } = req.params;
        const { jsonResponse, httpStatusCode } = await authorizeOrder(orderID);
        res.status(httpStatusCode).json(jsonResponse);
    } catch (error) {
        console.error("Failed to create order:", error);
        res.status(500).json({ error: "Failed to authorize order." });
    }
});

/**
 * Captures an authorized payment, by ID.
 * @see https://developer.paypal.com/docs/api/payments/v2/#authorizations_capture
 */
const captureAuthorize = async (authorizationId) => {
    const collect = {
        authorizationId: authorizationId,
        prefer: "return=minimal",
        body: { finalCapture: false },
    };
    try {
        const { body, ...httpResponse } = await paymentsController.captureAuthorize(collect);
        return { jsonResponse: JSON.parse(body), httpStatusCode: httpResponse.statusCode };
    } catch (error) {
        if (error instanceof ApiError) throw new Error(error.message);
    }
};

app.post("/orders/:authorizationId/captureAuthorize", async (req, res) => {
    try {
        const { authorizationId } = req.params;
        const { jsonResponse, httpStatusCode } = await captureAuthorize(authorizationId);
        res.status(httpStatusCode).json(jsonResponse);
    } catch (error) {
        console.error("Failed to create order:", error);
        res.status(500).json({ error: "Failed to capture authorize." });
    }
});

const refundCapturedPayment = async (capturedPaymentId) => {
    const collect = { captureId: capturedPaymentId, prefer: "return=minimal" };
    try {
        const { body, ...httpResponse } = await paymentsController.refundCapturedPayment(collect);
        return { jsonResponse: JSON.parse(body), httpStatusCode: httpResponse.statusCode };
    } catch (error) {
        if (error instanceof ApiError) throw new Error(error.message);
    }
};

app.post("/api/payments/refund", async (req, res) => {
    try {
        const { capturedPaymentId } = req.body;
        const { jsonResponse, httpStatusCode } = await refundCapturedPayment(capturedPaymentId);
        res.status(httpStatusCode).json(jsonResponse);
    } catch (error) {
        console.error("Failed refund captured payment:", error);
        res.status(500).json({ error: "Failed refund captured payment." });
    }
});

app.listen(PORT, () => {
    console.log(`Node server listening at http://localhost:${PORT}/`);
});
```
