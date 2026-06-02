---
title: Save PayPal for purchase later with the JavaScript SDK
slug: /docs/checkout/save-payment-methods/purchase-later/js-sdk/paypal/
createTime: "2024-10-24T11:54:50.103Z"
updateTime: "2025-08-25T11:29:32.706Z"
---

# Save PayPal for purchase later with the JavaScript SDK

Save payment methods to charge payers after a set amount of time. For example, you can offer a free trial and charge payers after the trial expires. Payers don't need to be present when charged. No checkout required.

To save PayPal Wallets, payers need to log in to your site, make a purchase, and remain on your site when transactions take place.

Customers with a PayPal Wallet can:

- Review PayPal transactions and transaction history
- Review, add, or remove funding sources
- Review and cancel recurring payments
- Hold a balance in their PayPal account
- Use PayPal to send and receive money
- Withdraw money to a linked bank account
- Use PayPal to transact with merchants

## Availability

#### See Supported Countries

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

PayPal encrypts payment method information and stores it in a digital vault for that customer.

- The payer saves their payment method.
- For a first-time payer, PayPal creates a customer ID. Store this within your system for future use.
- When the customer returns to your website and is ready to check out, pass their PayPal-generated customer ID to the JavaScript SDK. The customer ID tells the JavaScript SDK to save or reuse a saved payment method.
- The payer completes a billing agreement.
- The JavaScript SDK populates the checkout page with each saved payment method. Each payment method appears as a one-click button next to other ways to pay.

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

## Generate user ID token for payer

The PayPal OAuth 2.0 API has a has a response_type parameter. Set the response_type to id_token to retrieve a unique ID token for a payer.

### First-time Payer

A payer wants to save a payment method for the first time. Modify the following code to generate an id_token for the payer:

### Sample server-side user ID token request

1curl-s -X POST'https://api-m.sandbox.paypal.com/v1/oauth2/token'\2-u'CLIENT-ID:CLIENT-SECRET'\3-H'Content-Type: application/x-www-form-urlencoded'\4-d'grant_type=client_credentials'\5-d'response_type=id_token'### Modify the code
Copy the code sample and modify it as follows:

- Change CLIENT-ID to your client ID.
- Change CLIENT-SECRET to your client secret.

,### Returning Payer
A payer wants to use a saved payment method.

Use the saved PayPal-generated customer ID in the POST body parameter target_customer_id . The target_customer_id is a unique ID for a customer generated when the payment_source is saved to the vault. The target_customer_id is available when capturing the order or retrieving saved payment information.

**Note:** Use the customer identifier generated by PayPal, not the identifier that you use to identify the customer in your system.

### Sample server-side user ID token request with a customer ID

1curl-s -X POST'https://api-m.sandbox.paypal.com/v1/oauth2/token'\2-u'CLIENT-ID:CLIENT-SECRET'\3-H'Content-Type: application/x-www-form-urlencoded'\4-d'grant_type=client_credentials'\5-d'response_type=id_token'\6-d'target_customer_id=CUSTOMER-ID'### Modify the code
Copy the code sample and modify it as follows:

- Change CLIENT-ID to your client ID.
- Change CLIENT-SECRET to your client secret.
- Change CUSTOMER-ID to the PayPal-generated customer ID.

A successful request returns fields including an access_token , id_token , and the number of seconds the access_token token is valid.

The id_token :

- Uniquely identifies each payer.
- Expires in a few minutes because it's meant to be used during checkout. Generate new tokens if the current tokens expire.

**Tip** : Each buyer session is unique. Set up your server to generate a new client token each time payment fields render on your page.

Pass the id_token into the JavaScript SDK through the data-user-id-token .

#### **`Pass the id_token`**

```javascript
<script
  src="https://www.paypal.com/sdk/js?client-id=CLIENT-ID"
  data-user-id-token="ID-TOKEN"
></script>
```

### Modify the code

