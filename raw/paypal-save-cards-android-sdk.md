---
title: Save cards with the Android SDK
slug: /docs/checkout/save-payment-methods/during-purchase/android-sdk/cards/
createTime: "2025-02-26T05:35:48.260Z"
updateTime: "2025-02-27T08:47:25.994Z"
---

# Save cards with the Android SDK

Allow customers to save their credit or debit cards in order to eliminate the need to re-enter payment details on subsequent purchases - leading to a faster checkout experience.

## Use cases

Businesses save payment methods if they want customers to:

- Check out without re-entering a payment method
- Pay after use, for example, ride-sharing and food delivery

## Availability

### See supported countries\*\*\*\*

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

- This client-side and server-side integration uses the following: - [PayPal Android SDK](https://developer.paypal.com/docs/checkout/advanced/android/)
- [Orders REST API](https://developer.paypal.com/docs/api/orders/v2/)

## 1. Set up sandbox to save payment methods

Set up your sandbox and live business accounts to save payment methods:

- Log in to the Developer Dashboard.
- Under **REST API apps** , select your app name.
- Under **Sandbox App Settings** &gt; **App Feature Options** , check **Accept payments** .
- Expand **Advanced options** . Confirm that **Vault** is selected.

Add a checkbox element grouped with your card collection fields to give payers the option to save their card.

#### **`checkbox`**

```javascript

@Composable
fun CheckoutScreen() {
  var shouldSaveCard by remember { mutableStateOf(false) }
  Column {
    ...
    Row {
      Checkbox(
        checked = shouldSaveCard,
        onCheckedChange = { value -> shouldSaveCard = value }
      )
      Text("Save your card")
    }
  }
}

```

## 3. Create order and save card

Set up your server to call the Orders API. Use the Orders API request to add attributes needed to save a card.

### First-time payer

### Save payment method for first-time payers

This request is for payers who:

- Don't have a payment source saved into the vault.

To run 3D Secure on the card, set the payment_source.card.attributes.verification.method to SCA_ALWAYS or SCA_WHEN_REQUIRED .

SCA_ALWAYS triggers an authentication for every transaction, while SCA_WHEN_REQUIRED triggers an authentication only when a regional compliance mandate such as PSD2 is required. 3D Secure is supported only in countries with a [PSD2 compliance mandate](https://www.paypal.com/uk/webapps/mpp/PSD2?_ga=1.51925228.43968804.1640649786PSD2) .

**Note:** In the following request, the payment_source.attributes.vault.store_in_vault with the value ON_SUCCESS means the card is saved with a successful authorization or capture.

curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer 'ACCESS-TOKEN'" \
 -d '{
"intent": "CAPTURE",
"purchase_units": [{
"reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
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
,### Returning payer

### Save payment method for returning payers

This request is for payers who:

- Already have a payment method saved in the vault.
- Want to save another payment method to the vault.

Pass the PayPal-generated customer.id as part of this request. Link additional payment_sources to this customer through their customer.id . The customer.id is returned in the response from an authorize or capture request.

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
"customer" : {
"id": "'PayPal-generated customer id'"
}
}
}
}
}

### Response

Pass the order id and card details to the Android SDK. Calling CardClient.approveOrder() updates the order with the new card details. PayPal handles any PCI compliance issues.

When approveOrder() succeeds, you can then authorize or capture the order using the orderID .

**Note:** The request to save a payment method is made when an order is created with the payment_source.attributes.vault.store_in_vault property set to true . Vault details are available only after an order is authorized or captured.

#### **`Response`**

```javascript

  {
    "id": "5O190127TN364715T",
    "status": "CREATED",
    "intent": "CAPTURE",
    "payment_source": {
      "card": {
        "brand": "VISA",
        "last-digits": "1881",
        "billing_address": {
          "address_line_1": "123 Main St.",
          "address_line_2": "Unit B",
          "admin_area_2": "Anytown",
          "admin_area_1": "CA",
          "postal_code": "12345",
          "country_code": "US"
        }
      }
    },
    "purchase_units": [{
      "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
      "amount": {
        "currency_code": "USD",
        "value": "100.00"
      }
    }],
    "create_time": "2021-10-28T21:18:49Z",
    "links": [{
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",
        "rel": "self",
        "method": "GET"
      },
      {
        "href": "https://www.sandbox.paypal.com/checkoutnow?token=5O190127TN364715T",
        "rel": "approve",
        "method": "GET"
      },
      {
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",
        "rel": "update",
        "method": "PATCH"
      },
      {
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T/capture",
        "rel": "capture",
        "method": "POST"
      }
    ]
  }

```

Use the orderId along with the customer's Card information to approve the order using the PayPal SDK:

#### **`Approve order using SDK`**

```javascript

@Composable
fun CheckoutScreen(card: Card) {
  Column {
    ...
    Button(
      onClick = { approveCardOrder(card) }
    ) {
      Text("Complete Purchase")
    }
  }
}

fun approveCardOrder(card: Card) {

  // Set up CardClient
  val coreConfig = CoreConfig("CLIENT_ID")
  val cardClient = CardClient(activity, coreConfig)

  // setup CardListener
  cardClient.approveOrderListener = object : ApproveOrderListener {
    override fun onApproveOrderSuccess(result: CardResult) {
      // Capture or authorize order (see next step)
    }
    override fun onApproveOrderFailure(error: PayPalSDKError) {
      // Handle error
    }
    override fun onApproveOrderCanceled() {
      // 3DS canceled by the user
    }
    override fun onApproveOrderThreeDSecureWillLaunch() {
      // 3DS will launch
    }
    override fun onApproveOrderThreeDSecureDidFinish() {
      // 3DS finished
    }
  }

  val returnUrl = "com.myapp.package://example.com/return_url""
  val request = CardRequest("ORDER_ID", card, returnUrl)
  cardClient.approveOrder(activity, request)
}

```

### Server side

Set up your server to call the [v2 Orders API](https://developer.paypal.com/api/orders/v2/) :

- Call the [authorize order endpoint](https://developer.paypal.com/docs/api/orders/v2/#orders_authorize) if the intent passed was AUTHORIZE .
- Call the [capture order endpoint](https://developer.paypal.com/docs/api/orders/v2/#orders_capture) if the intent passed was CAPTURE .

### Request

#### Authorize or capture order request

#### **`Authorize`**

```javascript

curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T/authorize \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer 'ACCESS-TOKEN'" \
 -d '{}'

```

#### **`Capture`**

```javascript

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

#### **`attributes`**

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

The Payment Method Tokens API still saves the payment source even after the Orders API returns its response and sends a webhook after the payment source is saved.

In order to retrieve a vault_id when an APPROVED status is returned, you'll need to subscribe to the VAULT.PAYMENT-TOKEN.CREATED [webhook](https://developer.paypal.com/api/rest/webhooks/) .

The Payment Method Tokens API sends a webhook after the payment source is saved. An example of the VAULT.PAYMENT-TOKEN.CREATED webhook payload is shown in the following sample:

#### **`VAULT.PAYMENT-TOKEN.CREATED`**

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

## 6. Pay with saved payment methods

When a payer returns to your site, you can show the payer's saved payment methods with the Payment Method Tokens API.

### List all saved payment methods

Make the server-side [list all payment tokens API call](https://developer.paypal.com/docs/api/payment-tokens/v3/#customer_payment-tokens_get) to retrieve payment methods saved to a payer's PayPal-generated customer ID. Based on this list, you can show all saved payment methods to a payer to select during checkout.

### Show saved card to payer

Display the saved card to the payer and use the Orders API to make another transaction. Use the vault ID the payer selects as an input to the Orders API.

## 7. Test your integration

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

## Next steps

- [Test and go live](https://developer.paypal.com/api/rest/production/) with this integration. - Complete [production onboarding](https://www.paypal.com/bizsignup/entry/product/ppcp) to be eligible to process cards with your live PayPal account.
- Be sure to swap the credentials and API URL from sandbox to production when going live with your integration.

- Follow [Use payment method token with checkout](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/cards/#link-usesavedpaymenttoken) for subsequent or recurring transactions.
- You can [get a payment token](https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_get) , [list all payment tokens](https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_payment-tokens) , [delete a payment token](https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_delete) , and more with the Payment Method Tokens API.
- Keep saved cards up-to-date with the [real-time account updater](https://developer.paypal.com/docs/checkout/advanced/customize/rtau/) .
