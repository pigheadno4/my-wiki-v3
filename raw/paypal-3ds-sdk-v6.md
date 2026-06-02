<!-- Source URL: https://docs.paypal.ai/payments/methods/3d-secure/integrate -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrate 3D Secure with PayPal's JavaScript SDK v6

With PayPal's JavaScript SDK v6, you can support Strong Customer Authentication (SCA) and 3D Secure (3DS) in two payment flows:

- **One-time payments** process a single transaction with 3DS when required. The SDK collects card details, creates an order, and captures payment upon approval.
- **Save payment methods (vaulting)** store cards for future purchases. The server creates setup tokens, and the client submits card details to complete vaulting with optional 3DS.

## One-time payment

On your server, create an order and define SCA and 3DS settings. Use `payment_source.card.attributes.verification.method` and supply return and cancel URLs in `experience_context`.

```javascript theme={null}
// POST /paypal-api/checkout/orders
// Body (example — adapt amounts, currency, and URLs)
{
  "intent": "CAPTURE",
  "purchase_units": [
    { "amount": { "currency_code": "USD", "value": "100.00" } }
  ],
  "payment_source": {
    "card": {
      "attributes": {
        "verification": { "method": "SCA_ALWAYS" } // or SCA_WHEN_REQUIRED
      },
      "experience_context": {
        "return_url": "https://example.com/returnUrl",
        "cancel_url": "https://example.com/cancelUrl"
      }
    }
  }
}
```

### Verification methods

- Use `SCA_ALWAYS` to attempt 3DS for eligible cards and regions.
- Use `SCA_WHEN_REQUIRED` to rely on network or regulatory mandates.

### Submit card details

On the client side, initialize the SDK and card fields. Submit the order and handle each possible outcome.

```javascript theme={null}
const sdk = await window.paypal.createInstance({
  clientId: "YOUR_CLIENT_ID",
  components: ["card-fields"],
});
const session = sdk.createCardFieldsOneTimePaymentSession();

// Render fields
const numberField = session.createCardFieldsComponent({
  type: "number",
  placeholder: "Card number",
});
const cvvField = session.createCardFieldsComponent({
  type: "cvv",
  placeholder: "CVV",
});
const expiryField = session.createCardFieldsComponent({
  type: "expiry",
  placeholder: "MM/YY",
});

[
  "#paypal-card-fields-number",
  "#paypal-card-fields-cvv",
  "#paypal-card-fields-expiry",
].map((sel, i) =>
  document
    .querySelector(sel)
    .appendChild([numberField, cvvField, expiryField][i]),
);

// Pay click
document.querySelector("#pay-button").addEventListener("click", async () => {
  try {
    const orderId = await createOrder({
      enable3DS: true,
      scaMethod: getScaMethodFromUI(),
    });
    const { state, data } = await session.submit(orderId, {
      billingAddress: { postalCode: "95131" },
    });

    switch (state) {
      case "succeeded": {
        const { orderId, liabilityShift } = data;
        // 3DS may or may not have occurred; Use liabilityShift
        // to determine if the payment should be captured
        const result = await captureOrder(data.orderId);
        // success UI
        break;
      }
      case "canceled": {
        // buyer closed 3DS modal
        break;
      }
      case "failed": {
        // inspect data.message
        break;
      }
    }
  } catch (e) {
    console.error(e);
  }
});
```

### Example order endpoint

Use this Express handler to create a PayPal order and optionally include 3DS parameters based on your request body.

```javascript theme={null}
app.post("/paypal-api/checkout/orders", async (req, res) => {
  const { enable3DS, scaMethod = "SCA_WHEN_REQUIRED" } = req.body || {};
  const body = {
    intent: "CAPTURE",
    purchase_units: [{ amount: { currency_code: "USD", value: "100.00" } }],
  };
  if (enable3DS) {
    body.payment_source = {
      card: {
        attributes: { verification: { method: scaMethod } },
        experience_context: {
          return_url: "https://example.com/returnUrl",
          cancel_url: "https://example.com/cancelUrl",
        },
      },
    };
  }
  // call PayPal Orders API with body and return { id }
});
```

## Save payment method

On the server, create a vault setup token to save a payment method and require 3DS. Specify a verification method in the request.

```javascript theme={null}
// POST /paypal-api/vault/setup-token
// Body (example)
{
  "payment_source": {
    "card": {
      "experience_context": {
        "return_url": "https://example.com/returnUrl",
        "cancel_url": "https://example.com/cancelUrl"
      },
      "verification_method": "SCA_ALWAYS" // or SCA_WHEN_REQUIRED
    }
  }
}
```

### Submit card with setup token

On the client side, initialize the SDK and card fields. Submit the order and handle each possible outcome.

```javascript theme={null}
const sdk = await window.paypal.createInstance({
  clientId: "YOUR_CLIENT_ID",
  components: ["card-fields"],
});
const session = sdk.createCardFieldsSavePaymentSession();

// Render 3 fields as shown above...

const { setupToken } = await createVaultSetupToken({
  enable3DS: true,
  scaMethod: getScaMethodFromUI(),
});
const { state, data } = await session.submit(setupToken);

switch (state) {
  case "succeeded": {
    // Persist data.vaultSetupToken on your server (maps to a vaulted instrument)
    break;
  }
  case "canceled": {
    // user dismissed 3DS
    break;
  }
  case "failed": {
    // show retry message
    break;
  }
}
```

## Best practices

- Include both the `return_url` and `cancel_url` in all 3DS requests.
- Handle every submit state and add `break;` in each switch case.
- Track the liability shift in `data` to manage risk.
