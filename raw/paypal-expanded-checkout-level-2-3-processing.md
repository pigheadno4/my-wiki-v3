<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/processing/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Level 2/Level 3 processing
slug: /docs/checkout/advanced/customize/processing/
createTime: '2024-05-11T00:22:52.310Z'
updateTime: '2026-01-07T06:51:06.922Z'
---


# Level 2/Level 3 processing

Card payment processing has three levels: Level 1, Level 2, and Level 3. The information required to complete the payment as a Level 1, Level 2, or Level 3 eligible transaction differs between the levels. Level 1 requires less information andgenerally incurs higher interchange fees than the transactions processed with Level 2 and Level 3 data. Most businesses can operate at Level 1.

However, IC++ merchants can benefit from reduced interchange fees when processing corporate and purchase credit cards by providing additional transaction information called Level 2 and Level 3 data.



## Availability 
**Feature availability:** US only.

**Applicable currency:** US Domestic ( USD )



## Eligibility 
#### Country
Available for merchants in the United States for USD transactions.

#### Card payments that qualify for level 2/level 3 processing
Corporate and purchase credit cards are eligible for Levels 2 and 3 processing if the required information is provided. Consumer cards are only eligible for Level 1 processing.

Level 2 and Level 3 cost optimization benefits don't apply to debit cards.

#### Card networks that support level 2/level 3 processing
Visa and Mastercard offer Levels 2 and 3 processing. American Express offers Level 2, and Discover offers only Level 1 processing.


### Qualifying information for level 2/level 3 payment processing
Merchants must send the following information to qualify for Levels 2 and 3 processing. However, the card network and cardholder issuing bank ultimately determine whether a transaction qualifies for Level 2 or Level 3 processing:

 

#### Level 2 data
- Card number, expiration, billing address, shipping address, and invoice number.
- Customer Code or PO number: A unique reference ID for the order.
- Tax amount: An amount must be submitted separately from the transaction amount.

 

#### Level 3 data
- Level 2 data
- Unit amount or unit price.
- Unit of measure.
- Freight or shipping amount: The shipping and handling charges.
- Duty amount: The charges for any import or export duties.
- Discount amount.
- Item commodity code.
- Item description.
- Item product code.
- Item quantity.
- Unit tax amount.
- Unit discount amount.
- Ship-from ZIP code.


**Note:** The partner, merchant, or other initiating party must provide the Level 2 and 3 payment details when using the Orders v2 API to start a payment.


This code sample shows Level 2 and 3 data in the body of a POST call to the Create order endpoint of the Orders v2 API. This request creates a new order and completes the payment in a single step by declaring the intent as CAPTURE.


#### Create Order request
```bash
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer ACCESS-TOKEN' \
-H 'PayPal-Partner-Attribution-Id: BN-CODE' \
-H 'PayPal-Auth-Assertion: AUTH-ASSERTION-JWT' \
-H 'PayPal-Request-Id: REQUEST-ID' \
-d '{
    "intent": "CAPTURE",
    "payer": {
      "name": {
        "given_name": "Firstname",
        "surname": "Lastname"
      },
      "address": {
        "address_line_1": "123 Main St.",
        "admin_area_2": "Anytown",
        "admin_area_1": "CA",
        "postal_code": "12345",
        "country_code": "US"
      }
    },
    "purchase_units": [
      {
        "reference_id": "Reference_ID_L2L32",
        "description": "Description of PU",
        "custom_id": "Custom-ID",
        "soft_descriptor": "Purchase Descriptor",
        "invoice_id": "INV_202302011234",
        "supplementary_data": {
          "card": {
            "level_2": {
              "invoice_id": "INV_202302011234",
              "tax_total": {
                "currency_code": "USD",
                "value": "5.20"
              }
            },
            "level_3": {
              "shipping_amount": {
                "currency_code": "USD",
                "value": "1.17"
              },
              "duty_amount": {
                "currency_code": "USD",
                "value": "1.16"
              },
              "discount_amount": {
                "currency_code": "USD",
                "value": "1.15"
              },
              "shipping_address": {
                "address_line_1": "123 Main St.",
                "admin_area_2": "Anytown",
                "admin_area_1": "CA",
                "postal_code": "12345",
                "country_code": "US"
              },
              "ships_from_postal_code": "12345",
              "line_items": [
                {
                  "name": "Item1",
                  "description": "Description of Item1",
                  "upc": {
                    "type": "UPC-A",
                    "code": "001004697"
                  },
                  "unit_amount": {
                    "currency_code": "USD",
                    "value": "9.50"
                  },
                  "tax": {
                    "currency_code": "USD",
                    "value": "5.12"
                  },
                  "discount_amount": {
                    "currency_code": "USD",
                    "value": "1.11"
                  },
                  "total_amount": {
                    "currency_code": "USD",
                    "value": "95.10"
                  },
                  "unit_of_measure": "POUND_GB_US",
                  "quantity": "10",
                  "commodity_code": "98756"
                }
              ]
            }
          }
        },
        "amount": {
          "currency_code": "USD",
          "value": "100.30",
          "breakdown": {
            "item_total": {
              "currency_code": "USD",
              "value": "90.20"
            },
            "tax_total": {
              "currency_code": "USD",
              "value": "10.10"
            },
            "shipping": {
              "currency_code": "USD",
              "value": "10.00"
            },
            "discount": {
              "currency_code": "USD",
              "value": "10.00"
            }
          }
        },
        "items": [
          {
            "name": "Item1",
            "description": "Description of Item1",
            "sku": "SKU - 0",
            "url": "http: //example.com",
            "unit_amount": {
              "currency_code": "USD",
              "value": "45.10"
            },
            "tax": {
              "currency_code": "USD",
              "value": "5.05"
            },
            "quantity": "2",
            "category": "PHYSICAL_GOODS"
          }
        ],
        "shipping": {
          "address": {
            "address_line_1": "123 Main St.",
            "admin_area_2": "Anytown",
            "admin_area_1": "CA",
            "postal_code": "12345",
            "country_code": "US"
          }
        }
      }
    ]
  }'
```

