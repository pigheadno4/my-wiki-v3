---
title: Save PayPal with the Payment Method Tokens API
slug: /docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/paypal/
createTime: "2024-10-24T18:53:36.198Z"
updateTime: "2025-08-25T11:29:32.706Z"
---

# Save PayPal with the Payment Method Tokens API

No transaction is required when payment methods are saved with the [Payment Method Tokens API](https://developer.paypal.com/docs/api/payment-tokens/v3/) . You can charge payers after a set amount of time. Payers don't need to be present when charged. A common use case is offering a free trial and charging payers after the trial expires.

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

## Know before you code

- This server-side integration uses the [Payment Method Tokens API](/docs/api/payment-tokens/v3/) .
- The Payment Method Tokens API supports saving cards and PayPal Wallets.
- Complete the steps in [Get started](/api/rest/) to get the following sandbox account information from the Developer Dashboard: - Your sandbox account login information
- Your access token

- You must be approved and have your account configured for billing agreements to set up a reference transaction. Contact your account manager for details.

## Check eligibility

- Go to [paypal.com](https://www.paypal.com) and sign in with your business account.
- Go to **Account Settings** &gt; **Payment Preferences** &gt; **Save PayPal and Venmo payment methods** .
- In the Save PayPal and Venmo payment methods section, select **Get Started** .
- When you submit profile details, PayPal reviews your eligibility to save PayPal Wallets and Venmo accounts.
- After PayPal reviews your eligibility, you'll see a status of **Success** , **Need more information** , or **Denied** .

## 1. Set up your account to save payments

Set up your sandbox and live business accounts to save payment methods:

- Log in to the Developer Dashboard.
- Under **REST API apps** , select your app name.
- Under **Sandbox App Settings** &gt; **App Feature Options** , check **Accept payments** .
- Expand **Advanced options** . Confirm that **Vault** is selected.

## 2. Create setup token to save PayPal Wallet

The payer must authenticate and approve the creation of a billing agreement. Then you can create a setup token to save PayPal as a payment method.

The initial POST on setup-tokens completes the following actions:

- Returns a PAYER_ACTION_REQUIRED status
- Creates a temporary setup token
- Redirects to the approve URL

When saving a payer's PayPal Wallet for first time, the response to the setup-token request returns the PayPal-generated customer.id and the setup_token_id .

**info**
**Tip:** For a payer with previously-stored payment_sources , pass the customer.id in the setup-token request. This links additional payment_sources to the payer.

You can store a Merchant Customer ID aligned with your system to simplify the mapping of customer information within your system and PayPal when creating a setup token. This is an optional field that will return the value shared in the response.

To create a setup token for PayPal that triggers a payer action, copy and modify the following code:

#### **`Sample API request`**

```curl
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens' \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS-TOKEN" \
 -H "PayPal-Request-Id: REQUEST-ID" \
 -d '{
      "payment_source": {
          "paypal": {
              "description": "Description for PayPal to be shown to PayPal payer",
              "shipping": {
                  "name": {
                      "full_name": "Firstname Lastname"
                  },
                  "address": {
                      "address_line_1": "2211 N First Street",
                      "address_line_2": "Building 17",
                      "admin_area_2": "San Jose",
                      "admin_area_1": "CA",
                      "postal_code": "95131",
                      "country_code": "US"
                  }
              },
              "permit_multiple_payment_tokens": false,
              "usage_pattern": "IMMEDIATE",
              "usage_type": "MERCHANT",
              "customer_type": "CONSUMER",
              "experience_context": {
                  "shipping_preference": "SET_PROVIDED_ADDRESS",
                  "payment_method_preference":    "IMMEDIATE_PAYMENT_REQUIRED",
                  "brand_name": "EXAMPLE INC",
                  "locale": "en-US",
                  "return_url": "https://example.com/returnUrl",
                  "cancel_url": "https://example.com/cancelUrl"
              }
          }
      }
  }'
```

### Modify the code

- Copy the code sample.
- Change ACCESS-TOKEN to your [sandbox access token](https:/api/rest/authentication) .
- Change REQUEST-ID to a set of unique alphanumeric characters such as a timestamp.
- Use PayPal as the payment_source . Complete the rest of the source object for your use case and business.
- Update the return_url value with the URL where the payer is redirected after they approve the flow.
- Update the cancel_url value with the URL where the payer is redirected after they cancel the flow.

### Step result

A successful request results in the following:

- An HTTP response code of 200 or 201 . Returns 200 for an idempotent request.
- A status of PAYER_ACTION_REQUIRED .
- HATEOAS links:

| Rel                                                                                                                               | Method | Description                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------- |
| [](#approvegetuse-this-link-to-take-your-payer-through-a-paypal-hosted-approval-flow.)approve                                     | GET    | Use this link to take your payer through a PayPal-hosted approval flow.                                    |
| [](#confirmpostmake-a-post-request-to-use-an-approved-setup-token-to-save-the-paypal-wallet-and-generate-a-payment-token.)confirm | POST   | Make a POST request to use an approved setup token to save the PayPal Wallet and generate a payment token. |
| [](#selfgetmake-a-get-request-to-view-the-state-of-your-setup-token-and-payment-method-details.)self                              | GET    | Make a GET request to view the state of your setup token and payment method details.                       |

### Sample API response

#### **`Sample API response`**

```javascript

  {
  "id": "4G4976650J0948357",
  "customer": {
    "id": "customer_4029352051"
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
          "address_line_1": "2211 N First Street",
          "address_line_2": "Building 17",
          "admin_area_2": "San Jose",
          "admin_area_1": "CA",
          "postal_code": "95131",
          "country_code": "US"
        }
      },
      "permit_multiple_payment_tokens": false,
      "usage_type": "MERCHANT",
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

By default, the setup token expires after 3 days. After the payer completes the approval flow, you can upgrade the setup token to a full payment method token by calling [create-payment-tokens](https:/docs/api/payment-tokens/v3/#payment-tokens_create) .

You can store a Merchant Customer ID aligned with your system to simplify the mapping of customer information within your system and PayPal when creating a payment token. This is an optional field that will return the value shared in the response.

Use an approved setup token to save the payer's payment method to the vault. Then, copy the sample request code to generate a payment token:

### Sample API request

#### **`Sample API request`**

```curl

  curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v3/vault/payment-tokens' \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS-TOKEN" \
 -H "PayPal-Request-Id: REQUEST-ID" \
 -d '{
      "payment_source": {
          "token": {
              "id": "4G4976650J0948357",
              "type": "SETUP_TOKEN"
          }
      }
  }'

```

### Modify the code

- Copy the code sample.
- Change ACCESS-TOKEN to your sandbox access token.
- Change REQUEST-ID to a unique alphanumeric set of characters such as a time stamp.
- Use token as the payment source and complete the rest of the source object for your use case and business.
- Use your setup token ID to pass in the payment source parameter and type as the SETUP_TOKEN .

### Step result

A successful request results in the following:

- An HTTP response code of 200 or 201 . Returns 200 for an idempotent request.
- ID of the payment token and associated payment method information.
- HATEOAS links:

| Rel    | Method | Description                                                                      |
| ------ | ------ | -------------------------------------------------------------------------------- |
| self   | GET    | Make a GET request to this link to retrieve data about the saved payment method. |
| delete | DELETE | Make a DELETE request to delete the payment token.                               |

### Sample API response

#### **`Sample API response`**

```javascript

  {
  "id": "jwgvx42",
  "customer": {
    "id": "customer_4029352051"
  },
  "payment_source": {
    "paypal": {
      "description": "Description for PayPal to be shown to PayPal payer",
      "usage_pattern": "IMMEDIATE",
      "shipping": {
        "name": {
          "full_name": "Firstname Lastname"
        },
        "address": {
          "address_line_1": "2211 N First Street",
          "address_line_2": "Building 17",
          "admin_area_2": "San Jose",
          "admin_area_1": "CA",
          "postal_code": "95131",
          "country_code": "US"
        }
      },
      "permit_multiple_payment_tokens": false,
      "usage_type": "MERCHANT",
      "customer_type": "CONSUMER",
      "email_address": "email@example.com",
      "payer_id": "AJM9JTWQJCFTA"
    }
  },
  "links": [
    {
      "rel": "self",
      "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/jwgvx42",
      "method": "GET",
      "encType": "application/json"
    },
    {
      "rel": "delete",
      "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/jwgvx42",
      "method": "DELETE",
      "encType": "application/json"
    }
  ]
}

```

After you create a payment method token, use the token instead of the payment method to create a purchase and capture the payment with the Orders API.

You can store a Merchant Customer ID aligned with your system to simplify the mapping of customer information within your system and PayPal. This is an optional field that will return the value shared in the response.

Set the payment_source to specify the payment source type. Set the vault_id to the payment method token you received.

### Sample API request with payment token associated with PayPal account

Copy the following code sample and modify it.

#### **`Sample API request with payment token associated with PayPal account`**

```curl

  curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders' \
 -H "PayPal-Request-Id: REQUEST-ID" \
 -H "Authorization: Bearer ACCESS-TOKEN" \
 -H "Content-Type: application/json" \
 -d '{
      "intent": "CAPTURE",
      "purchase_units": [
          {
              "amount": {
                  "currency_code": "USD",
                  "value": "100.00"
              }
          }
      ],
      "payment_source": {
          "paypal": {
              "vault_id":"jwgvx42"
          }
      }
  }'

```

### Modify the code

- Copy the code sample.
- Change ACCESS-TOKEN to your [sandbox access token](https:/api/rest/authentication) .
- Change REQUEST-ID to a set of unique alphanumeric characters such as a time stamp.
- Use the ID of your payment method token as the vault_id .

### Sample API response

#### **`Sample API response`**

```javascript

  {
  "id": "4TH21426N05692944",
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
      }
    }
  },
  "purchase_units": [
    {
      "reference_id": "default",
      "payments": {
        "captures": [
          {
            "id": "3B017991HX624902V",
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
            "links": [
              {
                "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/3B017991HX624902V",
                "rel": "self",
                "method": "GET"
              },
              {
                "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/3B017991HX624902V/refund",
                "rel": "refund",
                "method": "POST"
              },
              {
                "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/4TH21426N05692944",
                "rel": "up",
                "method": "GET"
              }
            ],
            "create_time": "2022-08-08T23:13:35Z",
            "update_time": "2022-08-08T23:13:35Z"
          }
        ]
      }
    }
  ],
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
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/4TH21426N05692944",
      "rel": "self",
      "method": "GET"
    }
  ]
}

