---
title: Save PayPal with the Orders API
slug: /docs/checkout/save-payment-methods/during-purchase/orders-api/paypal/
createTime: "2024-10-24T00:05:36.317Z"
updateTime: "2025-05-13T10:57:09.893Z"
---

# Save PayPal with the Orders API

After customers save their PayPal Wallet, they can select it for faster checkout. Customers won't have to enter payment details for future transactions.

You can use the [Orders API](/docs/api/orders/v2/) to create a transaction and save the payer's PayPal Wallet.

Use a direct integration with the Orders API if you:

- Are PCI compliant when capturing and passing card information.
- Have opted not to integrate with a PayPal client-side JavaScript SDK and want to make a purchase and save the instrument used.

To save a payment method outside of a purchase, use the [Vault Payment Method API](/docs/api/payment-tokens/v3/) .

**warning**
**Important:** Don’t save PayPal as a payment method during purchase. For more information about securely saving payment methods and optimizing the buyer experience, see our [Best practices guide](/docs/checkout/standard/best-practices/) .

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
- You must be approved to enable a reference transaction if you want to save PayPal as a payment source. Contact your account manager for details.

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

##

## Set up your account to save payments

Set up your sandbox and live business accounts to save payment methods:

- Log in to the Developer Dashboard.
- Under **REST API apps** , select your app name.
- Under **Sandbox App Settings** &gt; **App Feature Options** , check **Accept payments** .
- Expand **Advanced options** . Confirm that **Vault** is selected.

##

Set up your server to call the Create Order API. The button that the payer selects determines the payment_source sent in the following sample. In the following sample, the payment_source is PayPal . The vault parameters in the request saves the payment_source for future use by the payer.

### Request to create order and save PayPal

#### **`Request to create order and save PayPal`**

```curl

      curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/ \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS-TOKEN" \
 -d '{
        "intent": "CAPTURE",
        "payment_source": {
        "paypal": {
          "attributes": {
            "vault": {
              "store_in_vault": "ON_SUCCESS",
              "usage_type": "MERCHANT"
            }
          },
          "experience_context": {
            "return_url": "https://example.com/returnUrl",
            "cancel_url": "https://example.com/cancelUrl"
          }
        }
      },
      "purchase_units": [
        {
          "amount": {
          "currency_code": "USD",
          "value": "100.00"
        }
      }
    ]
  }'

```

### Response

Note the status of the response. Some payment sources need payer approval before payment. If so, return the id back to your client to redirect the payer to a flow where they approve the payment method.

#### **`Response`**

```javascript

      {
  "id": "46299262185816041",
  "status": "PAYER_ACTION_REQUIRED",
  "payment_source": {
    "paypal": {}
  },
  "links": [{
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/46299262185816041",
      "rel": "self",
      "method": "GET",
    },
    {
      "href": "https://www.sandbox.paypal.com/checkoutnow?token=46299262185816041",
      "rel": "approve",
      "method": "GET",
    }
  ]
}

```

## Payer approval

Note the status of the response. Some payment sources need payer approval before payment. If so, return the id back to your client to redirect the payer to a flow where they approve the payment method.

## Authorize or capture order

After the payer approves, your server should call the following APIs:

- Capture Order API if the intent passed was CAPTURE .
- Authorize Order API if the intent passed was AUTHORIZE .

### Request

### Authorize

1curl-v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T/authorize\2-H"Content-Type: application/json"\3-H"Authorization: Bearer ACCESS-TOKEN"\4-d'{}'### Capture
1curl-v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T/capture\2-H"Content-Type: application/json"\3-H"Authorization: Bearer ACCESS-TOKEN"\4-d'{}'

### Response

The HTTP response codes HTTP 2xx or HTTP 200 are returned for a successful request.

The capture is successful if the purchase_units[0].payments.captures.status is COMPLETED . You can confirm with the payer that the payment has been captured.

#### **`Response`**

