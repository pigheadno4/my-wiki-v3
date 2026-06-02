<!-- Source URL: https://docs.paypal.ai/payments/methods/save-cards/integrate-without-purchase -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Save cards without purchase with the JavaScript SDK

Save payment methods to charge payers after a set amount of time. For example, you can offer a free trial and charge payers after the trial expires. Payers don't need to be present when charged. No checkout required.

Use the JavaScript SDK to save a payer's card if you aren't <a href="https://www.pcisecuritystandards.org/pci_security/completing_self_assessment">PCI Compliant - SAQ A</a> but want to save credit or debit cards during checkout.

## Availability

<Accordion title="Supported countries">
  * Australia
  * Austria
  * Belgium
  * Bulgaria
  * Canada
  * China
  * Cyprus
  * Czech Republic
  * Denmark
  * Estonia
  * Finland
  * France
  * Germany
  * Hong Kong
  * Hungary
  * Ireland
  * Italy
  * Japan
  * Latvia
  * Liechtenstein
  * Lithuania
  * Luxembourg
  * Malta
  * Netherlands
  * Norway
  * Poland
  * Portugal
  * Romania
  * Singapore
  * Slovakia
  * Slovenia
  * Spain
  * Sweden
  * United Kingdom
  * United States
</Accordion>

## Prerequisites

