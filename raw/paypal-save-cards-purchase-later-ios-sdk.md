<!-- Source URL: https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/ios-sdk/cards/ -->
<!-- Fetched: 2026-04-14 -->

---
title: Save cards for purchase later with the iOS SDK
slug: /docs/checkout/save-payment-methods/purchase-later/ios-sdk/cards/
Last updated: February 6th 2025, @ 1:45:14 am
---

# Save cards for purchase later with the iOS SDK

Save customer credit or debit cards to charge them at a later time. For example, you can offer a free trial and charge payers after the trial expires. Payers don't need to be present when charged and no checkout is required.

Use the iOS SDK to save a payer's credit or debit cards.

## Availability

See supported countries

## Know before you code

To save payment methods, you must be able to identify payers uniquely. For example, payers create an account and log in to your app.

Complete the steps in Get started to get the following sandbox account information from the Developer Dashboard:

- Your sandbox account login information
- Your access token

The iOS SDK saves the following card types for purchase later:

- American Express
- Discover
- Mastercard
- Visa

You'll need an existing advanced credit and debit integration. PayPal must approve your business account for advanced credit and debit card payments.

## How it works

PayPal encrypts payment method information and stores it in a digital vault for that customer.

- The payer saves their payment method.
- For a first-time payer, PayPal creates a customer ID. Store this within your system for future use.
- Use the customer ID to retrieve saved payment methods and add new ones for existing customers in your application.

The checkout process is now shorter because it uses saved payment information.

## 1. Set up account to save payments

Set up your sandbox and live business accounts to save payment methods:

- Log in to the Developer Dashboard.
- Under **REST API apps**, select your app name.
- Under **Sandbox App Settings** > **App Feature Options**, check **Accept payments**.
- Expand **Advanced options**. Confirm that **Vault** is selected.

## 2. Add the CardPayments module to your app

Add the CardPayments package dependency for your app using Swift Package Manager or CocoaPods:

Swift Package Manager | CocoaPods

1. Open Xcode.
2. Follow the guide to add package dependencies to your app.
3. Enter https://github.com/paypal/paypal-ios/ as the repository URL.
4. Select the checkbox for the CardPayments framework.

## 3. Add a button to initiate vault

Add a button to your app's UI to save a card.

```swift
Button("Save Card") {
   // Create a setup token on server-side (see next step)
}
```

## 4. Create setup token

On your server, you need to create a setup token.

From your server, create a setup token for cards that have:

- No verification
- 3D Secure verification

### Request for new customer

Generate a setup token with an empty card as its payment_source. Later, you will attach card details to the setup token in the SDK.

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

### Request for returning customer with saved payment

For a returning payer with previously stored payment sources, include the PayPal-generated customerId in the request to save a different payment method for the same customer.

```curl
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens' \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS-TOKEN" \
 -H "PayPal-Request-Id: REQUEST-ID" \
 -d '{
      "payment_source": {
        "card": {}
      }
      "customer": {
         "id": "llPdZofmwR"
      }
    }'
```

#### Modify the code

- Change ACCESS-TOKEN to your sandbox app's access token.
- Change REQUEST-ID to a set of unique alphanumeric characters such as a timestamp.

### Response

The card payment source in the response is empty. You'll attach additional information to the setup token in the steps that follow.

```javascript
{
  "id": "86S246162E316080B", 
  "customer": {
    "id": "ZUzLMNMrJD" 
    },
  "status": "CREATED",
  "payment_source": {
      "card": {}
    },
  "links": [{
    "href": "https://api-m.sandbox.paypal.com/v3/vault/setup-tokens/86S246162E316080B",
    "rel": "self",
    "method": "GET",
    "encType": "application/json"
    }]
   }
```

#### Note

- id is the setup token ID.
- For a first-time customer, this endpoint generates a new customer ID returned in customer.id.
- For a returning customer, the customer ID in the response should match the customer ID passed into the request.

## 5. Implement vaulting in iOS SDK

In the iOS SDK, you need to create a CardVaultRequest to pass into the vault function.

The **vault** method:

- Attaches a card to a setup token.
- Launches 3D Secure when a payment requires additional authentication.

### 1. Collect card payment details

Build a Card object with the buyer's card details:

