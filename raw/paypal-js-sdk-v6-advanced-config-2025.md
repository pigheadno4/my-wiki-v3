<!-- Source URL: https://docs.paypal.ai/developer/how-to/js-sdk/v6/advanced-configuration -->
<!-- Fetched: 2026-04-19 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Advanced configuration

Advanced configuration options for the JavaScript SDK v6 help you customize the payment experience.

## Prerequisites

Before you integrate:

- Get a [client ID and secret](/developer/how-to/api/get-started#1-get-your-client-id-and-client-secret).
- [Set up the v6 SDK](/developer/how-to/sdk/js/v6/configuration).

## Configure presentation modes and fallback

For advanced use cases, you can choose a [specific presentation mode](/reference/sdk/js/v6/reference#parameters-6). Then, implement your own fallback logic with the `isRecoverable` error property.

```javascript expandable lines theme={null}
// Alternatively, set up a standard PayPal button with a custom order of presentation modes
async function setupPayPalButton(sdkInstance) {
  const paypalPaymentSession = sdkInstance.createPayPalOneTimePaymentSession(
    paymentSessionOptions,
  );

  const paypalButton = document.querySelector("paypal-button");
  paypalButton.removeAttribute("hidden");

  paypalButton.addEventListener("click", async () => {
    const createOrderPromiseReference = createOrder();
    const presentationModesToTry = ["payment-handler", "popup", "modal"];

    for (const presentationMode of presentationModesToTry) {
      try {
        await paypalPaymentSession.start(
          { presentationMode },
          createOrderPromiseReference,
        );
        // Exit early when start() successfully resolves
        break;
      } catch (error) {
        // Try another presentationMode for a recoverable error
        if (error.isRecoverable) {
          continue;
        }
        throw error;
      }
    }
  });
}
```