```javascript

      {
        {
          "id": "9YF83379T2523751N",
          "status": "COMPLETED",
          "payment_source": {
            "paypal": {
              "email_address": "email@example.com",
              "account_id": "AJM9JTWQJCFTA",
              "name": {
                "given_name": "Firstname",
                "surname": "Lastname"
              },
              "address": {
                "country_code": "US"
              },
              "attributes": {
                "vault": {
                  "id": "nkq2y9g",
                  "customer": {
                    "id" = "ROaPMoZUaV"
                  },
                  "status": "VAULTED",
                  "links": [{
                      "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/64n9c42",
                      "rel": "self",
                      "method": "GET"
                    },
                    {
                      "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/64n9c42",
                      "rel": "delete",
                      "method": "DELETE"
                    },
                    {
                      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/9YF83379T2523751N",
                      "rel": "up",
                      "method": "GET"
                    }
                  ]
                }
              }
            }
          },
          "purchase_units": [{
            "reference_id": "default",
            "shipping": {
              "name": {
                "full_name": "Firstname Lastname"
              },
              "address": {
                "address_line_1": "1 Main St",
                "admin_area_2": "San Jose",
                "admin_area_1": "CA",
                "postal_code": "95131",
                "country_code": "US"
              }
            },
            "payments": {
              "captures": [{
                "id": "9LY87817BF120310A",
                "status": "COMPLETED",
                "amount": {
                  "currency_code": "USD",
                  "value": "100.00"
                },
                "final_capture": true,
                "seller_protection": {
                  "status": "ELIGIBLE",
                  "dispute_categories": [
                    "ITEM_NOT_RECEIVED",
                    "UNAUTHORIZED_TRANSACTION"
                  ]
                },
                "seller_receivable_breakdown": {
                  "gross_amount": {
                    "currency_code": "USD",
                    "value": "100.00"
                  },
                  "paypal_fee": {
                    "currency_code": "USD",
                    "value": "3.98"
                  },
                  "net_amount": {
                    "currency_code": "USD",
                    "value": "96.02"
                  }
                },
                "links": [{
                    "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/9LY87817BF120310A",
                    "rel": "self",
                    "method": "GET"
                  },
                  {
                    "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/9LY87817BF120310A/refund",
                    "rel": "refund",
                    "method": "POST"
                  },
                  {
                    "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/9YF83379T2523751N",
                    "rel": "up",
                    "method": "GET"
                  }
                ],
                "create_time": "2022-08-12T18:16:42Z",
                "update_time": "2022-08-12T18:16:42Z"
              }]
            }
          }],
          "payer": {
            "name": {
              "given_name": "Firstname",
              "surname": "Lastname"
            },
            "email_address": "email@example.com",
            "payer_id": "AJM9JTWQJCFTA",
            "address": {
              "country_code": "US"
            }
          },
          "links": [{
            "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/9YF83379T2523751N",
            "rel": "self",
            "method": "GET"
          }]
        }

```

In the response from the Authorize or Capture request, the Orders v2 API interacts with the Vault v3 API. The Vault v3 API allows a PayPal Wallet to be saved. The response from the Orders v2 API contains the:

- vault.id .
- vault.status .
- links for the payment token of a recently vaulted PayPal Wallet.

Saving a payment source doesn't require the payer to be present after the payment has been authorized or captured. To keep checkout times as short as possible for payers, the Orders API returns a response as soon as a payment is captured.

Payment may be authorized or captured and a successful response returned from the Orders API without the provided payment_source being saved. In this scenario, the response returns the attributes.vault.status as "APPROVED" , instead of "VAULTED" .

An example of the attributes object from this scenario is included in the following sample

#### **`Check Orders API response code`**

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

## Webhooks for saving payment methods

You can configure and subscribe to the VAULT.PAYMENT-TOKEN.CREATED webhook, which is generated when saving payment methods with the Orders API.

You'll receive a vault_id when an APPROVED status is returned.

| Event                                                                                                                                                                           | Trigger                                                                                                                                       | Payment methods  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| [](#vault.payment-token.createda-payment-token-is-created-to-save-a-payment-method.cards-and-paypal)VAULT.PAYMENT-TOKEN.CREATED                                                 | A payment token is created to save a payment method.                                                                                          | Cards and PayPal |
| [](#vault.payment-token.deleteda-payment-token-is-deleted.-the-payer's-payment-method-is-no-longer-saved-to-the-paypal-vault.cards-and-paypal)VAULT.PAYMENT-TOKEN.DELETED       | A payment token is deleted. The payer's payment method is no longer saved to the PayPal vault.                                                | Cards and PayPal |
| [](#vault.payment-token.deletion-initiateda-request-to-delete-a-payment-token-has-been-submitted-to-the-payment-method-tokens-api.paypal)VAULT.PAYMENT-TOKEN.DELETION-INITIATED | A request to delete a payment token has been submitted to the[Payment Method Tokens API](/docs/api/payment-tokens/v3/#payment-tokens_delete). | PayPal           |

For more information on webhooks, see [webhooks](https://developer.paypal.com/api/rest/webhooks/) .

## Next step

Follow [Use payment method token with checkout](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/paypal/#link-usepaymenttokenonbehalfofpayer) for subsequent or recurring transactions.

## See also

[Payment Method Token API errors](https://developer.paypal.com/docs/api/payment-tokens/v3/#errors/)
