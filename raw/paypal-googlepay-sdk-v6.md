<!-- Source URL: https://docs.paypal.ai/payments/methods/google-pay/integrate -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrate Google Pay with PayPal's JavaScript SDK v6

Google Pay enables merchants to accept fast payments in using PayPal's Javascript SDK v6. This integration supports setup in test and production environments and provides a streamlined checkout experience for customers.

## Prerequisites

Before beginning your integration, meet these requirements:

- Create a [PayPal developer account](https://developer.paypal.com/dashboard/) and enable Google Pay in your sandbox settings.
- Enable Google Pay in your PayPal sandbox account. See [Set up your sandbox account to accept Google Pay](https://developer.paypal.com/docs/checkout/apm/google-pay/#set-up-your-sandbox-account-to-accept-google-pay) for more information.
- Set up your PayPal sandbox credentials.

> **Note:** You'll use your sandbox credentials to create a `.env` file during the **Development setup**.

## Development setup

Configure your local development environment with the required dependencies and credentials. For reference, see this [Google Pay demo](https://github.com/paypal-examples/v6-web-sdk-sample-integration/tree/main/client/components/googlepayPayments/oneTimePayment/html).

1. Install project dependencies:

```bash theme={null}
cd client/components/googlePayPayments/oneTimePayment/html
npm install
```

2. Create environment configuration:

```bash theme={null}
# .env file
PAYPAL_SANDBOX_CLIENT_ID=your_client_id
PAYPAL_SANDBOX_CLIENT_SECRET=your_client_secret
```

3. Start the development server:

```bash theme={null}
npm start
```

To load the application, see `http://localhost:3000`.

## Implementation steps

Implement Google Pay by following the detailed steps.

### Step 1: HTML structure setup

Create your basic HTML page and include the Google Pay and PayPal SDK scripts.

```html theme={null}
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>One-Time Payment - Google Pay - PayPal JavaScript SDK</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
  </head>
  <body>
    <h1>One-Time Payment Google Pay Integration</h1>

    <div class="buttons-container">
      <div id="googlepay-button-container"></div>
    </div>

    <!-- Load Google Pay SDK -->
    <script src="https://pay.google.com/gp/p/js/pay.js"></script>
    <script src="app.js"></script>

    <!-- Load PayPal SDK -->
    <script
      async
      src="https://www.sandbox.paypal.com/web-sdk/v6/core"
      onload="onPayPalWebSdkLoaded()"
    ></script>
  </body>
</html>
```

### Step 2: Initialize PayPal SDK

Set up the PayPal SDK with Google Pay components once it loads.

```javascript theme={null}
async function onPayPalWebSdkLoaded() {
  try {
    // Create PayPal SDK instance with Google Pay component
    const sdkInstance = await window.paypal.createInstance({
      clientId: "YOUR_CLIENT_ID",
      components: ["googlepay-payments"],
      pageType: "checkout",
    });

    setupGooglePayButton(sdkInstance);
  } catch (error) {
    console.error(error);
  }
}
```

### Step 3: Configure Google Pay button

Create the Google Pay session and set up the payment button.

```javascript theme={null}
async function setupGooglePayButton(sdkInstance) {
  // Create Google Pay session
  const googlePaySession = sdkInstance.createGooglePayOneTimePaymentSession();
  const purchaseAmount = "10.00";

  try {
    // Initialize Google Pay client
    const paymentsClient = new google.payments.api.PaymentsClient({
      environment: "TEST", // Use "PRODUCTION" for live transactions
      paymentDataCallbacks: {
        onPaymentAuthorized: (paymentData) =>
          onPaymentAuthorized(purchaseAmount, paymentData, googlePaySession),
      },
    });

    // Get Google Pay configuration from PayPal
    const googlePayConfig = await googlePaySession.getGooglePayConfig();

    // Check if Google Pay is available
    const isReadyToPay = await paymentsClient.isReadyToPay({
      allowedPaymentMethods: googlePayConfig.allowedPaymentMethods,
      apiVersion: googlePayConfig.apiVersion,
      apiVersionMinor: googlePayConfig.apiVersionMinor,
    });

    if (isReadyToPay.result) {
      // Create and append Google Pay button
      const button = paymentsClient.createButton({
        onClick: () =>
          onGooglePayButtonClick(
            purchaseAmount,
            paymentsClient,
            googlePayConfig,
          ),
      });

      document.getElementById("googlepay-button-container").appendChild(button);
    }
  } catch (error) {
    console.error("Setup error:", error);
  }
}
```

### Step 4: Configure payment data request

Set up the Google Pay payment data request with transaction details.

```javascript theme={null}
async function getGooglePaymentDataRequest(purchaseAmount, googlePayConfig) {
  const {
    allowedPaymentMethods,
    merchantInfo,
    apiVersion,
    apiVersionMinor,
    countryCode,
  } = googlePayConfig;

  const baseRequest = {
    apiVersion,
    apiVersionMinor,
  };

  const paymentDataRequest = Object.assign({}, baseRequest);
  paymentDataRequest.allowedPaymentMethods = allowedPaymentMethods;
  paymentDataRequest.transactionInfo = getGoogleTransactionInfo(
    purchaseAmount,
    countryCode,
  );
  paymentDataRequest.merchantInfo = merchantInfo;
  paymentDataRequest.callbackIntents = ["PAYMENT_AUTHORIZATION"];

  return paymentDataRequest;
}
```

### Step 5: Set up transaction information

Define the transaction details and pricing breakdown for the Google Pay request.

```javascript theme={null}
function getGoogleTransactionInfo(purchaseAmount, countryCode) {
  const totalAmount = parseFloat(purchaseAmount);
  const subtotal = (totalAmount * 0.9).toFixed(2);
  const tax = (totalAmount * 0.1).toFixed(2);

  return {
    displayItems: [
      {
        label: "Subtotal",
        type: "SUBTOTAL",
        price: subtotal,
      },
      {
        label: "Tax",
        type: "TAX",
        price: tax,
      },
    ],
    countryCode: countryCode,
    currencyCode: "USD",
    totalPriceStatus: "FINAL",
    totalPrice: purchaseAmount,
    totalPriceLabel: "Total",
  };
}
```

### Step 6: Handle payment authorization

Process the payment authorization and complete the transaction.

```javascript theme={null}
async function onPaymentAuthorized(
  purchaseAmount,
  paymentData,
  googlePaySession,
) {
  try {
    // Create PayPal order payload
    const orderPayload = getPayPalOrderPayload(purchaseAmount);
    const id = await createOrder(orderPayload);

    // Confirm order with Google Pay payment data
    const { status } = await googlePaySession.confirmOrder({
      orderId: id,
      paymentMethodData: paymentData.paymentMethodData,
    });

    if (status !== "PAYER_ACTION_REQUIRED") {
      // Capture the order
      const orderData = await captureOrder({ orderId: id });
      console.log(JSON.stringify(orderData, null, 2));
    }

    return { transactionState: "SUCCESS" };
  } catch (err) {
    console.error("Payment authorization error:", err);
    return {
      transactionState: "ERROR",
      error: {
        message: err.message,
      },
    };
  }
}
```

### Step 7: PayPal order configuration

Configure a PayPal order with the Google Pay payment source.

```javascript theme={null}
function getPayPalOrderPayload(purchaseAmount) {
  return {
    intent: "CAPTURE",
    purchaseUnits: [
      {
        amount: {
          currencyCode: "USD",
          value: purchaseAmount,
          breakdown: {
            itemTotal: {
              currencyCode: "USD",
              value: purchaseAmount,
            },
          },
        },
      },
    ],
    paymentSource: {
      googlePay: {
        attributes: {
          verification: {
            method: "SCA_WHEN_REQUIRED",
          },
        },
      },
    },
  };
}
```

## API endpoints

The integration requires these server-side endpoints.

### Create order endpoint

```javascript theme={null}
// POST /paypal-api/checkout/orders/create
async function createOrder(orderPayload) {
  const response = await fetch("/paypal-api/checkout/orders/create", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(orderPayload),
  });
  const { id } = await response.json();
  return id;
}
```

### Capture order endpoint

```javascript theme={null}
// POST /paypal-api/checkout/orders/{orderId}/capture
async function captureOrder({ orderId }) {
  const response = await fetch(
    `/paypal-api/checkout/orders/${orderId}/capture`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    },
  );
  const data = await response.json();
  return data;
}
```

## Key components

<table>
  <thead>
    <tr>
      <th>Key component</th>
      <th>Purpose</th>
      <th>Details</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><strong>PayPal SDK instance</strong></td>
      <td>Main entry point for PayPal functionality</td>

      <td>
        <ul>
          <li>Includes <code>googlepay-payments</code> component</li>
          <li>Authenticate with your client ID</li>
        </ul>
      </td>
    </tr>

    <tr>
      <td><strong>Google Pay session</strong></td>
      <td>Manages Google Pay payment flow</td>

      <td>
        <ul>
          <li>Provides Google Pay–specific settings</li>
          <li>Handles order confirmation and capture</li>
        </ul>
      </td>
    </tr>

    <tr>
      <td><strong>Google Pay client</strong></td>
      <td>Interface with Google Pay API</td>

      <td>
        <ul>
          <li>Set to <code>TEST</code> for sandbox</li>
          <li>Set to <code>PRODUCTION</code> for live</li>
          <li>Handles payment authorization callbacks</li>
        </ul>
      </td>
    </tr>

  </tbody>
</table>

## Security considerations

- Never expose client secrets in frontend code.
- Always process payments through PayPal’s servers.
- Use HTTPS in production.

## Error handling

- Catch and log errors in both client and server code.
- Avoid logging sensitive data.
- Show clear, user-friendly error messages.

## Testing

- Run transactions with different payment amounts.
- Verify order creation and capture flows.
- Simulate error scenarios and edge cases.

## Next steps

1. Configure your production credentials and endpoints.
2. Add 3D Secure (3DS) support if required.
3. Extend your integration to support multiple currencies.
4. Strengthen error handling and customer messaging.
5. Build a complete automated test suite.

## Resources

- [One-time payments Google Pay sample integration](https://github.com/paypal-examples/v6-web-sdk-sample-integration)
- [Integrate Google Pay with the PayPal Javascript SDK v5](https://developer.paypal.com/docs/checkout/apm/google-pay/)
- [Google Pay Web API](https://developers.google.com/pay/api/web/overview)
- [PayPal Developer Dashboard](https://developer.paypal.com/dashboard/)
