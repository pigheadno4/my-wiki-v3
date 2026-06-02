<!-- Source URL: https://developer.paypal.com/studio/checkout/standard/integrate -->
<!-- Fetched: 2026-04-13 -->

Online / Checkout / PayPal / Integrate / One-time Payment

Note: Get the latest on our platform's capabilities and best practices by exploring our new documentation site.

# Integrate PayPal Checkout

Before beginning your integration, you need to set up your development environment. You can refer to this flow diagram, and watch a video demonstrating how to integrate PayPal Checkout.

Start your integration by grabbing the sample code from PayPal's GitHub repo, or visiting the PayPal GitHub Codespace. Read the Codespaces guide for more information. You can also use Postman to explore and test PayPal APIs. Read the Postman Guide for more information.

[Download sample code] [Open in Codespaces] [Run in Postman]

---

## 1. Integrate front end (CLIENT)

Set up your front end to integrate checkout payments.

### Front-end process
- Your app shows the PayPal checkout buttons.
- Your app calls server endpoints to create the order and capture payment.

### Front-end code
This example uses a `index.html` file to show how to set up the front end to integrate payments.

The `/src/index.html` and `/src/app.js` files handle the client-side logic and define how the PayPal front-end components connect with the back end. Use these files to set up the PayPal checkout using the JavaScript SDK and handle the payer's interactions with the PayPal checkout button.

You'll need to:
- Save the `index.html` file in a folder named `/src`.
- Save the `app.js` file in a folder named `/src`.

### Step 1. Add the script tag

Include the `<script>` tag on any page that shows the PayPal buttons. This script will fetch all the necessary JavaScript to access the buttons on the window object.

### Step 2. Configure your script parameters

The snippet in Step 1 shows that you need to pass a `client-id` and specify which components you want to use. The SDK offers Buttons, Marks, Card Fields, and other components. This sample focuses on the buttons component.

In addition to passing the `client-id` and specifying which components you want to use, you can also pass the currency you want to use for pricing. For this exercise, we'll use USD.

> Buyer Country and Currency are only for use in sandbox testing. These are not to be used in production.

Parameters:
- `client-id`: your PayPal app client ID
- `buyer-country`: e.g. US (sandbox only)
- `currency`: e.g. USD
- `components`: e.g. buttons
- `enable-funding`: e.g. venmo,paylater,card

NOTE: Learn more about Funding eligibility in the JS SDK documentation. See `disable-funding` and `enable-funding` for more details.

### Step 3. Render the PayPal buttons

After setting up the SDK for your website, you need to render the buttons.

The `paypal` namespace has a `Buttons` function that initiates the callbacks needed to set up a payment.

The `createOrder` callback launches when the customer clicks the payment button. The callback starts the order and returns an order ID. After the customer checks out using the PayPal pop-up, this order ID helps you to confirm when the payment is completed.

Completing the payment launches an `onApprove` callback. Use the `onApprove` response to update business logic, show a celebration page, or handle error responses.

If your website handles shipping physical items, this documentation includes details about our shipping callbacks.

> Canadian merchants typically need to render a site in both English and French. To support this requirement, see Pay Later (CA).

### Step 4. Configure the layout of the Buttons component (OPTIONAL)

Depending on where you want these buttons to show up on your website, you can lay out the buttons in a horizontal or vertical stack. You can also customize the buttons with different colors and shapes.

To override the default style settings for your page, use a `style` object inside the `Buttons` component. Read more about how to customize your payment buttons in the style section of the JavaScript SDK reference page.

Options:
- Button Shape: Rectangle | Pill
- Button Color: Gold (default) | others
- Button Layout: Vertical | Horizontal
- Button Label Text: PayPal (default) | others
- Button Message: Enable | Disable

### Step 5. Support multiple shipping options (OPTIONAL)

The client-side shipping address and options callback process involves the following steps:

- The `onShippingAddressChange` callback is triggered when the buyer selects a new shipping address. Use the data in this callback to tell the buyer if you support the new shipping address, update shipping costs, and update the line items in the cart.
- The `onShippingOptionsChange` callback is triggered when the buyer selects a new shipping option. Use the data in this callback to tell the buyer if you support the new shipping method, update shipping costs, and update the line items in the cart.

Visit the JavaScript SDK reference page for more details about the `onShippingAddressChange` and `onShippingOptionsChange` callbacks.

