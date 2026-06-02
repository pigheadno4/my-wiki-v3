<!-- Source URL: https://docs.paypal.ai/developer/how-to/js-sdk/v6/upgrade-from-v5 -->
<!-- Fetched: 2026-04-19 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Upgrade from v5

Use this guide to upgrade your PayPal integration from the JavaScript SDK v5 to the JavaScript SDK v6. The v6 SDK introduces custom elements for UI, uses payment sessions to manage checkout flows, and offers flexible authentication with a client ID or client token.

***

## Compare v5 and v6

The following table shows how the v5 and v6 SDKs are different.

| Feature                    | v5                                                                                           | v6                                                                                       |
| -------------------------- | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **SDK script URL**         | You load the SDK with `https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&currency=USD`. | You load the SDK with `https://www.sandbox.paypal.com/web-sdk/v6/core`.                  |
| **Global `paypal` object** | All features are available from the global object.                                           | You call `createInstance`, which sets up the SDK.                                        |
| **Button rendering**       | You render buttons with `paypal.Buttons({ ... }).render()`.                                  | You use `<paypal-button/>` with an event listener and call `session.start()`.            |
| **Callbacks**              | You pass callbacks into `paypal.Buttons()`.                                                  | You pass callbacks into a checkout session, such as `createPayPalOneTimePaymentSession`. |
| **Venmo support**          | Venmo is included automatically in the smart stack.                                          | You enable Venmo with the `venmo-payments` component.                                    |

## Migration overview

### SDK script

In v5, you load the SDK using a script tag with the client ID and configuration directly in the URL.

```javascript theme={null}
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&currency=USD"></script>
```

In v6, you load the SDK core script without the client ID or any configuration in the URL.

```javascript theme={null}
<script async src="https://www.sandbox.paypal.com/web-sdk/v6/core" onload="onPayPalLoaded()"></script>
```

### Authentication: Client ID (Recommended)

v5 uses your client ID in the script URL. v6 uses your client ID in the `createInstance` call when initializing the SDK (recommended for most integrations):

```javascript theme={null}
const sdkInstance = await window.paypal.createInstance({
  clientId: "YOUR_CLIENT_ID",
  components: ["paypal-payments", "venmo-payments"],
  pageType: "checkout",
});
```

**Alternative: Client Token**

For specific features like PayPal payment vaulting or Fastlane, you'll need to use client token authentication instead.

See [Authenticate the SDK](/developer/how-to/sdk/js/v6/configuration#authenticate-the-sdk) for details on when to use each method.

### Render payment buttons

In v5, you render PayPal buttons directly through `paypal.Buttons().render()`.

```javascript theme={null}
paypal.Buttons({ ... }).render('#paypal-button-container');
```

In v6, you use custom elements for payment buttons. You control visibility and actions in JavaScript.

```javascript theme={null}
<paypal-button id="paypal-button" type="pay" hidden></paypal-button>
<venmo-button id="venmo-button" type="pay" hidden></venmo-button>
```

### Manage orders and callbacks

In v5, you define `createOrder` and `onApprove` inside the button configuration.

In v6, you define these as standalone functions and pass them to the payment session.

```javascript theme={null}
async function createOrder() {
  // call your server to create an order
  // pass the order ID Promise returned from this function to start()
}
async function onApprove({ orderId }) {
  // call your server to capture the order
}
const paypalCheckout = sdkInstance.createPayPalOneTimePaymentSession({
  onApprove,
});
```

### Handle sessions and button events

In v6, you create a payment session and attach a click handler to the button.

```javascript theme={null}
const paypalPaymentSession = sdkInstance.createPayPalOneTimePaymentSession({
  onApprove, onCancel, onError
});

paypalButton.addEventListener("click", async () => {
  await paypalPaymentSession.start(
    { presentationMode: "auto" },
    createOrder()
  );
});
```

### Check eligibility

In v5, eligibility checks are built in internally before rendering each button.

In v6, you check eligibility with the `findEligibleMethods` method or by calling the server-side API.

```javascript theme={null}
const paymentMethods = await sdkInstance.findEligibleMethods({ currencyCode: "USD" });
if (paymentMethods.isEligible("paypal")) {
  setupPayPalButton(sdkInstance);
}
```

## Summary of changes

- v6 uses client ID authentication (similar to v5) for most integrations, making migration straightforward. A client token is required only for specific features like PayPal vaulting and Fastlane.
- You use custom elements and payment sessions instead of button configurations.
- Built-in methods to check payment method availability.
- Load only the components you need for your integration.
- You pass callbacks directly to checkout sessions instead of button configurations.

For detailed code samples and advanced scenarios, see the Javascript SDK v6 examples on [GitHub](https://github.com/paypal-examples/v6-web-sdk-sample-integration).
