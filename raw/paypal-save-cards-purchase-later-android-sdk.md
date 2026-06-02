---
title: "Save cards for purchase later with the Android SDK "
slug: /docs/checkout/save-payment-methods/purchase-later/android-sdk/cards/
createTime: "2024-12-18T10:00:05.732Z"
updateTime: "2025-03-11T23:28:17.587Z"
---

# Save cards for purchase later with the Android SDK

Save customer credit or debit cards to charge them at a later time. For
example, you can offer a free trial and charge payers after the trial expires.
Payers don't need to be present when charged and no checkout is required.

Use the Android SDK to save a payer's credit or debit cards.

## Availability

### See supported countries

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

- To save payment methods, you must be able to identify payers uniquely. For
  example, payers create an account and log in to your app.
- Complete the steps in [Get started](https:/api/rest/) to get
  the following sandbox account information from the Developer Dashboard: - Your sandbox account login information
- Your access token

- The Android SDK saves the following card types for purchase later: - American Express
- Discover
- Mastercard
- Visa

- You'll need an existing [advanced credit and debit](https:/docs/checkout/advanced/android) integration. PayPal must approve your business account for advanced credit
  and debit card payments.

## How it works

PayPal encrypts payment method information and stores it in a digital vault
for that customer.

- The payer saves their payment method.
- For a first-time payer, PayPal creates a customer ID. Store this within your
  system for future use.
- Use the customer ID to retrieve saved payment methods and add new ones for
  existing customers in your application.

The checkout process is now shorter because it uses saved payment information.

## 1. Set up account to save payments

Set up your sandbox and live business accounts to save payment methods:

- Log in to the Developer Dashboard.
- Under **REST API apps** , select your app name.
- Under **Sandbox App Settings** &gt; **App Feature Options** , check **Accept payments** .
- Expand **Advanced options** . Confirm that **Vault** is selected.

## 2. Add the CardPayments module to your app

Add the CardPayments package as a Gradle dependency in your app:

- Groovy
- Kotlin

Add the following dependency to your app'sbuild.gradlefile.1dependencies {2implementation 'com.paypal.android:card-payments:&lt;CURRENT-VERSION&gt;'3}## 3. Add a button to initiate vault
Add a button to your app's UI to save a card.