```

When the payer isn't present to check out, you can use the payment method token to create an order on behalf of the payer.

### 1. Retrieve a payer's payment method token

If you stored the payment token the payer created on your site, skip this step.

To make a payment on behalf of the payer, retrieve the payment token they created. You'll need the customer ID that you assigned to this payer when saving the payment method.

### Sample API request

**API endpoint used:** [Payment tokens](https://developer.paypal.com/docs/api/payment-tokens/v3/)

#### **`Sample API request`**

```curl

  curl -v -k -X GET 'https://api-m.sandbox.paypal.com/v3/vault/payment-tokens?customer_id=customer_4029352051' \
 -H 'Authorization: Bearer ACCESS-TOKEN' \
 -H 'Content-Type: application/json'

```

### Modify the code

- Copy the code sample.
- Change ACCESS-TOKEN to your [sandbox access token](https://developer.paypal.com/api/rest/authentication) .
- Pass the PayPal-generated customer.id to retrieve the payment token details associated with the payer.
- If stored in the payment token, the response will return the Merchant Customer ID.

### Sample response

#### **`Sample response`**

```javascript

  {
  "customer": {
    "id": "customer_4029352051"
  },
  "payment_tokens": [
    {
      "id": "jwgvx42",
      "customer": {
        "id": "customer_4029352051"
      },
      "payment_source": {
        "paypal": {
          "description": "Description for PayPal to be shown to PayPal payer",
          "shipping": {
            "name": {
              "full_name": "Firstname Lastname"
            },
            "address": {
              "address_line_1": "2211 N First Street",
              "address_line_2": "Building 17",
              "admin_area_2": "San Jose",
              "admin_area_1": "CA",
              "postal_code": "95131",
              "country_code": "US"
            }
          },
          "usage_type": "MERCHANT",
          "customer_type": "CONSUMER",
          "name": {
            "given_name": "Firstname",
            "surname": "Lastname",
            "full_name": "Firstname Lastname"
          },
          "email_address": "email@example.com",
          "payer_id": "AJM9JTWQJCFTA",
          "phone": {
            "phone_number": {
              "country_code": "US",
              "national_number": "408-208-9263"
            }
          }
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/jwgvx42",
          "method": "GET",
          "encType": "application/json"
        },
        {
          "rel": "delete",
          "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/jwgvx42",
          "method": "DELETE",
          "encType": "application/json"
        }
      ]
    }
  ],
  "links": [
    {
      "rel": "self",
      "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens?customer_id=customer_4029352051&page=1&page_size=5&total_required=false",
      "method": "GET",
      "encType": "application/json"
    },
    {
      "rel": "first",
      "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens?customer_id=customer_4029352051&page=1&page_size=5&total_required=false",
      "method": "GET",
      "encType": "application/json"
    },
    {
      "rel": "last",
      "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens?customer_id=customer_4029352051&page=1&page_size=5&total_required=false",
      "method": "GET",
      "encType": "application/json"
    }
  ]
}

