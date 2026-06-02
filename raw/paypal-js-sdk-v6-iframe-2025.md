<!-- Source URL: https://docs.paypal.ai/developer/how-to/js-sdk/v6/sandboxed-iframe -->
<!-- Fetched: 2026-04-19 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Sandboxed <iframe> integration

PayPal's sandboxed `<iframe>` integration provides enhanced security by isolating payment processing code within a secure `<iframe>` wrapper while maintaining seamless communication with the parent merchant page through the `postMessage` API. In this case, the term "sandboxed" refers to the isolation of payment processing in an `<iframe>` wrapper, not the sandbox testing environment that PayPal provides.

In a sandboxed `<iframe>` integration, the parent page is a merchant page. Within the merchant page, an `<iframe>` wrapper uses the PayPal JavaScript SDK v6 and communicates with a server that accesses the PayPal server SDK. The merchant page and `<iframe>` use `postMessage` to communicate about the state of a payment. Using the PayPal SDK inside an `<iframe>` wrapper prevents having to request the SDK script directly from the merchant page.

This type of integration is recommended for high-security uses, such as banking and financial services or integrations with strict compliance requirements, such as PCI DSS, or SOC 2. However, it requires more complex setup and maintenance than other PayPal integrations.

This implementation consists of two separate applications:

- A merchant page at `localhost:3001` for your main website and app
- A PayPal `<iframe>` at `localhost:3000` that provides an isolated payment processing environment with secure cross-frame communication through the `postMessage` API

This page provides examples that you can use to help you understand and set up this kind of integration.

## Prerequisites

Before you integrate:

