<!-- Source URL: https://docs.paypal.ai/payments/methods/apple-pay/integrate -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrate Apple Pay with PayPal's JavaScript SDK v6

With PayPal's JavaScript SDK v6, you can accept Apple Pay for secure, one-tap payments. You'll set up a test environment, add the needed frontend and backend, and then launch Apple Pay in both sandbox and production.

## Prerequisites

Before beginning your integration, meet these requirements:

- Create a [PayPal Developer account](https://developer.paypal.com) with Apple Pay enabled.
- Obtain an Apple Developer Program membership for live payments.
- Set up an HTTPS environment or ngrok for local development.

## Development setup

Configure your local development environment to work with Apple Pay's HTTPS requirement and PayPal's domain validation. For reference, see this [Apple Pay demo](https://github.com/paypal-examples/v6-web-sdk-sample-integration/tree/main/client/components/applepayPayments/html).

1. Install and configure ngrok:

   ```bash theme={null}
   npm install -g ngrok
   ngrok config add-authtoken YOUR_AUTHTOKEN
   ngrok http 3000
   ```

2. Update the Vite configuration:

   ```javascript theme={null}
   // vite.config.js
   export default defineConfig({
     server: {
       allowedHosts: ["your-ngrok-domain.ngrok-free.app"],
       proxy: {
         "/paypal-api": {
           target: "http://localhost:8080",
           changeOrigin: true,
           secure: false,
         },
       },
     },
   });
   ```

3. Register your domain with PayPal:
   - Add your ngrok domain to PayPal's Apple Pay settings
   - Download and save the domain association file

## Implementation steps

Implement Apple Pay by following the detailed steps.

### Step 1: HTML structure setup

Create your basic HTML page and include the Apple Pay and PayPal SDK scripts.

```html theme={null}
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Apple Pay Integration</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
  </head>
  <body>
    <h1>Apple Pay Payment</h1>
    <div id="apple-pay-button-container"></div>

    <!-- Apple Pay SDK -->
    <script src="https://applepay.cdn-apple.com/jsapi/v1/apple-pay-sdk.js"></script>

    <!-- PayPal JavaScript SDK -->
    <script
      async
      src="https://www.sandbox.paypal.com/web-sdk/v6/core"
      onload="onPayPalWebSdkLoaded()"
    ></script>

    <script src="app.js"></script>
  </body>
</html>
```

### Step 2: Initialize PayPal SDK

Set up the v6 SDK with Apple Pay components once it loads.

```javascript theme={null}
async function onPayPalWebSdkLoaded() {
  try {
    const sdkInstance = await window.paypal.createInstance({
      clientId: "YOUR_CLIENT_ID",
      components: ["applepay-payments"],
      pageType: "checkout",
    });

    setupApplePayButton(sdkInstance);
  } catch (error) {
    console.error("SDK initialization failed:", error);
  }
}
```

### Step 3: Configure Apple Pay button

Generate the Apple Pay button element and configure it for your payment flow.

```javascript theme={null}
async function setupApplePayButton(sdkInstance) {
  const paypalSdkApplePayPaymentSession =
    await sdkInstance.createApplePayOneTimePaymentSession();

  const { merchantCapabilities, supportedNetworks } =
    await paypalSdkApplePayPaymentSession.config();

  // Create Apple Pay button
  document.getElementById("apple-pay-button-container").innerHTML =
    '<apple-pay-button id="apple-pay-button" buttonstyle="black" type="buy" locale="en">';

  document
    .getElementById("apple-pay-button")
    .addEventListener("click", handleApplePayClick);
}
```

### Step 4: Configure payment request

Set up your payment details and start the Apple Pay session when users tap the button.

```javascript theme={null}
async function handleApplePayClick() {
  const paymentRequest = {
    countryCode: "US",
    currencyCode: "USD",
    merchantCapabilities,
    supportedNetworks,
    requiredBillingContactFields: ["name", "phone", "email", "postalAddress"],
    requiredShippingContactFields: [],
    total: {
      label: "Your Store Name",
      amount: "100.00",
      type: "final",
    },
  };

  const applePaySession = new ApplePaySession(4, paymentRequest);

  // Configure event handlers
  setupApplePayEventHandlers(applePaySession, paypalSdkApplePayPaymentSession);

  applePaySession.begin();
}
```

### Step 5: Handle Apple Pay events

Implement event handlers to process the payment through Apple Pay's workflow.

```javascript theme={null}
function setupApplePayEventHandlers(applePaySession, paypalSession) {
  // Merchant validation
  applePaySession.onvalidatemerchant = (event) => {
    paypalSession
      .validateMerchant({
        validationUrl: event.validationURL,
      })
      .then((payload) => {
        applePaySession.completeMerchantValidation(payload.merchantSession);
      })
      .catch((err) => {
        console.error("Merchant validation failed:", err);
        applePaySession.abort();
      });
  };

  // Payment method selection
  applePaySession.onpaymentmethodselected = () => {
    applePaySession.completePaymentMethodSelection({
      newTotal: paymentRequest.total,
    });
  };

  // Payment authorization
  applePaySession.onpaymentauthorized = async (event) => {
    try {
      // Create PayPal order
      const order = await createOrder();

      // Confirm order with Apple Pay token
      await paypalSession.confirmOrder({
        orderId: order.orderId,
        token: event.payment.token,
        billingContact: event.payment.billingContact,
        shippingContact: event.payment.shippingContact,
      });

      // Capture payment
      const result = await captureOrder({ orderId: order.orderId });

      applePaySession.completePayment({
        status: window.ApplePaySession.STATUS_SUCCESS,
      });

      console.log("Payment successful:", result);
    } catch (error) {
      console.error("Payment failed:", error);
      applePaySession.completePayment({
        status: window.ApplePaySession.STATUS_FAILURE,
      });
    }
  };

  // Payment cancellation
  applePaySession.oncancel = () => {
    console.log("Apple Pay cancelled");
  };
}
```

### Step 6: Add server integration

Implement server endpoints for order management.

```javascript theme={null}
// Create PayPal order
async function createOrder() {
  const response = await fetch(
    "/paypal-api/checkout/orders/create-with-sample-data",
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
    },
  );
  const { id } = await response.json();
  return { orderId: id };
}

// Capture order
async function captureOrder({ orderId }) {
  const response = await fetch(
    `/paypal-api/checkout/orders/${orderId}/capture`,
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
    },
  );
  return await response.json();
}
```

## Server-side requirements

Your backend needs these endpoints to support the Apple Pay integration:

- **Order creation endpoint**: Creates PayPal order and returns order ID for payment processing
- **Order capture endpoint**: Captures authorized payment and returns transaction details
- **Proper CORS and security headers**: Ensures secure communication between client and server

## Testing

Use the following steps to test your Apple Pay integration.

1. Open Safari browser on macOS or iOS device.
2. Sign into your sandbox iCloud account.
3. Add test credit cards to your Apple Pay wallet.
4. Test the complete payment flow.

## Production deployment

Deploy your Apple Pay integration to production.

1. Replace all sandbox URLs with production endpoints.
2. Update your application to use production PayPal credentials.
3. Register your production domain with Apple Pay.
4. Test the integration with a real Apple Pay setup
5. Add proper error monitoring to track payment issues

## Security considerations

- Use HTTPS in production.
- Ensure your merchant domain is valid.
- Keep domain association files current.
- Never expose client secrets in frontend code.
- Implement proper error handling.

## Troubleshooting

<table>
  <thead>
    <tr>
      <th>Issue</th>
      <th>Solution</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Button not appearing</td>

      <td>
        <ul>
          <li>Check Safari Apple Pay settings</li>
          <li>Verify domain registration</li>
          <li>Ensure HTTPS connection</li>
        </ul>
      </td>
    </tr>

    <tr>
      <td>Merchant validation fails</td>

      <td>
        <ul>
          <li>Check domain association file</li>
          <li>Verify PayPal domain registration</li>
          <li>Confirm ngrok domain in vite config</li>
        </ul>
      </td>
    </tr>

    <tr>
      <td>Payment authorization fails</td>

      <td>
        <ul>
          <li>Use sandbox iCloud account</li>
          <li>Check test credit card setup</li>
          <li>Verify server endpoints</li>
        </ul>
      </td>
    </tr>

  </tbody>
</table>

## Resources

- For more information, see the [Apple Pay HTML sample integration](https://github.com/paypal-examples/v6-web-sdk-sample-integration/tree/main/client/components/applePay/html).