1Button(onClick={2// Create a setup token on server-side (see next step)3}){4Text("Save Card")5}## 4. Create setup token
From your server, create a setup token for cards that have:

- No verification
- 3D Secure verification

- No verification
- 3D Secure

### Request for new customer

Generate a setup token with an empty card as its payment_source . Later, you will attach card details to the
setup token in the SDK.

1curl-v -k -X POST'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens'\\2-H"Content-Type: application/json"\\3-H"Authorization: Bearer ACCESS-TOKEN"\\4-H"PayPal-Request-Id: REQUEST-ID"\\5-d'{6"payment_source": {7"card": {}8}9}'### Request for returning customer with saved payment
For a returning payer with previously stored payment sources, include the
PayPal-generated customerId in the request to save a
different payment method for the same customer.

1curl-v -k -X POST'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens'\\2-H"Content-Type: application/json"\\3-H"Authorization: Bearer ACCESS-TOKEN"\\4-H"PayPal-Request-Id: REQUEST-ID"\\5-d'{6"payment_source": {7"card": {}8}9"customer": {10"id": "llPdZofmwR"11}12}'#### Modify the code

- Change ACCESS-TOKEN to your sandbox app's access token.
- Change REQUEST-ID to a set of unique alphanumeric
  characters such as a timestamp.

### Response

The card payment source in the response is empty. You'll
attach additional information to the setup token in the steps that follow.

1{2"id":"86S246162E316080B",3"customer":{4"id":"ZUzLMNMrJD"5},6"status":"CREATED",7"payment_source":{8"card":{}9},10"links":[{11"href":"https://api-m.sandbox.paypal.com/v3/vault/setup-tokens/86S246162E316080B",12"rel":"self",13"method":"GET",14"encType":"application/json"15}]16}#### Note

- id is the setup token ID.
- For a first-time customer, this endpoint generates a new customer ID
  returned in customer.id .
- For a returning customer, the customer ID in the response should match
  the customer ID passed into the request.

## 5. Implement vaulting in Android SDK

In the Android SDK, create a CardVaultRequest and use it to
invoke the CardClient.vault() method.

The **vault** method:

- Attaches a card to a setup token.
- Launches 3D Secure when a payment requires additional authentication.

### 1. Collect card payment details

Build a Card object with the buyer's card details:

1valcard=Card(2number="4005519200000004",3expirationMonth="01",4expirationYear="2025",5securityCode="123",6cardholderName="Jane Smith",7billingAddress=Address(8streetAddress="123 Main St.",9extendedAddress="Apt. 1A",10locality="City",11region="IL",12postalCode="12345",13countryCode="US"14)15)Collecting a billing address can reduce the probability of an authentication
challenge.

### 2. Build CardVaultRequest

Build a CardVaultRequest with the card object and
your SETUP-TOKEN :

1val cardVaultRequest=CardVaultRequest(2setupTokenID="SETUP-TOKEN",3card=card4)### 3. Call the vault function
After your CardVaultRequest has the card details and setupTokenID , call cardClient.vault() to process the
payment.

1valconfig=CoreConfig(clientID="CLIENT_ID",environemnt=.live)2valcardClient=CardClient(config=config)3cardClient.cardVaultListener=object:CardVaultListener{4overridefunonVaultSuccess(result:CardVaultResult){5// Vaulting has been approved and is ready to be used to create a paymentToken or vaultID6// The CardVaultResult contains a setupTokenID string used to create the paymentToken from your server7// Make sure you pass the cardVaultResult.setupTokenID to your server8}9overridefunonVaultFailure(error:PayPalSDKError){10// Handle error11}12}13cardClient.vault(context,cardVaultRequest)## 6. Create a payment token with the vault setup token ID
Convert the setup token to a payment token that can be used to process a
transaction:

1curl-v -k -X POST'https://api-m.sandbox.paypal.com/v3/vault/payment-tokens'\\2-H"Content-Type: application/json"\\3-H"Authorization: Bearer ACCESS-TOKEN"\\4-H"PayPal-Request-Id: REQUEST-ID"\\5-d'{6"payment_source": {7"token": {8"id": "VAULT-SETUP-TOKEN",9"type": "SETUP_TOKEN"10}11}12}'### Modify the code

- Change ACCESS-TOKEN to your sandbox app's access token.
- Change REQUEST-ID to a set of unique alphanumeric characters
  such as a timestamp.
- Change VAULT-SETUP-TOKEN to the value passed from the client.
- Save the resulting payment token returned from the API to use
  in future transactions.

## 7. Show saved payment methods to returning payers

When a payer returns to your app, you can show the payer's saved payment
methods with the Payment Method Tokens API.

### List all saved payment methods

Make the server-side list all [payment tokens API call](https:/docs/api/payment-tokens/v3/#customer_payment-tokens_get) to retrieve payment methods saved to a payer's PayPal-generated customer ID.
Based on this list, you can show all saved payment methods to a payer to
select during checkout.

**Important:** Don't expose payment method token IDs on the
client side. To protect your payers, create separate IDs for each token and
use your server to correlate them.

#### Sample request: List all saved payment methods

1curl-L -X GET"https://api-m.sandbox.paypal.com/v3/vault/payment-tokens?customer_id=CUSTOMER-ID"\\2-H"Content-Type: application/json"\\3-H"Accept-Language: en_US"\\4-H"Authorization: Bearer ACCESS-TOKEN"\\5-H"PayPal-Request-Id: REQUEST-ID"#### Modify the code

- Change CUSTOMER-ID to a PayPal-generated customer ID.
- Change ACCESS-TOKEN to your sandbox app's access token.
- Change REQUEST-ID to a set of unique alphanumeric characters
  such as a time stamp.

### Show saved card to payer

Display the saved card to the payer and use the Orders API to make another
transaction. Use the vault ID the payer selects as an input to the [Orders API to capture the payment](/docs/checkout/save-payment-methods/purchase-later/cards/#link-usesavedpaymenttoken) .

We recommend showing the card brand and the last 4 digits.

![Visa,ending,in,1234](assets/paypal-save-card-visa-example.png)

## 8. Test your integration

Run the following tests in the PayPal sandbox to ensure that you can save
cards.

### Save payment

- In your app, initiate the vault.
- Create a setup token with an empty card.
- Call the vault function in the SDK with setup token and card details.
- Create a payment token with the updated setup token.
- Store the PayPal-generated customer ID in your system.
- Log in to [sandbox](https://www.sandbox.paypal.com/) with your
  merchant account and verify the transaction.
- Return to your app and initiate another transaction. Use the
  PayPal-generated payment token as a payment source.
- Verify that the transaction captures successfully without having to complete
  PayPal Web Checkout again.

## Next steps

- [Test and go live](/reference/production/) with this integration.
- Change the credentials and API URLs from api-m.sandbox.paypal.com to api-m.paypal.com when
  going live with your integration.
- You can [create orders](/docs/api/orders/v2/#orders_create) without the payment_source.paypal.attributes.vault for subsequent or
  recurring transactions.
- You can [get a payment token](/docs/api/payment-tokens/v3/#payment-tokens_get) , [list all payment tokens](/docs/api/payment-tokens/v3/#payment-tokens_payment-tokens) , [delete a payment token](/docs/api/payment-tokens/v3/#payment-tokens_delete) , and more with the Payment Method Tokens API.