- You are responsible for the front-end user experience. The JavaScript SDK provides back-end support.
- To save payment methods, you must be able to identify payers uniquely. For example, payers create an account and log in to your site.
- Complete the steps in [Get started](https://developer.paypal.com/api/rest) to get the following sandbox account information from the Developer Dashboard:
  - Your sandbox account login information
  - Your access token
- This client-side integration uses the `createCardFieldsSavePaymentSession()` method to save a card without a transaction.
- The JavaScript SDK saves the following card types for purchase later:
  - American Express
  - Discover
  - Mastercard
  - Visa
    You'll need an existing [advanced credit and debit integration](https://developer.paypal.com/studio/checkout/advanced). PayPal must approve your business account for advanced credit and debit card payments.

## How it works

PayPal encrypts payment method information and stores it in a digital vault for that customer.

1. The payer saves their payment method.
2. For a first-time payer, PayPal creates a customer ID. Store this within your system for future use.
3. When the customer returns to your website and is ready to check out, pass their PayPal-generated customer ID to your server to retrieve saved instruments.
4. The payer completes any required verification (for example, 3DS) per your SCA policy.
5. Your UI can display saved payment methods as a one-click button alongside other ways to pay.

## 1. Set up account to save payments

Set up your sandbox and live business accounts to save payment methods:

1. Log in to the Developer Dashboard.
2. Under **REST API apps**, select your app name.
3. Under **Sandbox App Settings** > **App Feature Options**, check **Accept payments**.
4. Expand **Advanced options**. Confirm that **Vault** is selected.

## 2. Add SDK to HTML page

Pass your client ID to the SDK to identify yourself.
Replace `CLIENT-ID` with your app's client ID in the following sample:

```html theme={null}
<script
  async
  src="https://sandbox.paypal.com/web-sdk/v6/core"
  onload="onPayPalWebSdkLoaded()"
></script>
```

## 3. Create setup token

You request a setup token from your server. The setup token creation for v6 now supports optional 3D Secure verification per your SCA policy.

### Create a vault setup token on your server

This example for v6 includes optional 3DS or SCA behavior:

```bash theme={null}
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens' \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ACCESS-TOKEN" \
-H "PayPal-Request-Id: REQUEST-ID" \
-d '{
      "payment_source": {
        "card": {
          "verification_method": "SCA_WHEN_REQUIRED",
          "experience_context": {
            "return_url": "https://example.com/returnUrl",
            "cancel_url": "https://example.com/cancelUrl"
          }
        }
      }
  }'
```

Create a setup token for cards that have:

- No verification - omit `verification_method`
- 3D Secure verification - `"SCA_ALWAYS"` or `"SCA_WHEN_REQUIRED"`

### Front-end sample

```javascript theme={null}
const sdk = await window.paypal.createInstance({
  clientId: "YOUR_CLIENT_ID",
  components: ["card-fields"],
});
const session = sdk.createCardFieldsSavePaymentSession();
// ... render number/cvv/expiry as usual

const { setupToken } = await createVaultSetupToken({ enable3DS, scaMethod });
const { state, data } = await session.submit(setupToken);

switch (state) {
  case "succeeded": {
    // Persist data.vaultSetupToken (or returned instrument id) on your server
    break;
  }
  case "canceled": {
    // Buyer dismissed challenge
    break;
  }
  case "failed": {
    // Show retry message, inspect data.message
    break;
  }
}
```

### Back-end sample

Make this request from your server.

This setup token is generated with an empty `card` in the `payment_source` object. PayPal hosted fields use this token to securely update the setup token with card details.

Copy and modify the following code:

1. Change `ACCESS-TOKEN` to your sandbox app's access token.
2. Change `REQUEST-ID` to a set of unique alphanumeric characters such as a time stamp.
3. In the `createVaultSetupToken`, call the endpoint on your server to create a setup token with the [Payment Method Tokens API](https://developer.paypal.com/docs/api/payment-tokens/v3/). `createVaultSetupToken` returns the setup token as a string.

```bash theme={null}
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens'
-H "Content-Type: application/json"
-H "Authorization: Bearer ACCESS-TOKEN"
-H "PayPal-Request-Id: REQUEST-ID"
-d '{
      "payment_source": {
        "card": {}
      }
  }'
`}
```

## 4. Initialize card fields to save data

When you want to vault a card without taking a payment, use the Save Payment Session on the client: `sdk.createCardFieldsSavePaymentSession()`.

### Front-end sample

<Tabs>
  <Tab title="No verification">
    ```javascript theme={null}
    // Initialize the v6 SDK
    const sdk = await window.paypal.createInstance({ 
      clientId: "YOUR_CLIENT_ID",
      components: ["card-fields"] 
    });

    // Create the session
    const session = sdk.createCardFieldsSavePaymentSession();

    // Render the card fields (you still need this part)
    session.render({
      fields: {
        number: { selector: '#card-number' },
        cvv: { selector: '#card-cvv' },
        expirationDate: { selector: '#card-expiry' }
      }
    });

    // When user submits the form (replace the automatic callbacks)
    async function handleSubmit() {
      try {
        // This replaces your createVaultSetupToken callback
        const result = await fetch("example.com/create/setup/token");
        const setupToken = result.token;

        // Submit with the session (this is the new way)
        const { state, data } = await session.submit(setupToken);

        switch (state) {
          case "succeeded": {
            // This replaces your onApprove callback
            await fetch("example.com/create/payment/token", {
              body: JSON.stringify({ vaultSetupToken: data.vaultSetupToken })
            });
            break;
          }
          case "canceled": {
            // Handle when user cancels
            break;
          }
          case "failed": {
            // Handle errors
            console.error(data.message);
            break;
          }
        }
      } catch (error) {
        console.error("Error:", error);
      }
    }
    ```

  </Tab>

  <Tab title="3D Secure">
    ```javascript theme={null}
    // Initialize the v6 SDK
    const sdk = await window.paypal.createInstance({ 
      clientId: "YOUR_CLIENT_ID",
      components: ["card-fields"] 
    });

    // Create the session
    const session = sdk.createCardFieldsSavePaymentSession();

    // Render the card fields (you still need this part)
    session.render({
      fields: {
        number: { selector: '#card-number' },
        cvv: { selector: '#card-cvv' },
        expirationDate: { selector: '#card-expiry' }
      }
    });

    // When user submits the form (replace the automatic callbacks)
    async function handleSubmit() {
      try {
        // This replaces your createVaultSetupToken callback
        const result = await fetch("example.com/create/setup/token");
        const setupToken = result.token;

        // Submit with the session (this is the new way)
        const { state, data } = await session.submit(setupToken);

        switch (state) {
          case "succeeded": {
            // This replaces your onApprove callback
            // Send the vaultSetupToken to your server for later use
            const vaultSetupToken = data.vaultSetupToken;
            // Do whatever you need with the token here
            console.log("Vault setup token:", vaultSetupToken);
            break;
          }
          case "canceled": {
            // Handle when user cancels
            break;
          }
          case "failed": {
            // This replaces your onError callback
            console.error('Something went wrong:', data.message);
            break;
          }
        }
      } catch (error) {
        // This also replaces your onError callback for network/other errors
        console.error('Something went wrong:', error);
      }
    }
    ```

  </Tab>
</Tabs>

### Back-end sample

Make this request from your server. Copy and modify the following code.

1. Pass the `vaultSetupToken` returned by `onApprove` to your server.
2. Change `ACCESS-TOKEN` to your sandbox app's access token.
3. Change `REQUEST-ID` to a set of unique alphanumeric characters such as a time stamp.
4. Change `VAULT-SETUP-TOKEN` to the value passed from the client.
5. Save the resulting `payment token` returned from the API to use in future transactions.

```bash theme={null}
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v3/vault/payment-tokens'
-H "Content-Type: application/json"
-H "Authorization: Bearer ACCESS-TOKEN"
-H "PayPal-Request-Id: REQUEST-ID"
-d '{
      "payment_source": {
          "token": {
              "id": "VAULT-SETUP-TOKEN",
              "type": "SETUP_TOKEN"
          }
      }
  }'