Copy the code sample and modify it as follows:

- Change CLIENT-ID to your client ID.
- Change ID-TOKEN to the id_token from the previous step.

Include client-side callbacks to:

- Manage interactions with APIs
- Manage payer approval flows
- Handle any events that lead to cancellation or error during payer approval

#### **`Add PayPal button-code`**

```javascript

      <div id="your-div-id"></div>
<script>
    window.paypal.Buttons({
        createVaultSetupToken: async () => {},
        onApprove: async ({ vaultSetupToken }) => {},
        onError: (error) => {}
    }).render("#your-div-id");
</script>

```

### Modify the code

Copy the code sample and modify it as follows:

- Replace your-div-id with a div id of your choice.
- Replace #your-div-id with the div id you created.

## Create setup token

You request a setup token from your server. Pass the setup token from your server to the SDK with the createVaultSetupToken callback.

The createVaultSetupToken callback:

- Calls the server endpoint you created to generate and retrieve the setup token.
- Makes a request to your server endpoint.

Then, your server uses its access token to create and return the setup token to the client.

Any errors that occur while creating a setup token show up in the onError callback provided to the card fields component.

### Supported callback

| Callback              | Returns              | Description                                                                                                                                                                                                                                                                                                                               |
| --------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| createVaultSetupToken | Setup token (string) | The merchant's server must receive this callback.[Create a setup token for cards from the merchant server](https://developer.paypal.com/docs/multiparty/checkout/save-payment-methods/purchase-later/cards/#link-createsetuptokenforcard). The SDK then saves the payment method and updates the setup token with payment method details. |

### Client-side code sample

