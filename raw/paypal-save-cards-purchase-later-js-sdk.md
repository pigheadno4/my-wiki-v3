---
title: Save cards for purchase later with the JavaScript SDK
slug: /docs/checkout/save-payment-methods/purchase-later/js-sdk/cards/
createTime: "2024-07-09T10:00:07.232Z"
updateTime: "2025-07-01T15:02:35.988Z"
---

# Save cards for purchase later with the JavaScript SDK

Save payment methods to charge payers after a set amount of time. For example, you can offer a free trial and charge payers after the trial expires. Payers don't need to be present when charged. No checkout required.

Use the JavaScript SDK to save a payer's card if you aren't [PCI Compliant - SAQ A](https://www.pcisecuritystandards.org/pci_security/completing_self_assessment) but want to save credit or debit cards.

## Availability

Supported countries:

- Australia
- Austria
- Belgium
- Bulgaria
- Canada
- China
- Cyprus
- Czech Republic
- Denmark
- Estonia
- Finland
- France
- Germany
- Hong Kong
- Hungary
- Ireland
- Italy
- Japan
- Latvia
- Liechtenstein
- Lithuania
- Luxembourg
- Malta
- Netherlands
- Norway
- Poland
- Portugal
- Romania
- Singapore
- Slovakia
- Slovenia
- Spain
- Sweden
- United Kingdom
- United States

## Know before you code

- ou are responsible for the front-end user experience. The JavaScript SDK provides back-end support.

- To save payment methods, you must be able to identify payers uniquely. For example, payers create an account and log in to your site.
- Complete the steps in [Get started](https://developer.paypal.com/api/rest/) to get the following sandbox account information from the Developer Dashboard: - Your sandbox account login information
- Your access token

- This client-side integration uses information passed through the CardFields component to save a card without a transaction.
- The JavaScript SDK saves the following card types for purchase later: - American Express
- Discover
- Mastercard
- Visa

- You'll need an existing [advanced credit and debit](/docs/checkout/advanced/) integration. PayPal must approve your business account for advanced credit and debit card payments.

## How it works

PayPal encrypts payment method information and stores it in a digital vault for that customer.

- The payer saves their payment method.
- For a first-time payer, PayPal creates a customer ID. Store this within your system for future use.
- When the customer returns to your website and is ready to check out, pass their PayPal-generated customer ID to the JavaScript SDK. The customer ID tells the JavaScript SDK to save or reuse a saved payment method.
- The payer completes a billing agreement.
- The JavaScript SDK populates the checkout page with each saved payment method. Each payment method appears as a one-click button next to other ways to pay.

The checkout process is now shorter because it uses saved payment information.

## Set up account to save payments

Set up your sandbox and live business accounts to save payment methods:

- Log in to the Developer Dashboard.
- Under **REST API apps** , select your app name.
- Under **Sandbox App Settings** &gt; **App Feature Options** , check **Accept payments** .
- Expand **Advanced options** . Confirm that **Vault** is selected.

Pass your client ID to the SDK to identify yourself. Replace CLIENT-ID with your app's client ID in the following sample:

#### **`SDK to HTML`**

```html
<script src="https://www.paypal.com/sdk/js?components=card-fields&client-id=CLIENT-ID"></script>
```

## Create setup token

You request a setup token from your server. Pass the setup token from your server to the SDK with the createVaultSetupToken callback.

The createVaultSetupToken callback:

- Calls the server endpoint you created to generate and retrieve the setup token.
- Makes a request to your server endpoint.

Then, your server uses its access token to create and return the setup token to the client.

Any errors that occur while creating a setup token show up in the onError callback provided to the card fields component.

Create a setup token for cards that have:

- No verification
- 3D Secure verification

### No verification

| Callback              | Returns              | Description                                                                                                                                                                                                                                                                                                          |
| --------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| createVaultSetupToken | Setup token (string) | Your server must receive this callback. To get a setup token, see[Create a setup token for card](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/cards/#link-createsetuptokenforcard). The SDK then saves the payment method and updates the setup token with payment method details. |

,### 3D Secure verification

| Callback              | Returns              | Description                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| createVaultSetupToken | Setup token (string) | Your server must receive this callback. Send either"SCA_ALWAYS"or"SCA_WHEN_REQUIRED"inverification_methodwith this request's body. To get a setup token, see[Create a setup token for card](/docs/checkout/save-payment-methods/purchase-later/cards/#link-createsetuptokenforcard). The SDK then saves the payment method and updates the setup token with payment method details. |

#### **`Front-end sample for No verification`**

```javascript
const cardFields = paypal.CardFields({
      createVaultSetupToken: () => {
          // Call your server API to generate a vaultSetupToken and return it here as a string
        const result = await fetch("example.com/create/setup/token")
        return result.token
      },
      onError: (error) => {
        // Capture and log errors from the SDK
      }
    })
```

#### **`Front-end sample for 3D Secure`**

```javascript
 const cardFields = paypal.CardFields({
        createVaultSetupToken: () => {
        // Call your server API to generate a vaultSetupToken
        // Send the SCA_ALWAYS or SCA_WHEN_REQUIRED contingency with the request body
        // and return it here as a string
        const result = await fetch("example.com/create/setup/token")
        return result.token
          },
        onError: (error) => {
        // Capture and log errors from the SDK
      }
      })
```

Make this request from your server.

This setup token is generated with an empty card in the payment_source object. PayPal hosted fields use this token to securely update the setup token with card details.

#### **`Back-end sample`**

```curl
 curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens' \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS-TOKEN" \
 -H "PayPal-Request-Id: REQUEST-ID" \
 -d '{
      "payment_source": {
        "card": {}
      }
  }'
```

#### Modify the code

- Change ACCESS-TOKEN to your sandbox app's access token.
- Change REQUEST-ID to a set of unique alphanumeric characters such as a time stamp.
- In the createVaultSetupToken , call the endpoint on your server to create a setup token with the [Payment Method Tokens API](/docs/api/payment-tokens/v3/) . createVaultSetupToken returns the setup token as a string.

## 4. Initialize card fields to save data

After the SDK has a setup token, it renders card fields for the payer to submit card details. The SDK then returns the vaultSetupToken to the merchant through the onApprove callback.

When you complete this step, CardFields are ready to save card details for later use. ### Supported callback

### No verification

| Callback  | Returns                     | Description                                                                                                       |
| --------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| onApprove | { vaultSetupToken: string } | You get the updatedvaultSetupTokenwhen the payment method is saved. Store thevaultSetupTokentoken in your system. |

,### 3D Secure

| Callback  | Returns                                             | Description                                                                                                                        |
| --------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| onApprove | { vaultSetupToken: string, liabilityShift: string } | You get the updatedvaultSetupTokenandliabilityShiftwhen the payment method is saved. Store thevaultSetupTokentoken in your system. |

### Front-end sample for No verification

#### **`Initialize card fields: Front-end sample for No verfication`**

```javascript
const cardFields = paypal.CardFields({
  createVaultSetupToken: () => {
    // Call your server API to generate a vaultSetupToken
    // and return it here as a string
    const result = await fetch("example.com/create/setup/token")
    return result.token
  }
  onApprove: ({
    vaultSetupToken
  }) => {
    // Send the vaultSetupToken to your server
    // for the server to generate a payment token
        return fetch("example.com/create/payment/token", { body: JSON.stringify({ vaultSetupToken }) })
  },
  ...
})
```

### Front-end sample for 3D Secure

#### **`Initialize card fields: Front-end sample for 3D secure `**

```javascript
 const cardFields = paypal.CardFields({
          createVaultSetupToken: () => {
              // Call your server API to generate a vaultSetupToken
              // and return it here as a string
              const result = await fetch("example.com/create/setup/token")
              return result.token
          }
          onApprove: ({ vaultSetupToken }) => {
              // Send the vaultSetupToken to your server for later use
          },
          ...
      })
```

### Back-end sample

Make this request from your server.

#### **`Initialize card fields: Back-end sample`**

```curl
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v3/vault/payment-tokens' \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS-TOKEN" \
 -H "PayPal-Request-Id: REQUEST-ID" \
 -d '{
      "payment_source": {
          "token": {
              "id": "VAULT-SETUP-TOKEN",
              "type": "SETUP_TOKEN"
          }
      }
  }'
```

###

#### Modify the code

- Pass the vaultSetupToken returned by onApprove to your server.
- Change ACCESS-TOKEN to your sandbox app's access token.
- Change REQUEST-ID to a set of unique alphanumeric characters such as a time stamp.
- Change VAULT-SETUP-TOKEN to the value passed from the client.
- Save the resulting payment token returned from the API to use in future transactions.

###

### Avoid validation errors

CardFields can't be configured with both the createOrder callback and the createVaultSetupToken callback. When saving cards, only pass createVaultSetupToken .

#### **`Initialize card fields: Avoid validation errors`**

```javascript
// Throws a validation error: can't call both 'createVaultSetupToken' and 'createOrder'
paypal.CardFields({
    createVaultSetupToken: () => {...},
    createOrder: () => {...}
})
```

## Show error page

If an error prevents checkout, alert the payer that an error has occurred using the onError callback.

**info**
This script doesn't handle specific errors. It shows a specified error page for all errors.

#### **`Show error page code sample`**

```javascript
paypal.CardFields({
  onError(err) {
    console.error("Something went wrong:", error);
  },
});
```

### Supported callback

| Callback                                                                | Returns | Description                                                                  |
| ----------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------------- |
| onError                                                                 | void    | Implement the optionalonError()function to handle errors and display generic |
| error message or page to the buyers. This error handler is a catch-all. |

#### **`Handle 3D Secure Cancel `**

```javascript
paypal.CardFields({
  onCancel() {
    console.log("Your order was cancelled due to incomplete verification");
  },
});
```

### Supported callback

| Callback | Returns | Description                                                                                           |
| -------- | ------- | ----------------------------------------------------------------------------------------------------- |
| onCancel | void    | Called when the customer closes 3D Secure verification modal. This also means the order is cancelled. |

## Show saved payment methods to returning payers

When a payer returns to your site, you can show the payer's saved payment methods with the Payment Method Tokens API.

### List all saved payment methods

Make the server-side [list all payment tokens API call](https://developer.paypal.com/docs/api/payment-tokens/v3/#customer_payment-tokens_get) to retrieve payment methods saved to a payer's PayPal-generated customer ID. Based on this list, you can show all saved payment methods to a payer to select during checkout.

**info**
Don't expose payment method token IDs on the client side. To protect your payers, create separate IDs for each token and use your server to correlate them.

### Sample request: List all saved payment methods

#### **`Sample request: List all saved payment methods`**

```curl
 curl -L -X GET "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens?customer_id=CUSTOMER-ID"\
 -H "Content-Type: application/json" \
 -H "Accept-Language: en_US" \
 -H "Authorization: Bearer ACCESS-TOKEN" \
 -H "PayPal-Request-Id: REQUEST-ID"
```

####

#### Modify the code

- Change CUSTOMER-ID to a PayPal-generated customer ID.
- Change ACCESS-TOKEN to your sandbox app's access token.
- Change REQUEST-ID to a set of unique alphanumeric characters such as a time stamp.

### Show saved card to payer

Display the saved card to the payer and use the Orders API to make another transaction. Use the vault ID the payer selects as an input to the [Orders API to capture the payment](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/cards/#link-usesavedpaymenttoken) .

Use [supported CSS properties](https://developer.paypal.com/docs/checkout/advanced/customize/card-field-style/) to style the card fields. We recommend showing the card brand and last 4 digits.

![Visa,ending,in,1234](assets/paypal-save-card-visa-example.png)

The following sample shows a complete back-end integration to save cards for purchase later:

#### **`Integrate back end`**

```javascript
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
        body: JSON.stringify({ payment_source: { card: {} } }),
        headers: {
          Authorization: "Bearer ${ACCESS-TOKEN}",
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
          Authorization: "Bearer ${ACCESS-TOKEN}",
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
  console.log("Server listening at http://localhost:${PORT}/");
});
```

The following sample shows how a full script to save cards might appear in HTML:

#### **`Integrate front end`**

```html
<!DOCTYPE html>
<html>
  <head>
    <!-- Add meta tags for mobile and IE -->
    <meta charset="utf-8" />
  </head>
  <body>
    <!-- Include the PayPal JavaScript SDK -->
    <script src="https://www.paypal.com/sdk/js?components=card-fields&client-id=YOUR-CLIENT-ID&currency=USD"></script>
    <div align="center">or</div>
    <!-- Advanced credit and debit card payments form -->
    <div class="card_container">
      <div id="card-number"></div>
      <div id="expiration-date"></div>
      <div id="cvv"></div>
      <div id="card-holder-name"></div>
      <label> <input type="checkbox" id="vault" name="vault" /> Vault </label>
      <br /><br />
      <button value="submit" id="submit" class="btn">Pay</button>
    </div>
    ​
    <!-- Implementation -->
    <script>
      const cardFields = paypal.CardFields({
        createVaultSetupToken: async () => {
          // Call your server API to generate a vaultSetupToken
          // and return it here as a string
          const result = await fetch("https://example.com/api/vault/token", {
            method: "POST",
          });
          const { id } = await result.json();
          return id;
        },
        onApprove: async (data) => {
          // Only for 3D Secure
          if (data.liabilityShift) {
            // Handle liability shift
          }
          const result = await fetch(
            "https://example.com/api/vault/payment-token",
            {
              method: "POST",
              body: JSON.stringify(data),
            },
          );
          // id is the payment ID
          const { id } = await result.json();
        },
        onError: (error) => console.error("Something went wrong:", error),
      });
      // Check eligibility and display advanced credit and debit card payments
      if (cardFields.isEligible()) {
        cardFields.NameField().render("#card-holder-name");
        cardFields.NumberField().render("#card-number");
        cardFields.ExpiryField().render("#expiration-date");
        cardFields.CVVField().render("#cvv");
      } else {
        // Handle the workflow when credit and debit cards are not available
      }
      const submitButton = document.getElementById("submit");
      submitButton.addEventListener("click", () => {
        cardFields
          .submit()
          .then(() => {
            console.log("submit was successful");
          })
          .catch((error) => {
            console.error("submit erred:", error);
          });
      });
    </script>
  </body>
</html>
```

**info**
This setup token is generated with an empty payment_source . The CardFields script uses this token to securely update the setup token with payment details.

## Test saving cards

Use the following card numbers to test transactions in the sandbox:

**See test card numbers and types**

| Test number      | Card type        |
| ---------------- | ---------------- |
| 371449635398431  | American Express |
| 376680816376961  | American Express |
| 36259600000004   | Diners Club      |
| 6304000000000000 | Maestro          |
| 5063516945005047 | Maestro          |
| 2223000048400011 | Mastercard       |
| 4005519200000004 | Visa             |
| 4012000033330026 | Visa             |
| 4012000077777777 | Visa             |
| 4012888888881881 | Visa             |
| 4217651111111119 | Visa             |
| 4500600000000061 | Visa             |
| 4772129056533503 | Visa             |
| 4915805038587737 | Visa             |

Test your integration to see if it saves credit and debit cards as expected. Any errors that occur appear in the onError callback provided to the CardFields component.

- Render the card fields.
- Create a save button in your UI.
- When the save button is selected: - Create a setup token.
- Update the setup token with card details.

- On your server, use a server-side call to swap your setup token for a payment token from the Payment Method Tokens API. - For a first-time payer, save the PayPal-generated customer.id .
- For a returning payer, use the PayPal-generated customer.id to swap the setup-token for a payment-token .

- Save the payment-token for future use.
- Show saved payment methods: - Make a server-side call to the [list all payment tokens endpoint](https://developer.paypal.com/docs/api/payment-tokens/v3/#customer_payment-tokens_get) . Include the PayPal-generated customer.id .
- Style the card fields.

## Optional: Show saved payment methods

We recommend creating a page on your site where payers can see their saved payment methods as in the following example:

![A,website,showing,a,payment,methods,page.,The,page,shows,the,payer,saved,a,PayPal,Wallet,and,a,credit,card.,The,card,option,is,highlighted.](assets/paypal-save-card-wo-purchase.png)

## Next step

[Go live](https://developer.paypal.com/api/rest/production/) with your integration.
