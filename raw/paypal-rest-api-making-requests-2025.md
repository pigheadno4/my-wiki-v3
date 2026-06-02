<!-- Source URL: https://docs.paypal.ai/developer/how-to/api/make-api-requests -->
<!-- Fetched: 2026-04-19 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Making PayPal REST API requests

Build proper API requests with the correct headers and parameters to ensure successful communication with PayPal's REST APIs.

PayPal REST APIs authenticate with OAuth 2.0 access tokens, and return HTTP response codes with JSON-encoded responses.

> **Important:** Before making REST API calls, you'll need to [get credentials](developer/how-to/apps-scopes-credentials).

## Base URLs

All PayPal REST API requests target one of two base URLs:

- Sandbox for testing: `https://api-m.sandbox.paypal.com`
- Live for production: `https://api-m.paypal.com`

## 1st-party and 3rd-party calls

When you make REST API calls to PayPal, you can make first-party or third-party calls.

- **First-party calls:** API calls made to PayPal on behalf of your business. This method is also called a direct merchant integration.
- **Third-party calls:** API calls made to PayPal on behalf of another merchant. This is common when building marketplaces, platforms, or large enterprise solutions. This method is also called a multiparty or partner integration. Third-party calls require additional HTTP headers:
  - [`PayPal-Auth-Assertion`](#paypal-auth-assertion): Identifies the merchant you're making a call for.
  - [`PayPal-Partner-Attribution-Id`](#paypal-partner-attribution-id): Identifies your platform to PayPal.

## Important HTTP headers

The following is a list of all PayPal-specific HTTP request headers.

### PayPal-Auth-Assertion

> **Optional:** For platforms and marketplaces only.

This header is for platforms, marketplaces, large companies, and service providers that handle payments for more than one merchant. Examples include Square, eBay, Shopify, and other payment processors.

#### Purpose

Generating and storing separate access tokens for each merchant can be complex and costly. You can use the `PayPal-Auth-Assertion` header as one set of platform credentials for all merchants.

The `PayPal-Auth-Assertion` header is a <a href="https://tools.ietf.org/html/rfc7519">JSON Web Token (JWT)</a> that identifies which merchant each API call is for. This header requires explicit consent from each merchant you represent.

#### Build the JWT

PayPal recommends using an unsigned JWT, because the information passed with the JWT is not sensitive. Build the JWT with 3 parts:

- **Header:** For an unsigned JWT, set algorithm to `"alg": "none"`.
- **Payload:** Include the following fields:
  - `iss`: The platform's `client_id` (issuer).
  - `payer_id`: The specific merchant's PayPal payer ID.
- **Signature:** Use an empty string `""` for unsigned JWTs. If you prefer a signed JWT for security reasons, you can sign it with your secret from your API credentials.

Base64 encode each part separately, then concatenate with periods:

```
[encoded_header].[encoded_payload].[encoded_signature]
```

Example HTTP header:

```http theme={null}
PayPal-Auth-Assertion: eyJhbGciOiJub25lIn0.eyJpc3MiOiJZT1VSX1BMQVRGT1JNX0NMSUVOVF9JRCIsInBheWVyX2lkIjoiTUVSQ0hBTlRfUEFZRVJfSUQifQ.
```

Include the resulting JWT string in the `PayPal-Auth-Assertion` header when making API calls on behalf of that merchant.

```json theme={null}
{
  "iss": "your_platform_client_id",
  "payer_id": "merchant_payer_id_here"
}
```

### PayPal-Partner-Attribution-Id

> **Required:** For platforms and marketplaces only.

This header does two things:

- Identifies your platform to PayPal.
- Tracks all transactions associated with your platform.

The header value is your unique Build Notation (BN) code. Take the following steps to find your BN code:

1. From your developer dashboard, select **Apps & Credentials**.
2. Select the app you're using.
3. Under **App Settings**, scroll to **Reports**.
4. Your BN code appears on the last line of the Reports section.

### PayPal-Mock-Response

> **Optional.**

Use this header to simulate errors by passing an error code through the `mock_application_codes` parameter. For example, `"mock_application_codes": "DUPLICATE_INVOICE_ID"` to simulate two invoices sent with the same ID:

```bash theme={null}
curl -X POST \
https://api-m.sandbox.paypal.com/v2/checkout/orders/YOUR-ORDER-ID/capture \
  -H 'Authorization: Bearer YOUR-ACCESS-TOKEN' \
  -H 'Content-Type: application/json' \
  -H 'PayPal-Mock-Response: {"mock_application_codes": "DUPLICATE_INVOICE_ID"}'
```

For more information, see:

- [Payment API error messages](https://developer.paypal.com/docs/api/payments/v2/#errors)
- [Orders API error messages](https://developer.paypal.com/api/rest/reference/orders/v2/errors/)
- [Simulate negative responses with request headers](https://developer.paypal.com/tools/sandbox/negative-testing/request-headers/#test-api-error-handling-routines)

### PayPal-Request-Id

> **Important:** Recommended for all `POST` and `PUT` calls.

The `PayPal-Request-Id` contains a unique user-generated ID that prevents duplicate transactions. PayPal recommends including this header in any API call that creates or modifies data.

PayPal uses the `PayPal-Request-Id` to enforce **idempotency**. Idempotency means you can retry an API call multiple times without duplicating actions. For example, if a user presses a buy button multiple times, they aren't charged for each button press.

With this header, you can retry calls knowing that PayPal won't process the same action for as long as the server stores the ID. PayPal stores the ID for up to 45 days. If you retry a call with the same `PayPal-Request-Id`, PayPal recognizes it as a duplicate and returns the result of the original call.

```bash theme={null}
curl -v -X POST https://api-m.sandbox.paypal.com/v2/payments/authorizations/YOUR-ORDER-ID/capture \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR-ACCESS-TOKEN" \
  -H "PayPal-Request-Id: 123e4567-e89b-12d3-a456-426655440010" \
  -d '{
    "amount": {
      "value": "10.99",
      "currency_code": "USD"
    },
    "invoice_id": "INVOICE-123",
    "final_capture": true
    }'
```

## Common authentication errors

When using PayPal HTTP headers, you might encounter these issues:

- **401 Unauthorized**: Check that your platform credentials are valid and that you have permission to act on behalf of the merchant.
- **400 Bad Request**: Verify the JWT format is correct and all required fields are present.
- **403 Forbidden**: Ensure the merchant has granted your platform appropriate permissions.

For detailed error troubleshooting, check the response body. Find an error code, message, and debug ID to reference when contacting PayPal support. You can also refer to our [common errors](/developer/how-to/api/troubleshooting/common-errors/).

## Query PayPal REST APIs

When making a REST API request to PayPal, append query parameters to the endpoint URL using the following format:

```http theme={null}
https://api-m.sandbox.paypal.com/{resource}?parameter1=value1&parameter2=value2
```

- Separate each query parameter with an ampersand `&`.
- Introduce the first query parameter with a question mark `?`.
- URL-encode parameter names and values if they contain special characters.

### Example: list invoices

This example returns details for four invoices, starting from the third invoice, and includes the total invoice count.

```bash theme={null}
curl -v -X GET https://api-m.sandbox.paypal.com/v1/invoicing/invoices?page=3&page_size=4&total_count_required=true\
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS-TOKEN"
```

- `page=3` requests the third page of results.
- `page_size=4` limits the response to 4 items per page.
- `total_count_required=true` asks PayPal to include the total count of items in the response.

### Query parameters

> **Note:** Not all pagination parameters are available for all APIs.

| Parameter              | Type    | Description                                                                                                                                                                                                                                         |
| ---------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `count`                | integer | The number of items to list in the response.                                                                                                                                                                                                        |
| `end_time`             | integer | The end date and time for the range to show in the response, in <a href="https://tools.ietf.org/html/rfc3339#section-5.6" target="_blank">Internet date and time format</a>. For example, `end_time=2025-03-07T11:00:00Z`.                          |
| `page`                 | integer | The page number indicating which set of items will be returned in the response. For example, the combination of `page=1` and `page_size=20` returns the first 20 items. The combination of `page=2` and `page_size=20` returns items 21 through 40. |
| `page_size`            | integer | The number of items to return in the response.                                                                                                                                                                                                      |
| `total_count_required` | boolean | Indicates whether to show the total count in the response.                                                                                                                                                                                          |
| `sort_by`              | string  | Sorts the payments in the response by a specified value, such as the create time or update time.                                                                                                                                                    |
| `sort_order`           | string  | Sorts the items in the response in ascending or descending order.                                                                                                                                                                                   |
| `start_id`             | string  | The ID of the starting resource in the response. When results are paged, you can use the `next_id` value as the `start_id` to continue with the next set of results.                                                                                |
| `start_index`          | integer | The `start_index` parameter lets you specify the position in the list where results should begin. For example, setting `start_index=2` skips the first item and shows results from the second item onward.                                          |
| `start_time`           | string  | The start date and time for the range to show in the response, in Internet date and time format. For example, `start_time=2025-03-06T11:00:00Z`.                                                                                                    |

## Example request: create invoice

PayPal's REST APIs support standard HTTP methods - `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.

> **Important**: Include a `PayPal-Request-Id` header in all `POST` and `PUT` requests to prevent duplicate actions.

The following request creates an invoice as a direct merchant:

- From sender David Larusso, including address, email address, and phone number.
- To recipient Stephanie Meyers, including address, email address, and phone number.
- For one \$50 yoga mat including sales tax.
- For one \$10 t-shirt including sales tax.
- With \$20 minimum partial payments enabled.
- With an optional tip.
- With $10 packing charges and $10 shipping charges, including sales tax.
- With a 5% invoice discount.

```bash theme={null}
curl -v -X POST 'https://api-m.sandbox.paypal.com/v2/invoicing/invoices' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: Bearer YOUR-ACCESS-TOKEN' \
 -H 'PayPal-Request-Id: YOUR-REQUEST-ID' \
 -d '{
  "detail": {
    "invoice_number": "123",
    "reference": "deal-ref",
    "invoice_date": "2028-11-22",
    "currency_code": "USD",
    "note": "Thank you for your business.",
    "term": "No refunds after 30 days.",
    "memo": "This is a long contract",
    "payment_term": {
      "term_type": "NET_10",
      "due_date": "2028-11-22"
    }
  },
  "invoicer": {
    "name": {
      "given_name": "David",
      "surname": "Larusso"
    },
    "address": {
      "address_line_1": "1234 First Street",
      "address_line_2": "337673 Hillside Court",
      "admin_area_2": "Anytown",
      "admin_area_1": "CA",
      "postal_code": "98765",
      "country_code": "US"
    },
    "email_address": "merchant@example.com",
    "phones": [
      {
        "country_code": "001",
        "national_number": "4085551234",
        "phone_type": "MOBILE"
      }
    ],
    "website": "www.test.com",
    "tax_id": "ABcNkWSfb5ICTt73nD3QON1fnnpgNKBy-Jb5SeuGj185MNNw6g",
    "logo_url": "https://example.com/logo.PNG",
    "additional_notes": "2-4"
  },
  "primary_recipients": [
    {
      "billing_info": {
        "name": {
          "given_name": "Stephanie",
          "surname": "Meyers"
        },
        "address": {
          "address_line_1": "1234 Main Street",
          "admin_area_2": "Anytown",
          "admin_area_1": "CA",
          "postal_code": "98765",
          "country_code": "US"
        },
        "email_address": "buyer@example.com",
        "phones": [
          {
            "country_code": "001",
            "national_number": "4884551234",
            "phone_type": "HOME"
          }
        ]
      },
      "shipping_info": {
        "name": {
          "given_name": "Earl",
          "surname": "Gray"
        },
        "address": {
          "address_line_1": "1234 Main Street",
          "admin_area_2": "Anytown",
          "admin_area_1": "CA",
          "postal_code": "98765",
          "country_code": "US"
        }
      }
    }
  ],
  "items": [
    {
      "name": "Yoga mat",
      "description": "Elastic mat to practice yoga.",
      "quantity": "1",
      "unit_amount": {
        "currency_code": "USD",
        "value": "50.00"
      },
      "tax": {
        "name": "Sales Tax",
        "percent": "7.25"
      },
      "discount": {
        "percent": "5"
      },
      "unit_of_measure": "QUANTITY"
    },
    {
      "name": "Yoga t-shirt",
      "quantity": "1",
      "unit_amount": {
        "currency_code": "USD",
        "value": "10.00"
      },
      "tax": {
        "name": "Sales Tax",
        "percent": "7.25"
      },
      "unit_of_measure": "QUANTITY"
    }
  ]
}'
```
