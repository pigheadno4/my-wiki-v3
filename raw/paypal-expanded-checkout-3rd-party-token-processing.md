<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/3rd-party-token-processing/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Process payments using third-party network token processing
slug: /docs/checkout/advanced/3rd-party-token-processing/
createTime: '2025-03-25T16:30:09.790Z'
updateTime: '2025-05-30T11:53:59.736Z'
---


# Process payments using third-party network token processing

PayPal supports third-party network token processing for merchants and partners.



## Availability 
This integration is availablein the following countries:

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
- Hungary
- Ireland
- Italy
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
- Slovakia
- Slovenia
- Spain
- Sweden
- United Kingdom
- United States

For more information, contact [Sales](https://www.paypal.com/us/business/contact-sales) .



## Tokenization 
Tokenization keeps payment information private by turning card numbers into unique tokens, which are stored securely and used instead of the original card.

Tokenization creates a unique credential, or token, for a card that is different from its 15- or 16-digit primary account number. The merchant only sends the token, rather than the underlying account number. A network token only works for a specific card and merchant.

The benefits of using network tokens include:

- Improved authorization rates.
- Increased security by reducing opportunities for data theft and using cryptograms to protect credentials.
- Potentially reduced transaction-processing costs.
- Simplified payment processing.
- Helps maintain Payment Card Industry Data Security Standard compliance.

 

### Third-party network token
A third-party network token represents a payment method that is either:

- Saved in-house by the partner or merchant.
- Saved by an external Token Service Provider (TSP).

Third-party network token processing happens when PayPal processes a payment using a token that PayPal didn't create.



## How it works 
Integrate with third-party network token payments as follows:

- Save and tokenize a payer's payment method.
- Get a token number and expiration date to use for payments.
- Use this token when sending a payment through PayPal.
- PayPal processes the payment as a regular credit or debit card purchase.


**info**
**Note:** Third-party tokens aren't stored and can't be created, mapped, unmapped, or validated against their primary account number.



## Know before you code 

### PayPal Expanded Checkout
You'll need a PayPal Expanded Checkoutintegration.


### Third-party token integration liability
You acknowledge and agree that you are solely responsible for any third-party vaulting functionality (not provided by PayPal) that you use and PayPal will, under no circumstances, be responsible or liable for any damages, losses or costs whatsoever suffered or incurred by you as a result of using a third-party vaulting functionality on PayPal's platforms (including Products), services, or APIs.


**warning**
**Note:** Third-party network token integrations don't support reference or future transactions. Don't pass a reference transaction ID using the payment_source.token.id parameter.



## Using third-party network tokens with PayPal 
Review this section to learn how to integrate third-party network tokens in your PayPal integration.


### Sample third-party token processing request for direct merchants
This code sample shows a third-party network token in the body of a POST call to the [Create order](/docs/api/orders/v2/#orders_create) endpoint of the Orders v2 API. This request creates a new order and completes the payment in a single step by declaring the intent as CAPTURE .

The payment request includes the new network_token and stored_credential objects:


#### **`Sample third-party token processing request for direct merchants`**
```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H 'Content-Type: application/json' \
-H 'PayPal-Request-Id: REQUEST-ID' \
-H 'Authorization: Bearer ACCESS-TOKEN' \
-d '{
  "intent": "CAPTURE",
  "purchase_units": [
    {
      "reference_id": "REFID-000-1001",
      "amount": {
        "currency_code": "USD",
        "value": "100.00"
      }
    }
  ],
  "payment_source": {
    "card": {
      "name": "Firstname Lastname",
      "network_token": {
        "number": "4444444444444444",
        "expiry": "2030-11",
        "eci_flag": "NON_3D_SECURE_TRANSACTION",
        "token_requestor_id": "12324"
      },
      "stored_credential": {
        "payment_initiator": "MERCHANT",
        "payment_type": "UNSCHEDULED",
        "usage": "SUBSEQUENT",
        "previous_network_transaction_reference": {
          "id": "NETWORK-TRANSACTION-REFERENCE-ID",
          "network": "VISA"
        }
      }
    }
  }
}'
```
-  Lines 19-24: The payment_source.card.network_token object contains details about the third-party network token. PayPal passes this information to the issuer. See [network_token](/docs/api/orders/v2/#definition-network_token_request) for more details.

 
-  Line 22: Token service providers give each third-party network token a 2-digit Electronic Commerce Indicator (ECI) code. When you make a payment using a third-party network token, your integration needs to change the 2-digit ECI code to the corresponding string from the table below. Pass this value using the payment_source.card.network_token.eci_flag parameter. This value is required for customer-initiated payments and optional for merchant-initiated payments:

  | Numeric ECI code | String |
| --- | --- |
| 00 | MASTERCARD_NON_3D_SECURE_TRANSACTION |
| 07 | NON_3D_SECURE_TRANSACTION |

 
-  Lines 25-33: The payment_source.card.stored_credential object contains details about the type of card-on-file payment. See [stored_credential](/docs/api/orders/v2/#definition-card_stored_credential) for more details.

 


### Sample third-party token processing response for direct merchants
The HTTP 201 response includes the new bin_details and network_transaction_reference objects:


#### **`Sample third-party token processing response for direct merchants`**
```javascript
{
  "id": "ORDER-ID",
  "status": "COMPLETED",
  "payment_source": {
    "card": {
      "name": "Firstname Lastname",
      "last_digits": "4444",
      "expiry": "2030-11",
      "brand": "VISA",
      "available_networks": [
        "VISA"
      ],
      "type": "CREDIT",
      "bin_details": {
        "issuing_bank": "CREDIT UNION OF OHIO",
        "bin_country_code": "US",
        "products": [
          "CONSUMER"
        ]
      }
    }
  },
  "purchase_units": [
    {
      "reference_id": "REFID-000-1001",
      "payment_instruction": {
        ...
      },
      "shipping": {
        ...
      },
      "payments": {
        "captures": [
          {
            "id": "ORDER-ID",
            "status": "COMPLETED",
            "amount": {
              "currency_code": "USD",
              "value": "50.00"
            },
            "final_capture": true,
            "disbursement_mode": "DELAYED",
            "seller_protection": {
              "status": "NOT_ELIGIBLE"
            },
            "seller_receivable_breakdown": {
              ...
            },
            "invoice_id": "INVID-21-07-2023-05-56-55",
            "custom_id": "CUSTOMID-1001",
            "links": [
              ...
            ],
            "create_time": "2023-07-21T12:27:00Z",
            "update_time": "2023-07-21T12:27:00Z",
            "processor_response": {
              "avs_code": "Y",
              "cvv_code": "X",
              "response_code": "0000"
            },
            "network_transaction_reference": {
              "id": "NETWORK-TRANSACTION-REFERENCE-ID",
              "network": "VISA"
            }
          }
        ]
      }
    }
  ],
  "links": [
    ...
  ]
}
```
- Lines 14-18: The payment_source.card.bin_details object contains the bank identification number (BIN) information. See [bin_details](/docs/api/orders/v2/#definition-bin_details) for more details.
- Lines 59-62: The purchase_units.payments.captures.network_transaction_reference object includes the id and network name. See [network_transaction_reference](/docs/api/orders/v2/#definition-network_transaction_reference) for more details.



## Third-party network token processing test scenarios 
In the PayPal sandbox, you can use test cards to simulate third-party network token payment scenarios.

The test scenario on this page shows a successful payment capture with the following details:

- Merchant enrolled with Expanded Checkout.
- Customer-initiated payment.
- Externally provisioned token and cryptogram. Cryptograms are optional for MITs.

## Test cards
Use the following test cards as third-party network tokens. Pass the test card number in the body of the request using payment_source.card.network_token.number .


**info**
**Tip:** Enter a future expiration date when testing these card network tokens.


| **Card brand** | **Test card** | **Cryptogram** |
| --- | --- | --- |
| Visa | 4034772286582057 | "cryptogram":"ApIPtIgAMyrMgTx1RSnAMAACAAA=" |
| Visa | 4556871409493313 | "cryptogram":"ApIPtIgAMyrMgTx1RSnAMAACAAA=" |
| Mastercard | 5530238208956601 | "cryptogram":"ApIPtIgAMyrMgTx1RSnAMAACAAA=" |
| Mastercard | 5419720028804901 | "cryptogram":"ApIPtIgAMyrMgTx1RSnAMAACAAA=" |
| Amex | 379015087078375 | "cryptogram":"ApIPtIgAMyrMgTx1RSnAMAACAAA=" |
| Discover | 6011390662682995 | "cryptogram":"ApIPtIgAMyrMgTx1RSnAMAACAAA=" |


Test the third-party network payment token for each card brand by sending a POST call to the [Capture payment for order](/docs/api/orders/v2/#orders_capture) endpoint of the Orders v2 API with the following values:

- Pass the third-party network payment token for that card brand in the body of the request using the payment_source.card.network_token.number parameter.
- Enter a future expiration date using payment_source.card.network_token.expiry .
- Pass the cryptogram ApIPtIgAMyrMgTx1RSnAMAACAAA= using the payment_source.card.network_token.cryptogram parameter.
- Pass the Electronic Commerce Indicator (ECI) flag for the third-party network payment token using the payment_source.card.network_token.eci_flag parameter. For MasterCard, pass MASTERCARD_NON_3D_SECURE_TRANSACTION . For other cards, pass NON_3D_SECURE_TRANSACTION .


The transaction starts when you send a POST call to the [Create order](/docs/api/orders/v2/#orders_create) endpoint of the Orders v2 API.

A successful create order request returns the HTTP 201 Created status code and a JSON response body that includes by default a minimal response with the ID, status, and HATEOAS links.

Capture URL: [https://api-m.sandbox.paypal.com/v2/checkout/orders](https://api-m.sandbox.paypal.com/v2/checkout/orders)


#### **`Sample request`**
```javascript
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -H 'PayPal-Partner-Attribution-Id: BN-CODE' \
  -H 'PayPal-Auth-Assertion: AUTH-ASSERTION-JWT' \
  -H 'PayPal-Request-Id: REQUEST-ID' \
  -d '{
    "intent": "CAPTURE",
    "purchase_units": [
      {
        "reference_id": "reference_id_1_5.00",
        "payment_group_id": "1",
        "description": "Description of PU-1",
        "custom_id": "custom_id_1_5.00",
        "soft_descriptor": "soft_descr_1_5.00",
        "invoice_id": "invoice_id_create_order_1_1740637790",
        "amount": {
          "currency_code": "USD",
          "value": "5.00",
          "breakdown": {
            "item_total": {
              "currency_code": "USD",
              "value": "5.00"
            },
            "shipping": {
              "currency_code": "USD",
              "value": "0.00"
            },
            "handling": {
              "currency_code": "USD",
              "value": "0.00"
            },
            "tax_total": {
              "currency_code": "USD",
              "value": "0.00"
            },
            "gift_wrap": {
              "currency_code": "USD",
              "value": "0.00"
            },
            "shipping_discount": {
              "currency_code": "USD",
              "value": "0.00"
            }
          }
        },
        "items": [
          {
            "name": "Mug",
            "description": "Coffee Mug",
            "sku": "259483234812",
            "unit_amount": {
              "currency_code": "USD",
              "value": "5.00"
            },
            "tax": {
              "currency_code": "USD",
              "value": "0.00"
            },
            "quantity": "1",
            "category": "DIGITAL_GOODS"
          },
          {
            "name": "Mark-Up (0%)",
            "description": "Buyer Mark-Up Amount",
            "sku": "2594832348111",
            "unit_amount": {
              "currency_code": "USD",
              "value": "0.00"
            },
            "tax": {
              "currency_code": "USD",
              "value": "0.00"
            },
            "quantity": "1",
            "category": "DIGITAL_GOODS"
          }
        ],
        "payee": {
          "email_address": "payee@example.com",
          "display_data": {
            "business_email": "business@example.com",
            "brand_name": "PayPal Shop",
            "business_phone": {
              "country_code": "39",
              "national_number": "222-222-2222",
              "extension_number": "1"
            }
          }
        },
        "payment_instruction": {
          "disbursement_mode": "INSTANT",
          "platform_fees": [
            {
              "amount": {
                "currency_code": "USD",
                "value": "1.25"
              },
              "payee": {
                "email_address": "payee@example.com"
              }
            }
          ],
          "payee_pricing_tier_id": ""
        },
        "shipping": {
          "address": {
            "shipping_name": "Firstname Lastname",
            "phone": "555-555-5555",
            "address_line_1": "123 Main St.",
            "address_line_2": "#100",
            "admin_area_1": "CA",
            "admin_area_2": "Anytown",
            "postal_code": "12345",
            "country_code": "US",
            "address_details": {}
          },
          "method": "UPS"
        }
      }
    ],
    "payment_source": {
      "card": {
        "network_token": {
          "number": "4444444444444444",
          "expiry": "2029-01",
          "cryptogram": "ApIPtIgAMyrMgTx1RSnAMAACAAA=",
          "eci_flag": "NON_3D_SECURE_TRANSACTION",
          "token_requestor_id": "VK123PTR"
        }
      }
    },
    "application_context": {
      "locale": "en-US",
      "landing_page": "BILLING",
      "shipping_preference": "SET_PROVIDED_ADDRESS",
      "user_action": "PAY_NOW",
      "return_url": "https://example.com/returnUrl",
      "cancel_url": "https://example.com/cancelUrl"
    }
  }'
```


#### **`Sample response`**
```javascript
{
  "id": "ORDER-ID",
  "intent": "CAPTURE",
  "status": "CREATED",
  "payment_source": {
    "card": {
      "name": "Firstname Lastname",
      "last_digits": "4444",
      "expiry": "2029-01",
      "brand": "VISA",
      "available_networks": [
        "VISA"
      ],
      "type": "CREDIT",
      "bin_details": {
        "issuing_bank": "Services Credit Union",
        "bin_country_code": "US",
        "products": [
          "CONSUMER"
        ]
      }
    }
  },
  "purchase_units": [
    {
      "reference_id": "reference_id_1_5.00",
      "amount": {
        "currency_code": "USD",
        "value": "5.00",
        "breakdown": {
          "item_total": {
            "currency_code": "USD",
            "value": "5.00"
          },
          "shipping": {
            "currency_code": "USD",
            "value": "0.00"
          },
          "handling": {
            "currency_code": "USD",
            "value": "0.00"
          },
          "tax_total": {
            "currency_code": "USD",
            "value": "0.00"
          },
          "shipping_discount": {
            "currency_code": "USD",
            "value": "0.00"
          }
        }
      },
      "payee": {
        "email_address": "payee@example.com",
        "display_data": {
          "business_email": "business@example.com",
          "business_phone": {
            "country_code": "39",
            "national_number": "222-222-2222"
          },
          "brand_name": "PayPal Shop"
        }
      },
      "payment_instruction": {
        "platform_fees": [
          {
            "amount": {
              "currency_code": "USD",
              "value": "1.25"
            },
            "payee": {
              "email_address": "payee@example.com"
            }
          }
        ],
        "disbursement_mode": "INSTANT",
        "payee_pricing_tier_id": ""
      },
      "description": "Description of PU-1",
      "custom_id": "custom_id_1_5.00",
      "invoice_id": "invoice_id_create_order_1_1740637790",
      "soft_descriptor": "soft_descr_1_5.00",
      "items": [
        {
          "name": "Mug",
          "unit_amount": {
            "currency_code": "USD",
            "value": "5.00"
          },
          "tax": {
            "currency_code": "USD",
            "value": "0.00"
          },
          "quantity": "1",
          "description": "Coffee Mug",
          "sku": "259483234812",
          "category": "DIGITAL_GOODS"
        },
        {
          "name": "Mark-Up (0%)",
          "unit_amount": {
            "currency_code": "USD",
            "value": "0.00"
          },
          "tax": {
            "currency_code": "USD",
            "value": "0.00"
          },
          "quantity": "1",
          "description": "Buyer Mark-Up Amount",
          "sku": "2594832348111",
          "category": "DIGITAL_GOODS"
        }
      ],
      "shipping": {
        "method": "UPS",
        "address": {
          "address_line_1": "123 Main St.",
          "address_line_2": "#100",
          "admin_area_1": "CA",
          "admin_area_2": "Anytown",
          "postal_code": "12345",
          "country_code": "US"
        }
      }
    }
  ],
  "network_transaction_reference": {
    "id": "NETWORK-TRANSACTION-REFERENCE-ID",
    "network": "VISA"
  },
  "create_time": "2025-02-27T06:29:51Z",
  "links": [
    {
      "href": "https://api.sandbox.paypal.com/v2/checkout/orders/ORDER-ID",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://www.sandbox.paypal.com/checkoutnow?token=ORDER-ID",
      "rel": "approve",
      "method": "GET"
    },
    {
      "href": "https://api.sandbox.paypal.com/v2/checkout/orders/ORDER-ID",
      "rel": "update",
      "method": "PATCH"
    },
    {
      "href": "https://api.sandbox.paypal.com/v2/checkout/orders/ORDER-ID/capture",
      "rel": "capture",
      "method": "POST"
    }
  ]
}
```

The following code sample shows a capture order request using a third-party network token for a Visa card. The response includes a network_transaction_reference object showing the network transaction reference ID, and the card network, Visa. The Visa network doesn't return an expiration date .

Capture URL: [https://api-m.sandbox.paypal.com/v2/checkout/orders/ORDER-ID/capture](https://api-m.sandbox.paypal.com/v2/checkout/orders/9H765776SY493603U/capture)


#### **`Sample request`**
```javascript
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/{ORDER-ID}/capture \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -H 'PayPal-Partner-Attribution-Id: BN-CODE' \
  -H 'PayPal-Auth-Assertion: AUTH-ASSERTION-JWT' \
  -H 'PayPal-Request-Id: REQUEST-ID' \
  -d '{
    "payment_source": {
      "card": {
        "network_token": {
          "number": "4444444444444444",
          "expiry": "2029-01",
          "cryptogram": "ApIPtIgAMyrMgTx1RSnAMAACAAA=",
          "eci_flag": "NON_3D_SECURE_TRANSACTION",
          "token_requestor_id": "VK123PTR"
        }
      }
    }
  }'
```


#### **`Sample response`**
```javascript
{
  "id": "TOKEN-ID",
  "status": "COMPLETED",
  "payment_source": {
    "card": {
      "last_digits": "4444",
      "expiry": "2029-01",
      "brand": "VISA",
      "available_networks": [
        "VISA"
      ],
      "type": "CREDIT",
      "bin_details": {
        "issuing_bank": "TRELLANCE INC.",
        "bin_country_code": "US",
        "products": [
          "CONSUMER"
        ]
      }
    }
  },
  "purchase_units": [
    {
      "reference_id": "REFID-000-1001",
      "shipping": {
        "name": {
          "full_name": "Firstname Lastname"
        },
        "address": {
          "address_line_1": "123 Main St.",
          "address_line_2": "#100",
          "admin_area_1": "CA",
          "admin_area_2": "Anytown",
          "postal_code": "12345",
          "country_code": "US"
        }
      },
      "payments": {
        "captures": [
          {
            "id": "ORDER-ID",
            "status": "COMPLETED",
            "amount": {
              "currency_code": "USD",
              "value": "50.00"
            },
            "final_capture": true,
            "disbursement_mode": "INSTANT",
            "seller_protection": {
              "status": "NOT_ELIGIBLE"
            },
            "seller_receivable_breakdown": {
              "gross_amount": {
                "currency_code": "USD",
                "value": "50.00"
              },
              "paypal_fee": {
                "currency_code": "USD",
                "value": "1.74"
              },
              "net_amount": {
                "currency_code": "USD",
                "value": "48.26"
              }
            },
            "invoice_id": "INVID-13-05-2025-04-36-46",
            "custom_id": "CUSTOMID-1001",
            "links": [
              {
                "href": "https://api.sandbox.paypal.com/v2/payments/captures/ORDER-ID",
                "rel": "self",
                "method": "GET"
              },
              {
                "href": "https://api.sandbox.paypal.com/v2/payments/captures/ORDER-ID/refund",
                "rel": "refund",
                "method": "POST"
              },
              {
                "href": "https://api.sandbox.paypal.com/v2/checkout/orders/TOKEN-ID",
                "rel": "up",
                "method": "GET"
              }
            ],
            "create_time": "2025-05-13T11:07:39Z",
            "update_time": "2025-05-13T11:07:39Z",
            "network_transaction_reference": {
              "id": "NETWORK-TRANSACTION-REFERENCE-ID",
              "network": "VISA"
            },
            "processor_response": {
              "avs_code": "A",
              "cvv_code": "M",
              "response_code": "0000"
            }
          }
        ]
      }
    }
  ],
  "links": [
    {
      "href": "https://api.sandbox.paypal.com/v2/checkout/orders/TOKEN-ID",
      "rel": "self",
      "method": "GET"
    }
  ]
}
```
### Capture order response details
A successful response to a non-idempotent request returns the HTTP 201 Created status code with a JSON response body that shows captured payment details, including a network_transaction_reference object. If the order request was already processed, the endpoint returns the HTTP 200 OK status code to indicate an idempotent response.

The network_transaction_reference object passes the reference values used by the card network to identify this transaction. See [network_transaction_reference](/docs/api/orders/v2/#definition-network_transaction_reference) for details.
