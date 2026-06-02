<!-- Source URL: https://docs.paypal.ai/payments/methods/card-fields/integrate -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Render card fields for one-time checkout with PayPal's JavaScript SDK v6

This guide shows how to:

- Load the JavaScript SDK v6 core script
- Initialize an SDK instance using a client ID
- Render Card Fields (number, CVV, expiry)
- Create and submit an order
- Capture the order and handle 3-D Secure (3DS) outcomes

You'll connect two backend routes:

- `POST /paypal-api/checkout/orders/create-with-sample-data`: returns a new orderId
- `POST /paypal-api/checkout/orders/{orderId}/capture` captures the order

## Prerequisites

You'll need the following:

- A PayPal sandbox business account and REST app with permissions to create client tokens.
- A server capable of calling PayPal APIs securely. Node and Express examples included below.
- [PCI Compliance](https://www.pcisecuritystandards.org/).
  PCI DSS SAQ A-EP considerations: Card fields are hosted or iframes from PayPal. Your page must follow security best practices.

## Add the JavaScript SDK script

Include the core script and call the `onPayPalWebSdkLoaded()` handler when it's ready.

```html theme={null}
<script
  async
  src="https://sandbox.paypal.com/web-sdk/v6/core"
  onload="onPayPalWebSdkLoaded()"
></script>
```

Keep `async` to avoid blocking the render.

## Build an HTML container

Provide containers for each card field and a pay button.

The provided containers must have a defined height and width. The card field fills the entire space of the parent container.

The `button id` in the sample is `pay-button`. Make sure your JavaScript uses the same selector.

```html theme={null}
<style>
  .card-field {
    height: 3rem;
    margin-bottom: 1rem;
  }
</style>

<div class="card-fields-container">
  <div class="card-field" id="paypal-card-fields-number"></div>
  <div class="card-field" id="paypal-card-fields-expiry"></div>
  <div class="card-field" id="paypal-card-fields-cvv"></div>
</div>
<button id="pay-button" class="pay-button">Pay</button>
```

## Initialize the SDK and render card fields

Create an SDK instance with your client ID, then create a one‑time payment session for credit and debit card fields and mount the components.

To pass billing fields, use the `submit(orderId, { billingAddress: { ... } })` options object. Include at least the fields you require for your risk and SCA strategy, for example, `postalCode`.

```javascript theme={null}
async function onPayPalWebSdkLoaded() {
  try {
    const sdk = await window.paypal.createInstance({
      clientId: "YOUR_CLIENT_ID",
      components: ["card-fields"],
    });

    const paymentMethods = await sdk.findEligibleMethods();
    const isCardFieldsEligible = paymentMethods.isEligible("advanced_cards");
    if (isCardFieldsEligible) {
      await setupCardFields(sdk);
    }
  } catch (err) {
    console.error("SDK init failed", err);
  }
}

async function setupCardFields(sdk) {
  const cardSession = sdk.createCardFieldsOneTimePaymentSession();

  const numberField = cardSession.createCardFieldsComponent({
    type: "number",
    placeholder: "Card number",
  });

  const expiryField = cardSession.createCardFieldsComponent({
    type: "expiry",
    placeholder: "MM/YY",
  });

  const cvvField = cardSession.createCardFieldsComponent({
    type: "cvv",
    placeholder: "CVV",
  });

  document.querySelector("#paypal-card-fields-number").appendChild(numberField);
  document.querySelector("#paypal-card-fields-expiry").appendChild(expiryField);
  document.querySelector("#paypal-card-fields-cvv").appendChild(cvvField);

  const payButton = document.querySelector("#pay-button");
  payButton.addEventListener("click", () => onPayClick(cardSession));
}
```

## Create, submit, and capture the order

1. Create the order on your server, then receive the `orderId`.
2. Call `cardSession.submit(orderId, options)` to handle validations and 3D Secure.
3. If `state === "succeeded"`, capture the order on your server.

```javascript theme={null}
async function onPayClick(cardSession) {
  try {
    const orderId = await createOrder(); // returns a string id

    const { data, state } = await cardSession.submit(orderId, {
      billingAddress: {
        postalCode: "95131",
      }, // supply what your business needs
    });

    switch (state) {
      case "succeeded": {
        const { orderId, liabilityShift } = data;
        // 3DS may or may not have occurred; Use liabilityShift
        // to determine if the payment should be captured
        const capture = await captureOrder(orderId);
        // TODO: show success UI, redirect, etc.
        break;
      }
      case "canceled": {
        // Buyer dismissed 3DS modal or canceled the flow
        // TODO: show non-blocking message & allow retry
        break;
      }
      case "failed": {
        // Validation or processing failure. data.message may be present
        console.error("Card submission failed", data);
        // TODO: surface error to buyer, allow retry
        break;
      }
      default: {
        // Future-proof for other states (e.g., pending)
        console.warn("Unhandled submit state", state, data);
      }
    }
  } catch (err) {
    console.error("Payment flow error", err);
    // TODO: Show generic error and allow retry
  }
}
```

## Client helpers

[//]: # "Need introduction to this code"

```javascript theme={null}
async function createOrder() {
  const res = await fetch(
    "/paypal-api/checkout/orders/create-with-sample-data",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    },
  );
  const { id } = await res.json();
  return id; // return the string orderId
}

async function captureOrder(orderId) {
  const res = await fetch(`/paypal-api/checkout/orders/${orderId}/capture`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  });
  return res.json();
}
```

## Server examples

The following is a minimal example to support two routes. It uses the PayPal Orders v2 API. Replace placeholders and secure secrets appropriately.

```javascript theme={null}
import express from "express";
import fetch from "node-fetch";

const app = express();
app.use(express.json());

const PAYPAL_BASE =
  process.env.PAYPAL_BASE || "https://api-m.sandbox.paypal.com"; // use api-m.paypal.com in prod
const CLIENT_ID = process.env.PAYPAL_CLIENT_ID;
const CLIENT_SECRET = process.env.PAYPAL_CLIENT_SECRET;

async function appAccessToken(formBody) {
  const creds = Buffer.from(`${CLIENT_ID}:${CLIENT_SECRET}`).toString("base64");
  const res = await fetch(`${PAYPAL_BASE}/v1/oauth2/token`, {
    method: "POST",
    headers: {
      Authorization: `Basic ${creds}`,
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: formBody,
  });
  const json = await res.json();
  return json.access_token;
}

// 1) Create order with sample purchase units
app.post(
  "/paypal-api/checkout/orders/create-with-sample-data",
  async (_req, res) => {
    try {
      const fullScopeAccessTokenFormBody =
        "grant_type=client_credentials&response_type=token";
      const accessToken = await appAccessToken(fullScopeAccessTokenFormBody);
      const r = await fetch(`${PAYPAL_BASE}/v2/checkout/orders`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${accessToken}`,
        },
        body: JSON.stringify({
          intent: "CAPTURE",
          purchase_units: [
            {
              amount: {
                currency_code: "USD",
                value: "10.00",
              },
            },
          ],
        }),
      });
      const data = await r.json();
      res.json({
        id: data.id,
      });
    } catch (e) {
      console.error(e);
      res.status(500).json({
        error: "order_create_error",
      });
    }
  },
);