```

### Step result

A successful request results in the following:

- An HTTP response code of 200 OK .
- Payment method details and status for the provided payment token.
- HATEOAS links:

| Rel    | Method | Description                                                                      |
| ------ | ------ | -------------------------------------------------------------------------------- |
| self   | GET    | Make a GET request to this link to retrieve data about the saved payment method. |
| delete | DELETE | Make a DELETE request to delete the payment token from the vault.                |

### 2. Use payment method token with checkout

After you get the payment method token ID, you can use a payment method token with checkout to create your order with the [Orders v2 API](/docs/api/orders/v2/) .

#### **`Create order with payment method token`**

```curl
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders' \
  -H "PayPal-Request-Id: YOUR-REQUEST-ID" \
  -H "Authorization: Bearer YOUR-ACCESS-TOKEN" \
  -H "PayPal-Client-Metadata-Id: YOUR-PAYPAL-CLIENT-METADATA-ID" \
  -H "Content-Type: application/json" \
  -d '{
       "intent": "CAPTURE",
       "purchase_units": [
         {
           "amount": {
             "currency_code": "USD",
             "value": "100.00"
           }
         }
       ],
       "payment_source": {
         "paypal": {
           "vault_id": "jwgvx42"
         }
       }
     }'
```

## Webhooks

| Event                                                                                                                                                                                                                                                                                    | Trigger                                                                                                                                                                   | Payment methods  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| [](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/paypal/#vault.payment-token.createda-payment-token-is-created-to-save-a-payment-method.cards-and-paypal)VAULT.PAYMENT-TOKEN.CREATED                                                 | A payment token is created to save a payment method.                                                                                                                      | Cards and PayPal |
| [](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/paypal/#vault.payment-token.deleteda-payment-token-is-deleted.-the-payer's-payment-method-is-no-longer-saved-to-the-paypal-vault.cards-and-paypal)VAULT.PAYMENT-TOKEN.DELETED       | A payment token is deleted. The payer's payment method is no longer saved to the PayPal vault.                                                                            | Cards and PayPal |
| [](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/paypal/#vault.payment-token.deletion-initiateda-request-to-delete-a-payment-token-has-been-submitted-to-the-payment-method-tokens-api.paypal)VAULT.PAYMENT-TOKEN.DELETION-INITIATED | A request to delete a payment token has been submitted to the[Payment Method Tokens API](https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_delete). | PayPal           |

For more information on webhooks, see [webhooks](https://developer.paypal.com/api/rest/webhooks/) .

##

## Next steps

- [Test and go live](/api/rest/production/) with this integration. - Process PayPal Wallets with your live PayPal account by completing [production onboarding](https://www.paypal.com/bizsignup/entry/product/ppcp) .
- Remember to swap the credentials and API URL from sandbox to production when going live with your integration.

- You can [get a payment token](/docs/api/payment-tokens/v3/#payment-tokens_get) , [list all payment tokens](/docs/api/payment-tokens/v3/#payment-tokens_payment-tokens) , [delete a payment token](/docs/api/payment-tokens/v3/#payment-tokens_delete) , and more with the Payment Method Tokens API.

## See also

- [Set up payment buttons](https:/docs/checkout/standard/)
