---
title: Overcharge handling
slug: /docs/checkout/standard/customize/overcharge-handling/
createTime: '2024-04-25T23:54:30.361Z'
updateTime: '2025-05-06T06:26:00.563Z'
---

# Overcharge handling

In PSD2 rules, an overcharge is when a customer is charged an amount that is more than what they agreed to pay for a product or service. The payment service provider applies strong customer authentication (SCA) to the final amount of the transaction or declines the transaction if the final amount is higher than the amount the buyer agreed to when initiating the transaction. PayPal defines SCA as re-authorization in this case. For more information, see New overcapture requirements. If you charge more than the amount the buyer has approved to pay during checkout, the Capture Order API returns a `PAYER_ACTION_REQUIRED` error. The API provides a URL redirecting the buyer to re-approve the new amount.

## How it works

- The payer checks out and approves the amount presented on PayPal pages.
- A higher amount than the payer approved is authorized and captured.
- A `PAYER_ACTION_REQUIRED` error is returned.
- Optional: Use the Confirm Payment Source API to provide a `return_url` or `cancel_url`. The API can also block shipping address changes in which `shipping_preferences=SET_PROVIDED_ADDRESS`.
- Redirect the buyer to the payer-action URL.
- The buyer approves the higher amount and is redirected to the return URL.
- The order is captured.

### Integration

The flow chart shows the following integration steps:

1. Create an order with the Orders V2 API.
2. The smart button redirects the buyer to PayPal.
3. The buyer approves the order on the PayPal checkout pages.
4. The PayPal checkout window closes. The buyer is returned to merchant's checkout.
5. The buyer selects a shipping method and confirms other details.
6. Use the Patch Order API to update the shipping costs, shipping address, and other details.
7. Capture the order.
8. If capture fails with HTTP 422 `PAYER_ACTION_REQUIRED`, redirect the buyer to PayPal using the payer-action URL.
9. Buyer re-approves the order and is redirected to the return URL.
10. Capture the order.

![Swimlane diagram showing the overcharge handling integration flow.](assets/paypal-overcharge-handling-flow.png)

### Sample request — Patch Order

```json
[{
  "op": "replace",
  "path": "/purchase_units/@reference_id=='default'/amount",
  "value": {
    "currency_code": "USD",
    "value": "101",
    "breakdown": {
      "item_total": { "currency_code": "USD", "value": 1.00 },
      "shipping": { "currency_code": "USD", "value": 100.00 }
    }
  }
}]
```

The request returns HTTP 204.

### Successful capture response

```json
{
  "id": "5KM89009KL896372M",
  "intent": "CAPTURE",
  "status": "COMPLETED"
}
```

### Overcapture error response (HTTP 422)

```json
{
  "name": "UNPROCESSABLE_ENTITY",
  "details": [{
    "issue": "PAYER_ACTION_REQUIRED",
    "description": "Payer needs to perform the following action before proceeding with payment."
  }],
  "message": "The requested action could not be performed, semantically incorrect, or failed business validation.",
  "debug_id": "9495b4f46e3ff",
  "links": [
    {
      "href": "https://developer.paypal.com/docs/api/orders/v2/#error-PAYER_ACTION_REQUIRED",
      "rel": "information_link",
      "method": "GET"
    },
    {
      "href": "https://www.sandbox.paypal.com/checkoutnow?token=XYZ",
      "rel": "payer-action",
      "method": "GET"
    }
  ]
}
```

Set `shipping_preference` to `SET_PROVIDED_ADDRESS` to confirm the payment source. You need to pass `return_url` and `cancel_url` if you don't provide them in the Create Order API call.

### Sample request — Confirm payment source

```json
{
  "payment_source": {
    "paypal": {
      "experience_context": {
        "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED",
        "shipping_preference": "SET_PROVIDED_ADDRESS",
        "user_action": "PAY_NOW",
        "return_url": "https://example.com/returnUrl",
        "cancel_url": "https://example.com/cancelUrl"
      }
    }
  }
}
```

### Sample response — Confirm payment source

```json
{
  "id": "3VD082734S317882J",
  "intent": "CAPTURE",
  "status": "PAYER_ACTION_REQUIRED",
  "payment_source": { "paypal": {} },
  "purchase_units": [{
    "reference_id": "default",
    "amount": {
      "currency_code": "USD",
      "value": "101.00",
      "breakdown": {
        "item_total": { "currency_code": "USD", "value": "1.00" },
        "shipping": { "currency_code": "USD", "value": "100.00" }
      }
    },
    "payee": {
      "email_address": "buyer@example.com",
      "merchant_id": "1234567890"
    },
    "description": "Payment for order",
    "custom_id": "1234567890",
    "invoice_id": "JAkqXHx5UlAvzHf",
    "items": [{
      "name": "shoes",
      "unit_amount": { "currency_code": "USD", "value": "1.00" },
      "quantity": "1",
      "description": "Nadfsdf"
    }],
    "shipping": {
      "name": { "full_name": "Firstname Lastname" },
      "address": {
        "address_line_1": "123 Main St",
        "admin_area_2": "Anytown",
        "postal_code": "12345",
        "country_code": "US"
      }
    }
  }],
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/3VD082734S317882J",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://www.sandbox.paypal.com/checkoutnow?token=3VD082734S317882J",
      "rel": "payer-action",
      "method": "GET"
    }
  ]
}
```
