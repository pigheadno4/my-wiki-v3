---
title: Save cards with the iOS SDK
slug: /docs/checkout/save-payment-methods/during-purchase/ios-sdk/cards/
createTime: "2025-02-26T03:44:12.386Z"
updateTime: "2025-02-27T08:47:34.628Z"
---

# Save cards with the iOS SDK

Allow customers to save their credit or debit cards in order to eliminate the need to re-enter payment details on subsequent purchases - leading to a faster checkout experience.

## Use cases

Businesses save payment methods if they want customers to:

- Check out without re-entering a payment method
- Pay after use, for example, ride-sharing and food delivery

## Availability

- In the US only.
- For both desktop and mobile web.

## How it works

PayPal encrypts payment method information and stores it in a digital vault for that customer.

- The payer saves their payment method.
- For a first-time payer, PayPal creates a customer ID. Store this within your system for future use.
- The customer ID can be used to save another payment method for an existing customer or to display saved payment methods for a customer in your application.

The checkout process is now shorter because it uses saved payment information.

## Know before you code

- This integration requires a PayPal Developer account.
- You'll need to have an existing [advanced credit and debit card payments](https://developer.paypal.com/docs/checkout/advanced/) integration. PayPal must approve your account to process advanced credit and debit card payments.
- Complete the steps in [Get started](https://developer.paypal.com/api/rest/) to get the following sandbox account information from the Developer Dashboard: - The sandbox client ID and secret of [your REST app](https://www.paypal.com/signin?returnUri=https%3A%2F%2Fdeveloper.paypal.com%2Fdeveloper%2Fapplications) .
- An access token to use the PayPal REST API server.

- This client-side and server-side integration uses the following: - [PayPal iOS SDK](https://developer.paypal.com/docs/checkout/advanced/ios/)
- [Orders REST API](https://developer.paypal.com/docs/api/orders/v2/)

## 1. Set up sandbox to save payment methods

Set up your sandbox and live business accounts to save payment methods:

- Log in to the Developer Dashboard.
- Under **REST API apps** , select your app name.
- Under **Sandbox App Settings** &gt; **App Feature Options** , check **Accept payments** .
- Expand **Advanced options** . Confirm that **Vault** is selected.

##

Use a selection UI element to select the vault option.

#### **`2. Add toggle for payers to save card`**

```javascript

    VStack {
  Toggle("Save your card", isOn: $shouldSaveCard)
}

```

## 3. Send the user's preference to your endpoint

When the user selects the submit button, pass the user's vault preference to your endpoint that calls the Orders API. You will use the user's preference to populate the request to the Orders API in the next step.

### Server side

Set up your server to call the Orders API. If the user consents to save their payment method, include a payment_source object in the request to the Orders API. See the following code snippet.

**Note:** In the following request, the payment_source.attributes.vault.store_in_vault with the value ON_SUCCESS means the card is saved with a successful authorization or capture.

### First-time payer#### Save payment method for first-time payers

This request is for payers who:

- Don't have a payment source saved into the vault.

#### **`First-time payer`**

```curl

    curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer 'ACCESS-TOKEN'" \
 -d '{
      "intent": "CAPTURE",
      "purchase_units": [{
        "amount": {
          "currency_code": "USD",
          "value": "100.00"
        }
      }],
      "payment_source": {
        "card": {
          "attributes": {
            "vault": {
              "store_in_vault": "ON_SUCCESS"
            }
          }
        }
      }
    }

```

### Returning payer#### Save payment method for returning payers

This request is for payers who:

- Already have a payment method saved in the vault.
- Want to save another payment method to the vault.

Pass the PayPal-generated customer.id as part of this request. Link additional payment_sources to this customer through their customer.id . The customer.id is returned in the response from an authorize or capture request.

#### **`Returning payer`**

```curl

    curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer 'ACCESS-TOKEN'" \
 -d '{
      "intent": "CAPTURE",
      "purchase_units": [{
        "amount": {
          "currency_code": "USD",
          "value": "100.00"
        }
      }],
      "payment_source": {
        "card": {
          "attributes": {
            "vault": {
              "store_in_vault": "ON_SUCCESS"
            },
            "customer": {
              "id": "'PayPal-generated customer id'"
            }
          }
        }
      }
    }

```

Pass the order ID and card details to the iOS SDK. Calling CardClient.approveOrder() updates the order with the new card details. PayPal handles any PCI compliance issues. When approveOrder() succeeds, you can then authorize or capture the order using the orderID .

In the iOS SDK you will need to create a CardRequest to pass into the approve function.

A CardRequest object:

- Attaches a card to an ORDER_ID .
- Launches 3D Secure when a payment requires additional authentication.

### 1. Collect card payment details

Build a card object with the buyer's card details.

#### **`1. Collect card payment details`**

```javascript

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

### 2. Build CardRequest

Build a CardRequest with the card object and your ORDER_ID :

#### **`2. Build CardRequest`**

```javascript

let cardRequest = CardRequest(
  orderID: "ORDER_ID",
  card: card,
  sca: .scaAlways // default value is .scaWhenRequired
)

```

[3D Secure](https://developer.paypal.com/api/nvp-soap/payflow/3d-secure-overview/) is supported for all card payments to comply with the [Second Payment Services Directive (PSD2)](https://www.paypal.com/uk/webapps/mpp/PSD2?_ga=1.18434873.1625369690.1652045188) . PSD2 is a European Union regulation that introduces [Strong Customer Authentication (SCA)](https://www.ukfinance.org.uk/our-expertise/payments-and-innovation/strong-customer-authentication) and other security requirements.

Select your SCA launch option type using the sca parameter in the CardRequest initializer:

- SCA.scaWhenRequired launches an SCA challenge when applicable. This is enabled by default.
- SCA.scaAlways requires an SCA challenge for all card transactions.

### 3. Approve order

After your CardRequest has the card details, call cardClient.approveOrder() to process the payment. Set up your CardDelegate to handle successful payments, errors, cancellations, and 3D Secure transaction flows.

#### **` Approve order`**

```javascript

let coreConfig = CoreConfig(clientID: "CLIENT_ID", environment: .sandbox)
let cardClient = CardClient(config: coreConfig)
cardClient.delegate = self
cardClient.approveOrder(request: cardRequest)

```

### 4. Handle payment result scenarios

#### **`Handle payment result scenarios`**

```javascript

extension MyViewController: CardDelegate {
  // MARK: - CardDelegate
  func card(_ cardClient: CardClient, didFinishWithResult result: CardResult) {
    // Order was approved and is ready to be captured/authorized (refer to the next step)
  }
  func card(_ cardClient: CardClient, didFinishWithError error: CoreSDKError) {
    // Handle the error by accessing `error.localizedDescription`
  }
  func cardDidCancel(_ cardClient: CardClient) {
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

### Server side

Set up your server to call the [v2 Orders API](https://developer.paypal.com/api/orders/v2/) :

- Call the [authorize order endpoint](https://developer.paypal.com/docs/api/orders/v2/#orders_authorize) if the intent passed was AUTHORIZE .
- Call the [capture order endpoint](https://developer.paypal.com/docs/api/orders/v2/#orders_capture) if the intent passed was CAPTURE .

### Request

#### Authorize or capture order request

#### **`Authorize`**

```curl

curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T/authorize \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer 'ACCESS-TOKEN'" \
 -d '{}'

```

#### **`Capture`**

```curl

curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T/capture \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer 'ACCESS-TOKEN'" \
 -d '{}'

```

### Response

#### **`Response`**

```javascript

  {
    "id": "5O190127TN364715T",
    "status": "COMPLETED",
    "payment_source": {
      "card": {
        "brand": "VISA",
        "last_digits": "4949"
        "attributes": {
          "vault": {
            "id": "nkq2y9g",
            "customer": {
                "id": "695922590"
            },
            "status": "VAULTED",
            "links": [{
                "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/nkq2y9g",
                "rel": "self",
                "method": "GET"
              },
              {
                "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/nkq2y9g",
                "rel": "delete",
                "method": "DELETE"
              },
              {
                "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",
                "rel": "up",
                "method": "GET"
              }
            ]
          }
        }
      }
    },
    "purchase_units": [{
      "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
      "payments": {
        "captures": [{
          "id": "3C679366HH908993F",
          "status": "COMPLETED",
          "amount": {
            "currency_code": "USD",
            "value": "100.00"
          },
          "seller_protection": {
            "status": "NOT_ELIGIBLE"
          },
          "final_capture": true,
          "seller_receivable_breakdown": {
            "gross_amount": {
              "currency_code": "USD",
              "value": "100.00"
            },
            "paypal_fee": {
              "currency_code": "USD",
              "value": "3.00"
            },
            "net_amount": {
              "currency_code": "USD",
              "value": "97.00"
            }
          },
          "create_time": "2022-01-01T21:20:49Z",
          "update_time": "2022-01-01T21:20:49Z",
          "processor_response": {
              "avs_code": "Y",
              "cvv_code": "M",
              "response_code": "0000"
          },
          "links": [{
              "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/3C679366HH908993F",
              "rel": "self",
              "method": "GET"
            },
            {
              "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/3C679366HH908993F/refund",
              "rel": "refund",
              "method": "POST"
            }
          ]
        }]
      }
    }],
    "links": [{
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",
      "rel": "self",
      "method": "GET"
    }]
}

```

In the response from the Authorize or Capture request, the Orders v2 API interacts with the Payment Method Tokens v3 API to save the card.

The payment_source.card.attributes.vault stores the card information as the vault.id , which can be used for future payments when the vault.status is VAULTED .

#### Save approved payment source

If the payment has been authorized or captured, the payer does not need to be present to save a payment_source . To keep checkout times as short as possible, the Orders API responds as soon as payment is captured.

If the attributes.vault.status returned after payment is APPROVED , you won't have a vault.id yet. An example of the attributes object from this scenario is in the following sample:

#### **`Save approved payment source`**

```javascript

  "attributes": {
    "vault": {
      "status": "APPROVED",
      "links": [
        {
          "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",
          "rel": "up",
          "method": "GET"
        }
      ]
    }
  }

```

In order to retrieve a vault_id when an APPROVED status is returned, you'll need to subscribe to the VAULT.PAYMENT-TOKEN.CREATED [webhook](https://developer.paypal.com/api/rest/webhooks/) event.

The Payment Method Tokens API sends a webhook event after the payment source is saved. An example of the VAULT.PAYMENT-TOKEN.CREATED webhook payload is shown in the following sample:

#### **`The Payment Method Tokens API `**

```javascript

  {
     "id":"WH-1KN88282901968003-82E75604WM969463F",
     "event_version":"1.0",
     "create_time":"2022-08-15T14:13:48.978Z",
     "resource_type":"payment_token",
     "resource_version":"3.0",
     "event_type":"VAULT.PAYMENT-TOKEN.CREATED",
     "summary":"A payment token has been created.",
     "resource":{
        "time_created":"2022-08-15T07:13:48.964PDT",
        "links":[
           {
              "href":"https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/9n6724m",
              "rel":"self",
              "method":"GET",
              "encType":"application/json"
           },
           {
              "href":"https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/9n6724m",
              "rel":"delete",
              "method":"DELETE",
              "encType":"application/json"
           }
        ],
        "id":"nkq2y9g",
        "payment_source":{
           "card":{
              "last_digits":"1111",
              "brand":"VISA",
              "expiry":"2027-02",
              "billing_address":{
                 "address_line_1":"123 Main St.",
                 "address_line_2":"Unit B",
                 "admin_area_2":"Anytown",
                 "admin_area_1":"CA",
                 "postal_code":"12345",
                 "country_code":"US"
              }
           }
        },
        "customer":{
           "id":"695922590"
        }
     },
     "links":[
        {
           "href":"https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-1KN88282901968003-82E75604WM969463F",
           "rel":"self",
           "method":"GET"
        },
        {
           "href":"https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-1KN88282901968003-82E75604WM969463F/resend",
           "rel":"resend",
           "method":"POST"
        }
     ]
  }

```

In this example, the resource.id field is the vault ID, and resource.customer.id is the PayPal-generated customer ID.

You can now style your card fields and test a purchase.

#### Payment processor codes

Payment processors return the following codes when they receive a transaction request. For advanced card payments, the code displays in the authorization object under the response_code field.

The following sample shows the processor response codes returned in an authorization ( avs_code ) and capture call ( cvv_code ) response:

#### **`Payment processor codes`**

```javascript

  "processor_response": {
    "avs_code": "Y",
    "cvv_code": "S",
    "response_code": "0000"
  }

```

See the Orders API response_code object to get the [processor response code for the non-PayPal payment processor errors](https://developer.paypal.com/docs/api/orders/v2/#definition-processor_response) .

## 7. Pay with saved payment methods

When a payer returns to your site, you can show the payer's saved payment methods with the Payment Method Tokens API.

### List all saved payment methods

Make the server-side [list all payment tokens API call](https://developer.paypal.com/docs/api/payment-tokens/v3/#customer_payment-tokens_get) to retrieve payment methods saved to a payer's PayPal-generated customer ID. Based on this list, you can show all saved payment methods to a payer to select during checkout.

### Show saved card to payer

Display the saved card to the payer and use the Orders API to make another transaction. Use the vault ID the payer selects as an input to the Orders API.

##

## 8. Test your integration

Test your vault integration in the PayPal sandbox.

- Copy the sample request code.
- Change 'ACCESS_TOKEN' to your [access token](https://developer.paypal.com/api/rest/authentication/) .

### Save payment method

- On the checkout page, enter the card information and select the option to save the card. You can use test card numbers from [this page](https://developer.paypal.com/tools/sandbox/card-testing/) for testing.
- Capture the transaction.
- Log in to [sandbox](https://www.sandbox.paypal.com/) with your merchant account and verify the transaction.

### Pay with a saved payment method

- Use the [list all payment tokens](https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_payment-tokens) API to retrieve all the payment methods saved for the payer.
- Capture the payment by passing the payer-selected vault ID to the Orders API.
- Log in to the [sandbox](https://www.sandbox.paypal.com/) with your merchant account and verify the transaction.

##

## Next steps

- [Test and go live](https:/api/rest/production/) with this integration. - Complete [production onboarding](https://www.paypal.com/bizsignup/entry/product/ppcp) to be eligible to process cards with your live PayPal account.
- Be sure to swap the credentials and API URL from sandbox to production when going live with your integration.

- Follow [Use payment method token with checkout](https:/docs/checkout/save-payment-methods/purchase-later/cards/#link-usesavedpaymenttoken) for subsequent or recurring transactions.
- You can [get a payment token](https:/docs/api/payment-tokens/v3/#payment-tokens_get) , [list all payment tokens](https:/docs/api/payment-tokens/v3/#payment-tokens_payment-tokens) , [delete a payment token](https:/docs/api/payment-tokens/v3/#payment-tokens_delete) , and more with the Payment Method Tokens API.
- Keep saved cards up-to-date with the [real-time account updater](https:/docs/checkout/advanced/customize/rtau/) .
