---
title: Save cards with the Orders API
slug: /docs/checkout/save-payment-methods/during-purchase/orders-api/cards/
createTime: "2024-10-24T10:15:04.296Z"
updateTime: "2025-05-13T15:09:14.770Z"
---

# Save cards with the Orders API

After customers save their credit or debit card, they can select it for faster checkout. Customers won't have to enter payment details for future transactions.

Save cards with the Orders API if you want to save cards during checkout but aren't [PCI Compliant - SAQ A](https://www.pcisecuritystandards.org/pci_security/completing_self_assessment) .

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

## Know before you code

- The Orders API supports saving PayPal and card payment methods only.
- Passing card data to the Orders API requires you to be PCI Compliant - SAQ D.

- You'll need to have an existing [advanced credit and debit card payments](https://developer.paypal.com/docs/multiparty/checkout/advanced/) integration. PayPal must approve your account to process advanced credit and debit card payments.

## How it works

When a payer on your website saves their payment method, PayPal creates a customer record. PayPal then encrypts the payment method information and stores it in a digital vault. The vault is accessible only by the billing agreement holder.

- The payer saves their payment method.
- For a first-time payer, PayPal creates a customer ID. Store this within your system for future use.
- Pass a call into the Orders API. Include the payment method, customer ID, and an indication that the payment method should be saved.
- If the order is processed and the payment method is saved, you receive a payment method token in the Orders API response.
- Pass the payment method token into the Orders API to populate the checkout page with the saved payment method.

The checkout process is now shorter because it uses saved payment information.

##

## Check eligibility