```

### Avoid validation errors

`sdk.createCardFieldsSavePaymentSession()` cannot be used alongside `sdk.createCardFieldsPaymentSession()` on the same page. Create separate sessions for different use cases:

```javascript theme={null}
// Initialize the v6 SDK
const sdk = await window.paypal.createInstance({
  clientId: "YOUR_CLIENT_ID",
  components: ["card-fields"]
});

// Option 1: For vaulting (saving cards)
const vaultSession = sdk.createCardFieldsSavePaymentSession();

// Option 2: For immediate payments
const paymentSession = sdk.createCardFieldsPaymentSession();

// Render the same card fields (they can be reused)
const cardFieldsConfig = {
  fields: {
    number: { selector: '#card-number' },
    cvv: { selector: '#card-cvv' },
    expirationDate: { selector: '#card-expiry' }
  }
};

// You can render with either session
vaultSession.render(cardFieldsConfig);
// OR
// paymentSession.render(cardFieldsConfig);

// Then use the appropriate session based on user intent:

// For vaulting:
async function handleVault() {
  const result = await fetch("example.com/create/setup/token");
  const setupToken = result.token;
  const { state, data } = await vaultSession.submit(setupToken);
  // Handle vault result...
}

// For immediate payment:
async function handlePayment() {
  const result = await fetch("example.com/create/order");
  const orderId = result.id;
  const { state, data } = await paymentSession.submit(orderId);
  // Handle payment result...
```

## 5. Show error page

If an error prevents checkout, alert the payer that an error has occurred using the `console.error()` method call.

> **Note:** This script doesn't handle specific errors. It shows a specified error page for all errors.

```javascript theme={null}
// Initialize the v6 SDK
const sdk = await window.paypal.createInstance({
  clientId: "YOUR_CLIENT_ID",
  components: ["card-fields"],
});

// Create a session (choose based on your use case)
const session = sdk.createCardFieldsSavePaymentSession();
// OR
// const session = sdk.createCardFieldsPaymentSession();

// Render the card fields
session.render({
  fields: {
    number: { selector: "#card-number" },
    cvv: { selector: "#card-cvv" },
    expirationDate: { selector: "#card-expiry" },
  },
});

// Error handling is now done in your submit function
async function handleSubmit() {
  try {
    // Your token/order creation logic here
    const setupToken = "your-setup-token"; // or orderId for payments

    const { state, data } = await session.submit(setupToken);

    switch (state) {
      case "succeeded": {
        // Handle success
        break;
      }
      case "canceled": {
        // Handle cancellation
        break;
      }
      case "failed": {
        // This replaces your onError callback
        console.error("Something went wrong:", data.message);
        break;
      }
    }
  } catch (error) {
    // This also handles errors (like the onError callback)
    console.error("Something went wrong:", error);
  }
}
```

## 6. Show saved payment methods to returning payers

When a payer returns to your site, you can show the payer's saved payment methods with the Payment Method Tokens API.

### List all saved payment methods

Make the server-side [list all payment tokens API call](https://developer.paypal.com/docs/api/payment-tokens/v3/#customer_payment-tokens_get) to retrieve payment methods saved to a payer's PayPal-generated customer ID. Based on this list, you can show all saved payment methods to a payer to select during checkout.

> **Important:** Don't expose payment method token IDs on the client side. To protect your payers, create separate IDs for each token and use your server to correlate them.

#### Sample request: List all saved payment methods

Copy and modify the following code.

- Change `CUSTOMER-ID` to a PayPal-generated customer ID.
- Change `ACCESS-TOKEN` to your sandbox app's access token.
- Change `REQUEST-ID` to a set of unique alphanumeric characters such as a time stamp.

```bash theme={null}
curl -L -X GET "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens?customer_id=CUSTOMER-ID"
-H "Content-Type: application/json"
-H "Accept-Language: en_US"
-H "Authorization: Bearer ACCESS-TOKEN"
-H "PayPal-Request-Id: REQUEST-ID" \
```

### Show saved card to payer

Display the saved card to the payer and use the Orders API to make another transaction. Use the vault ID the payer selects as an input to the[Orders API to capture the payment](https://developer/paypal.com/docs/checkout/save-payment-methods/purchase-later/cards/#link-usesavedpaymenttoken).

Use [supported CSS properties](https://developer.paypal.com/docs/checkout/advanced/customize/card-field-style/) to style the card fields. We recommend showing the card brand and last 4 digits.

![Visa ending in 1234](assets/paypal-vault-visa-example.png)

## 7. Integrate back end

The following sample shows a complete back-end integration to save cards for purchase later:

```javascript theme={null}
import "dotenv/config";
import express from "express";
const { PORT = 8888 } = process.env;
const app = express();
app.set("view engine", "ejs");
app.use(express.static("public"));
// Create setup token
app.post("/api/vault/token", async (req, res) => {
  try {
    // Use your access token to securely generate a setup token
    // with an empty payment_source
    const vaultResponse = await fetch(
      "https://api-m.sandbox.paypal.com/v3/vault/setup-tokens",
      {
        method: "POST",
        body: JSON.stringify({
          payment_source: {
            card: {},
          },
        }),
        headers: {
          Authorization: "Bearer \${ACCESS-TOKEN}",
          "PayPal-Request-Id": Date.now(),
        },
      },
    );
    // Return the reponse to the client
    res.json(vaultResponse);
  } catch (err) {
    res.status(500).send(err.message);
  }
});
// Create payment token from a setup token
app.post("/api/vault/payment-token", async (req, res) => {
  try {
    const paymentTokenResult = await fetch(
      "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens",
      {
        method: "POST",
        body: {
          payment_source: {
            token: {
              id: req.body.vaultSetupToken,
              type: "SETUP_TOKEN",
            },
          },
        },
        headers: {
          Authorization: "Bearer \${ACCESS-TOKEN}",
          "PayPal-Request-Id": Date.now(),
        },
      },
    );
    const paymentMethodToken = paymentTokenResult.id;
    const customerId = paymentTokenResult.customer.id;
    await save(paymentMethodToken, customerId);
    res.json(captureData);
  } catch (err) {
    res.status(500).send(err.message);
  }
});
const save = async function (paymentMethodToken, customerId) {
  // Specify where to save the payment method token
};
app.listen(PORT, () => {
  console.log("Server listening at http://localhost:\${PORT}/");
});
```

## 8. Test saving cards

Use the following card numbers to test transactions in the sandbox:

<Accordion title="See test card numbers and types">
  <table>
    <thead>
      <tr>
        <th>Test number</th>
        <th>Card type</th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>`371449635398431`</td>
        <td>American Express</td>
      </tr>

      <tr>
        <td>`376680816376961`</td>
        <td>American Express</td>
      </tr>

      <tr>
        <td>`36259600000004`</td>
        <td>Diners Club</td>
      </tr>

      <tr>
        <td>`6304000000000000`</td>
        <td>Maestro</td>
      </tr>

      <tr>
        <td>`5063516945005047`</td>
        <td>Maestro</td>
      </tr>

      <tr>
        <td>`2223000048400011`</td>
        <td>Mastercard</td>
      </tr>

      <tr>
        <td>`4005519200000004`</td>
        <td>Visa</td>
      </tr>

      <tr>
        <td>`4012000033330026`</td>
        <td>Visa</td>
      </tr>

      <tr>
        <td>`4012000077777777`</td>
        <td>Visa</td>
      </tr>

      <tr>
        <td>`4012888888881881`</td>
        <td>Visa</td>
      </tr>

      <tr>
        <td>`4217651111111119`</td>
        <td>Visa</td>
      </tr>

      <tr>
        <td>`4500600000000061`</td>
        <td>Visa</td>
      </tr>

      <tr>
        <td>`4772129056533503`</td>
        <td>Visa</td>
      </tr>

      <tr>
        <td>`4915805038587737`</td>
        <td>Visa</td>
      </tr>
    </tbody>

  </table>
</Accordion>

Test your integration to see if it saves credit and debit cards as expected. Any errors that occur appear in the `console.error()` method call provided to the `CardFields` component. Test 3DS success, cancel, and fail cases behave as expected.

1. Render the card fields.
2. Create a save button in your UI.
3. When the save button is selected, `session.submit(setupToken)` returns `succeeded` and provides a reference you can store. Update the setup token with card details.
4. On your server, use a server-side call to swap your setup token for a payment token from the Payment Method Tokens API.
   1. For a first-time payer, save the PayPal-generated `customer.id`.
   2. For a returning payer, use the PayPal-generated `customer.id` to swap the `setup-token` for a `payment-token`.
5. Save the `payment-token` for future use. Test a purchase with the payment token.
6. Show saved payment methods:
   1. Make a server-side call to the [list all payment tokens endpoint](https://developer.paypal.com/docs/api/payment-tokens/v3/#customer_payment-tokens_get). Include the PayPal-generated `customer.id`.
   2. Style the card fields.

## Troubleshooting

| Issue                                               | Resolution                                                                                                                                                                                                                             |
| :-------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Vault setup is failing                              | **Check session type:** Verify you're using `createCardFieldsSavePaymentSession()` for vault-only flows, not `createCardFieldsOneTimePaymentSession()`. One-time sessions are for transactions, not vaulting.                          |
| 3D Secure verification is not completing properly   | **Check URLs:** Ensure you've included `return_url` and `cancel_url` in your `experience_context` when requesting SCA verification. These are required for the 3DS challenge flow to redirect users back to your application.          |
| Cannot use vaulted payment methods for transactions | **Check vault reference storage:** Verify that your server is capturing and persisting the payment token returned in the API response after vaulting. Without storing this reference, you won't be able to use the vaulted card later. |

## Optional: Show saved payment methods

We recommend creating a page on your site where payers can see their saved payment methods as in the following example:

![A website showing a payment methods page. The page shows the payer saved a PayPal Wallet and a credit card. The card option is highlighted.](assets/paypal-save-card-without-purchase.png)

## Next step

[Go live](https://developer.paypal.com/api/rest/production/) with your integration.
