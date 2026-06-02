<!-- Source URL: https://docs.paypal.ai/payments/pay-links-buttons-api/use-cases -->
<!-- Fetched: 2026-04-16 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Use cases

Explore key ways to apply the [Payment Links and Buttons API](/payments/pay-links-buttons-api) in your checkout and order flows. See how different configuration options map to common business scenarios so you can choose the pattern that best fits your integration.

The Payment Links and Buttons API currently supports payment links only and does not return button code.

| Use case                                                                                                                                                  | Endpoint                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [**Create payment links and buttons**](https://docs.paypal.ai/reference/api/rest/payment-resources/creates-a-payment-resource-for-a-single-item-purchase) | `POST /v1/checkout/payment-resources`        |
| [**List payment links**](https://docs.paypal.ai/reference/api/rest/payment-resources/list-payment-resources)                                              | `GET /v1/checkout/payment-resources`         |
| [**Get payment link details**](https://docs.paypal.ai/reference/api/rest/payment-resources/retrieve-a-payment-resource)                                   | `GET /v1/checkout/payment-resources/{id}`    |
| [**Update payment link**](https://docs.paypal.ai/reference/api/rest/payment-resources/replace-a-payment-resource)                                         | `PUT /v1/checkout/payment-resources/{id}`    |
| [**Delete payment link**](https://docs.paypal.ai/reference/api/rest/payment-resources/delete-a-payment-resource)                                          | `DELETE /v1/checkout/payment-resources/{id}` |

## Prerequisites

- Set up a [PayPal Business Account](https://www.paypal.com/business/open-business-account?_ga=2.49411041.673139926.1760916697-1259758161.1760473483).
- Navigate to the **Apps and Credentials** section on the [PayPal Developer Dashboard](https://www.paypal.com/signin?returnUri=https%3A%2F%2Fdeveloper.paypal.com%2Fdashboard%2F&intent=developer&ctxId=ul1761161497704) to ensure the **Payment Links and Buttons** option is checked.
- Implement OAuth 2.0 to obtain an access token for each API call.

## Create payment links and buttons (`POST`)

Create a buy now payment URL that links directly to a PayPal-hosted checkout experience. Use this endpoint to generate shareable payment URLs or various purchase flows.

Endpoint: `POST /v1/checkout/payment-resources`

### Request

The following sample request includes these key settings:

- Creates a reusable payment link for Premium Wireless Headphones with Noise Cancellation.
- Includes variant-specific pricing for four primary colors.
- Includes three variants where the color dimension is marked as primary and includes four options. The other two variants are `Warranty`, which has three options, and `Package Type`, which has two options. These variants do not affect pricing.
- Adds an 8.25% tax, applies a flat shipping rate, and requires customers to provide a shipping address.
- Provides customers with the option to add a gift message at checkout.
- Sets a maximum order quantity of 10 units.
- Redirects customers to a return URL after the transaction.

```json [expandable] theme={null}
{
  "integration_mode": "LINK",
  "type": "BUY_NOW",
  "reusable": "MULTIPLE",
  "return_url": "https://example-merchant.com/payment/return-success",
  "line_items": [
    {
      "name": "Premium Wireless Headphones with Noise Cancellation",
      "product_id": "PROD-WH-NC-2024-12345",
      "description": "Experience crystal-clear sound with our premium wireless headphones featuring active noise cancellation, 30-hour battery life",
      "taxes": [
        {
          "name": "State Sales Tax",
          "type": "PERCENTAGE",
          "value": "8.25"
        }
      ],
      "shipping": [
        {
          "type": "FLAT",
          "value": "12.50"
        }
      ],
      "collect_shipping_address": true,
      "customer_notes": [
        {
          "label": "Gift Message (Optional)",
          "required": false
        }
      ],
      "variants": {
        "dimensions": [
          {
            "name": "Color",
            "primary": true,
            "options": [
              {
                "label": "Midnight Black",
                "unit_amount": {
                  "currency_code": "USD",
                  "value": "149.99"
                }
              },
              {
                "label": "Silver Gray",
                "unit_amount": {
                  "currency_code": "USD",
                  "value": "149.99"
                }
              },
              {
                "label": "Rose Gold",
                "unit_amount": {
                  "currency_code": "USD",
                  "value": "169.99"
                }
              },
              {
                "label": "Navy Blue",
                "unit_amount": {
                  "currency_code": "USD",
                  "value": "159.99"
                }
              }
            ]
          },
          {
            "name": "Warranty",
            "primary": false,
            "options": [
              { "label": "Standard 1-Year" },
              { "label": "Extended 2-Year" },
              { "label": "Premium 3-Year" }
            ]
          },
          {
            "name": "Package Type",
            "primary": false,
            "options": [
              { "label": "Standard Box" },
              { "label": "Gift Wrapped" }
            ]
          }
        ]
      },
      "adjustable_quantity": {
        "maximum": 10
      }
    }
  ]
}
```

### Response

The following response contains a fixed-price payment resource link with product details and variants. The API returns HTTP status code `201 Created` and content type `application/json`.

```json [expandable] theme={null}
{
  "id": "PLB-8H2K9J3N5P7Q",
  "integration_mode": "LINK",
  "type": "BUY_NOW",
  "reusable": "MULTIPLE",
  "return_url": "https://example.com/return",
  "line_items": [
    {
      "name": "Premium Wireless Headphones",
      "product_id": "HEADPHONE-001",
      "description": "High-quality noise-canceling wireless headphones",
      "unit_amount": { "currency_code": "USD", "value": "199.99" },
      "taxes": [
        {
          "name": "Sales Tax",
          "amount": { "currency_code": "USD", "value": "16.00" }
        }
      ],
      "shipping": [
        {
          "name": "Standard Shipping",
          "amount": { "currency_code": "USD", "value": "5.99" }
        }
      ],
      "collect_shipping_address": true,
      "customer_notes": [{ "label": "Gift message", "required": false }],
      "variants": {
        "options": [{ "name": "Color", "values": ["Black", "Silver", "White"] }]
      },
      "adjustable_quantity": {
        "enabled": true,
        "min_quantity": 1,
        "max_quantity": 10
      }
    }
  ],
  "status": "ACTIVE",
  "create_time": "2025-10-10T12:30:45Z",
  "payment_link": "https://www.paypal.com/paymentpage/PLB-8H2K9J3N5P7Q"
}
```

### Additional use cases

The following use cases demonstrate how to create payment links for additional scenarios.

#### Create a payment link with a return URL

Create a payment link for a wireless mouse priced at \$39.99 USD. After completing payment, customers are redirected to the specified return URL, such as `https://merchant.example.com/thank-you`.

```bash [expandable] theme={null}
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v1/checkout/payment-resources' \
 -H 'Authorization: Bearer ACCESS-TOKEN' \
 -H 'Accept: application/json' \
 -H 'Content-Type: application/json' \
 -d '{
    "type": "BUY_NOW",
    "integration_mode": "LINK",
    "reusable": "MULTIPLE",
    "return_url": "https://merchant.example.com/thank-you",
    "line_items": [
        {
            "name": "Wireless Mouse",
            "unit_amount": {
                "currency_code": "USD",
                "value": "39.99"
            }
        }
    ]
}'
```

#### Create a payment link with variants

Create a payment link for a T-shirt priced at \$20.00 USD. The `Color` dimension is marked as primary and includes two options: `White` and `Black`. The `Size` dimension is secondary and includes `11oz` and `15oz` options. The base price of \$20.00 applies to all variant combinations.

```bash [expandable] theme={null}
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v1/checkout/payment-resources' \
 -H 'Authorization: Bearer ACCESS-TOKEN' \
 -H 'Accept: application/json' \
 -H 'Content-Type: application/json' \
 -d '{
    "type": "BUY_NOW",
    "integration_mode": "LINK",
    "reusable": "MULTIPLE",
    "line_items": [
        {
            "name": "T-Shirt",
            "unit_amount": {
                "currency_code": "USD",
                "value": "20.00"
            },
            "variants": {
                "dimensions": [
                    {
                        "name": "Color",
                        "primary": true,
                        "options": [
                            {
                                "label": "White"
                            },
                            {
                                "label": "Black"
                            }
                        ]
                    },
                    {
                        "name": "Size",
                        "primary": false,
                        "options": [
                            {
                                "label": "11oz"
                            },
                            {
                                "label": "15oz"
                            }
                        ]
                    }
                ]
            }
        }
    ]
}'
```

#### Create a payment link with variant-level pricing

Create a payment link for a T-shirt with variant-specific pricing. The `Color` dimension is marked as primary and includes two options: `White` priced at \$19.00 USD, and `Black` priced at \$20.00 USD. The `Size` dimension is secondary and includes `11oz` and `15oz` options, with no price difference. No base `unit_amount` shows up in the payload because each color variant specifies its own price.

```bash [expandable] theme={null}
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v1/checkout/payment-resources' \
 -H 'Authorization: Bearer ACCESS-TOKEN' \
 -H 'Accept: application/json' \
 -H 'Content-Type: application/json' \
 -d '{
    "integration_mode": "LINK",
    "type": "BUY_NOW",
    "reusable": "MULTIPLE",
    "line_items": [
        {
            "name": "T-Shirt",
            "variants": {
                "dimensions": [
                    {
                        "name": "Color",
                        "primary": true,
                        "options": [
                            {
                                "label": "White",
                                "unit_amount": {
                                    "currency_code": "USD",
                                    "value": "19.00"
                                }
                            },
                            {
                                "label": "Black",
                                "unit_amount": {
                                    "currency_code": "USD",
                                    "value": "20.00"
                                }
                            }
                        ]
                    },
                    {
                        "name": "Size",
                        "primary": false,
                        "options": [
                            {
                                "label": "11oz"
                            },
                            {
                                "label": "15oz"
                            }
                        ]
                    }
                ]
            }
        }
    ]
}'
```

#### Create a payment link with taxes and shipping

Create a payment link for a coffee mug priced at \$12.00 USD with tax and shipping calculations. The `taxes` and `shipping` arrays specify `type: PREFERENCE` and `value: PROFILE` to apply the merchant's preconfigured tax and shipping settings from their PayPal account. Merchants must configure these tax and shipping settings in their PayPal account for this feature to work.

```bash [expandable] theme={null}
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v1/checkout/payment-resources' \
 -H 'Authorization: Bearer ACCESS-TOKEN' \
 -H 'Accept: application/json' \
 -H 'Content-Type: application/json' \
 -d '{
    "integration_mode": "LINK",
    "type": "BUY_NOW",
    "reusable": "MULTIPLE",
    "return_url": "https://merchant.example.com/thank-you",
    "line_items": [
        {
            "name": "Coffee Mug",
            "unit_amount": {
                "currency_code": "USD",
                "value": "12.00"
            },
            "taxes": [
                {
                    "name": "Sales Tax",
                    "type": "PREFERENCE",
                    "value": "PROFILE"
                }
            ],
            "shipping": [
                {
                    "type": "PREFERENCE",
                    "value": "PROFILE"
                }
            ]
        }
    ]
}'
```

## List payment links (`GET`)

Retrieve a paginated list of all payment links created by the merchant. This endpoint supports filtering and pagination through query parameters, including filtering by link status and tags.

Endpoint: `GET /v1/checkout/payment-resources`

### Request

The following sample request includes these key details:

- Sends a `GET` request to list payment links you created.
- Uses the `page_size` parameter to limit results. For example, setting `page_size=2` returns two payment links per page.
- Includes an OAuth 2.0 Bearer token for authentication.
- Headers set to `Accept: application/json` and `Content-Type: application/json`.
- Uses a `page_token` from the response to retrieve additional pages.

```bash theme={null}
curl -v -k -X GET 'https://api-m.sandbox.paypal.com/v1/checkout/payment-resources' \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json'
```

### Response

The following sample response includes these key details:

- Returns a resources array with two payment links.
- The first payment link is for a `Wireless Mouse`, priced at \$29.99 USD. This link is active, set to `BUY_NOW`, and is reusable.
- The second payment link is for a Wireless Keyboard, priced at \$99.99 USD. It has the same status, type, and reusability settings as the first link.
- Each resource includes a shareable `payment_link` URL, metadata such as ID, product name, price, status, type, and creation timestamp, and a links array with HATEOAS actions to retrieve, update, edit, delete, or access the payment link.
- The response also includes a top-level links array for navigation, with a self link referencing the current request and a next link with a `page_token` for retrieving additional results.

```json [expandable] theme={null}
{
  "resources": [
    {
      "id": "PLB-X7MNK9P2QR8T",
      "integration_mode": "LINK",
      "create_time": "2025-11-29T13:13:25.832592Z",
      "status": "ACTIVE",
      "payment_link": "https://www.paypal.com/ncp/payment/PLB-X7MNK9P2QR8T",
      "type": "BUY_NOW",
      "reusable": "MULTIPLE",
      "line_items": [
        {
          "name": "Wireless Mouse",
          "unit_amount": {
            "currency_code": "USD",
            "value": "29.99"
          }
        }
      ],
      "links": [
        {
          "href": "https://api.paypal.com/v1/checkout/payment-resources/PLB-X7MNK9P2QR8T",
          "rel": "self",
          "method": "GET"
        },
        {
          "href": "https://api.paypal.com/v1/checkout/payment-resources/PLB-X7MNK9P2QR8T",
          "rel": "replace",
          "method": "PUT"
        },
        {
          "href": "https://api.paypal.com/v1/checkout/payment-resources/PLB-X7MNK9P2QR8T",
          "rel": "delete",
          "method": "DELETE"
        },
        {
          "href": "https://www.paypal.com/ncp/payment/PLB-X7MNK9P2QR8T",
          "rel": "payment_link",
          "method": "GET"
        }
      ]
    },
    {
      "id": "PLB-P2QR8TX7MNK9",
      "integration_mode": "LINK",
      "create_time": "2025-11-29T13:13:25.832592Z",
      "status": "ACTIVE",
      "payment_link": "https://www.paypal.com/ncp/payment/PLB-P2QR8TX7MNK9",
      "type": "BUY_NOW",
      "reusable": "MULTIPLE",
      "line_items": [
        {
          "name": "Wireless Keyboard",
          "unit_amount": {
            "currency_code": "USD",
            "value": "99.99"
          }
        }
      ],
      "links": [
        {
          "href": "https://api.paypal.com/v1/checkout/payment-resources/PLB-P2QR8TX7MNK9",
          "rel": "self",
          "method": "GET"
        },
        {
          "href": "https://api.paypal.com/v1/checkout/payment-resources/PLB-P2QR8TX7MNK9",
          "rel": "replace",
          "method": "PUT"
        },
        {
          "href": "https://api.paypal.com/v1/checkout/payment-resources/PLB-P2QR8TX7MNK9",
          "rel": "delete",
          "method": "DELETE"
        },
        {
          "href": "https://www.paypal.com/ncp/payment/PLB-P2QR8TX7MNK9",
          "rel": "payment_link",
          "method": "GET"
        }
      ]
    }
  ],
  "links": [
    {
      "href": "https://api.paypal.com/v1/checkout/payment-resources?page_size=2",
      "rel": "self"
    },
    {
      "href": "https://api.paypal.com/v1/checkout/payment-resources?page_token=eyJleGNsdXNpdmVfc3RhcnRfa2V5Ijp7ImlkIjoiUExCLVAyUVI4VFg3TU5LOSJ9LCJwYWdlX3NpemUiOjJ9",
      "rel": "next"
    }
  ]
}
```

## Get payment link details (`GET`)

Get the details of a specific payment link by its unique ID. This endpoint returns all available metadata, including payment status, links, reusable type, and line item details for the requested payment link.

Endpoint: `GET /v1/checkout/payment-resources/{id}`

### Request

The following sample request includes these key details:

- Includes the complete details for a specific payment link identified by the resource ID `PLB-X7MNK9P2QR8T` using a `GET` request.
- Uses an OAuth 2.0 Bearer token in the Authorization header to authenticate the request.
- Sets the `Accept` and `Content-Type` headers to `application/json` for proper formatting.

```bash theme={null}
curl -v -k -X GET 'https://api-m.sandbox.paypal.com/v1/checkout/payment-resources/PLB-X7MNK9P2QR8T' \
 -H 'Authorization: Bearer ACCESS-TOKEN' \
 -H 'Accept: application/json' \
 -H 'Content-Type: application/json'
```

### Response

The following response contains the complete details for a single fixed-price payment link. The API returns status code `200 OK` and content type `application/json`.

The following sample response includes these key details:

- Returns the full details of payment link `PLB-X7MNK9P2QR8T`.
- The payment link is active, set to `BUY_NOW`, and configured for multiple uses.
- Shows a product called Wireless Mouse, priced at \$29.99 USD
- The link was created on `2025-11-29T13:13:25.832592Z` with integration mode `LINK`.
- After payment, customers are redirected to `https://merchant.example.com/thank-you` that is specified by `return_url`.
- Includes a shareable payment link URL at `https://www.paypal.com/ncp/payment/PLB-X7MNK9P2QR8T`.
- Provides a links array with HATEOAS actions: retrieve the link details (`self`), update the link (`replace`), delete the link (`delete`), and access the customer-facing payment page (`payment_link`).

```json [expandable] theme={null}
{
  "id": "PLB-X7MNK9P2QR8T",
  "integration_mode": "LINK",
  "create_time": "2025-11-29T13:13:25.832592Z",
  "status": "ACTIVE",
  "payment_link": "https://www.paypal.com/ncp/payment/PLB-X7MNK9P2QR8T",
  "type": "BUY_NOW",
  "reusable": "MULTIPLE",
  "return_url": "https://merchant.example.com/thank-you",
  "line_items": [
    {
      "name": "Wireless Mouse",
      "unit_amount": {
        "currency_code": "USD",
        "value": "29.99"
      }
    }
  ],
  "links": [
    {
      "href": "https://api.paypal.com/v1/checkout/payment-resources/PLB-X7MNK9P2QR8T",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api.paypal.com/v1/checkout/payment-resources/PLB-X7MNK9P2QR8T",
      "rel": "replace",
      "method": "PUT"
    },
    {
      "href": "https://api.paypal.com/v1/checkout/payment-resources/PLB-X7MNK9P2QR8T",
      "rel": "delete",
      "method": "DELETE"
    },
    {
      "href": "https://www.paypal.com/ncp/payment/PLB-X7MNK9P2QR8T",
      "rel": "payment_link",
      "method": "GET"
    }
  ]
}
```

## Update payment link (`PUT`)

Update a specific payment link by its unique identifier. This endpoint helps you replace the product and checkout details for a fixed price payment link with new configuration data.

Endpoint: `PUT /v1/checkout/payment-resources/{id}`

### Request

The following sample request includes these key details:

- Sends a `PUT` request to update the payment link with ID `PLB-X7MNK9P2QR8T`.
- Uses an OAuth 2.0 Bearer token in the Authorization header for authentication.
- Includes the `Accept` and `Content-Type` headers set to `application/json`.
- Sends the updated link configuration in the request body, replacing the existing product information entirely.
- Maintains the same payment link ID and URL while applying the new settings.

> **Note:** The API currently only uses `PUT` calls instead of `PATCH` calls.

```bash [expandable] theme={null}
curl -v -k -X PUT 'https://api-m.sandbox.paypal.com/v1/checkout/payment-resources/PLB-X7MNK9P2QR8T' \
 -H 'Authorization: Bearer ACCESS-TOKEN' \
 -H 'Accept: application/json' \
 -H 'Content-Type: application/json' \
 -d '{
    "type": "BUY_NOW",
    "integration_mode": "LINK",
    "reusable": "MULTIPLE",
    "return_url": "https://merchant.example.com/thank-you",
    "line_items": [
        {
            "name": "Wireless Mouse",
            "unit_amount": {
                "currency_code": "USD",
                "value": "29.99"
            }
        }
    ]
}'
```

### Response

The following response contains the confirmation details of an updated payment link.

The API returns HTTP status `204 No Content` or, in some cases, a confirmation response body with the content type `application/json`.

The following sample response includes these key details:

- Confirms that the updated payment link `PLB-X7MNK9P2QR8T` has been successfully applied.
- Returns the payment link with `ACTIVE` status, maintaining the same ID and payment link URL.
- Preserves the original creation time.

```json [expandable] theme={null}
{
  "id": "PLB-X7MNK9P2QR8T",
  "integration_mode": "LINK",
  "create_time": "2025-11-29T13:13:25.832592Z",
  "status": "ACTIVE",
  "payment_link": "https://www.paypal.com/ncp/payment/PLB-X7MNK9P2QR8T",
  "type": "BUY_NOW",
  "reusable": "MULTIPLE",
  "return_url": "https://merchant.example.com/thank-you",
  "line_items": [
    {
      "name": "Wireless Mouse",
      "unit_amount": {
        "currency_code": "USD",
        "value": "29.99"
      }
    }
  ],
  "links": [
    {
      "href": "https://api.paypal.com/v1/checkout/payment-resources/PLB-X7MNK9P2QR8T",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api.paypal.com/v1/checkout/payment-resources/PLB-X7MNK9P2QR8T",
      "rel": "replace",
      "method": "PUT"
    },
    {
      "href": "https://api.paypal.com/v1/checkout/payment-resources/PLB-X7MNK9P2QR8T",
      "rel": "delete",
      "method": "DELETE"
    },
    {
      "href": "https://www.paypal.com/ncp/payment/PLB-X7MNK9P2QR8T",
      "rel": "payment_link",
      "method": "GET"
    }
  ]
}
```

## Delete payment link (`DELETE`)

Delete a specific payment link by its unique identifier. This endpoint permanently removes a payment link associated with the specified ID.

Endpoint: `DELETE /v1/checkout/payment-resources/{id}`

### Request

The following sample request includes these key details:

- Sends a `DELETE` request to permanently remove the payment link with ID `PLB-X7MNK9P2QR8T`.
- Uses an OAuth 2.0 Bearer token in the Authorization header for authentication.
- Includes the `Accept` and `Content-Type` headers set to `application/json`.

```bash theme={null}
curl -v -k -X DELETE 'https://api-m.sandbox.paypal.com/v1/checkout/payment-resources/PLB-X7MNK9P2QR8T' \
 -H 'Authorization: Bearer ACCESS-TOKEN' \
 -H 'Accept: application/json' \
 -H 'Content-Type: application/json'
```

### Response

The API returns HTTP status `204 No Content` with the content type `application/json`, indicating that the payment link was deleted. No response body is returned.

## Test

- Create a sandbox account through the PayPal Developer Portal.
- Use your sandbox environment for all development and testing. All endpoints are duplicated for the sandbox (`api-m.sandbox.paypal.com`) and live environments. See [Card testing](https://developer.paypal.com/tools/sandbox/card-testing/) to simulate transactions in the sandbox.
- To test live behavior, create a low-value payment link, complete a test purchase, and verify the transaction in the **Activity** section of your PayPal account. Refund the test transaction after verification.

## Common errors

For error handling and troubleshooting, see [Common errors](https://docs.paypal.ai/developer/how-to/api/troubleshooting/common-errors/overview).