### Contact Module (OPTIONAL)

Contact Module helps buyers view and modify the email and phone number shared with merchants for a given order. It offers flexibility to buyers, particularly for gift orders where buyers need to specify alternative contact details.

Merchant can pass an explicit indicator `contact_preference` in `payment_source.paypal.experience_context` object in a Create order request to determine if they want buyers to see and edit contact information on the PayPal checkout during the order review phase. PayPal supports three contact preferences:

- `NO_CONTACT_INFO` [Default]: Contact info module is hidden from the buyers and they cannot see or edit any contact information.
- `UPDATE_CONTACT_INFO`: Buyers will see the contact module and can add or update their contact details on the PayPal side. Once buyer updates their details, merchants will see the latest contact information as part of shipping email & phone.
- `RETAIN_CONTACT_INFO`: Buyers will see the contact module but they cannot edit their details on the PayPal side. Merchant is expected to collect buyer's contact details on their website and pass it in the create order call using `shipping.email_address` and `shipping.phone_number`.

---

## 2. Integrate back end (SERVER)

This section explains how to set up your backend to integrate PayPal checkout payments.

The PayPal Server SDK provides integration access to the PayPal REST APIs. The API endpoints are divided into distinct controllers:
- Orders Controller: Orders API v2
- Payments Controller: Payments API v2

### Backend process
- Your app creates an order on the backend by calling to the `ordersCreate` method in the Orders Controller. See Create Orders V2 API endpoint.
- Your app calls the `ordersCapture` method in the Orders Controller on the backend to move the money when the payer confirms the order. See Capture Payment for Order V2 API endpoint.

### Backend Code

The sample integration uses the PayPal Server SDK to connect to the PayPal REST APIs. Use the server folder to setup the backend to integrate with the payments flow.

- The server side code runs on port 8080
- Declare the `PAYPAL_CLIENT_ID` and `PAYPAL_CLIENT_SECRET` as environment variables. The server side code is configured to fetch these values from the environment to authorize the calls to the PayPal REST APIs.
- By default the server SDK clients are configured to connect to the PayPal's sandbox API.

### Step 1. Generate access token

Initialize the Server SDK client using OAuth 2.0 Client Credentials (`PAYPAL_CLIENT_ID` and `PAYPAL_CLIENT_SECRET`). The SDK will automatically retrieve the OAuth token when any endpoint that requires OAuth 2.0 Client Credentials is invoked.

### Step 2. Create Order

You need a `createOrder` function to start a payment between a payer and a merchant.

Set up the `createOrder` function to make a request to the `ordersCreate` method in the Orders Controller and pass data from the cart object to calculate the purchase units for the order.

See the Create order endpoint of the PayPal Orders v2 API for sample responses and other details.

- Intent: CAPTURE
- Currency Code: USD
- Amount: 100

If you process payments that require Strong Customer Authentication, you need to provide additional context with payment indicators.

### Step 3. Capture Payment

You need a `captureOrder` function to move money from the payer to the merchant.

Set up the `captureOrder` function to make a request to the `ordersCapture` method in the Orders Controller and pass the `orderID` generated from the Create Order step.

See the Capture Payment for Order V2 API endpoint for sample responses and other details.

---

## Enable App Switch

Note: To test the App Switch URL post-integration, open this URL in a mobile browser or other platform with an active installation of the PayPal mobile app.

### Client Side

Enable App Switch on the client side using the PayPal JavaScript SDK. You'll need to make 2 changes to integrate client-side:
1. Add the App Switch flag to the PayPal Buttons component setup.
2. Determine whether the buyer is returning from App Switch. If so, run `buttons.resume()` before rendering the button.

When you run the client-side Buttons component for App Switch, include the following declaration: `appSwitchWhenAvailable: true`.

See the Integrate client-side section of the App Switch page for more information.

#### Resume flow

When your app detects that the buyer is returning from App Switch, run `buttons.resume()` before rendering the button.

Note: You can set up a resume flow to help a buyer resume a transaction completed in a different window or browser tab.

### Server Side

Configure App Switch on the server side by making a POST call to the Create order endpoint of the Orders v2 API. You'll need to include the following 2 parameters in `payment_source.paypal.experience_context.app_switch_preference` object:

