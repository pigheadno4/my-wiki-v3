<!-- Source URL: https://docs.paypal.ai/payments/methods/paypal/troubleshoot -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshoot

Find solutions to common PayPal integration issues.

## The PayPal button does not appear

- Check that the client ID in your HTML matches the client ID in the .env file.
- Make sure to use sandbox credentials for development and production credentials for live.

## 404 Page Not Found error

Make sure `index.html` is in the `public` folder. Express serves static files from there.

## Invalid Client error

The client ID and secret don't match, or there's a mix of sandbox and production credentials. PayPal provides separate credentials for sandbox and production. Make sure your client ID and secret are both from the same environment.

## Multipage and modular app issues

If your app uses PayPal buttons across multiple pages or a modular JavaScript architecture, errors typically stem from one root cause: the SDK instance isn't accessible where your code expects it. The following errors are related symptoms of the same scoping problem.

### `window.paypalSdkInstance` is undefined

This browser console error means the SDK instance was created but never exposed outside of `onLoad()`.

In the file where you define `onLoad()` (usually `paypal-init.js` or `index.html`), add the following two lines after creating the instance:

```js lines expandable theme={null}
async function onLoad() {
  try {
    const sdkInstance = await window.paypal.createInstance({...});

    // ⚠️ ADD THIS LINE
    window.paypalSdkInstance = sdkInstance;

    // ⚠️ ALSO ADD THIS (required for the waiting pattern)
    window.dispatchEvent(new CustomEvent('paypalReady', {
      detail: { instance: sdkInstance }
    }));
  }
}
```

To verify the fix, open the browser console and run:

```js theme={null}
window.paypalSdkInstance;
```

You should see an object with methods such as `createPayPalOneTimePaymentSession`.

### PayPal button appears on one page but not others

These symptoms indicate the SDK instance isn't accessible to pages other than the one where it was initialized:

- Buttons work on your main page but not on product, cart, or checkout pages
- Console shows errors about an undefined SDK instance

To fix this, include the SDK script and initialization on every page that has PayPal buttons. The cleanest way to do this is through a shared layout or template:

```html lines theme={null}
<!-- Include in your shared layout, or add to EVERY page with PayPal buttons -->
<script
  async
  src="https://www.sandbox.paypal.com/web-sdk/v6/core"
  onload="onLoad()"
></script>
<script src="/js/paypal-init.js"></script>
```

For Single-Page Applications (SPAs), set `window.paypalSdkInstance` during initialization and ensure it persists across route changes.

A typical file structure for multipage apps looks like this:

```text theme={null}
your-app/
├── public/
│   ├── index.html              # Loads SDK script
│   ├── js/
│   │   ├── paypal-init.js      # Contains onLoad() and initPayPalButton()
│   │   ├── products.js         # Product page buttons
│   │   ├── cart.js             # Cart page button
│   │   └── checkout.js         # Checkout page button
├── server.js
└── .env
```

### SDK initialization timing errors

These symptoms indicate your code is trying to access `window.paypalSdkInstance` before `onLoad()` has finished creating it:

- Buttons appear intermittently
- Buttons work sometimes but fail on page load
- Errors occur randomly

The problem is a race condition between when the SDK loads and when your page scripts run:

```text theme={null}
Timeline 1 (Success):  SDK loads → onLoad() → createInstance() → Your code runs ✓
Timeline 2 (Failure):  Your code runs → Error! → SDK loads (too late) ✗
```

In any file other than your main initialization file, use this waiting pattern instead of accessing `window.paypalSdkInstance` directly:

```js lines expandable theme={null}
function initButtonWhenReady(containerId) {
  if (window.paypalSdkInstance) {
    // SDK already loaded, initialize immediately
    initPayPalButton(containerId);
  } else {
    // SDK still loading, wait for it
    window.addEventListener(
      "paypalReady",
      () => {
        initPayPalButton(containerId);
      },
      { once: true },
    );
  }
}

document.addEventListener("DOMContentLoaded", () => {
  initButtonWhenReady("#my-button");
});
```

This pattern handles both timelines:

- If the SDK is already loaded, it runs immediately.
- If the SDK is still loading, it waits for the `paypalReady` event dispatched in `onLoad()`.

### Debugging checklist

On the page where buttons aren't appearing, open the browser console and run:

```js theme={null}
console.log("SDK loaded:", !!window.paypal);
console.log("Instance ready:", !!window.paypalSdkInstance);
```

If either value is `false`:

- `window.paypal` is `false`: the SDK script isn't loading on this page.
- `window.paypalSdkInstance` is `false`: `onLoad()` isn't running, or `window.paypalSdkInstance = sdkInstance` is missing.