- Go to [paypal.com](https://www.paypal.com/) and sign in with your business account.
- Go to **Account Settings** &gt; **Payment Preferences** &gt; **Save PayPal and Venmo payment methods** .
- In the Save PayPal and Venmo payment methods section, select **Get Started** .
- When you submit profile details, PayPal reviews your eligibility to save PayPal Wallets and Venmo accounts.
- After PayPal reviews your eligibility, you'll see a status of **Success** , **Need more information** , or **Denied** .

## Set up your account to save payments

Set up your sandbox and live business accounts to save payment methods:

- Log in to the Developer Dashboard.
- Under **REST API apps** , select your app name.
- Under **Sandbox App Settings** &gt; **App Feature Options** , check **Accept payments** .
- Expand **Advanced options** . Confirm that **Vault** is selected.

Set up your server to call the Create Order API. When a payer is using a card to check out, the Orders API allows you to capture the payment in a single request. In the following sample, the Authorize and Capture requests occur in a single request, and the card is stored in PayPal's vault.

Use [3D Secure authentication](https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/) to reduce the likelihood of fraud and improve transaction performance with supported cards. In some countries, authorizing a card can trigger a [3D Secure contingency](https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/api/#link-includeacontingencyfordsecure) . 3D Secure verification may occur in PSD2 countries, including members of the EU. For 3D Secure verification, pass SCA_ALWAYS or SCA_WHEN_REQUIRED in the payment_source.card.attributes.verification.method field for the create order request. The API response returns the order status as PAYER_ACTION_REQUIRED .

### Request

Create an order with a card as a payment source and store the card in the vault with 3D Secure verification when required:

#### **`Request`**

```curl

  curl -v -X POST "https://api-m.sandbox.paypal.com/v2/checkout/orders/" \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS-TOKEN" \
 -d '{
    "intent": "CAPTURE",
    "payment_source": {
        "card": {
            "number": "4111111111111111",
            "expiry": "2026-02",
            "name": "Firstname Lastname",
            "billing_address": {
                "address_line_1": "2211 N First Street",
                "address_line_2": "Building 17",
                "admin_area_2": "San Jose",
                "admin_area_1": "CA",
                "postal_code": "95131",
                "country_code": "US"
            },
            "attributes": {
                "verification": {
                  "method": "SCA_WHEN_REQUIRED"
                },
                "vault": {
                    "store_in_vault": "ON_SUCCESS"
                }
            }
        }
    },
    "purchase_units": [
        {
            "amount": {
                "currency_code": "USD",
                "value": "101.00"
            }
        }
    ]
}

```

### Response

**info**
**Note:** Store the payment_source.card.attributes.vault.id in your database. The vault ID represents the payer's card in future transactions.

Because 3D Secure verification wasn't required in this example, the API response doesn't return PAYER_ACTION_REQUIRED as the order status.

#### **`Response`**

```.net

  {
    "id": "5O190127TN364715T",
    "status": "COMPLETED",
    "payment_source": {
      "card": {
        "last_digits": "1111",
        "brand": "VISA",
        "attributes": {
            "vault": {
            "id": "nkq2y9g",
            "customer" : {
                "id" = "ROaPMoZUaV"
            },
           "status" : "VAULTED",
            "links": [{
                "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/7dyps8w",
                "rel": "self",
                "method": "GET"
              },
              {
                "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/7dyps8w",
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
      "reference_id": "refernece_id_1001",
      "payments": {
        "captures": [{
          "id": "9ET27879VC451574K",
          "status": "COMPLETED",
          "amount": {
            "currency_code": "USD",
            "value": "100.00"
          },
          "final_capture": true,
          "disbursement_mode": "INSTANT",
          "seller_protection": {
            "status": "NOT_ELIGIBLE"
          },
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
          "invoice_id": "invoice_id_8L181959W1796210B",
          "custom_id": "custom_id_1001",
          "links": [{
              "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/9ET27879VC451574K",
              "rel": "self",
              "method": "GET"
            },
            {
              "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/9ET27879VC451574K/refund",
              "rel": "refund",
              "method": "POST"
            },
            {
              "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/0M526810X2956752F",
              "rel": "up",
              "method": "GET"
            }
          ],
          "create_time": "2022-05-04T21:24:00Z",
          "update_time": "2022-05-04T21:24:00Z",
          "processor_response": {
            "avs_code": "A",
            "cvv_code": "M",
            "response_code": "0000"
          }
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

In the response from the Authorize or Capture request, the Orders v2 API interacts with the Vault v3 API. The Vault v3 API allows a card to be saved.

As seen previously, payment_source.card.attributes.vault has the relevant information with the vault.id (when vault.status is VAULTED ) which can be used for subsequent payments.

### Check Orders API response

Saving a payment source does not require the payer to be present after the payment has been authorized or captured. In order to keep checkout times as short as possible for payers, the Orders API is optimized to return a response as soon as a payment is captured.

This means that the payment may be authorized or captured, and a successful response is returned from the Orders API without the provided payment_source being vaulted. The Orders response after authorization or capture will instead return attributes.vault.status as "APPROVED" , instead of "VAULTED" .

An example of the attributes object from this scenario:

#### **`attributes`**

```.net

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

### Save approved payment source

The Payment Method Tokens API still saves the payment source even after the Orders API returns its response and sends a webhook after the payment source is saved.

In order to retrieve a vault_id when an APPROVED status is returned, you'll need to subscribe to the VAULT.PAYMENT-TOKEN.CREATED [webhook](https://developer.paypal.com/api/rest/webhooks/) .

The Payment Method Tokens API sends a webhook after the payment source is saved. An example of the VAULT.PAYMENT-TOKEN.CREATED webhook payload is shown in the following sample:

#### **`VAULT.PAYMENT-TOKEN.CREATED`**

```.net

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
            "id":"9n6724m",
            "payment_source":{
               "card":{
                  "last_digits":"1111",
                  "brand":"VISA",
                  "expiry":"2027-02",
                  "billing_address":{
                     "address_line_1":"2211 N First Street",
                     "address_line_2":"17.3.160",
                     "admin_area_2":"San Jose",
                     "admin_area_1":"CA",
                     "postal_code":"95131",
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

As seen previously, the resource.id field is the vault ID. The resource.customer.id is the PayPal-generated customer ID.

## Next steps

- Follow [Use payment method token with checkout](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/paypal/#link-usepaymenttokenonbehalfofpayer) for subsequent or recurring transactions.
- You can configure and subscribe to the VAULT.PAYMENT-TOKEN.CREATED webhook, which is generated when vaulting with the Orders API.
- To learn more about webhooks, see the [webhooks documentation](https://developer.paypal.com/api/rest/webhooks/) .
- Keep saved cards up-to-date with the [real-time account updater](https://developer.paypal.com/docs/checkout/advanced/customize/rtau/) .
