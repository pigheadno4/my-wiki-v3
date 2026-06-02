<!-- Source URL: https://docs.paypal.ai/payments/methods/fastlane/integrate -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Fastlane integration

PayPal Fastlane is a streamlined checkout experience that allows returning customers to authenticate and pay quickly using saved payment methods and shipping addresses. New customers can also use it for a smooth guest checkout experience. For more information about Fastlane, see the <a href="https://developer.paypal.com/studio/checkout/fastlane" rel="nofollow" target="_blank" rel="noopener" rel="noreferrer">PayPal Fastlane documentation</a>.

This guide provides instructions for integrating PayPal Fastlane into your web application using the v6 web SDK.

## Prerequisites

- PayPal sandbox account with appropriate credentials. For more information about using PayPal's sandbox for testing, see the <a href="https://developer.paypal.com/tools/sandbox/" target="_blank" rel="noopener" rel="noreferrer">PayPal sandbox testing guide</a>.
- Backend server for API proxy. For more information, see <a href="https://github.com/paypal-examples/v6-web-sdk-sample-integration/blob/main/server/node/README.md" target="_blank" rel="noopener" rel="noreferrer">`/server/node/README.md`</a>.
- A web browser with ES6 support.

There also are requirements for the [backend](#backend-endpoints) and your [HTML](#html-structure).

### Backend endpoints

Your backend must provide these API endpoints:

- The client token endpoint provides a client token for SDK initialization.
  - URL: `GET /paypal-api/auth/browser-safe-client-token`
  - Response: `{ "accessToken": "YOUR-CLIENT-TOKEN" }`
- The order creation endpoint creates a PayPal order using the payment token.
  - URL: `POST /paypal-api/checkout/orders/create`
  - Headers: <br />
    `Content-Type: application/json` <br />
    `PayPal-Request-Id: <unique-id>`

### HTML structure

Your HTML must include these elements.

```html theme={null}
<!-- Email form -->
<form id="email-form">
  <input type="email" id="email-input" />
  <div id="watermark-container"></div>
  <button id="email-submit-button">Submit</button>
</form>

<!-- Payment containers -->
<div id="card-container"></div>
<div id="payment-container"></div>

<!-- Shipping display -->
<div id="shipping-display-container" hidden></div>
<button id="change-shipping-button" hidden>Change Shipping Address</button>

<!-- Order submission -->
<button id="submit-button" hidden>Submit Order</button>

<!-- Card testing info -->
<p id="card-testing-info" hidden>
  For more info on testing cards with PayPal, see
  <a href="https://developer.paypal.com/tools/sandbox/card-testing/">
    https://developer.paypal.com/tools/sandbox/card-testing/
  </a>
</p>
```

## Integration

Fastlane integration consists of three main JavaScript files:

- `fastlaneSdkComponent.js`: SDK initialization and client token management
- `fastlane.js`: Main integration logic and UI handling
- `fastlane.css`: Basic styling for the checkout experience

For examples of these files, see <a href="https://github.com/paypal-examples/v6-web-sdk-sample-integration/tree/fcaf5ceb342a41813803c060bdbe4039ccbe3f56/client/components/fastlane/html/src" target="_blank" rel="noopener" rel="noreferrer">this GitHub repo folder</a>.

To complete the integration:

1. Include the PayPal SDK script in your HTML.

```html theme={null}
<script
  async
  onload="onPayPalLoaded()"
  src="https://www.sandbox.paypal.com/web-sdk/v6/core"
></script>
```

1. Initialize the SDK and Fastlane (`fastlaneSdkComponent.js`).

In this example, you see some Fastlane SDK options:

- `pageType`: The applicable page type, such as `product-details`
- `clientMetadataId`: Unique session identifier
- `components`: Array that includes `fastlane` <br /><br />

```javascript theme={null}
async function onPayPalLoaded() {
  const clientToken = await getBrowserSafeClientToken();
  const sdkInstance = await window.paypal.createInstance({
    clientToken,
    pageType: "product-details",
    clientMetadataId: crypto.randomUUID(),
    components: ["fastlane"],
  });
  fastlane = await sdkInstance.createFastlane();
  setupFastlaneSdk();
}
```

2. Set up the email-lookup flow (`fastlane.js`).

The email-lookup process determines whether a user is a Fastlane member.

```javascript theme={null}
async function setupFastlaneSdk() {
  fastlane.setLocale("en_us");
  // Render Fastlane watermark
  const fastlaneWatermark = await fastlane.FastlaneWatermarkComponent({
    includeAdditionalInfo: true,
  });
  fastlaneWatermark.render("#watermark-container");
  // Handle email submission
  const emailSubmitButton = document.getElementById("email-submit-button");
  emailSubmitButton.addEventListener("click", async (e) => {
    e.preventDefault();
    const { customerContextId } = await fastlane.identity.lookupCustomerByEmail(
      emailInput.value,
    );
    let shouldRenderFastlaneMemberExperience = false;
    let profileData;
    if (customerContextId) {
      const response =
        await fastlane.identity.triggerAuthenticationFlow(customerContextId);
      if (response.authenticationState === "succeeded") {
        shouldRenderFastlaneMemberExperience = true;
        profileData = response.profileData;
      }
    }
    // Route to appropriate experience
    if (shouldRenderFastlaneMemberExperience) {
      renderFastlaneMemberExperience(profileData);
    } else {
      renderFastlaneGuestExperience();
    }
  });
}
```

3. Set up handling for members (`fastlane.js`).

Members are authenticated Fastlane members who have saved data.

```javascript theme={null}
async function renderFastlaneMemberExperience(profileData) {
  if (profileData.shippingAddress) {
    setShippingAddressDisplay(profileData.shippingAddress);
    // Allow address changes
    const changeAddressButton = document.getElementById(
      "change-shipping-button",
    );
    changeAddressButton.addEventListener("click", async () => {
      const { selectedAddress, selectionChanged } =
        await fastlane.profile.showShippingAddressSelector();
      if (selectionChanged) {
        profileData.shippingAddress = selectedAddress;
        setShippingAddressDisplay(profileData.shippingAddress);
      }
    });
    // Render payment component with shipping address
    const fastlanePaymentComponent = await fastlane.FastlanePaymentComponent({
      options: {},
      shippingAddress: profileData.shippingAddress,
    });
    fastlanePaymentComponent.render("#payment-container");
  }
}
```

4. Set up handling for guests (`fastlane.js`).

Guests are new or unauthenticated users.

```javascript theme={null}
async function renderFastlaneGuestExperience() {
  const cardTestingInfo = document.getElementById("card-testing-info");
  cardTestingInfo.removeAttribute("hidden");
  const FastlanePaymentComponent = await fastlane.FastlanePaymentComponent({});
  await FastlanePaymentComponent.render("#card-container");
}
```

5. Set up payment processing (`fastlane.js`).

Payment processing includes generating a payment token and creating an order.

In this step, you see these payment component options:

- `options`: Additional payment component configuration
- `shippingAddress`: Pre-populate with a member's saved address <br /><br />

```javascript theme={null}
// Get payment token
const { id } = await fastlanePaymentComponent.getPaymentToken();
// Create order via backend API
async function createOrder(paymentToken) {
  const response = await fetch("/paypal-api/checkout/orders/create", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "PayPal-Request-Id": Date.now().toString(),
    },
    body: JSON.stringify({
      paymentSource: {
        card: {
          singleUseToken: paymentToken,
        },
      },
      purchaseUnits: [
        {
          amount: {
            currencyCode: "USD",
            value: "10.00",
            breakdown: {
              itemTotal: {
                currencyCode: "USD",
                value: "10.00",
              },
            },
          },
        },
      ],
      intent: "CAPTURE",
    }),
  });
  return await response.json();
}
```

## Error handling

This integration includes basic error handling, including:

- If a member's authentication fails, they get the guest experience.
- Errors in order creation display user-friendly messages.
- The console logs error information to help with debugging.

## Testing

For testing, use PayPal's <a href="https://developer.paypal.com/tools/sandbox/" target="_blank" rel="noopener" rel="noreferrer">sandbox environment</a> with sandbox credentials.

Test <a href="https://developer.paypal.com/studio/checkout/fastlane/integrate#test-integration" target="_blank" rel="noopener" rel="noreferrer"> member and guest flows with card numbers</a>.

## Sample app

To see the sample app, run these commands.

```bash theme={null}
npm install
npm start
```

The sample app will run at `http://localhost:3000/`. The sample requires a backend server at `http://localhost:8080`.

## See also

Examine a full example of a Fastlane integration on <a href="https://github.com/paypal-examples/v6-web-sdk-sample-integration/tree/main/client/components/fastlane/html/" target="_blank" rel="noopener" rel="noreferrer">GitHub</a>.