- Lines 25-31 declare a level_2 object inside purchase_units.supplementary_data.card, including the invoice ID and the taxes charged for the payment.
- Lines 32-82 declare a level_3 object inside purchase_units.supplementary_data.card. Data includes shipping, duty, discount amounts, line-item information, and units of measure.



#### Ensure consistent field mapping between purchase units and supplementary data
Ensure that the field names, data types, formats, and values in the supplementary_data object match the corresponding fields in the purchase_units object. The following table shows which fields from each object need to match.

| **supplementary_data** | **purchase_units** |
| card.level_2.invoice_id | invoice_id |
| card.level_2.tax_total.currency_code | amount.breakdown.tax_total.currency_code |
| card.level_2.tax_total.value | amount.breakdown.tax_total.value |
| card.level_3.shipping_amount.currency_code | amount.breakdown.shipping.currency_code |
| card.level_3.shipping_amount.value | amount.breakdown.shipping.value |
| card.level_3.discount_amount.currency_code | amount.breakdown.discount.currency_code |
| card.level_3.discount_amount.value | amount.breakdown.discount.value |
| card.level_3.shipping_address.address_line_1 | shipping.address.address_line_1 |
| card.level_3.shipping_address.address_line_2 | shipping.address.address_line_2 |
| card.level_3.shipping_address.admin_area_2 | shipping.address.admin_area_2 |
| card.level_3.shipping_address.admin_area_1 | shipping.address.admin_area_1 |
| card.level_3.shipping_address.postal_code | shipping.address.admin_area_1 |
| card.level_3.shipping_address.country_code | shipping.address.country_code |
| card.level_3.line_items[0].name | items[0].name |
| card.level_3.line_items[0].description | items[0].description |
| card.level_3.line_items[0].upc.type | items[0].upc.type |
| card.level_3.line_items[0].upc.code | items[0].upc.code |
| card.level_3.line_items[0].unit_amount.currency_code | items[0].unit_amount.currency_code |
| card.level_3.line_items[0].unit_amount.value | items[0].unit_amount.value |
| card.level_3.line_items[0].tax.currency_code | items[0].tax.currency_code |
| card.level_3.line_items[0].tax.value | items[0].tax.value |
| card.level_3.line_items[0].total_amount.currency_code | amount.breakdown.item_total.currency_code |
| card.level_3.line_items[0].total_amount.value | amount.breakdown.item_total.value |
| card.level_3.line_items[0].quantity | items[0].quantity |



**Notes:**

- When the common fields between purchase_units and supplementary_data don't match, the values from the latter take precedence.
- When you send a PATCH request that modifies the purchase_units object, include the corresponding supplementary_data object. Update both objects simultaneously to maintain consistency.
- If you don't send supplementary_data in the PATCH request, the system automatically deletes the existing supplementary_data object to prevent discrepancies and ensure data integrity.
