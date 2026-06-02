<!-- Source URL: https://docs.paypal.ai/payments/methods/venmo/integrate -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrate Venmo with PayPal's JavaScript SDK v6

You can accept Venmo for secure payments from US customers with the JavaScript SDK v6. This guide shows you how to set up your environment, review eligibility requirements, add Venmo payments, and work with advanced features.

## Prerequisites

Before beginning your integration, meet these requirements:

- Create a [PayPal developer account](https://developer.paypal.com/dashboard/).
- Use a **PayPal business account** to accept Venmo payments
- Set up your sandbox credentials.

> **Note:** You'll use your sandbox credentials to create a `.env` file during the **Development setup**.

## Eligibility

- US-based merchants and US-based consumers only.
- Payment must be in USD.

## Development setup

Before continuing, complete the steps in the [JavaScript SDK v6 sample integration README](https://github.com/paypal-examples/v6-web-sdk-sample-integration).

Once setup is complete, verify the JavaScript SDK v6 examples are running at `http://localhost:8080`.

To view the Venmo one-time payment example, navigate to: `http://localhost:8080/client/components/venmoPayments/oneTimePayment/html/src/index.html`.

## Implementation steps

### Step 1: HTML structure setup

Create your HTML page and include the PayPal SDK script.

```html theme={null}
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>One-Time Payment - Venmo - PayPal JavaScript SDK</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style>
      .buttons-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
      }
    </style>
  </head>
  <body>
    <h1>One-Time Payment Venmo Integration</h1>

    <div class="buttons-container">
      <!-- Venmo button is initially hidden until eligibility is confirmed -->
      <venmo-button id="venmo-button" type="pay" hidden></venmo-button>
    </div>

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

Set up the PayPal SDK with the Venmo component after it loads.

```javascript theme={null}
async function onPayPalWebSdkLoaded() {
  try {
    // Create PayPal SDK instance with Venmo component
    const sdkInstance = await window.paypal.createInstance({
      clientId: "YOUR_CLIENT_ID",
      components: ["venmo-payments"],
      pageType: "checkout",
    });

    // Check payment method eligibility
    const paymentMethods = await sdkInstance.findEligibleMethods({
      currencyCode: "USD",
    });

    // Only setup Venmo button if eligible
    if (paymentMethods.isEligible("venmo")) {
      setupVenmoButton(sdkInstance);
    } else {
      console.log("Venmo is not eligible for this session");
    }
  } catch (error) {
    console.error("SDK initialization error:", error);
  }
}
```

### Step 3: Configure Venmo button

Create the Venmo payment session and set up the button.

```javascript theme={null}
async function setupVenmoButton(sdkInstance) {
  // Create Venmo payment session with callback options
  const venmoPaymentSession = sdkInstance.createVenmoOneTimePaymentSession(
    paymentSessionOptions,
  );

  // Get reference to the Venmo button element
  const venmoButton = document.querySelector("#venmo-button");

  // Show the button since Venmo is eligible
  venmoButton.removeAttribute("hidden");

  // Add click handler to start payment flow
  venmoButton.addEventListener("click", async () => {
    try {
      // Start the payment session
      await venmoPaymentSession.start(
        {
          presentationMode: "auto", // Auto-detects best presentation mode
        },
        createOrder(), // Create order and return order details
      );
    } catch (error) {
      console.error("Payment start error:", error);
      handlePaymentError(error);
    }
  });
}
```

### Step 4. Configure payment session callbacks

Define callback handlers for payment approval, cancellation, and error scenarios.

```javascript theme={null}
const paymentSessionOptions = {
  // Called when payment is approved by the user
  async onApprove(data) {
    console.log("Payment approved:", data);
    try {
      // Capture the order on your server
      const orderData = await captureOrder({
        orderId: data.orderId,
      });
      console.log("Payment captured successfully:", orderData);

      // Handle successful payment (e.g., redirect, show success message)
      handlePaymentSuccess(orderData);
    } catch (error) {
      console.error("Payment capture failed:", error);
      handlePaymentError(error);
    }
  },

  // Called when user cancels the payment
  onCancel(data) {
    console.log("Payment cancelled:", data);
    // Handle cancellation (e.g., show message, return to cart)
    handlePaymentCancellation();
  },

  // Called when an error occurs during payment
  onError(error) {
    console.error("Payment error:", error);
    // Handle error (e.g., show error message, retry option)
    handlePaymentError(error);
  },
};
```

### Step 5. Choose presentation mode

The presentation mode determines how the payment UI appears for the customer.

```javascript theme={null}
// Auto mode - automatically chooses the best presentation mode
await venmoPaymentSession.start({ presentationMode: "auto" }, createOrder());
```

> **Note:** For Venmo, `"auto"` is the only supported presentation mode.

## API endpoints

The integration requires these server-side endpoints.

## Create order endpoint

```javascript theme={null}
// POST /paypal-api/checkout/orders/create-with-sample-data
async function createOrder() {
  const response = await fetch(
    "/paypal-api/checkout/orders/create-with-sample-data",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    },
  );
  const { id } = await response.json();

  return { orderId: id };
}
```

## Capture order endpoint

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

Integrate Venmo effectively by understanding the essential parts of the JavaScript SDK v6 workflow.

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
          <li>Includes <code>venmo-payments</code> component</li>
          <li>Authenticate with your client ID</li>
        </ul>
      </td>
    </tr>

    <tr>
      <td><strong>Eligibility check</strong></td>
      <td>Determines if Venmo is available</td>

      <td>
        <ul>
          <li>Based on user location, device type, currency, and account status</li>
          <li>Always check before showing Venmo button</li>
        </ul>
      </td>
    </tr>

    <tr>
      <td><strong>Payment session</strong></td>
      <td>Manages Venmo payment flow and callbacks</td>

      <td>
        <ul>
          <li>Handles approve, cancel, and error scenarios</li>
          <li>Created once and reused for multiple payment attempts</li>
        </ul>
      </td>
    </tr>

    <tr>
      <td><strong>Presentation modes</strong></td>
      <td>Defines how Venmo is displayed</td>

      <td>
        <ul>
          <li><strong>Auto</strong> — Only available presentation mode for Venmo</li>
        </ul>
      </td>
    </tr>

  </tbody>
</table>

## Security considerations

- Never expose client secrets in frontend code.
- Process all payments through PayPal’s servers.
- Use HTTPS in production.

## Testing

- Run transactions across desktop and mobile devices.
- Verify eligibility logic and Venmo button rendering.
- Test payment approval, cancellation, and error handling.

## Resources

- [Pay with Venmo](https://developer.paypal.com/docs/checkout/pay-with-venmo/)
- [Pay with Venmo integration](https://developer.paypal.com/docs/checkout/pay-with-venmo/integrate/)
- [JavaScript SDK](https://developer.paypal.com/sdk/js/)
- [PayPal Developer Dashboard](https://developer.paypal.com/dashboard/)
