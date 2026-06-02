<!-- Source URL: https://docs.paypal.ai/payments/methods/guest-payments/integrate -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrate standalone payment buttons with PayPal's JavaScript SDK v6

With PayPal's JavaScript SDK v6, you can accept basic card and debit card processing without requiring payers to log in or create a PayPal account. You'll set up a test environment, add the needed frontend and backend, and then launch your standalone payment button in both sandbox and production.

## Prerequisites

Before beginning your integration, meet these requirements:

- Create a [PayPal Developer account](https://developer.paypal.com).
- Create a PayPal app in the **Apps & Credentials** section of your account.
- Use the **Sandbox** environment for testing.
- Note your **Client ID** and **Secret** for server configuration.

## Development setup

Before you run the [v6-web-sdk-sample-integration](https://github.com/paypal-examples/v6-web-sdk-sample-integration) locally, complete both server and client setup.

## Server set up

1. Navigate to your demo directory and install dependencies:

```
npm install
```

2. Create environment configuration:

```bash theme={null}
# .env file
PAYPAL_SANDBOX_CLIENT_ID=your_client_id
PAYPAL_SANDBOX_CLIENT_SECRET=your_client_secret
```

3. Start the server:

```bash theme={null}
npm start
```

To load the application, see `http://localhost:8080`.

## Client set up

1. Navigate to the demo directory:

```
cd client/components/paypalGuestPayments/html
```

2. Install dependencies:

```
npm install
```

3. Start development server:

```
npm start
```

To load the application, see `http://localhost:3000`.

## Integration patterns

The v6 SDK supports a variety of standalone payment button integration flows. The following patterns help you tailor the user experience for different requirements.

### Standard button

Use the standard button implementation for payers to select a button to start the standalone payment button flow (Recommended).

- **File**: `html/src/recommended/app.js`

```javascript theme={null}
// 1. Initialize SDK when script loads
async function onPayPalWebSdkLoaded() {
  const sdkInstance = await window.paypal.createInstance({
    clientId: "YOUR_CLIENT_ID",
    components: ["paypal-guest-payments"],
  });

  setupGuestPaymentButton(sdkInstance);
}

// 2. Setup the payment session
async function setupGuestPaymentButton(sdkInstance) {
  // Check eligibility
  const eligiblePaymentMethods = await sdkInstance.findEligibleMethods({
    currencyCode: "USD",
  });

  // Create payment session with callbacks
  const paypalGuestPaymentSession =
    await sdkInstance.createPayPalGuestOneTimePaymentSession({
      onApprove,
      onCancel,
      onComplete,
      onError,
      onWarn,
    });

  // 3. Start checkout on button click
  document
    .getElementById("paypal-basic-card-button")
    .addEventListener("click", async () => {
      const startOptions = {
        presentationMode: "auto",
      };
      await paypalGuestPaymentSession.start(startOptions, createOrder());
    });
}
```

#### HTML setup

```html theme={null}
<paypal-basic-card-container>
  <paypal-basic-card-button id="paypal-basic-card-button">
  </paypal-basic-card-button>
</paypal-basic-card-container>

<script src="app.js"></script>
<script
  async
  src="https://www.sandbox.paypal.com/web-sdk/v6/core"
  onload="onPayPalWebSdkLoaded()"
></script>
```

### Auto-start on load

Use the auto-start on load integration to automatically initiate the standalone payment button.

- **File**: `html/src/onload/app.js`

```javascript theme={null}
async function onPayPalWebSdkLoaded() {
  // ... standard setup ...

  const checkoutButton = document.getElementById("paypal-basic-card-button");

  // Auto-start checkout on page load
  startGuestPaymentSession(checkoutButton, paypalGuestPaymentSession);

  // Also setup button for manual trigger
  setupGuestPaymentButton(checkoutButton, paypalGuestPaymentSession);
}

// Reusable function for starting checkout
async function startGuestPaymentSession(
  checkoutButton,
  paypalGuestPaymentSession,
) {
  const startOptions = {
    targetElement: checkoutButton,
    presentationMode: "auto",
  };
  await paypalGuestPaymentSession.start(startOptions, createOrder());
}
```

### Shipping callbacks

Use the shipping callback integration to handle address validation and shipping option changes.

- **File**: `html/src/shipping/app.js`

```javascript theme={null}
const paypalGuestPaymentSession =
  await sdkInstance.createPayPalGuestOneTimePaymentSession({
    onApprove,
    onCancel,
    onComplete,
    onError,
    onWarn,
    onShippingAddressChange, // New callback
    onShippingOptionsChange, // New callback
  });

// Validate shipping address (example: US-only)
function onShippingAddressChange(data) {
  const countryCode = data?.shippingAddress?.countryCode ?? "US";
  if (countryCode !== "US") {
    throw new Error(data?.errors?.COUNTRY_ERROR);
  }
}

// Handle shipping option changes
function onShippingOptionsChange(data) {
  const selectedShippingOption = data?.selectedShippingOption?.id;
  if (selectedShippingOption === "SHIP_UNV") {
    throw new Error(data?.errors?.METHOD_UNAVAILABLE);
  }
}
```

#### Sample order creation with shipping options

```javascript theme={null}
async function createOrder() {
  const orderPayload = {
    intent: "CAPTURE",
    purchaseUnits: [
      {
        amount: {
          currencyCode: "USD",
          value: "10.00",
          breakdown: {
            itemTotal: { currencyCode: "USD", value: "10.00" },
          },
        },
        shipping: {
          options: [
            {
              id: "SHIP_FRE",
              label: "Free",
              type: "SHIPPING",
              selected: true,
              amount: { value: "0.00", currencyCode: "USD" },
            },
            {
              id: "SHIP_EXP",
              label: "Expedited",
              type: "SHIPPING",
              selected: false,
              amount: { value: "5.00", currencyCode: "USD" },
            },
          ],
        },
      },
    ],
  };

  const response = await fetch("/paypal-api/checkout/orders/create", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(orderPayload),
  });

  const { id } = await response.json();
  return { orderId: id };
}
```

## Implementation support functions

These helper functions allow the client to interact with your backend for order creation and payment capture.

### Create order

```javascript theme={null}
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
```

### Capture order

```javascript theme={null}
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

## Callback functions

Define the callback functions to handle key events during the standalone payment button flow, such as approvals, cancellations, errors, and warnings.

### Required callbacks

```javascript theme={null}
// Handle successful payment approval
async function onApprove(data) {
  console.log("onApprove", data);
  const orderData = await captureOrder({ orderId: data.orderId });
  console.log("Capture result", orderData);
}

// Handle payment cancellation
function onCancel(data) {
  console.log("onCancel", data);
  // Handle cancellation logic
}

// Handle payment completion
function onComplete(data) {
  console.log("onComplete", data);
  // Handle completion logic (success page, etc.)
}

// Handle errors
function onError(data) {
  console.log("onError", data);
  // Handle error display to user
}

// Handle warnings
function onWarn(data) {
  console.log("onWarn", data);
  // Handle warnings as needed
}
```

The `data` argument to `onWarn` will always have the following shape:

```json theme={null}
{
  "message": "PayPalGuestCheckoutSession form submit failed: GUEST_CHECKOUT_INLINE_FORM_SUBMIT_FAILURE",
  "name": "PaymentFlowWarning",
  "code": "WARN_FLOW_GUEST_CHECKOUT_SUBMIT_ERROR"
}
```

When the `onWarn` callback executes, the buyer has encountered an error after they pressed the form submit button. These errors could include
card failures, first/last name formatting errors, or address errors.

## Start options

When starting a payment session, you can configure presentation mode.

```javascript theme={null}
const startOptions = {
  presentationMode: "auto", // "auto", "modal", "popup", or "redirect"
  targetElement: checkoutButton, // Optional: element to attach to
};

await paypalGuestPaymentSession.start(startOptions, createOrder());
```

## API endpoints

Your backend server must provide these endpoints:

- `POST /paypal-api/checkout/orders/create-with-sample-data` - Creates PayPal order with sample data
- `POST /paypal-api/checkout/orders/create` - Creates PayPal order with custom data
- `POST /paypal-api/checkout/orders/{order-id}/capture` - Captures the authorized payment

## Testing

See the steps for running and validating your integration.

1. Ensure both server and client are running.
2. Navigate to the demo page.
3. Use PayPal Sandbox test accounts.
4. Test all three integration patterns:
   - Standard button
   - Auto-start on load
   - Shipping callbacks

## Best practices

- **Error handling**: Always wrap PayPal API calls in try-catch blocks.
- **Eligibility check**: Call `findEligibleMethods()` to determine available payment options.
- **Security**: Never expose client secrets in frontend code.
- **User experience**: Choose the most suitable presentation mode for your use case.
- **Validation**: Validate shipping callbacks if needed.
- **Testing**: Test thoroughly in PayPal Sandbox before going live.

## Troubleshooting

Quick solutions for common issues:

- **SDK load errors**: Ensure the JavaScript SDK v6 script loads before `onPayPalWebSdkLoaded()`.

- **SDK initialization issues**: Verify that your client ID is correct and that the server endpoints are running and accessible.

- **Eligibility issues**: Check that your standalone payments are enabled in PayPal app settings.

- **CORS errors**: Confirm proper CORS configuration between client and server.