- `return_url`: This URL tells App Switch where to send the buyer after completing checkout on the PayPal app. Set the URL to the page where the buyer selected the PayPal button.
- `cancel_url`: This URL tells App Switch where to send the buyer when the buyer cancels or doesn't complete the transaction on the PayPal app. Set the URL to the page where the buyer selected the PayPal button.

The `return_url` and `cancel_url` must:
- Be the same.
- Match the URL of the page where the buyer selected the PayPal button.
- Contain a unique identifier for the buyer's session to identify the buyer when they return from App Switch.
- Not contain any hash value at the end.

---

## 3. Custom Integration (OPTIONAL)

### Handle buyer checkout errors

Use `onError` callbacks and alternate checkout pages to handle buyer checkout errors.

If an error prevents buyer checkout, alert the user that an error has occurred with the buttons using the `onError` callback. This error handler is a catch-all. Errors at this point are not expected to be handled beyond showing a generic error message or page.

If a null pointer error prevents the script from loading, provide a different checkout experience.

### Handle funding failures

If your payer's funding source fails, the Orders API returns an `INSTRUMENT_DECLINED` error. A funding source might fail because the billing address associated with the payment method is incorrect, the transaction exceeds the card limit, or the card issuer denies the transaction. To handle this error, restart the payment so the payer can select a different payment option.

### Show cancellation page

Show a page to your payers to confirm that the payment was cancelled.

### Refund a captured payment

Refund a captured payment from a seller back to a buyer.

---

## 4. Test integration

Before going live, test your integration in the sandbox environment. Learn more about card testing, simulating successful payments using test card numbers and generating card error scenarios using rejection triggers.

Note: Use the credit card generator to generate test credit cards for sandbox testing.

### Test the following use cases before going live:

#### PayPal Payment

Test a purchase as a payer:
1. Select the PayPal button on your checkout page.
2. Log in using one of your personal sandbox accounts. This ensures the payments will be sent to the correct account. Make sure that you use the sandbox business account that corresponds to the REST app you are using.
3. Note the purchase amount in the PayPal checkout window.
4. Approve the purchase with the Pay Now button. The PayPal window closes and redirects you to your page, indicating that the transaction was completed.

Confirm the money reached the business account:
1. Log in to the PayPal sandbox using the sandbox business account that received the payment. Remember that the SDK source now uses a sandbox client ID from one of your REST apps, and not the default test ID.
2. In Recent Activity, confirm that the sandbox business account received the money, subtracting any fees.
3. Log out of the account.

#### Card payment

1. Go to the checkout page for your integration.
2. Generate a test card using the credit card generator.
3. Enter the card details in the hosted field, including the name on the card, billing address, and 2-character country code. Then, submit the order.
4. Confirm that the order was processed.
5. Log in to your merchant sandbox account and navigate to the activity page to ensure the payment amount shows up in the account.

---

## 5. Go live

Follow this checklist to take your application live:
1. Log into the PayPal Developer Dashboard with your PayPal business account.
2. Obtain your live credentials.
3. Include the new credentials in your integration and Update your PayPal endpoint.

