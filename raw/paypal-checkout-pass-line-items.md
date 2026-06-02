---
title: Pass line-item details
slug: /docs/checkout/standard/customize/pass-line-items/
createTime: '2024-12-27T11:19:08.545Z'
updateTime: '2025-05-06T22:42:50.061Z'
---

# Pass line-item details

You can pass the details of the items a buyer purchases to PayPal through the Create order request. When a buyer checks out their purchase, PayPal displays these invoice-line-item details, such as the item name, quantity, detailed description, and price, for buyer verification.

## Buyer experience

The details you pass to PayPal are presented to the buyer:

- On the PayPal review page during the Pay with PayPal flow.
- In the post-purchase email sent to the buyer about their payment transaction.
- In the buyer's PayPal account **Activity** > **Transactions** > **All transactions** section.

Displaying the purchase details:

- Enhances buyer experience.
- Provides greater transparency and increases conversion.
- Minimizes disputes as buyers can verify the specifics of their purchase.
- Enhances dispute management by providing merchants with specifics about the disputed item.

![Paysheet with line-item details showing item names, quantities, and prices.](assets/paypal-line-items-paysheet-example.png)

## How it works

1. Pass the buyer's purchase details to PayPal. PayPal displays these details on the PayPal review page for buyer verification.
2. (Optional) Confirm whether the PayPal review page details match the details in your system.
3. Handle buyer updates to the shipping addresses or options that modify line-items.
4. Handle buyer updates to the purchases before you capture the order and complete payment processing.

## Create an order and pass line-item details

In your app code, when you Create an Order, send the line-item details in the `purchase_units[].items[]` array. If multiple line items exist, send multiple item objects in the array.

### Item attributes

| Attribute | Required | Description |
| --------- | -------- | ----------- |
| `name` | Yes | Name of the purchased item |
| `quantity` | Yes | Quantity as a whole number |
| `unit_amount` | Yes | Price per unit — object with `currency_code` and `value`. Must align with `purchase_units[].amount.breakdown.item_total` |
| `description` | No | Detailed item description |
| `sku` | No | Stock keeping unit |
| `url` | No | URL to the purchased item — visible to buyer |
| `category` | No | `DIGITAL_GOODS`, `PHYSICAL_GOODS`, or `DONATION` |
| `image_url` | No | URL of item image — file type and size restrictions apply |
| `tax` | No | Item tax per unit — object. Must align with `purchase_units[].amount.breakdown.tax_total` |

Also send total amount breakdown in `purchase_units[].amount.breakdown`.

### Sample request — Create order with line items

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H 'Content-Type: application/json' \
-H 'PayPal-Request-Id: REQUEST-ID' \
-H 'Authorization: Bearer ACCESS-TOKEN' \
-d '{
  "intent": "CAPTURE",
  "purchase_units": [
    {
      "invoice_id": "90210",
      "items": [
        {
          "name": "T-Shirt",
          "description": "Super Fresh Shirt",
          "unit_amount": { "currency_code": "USD", "value": "20.00" },
          "quantity": "1",
          "category": "PHYSICAL_GOODS",
          "sku": "sku01",
          "image_url": "https://example.com/static/images/items/1/tshirt_green.jpg",
          "url": "https://example.com/url-to-the-item-being-purchased-1",
          "upc": { "type": "UPC-A", "code": "123456789012" },
          "tax": { "currency_code": "USD", "value": "10.00" }
        },
        {
          "name": "Shoes",
          "description": "Running, Size 10.5",
          "sku": "sku02",
          "unit_amount": { "currency_code": "USD", "value": "100.00" },
          "quantity": "2",
          "category": "PHYSICAL_GOODS",
          "image_url": "https://example.com/static/images/items/1/shoes_running.jpg",
          "url": "https://example.com/url-to-the-item-being-purchased-2",
          "upc": { "type": "UPC-A", "code": "987654321012" },
          "tax": { "currency_code": "USD", "value": "5.00" }
        }
      ],
      "amount": {
        "currency_code": "USD",
        "value": "230.00",
        "breakdown": {
          "item_total": { "currency_code": "USD", "value": "220.00" },
          "shipping": { "currency_code": "USD", "value": "10.00" },
          "tax_total": { "currency_code": "USD", "value": "20.00" }
        }
      }
    }
  ]
}'
```

## Optional: Retrieve line-item details

To confirm whether the line-item(s) details with PayPal match the details in your system, use the Show order details API request.

### Sample request — Show order details

```curl
curl -v -X GET https://api-m.sandbox.paypal.com/v2/checkout/orders/ORDER-ID \
-H 'Authorization: Bearer ACCESS-TOKEN'
```

### Sample response

```json
{
  "intent": "CAPTURE",
  "purchase_units": [
    {
      "invoice_id": "90210",
      "amount": {
        "currency_code": "USD",
        "value": "230.00",
        "breakdown": {
          "item_total": { "currency_code": "USD", "value": "220.00" },
          "shipping": { "currency_code": "USD", "value": "10.00" }
        }
      },
      "items": [
        {
          "name": "T-Shirt",
          "description": "Super Fresh Shirt",
          "unit_amount": { "currency_code": "USD", "value": "20.00" },
          "quantity": "1",
          "category": "PHYSICAL_GOODS",
          "sku": "sku01",
          "image_url": "https://example.com/static/images/items/1/tshirt_green.jpg",
          "url": "https://example.com/url-to-the-item-being-purchased-1",
          "upc": { "type": "UPC-A", "code": "123456789012" }
        },
        {
          "name": "Shoes",
          "description": "Running, Size 10.5",
          "sku": "sku02",
          "unit_amount": { "currency_code": "USD", "value": "100.00" },
          "quantity": "2",
          "category": "PHYSICAL_GOODS",
          "image_url": "https://example.com/static/images/items/1/shoes_running.jpg",
          "url": "https://example.com/url-to-the-item-being-purchased-2",
          "upc": { "type": "UPC-A", "code": "987654321012" }
        }
      ]
    }
  ]
}
```

## Handle shipping updates that modify line-items

> **Note**: This step is valid only if you implement the Shipping callback.

During the Pay with PayPal flow, if the buyer modifies the shipping address or shipping options and if these changes impact the items that can be delivered to the buyer, use the Shipping callback update to update the line items in the order.

## Handle buyer updates to line-items

After payment approval from the buyer, the line-items may require modification due to:

- Purchase changes that the buyer makes after verifying the paysheet.
- Changes on your website before capturing the order.

To update the line-item details, use the Update order details API request (`PATCH /v2/checkout/orders/{order_id}`).

Pass the following:
- `op`: Operation — `add`, `remove`, or `replace`
- `value`: Required if `op` is `add` or `replace`

### Sample request — Update line item

```curl
curl -v -X PATCH https://api-m.sandbox.paypal.com/v2/checkout/orders/ORDER-ID \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer ACCESS-TOKEN' \
-d '[
  {
    "op": "replace",
    "path": "/purchase_units/@reference_id=='\''default'\''/items/quantity",
    "value": 2
  }
]'
```