```swift
let card = Card(
  number: "4005519200000004",
  expirationMonth: "01",
  expirationYear: "2025",
  securityCode: "123",
  cardholderName: "Jane Smith",
  billingAddress: Address(
    addressLine1: "123 Main St.",
    addressLine2: "Apt. 1A",
    locality: "City",
    region: "IL",
    postalCode: "12345",
    countryCode: "US"
  )
)
```

Collecting a billing address can reduce the probability of an authentication challenge.

### 2. Build CardVaultRequest

Build a CardVaultRequest with the card object and your SETUP-TOKEN:

```swift
let cardVaultRequest = CardVaultRequest(
  setupTokenID: "SETUPTOKEN",
  card: card
)
```

### 3. Call the vault function

After your CardVaultRequest has the card details and setupTokenID, call cardClient.vault() to process the payment.

```swift
let config = CoreConfig(clientID: "CLIENT_ID", environemnt: .live)
let cardClient = CardClient(config: config)
cardClient.vaultDelegate = self
cardClient.vault(cardVaultRequest)
```

### 4. Handle vault result scenarios

```swift
extension MyViewController: CardVaultDelegate {
  // MARK: - CardVaultDelegate
  func card(_ cardClient: CardClient, didFinishWithVaultResult vaultResult: CardVaultResult) {
    // Vaulting has been approved and is ready to be used to create a paymentToken or vaultID
    // The CardVaultResult contains a setupTokenID string used to create the paymentToken from your server
    // Make sure you pass the cardVaultResult.setupTokenID to your server
  }
  func card(_ cardClient: CardClient, didFinishWithVaultError error: CoreSDKError) {
    // Handle the error by accessing `error.localizedDescription`
  }
  func cardVaultDidCancel(_ cardClient: CardClient) {
    // 3D Secure auth was canceled by the user
  }
  func cardThreeDSecureWillLaunch(_ cardClient: CardClient) {
    // 3D Secure auth will launch
  }
  func cardThreeDSecureDidFinish(_ cardClient: CardClient) {
    // 3D Secure auth finished
  }
}
```

## 6. Create a payment token with the vault setup token ID

Convert the setup token to a payment token that can be used to process a transaction:

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

## 7. Show saved payment methods to returning payers

When a payer returns to your app, you can show the payer's saved payment methods with the Payment Method Tokens API.

### List all saved payment methods

Make the server-side list all payment tokens API call to retrieve payment methods saved to a payer's PayPal-generated customer ID. Based on this list, you can show all saved payment methods to a payer to select during checkout.

**Important:** Don't expose payment method token IDs on the client side. To protect your payers, create separate IDs for each token and use your server to correlate them.

#### Sample request: List all saved payment methods

```curl
curl -L -X GET "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens?customer_id=CUSTOMER-ID" \
 -H "Content-Type: application/json" \
 -H "Accept-Language: en_US" \
 -H "Authorization: Bearer ACCESS-TOKEN" \
 -H "PayPal-Request-Id: REQUEST-ID"
```

#### Modify the code

- Change CUSTOMER-ID to a PayPal-generated customer ID.
- Change ACCESS-TOKEN to your sandbox app's access token.
- Change REQUEST-ID to a set of unique alphanumeric characters such as a time stamp.

### Show saved card to payer

Display the saved card to the payer and use the Orders API to make another transaction. Use the vault ID the payer selects as an input to the Orders API to capture the payment.

We recommend showing the card brand and the last 4 digits.

Visa ending in 1234

## 8. Test your integration

Run the following tests in the PayPal sandbox to ensure that you can save cards.

### Save payment

- In your app, initiate the vault.
- Create a setup token with an empty card.
- Call the vault function in the SDK with setup token and card details.
- Create a payment token with the updated setup token.
- Store the PayPal-generated customer ID in your system.
- Log in to sandbox with your merchant account and verify the transaction.
- Return to your app and initiate another transaction. Use the PayPal-generated payment token as a payment source.
- Verify that the transaction captures successfully without having to complete PayPal Web Checkout again.

## Next steps

- Test and go live with this integration.
- Change the credentials and API URLs from api-m.sandbox.paypal.com to api-m.paypal.com when going live with your integration.
- You can create orders without the payment_source.paypal.attributes.vault for subsequent or recurring transactions.
- You can get a payment token, list all payment tokens, delete a payment token, and more with the Payment Method Tokens API.
