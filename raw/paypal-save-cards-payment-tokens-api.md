---
title: Save cards with the Payment Method Tokens API
slug: /docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/cards/
createTime: "2024-10-25T07:56:13.187Z"
updateTime: "2025-08-25T11:29:32.706Z"
---

# Save cards with the Payment Method Tokens API

No transaction is required when payment methods are saved with the [Payment Method Tokens API](https://developer.paypal.com/docs/api/payment-tokens/v3/) . You can charge payers after a set amount of time. Payers don't need to be present when charged. A common use case is offering a free trial and charging payers after the trial expires.

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

- This server-side integration uses the [Payment Method Tokens REST API](https://developer.paypal.com/docs/api/payment-tokens/v3/) .
- The Payment Method Tokens API supports saving cards and PayPal Wallets.
- Complete the steps in [Get started](https://developer.paypal.com/api/rest/) to get the following sandbox account information from the Developer Dashboard: - Your sandbox account login information
- Your access token

- You'll need an existing [advanced credit and debit card payments](https://developer.paypal.com/docs/checkout/advanced/) integration. PayPal must approve your business account for advanced credit and debit card payments.
- The Payment Method Tokens API requires SAQ D PCI Compliance.

## 1. Set up your account to save payments

Set up your sandbox and live business accounts to save payment methods:

- Log in to the Developer Dashboard.
- Under **REST API apps** , select your app name.
- Under **Sandbox App Settings** &gt; **App Feature Options** , check **Accept payments** .
- Expand **Advanced options** . Confirm that **Vault** is selected.

## 2. Create setup token for card

Create a setup token for cards that have:

- No verification
- Smart authorization
- 3D Secure verification

When saving a card for the first time for a payer, the response to the setup token request returns the customer.id and the setup_token_id.

**info**
**Tip:** For a payer with previously stored payment_sources , pass the PayPal-generated customer.id in the setup token request. Then you can link additional payment_sources to this payer.

### No verification

### Setup token for card with no verification

There's usually no transaction when saving a card and creating a setup token. The data passed to the API is checked only for format.

### Sample API request

1curl-v -k -X POST'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens'\2-H"Content-Type: application/json"\3-H"Authorization: Bearer ACCESS-TOKEN"\4-H"PayPal-Request-Id: REQUEST-ID"\5-d'{6"payment_source": {7"card": {8"number": "4111111111111111",9"expiry": "2027-02",10"name": "Firstname Lastname",11"billing_address": {12"address_line_1": "2211 N First Street",13"address_line_2": "17.3.160",14"admin_area_1": "CA",15"admin_area_2": "San Jose",16"postal_code": "95131",17"country_code": "US"18},19"experience_context": {20"brand_name": "YourBrandName",21"locale": "en-US",22"return_url": "https://example.com/returnUrl",23"cancel_url": "https://example.com/cancelUrl"24}25}26}27}'### Modify the code

- Copy the sample request code.
- Change ACCESS-TOKEN to your [sandbox access token](https://developer.paypal.com/api/rest/authentication) .
- Change REQUEST-ID to a unique alphanumeric set of characters, for example, a time stamp.

### Step result

A successful request returns the following:

- An HTTP response code of 200 or 201 . Returns 200 for an idempotent request.
- The ID of the token in the id field.
- HATEOAS links:

| Rel     | Method | Description                                                                                         |
| ------- | ------ | --------------------------------------------------------------------------------------------------- |
| self    | GET    | Make a GET request to this link to retrieve payment source data associated with the setup token ID. |
| confirm | POST   | Make a POST request to generate the payment token using the approved setup token.                   |

### Sample API response

1{2"id":"5C991763VB2781612",3"customer":{4"id":"customer_4029352050"5},6"status":"APPROVED",7"payment_source":{8"card":{9"last_digits":"1111",10"expiry":"2027-02",11"name":"Firstname Lastname",12"billing_address":{13"address_line_1":"2211 N First Street",14"address_line_2":"17.3.160",15"admin_area_2":"San Jose",16"admin_area_1":"CA",17"postal_code":"95131",18"country_code":"US"19}20}21},22"links":[23{24"href":"https://api-m.sandbox.paypal.com/v3/vault/setup-tokens/5C991763VB2781612",25"rel":"self",26"method":"GET",27"encType":"application/json"28},29{30"href":"https://api-m.sandbox.paypal.com/v3/vault/payment-tokens",31"rel":"confirm",32"method":"POST",33"encType":"application/json"34}35]36}

### Smart Authorization

### Setup token for card with smart authorization

You can use the POST action to run smart authorization against the card. In countries where the issuing banks support it, smart authorization runs a zero-value authorization against the card.

If zero-value authorization is not supported, an authorization for a minimal value in the local currency is requested. Authorizations for minimal amounts aren't automatically voided and create a temporary hold against the payer's card.

To request verification of card data, add the verification_method parameter on the POST [setup-tokens](https://developer.paypal.com/docs/api/payment-tokens/v3/#setup-tokens) call.

### Sample API request

1curl-v -k -X POST'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens'\2-H"Authorization: Bearer ACCESS-TOKEN"\3-H"PayPal-Request-Id: REQUEST-ID"\4-H'Content-Type: application/json'\5-d'{6"payment_source": {7"card": {8"number": "4111111111111111",9"expiry": "2027-02",10"name": "Firstname Lastname",11"billing_address": {12"address_line_1": "2211 N First Street",13"address_line_2": "17.3.160",14"admin_area_1": "CA",15"admin_area_2": "San Jose",16"postal_code": "95131",17"country_code": "US"18},19"verification_method": "SCA_WHEN_REQUIRED",20"experience_context": {21"brand_name": "YourBrandName",22"locale": "en-US",23"return_url": "https://example.com/returnUrl",24"cancel_url": "https://example.com/cancelUrl"25}26}27}28}'### Modify the code

- Copy the sample request code.
- Change ACCESS-TOKEN to your sandbox access token.
- Change REQUEST-ID to a set of unique alphanumeric characters such as a time stamp.
- Use the card as the payment source and complete the rest of the source object for your use case and business.
- Pass the verification_method parameter with SCA_WHEN_REQUIRED to verify card data.
- Update the return_url value with the URL where the payer is redirected after they approve the flow.
- Update the cancel_url value with the URL where the payer is redirected after they cancel the flow.

### Step result

A successful request results in the following:

- An HTTP response code of 200 or 201 . Returns 200 for an idempotent request.
- A status of APPROVED .
- HATEOAS links:

| Rel     | Method | Description                                                                                             |
| ------- | ------ | ------------------------------------------------------------------------------------------------------- |
| confirm | POST   | Make a POST request to generate the payment token using the approved setup token.                       |
| self    | GET    | Make a GET request to this link to retrieve the payment source data associated with the setup token ID. |

If the request and authorization succeed:

- The setup token is approved
- Additional parameters are returned in the response.

### Sample API response

1{2"id":"5C991763VB2781612",3"status":"APPROVED",4"payment_source":{5"card":{6"brand":"VISA",7"last_digits":"1111",8"verification_status":"VERIFIED",9"verification":{10"network_transaction_id":"20286098380002303",11"time":"2020-10-07T22:44:41.000Z",12"amount":{13"value":"0.00",14"currency_code":"USD"15},16"processor_response":{17"avs_code":"M",18"cvv_code":"P"19}20}21}22},23"links":[24{25"href":"https://api-m.sandbox.paypal.com/v3/vault/payment-token",26"rel":"confirm",27"method":"POST",28"encType":"application/json"29},30{31"href":"https://api-m.sandbox.paypal.com/v3/vault/setup-tokens/5C991763VB2781612",32"rel":"self",33"method":"GET",34"encType":"application/json"35}36]37}### Testing AVS and CVV response codes
When running tests in the PayPal sandbox, you can generate AVS and CVV response codes.

When testing saved cards in the sandbox, use these [test cards](https://developer.paypal.com/api/rest/sandbox/card-testing/) .

Set Address Line 1 to the following values to generate an AVS response. Not all AVS codes are supported by all card types:

| Address Line 1 | AVS Response | Visa | Mastercard | American Express | Discover |
| -------------- | ------------ | ---- | ---------- | ---------------- | -------- |
| AVS_A_971      | A            | Yes  | Yes        | Yes              | Yes      |
| AVS_B_972      | B            | Yes  | No         | No               | No       |
| AVS_C_973      | C            | Yes  | No         | No               | No       |
| AVS_D_974      | D            | Yes  | No         | Yes              | No       |
| AVS_E_975      | E            | No   | Yes        | Yes              | No       |
| AVS_F_976      | F            | Yes  | No         | Yes              | No       |
| AVS_G_977      | G            | Yes  | No         | No               | Yes      |
| AVS_I_979      | I            | Yes  | No         | No               | No       |
| AVS_K_981      | K            | No   | No         | Yes              | No       |
| AVS_L_982      | L            | No   | No         | Yes              | No       |
| AVS_M_983      | M            | Yes  | No         | Yes              | No       |
| AVS_N_984      | N            | Yes  | Yes        | Yes              | Yes      |
| AVS_O_985      | O            | No   | No         | Yes              | No       |
| AVS_P_986      | P            | Yes  | No         | No               | No       |
| AVS_R_988      | R            | Yes  | Yes        | Yes              | Yes      |
| AVS_S_989      | S            | Yes  | Yes        | Yes              | Yes      |
| AVS_U_991      | U            | Yes  | Yes        | Yes              | Yes      |
| AVS_W_993      | W            | Yes  | Yes        | Yes              | Yes      |
| AVS_X_994      | X            | Yes  | Yes        | No               | Yes      |
| AVS_Y_995      | Y            | Yes  | Yes        | Yes              | Yes      |
| AVS_Z_996      | Z            | Yes  | Yes        | Yes              | Yes      |

- Set the CVV to the following values to generate a CVV response:

| CVV | CVV response | Description                                                        |
| --- | ------------ | ------------------------------------------------------------------ |
| 115 | M            | CVV2/CVC2/CID Match                                                |
| 116 | N            | CVV2/CVC2/CID No Match                                             |
| 120 | P            | Not Processed                                                      |
| 123 | S            | CVV2 should be on the card, but merchant indicated that it was not |
| 125 | U            | Unknown/Issuer does not participate                                |
| 130 | X            | Server provider did not respond (default)                          |

### 3D Secure

### Setup token for card with 3D Secure verification

Use [3D Secure authentication](https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/) to reduce the likelihood of fraud and improve transaction performance with supported cards. In some countries, authorizing a card can trigger a [3D Secure contingency](https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/api/#link-includeacontingencyfordsecure) . 3D Secure verification may occur in PSD2 countries, including members of the EU. For 3D Secure verification, pass SCA_ALWAYS or SCA_WHEN_REQUIRED in the payment_source.card.attributes.verification.method field for the create order request. The API response returns the order status as PAYER_ACTION_REQUIRED .

### Sample API request

1curl-v -k -X POST'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens'\2-H"Content-Type: application/json"\3-H"Authorization: Bearer ACCESS-TOKEN"\4-H"PayPal-Request-Id: REQUEST-ID"\5-d'{6"payment_source": {7"card": {8"number": "4111111111111111",9"expiry": "2027-02",10"name": "Firstname Lastname",11"billing_address": {12"address_line_1": "2211 N First Street",13"address_line_2": "17.3.160",14"admin_area_1": "CA",15"admin_area_2": "San Jose",16"postal_code": "95131",17"country_code": "US"18},19"verification_method": "SCA_WHEN_REQUIRED",20"experience_context": {21"brand_name": "YourBrandName",22"locale": "en-US",23"return_url": "https://example.com/returnUrl",24"cancel_url": "https://example.com/cancelUrl"25}26}27}28}'### Modify the code

- Copy the sample request code.
- Change ACCESS-TOKEN to your sandbox access token.
- Change REQUEST-ID to a unique alphanumeric set of characters such as a time stamp.
- Use a card as the payment source and complete the rest of the source object for your use case and business.
- Pass the verification_method parameter to verify card data.
- Update the return_url value with the URL where the payer is redirected after they approve the flow.
- Update the cancel_url value with the URL where the payer is redirected after they cancel the flow.

Pass one of the following verification_method attributes to verify card data:

| Verification Method | Description                                                |
| ------------------- | ---------------------------------------------------------- |
| SCA_WHEN_REQUIRED   | Triggers 3D Secure when mandated in your operating region. |
| SCA_ALWAYS          | Triggers 3D Secure for every transaction.                  |

### Step result

A successful request results in the following:

- An HTTP response code of 200 or 201 . Returns 200 for an idempotent request.
- A status of PAYER_ACTION_REQUIRED .
- HATEOAS links:

| Rel     | Method | Description                                                                                                 |
| ------- | ------ | ----------------------------------------------------------------------------------------------------------- |
| approve | GET    | Use this link to take the payer through the card approval flow.                                             |
| confirm | POST   | Make a POST request to use an approved setup token to save the payment method and generate a payment token. |
| self    | GET    | Make a GET request to view the state of your setup token and payment method details.                        |

### Sample API response

1{2"id":"5C991763VB2781612",3"customer":{4"id":"customer_4029352050"5},6"status":"PAYER_ACTION_REQUIRED",7"payment_source":{8"card":{9"last_digits":"1111",10"brand":"VISA",11"type":"CREDIT",12"expiry":"2027-02"13}14},15"links":[16{17"href":"https://paypal.com/webapps/helios?action=authenticate&validate_session_id=82cf4a87-5c40-0a27-1a09-4ffbb0d05fdc",18"rel":"approve",19"method":"GET",20"encType":"application/json"21},22{23"href":"https://api-m.sandbox.paypal.com/v3/vault/payment-token",24"rel":"confirm",25"method":"POST",26"encType":"application/json"27},28{29"href":"https://api-m.sandbox.paypal.com/v3/vault/setup-tokens/5C991763VB2771612",30"rel":"self",31"method":"GET",32"encType":"application/json"33}34]35}After the payer completes verification, make a POST request on the [payment-token](https://developer.paypal.com/docs/api/payment-tokens/v3/#create-a-payment-token) endpoint to convert the approved setup token to a payment token.

To retrieve 3D secure verification data associated with a setup token, make a GET request on a [setup-token](https://developer.paypal.com/docs/api/payment-tokens/v3/#setup-token) .

### Sample API request

1curl-v -k -X GET'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens/5C991763VB2781612'\2-H"Content-Type: application/json"\3-H"Authorization: Bearer ACCESS-TOKEN"\4-H"PayPal-Request-Id: REQUEST-ID"\### Step result
A successful request results in the following:

- An HTTP response code of 200 OK .
- A status of APPROVED .

| Parameter           | Description                                                                                                                                                                     |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| verification_method | The verification method value from the request is included in the response.                                                                                                     |
| verification_status | If the card is authorized, the status is set toVERIFIED.                                                                                                                        |
| authorization       | Details from the authorization are returned in anauthorizationobject. This includes the amount and currency requested, and the AVS and CVV results from the processor response. |

### Sample API response

1{2"id":"5C991763VB2771612",3"status":"APPROVED",4"payment_source":{5"card":{6"brand":"VISA",7"last_digits":"1111",8"verification_status":"VERIFIED",9"verification":{10"network_transaction_id":"20286098380002303",11"time":"2020-10-07T22:44:41.000Z",12"amount":{13"value":"0.00",14"currency_code":"USD"15},16"processor_response":{17"avs_code":"M",18"cvv_code":"P"19},20"three_d_secure":{21"type":"THREE_DS_AUTHENTICATION",22"eci_flag":"FULLY_AUTHENTICATED_TRANSACTION",23"card_brand":"VISA",24"enrolled":"Y",25"pares_status":"Y",26"three_ds_version":"2",27"authentication_type":"DYNAMIC",28"three_ds_server_transaction_id":"3d-secure-txn-id"29}30}31}32},33"links":[34{35"href":"https://api-m.sandbox.paypal.com/v3/vault/payment-token",36"rel":"confirm",37"method":"POST",38"encType":"application/json"39},40{41"href":"https://api-m.sandbox.paypal.com/v3/vault/setup-tokens/5C991763VB2771612",42"rel":"self",43"method":"GET",44"encType":"application/json"45}46]47}The issuing bank can still issue an authorization if a card fails the AVS and CVV checks. In this case, the setup token is created with an APPROVED status and the processor responses are returned to you. The eci_flag parameter of an authentication block indicates that 3D Secure was not completed.

You can choose whether to use a card that did not complete 3D Secure or failed AVS and CVV checks:

- To use the card, make a POST request on [add-payment-token](https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_create) . Convert the approved setup token to a full payment token.
- To reject the card, don't add the payment token or convert it to a full payment token.

### Testing with 3D Secure

In the sandbox, create a setup token and a 3D Secure token. Validate a card using card data from [3D Secure test scenarios](https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/test/) .

Use an approved setup token to save the payer's credit or debit card. Then, copy the sample request code to generate a payment token:

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
              "id": "5C991763VB2781612",
              "type": "SETUP_TOKEN"
          }
      }
  }'

```

### Modify the code

- Copy the sample request code.
- Change ACCESS-TOKEN to your sandbox access token.
- Change REQUEST-ID to a unique alphanumeric set of characters such as a time stamp.
- Use token as the payment source and complete the rest of the source object as appropriate for your use case and business.
- Use your setup token ID to pass in the payment source parameter and type as the SETUP_TOKEN .

### Step result

A successful request results in the following:

- HTTP response code HTTP 2xx or HTTP 200 .
- ID of the payment token and the associated payment method information.
- HATEOAS links:

| Rel                                                                                                                                                                                              | Method | Description                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | ------------------------------------------------------------------------ |
| [](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/cards/#selfgetmake-a-get-request-to-this-link-to-retrieve-data-about-the-saved-method.)self | GET    | Make a GET request to this link to retrieve data about the saved method. |
| [](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/cards/#deletedeletemake-a-delete-request-to-delete-the-saved-payment-token.)delete          | DELETE | Make a DELETE request to delete the saved payment token.                 |

###

### Sample API response

#### **`Sample API response`**

```.net

{
  "id": "dnbbj3g",
  "customer": {
    "id": "customer_4029352050"
  },
  "payment_source": {
    "card": {
      "last_digits": "1111",
      "name": "Firstname Lastname",
      "expiry": "2027-02",
      "brand": "VISA",
      "billing_address": {
        "address_line_1": "2211 N First Street",
        "address_line_2": "17.3.160",
        "admin_area_2": "San Jose",
        "admin_area_1": "CA",
        "postal_code": "95131",
        "country_code": "US",
      }
    }
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/dnbbj3g",
      "rel": "self",
      "method": "GET",
      "encType": "application/json"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/dnbbj3g",
      "rel": "delete",
      "method": "DELETE",
      "encType": "application/json"
    }
  ]
}

```

After you create a payment method token, use the token instead of the payment method to create a purchase and capture the payment with the Orders API.

You can store a Merchant Customer ID aligned with your system to simplify the mapping of customer information within your system and PayPal. This is an optional field that will return the value shared in the response.

Set the payment_source to specify the payment source type. Set the vault_id to the payment method token you received.

### Sample API request with payment token associated with card

Copy the following code sample and modify it.

#### **`Sample API request with payment token associated with card`**

```curl

  curl -v -k -X POST ' https://api-m.sandbox.paypal.com/v2/checkout/orders' \
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
          "card": {
              "vault_id":"dnbbj3g"
          }
      }
  }'

```

### Modify the code

- Copy the sample request code.
- Change ACCESS-TOKEN to your [sandbox access token](https://developer.paypal.com/api/rest/authentication) .
- Change REQUEST-ID to a set of unique alphanumeric characters such as a time stamp.
- For vault_id , enter the ID of your payment method token.

### Sample API response

#### **`Sample API response`**

```.net

  {
  "id": "5O190127TN364715T",
  "status": "COMPLETED",
  "payment_source": {
    "card": {
      "brand": "VISA",
      "last_digits": "1111"
    }
  }
  "purchase_units": [
    {
      "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
      "payments": {
        "captures": [
          {
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
            "links": [
              {
                "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/3C679366HH908993F",
                "rel": "self",
                "method": "GET"
              },
              {
                "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/3C679366HH908993F/refund",
                "rel": "refund",
                "method": "POST"
              },
              {
                "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",
                "rel": "up",
                "method": "GET"
              }
            ]
          }
        ]
      }
    }
  ],
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",
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

  curl -v -k -X GET 'https://api-m.sandbox.paypal.com/v3/vault/payment-tokens?customer_id=customer_4029352050' \
 -H 'Authorization: Bearer ACCESS-TOKEN' \
 -H 'Content-Type: application/json'

```

### Modify the code

- Copy the code sample.
- Change ACCESS-TOKEN to your [sandbox access token](https://developer.paypal.com/api/rest/authentication) .
- Pass the PayPal-generated customer.id to retrieve the payment token details associated with the payer.
- If stored in the payment token, the response will return the Merchant Customer ID.

### Sample API response

#### **`Sample API response`**

```.net

  {
  "customer": {
    "id": "customer_4029352050"
  },
  "payment_tokens": [
    {
      "id": "dnbbj3g",
      "customer": {
        "id": "customer_4029352050"
      },
      "payment_source": {
        "card": {
          "name": "Firstname Lastname",
          "last_digits": "1111",
          "brand": "VISA",
          "expiry": "2027-02",
          "billing_address": {
            "address_line_1": "2211 N First Street",
            "address_line_2": "17.3.160",
            "admin_area_2": "San Jose",
            "admin_area_1": "CA",
            "postal_code": "95131",
            "country_code": "US",
          }
        }
      },
      "links": [
        {
          "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/dnbbj3g",
          "rel": "self",
          "method": "GET",
          "encType": "application/json"
        },
        {
          "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/dnbbj3g",
          "rel": "delete",
          "method": "DELETE",
          "encType": "application/json"
        }
      ]
    }
  ],
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens?pageNumber=1&totalRequired=false&customer_id=customer_4029352050&pageSizeInternal=5",
      "rel": "self",
      "method": "GET",
      "encType": "application/json"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens?pageNumber=1&totalRequired=false&customer_id=customer_4029352050&pageSizeInternal=5",
      "rel": "first",
      "method": "GET",
      "encType": "application/json"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens?pageNumber=1&totalRequired=false&customer_id=customer_4029352050&pageSizeInternal=5",
      "rel": "last",
      "method": "GET",
      "encType": "application/json"
    }
  ]
}

```

### Step result

A successful request results in the following:

- An HTTP response code of 200 OK .
- Payment method details and status for given payment token.
- HATEOAS links:

| Rel                                                                                                                                                                                              | Method | Description                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | ------------------------------------------------------------------------ |
| [](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/cards/#selfgetmake-a-get-request-to-this-link-to-retrieve-data-about-the-saved-method.)self | GET    | Make a GET request to this link to retrieve data about the saved method. |
| [](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/cards/#deletedeletemake-a-delete-request-to-delete-the-payment-token.)delete                | DELETE | Make a DELETE request to delete the payment token.                       |

### 2. Use payment method token with checkout

After you get the payment method token ID, you can use a payment method token with checkout to create your order.

## Webhooks

| Event                                                                                                                                                                                                                                                                                    | Trigger                                                                                                                                                                   | Payment methods  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| [](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/paypal/#vault.payment-token.createda-payment-token-is-created-to-save-a-payment-method.cards-and-paypal)VAULT.PAYMENT-TOKEN.CREATED                                                 | A payment token is created to save a payment method.                                                                                                                      | Cards and PayPal |
| [](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/paypal/#vault.payment-token.deleteda-payment-token-is-deleted.-the-payer's-payment-method-is-no-longer-saved-to-the-paypal-vault.cards-and-paypal)VAULT.PAYMENT-TOKEN.DELETED       | A payment token is deleted. The payer's payment method is no longer saved to the PayPal vault.                                                                            | Cards and PayPal |
| [](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/paypal/#vault.payment-token.deletion-initiateda-request-to-delete-a-payment-token-has-been-submitted-to-the-payment-method-tokens-api.paypal)VAULT.PAYMENT-TOKEN.DELETION-INITIATED | A request to delete a payment token has been submitted to the[Payment Method Tokens API](https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_delete). | PayPal           |

For more information on webhooks, see [webhooks](https://developer.paypal.com/api/rest/webhooks/) .

##

## Next steps

- [Test and go live](https://developer.paypal.com/api/rest/production/) with this integration. - Process credit and debit cards with your live PayPal account by completing [production onboarding](https://www.paypal.com/bizsignup/entry/product/ppcp) .
- Remember to swap the credentials and API URL from sandbox to production when going live with your integration.

- You can [get a payment token](https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_get) , [list all payment tokens](https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_payment-tokens) , [delete a payment token](https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_delete) , and more with the Payment Method Tokens API.

## See also

- [Set up payment buttons](https://developer.paypal.com/docs/checkout/standard/)
- [Advanced credit and debit cards payments](https://developer.paypal.com/docs/checkout/advanced/)
- [Real-time account updater](https://developer.paypal.com/docs/checkout/advanced/customize/rtau/) to keep saved cards up-to-date