- Get a [client ID and secret](/developer/how-to/api/get-started#1-get-your-client-id-and-client-secret).
- [Set up the v6 SDK](/developer/how-to/sdk/js/v6/configuration).

## Environment configuration

To work with these examples, create a .env file with your PayPal sandbox credentials to enable proper authentication and API communication.

```bash theme={null}
PAYPAL_SANDBOX_CLIENT_ID=YOUR_CLIENT_ID
PAYPAL_SANDBOX_CLIENT_SECRET=YOUR_CLIENT_SECRET
```

## Merchant page HTML structure

Set up yor merchant page HTML before setting up your `<iframe>` wrapper. This example shows how to set up the main merchant page with proper `<iframe>` sandbox attributes, overlay containers for modal presentation, and debug information displays.

```html lines expandable theme={null}
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>PayPal iframe Example</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style>
      #iframeWrapper {
        border: none;
        width: 100%;
        height: 300px;
      }

      #iframeWrapper.fullWindow {
        position: absolute;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;
      }

      #overlayContainer::backdrop {
        background: rgba(0, 0, 0, 0.67);
      }
    </style>
  </head>
  <body>
    <script async src="/app.js" onload="onLoad()"></script>

    <div id="mainContainer">
      <h1>PayPal iframe Example</h1>

      <!-- Sandboxed iframe with proper permissions -->
      <iframe
        id="iframeWrapper"
        src="http://localhost:3000/?origin=http://localhost:3001"
        sandbox="allow-scripts allow-same-origin allow-popups allow-forms"
        allow="payment"
      ></iframe>
    </div>

    <!-- Modal overlay for popup presentation mode -->
    <dialog id="overlayContainer">
      <div id="overlayContainerLogo">
        <img
          src="https://www.paypalobjects.com/js-sdk-logos/2.2.7/paypal-white.svg"
        />
      </div>
      <button id="overlayCloseButtonCTA">Close</button>
      <button id="overlayCloseButtonBackdrop">X</button>
    </dialog>
  </body>
</html>
```

## Merchant page JavaScript implementation

This example implements page-state management, secure postMessage listeners with origin validation, and handlers for different presentation modes (`popup`, `modal`, `payment-handler`).

```javascript lines expandable theme={null}
class PageState {
  state = {
    presentationMode: null,
    lastPostMessage: null,
    merchantDomain: null,
  };

  constructor() {
    this.merchantDomain = window.location.origin;
  }

  set presentationMode(value) {
    this.state.presentationMode = value;
    const element = document.getElementById("presentationMode");
    element.innerHTML = value;
  }

  set lastPostMessage(event) {
    const statusContainer = document.getElementById("postMessageStatus");
    statusContainer.innerHTML = JSON.stringify(event.data);
    this.state.lastPostMessage = event;
  }
}

const pageState = new PageState();

// Set up secure postMessage listener with origin validation
function setupPostMessageListener() {
  window.addEventListener("message", (event) => {
    // 🔒 CRITICAL: Always validate origin to prevent XSS attacks!
    if (event.origin !== "http://localhost:3000") {
      return;
    }

    pageState.lastPostMessage = event;
    const { eventName, data } = event.data;
    const { presentationMode } = pageState;

    if (eventName === "presentationMode-changed") {
      const { presentationMode } = data;
      pageState.presentationMode = presentationMode;
    } else if (presentationMode === "popup") {
      popupPresentationModePostMessageHandler(event);
    } else if (presentationMode === "modal") {
      modalPresentationModePostMessageHandler(event);
    }
  });
}
```

## PayPal `<iframe>` HTML structure

This example creates the `<iframe>` content with configuration options for the presentation mode, the PayPal button element, and proper script loading for the v6 SDK.

```html lines expandable theme={null}
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>PayPal Payment Handler</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style>
      body {
        font-family: sans-serif;
        color: #e5f5ea;
        background: #334037;
      }
    </style>
  </head>
  <body>
    <!-- Presentation mode configuration -->
    <div id="config">
      <div>Payment flow config</div>
      <fieldset>
        <legend>presentationMode</legend>
        <div>
          <input
            checked
            type="radio"
            id="presentationMode-popup"
            name="presentationMode"
            value="popup"
          />
          <label for="presentationMode-popup">popup</label>
        </div>
        <div>
          <input
            type="radio"
            id="presentationMode-modal"
            name="presentationMode"
            value="modal"
          />
          <label for="presentationMode-modal">modal</label>
        </div>
      </fieldset>
    </div>

    <!-- PayPal button -->
    <paypal-button id="paypal-button"></paypal-button>

    <script src="/integration.js"></script>
    <script
      async
      src="https://www.sandbox.paypal.com/web-sdk/v6/core"
      onload="onPayPalWebSdkLoaded()"
    ></script>
  </body>
</html>
```

## PayPal `<iframe>` JavaScript implementation

This JavaScript runs inside the `<iframe>`, not the merchant page. It initializes the SDK, creates the payment session, and sends status updates back to the merchant page using `postMessage`.

### Initialize the SDK

The v6 SDK script in the `<iframe>` HTML calls `onPayPalWebSdkLoaded()` when it finishes loading. This function initializes the SDK and passes the instance to `setupPayPalButton()`.

- Replace `"YOUR_CLIENT_ID"` with your client ID.
- Partners: replace `"SELLER_MERCHANT_ID"` with the merchant ID of the seller you're creating the payment session for.
- Non-partners: omit `merchantId`.

```javascript lines theme={null}
async function onPayPalWebSdkLoaded() {
  const sdkInstance = await window.paypal.createInstance({
    clientId: "YOUR_CLIENT_ID",
    merchantId: "SELLER_MERCHANT_ID",
    components: ["paypal-payments"],
    pageType: "checkout",
  });

  setupPayPalButton(sdkInstance);
}
```

### Set up the payment session

`setupPayPalButton()` uses the SDK instance to create a payment session and attach a click handler to the PayPal button. When the buyer completes, cancels, or triggers an error in the payment flow, the function sends a `postMessage` event to the merchant page.

```javascript lines expandable theme={null}
class PageState {
  state = {
    paymentSession: null,
  };

  get paymentSession() {
    return this.state.paymentSession;
  }

  set paymentSession(value) {
    this.state.paymentSession = value;
  }
}

const pageState = new PageState();

// Set up PayPal button with payment session
async function setupPayPalButton(sdkInstance) {
  pageState.paymentSession = sdkInstance.createPayPalOneTimePaymentSession({
    onApprove: async (data) => {
      const orderData = await captureOrder({
        orderId: data.orderId,
      });

      sendPostMessageToParent({
        eventName: "payment-flow-approved",
        data: orderData,
      });
    },
    onCancel: (data) => {
      sendPostMessageToParent({
        eventName: "payment-flow-canceled",
        data: {
          orderId: data?.orderId,
        },
      });
    },
    onError: (data) => {
      sendPostMessageToParent({
        eventName: "payment-flow-error",
        data: {
          orderId: data?.orderId,
        },
      });
    },
  });

  const paypalButton = document.querySelector("#paypal-button");
  paypalButton.addEventListener("click", async () => {
    const paymentFlowConfig = {
      presentationMode: getSelectedPresentationMode(),
      fullPageOverlay: { enabled: false },
    };

    sendPostMessageToParent({
      eventName: "payment-flow-start",
      data: { paymentFlowConfig },
    });

    try {
      await pageState.paymentSession.start(paymentFlowConfig, createOrder());
    } catch (e) {
      console.error("Payment start error:", e);
      sendPostMessageToParent({
        eventName: "payment-flow-error",
        data: { error: e.message },
      });
    }
  });
}
```

## Package.json configuration

This example configures `npm` scripts to run the merchant page and the PayPal `<iframe>` servers concurrently using the <a href="https://vite.dev/guide/build" target="_blank">Vite</a> build tool with proper port assignments. For more information about Vite, see [Vite configuration files](#vite-configuration-files).

```bash lines expandable theme={null}
{
  "name": "v6-web-sdk-sample-html-iframe",
  "version": "1.0.0",
  "description": "PayPal sandboxed iframe integration example",
  "scripts": {
    "merchant-page": "vite --config vite-merchant-example.config.js",
    "paypal-iframe": "vite --config vite-paypal-iframe.config.js",
    "start": "concurrently \"npm run merchant-page\" \"npm run paypal-iframe\"",
    "format": "prettier . --write",
    "format:check": "prettier . --check"
  },
  "dependencies": {
    "concurrently": "^9.1.2",
    "vite": "^7.0.4"
  }
}
```

## Vite configuration files

This example sets up separate <a href="https://vite.dev/guide/build" target="_blank">Vite</a> configurations for the merchant page (port 3001) and PayPal iFrame (port 3000) with proper proxy settings for PayPal API endpoints.

```javascript lines expandable theme={null}
// vite-merchant-example.config.js
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [],
  root: "src/merchant-example",
  server: {
    port: 3001,
  },
});

// vite-paypal-iframe.config.js
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [],
  root: "src/paypal-iframe",
  server: {
    port: 3000,
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

## `<iframe>` sandbox security configuration

This example configures `<iframe>` sandbox attributes to enable necessary permissions while maintaining security isolation with `allow-scripts`, `allow-same-origin`, `allow-popups`, and `allow-forms`.

```html lines theme={null}
<iframe
  src="http://localhost:3000/?origin=http://localhost:3001"
  sandbox="allow-scripts allow-same-origin allow-popups allow-forms"
  allow="payment"
></iframe>
```

## PostMessage origin validation

This example implements critical security measures, such as validating message origins to prevent XSS attacks and ensuring that only trusted domains can communicate with your application.

```javascript lines expandable theme={null}
// ✅ ALWAYS validate message origin
window.addEventListener("message", (event) => {
  if (event.origin !== expectedOrigin) {
    return; // Ignore messages from unknown origins
  }
  // Process trusted message
});

// ❌ NEVER accept messages without validation
window.addEventListener("message", (event) => {
  // Vulnerable to XSS attacks!
  processMessage(event.data);
});
```

## Content security policy header configuration

<a href="https://content-security-policy.com/" target="_blank">Content Security Policy (CSP) headers</a> control resource loading and prevent unauthorized script execution while allowing necessary PayPal SDK and `<iframe>` communication in this example. You learn more about security headers in [Production security headers](#production-security-headers).

```html theme={null}
<meta
  http-equiv="Content-Security-Policy"
  content="
  default-src 'self';
  script-src 'self' 'unsafe-inline' https://www.sandbox.paypal.com;
  frame-src 'self' http://localhost:3000;
  connect-src 'self' http://localhost:8080;
  img-src 'self' https://www.paypalobjects.com;
"
/>
```

## Communication protocol messages

Define standardized message formats for iframe-to-parent communication, including changes to the presentation mode, payment flow events, and error handling, as shown in this example.

```javascript lines expandable theme={null}
// Presentation mode changed
{
  eventName: "presentationMode-changed",
  data: { presentationMode: "popup" }
}

// Payment flow started
{
  eventName: "payment-flow-start",
  data: { paymentFlowConfig: {...} }
}

// Payment approved
{
  eventName: "payment-flow-approved",
  data: { orderId: "...", captureData: {...} }
}

// Payment canceled
{
  eventName: "payment-flow-canceled",
  data: { orderId: "..." }
}

// Payment error
{
  eventName: "payment-flow-error",
  data: { error: "..." }
}
```

## Advanced event handling

You can implement a comprehensive event-handling system with custom logic for payment start, success, cancellation, and error scenarios. This example also includes analytics tracking and user feedback.

```javascript lines expandable theme={null}
function setupAdvancedPostMessageListener() {
  window.addEventListener("message", (event) => {
    if (event.origin !== "http://localhost:3000") {
      return;
    }

    const { eventName, data } = event.data;

    switch (eventName) {
      case "payment-flow-start":
        handlePaymentStart(data);
        break;
      case "payment-flow-approved":
        handlePaymentSuccess(data);
        break;
      case "payment-flow-canceled":
        handlePaymentCancellation(data);
        break;
      case "payment-flow-error":
        handlePaymentError(data);
        break;
      case "presentationMode-changed":
        handlePresentationModeChange(data);
        break;
      default:
        console.warn("Unknown event:", eventName);
    }
  });
}

function handlePaymentSuccess(data) {
  // Hide loading state
  hideLoadingIndicator();

  // Show success message
  showSuccessMessage("Payment completed successfully!");

  // Redirect or update UI
  setTimeout(() => {
    window.location.href = "/success";
  }, 2000);

  // Track conversion
  trackEvent("payment_completed", data);
}
```

## Dynamic `<iframe>` management

The `IframeManager` class can handle message queuing, ready-state management, and cleanup operations for better control over `<iframe>` lifecycle, as shown in this example.

```javascript lines expandable theme={null}
class IframeManager {
  constructor(iframeId, targetOrigin) {
    this.iframe = document.getElementById(iframeId);
    this.targetOrigin = targetOrigin;
    this.messageQueue = [];
    this.isReady = false;
  }

  sendMessage(payload) {
    if (this.isReady) {
      this.iframe.contentWindow.postMessage(payload, this.targetOrigin);
    } else {
      this.messageQueue.push(payload);
    }
  }

  onReady() {
    this.isReady = true;
    // Send queued messages
    this.messageQueue.forEach((payload) => {
      this.iframe.contentWindow.postMessage(payload, this.targetOrigin);
    });
    this.messageQueue = [];
  }

  destroy() {
    this.iframe.remove();
    this.isReady = false;
    this.messageQueue = [];
  }
}

const iframeManager = new IframeManager(
  "iframeWrapper",
  "http://localhost:3000",
);
```

## Error recovery and retry logic

Implement payment retry management with configurable retry limits, user confirmation dialogs, and graceful fallback handling for failed payment attempts, as shown in this example.

```javascript lines expandable theme={null}
class PaymentRetryManager {
  constructor(maxRetries = 3) {
    this.maxRetries = maxRetries;
    this.currentRetries = 0;
  }

  async handlePaymentError(error, retryCallback) {
    console.error("Payment error:", error);

    if (this.currentRetries < this.maxRetries) {
      this.currentRetries++;

      // Show retry option to user
      const shouldRetry = await showRetryDialog(
        `Payment failed (${this.currentRetries}/${this.maxRetries}). Would you like to try again?`,
      );

      if (shouldRetry) {
        return retryCallback();
      }
    }

    // Max retries reached or user declined retry
    this.currentRetries = 0;
    showFinalErrorMessage(
      "Payment could not be completed. Please try a different payment method.",
    );
  }

  reset() {
    this.currentRetries = 0;
  }
}

const retryManager = new PaymentRetryManager();
```

## Production security headers

In a production environment, configure `Express.js` security headers for production deployment, including `X-Frame-Options`, content security policy (CSP), and MIME-type protection. For more information about CSP, see [Content security policy header configuration](#content-security-policy-header-configuration).

```javascript lines expandable theme={null}
// Express.js security headers
app.use((req, res, next) => {
  // Prevent iframe embedding from untrusted domains
  res.setHeader("X-Frame-Options", "SAMEORIGIN");

  // Content Security Policy
  res.setHeader(
    "Content-Security-Policy",
    `
    default-src 'self';
    script-src 'self' 'unsafe-inline' https://www.paypal.com;
    frame-src 'self' https://payments.example.com;
    connect-src 'self' https://api.paypal.com;
    img-src 'self' https://www.paypalobjects.com;
  `
      .replace(/\s+/g, " ")
      .trim(),
  );

  // Prevent MIME type sniffing
  res.setHeader("X-Content-Type-Options", "nosniff");

  next();
});
```

## Troubleshooting PostMessage

To troubleshoot common postMessage communication issues, check origin validation and `<iframe>` loading status. Also, confirm that you configured the proper sandbox attributes.

```javascript lines expandable theme={null}
// Check origin validation
if (event.origin !== expectedOrigin) {
  console.warn(`Message rejected from origin: ${event.origin}`);
  return;
}

// Check iframe loading
iframe.onload = () => {
  console.log("Iframe ready for postMessage communication");
};

// Ensure proper sandbox attributes
const requiredSandboxAttrs = [
  "allow-scripts",
  "allow-same-origin",
  "allow-popups",
  "allow-forms",
];

const sandboxAttr = iframe.getAttribute("sandbox");
requiredSandboxAttrs.forEach((attr) => {
  if (!sandboxAttr.includes(attr)) {
    console.error(`Missing sandbox attribute: ${attr}`);
  }
});
```

## See also

You can see an end-to-end (E2E) example of an `<iframe>` integration with PayPal in <a href="https://github.com/paypal-examples/v6-web-sdk-sample-integration/tree/main/client/components/paypalPayments/oneTimePayment/html/src/advanced/sandboxedIframe/" target="_blank">the public examples repository on GitHub</a>.
