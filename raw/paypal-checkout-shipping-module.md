---
title: Shipping module
slug: /docs/checkout/standard/customize/shipping-module/
createTime: '2025-01-07T20:48:25.803Z'
updateTime: '2026-03-09T09:49:38.970Z'
---

# Shipping module

## Overview

The shipping module presents shipping details to a buyer during the Pay with PayPal and Pay with Venmo flow. The merchant has several options available for controlling how shipping addresses and shipping options are handled. The server-side shipping callbacks allow you to update the shipping and order amount information as buyers make changes on the review page.

### Merchant and buyer interaction

Buyers can use the shipping module to specify the shipping address and shipping options on the review page. The system sends a callback to the merchant's URL with the updated shipping information.

When the buyer provides their shipping address, a callback is sent to the merchant server with the buyer's address using the server-side shipping callbacks. In response, the merchant can send the shipping options and updated order cost amounts.

You can use server-side callbacks to:

- Verify that you support the shipping method.
- Update shipping costs.
- Change line items in the cart.
- Inform the buyer that you do not support their shipping method.

> While both server-side and client-side callbacks are possible, it is generally recommended to use server-side callbacks, as client-side callbacks may not be available in all situations. For example, client-side callbacks using JS-SDK are designed primarily for web-based integrations and are incompatible with Venmo. They may not be suitable for native mobile applications that often require different APIs or SDKs tailored for mobile platforms.