See Move your app to production for more details.

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
            src="https://www.paypal.com/sdk/js?client-id=test&buyer-country=US&currency=USD&components=buttons&enable-funding=venmo,paylater,card"
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
    message: {
        amount: 100,
    },
    async createOrder() {
        try {
            const response = await fetch("/api/orders", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                // use the "body" param to optionally pass additional order information
                // like product ids and quantities
                body: JSON.stringify({
                    cart: [
                        {
                            id: "YOUR_PRODUCT_ID",
                            quantity: "YOUR_PRODUCT_QUANTITY",
                        },
                    ],
                }),
            });

            const orderData = await response.json();

            if (orderData.id) {
                return orderData.id;
            }
            const errorDetail = orderData?.details?.[0];
            const errorMessage = errorDetail
                ? `${errorDetail.issue} ${errorDetail.description} (${orderData.debug_id})`
                : JSON.stringify(orderData);

            throw new Error(errorMessage);
        } catch (error) {
            console.error(error);
            // resultMessage(`Could not initiate PayPal Checkout...<br><br>${error}`);
        }
    },
    async onApprove(data, actions) {
        try {
            const response = await fetch(
                `/api/orders/${data.orderID}/capture`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                }
            );

            const orderData = await response.json();
            // Three cases to handle:
            //   (1) Recoverable INSTRUMENT_DECLINED -> call actions.restart()
            //   (2) Other non-recoverable errors -> Show a failure message
            //   (3) Successful transaction -> Show confirmation or thank you message

            const errorDetail = orderData?.details?.[0];

            if (errorDetail?.issue === "INSTRUMENT_DECLINED") {
                // (1) Recoverable INSTRUMENT_DECLINED -> call actions.restart()
                // recoverable state, per
                // https://developer.paypal.com/docs/checkout/standard/customize/handle-funding-failures/
                return actions.restart();
            } else if (errorDetail) {
                // (2) Other non-recoverable errors -> Show a failure message
                throw new Error(
                    `${errorDetail.description} (${orderData.debug_id})`
                );
            } else if (!orderData.purchase_units) {
                throw new Error(JSON.stringify(orderData));
            } else {
                // (3) Successful transaction -> Show confirmation or thank you message
                // Or go to another URL:  actions.redirect('thank_you.html');
                const transaction =
                    orderData?.purchase_units?.[0]?.payments?.captures?.[0] ||
                    orderData?.purchase_units?.[0]?.payments
                        ?.authorizations?.[0];
                resultMessage(
                    `Transaction ${transaction.status}: ${transaction.id}<br>
          <br>See console for all available details`
                );
                console.log(
                    "Capture result",
                    orderData,
                    JSON.stringify(orderData, null, 2)
                );
            }
        } catch (error) {
            console.error(error);
            resultMessage(
                `Sorry, your transaction could not be processed...<br><br>${error}`
            );
        }
    },

    onError: (err) => {
        // redirect to your specific error page
        window.location.assign("/your-error-page-here");
    },
    onCancel: (data) => {
        // Show a cancel page or return to cart
        window.location.assign("/your-error-page-here");
    },
    appSwitchWhenAvailable: true,
});
if (paypalButtons.hasReturned()) {
    paypalButtons.resume();
} else {
    paypalButtons.render("#paypal-button-container");
}

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
    PaymentsController,
    PaypalExperienceLandingPage,
    PaypalExperienceUserAction,
    ShippingPreference,
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

/**
 * Create an order to start the transaction.
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
                        breakdown: {
                            itemTotal: {
                                currencyCode: "USD",
                                value: "100",
                            },
                        },
                    },
                    // lookup item details in `cart` from database
                    items: [
                        {
                            name: "T-Shirt",
                            unitAmount: {
                                currencyCode: "USD",
                                value: "100",
                            },
                            quantity: "1",
                            description: "Super Fresh Shirt",
                            sku: "sku01",
                        },
                    ],
                    shipping: {
                        email_address: "buyer_shipping_email@example.com",
                        phone_number: {
                            country_code: "1",
                            national_number: "4081111111",
                        },
                    },
                },
            ],
            paymentSource: {
                paypal: {
                    experienceContext: {
                        userAction: PaypalExperienceUserAction.PayNow,
                        returnUrl:
                            "https://developer.paypal.com/studio/checkout/standard/integrate?appswitch=true",
                        cancelUrl:
                            "https://developer.paypal.com/studio/checkout/standard/integrate?appswitch=true",
                        appSwitchPreference: {
                            launchPaypalApp: true,
                        },
                        contactPreference: "NO_CONTACT_INFO",
                    },
                },
            },
        },
        prefer: "return=minimal",
    };

    try {
        const { body, ...httpResponse } = await ordersController.createOrder(
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

/**
 * Capture payment for the created order to complete the transaction.
 * @see https://developer.paypal.com/docs/api/orders/v2/#orders_capture
 */
const captureOrder = async (orderID) => {
    const collect = {
        id: orderID,
        prefer: "return=minimal",
    };

    try {
        const { body, ...httpResponse } = await ordersController.captureOrder(
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

// captureOrder route
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

const refundCapturedPayment = async (capturedPaymentId) => {
    const collect = {
        captureId: capturedPaymentId,
        prefer: "return=minimal",
    };

    try {
        const { body, ...httpResponse } =
            await paymentsController.refundCapturedPayment(collect);
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

// refundCapturedPayment route
app.post("/api/payments/refund", async (req, res) => {
    try {
        const { capturedPaymentId } = req.body;
        const { jsonResponse, httpStatusCode } = await refundCapturedPayment(
            capturedPaymentId
        );
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
