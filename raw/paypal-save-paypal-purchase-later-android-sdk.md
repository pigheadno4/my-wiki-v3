---
title: Save PayPal for purchase later with the Android SDK
slug: /docs/checkout/save-payment-methods/purchase-later/android-sdk/paypal/
createTime: "2025-02-25T08:22:59.091Z"
updateTime: "2025-02-27T08:48:19.627Z"
---

# Save PayPal for purchase later with the Android SDK

Allow customers to save their PayPal Wallets and charge them after a set amount of time. For example, you can offer a free trial and charge payers after the trial expires. Payers don't need to be present when charged and no checkout is required.

Customers with a PayPal Wallet can:

- Review PayPal transactions and transaction history
- Review, add, or remove funding sources
- Review and cancel recurring payments
- Hold a balance in their PayPal account
- Use PayPal to send and receive money
- Withdraw money to a linked bank account
- Use PayPal to transact with merchants

## Availability

See supported countries:- Australia

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

## Use cases

Businesses save payment methods if they want customers to:

- Check out without re-entering a payment method
- Pay after use, for example, ride-sharing and food delivery

## Know before you code

- To save payment methods, you must be able to identify payers uniquely. For example, payers create an account and log in to your site.
- Complete the steps in [Get started](/api/rest/) to get the following sandbox account information from the Developer Dashboard: - Your sandbox account login information
- Your access token

- This integration requires a PayPal Developer account.
- This integration must include a server-side call to exchange a setup token for a payment method token.

## How it works

PayPal encrypts payment method information and stores it in a digital vault for that custome

- The payer saves their payment method.
- For a first-time payer, PayPal creates a customer ID. Store this within your system for future use.
- Use the customer ID to retrieve saved payment methods and add new ones for existing customers in your application.

The checkout process is now shorter because it uses saved payment information.

## Check eligibility