![PayPal and Venmo review pages showing buyer's shipping address and options.](assets/paypal-shipping-module-review-page.png)

## How it works

1. A buyer clicks on the PayPal or Venmo button displayed on the merchant site.
2. The merchant makes a Create Order API request to set up the flow, including the parameters needed to enable the server-side callbacks.
3. The buyer is taken to the flow where they are authenticated and shown the review page.
4. A server-side callback is created to the merchant's server with the default shipping address from the buyer's wallet.
5. The merchant processes the callback and responds with shipping options for the address and updated order amount.
6. The review page updates to reflect the merchant's revised order amount and shipping options.
7. If the buyer changes the shipping address or shipping options, a callback is made to the merchant. The merchant's response updates the review page.
8. The buyer clicks the pay button on the review page to complete the transaction, which is returned to the merchant.
9. The merchant may make a Show Order Details API call to get the final order information and verify it still matches the information in their system.
10. The merchant captures the order to complete the transaction.

## Create order

Use the Orders v2 API Create Order request to set up the flow. Both Pay with PayPal and Pay with Venmo support the shipping module. The request can utilize either `payment_source:paypal` or `payment_source:venmo`.

### Enabling server-side callbacks

The `payment_source.*.experience_context.order_update_callback_config` object enables and configures server-side callbacks. The `callback_url` field specifies the endpoint on your servers. The `callback_events` array specifies which events you support:

- `SHIPPING_ADDRESS`: Fires when the review page loads for the first time and when the buyer changes their shipping address. **Recommended** — subscribe only to this event and return all shipping options upfront; reduces delays and number of requests.
- `SHIPPING_OPTIONS`: Fires when the buyer selects or changes a shipping option. Subscribe only if you need to recalculate amounts when the selected option changes.

### Configuring shipping preferences

Set via `payment_source.*.experience_context.shipping_preference`:

| Value | Behavior |
| ----- | -------- |
| `GET_FROM_FILE` | Default. Uses the buyer's wallet address. Buyer can change address. Callbacks fire. |
| `NO_SHIPPING` | Removes shipping address from review page and API response. `shipping.phone_number` and `shipping.email_address` still returned for digital goods. |
| `SET_PROVIDED_ADDRESS` | Shows merchant-provided address. Buyer cannot change it. If no address provided, buyer can choose. |

### Passing a shipping address

If you pass a shipping address with `GET_FROM_FILE`, it displays on the review page but buyer can change it. Use `SET_PROVIDED_ADDRESS` to lock it. Use `NO_SHIPPING` for non-shipping transactions.

### Sample Create Order request — Pay with PayPal

```javascript
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -H 'PayPal-Request-Id: REQUEST-ID' \
  -d '{
      "intent": "CAPTURE",
      "payment_source": {
        "paypal": {
          "experience_context": {
            "user_action": "PAY_NOW",
            "shipping_preference": "GET_FROM_FILE",
            "return_url": "https://example.com/returnUrl",
            "cancel_url": "https://example.com/cancelUrl",
            "order_update_callback_config": {
              "callback_events": ["SHIPPING_ADDRESS", "SHIPPING_OPTIONS"],
              "callback_url": "https://example.com/orders?cart_id=h98h98h&session_id=89h788fg8"
            }
          }
        }
      },
      "purchase_units": [{
        "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
        "items": [
          {
            "name": "T-Shirt",
            "description": "Super Fresh Shirt",
            "unit_amount": { "currency_code": "USD", "value": "50.00" },
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
            "unit_amount": { "currency_code": "USD", "value": "25.00" },
            "quantity": "2",
            "category": "PHYSICAL_GOODS",
            "image_url": "https://example.com/static/images/items/1/shoes_running.jpg",
            "url": "https://example.com/url-to-the-item-being-purchased-2",
            "upc": { "type": "UPC-A", "code": "987654321012" }
          }
        ],
        "amount": {
          "currency_code": "USD",
          "value": "100.00",
          "breakdown": { "item_total": { "currency_code": "USD", "value": "100.00" } }
        }
      }]
    }'
```

### Sample Create Order request — Pay with Venmo

Same structure as above with `"venmo"` instead of `"paypal"` in `payment_source`.

## Server-side shipping callbacks

The server-side callback request to the merchant is structurally similar to GET orders, with updated shipping addresses and options sent separately from the order object.

Key points:
- Cart identifier should be embedded in the callback URL if merchants cannot associate their shopping cart with the order.
- Merchants with client-side shopping carts should include item details when they create the order for server-side shipping callbacks.

### Callback request to merchant — shipping address event

> **Warning:** The initial callback to the merchant does NOT include the `shipping_option` section.

```json
{
  "id": "5O190127TN364715T",
  "shipping_address": {
    "country_code": "US",
    "admin_area_1": "TX",
    "admin_area_2": "Dallas",
    "postal_code": "75001"
  },
  "shipping_option": {
    "id": "2",
    "amount": { "currency_code": "USD", "value": "20.00" },
    "type": "SHIPPING",
    "label": "Free Shipping"
  },
  "purchase_units": [{
    "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
    "amount": { "currency_code": "USD", "value": "100.00" }
  }]
}
```

### Merchant success response (HTTP 200)

Amount consistency rules:
- `purchase_units[].amount.breakdown.shipping.value` must equal the selected shipping option's `amount.value`
- `purchase_units[].amount.value` must equal sum of all breakdown amounts
- `item_total` and `tax_total` must match Order/Cart totals
- All `currency_code` values must match across the response

```json
{
  "id": "8HFTASDATTV",
  "purchase_units": [{
    "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
    "amount": {
      "currency_code": "USD",
      "value": "105.00",
      "breakdown": {
        "item_total": { "currency_code": "USD", "value": "100.00" },
        "tax_total": { "currency_code": "USD", "value": "5.00" },
        "shipping": { "currency_code": "USD", "value": "0.00" }
      }
    },
    "shipping_options": [
      { "id": "1", "amount": { "currency_code": "USD", "value": "0.00" }, "type": "SHIPPING", "label": "Free Shipping", "selected": true },
      { "id": "2", "amount": { "currency_code": "USD", "value": "7.00" }, "type": "SHIPPING", "label": "USPS Priority Shipping", "selected": false },
      { "id": "3", "amount": { "currency_code": "USD", "value": "10.00" }, "type": "SHIPPING", "label": "1-Day Shipping", "selected": false }
    ]
  }]
}
```

### Merchant decline response (HTTP 422)

| Callback event | Error code | Message |
| -------------- | ---------- | ------- |
| Shipping address | `ADDRESS_ERROR` | Your order can't be shipped to this address. |
| Shipping address | `COUNTRY_ERROR` | Your order can't be shipped to this country. |
| Shipping address | `STATE_ERROR` | Your order can't be shipped to this state. |
| Shipping address | `ZIP_ERROR` | Your order can't be shipped to this zip. |
| Shipping option | `METHOD_UNAVAILABLE` | The shipping method you selected is unavailable. |
| Shipping option | `STORE_UNAVAILABLE` | Part of your order isn't available at this store. |

```json
{
  "name": "UNPROCESSABLE_ENTITY",
  "details": [{ "issue": "COUNTRY_ERROR" }]
}
```
