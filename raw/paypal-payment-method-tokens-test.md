<!-- Source URL: https://docs.paypal.ai/payments/methods/save-payment-tokens/test -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Test saving cards with a direct Payment Method Tokens API integration

The Payment Method Tokens API can create a setup token for credit or debit cards that have:

- No verification
- Smart authorization
- 3D Secure verification

Send a call for each card type to test your integration works as expected.

## Prerequisites

You'll need a [Payment Method Tokens API cards integration](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/cards/).

## No verification

For cards with no verification, the card data passed to the API is checked only for format.

### Sample request for setup token with no verification

1. Change `ACCESS-TOKEN` to your sandbox access token.
2. Change `REQUEST-ID` to a unique alphanumeric set of characters, for example, a time stamp.

Copy and modify the following code sample to create a setup token associated with a credit or debit card with no verification.

Endpoint: [Create a setup token](https://developer.paypal.com/docs/api/payment-tokens/v3/#setup-tokens_create)

```bash theme={null}
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens' \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ACCESS-TOKEN" \
  -H "PayPal-Request-Id: REQUEST-ID" \
  -d '{
        "payment_source": {
          "card": {
            "number": "4111111111111111",
            "expiry": "2027-02",
            "name": "Firstname Lastname",
            "billing_address": {
              "address_line_1": "2211 N First Street",
              "address_line_2": "17.3.160",
              "admin_area_1": "CA",
              "admin_area_2": "San Jose",
              "postal_code": "95131",
              "country_code": "US"
            },
            "experience_context": {
              "brand_name": "YourBrandName",
              "locale": "en-US",
              "return_url": "https://example.com/returnUrl",
              "cancel_url": "https://example.com/cancelUrl"
            }
          }
        }
      }'
```

### Sample response for setup token with no verification

A successful request returns the following:

- An HTTP response code of `200` or `201`. Returns `200` for an idempotent request.
- The ID of the token in the `id` field.
- [HATEOAS links](/payments/save/api/vault-api-integration#cards-setup-token-response)

```bash theme={null}
{
  "id": "5C991763VB2781612",
  "customer": {
    "id": "customer_4029352050"
  },
  "status": "APPROVED",
  "payment_source": {
    "card": {
      "last_digits": "1111",
      "expiry": "2027-02",
      "name": "Firstname Lastname",
      "billing_address": {
        "address_line_1": "2211 N First Street",
        "address_line_2": "17.3.160",
        "admin_area_2": "San Jose",
        "admin_area_1": "CA",
        "postal_code": "95131",
        "country_code": "US"
      }
    }
  },
  "links": [{
      "href": "https://api-m.sandbox.paypal.com/v3/vault/setup-tokens/5C991763VB2781612",
      "rel": "self",
      "method": "GET",
      "encType": "application/json"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens",
      "rel": "confirm",
      "method": "POST",
      "encType": "application/json"
    }
  ]
}
```

## Smart authorization

Smart authorization runs a zero-value or minimal-value authorization to validate the card is real and active.

Some issuing banks or regions don't support zero-value authorization, so a minimal-value authorization is run. The seller must manually cancel minimal-value authorizations or the customer will have a small pending charge on their card.

### Sample request for setup token with smart authorization

1. Change `ACCESS-TOKEN` to your sandbox access token.
2. Change `REQUEST-ID` to a set of unique alphanumeric characters such as a time stamp.
3. Use the card as the payment source and complete the rest of the source object for your use case and business.
4. Pass the `verification_method` parameter with `SCA_WHEN_REQUIRED` to verify card data.
5. Update the `return_url` value with the URL where the payer is redirected after they approve the flow.
6. Update the `cancel_url` value with the URL where the payer is redirected after they cancel the flow.

Copy and modify the following code:

Endpoint: [Create a setup token](https://developer.paypal.com/docs/api/payment-tokens/v3/#setup-tokens_create)

```bash theme={null}
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens' \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ACCESS-TOKEN" \
  -H "PayPal-Request-Id: REQUEST-ID" \
  -d '{
        "payment_source": {
          "card": {
            "number": "4111111111111111",
            "expiry": "2027-02",
            "name": "Firstname Lastname",
            "billing_address": {
              "address_line_1": "2211 N First Street",
              "address_line_2": "17.3.160",
              "admin_area_1": "CA",
              "admin_area_2": "San Jose",
              "postal_code": "95131",
              "country_code": "US"
            },
            "experience_context": {
              "brand_name": "YourBrandName",
              "locale": "en-US",
              "return_url": "https://example.com/returnUrl",
              "cancel_url": "https://example.com/cancelUrl"
            }
          }
        }
      }'
```

### Sample response for setup token with smart authorization

A successful request returns the following:

- An HTTP response code of `200` or `201`. Returns `200` for an idempotent request.
- A status of `APPROVED`
- The ID of the token in the `id` field.
- [HATEOAS links](/payments/save/api/vault-api-integration#cards-setup-token-response)

```json theme={null}
{
  "id": "5C991763VB2781612",
  "status": "APPROVED",
  "payment_source": {
    "card": {
      "brand": "VISA",
      "last_digits": "1111",
      "verification_status": "VERIFIED",
      "verification": {
        "network_transaction_id": "20286098380002303",
        "time": "2020-10-07T22:44:41.000Z",
        "amount": {
          "value": "0.00",
          "currency_code": "USD"
        },
        "processor_response": {
          "avs_code": "M",
          "cvv_code": "P"
        }
      }
    }
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-token",
      "rel": "confirm",
      "method": "POST",
      "encType": "application/json"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v3/vault/setup-tokens/5C991763VB2781612",
      "rel": "self",
      "method": "GET",
      "encType": "application/json"
    }
  ]
}
```

## 3D Secure

Use 3D Secure authentication to reduce the likelihood of fraud and improve transaction performance with supported cards. In some countries, authorizing a card can trigger a 3D Secure contingency.

3D Secure verification may occur in PSD2 countries, including members of the EU. For 3D Secure verification, pass `SCA_ALWAYS` or `SCA_WHEN_REQUIRED` in the `payment_source.card.attributes.verification`.method field for the create order request. The API response returns the order status as `PAYER_ACTION_REQUIRED`.

### Sample request for setup token with 3D Secure

1. Change `ACCESS-TOKEN` to your sandbox access token.
2. Change `REQUEST-ID` to a set of unique alphanumeric characters such as a time stamp.
3. Use the card as the payment source and complete the rest of the source object for your use case and business.
4. Pass the `verification_method` parameter with `SCA_ALWAYS` to verify card data.
5. Update the `return_url` value with the URL where the payer is redirected after they approve the flow.
6. Update the `cancel_url` value with the URL where the payer is redirected after they cancel the flow.

Copy and modify the following code:

```bash theme={null}
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens'\
 -H "Content-Type: application/json"\
 -H "Authorization: Bearer ACCESS-TOKEN"\
 -H "PayPal-Request-Id: REQUEST-ID"\
 -d '{
     "payment_source": {
       "card": {
         "number": "4111111111111111",
         "expiry": "2027-02",
         "name": "Firstname Lastname",
         "billing_address": {
           "address_line_1": "2211 N First Street",
           "address_line_2": "17.3.160",
           "admin_area_1": "CA",
           "admin_area_2": "San Jose",
           "postal_code": "95131",
           "country_code": "US"
         },
         "verification_method": "SCA_WHEN_REQUIRED",
         "experience_context": {
           "brand_name": "YourBrandName",
           "locale": "en-US",
           "return_url": "https://example.com/returnUrl",
           "cancel_url": "https://example.com/cancelUrl"
         }
       }
     }
    }'
```

### Sample response for setup token with 3D Secure

A successful request returns the following:

- An HTTP response code of `200` or `201`. Returns `200` for an idempotent request.
- A status of `PAYER_ACTION_REQUIRED`
- [HATEOAS links](/payments/save/api/vault-api-integration#cards-setup-token-response)

```json theme={null}
{
  "id": "5C991763VB2781612",
  "customer": {
    "id": "customer_4029352050"
  },
  "status": "PAYER_ACTION_REQUIRED",
  "payment_source": {
    "card": {
      "last_digits": "1111",
      "brand": "VISA",
      "type": "CREDIT",
      "expiry": "2027-02"
    }
  },
  "links": [
    {
      "href": "https://paypal.com/webapps/helios?action=authenticate&validate_session_id=82cf4a87-5c40-0a27-1a09-4ffbb0d05fdc",
      "rel": "approve",
      "method": "GET",
      "encType": "application/json"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-token",
      "rel": "confirm",
      "method": "POST",
      "encType": "application/json"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v3/vault/setup-tokens/5C991763VB2771612",
      "rel": "self",
      "method": "GET",
      "encType": "application/json"
    }
  ]
}
```

### Convert approved setup token to payment token

After the payer completes verification, make a `POST` request on the [payment token endpoint](https://developer.paypal.com/docs/api/payment-tokens/v3/#create-a-payment-token) to convert the approved setup token to a payment token.

To retrieve 3D secure verification data associated with a setup token, make a `GET` request on the [setup token endpoint](https://developer.paypal.com/docs/api/payment-tokens/v3/#setup-token).

#### Sample request

```bash theme={null}
curl -v -k -X GET 'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens/5C991763VB2781612'\
  -H "Content-Type: application/json"\
  -H "Authorization: Bearer ACCESS-TOKEN"\
  -H "PayPal-Request-Id: REQUEST-ID"\
```

#### Sample response

A successful request returns the following:

- An HTTP response code of `200 OK`
- A status of `APPROVED`

| Parameter             | Description                                                                                                                                                                         |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `verification_method` | The verification method value from the request is included in the response.                                                                                                         |
| `verification_status` | If the card is authorized, the status is set to `VERIFIED`.                                                                                                                         |
| `authorization`       | Details from the authorization are returned in an `authorization` object. This includes the amount and currency requested, and the AVS and CVV results from the processor response. |

The issuing bank can still issue an authorization if a card fails the AVS and CVV checks. In this case, the setup token is created with an `APPROVED` status and the processor responses are returned to you. The `eci_flag` parameter indicates that 3D Secure was not completed.

You can choose whether to use a card that did not complete 3D Secure or failed AVS and CVV checks:

- To use the card, make a `POST` request on [add-payment-token](https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_create). Convert the approved setup token to a full payment token.
- To reject the card, don't add the payment token or convert it to a full payment token.

In the sandbox, create a setup token and a 3D Secure token. Validate a card with card data from [3D Secure test scenarios](https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/test/).

```json theme={null}
{
  "id": "5C991763VB2771612",
  "status": "APPROVED",
  "payment_source": {
    "card": {
      "brand": "VISA",
      "last_digits": "1111",
      "verification_status": "VERIFIED",
      "verification": {
        "network_transaction_id": "20286098380002303",
        "time": "2020-10-07T22:44:41.000Z",
        "amount": {
          "value": "0.00",
          "currency_code": "USD"
        },
        "processor_response": {
          "avs_code": "M",
          "cvv_code": "P"
        },
        "three_d_secure": {
          "type": "THREE_DS_AUTHENTICATION",
          "eci_flag": "FULLY_AUTHENTICATED_TRANSACTION",
          "card_brand": "VISA",
          "enrolled": "Y",
          "pares_status": "Y",
          "three_ds_version": "2",
          "authentication_type": "DYNAMIC",
          "three_ds_server_transaction_id": "3d-secure-txn-id"
        }
      }
    }
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-token",
      "rel": "confirm",
      "method": "POST",
      "encType": "application/json"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v3/vault/setup-tokens/5C991763VB2771612",
      "rel": "self",
      "method": "GET",
      "encType": "application/json"
    }
  ]
}
```

## Test AVS and CVV response codes

Generate AVS and CVV response codes when running tests in the PayPal sandbox.

Use [test card numbers](https://developer.paypal.com/tools/sandbox/card-testing/#link-teststaticcardnumbers).

### Generate AVS response

Set `address_line_1` to the following values to generate an AVS response.

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

### Generate CVV response

Set the CVV to the following values to generate a CVV response:

| CVV | CVV response | Description                                                        |
| --- | ------------ | ------------------------------------------------------------------ |
| 115 | M            | CVV2/CVC2/CID Match                                                |
| 116 | N            | CVV2/CVC2/CID No Match                                             |
| 120 | P            | Not Processed                                                      |
| 123 | S            | CVV2 should be on the card, but merchant indicated that it was not |
| 125 | U            | Unknown/Issuer does not participate                                |
| 130 | X            | Server provider did not respond (default)                          |