- Go to [paypal.com](https://www.paypal.com) and sign in with your business account.
- Go to **Account Settings** &gt; **Payment Preferences** &gt; **Save PayPal and Venmo payment methods** .
- In the Save PayPal and Venmo payment methods section, select **Get Started** .
- When you submit profile details, PayPal reviews your eligibility to save PayPal Wallets and Venmo accounts.
- After PayPal reviews your eligibility, you'll see a status of **Success** , **Need more information** , or **Denied** .

## Set up account to save payments

Set up your sandbox and live business accounts to save payment methods:

- Log in to the Developer Dashboard.
- Under **REST API apps** , select your app name.
- Under **Sandbox App Settings** &gt; **App Feature Options** , check **Accept payments** .
- Expand **Advanced options** . Confirm that **Vault** is selected.

To go live, you'll need to be vetted to save PayPal Wallets. You can start the vetting process from the Developer Dashboard.

- Only your sandbox business account is enabled to save payment methods. Your developer account remains unaffected.
- You'll complete production onboarding when you're ready to go live.

**Tip:** When prompted for data such as a phone number for a sandbox business request, enter any number that fits the required format. Since this is a sandbox request, the data doesn't have to be real.

Add the PayPalWebPayments package dependency for your app using a Gradle dependency:

Add the following dependency to your app's build.gradle file.

#### **`Groovy`**

```curl
dependencies {
  implementation 'com.paypal.android:paypal-web-payments:<CURRENT-VERSION>'
}
```

#### **`Kotlin`**

```kotlin
dependencies {
  implementation('com.paypal.android:paypal-web-payments:<CURRENT-VERSION>')
}
```

Add a button to your app's UI:

#### **`Add PayPal Button`**

```javascript
Button("PayPal") {
    // Create a setup token server-side (see next step)
}
```

Request a setup token from your server, create a PayPalVaultRequest object, and call the vault() method.

#### **`Client-side code sample`**

```kotlin
// Client-side code sample

val coreConfig = CoreConfig(CLIENT_ID)
val setupTokenResponse = createVaultSetupToken()
val vaultRequest = PayPalWebVaultRequest(setupTokenResponse.setupTokenId)

val paypalClient = PayPalWebCheckoutClient(activity, coreConfig, URL_SCHEME)
paypalClient.vaultListener = this
paypalClient.vault(vaultRequest)

override fun onPayPalWebVaultSuccess(result: PayPalWebVaultResult) {
    // Handle success
}

override fun onPayPalWebVaultFailure(error: PayPalSDKError) {
    // Handle failure
}

override fun onPayPalWebVaultCanceled() {
    // Handle cancellation
}
```

### Modify the code

Copy the code sample and modify it as follows:

- Change CLIENT_ID to your clientId.
- Replace URL_SCHEME with the custom URL scheme used to return to your app.
- Implement the callback listeners to handle success, failure, and cancellation.
- In the createPayPalSetupToken method, call the endpoint on your server to create a setup token with the [Payment Method Tokens API](https:/docs/api/payment-tokens/v3/) . createPayPalSetupToken returns the setup token as a string.

Set up your server to call the [Payment Method Tokens API](https:/docs/api/payment-tokens/v3/)

The SDK uses the Payment Method Tokens API to save payment methods in the background. Use the following request as a template to create a setup token.

**Note:** The return_url and cancel_url values are required, but can have filler values such as in the following sample.

#### **`Server-side code sample`**

```curl
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: Bearer ACCESS-TOKEN' \
 -H 'PayPal-Request-Id: REQUEST-ID' \
 -d '{
            "payment_source": {
                "paypal": {
                  "usage_type": "PLATFORM",
                  "experience_context": {
                    "return_url": "https://example.com/returnUrl",
                    "cancel_url": "https://example.com/cancelUrl"
                  }
                }
            }
        }'
```

### Modify the code

- Change ACCESS-TOKEN to your sandbox app's access token.
- Change REQUEST-ID to a set of unique alphanumeric characters such as a timestamp.

#### **`Response Code - Create setup token`**

```javascript

  {
    "id": "4G4976650J0948357",
    "customer": {
      "id": "customer_4029352050"
    },
    "status": "PAYER_ACTION_REQUIRED",
    "payment_source": {
      "paypal": {
        "description": "Description for PayPal to be shown to PayPal payer",
        "usage_pattern": "IMMEDIATE",
        "shipping": {
          "name": {
            "full_name": "Firstname Lastname"
          },
          "address": {
            "address_line_1": "123 Main Street",
            "address_line_2": "Unit A",
            "admin_area_2": "Anytown",
            "admin_area_1": "CA",
            "postal_code": "12345",
            "country_code": "US"
          }
        },
        "permit_multiple_payment_tokens": false,
        "usage_type": "PLATFORM",
        "customer_type": "CONSUMER"
      }
    },
    "links": [
      {
        "href": "https://api-m.sandbox.paypal.com/v3/vault/setup-tokens/4G4976650J0948357",
        "rel": "self",
        "method": "GET",
        "encType": "application/json"
      },
      {
        "href": "https://sandbox.paypal.com/agreements/approve?approval_session_id=4G4976650J0948357",
        "rel": "approve",
        "method": "GET",
        "encType": "application/json"
      }
    ]
  }
```

### Payer approval

Convert the setup token to a payment token that can be used to process a transaction:

Convert the setup token to a payment token that can be used to process a transaction:

#### **`Create a payment token with the vault setup token code`**

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

### Modify the code

- Change ACCESS-TOKEN to your sandbox app's access token.
- Change REQUEST-ID to a set of unique alphanumeric characters such as a timestamp.
- Change VAULT-SETUP-TOKEN to the value passed from the client.
- Save the resulting payment token returned from the API to use in future transactions.

The following sample shows a complete back-end integration to save PayPal for purchase later:

#### **`Integrate back end`**

```javascript
import "dotenv/config";
import express from "express";
const { PORT = 8888 } = process.env;
const app = express();
app.set("view engine", "ejs");
app.use(express.static("public"));

// Create setup token
app.post("/create/setup/token", async (req, res) => {
  try {
    // Use your access token to securely generate a setup token
    // with an empty payment_source
    const vaultResponse = await fetch(
      "https://api-m.sandbox.paypal.com/v3/vault/setup-tokens",
      {
        method: "POST",
        body: JSON.stringify({ payment_source: { paypal: {} } }),
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
app.post("/create/payment/token/", async (req, res) => {
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

## Test your integration

- In your app, render a PayPal button and initate the vault.
- Create a setup token.
- Call the vault function in the SDK.
- Create a payment token with the updated setup token.
- Store the PayPal-generated customer ID in your system.
- Log in to [sandbox](https://www.sandbox.paypal.com/) with your merchant account and verify the transaction.
- Return to your app and initiate another transaction. Use the PayPal-generated payment token as a payment source.
- Verify that the transaction captures successfully without having to complete PayPal Web Checkout again.

## Optional: Show saved payment methods

Create a view where payers can see their payment methods using the [Payment Method Tokens API](https:/docs/api/payment-tokens/v3/#customer_payment-tokens_get)

## Next step

[Go live](https:/api/rest/production/) with your integration.
