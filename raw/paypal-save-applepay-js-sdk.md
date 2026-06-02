<!-- Source URL: https://developer.paypal.com/docs/checkout/save-payment-methods/during-purchase/js-sdk/applepay/ -->
<!-- Fetched: 2026-04-14 -->

---
title: Save Apple Pay with the JavaScript SDK
slug: /docs/checkout/save-payment-methods/during-purchase/js-sdk/applepay/
createTime: '2024-10-22T08:06:26.131Z'
updateTime: '2025-11-27T22:21:00.220Z'
---


# Save Apple Pay with the JavaScript SDK

Save Apple Pay payment methods so merchants can make recurring payments without the payer being present.


**info**
**Note:** Apple Pay can't be used as a payment method for returning buyers, according to Apple guidelines.



## How it works 
When a payer on your website agrees to save the Apple Pay payment method, PayPal creates a customer record after the first successful transaction, encrypts the payment method information, and stores it in the vault. The saved payment information can only be accessed by the merchant. The merchant can use this saved payment method to make recurring payments on behalf of the payer.

- The payer chooses to save their payment method.
- For a first-time payer, PayPal generates a customer ID. Store this in your system for future use.



## Know before you code 
- To accept one-time or recurring payments using Apple Pay, you need a business account that is approved by PayPal.
- You'll need an existing [Apple Pay](https:/docs/checkout/apm/apple-pay/) integration.
- Complete the steps in [Get started](https:/api/rest/) to get the following sandbox account information from the Developer Dashboard: - Sandbox client ID and secret of [a REST app](https://www.paypal.com/signin?returnUri=https%3A%2F%2Fdeveloper.paypal.com%2Fdeveloper%2Fapplications&intent=developer) .
- Access token to use the PayPal REST API server.

 
- This integration uses the following: - [PayPal JavaScript SDK](https:/sdk/js/)
- [Orders REST API](https:/docs/api/orders/v2/)

 



## Enable Apple Pay 
Before your app can save Apple Pay as a payment method, verify that your sandbox business account supports Apple Pay. See the [Apple Pay integration guide](https:/docs/checkout/apm/apple-pay/#link-setupyoursandboxaccounttoacceptapplepay) for more information.


**info**
**Note:** When your integration is ready to go live, read the **Go live** section below for details about the additional steps needed for Apple Pay onboarding.


This screenshot shows the Apple Pay sandbox settings in the mobile and digital payments section of the PayPal Developer Dashboard. This only applies to direct merchant integrations:


![A,screenshot,showing,the,Apple,Pay,sandbox,settings,in,the,mobile,and,digital,payments,section,of,the,PayPal,Developer,Dashboard](assets/paypal-applepay-sandbox-settings.png)



## Create an Apple Pay Payment Session 
An Apple Pay Payment Session is a payment sheet that PayPal shows to the payer to start a payment.

Request an Apple Pay Payment Session by passing the following request object:



#### **`Apple Pay Payment Session`**
```javascript

// Note: the `applepayConfig` object in this request is the response from `paypal.Applepay().config()`.
const paymentRequest = {
  countryCode: applepayConfig.countryCode,
  merchantCapabilities: applepayConfig.merchantCapabilities,
  supportedNetworks: applepayConfig.supportedNetworks,
  currencyCode: "USD",
  requiredShippingContactFields: ["name", "phone", "email", "postalAddress"],
  requiredBillingContactFields: ["postalAddress"],
  lineItems: [
    {
        label: "Recurring",
        amount: "100.00",
        paymentTiming: "recurring",
        recurringPaymentStartDate: "2023-06-08T18:09:07.501Z"
    }
  ],
  total: {
      label: "Demo",
      type: "final",
      amount: "100.00"
  }
};
const session = new ApplePaySession(4, paymentRequest);

```


## Create order and Save Apple Pay 
### Server-side
Set up your server to call the [Create Order v2 API endpoint](https:/docs/api/orders/v2/#orders_create) . The Apple Pay button pressed on the client side determines the payment_source sent in the following sample.

This SDK uses the [Orders v2 REST API](https:/docs/api/orders/v2/) to save the Apple Pay payment method in the background. Add the attributes needed to save an Apple Pay payment method by using the request from **Save Apple Pay for the first time** below.

 

#### Platform considerations
When your platform saves a payment method, it can be owned by either:

- Your platform.
- A merchant on your platform.

If you are a platform, pass the the build notation (BN) code of the partner in the [PayPal-Partner-Attribution-Id](https:/api/rest/requests/#link-httprequestheaders) header for server-side calls to the Orders API. PayPal uses this information for reporting and tracking purposes.

For a merchant on your platform, pass the [PayPal-Auth-Assertion](https:/api/rest/requests/) header as part of calls to the Orders API. This ensures that the owner of the saved payment method is the merchant, not your platform.

 

### Save Apple Pay for the first time
Save the Apple Pay payment method the first time a payer opts in. This request is for payers who meet both of these conditions:

- Payer hasn't previously stored Apple Pay as a payment method for recurring purchases.
- Payer consents to store the Apple Pay payment method for future use.

#### Request


#### **`Apple Pay request Code`**
```javascript

curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders  -H "Content-Type: application/json"  -H "Authorization: Bearer ACCESS-TOKEN"  -H "PayPal-Partner-Attribution-Id: BN-CODE"  -d '{
      "intent": "CAPTURE",
      "purchase_units": [{
        "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
        "amount": {
         "currency_code": "USD",
          "value": "100.00"
        }
      }],
      "payment_source": {
        "apple_pay": {
          "stored_credential": {
            "payment_initiator": "CUSTOMER",
            "payment_type": "RECURRING"
          },
          "attributes": {
            "vault": {
              "store_in_vault": "ON_SUCCESS"
            }
          }
        }
      }
    }

```

**info**
**Note:** When payment_source.apple_pay.attributes.vault.store_in_vault is set to ON_SUCCESS , that means the Apple Pay payment method is saved when the authorization or capture succeeds.


### Response
Pass the order.id to the JavaScript SDK. The SDK updates the order with the Apple Pay payment method that the payer selects. PayPal handles any PCI Compliance checks.

The request needs to pass payment_source.attributes.vault.store_in_vault to save the Apple Pay payment method. Details about a saved payment method are available only after an order is authorized or captured.


#### **`Response Code`**
```javascript

{
    "id": "5O190127TN364715T",
    "status": "CREATED",
    "intent": "CAPTURE",
    "payment_source": {
      "apple_pay": {
        "name": "Firstname Lastname",
       "email_address": "payer@example.com",
        "phone_number": {
           "national_number": "15555555555"
        },
        "card": {
            "name": "Firstname Lastname",
            "last_digits": "4949",
            "brand": "VISA",
            "type": "CREDIT",
            "billing_address": {
                "address_line_1": "123 Main St.",
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

### Save Apple Pay for returning payer
This request is for payers who:

- Have an Apple Pay payment method already saved to the vault.
- Want to save another Apple Pay payment method to the vault.

Pass the previously-stored PayPal-generated customer.id as part of this request. Link additional payment_sources to this customer using their customer.id .

 

#### Request

#### **`request`**
```javascript

curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders  -H "Content-Type: application/json"  -H "Authorization: Bearer ACCESS-TOKEN"  -d '{
      "intent": "CAPTURE",
      "purchase_units": [{
        "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
        "amount": {
          "currency_code": "USD",
          "value": "100.00"
        }
      }],
      "payment_source": {
        "apple_pay": {
          "stored_credential": {
            "payment_initiator": "CUSTOMER",
            "payment_type": "RECURRING"
          },
          "attributes": {
            "customer": {
                "id": "PayPal-generated customer id"
            },
            "vault": {
              "store_in_vault": "ON_SUCCESS"
            },
          }
        }
      }
    }

```

#### Response
Pass the order.id to the JavaScript SDK. The SDK updates the order with the Apple Pay payment method that the payer selects. PayPal handles any PCI Compliance checks.

The request needs to pass payment_source.attributes.vault.store_in_vault to save the Apple Pay payment method. Details about a saved payment method are available only after an order is authorized or captured.


#### **`response`**
```javascript

{
    "id": "5O190127TN364715T",
    "status": "CREATED",
    "intent": "CAPTURE",
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

Set up your server to call the Authorize or Capture Order APIs:

After the payer approves, the onApprove function is called in the JavaScript SDK. Depending on the intent passed as part of your Create Order call, the server calls the following APIs:

- [Capture Order v2](https:/docs/api/orders/v2/#orders_capture) API endpoint if the intent passed was CAPTURE .
- [Authorize Order v2](https:/docs/api/orders/v2/#orders_authorize) API endpoint if the intent passed was AUTHORIZE .
- Platform integrations need to pass the PayPal-Partner-Attribution-Id header for reporting and tracking purposes.

 

### Request
#### Authorize order request

#### **`Authorize Code`**
```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T/authorize  -H "Content-Type: application/json"  -H "Authorization: Bearer ACCESS-TOKEN"  -H "PayPal-Partner-Attribution-Id: BN-CODE"  -d '{}'

```

#### Capture order request

#### **`Capture order request`**
```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T/capture \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS-TOKEN" \
 -d '{}'

```

#### Response

#### **`Response`**
```javascript

{
    "id": "5O190127TN364715T",
    "intent": "CAPTURE",
    "status": "COMPLETED",
    "payment_source": {
      "apple_pay": {
        "name": "Firstname Lastname",
        "email_address": "payer@example.com",
        "phone_number": {
          "national_number": "15555555555"
        },
        "card": {
            "name": "Firstname Lastname",
            "last_digits": "4949",
            "brand": "VISA",
            "type": "CREDIT",
            "billing_address": {
                "address_line_1": "123 Main St.",
                "admin_area_2": "Anytown",
                "admin_area_1": "CA",
                "postal_code": "12345",
                "country_code": "US"
            },
        },
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
The response to the authorize or capture request shows that the Orders v2 API calls the [Payment Method Tokens v3 API](https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/nkq2y9g) to save the payment method.

This response passes the relevant information with the vault.id when the vault.status is VAULTED . Use this vault.id for future payments.


### Check Orders API response
When a payer chooses to save Apple Pay for recurring purchases and the payment has been authorized or captured, the payer doesn't need to be present to save a payment_source . To keep checkout times as short as possible, the Orders API responds as soon as payment is captured.

If the attributes.vault.status returned after payment is "APPROVED" , you won't have a vault.id yet. "APPROVED" means the payment is approved to be saved.

Payment methods are saved with a vault.id if the response returned is "VAULTED" . An example of an "APPROVED" status is in the following sample:


#### **`Check Orders API response`**
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

In order to retrieve a vault_id when an APPROVED status is returned, you'll need to subscribe to the VAULT.PAYMENT-TOKEN.CREATED  [webhook](https:/api/rest/webhooks/event-names/#vault) .


The Payment Method Tokens API sends a webhook after the payment source is saved. An example of the VAULT.PAYMENT-TOKEN.CREATED webhook payload is shown in the following sample:


#### **`Check Orders API response part 2 code`**
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
In the previous example, the resource.id field is the vault ID. The resource.customer.id is the PayPal-generated customer ID.

### See also
- Make Orders API calls from your server with the [Orders v2 API](/docs/api/orders/v2/) .
- Refer to the [Capture Payment for Order endpoint](https:/docs/api/orders/v2/#orders_capture) of the Orders v2 API to learn more about the values you can pass as you build your code.


To delete a saved payment method token, call the [Delete Payment Token endpoint](https:/docs/api/payment-tokens/v3/#payment-tokens_delete) of the Payment Method Tokens v3 API:


#### **`Delete saved payment method token`**
```curl

curl -v -X DELETE https://api-m.sandbox.paypal.com//v3/vault/payment-tokens/ nkq2y9g  -H "Content-Type: application/json"  -H "Authorization: Bearer ACCESS-TOKEN"  -d '{}'

```


## Pay with a saved payment method 
Set up your checkout page to show a returning customer their saved Apple Pay payment method. Make a call to the [Capture Payment for Order endpoint](https:/docs/api/orders/v2/#orders_capture) of the Orders v2 API and pass the apple_pay.vault_id .

To use a saved payment method:

- Use the [List All Payment Tokens endpoint](https:/docs/api/payment-tokens/v3/#payment-tokens_payment-tokens) of the Payment Method Tokens v3 API to retrieve all the payment methods saved for the customer.
- Use the vault_id associated with the payment method the customer selected in the input of the [Capture Payment for Order endpoint](https:/docs/api/orders/v2/#orders_capture) of the Orders v2 API.
- Log in to the [sandbox](https://www.sandbox.paypal.com/) with your merchant account and verify the transaction.


**info**
**Note:** The Javascript SDK has no direct support to show saved payments.


### Merchant-initiated transactions
For merchants or partners who want to process a recurring payment for a customer with an Apple Pay payment method already saved:


#### **`code of Merchant-initiated transactions`**
```curl

 curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders  -H "Content-Type: application/json"  -H "Authorization: Bearer ACCESS-TOKEN"  -d '{
      "intent": "CAPTURE",
      "purchase_units": [{
        "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
        "amount": {
          "currency_code": "USD",
          "value": "100.00"
        }
      }],
      "payment_source": {
        "apple_pay": {
          "stored_credential": {
            "payment_initiator": "MERCHANT",
            "payment_type": "RECURRING",
            "usage": "SUBSEQUENT",
          },
          "vault_id": "nkq2y9g"
        }
      }
    }

```


## Test your integration 
Test your Apple Pay integration in the PayPal sandbox and production environments to ensure that your app works correctly.

Use your personal sandbox login information during checkout to complete a payment using Apple Pay. Then, log into the sandbox site [sandbox.paypal.com](https://sandbox.paypal.com/) to see that the money has moved into your account.

- Open your test page with the Safari web browser on an iOS device or computer.
- Get a test card from your Apple sandbox account.
- Add the test card to your Apple Wallet on your iOS device or by using the Safari browser on the web.
- Tap the **Apple Pay** button to open a pop-up with the Apple Pay payment sheet.
- Make a payment using the Apple Pay payment sheet.
- If you have an additional confirmation page on your merchant website, continue to confirm the payment.
- Log in to your merchant account and continue to your confirmation page to confirm that the money you used for payment showed up in the account.

 

### Test cards for Apple Pay
Refer to Apple's [sandbox testing page](https://developer.apple.com/apple-pay/sandbox-testing/) to learn more about using test cards for Apple Pay.



## Next steps 
- Test and go live with this integration. See the **Go live** section below for more details.
- Complete [production onboarding](https://www.paypal.com/bizsignup/entry/product/ppcp) to be eligible to process cards with your live PayPal account.
- Change the credentials and API URLs from api-m.sandbox.paypal.com to api-m.paypal.com when going live with your integration.
- You can [create orders](https:/docs/api/orders/v2/#orders_create) without the payment_source.paypal.attributes.vault for subsequent or recurring transactions.
- You can [get a payment token](https:/docs/api/payment-tokens/v3/#payment-tokens_get) , [list all payment tokens](https:/docs/api/payment-tokens/v3/#payment-tokens_payment-tokens) , [delete a payment token](https:/docs/api/payment-tokens/v3/#payment-tokens_delete) , and more with the [Payment Method Tokens API](https:/docs/api/payment-tokens/v3/) .
- To manage subsequent or recurring transactions, see [Use Saved Payment Token](https:/docs/checkout/save-payment-methods/purchase-later/cards/#link-sampleapirequestwithpaymenttokenassociatedwithcard) .



## Go live 
- Go to paypal.com and sign in with your business account.
- Go to **Account Settings &gt; Payment Method &gt; Enable Apple Pay** .
- In the Apple Pay payment methods section, select **Get Started** .
- After you submit the details on the Profile collection, your status will change to "Your eligibility to save customer Apple Pay payment methods is under review". It might be approved instantly as well.
- Based on information provided in the profile collection of the Business Account, you might see a status like **Denied** , **Success** , or **Need more information** . Once the information is vetted, you get a **Success** status.