1window.paypal.Buttons({2createVaultSetupToken:async()=&gt;{3// Call your server API to generate a setup token4// and return it here as a string5constresult=awaitfetch("https://example.com/create/setup/token")6returnresult.token7}8})### Modify the code
Copy the code sample and modify it as follows:

- Change ACCESS-TOKEN to your sandbox app's access token.
- Change REQUEST-ID to a set of unique alphanumeric characters such as a time stamp.
- Set the usage_type under payment_source.paypal to be PLATFORM .
- In the createVaultSetupToken , call the endpoint on your server to create a setup token with the [Payment Method Tokens API](https://developer.paypal.com/docs/api/payment-tokens/v3/) . createVaultSetupToken returns the setup token as a string.

### Server-side code sample

Set up your server to call the [Payment Method Tokens API](https://developer.paypal.com/docs/api/payment-tokens/v3/) . The button that the payer selects determines the payment_source sent in the following sample.

This SDK uses the Payment Method Tokens API to save payment methods in the background. Use the following request to add attributes needed to save a PayPal Wallet:

**Note:** The return_url and cancel_url values are required, but can have filler values such as in the following sample.

1curl-v -k -X POST'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens'\2-H'Content-Type: application/json'\3-H'Authorization: Bearer ACCESS-TOKEN'\4-H'PayPal-Request-Id: REQUEST-ID'\5-d'{6"payment_source": {7"paypal": {8"usage_type": "MERCHANT",9"experience_context": {10"return_url": "https://example.com/returnUrl",11"cancel_url": "https://example.com/cancelUrl"12}13}14}15}'### Response
Return the id to your client to call for the payer approval flow if the payment_source needs payer approval.

1{2"id":"4G4976650J0948357",3"customer":{4"id":"customer_4029352050"5},6"status":"PAYER_ACTION_REQUIRED",7"payment_source":{8"paypal":{9"description":"Description for PayPal to be shown to PayPal payer",10"usage_pattern":"IMMEDIATE",11"shipping":{12"name":{13"full_name":"Firstname Lastname"14},15"address":{16"address_line_1":"123 Main Street",17"address_line_2":"Unit A",18"admin_area_2":"Anytown",19"admin_area_1":"CA",20"postal_code":"12345",21"country_code":"US"22}23},24"permit_multiple_payment_tokens":false,25"usage_type":"MERCHANT",26"customer_type":"CONSUMER"27}28},29"links":[30{31"href":"https://api-m.sandbox.paypal.com/v3/vault/setup-tokens/4G4976650J0948357",32"rel":"self",33"method":"GET",34"encType":"application/json"35},36{37"href":"https://sandbox.paypal.com/agreements/approve?approval_session_id=4G4976650J0948357",38"rel":"approve",39"method":"GET",40"encType":"application/json"41}42]43}**Note:** This setup token is generated with an empty payment_source . The Buttons script uses this token to securely update the setup token with payment details.

### Modify the code

- Change ACCESS-TOKEN to your sandbox app's access token.
- Change REQUEST-ID to a set of unique alphanumeric characters such as a time stamp.
- In the createVaultSetupToken , call the endpoint on your server to create a setup token with the [Payment Method Tokens API](https:/docs/api/payment-tokens/v3/) . createVaultSetupToken returns the setup token as a string.

### Payer approval

If payer approval is required, the client SDK calls the payer approval flow. The approval flow takes the payer through PayPal Checkout.

You can store a Merchant Customer ID aligned with your system to simplify the mapping of customer information within your system and PayPal when creating a payment token. This is an optional field that will return the value shared in the response.

Use an approved setup token to save the payer's payment method to the vault. Then, copy the sample request code to generate a payment token:

### Supported callback

| Callback                                                                                                                                                                                                                                                                                                     | Returns                     | Description                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| [](https://developer.paypal.com/docs/multiparty/checkout/save-payment-methods/purchase-later/js-sdk/paypal/#onapprove{-vaultsetuptoken:-string-}the-merchant-gets-the-updated-vaultsetuptoken-when-the-payment-method-is-saved.-the-merchant-must-store-the-vaultsetuptoken-token-in-their-system.)onApprove | { vaultSetupToken: string } | The merchant gets the updatedvaultSetupTokenwhen the payment method is saved. The merchant must store thevaultSetupTokentoken in their system. |

### Client-side sample request

Modify the following request to match your server endpoint and payload:

#### **`Client-side sample request code`**

```javascript
window.paypal.Buttons({
  onApprove: ({ vaultSetupToken }) => {
    // Send the vaultSetupToken to your server
    // for your server to generate a payment token
    return fetch("example.com/create/payment/token", {
      body: JSON.stringify({ vaultSetupToken }),
    });
  },
});
```

### Sample API request

1curl-v -k -X POST'https://api-m.sandbox.paypal.com/v3/vault/payment-tokens'\2-H'Content-Type: application/json'\3-H'Authorization: Bearer ACCESS-TOKEN'\4-H'PayPal-Request-Id: REQUEST-ID'\5-d'{6"payment_source": {7"token": {8"id": "4G4976650J0948357",9"type": "SETUP_TOKEN"10}11}12}'#### Modify the code
Copy the code sample and modify it as follows:

- Change ACCESS-TOKEN to your sandbox access token.
- Change REQUEST-ID to a unique alphanumeric set of characters such as a time stamp.
- Use token as the payment source and complete the rest of the source object for your use case and business.
- Use your setup token ID to pass in the payment source parameter and type as the SETUP_TOKEN .

#### Step result

A successful request results in the following:

- An HTTP response code of 200 or 201 . Returns 200 for an idempotent request.
- ID of the payment token and associated payment method information.
- HATEOAS links:

| Rel    | Method | Description                                                                      |
| ------ | ------ | -------------------------------------------------------------------------------- |
| delete | DELETE | Make a DELETE request to delete the payment token.                               |
| self   | GET    | Make a GET request to this link to retrieve data about the saved payment method. |

#### Sample API response

1{2"id":"jwgvx42",3"customer":{4"id":"customer_4029352050"5},6"payment_source":{7"paypal":{8"description":"Description for PayPal to be shown to PayPal payer",9"usage_pattern":"IMMEDIATE",10"shipping":{11"name":{12"full_name":"Firstname Lastname"13},14"address":{15"address_line_1":"123 Main St",16"address_line_2":"Unit A",17"admin_area_2":"Anytown",18"admin_area_1":"CA",19"postal_code":"12345",20"country_code":"US"21}22},23"permit_multiple_payment_tokens":false,24"usage_type":"MERCHANT",25"customer_type":"CONSUMER",26"email_address":"payer@example.com",27"payer_id":"AJM9JTWQJCFTA"28}29},30"links":[31{32"rel":"self",33"href":"https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/jwgvx42",34"method":"GET",35"encType":"application/json"36},37{38"rel":"delete",39"href":"https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/jwgvx42",40"method":"DELETE",41"encType":"application/json"42}43]44}
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
    const vaultResponse = await fetch("https://api-m.sandbox.paypal.com/v3/vault/setup-tokens", {
        method: "POST",
        body: JSON.stringify({ payment_source: { paypal: {}} }),
        headers: {
            Authorization: 'Bearer ${ACCESS-TOKEN}'',
            "PayPal-Request-Id": Date.now(),
        }
    })
    // Return the reponse to the client
    res.json(vaultResponse);
  } catch (err) {
    res.status(500).send(err.message);
  }
})
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
                      type: "SETUP_TOKEN"
                  }
              }
          },
          headers: {
            Authorization: 'Bearer ${ACCESS-TOKEN}',
            "PayPal-Request-Id": Date.now(),
          }
        })
    const paymentMethodToken = paymentTokenResult.id
    const customerId = paymentTokenResult.customer.id
    await save(paymentMethodToken, customerId)
    res.json(captureData);
  } catch (err) {
    res.status(500).send(err.message);
  }
})
const save = async function(paymentMethodToken, customerId) {
    // Specify where to save the payment method token
}
app.listen(PORT, () => {
  console.log('Server listening at http://localhost:${PORT}/');
})

