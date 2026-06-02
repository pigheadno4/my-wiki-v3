---
title: Pass a buyer identifier to streamline buyer login
slug: /docs/checkout/standard/customize/pass-buyer-identifier/
createTime: '2024-12-24T08:47:51.266Z'
updateTime: '2025-02-16T22:27:38.513Z'
---

# Pass a buyer identifier to streamline buyer login

You can pass a buyer's email address as the buyer identifier to PayPal through the Create Order request. During one-time checkout, PayPal uses this email address to prefill the buyer's PayPal login page. This streamlines and quickens the buyer authentication process for an effortless login.

In your app, when you Create an order, as part of the request body, send the buyer's email address in the `payment_source.paypal.email_address` field.

#### Sample request

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H 'Content-Type: application/json' \
-H 'PayPal-Request-Id: REQUEST-ID' \
-H 'Authorization: Bearer ACCESS-TOKEN' \
-d '{
    "intent": "CAPTURE",
    "payment_source": {
        "paypal": {
            "email_address": "customer@example.com",
            "experience_context": {
                "shipping_preference": "GET_FROM_FILE",
                "user_action": "PAY_NOW",
                "return_url": "https://example.com/returnUrl",
                "cancel_url": "https://example.com/cancelUrl"
            }
        }
    },
    "purchase_units": [
        {
            "invoice_id": "005384",
            "amount": {
                "currency_code": "USD",
                "value": "40.00"
            }
        }
    ]
}'
```

After a successful request, the passed email address is used to prepopulate the PayPal login page when the buyer pays with PayPal.