// 2) Capture order
app.post("/paypal-api/checkout/orders/:orderId/capture", async (req, res) => {
  try {
    const fullScopeAccessTokenFormBody =
      "grant_type=client_credentials&response_type=token";
    const accessToken = await appAccessToken(fullScopeAccessTokenFormBody);
    const r = await fetch(
      `${PAYPAL_BASE}/v2/checkout/orders/${req.params.orderId}/capture`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${accessToken}`,
        },
      },
    );
    const data = await r.json();
    res.json(data);
  } catch (e) {
    console.error(e);
    res.status(500).json({
      error: "order_capture_error",
    });
  }
});

app.listen(3000, () => console.log("Server listening on 3000"));
```

## Style card fields

Use the `style` option to control input styling such as font size and color. Keep contrast [AA or better](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html). Avoid setting styles that imply validation, such as red and green, unless synchronized with real validation states.

Allowed CSS selectors:

- `appearance`
- `background`
- `border`
- `borderRadius`
- `boxShadow`
- `color`
- `direction`
- `font`
- `fontFamily`
- `fontSize`
- `fontSizeAdjust`
- `fontStretch`
- `fontStyle`
- `fontVariant`
- `fontVariantAlternates`
- `fontVariantCaps`
- `fontVariantEastAsian`
- `fontVariantLigatures`
- `fontVariantNumeric`
- `fontWeight`
- `height`
- `letterSpacing`
- `lineHeight`
- `opacity`
- `outline`
- `padding`
- `paddingBottom`
- `paddingLeft`
- `paddingRight`
- `paddingTop`
- `textShadow`
- `transition`

```javascript theme={null}
const numberField = cardSession.createCardFieldsComponent({
  type: "number",
  style: {
    input: {
      fontSize: "16px",
      lineHeight: "24px",
    },
    ".invalid": {
      color: orange,
    },
  },
});
```

## Handle outcomes and errors

There are 3 possible outcomes from checkout:

- `state === "succeeded"`: Proceed to capture on server and show success.
- `state === "canceled"`: Buyer closed 3DS modal. Allow retry.
- `state === "failed"`: Inspect `data.message` and field errors if provided. Keep logs server‑side with correlation IDs from API responses.

Common troubleshooting issues:

- **Button id mismatch**: Ensure your JS listens to `#pay-button` and not `#save-payment-method-button`.
- **OrderId shape**: Pass the string `orderId` to `submit()`. Do not pass an object such as `{ orderId }`.
- **Missing breaks in switch**: Include `break;` in each case to avoid fall‑through.

## Test

- Test in the PayPal sandbox environment and use [test credit cards](https://developer.paypal.com/tools/sandbox/card-testing/#link-testgeneratedcardnumbers).
- Test the following scenarios:
  - Valid payment
  - Card validation error
  - 3DS succeeded
  - 3DS canceled
  - Network or server error on capture

## Production readiness checklist

- Use production script at [https://www.paypal.com/web-sdk/v6/core](https://www.paypal.com/web-sdk/v6/core).
- Use CSRF protection on your backend routes
- Ensure your integration has robust error handling and user‑friendly retry states
- Ensure your integration logs PayPal API correlation IDs for support
- Check your site for accessibility by keyboard and screen reader
- Ensure your Content Security Policy is updated for PayPal domains

## Full working example

The following example shows a JavaScript and HTML page that renders card fields for one-time checkout. You can localize placeholder strings when creating each component.

When available, use `sdk.findEligibleMethods({ currencyCode: "USD" })` and gate Card Fields rendering accordingly. The card may not appear in the eligibility response yet. Integrate defensively.

```html theme={null}
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>One‑Time Payment — Card Fields</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style>
      .card-fields-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
      }
      .pay-button {
        padding: 12px 16px;
        font-size: 16px;
      }
      .is-loading {
        opacity: 0.6;
        pointer-events: none;
      }
    </style>
  </head>
  <body>
    <h1>Card Fields — One‑Time Payment</h1>

    <div class="card-fields-container">
      <div class="card-field" id="paypal-card-fields-number"></div>
      <div class="card-field" id="paypal-card-fields-expiry"></div>
      <div class="card-field" id="paypal-card-fields-cvv"></div>
    </div>
    <button id="pay-button" class="pay-button">Pay</button>

    <button id="pay-button" class="pay-button">Pay</button>

    <script>
      async function onPayPalWebSdkLoaded() {
        try {
          const sdk = await window.paypal.createInstance({
            clientId: "YOUR_CLIENT_ID",
            components: ["card-fields"],
            pageType: "checkout",
          });
          const paymentMethods = await sdk.findEligibleMethods();
          const isCardFieldsEligible =
            paymentMethods.isEligible("advanced_cards");
          if (isCardFieldsEligible) {
            await setupCardFields(sdk);
          }
        } catch (err) {
          console.error(err);
        }
      }

      async function setupCardFields(sdk) {
        const session = sdk.createCardFieldsOneTimePaymentSession();

        const numberField = session.createCardFieldsComponent({
          type: "number",
          placeholder: "Card number",
        });
        const expiryField = session.createCardFieldsComponent({
          type: "expiry",
          placeholder: "MM/YY",
        });
        const cvvField = session.createCardFieldsComponent({
          type: "cvv",
          placeholder: "CVV",
        });

        document
          .querySelector("#paypal-card-fields-number")
          .appendChild(numberField);
        document
          .querySelector("#paypal-card-fields-expiry")
          .appendChild(expiryField);
        document.querySelector("#paypal-card-fields-cvv").appendChild(cvvField);

        const button = document.querySelector("#pay-button");
        button.addEventListener("click", async () => {
          try {
            button.classList.add("is-loading");
            const orderId = await createOrder();
            const { data, state } = await session.submit(orderId, {
              billingAddress: { postalCode: "95131" },
            });

            switch (state) {
              case "succeeded": {
                const capture = await captureOrder(data.orderId);
                alert("Payment captured");
                break;
              }
              case "canceled": {
                alert("Authentication canceled. Please try again.");
                break;
              }
              case "failed": {
                alert(
                  data?.message ||
                    "Payment failed. Check your details and try again.",
                );
                break;
              }
              default: {
                console.warn("Unhandled state", state);
              }
            }
          } catch (err) {
            console.error(err);
            alert("Unexpected error. Please try again.");
          } finally {
            button.classList.remove("is-loading");
          }
        });
      }

      async function createOrder() {
        const r = await fetch(
          "/paypal-api/checkout/orders/create-with-sample-data",
          { method: "POST" },
        );
        const { id } = await r.json();
        return id;
      }

      async function captureOrder(orderId) {
        const r = await fetch(
          `/paypal-api/checkout/orders/${orderId}/capture`,
          { method: "POST" },
        );
        return r.json();
      }
    </script>

    <script
      async
      src="https://www.sandbox.paypal.com/web-sdk/v6/core"
      onload="onPayPalWebSdkLoaded()"
    ></script>
  </body>
</html>
```