```

The following sample shows how a full script to save PayPal might appear in HTML:

#### **`Integrate front end`**

```javascript

      <div id="paypal-buttons-container"></div>
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT-ID&merchant-id=MERCHANT-ID" data-user-id-token="ID-TOKEN"></script>
<script>
    window.paypal.Buttons({
        createVaultSetupToken: async () => {
                // Call your server API to generate a setup token
                // and return it here as a string
                const result = await fetch("example.com/create/setup/token", { method: "POST" })
                return result.token
        },
        onApprove: async ({ vaultSetupToken }) => {
            return fetch("example.com/create/payment/token", { body: JSON.stringify({ vaultSetupToken }) })
        },
        onError: (error) => {
            console.log("An error occurred: ", error)
        }
    }).render("#paypal-buttons-container");
</script>

```

## Test your integration

- Render a PayPal Button with callbacks defined.
- Select the button and complete the pop-up flow to approve saving the PayPal Wallet.
- On your server, save the vaultSetupToken and the PayPal-generated customer.id . Associate these tokens with the designated payer.
- Make a call on your server to swap your setup token for a payment token from the Payment Method Tokens API.
- Save or use an existing customer.id depending on whether the payer is a first-time payer or returning payer: - For a first-time payer, save the PayPal-generated customer.id . The customer.id identifies the payer and their saved payment methods.
- For a returning payer, use the PayPal-generated customer.id to swap the setup-token for a payment-token .

- Save the payment-token for future use.

##

## Optional: Show saved payment methods

We recommend creating a page on your site where payers can see their saved payment methods as in the following example:

![A,website,showing,a,payment,methods,page.,The,page,shows,the,payer,saved,a,PayPal,Wallet,and,a,credit,card.,The,PayPal,Wallet,option,is,highlighted](assets/paypal-save-pp-wo-purchase.png)

## Next step

[Go live](https://developer.paypal.com/api/rest/production/) with your integration.
