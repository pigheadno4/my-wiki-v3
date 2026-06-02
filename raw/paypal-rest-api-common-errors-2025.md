<!-- Source URL: https://docs.paypal.ai/developer/how-to/api/troubleshooting/common-errors/overview -->
<!-- Fetched: 2026-04-19 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Common errors overview

Troubleshooting is an important part of integrating with the PayPal Orders API. The following provides explanations and solutions to help you quickly find and fix issues in your integration.

| Issue                                     | Action                                                                                                                                                                                                                                                                                                                                                                   |
| :---------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AMOUNT_MISMATCH`                         | Ensure the total amount equals the sum of line items, taxes, and discounts. The API returns this error if the sale amounts are not reflected in the request.                                                                                                                                                                                                             |
| `CARD_EXPIRED`                            | Show the error to the payer and ask them to use a different card.                                                                                                                                                                                                                                                                                                        |
| `CANNOT_BE_NEGATIVE`                      | Enter a positive amount with no more than two decimal places.                                                                                                                                                                                                                                                                                                            |
| `CANNOT_BE_ZERO_OR_NEGATIVE`              | Enter a positive, non-zero amount with no more than two decimal places.                                                                                                                                                                                                                                                                                                  |
| `CURRENCY_NOT_SUPPORTED`                  | Use a PayPal-supported currency. Make sure the receiving PayPal account accepts the currency. For a list of supported currencies, see [Currency codes](https://developer.paypal.com/docs/api/rest/reference/currency-codes/currency-codes/).                                                                                                                             |
| `DECIMAL_PRECISION`                       | Round the amount to 2 decimal places and try again. If the issue persists, contact [PayPal support](https://www.paypal.com/us/cshelp/technical) and provide the `debug_id` from the API response.                                                                                                                                                                        |
| `DECIMALS_NOT_SUPPORTED`                  | Adjust the amount to match the number of decimal places the currency supports.                                                                                                                                                                                                                                                                                           |
| `DUPLICATE_INVOICE_ID`                    | Use a different `invoice_id`. If you must reuse the same `invoice_id` and the issue persists, contact [PayPal support](https://www.paypal.com/us/cshelp/technical).                                                                                                                                                                                                      |
| `INCOMPATIBLE_PARAMETER_VALUE`            | Make sure the parameters in the API request match the expected data types. For more information, see [Authentication](https://developer.paypal.com/api/rest/authentication/).                                                                                                                                                                                            |
| `INVALID_PARAMETER_SYNTAX`                | Make sure the API request JSON is correct and follows the PayPal API request format. If the issue persists, contact [PayPal support](https://www.paypal.com/us/cshelp/technical) and provide the `debug_id` from the API response.                                                                                                                                       |
| `INVALID_PARAMETER_VALUE`                 | Enter a valid parameter value.                                                                                                                                                                                                                                                                                                                                           |
| `INVALID_RESOURCE_ID`                     | Check the resource ID and try again. If the resource ID belongs to a different PayPal account, check the scopes and permissions for the receiving account.                                                                                                                                                                                                               |
| `INVALID_STRING_LENGTH`                   | Make sure text fields are not too long and include all required data. For string length requirements, see the [Orders API](https://developer.paypal.com/docs/api/orders/v2/#orders_create).                                                                                                                                                                              |
| `ITEM_TOTAL_MISMATCH`                     | Make sure the item totals match the quantity total.                                                                                                                                                                                                                                                                                                                      |
| `MAX_NUMBER_OF_PAYMENT_ATTEMPTS_EXCEEDED` | Ask the payer to use a different payment method.                                                                                                                                                                                                                                                                                                                         |
| `MISSING_REQUIRED_PARAMETER`              | Make sure the JSON follows the PayPal API request format and includes all [required parameters](https://developer.paypal.com/docs/api/orders/v2/#orders_create). If the issue persists, contact [PayPal support](https://www.paypal.com/us/cshelp/technical) and provide the `debug_id` from the API response.                                                           |
| `ORDER_ALREADY_AUTHORIZED`                | To proceed, [call capture](https://developer.paypal.com/docs/api/orders/v2/#orders_capture) because the funds are authorized. If the authorization is more than 3 days old, reauthorize the funds before capturing.                                                                                                                                                      |
| `ORDER_ALREADY_CAPTURED`                  | No action needed. Use a `GET` call on the order ID to get the capture ID or PayPal transaction ID. For multi-capture or split shipments, use `intent=AUTHORIZE`. See [Capture authorized payment](https://developer.paypal.com/docs/api/payments/v2/#authorizations_capture) for more information.                                                                       |
| `ORDER_NOT_APPROVED`                      | Ask the payer to complete PayPal checkout again to approve the order. Redirect them to the `'rel':'approve'` URL in the HATEOAS links from the create order call or provide a valid `payment_source` in the request.                                                                                                                                                     |
| `PAYEE_ACCOUNT_RESTRICTED`                | Contact PayPal customer support to lift restrictions on the receiving account. If you are a marketplace, ask the seller to resolve restrictions with PayPal.                                                                                                                                                                                                             |
| `PAYEE_NOT_CONSENTED`                     | Make sure the API caller has consent to collect partner fees for the payee. Add `PARTNER_FEE` to the capabilities during [signup](https://developer.paypal.com/docs/multiparty/seller-onboarding/before-payment/#generate-a-signup-link). If `PARTNER_FEE` is already added or the issue persists, contact [PayPal support](https://www.paypal.com/us/cshelp/technical). |
| `PAYEE_NOT_ENABLED_FOR_CARD_PROCESSING`   | Contact [PayPal support](https://www.paypal.com/us/cshelp/technical) to check the merchant or payee account configuration.                                                                                                                                                                                                                                               |
| `PAYER_ACTION_REQUIRED`                   | Redirect the payer to the `'rel':'payer-action'` HATEOAS link before authorizing or capturing the order. Some payment methods require a webhook subscription to notify you of background payer actions before capture succeeds.                                                                                                                                          |
| `PERMISSION_DENIED`                       | Make sure you have the correct permissions and scopes for the resource. If the resource ID belongs to another account, grant the necessary permissions.                                                                                                                                                                                                                  |
| `POSTAL_CODE_REQUIRED`                    | Add a postal code to the request and try again.                                                                                                                                                                                                                                                                                                                          |
| `REDIRECT_PAYER_FOR_ALTERNATE_FUNDING`    | Redirect the payer to choose a different payment method. In PayPal, the payer can add a new payment method to their wallet or use a different card.                                                                                                                                                                                                                      |
| `REFERENCED_CARD_EXPIRED`                 | Ask the payer to update their card information. Otherwise, future attempts will fail.                                                                                                                                                                                                                                                                                    |
| `SHIPPING_ADDRESS_INVALID`                | Fix the shipping address and try again. If using saved payment details, ask the payer for the correct shipping address.                                                                                                                                                                                                                                                  |
| `TOKEN_ID_NOT_FOUND`                      | Validate the payment token. If your PayPal account is making API calls for another account, make sure the recipient account grants the necessary permissions.                                                                                                                                                                                                            |
| `UNPROCESSABLE_ENTITY`                    | Contact [PayPal support](https://www.paypal.com/us/cshelp/technical) with the `debug_id` or `correlation_id` from the response header. For legacy integrations, check the body or response parameters.                                                                                                                                                                   |
| `VALIDATION_ERROR`                        | Tell the payer the card number is incorrect and ask them to enter the correct number.                                                                                                                                                                                                                                                                                    |

## HTTP status codes and error messages

The following table lists the most common HTTP status codes and error messages returned by the [Orders v2 API](https://developer.paypal.com/docs/api/orders/v2/#errors).

| HTTP status code            | Error message                                                                                        | Error code               |
| :-------------------------- | :--------------------------------------------------------------------------------------------------- | :----------------------- |
| `400 Bad Request`           | The request has the wrong format.                                                                    | `INVALID_REQUEST`        |
| `401 Unauthorized`          | Authentication failed because the authorization header is missing, or the credentials are not valid. | `AUTHENTICATION_FAILURE` |
| `403 Forbidden`             | Authorization failed because of lack of permissions.                                                 | `NOT_AUTHORIZED`         |
| `404 Not Found`             | The specified resource does not exist.                                                               | `RESOURCE_NOT_FOUND`     |
| `422 Unprocessable Entity`  | The requested action could not be performed, won't work, or failed business rules.                   | `UNPROCESSABLE_ENTITY`   |
| `500 Internal Server Error` | An internal server error occurred.                                                                   | `INTERNAL_SERVER_ERROR`  |
| `503 Service Unavailable`   | The service is unavailable.                                                                          | `SERVICE_UNAVAILABLE`    |

## Error samples

The following examples show common error scenarios for the Orders v2 API. Each sample includes a request and the corresponding error response.

### Internal server error (500)

The Orders v2 API returns a `500` status code when the server encounters an unexpected condition. The following sample shows a response when the server has an underlying issue or does not handle an internal exception.

#### Create order request

```bash theme={null}
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/ \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer ACCESS_TOKEN' \
-d '{
    "intent": "CAPTURE",
    "purchase_units": [
        {
            "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f7b",
            "amount": {
                "currency_code": "USD",
                "value": "10.00"
            }
        }
    ],
    "payment_source": {
        "paypal": {
            "address": {
                "address_line_1": "2211 N First Street",
                "address_line_2": "17.3.160",
                "admin_area_1": "CA",
                "admin_area_2": "San Jose",
                "postal_code": "95131",
                "country_code": "US"
            },
            "email_address": "johndoe@paypal.com",
            "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED",
            "experience_context": {
                "return_url": "https://example.com/returnUrl",
                "cancel_url": "https://example.com/cancelUrl"
            }
        }
    }
}'
```

#### Error response

```json theme={null}
{
  "name": "INTERNAL_SERVER_ERROR",
  "message": "An internal server error has occurred.",
  "debug_id": "90957fca61718",
  "links": [
    {
      "href": "https://developer.paypal.com/api/orders/v2/#error-INTERNAL_SERVER_ERROR",
      "rel": "information_link",
      "method": "GET"
    }
  ]
}
```

### Unprocessable entity error (422)

The Orders v2 API returns a `422` status code when an order fails business validation. For example, this can happen if the payer uses an expired payment card.

The following sample shows a create order request with an expired card and the resulting error response.

#### Create order request

```bash theme={null}
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/ \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer ACCESS_TOKEN' \
-d '{
    "intent": "AUTHORIZE",
    "purchase_units": [
        {
            "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
            "amount": {
                "currency_code": "USD",
                "value": "100.00"
            }
        }
    ],
    "payment_source": {
        "card": {
            "number": "4111111111111111",
            "expiry": "2010-02",
            "name": "John Doe",
            "billing_address": {
                "address_line_1": "2211 N First Street",
                "address_line_2": "17.3.160",
                "admin_area_1": "CA",
                "admin_area_2": "San Jose",
                "postal_code": "95131",
                "country_code": "US"
            },
            "stored_credential": {
                "payment_initiator": "MERCHANT",
                "payment_type": "ONE_TIME",
                "usage": "SUBSEQUENT"
            }
        }
    }
}'
```

#### Error response

```json theme={null}
{
  "name": "UNPROCESSABLE_ENTITY",
  "details": [
    {
      "field": "/payment_source/card/expiry",
      "location": "body",
      "issue": "CARD_EXPIRED",
      "description": "The card is expired."
    }
  ],
  "message": "The requested action could not be performed, semantically incorrect, or failed business validation.",
  "debug_id": "866780170332c",
  "links": [
    {
      "href": "https://developer.paypal.com/docs/api/orders/v2/#error-CARD_EXPIRED",
      "rel": "information_link",
      "method": "GET"
    }
  ]
}
```

### Bad request (400)

The Orders v2 API returns a `400` status code when a request includes an incorrect or unsupported value. The following sample shows a create order request with an invalid `usage_pattern` and the resulting error response.

#### Create order request

```bash theme={null}
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/ \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer ACCESS_TOKEN' \
-d '{
    "intent": "CAPTURE",
    "purchase_units": [
        {
            "reference_id": "PUHF",
            "amount": {
                "currency_code": "USD",
                "value": "10.00"
            }
        }
    ],
    "payment_source": {
        "paypal": {
            "attributes": {
                "customer": {
                    "id": "jd120252fg4dm"
                },
                "vault": {
                    "confirm_payment_token": "ON_ORDER_COMPLETION",
                    "usage_type": "MERCHANT",
                    "usage_pattern": "IMM3DI4T3"
                }
            }
        }
    }
}'
```

#### Error response

```json theme={null}
{
  "name": "INVALID_REQUEST",
  "message": "Request is not well-formed, syntactically incorrect, or violates schema.",
  "debug_id": "10398537340c8",
  "details": [
    {
      "field": "/payment_source/paypal/attributes/vault/usage_pattern",
      "value": "IMM3DI4T3",
      "location": "body",
      "issue": "INVALID_PARAMETER_VALUE",
      "description": "A parameter value is not valid."
    }
  ],
  "links": [
    {
      "href": "https://developer.paypal.com/docs/api/orders/v2/#error-INVALID_PARAMETER_VALUE",
      "rel": "information_link"
    }
  ]
}
```

### Forbidden (403)

The Orders v2 API returns a `403` status code when the API caller or payee does not have the required permissions for the request. The following sample shows a create order request that sets `items.category` to `DONATION` without the necessary permissions.

#### Create order request

```bash theme={null}
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/ \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer ACCESS_TOKEN' \
-d '{
    "intent": "CAPTURE",
    "purchase_units": [
        {
            "amount": {
                "currency_code": "USD",
                "value": "5.00",
                "breakdown": {
                    "item_total": {
                        "currency_code": "USD",
                        "value": "5.00"
                    }
                }
            },
            "items": [
                {
                    "name": "Donation to WWF",
                    "unit_amount": {
                        "currency_code": "USD",
                        "value": "5.00"
                    },
                    "quantity": "1",
                    "category": "DONATION"
                }
            ]
        }
    ]
}'
```

#### Error response

```json theme={null}
{
  "name": "NOT_AUTHORIZED",
  "details": [
    {
      "issue": "PERMISSION_DENIED_FOR_DONATION_ITEMS",
      "description": "The API Caller or Payee have not been granted appropriate permissions to send 'items.category' as 'DONATION'. Please speak to your account manager if you want to process these type of items."
    }
  ],
  "message": "Authorization failed due to insufficient permissions.",
  "debug_id": "90957fca61718",
  "links": [
    {
      "href": "https://developer.paypal.com/api/orders/v2/#error-PERMISSION_DENIED_FOR_DONATION_ITEMS",
      "rel": "information_link",
      "method": "GET"
    }
  ]
}
```
