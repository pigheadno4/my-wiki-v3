---
title: Integrate Multibanco using the Orders API
slug: /docs/checkout/apm/multibanco/orders-api/
createTime: "2024-12-06T00:43:39.207Z"
updateTime: "2025-05-06T01:41:19.795Z"
---

# Integrate Multibanco using the Orders API

## Know before you code

- Request approval to enable Multibanco by visiting these sandbox and live links: - Sandbox: [https://www.sandbox.paypal.com/bizsignup/entry?product=multibanco&capabilities=MULTIBANCO&country.x=&lt;merchant's country&gt;](https://www.sandbox.paypal.com/bizsignup/entry?product=multibanco&capabilities=MULTIBANCO&country.x=)
- Live: [https://www.paypal.com/bizsignup/add-product?product=multibanco&capabilities=MULTIBANCO&country.x=&lt;merchant's country&gt;](https://www.paypal.com/bizsignup/add-product?product=multibanco&capabilities=MULTIBANCO&country.x=)

- Partners: Be sure to onboard your merchants upfront, [before they accept payments](/docs/multiparty/seller-onboarding/before-payment/) . Onboarding after making payments, specifically Progressive Onboarding, isn't supported for alternative payment methods.

**Note:** The integration steps for implementing alternative payment methods are similar. If you've integrated another alternative payment method before, you can reuse that code with adjustments for this payment method.

- Make sure you're [subscribed to the following webhook events](/docs/checkout/apm/reference/subscribe-to-webhooks/) : - PAYMENT.CAPTURE.PENDING – Listen for this webhook as an indication that payment initiation was successful, the payment is in a pending state, and is waiting for the buyer to complete the payment.
- PAYMENT.CAPTURE.COMPLETED – Listen for this webhook as an indication that the buyer has completed the payment, which can take up to seven days. You can ship the order to the buyer at this point.
- PAYMENT.CAPTURE.DENIED - Listen for this webhook as an indication that the Multibanco payment instruction has expired or the payer didn't complete the payment on time. You can cancel the order at this point. After you receive each webhook, fetch the latest order details using [Show order details](/docs/api/orders/v2/#orders_get) . The up HATEOAS link in the webhook payload indicates the order associated with the capture.

- Make sure your preference for receiving payments in your PayPal business or merchant account is set to accept and convert to the currency in your account. In your profile, select **Account Settings** &gt; **Payment preferences** &gt; **Block payments** and click **Update** to mark this preference.

- When processing Multibanco payments, you don't need to capture payment for the order.

## Offer Multibanco on the checkout page

You'll need to create the user interface to offer Multibanco and collect the buyer's information, then you'll use the API calls described in the remainder of this topic to:

- create the order
- specify Multibanco as the payment method
- present Multibanco payment instruction to the buyer

Refer to [Payment method icons](https://developer.paypal.com/beta/apm-beta/additional-information/method-icons/) for icons you can use and download locations.

Use the buyer information you captured from your user interface to create an order.

API endpoint used: [Create order](/docs/api/orders/v2/#orders_create)

#### **`Sample request `**

```javascript
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <Access-Token>" \
-d '{
    "intent": "CAPTURE",
    "purchase_units": [
        {
            "amount": {
                "currency_code": "EUR",
                "value": "100.00"
            }
        }
    ]
}'
```

#### **`Sample response`**

```javascript
{
  "id": "54K10082DX701193V",
  "status": "CREATED",
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/54K10082DX701193V",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://www.sandbox.paypal.com/checkoutnow?token=54K10082DX701193V",
      "rel": "approve",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/54K10082DX701193V",
      "rel": "update",
      "method": "PATCH"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/54K10082DX701193V/capture",
      "rel": "capture",
      "method": "POST"
    }
  ]
}
```

### Modify the code

After you copy the code in the sample request, modify the following:

- Access-Token - Your [access token](https://developer.paypal.com/api/rest/authentication) .
- intent - To use an alternative payment method, this parameter must be set to CAPTURE as it is in this sample code.
- purchase_units[0].amount - Pass the value of the order and the currency code.
- Optional: Add other parameters in the [Create order request body](/docs/api/orders/v2/#orders_create) to create an order that reflects the actual order details.

### Step result

A successful request results in the following:

- A return status code of HTTP 201 Created .
- A JSON response body that contains the order ID. You'll use the order ID in the next step.

To specify Multibanco as the payment method the buyer selected in your user interface, confirm the payment source for the order.

Orders API endpoint used: [Confirm the Order](/docs/api/orders/v2/#orders_confirm)

#### **`Sample request`**

```javascript
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/54K10082DX701193V/confirm-payment-source \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <Access-Token>" \
-d '{
    "payment_source": {
        "multibanco": {
            "name": "John Doe",
            "country_code": "PT"
        }
    },
    "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
    "application_context": {
        "locale": "en-PT",
        "return_url": "https://example.com/returnUrl",
        "cancel_url": "https://example.com/cancelUrl"
    }
}'
```

#### **`Sample response `**

```javascript
{
  "id": "54K10082DX701193V",
  "intent": "CAPTURE",
  "payment_source": {
    "multibanco": {
      "name": "John Doe",
      "country_code": "PT"
    }
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/54K10082DX701193V",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://www.sandbox.paypal.com/payment/multibanco?token=54K10082DX701193V",
      "rel": "payer-action",
      "method": "GET"
    }
  ]
}

```

### Modify the code

After you copy the code in the sample request, modify the following:

- Access-Token - Your [access token](https://developer.paypal.com/api/rest/authentication/) .
- Order ID - In the URI for the API call, replace the sample ID with your order ID. In the sample, the order ID is 54K10082DX701193V .
- payment_source - Specify the following: - multibanco as the payment_source .
- PT as the country_code .
- Account holder's full name on name field.

- processing_instruction - Set this value to ORDER_COMPLETE_ON_PAYMENT_APPROVAL for processing Multibanco payments.
- application_context - Specify the preferred language for returned errors, the URL the buyer is returned to after approving the purchase with their selected payment method, and the URL the buyer is returned to after canceling an approval with their selected payment method. **Note:** While return_url and cancel_url are optional fields, this integration requires you specify them to handle the handoff from the payment method back to your site. You can use the cancel_url to redirect buyers when an error occurs while they're on the payment method's site, so make sure your cancel URL works for that situation as well as an actual cancellation by the buyer.

### Step result

A successful request results in the following:

- A return status code of HTTP 200 OK .
- A JSON response body that contains order details and HATEOAS links. You'll use the payer-action redirect in the next step. See also: [HATEOAS links](https://developer.paypal.com/api/rest/responses/#hateoas-links) .

In your user interface, attach the payer-action redirect returned in the Confirm payment source call to the Multibanco payment button. This renders the Multibanco payment instruction.

In the sample, the redirect is: "https://www.sandbox.paypal.com/payment/multibanco?token=54K10082DX701193V" .

You can also send the Multibanco payment instruction to your buyers in an email. Obtain the details from [Show order details](/docs/api/orders/v2/#orders_get) endpoint. References to the payment instruction are present in the payment_source.multibanco.payment_reference and payment_source.multibanco.payment_entity response parameter.

####

#### **`Sample request `**

```javascript
curl -v -X GET https://api-m.sandbox.paypal.com/v2/checkout/orders/54K10082DX701193V \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer <Access-Token>"
```

#### **`Sample response`**

```javascript
{
  "id": "54K10082DX701193V",
  "intent": "CAPTURE",
  "status": "COMPLETED",
  "payment_source": {
    "multibanco": {
      "name": "John Doe",
      "country_code": "PT",
      "payment_reference": "999999919",
      "payment_entity": "11854"
    }
  },
  "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
  "purchase_units": [
    {
      "reference_id": "default",
      "amount": {
        "currency_code": "EUR",
        "value": "100.00"
      },
      "payee": {
        "email_address": "merchant@example.com",
        "merchant_id": "7M4X6DXOX9B9C"
      },
      "payments": {
        "captures": [
          {
            "id": "6AS86814R5412231H",
            "status": "PENDING",
            "status_details": {
              "reason": "OTHER"
            },
            "amount": {
              "currency_code": "EUR",
              "value": "100.00"
            },
            "final_capture": true,
            "seller_protection": {
              "status": "ELIGIBLE",
              "dispute_categories": [
                "ITEM_NOT_RECEIVED",
                "UNAUTHORIZED_TRANSACTION"
              ]
            },
            "links": [
              {
                "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/6AS86814R5412231H",
                "rel": "self",
                "method": "GET"
              },
              {
                "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/6AS86814R5412231H/refund",
                "rel": "refund",
                "method": "POST"
              },
              {
                "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/54K10082DX701193V",
                "rel": "up",
                "method": "GET"
              }
            ],
            "create_time": "2021-06-16T22:52:17Z",
            "update_time": "2021-06-16T22:53:11Z"
          }
        ]
      }
    }
  ],
  "create_time": "2021-06-16T22:52:10Z",
  "update_time": "2021-06-16T22:53:11Z",
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/54K10082DX701193V",
      "rel": "self",
      "method": "GET"
    }
  ]
}
```

### Modify the code

After you copy the code in the sample request, modify the following:

- Access-Token - Your [access token](https://developer.paypal.com/api/rest/authentication/) .
- Order ID - In the URI for the API call, replace the sample ID with your Order ID. In the sample, the Order ID is 54K10082DX701193V .

### Step result

A successful request returns the HTTP 200 OK status code with a JSON response body that returns a COMPLETED status.

A successful approval results in the following:

- The order status changes to COMPLETED , which means the order was created successfully.
- A capture with PENDING status is present in the response parameter purchase_units[0].payments.captures[0] . The up HATEOAS link indicates the order associated with this capture.
- The PAYMENT.CAPTURE.PENDING webhook event is triggered, which indicates that payment initiation was successful, the payment is in a pending state, and is waiting for the buyer to complete the payment. - Wait for the buyer to complete the payment, which might take up to seven days.
- Send a payment confirmation to the buyer with Multibanco payment_reference and payment_entity .

#### Sample PAYMENT.CAPTURE.PENDING webhook

#### **`Sample PAYMENT.CAPTURE.PENDING`**

```javascript
{
  "id": "WH-3XD97656HT346122M-81M194208A0322526",
  "event_version": "1.0",
  "create_time": "2021-06-16T22:52:21.351Z",
  "resource_type": "capture",
  "resource_version": "2.0",
  "event_type": "PAYMENT.CAPTURE.PENDING",
  "summary": "Payment pending for EUR 100.0 EUR",
  "resource": {
    "amount": {
      "value": "100.00",
      "currency_code": "EUR"
    },
    "seller_protection": {
      "dispute_categories": [
        "ITEM_NOT_RECEIVED",
        "UNAUTHORIZED_TRANSACTION"
      ],
      "status": "ELIGIBLE"
    },
    "supplementary_data": {
      "related_ids": {
        "order_id": "54K10082DX701193V"
      }
    },
    "update_time": "2021-06-16T22:52:17Z",
    "create_time": "2021-06-16T22:52:17Z",
    "final_capture": true,
    "links": [
      {
        "method": "GET",
        "rel": "self",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/6AS86814R5412231H"
      },
      {
        "method": "POST",
        "rel": "refund",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/6AS86814R5412231H/refund"
      },
      {
        "method": "GET",
        "rel": "up",
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/54K10082DX701193V"
      }
    ],
    "id": "6AS86814R5412231H",
    "status_details": {
      "reason": "OTHER"
    },
    "status": "PENDING"
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-3XD97656HT346122M-81M194208A0322526",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-3XD97656HT346122M-81M194208A0322526/resend",
      "rel": "resend",
      "method": "POST"
    }
  ]
}
```

When the buyer completes the payment, PAYMENT.CAPTURE.COMPLETED webhook event is triggered, which indicates that payment completion was successful and you can fulfill the order.

Look for one of the following webhooks:

- PAYMENT.CAPTURE.COMPLETED – This webhook is an indication that the buyer has completed the payment, which can take up to seven days to complete. You can ship the order to the buyer at this point.
- PAYMENT.CAPTURE.DENIED - This webhook is an indication that the Multibanco payment has expired or the buyer didn't complete the payment successfully. You should not fulfill the order.

#### **`Sample PAYMENT.CAPTURE.COMPLETED`**

```javascript
{
  "id": "WH-6G192137AT164274E-1WK039370M324962E",
  "event_version": "1.0",
  "create_time": "2021-06-16T22:53:25.068Z",
  "resource_type": "capture",
  "resource_version": "2.0",
  "event_type": "PAYMENT.CAPTURE.COMPLETED",
  "summary": "Payment completed for EUR 100.0 EUR",
  "resource": {
    "amount": {
      "value": "100.00",
      "currency_code": "EUR"
    },
    "seller_protection": {
      "dispute_categories": [
        "ITEM_NOT_RECEIVED",
        "UNAUTHORIZED_TRANSACTION"
      ],
      "status": "ELIGIBLE"
    },
    "supplementary_data": {
      "related_ids": {
        "order_id": "54K10082DX701193V"
      }
    },
    "update_time": "2021-06-16T22:53:11Z",
    "create_time": "2021-06-16T22:52:17Z",
    "final_capture": true,
    "seller_receivable_breakdown": {
      "paypal_fee": {
        "value": "2.25",
        "currency_code": "EUR"
      },
      "gross_amount": {
        "value": "100.00",
        "currency_code": "EUR"
      },
      "net_amount": {
        "value": "97.75",
        "currency_code": "EUR"
      }
    },
    "links": [
      {
        "method": "GET",
        "rel": "self",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/6AS86814R5412231H"
      },
      {
        "method": "POST",
        "rel": "refund",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/6AS86814R5412231H/refund"
      },
      {
        "method": "GET",
        "rel": "up",
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/54K10082DX701193V"
      }
    ],
    "id": "6AS86814R5412231H",
    "status": "COMPLETED"
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-6G192137AT164274E-1WK039370M324962E",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-6G192137AT164274E-1WK039370M324962E/resend",
      "rel": "resend",
      "method": "POST"
    }
  ]
}

```

#### **`Sample PAYMENT.CAPTURE.DENIED`**

```javascript
{
  "id": "WH-6G192137AT164274E-1WK039370M324962E",
  "event_version": "1.0",
  "create_time": "2021-06-16T22:53:25.068Z",
  "resource_type": "capture",
  "resource_version": "2.0",
  "event_type": "PAYMENT.CAPTURE.DENIED",
  "summary": "Payment denied for EUR100.0 EUR",
  "resource": {
    "amount": {
      "value": "100.00",
      "currency_code": "EUR"
    },
    "seller_protection": {
      "dispute_categories": [
        "ITEM_NOT_RECEIVED",
        "UNAUTHORIZED_TRANSACTION"
      ],
      "status": "ELIGIBLE"
    },
    "supplementary_data": {
      "related_ids": {
        "order_id": "54K10082DX701193V"
      }
    },
    "update_time": "2021-06-16T22:53:11Z",
    "create_time": "2021-06-16T22:52:17Z",
    "final_capture": true,
    "seller_receivable_breakdown": {
      "gross_amount": {
        "value": "100.00",
        "currency_code": "EUR"
      },
      "net_amount": {
        "value": "100.00",
        "currency_code": "EUR"
      }
    },
    "links": [
      {
        "method": "GET",
        "rel": "self",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/6AS86814R5412231H"
      },
      {
        "method": "POST",
        "rel": "refund",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/6AS86814R5412231H/refund"
      },
      {
        "method": "GET",
        "rel": "up",
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/54K10082DX701193V"
      }
    ],
    "id": "6AS86814R5412231H",
    "status": "DECLINED"
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-6G192137AT164274E-1WK039370M324962E",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-6G192137AT164274E-1WK039370M324962E/resend",
      "rel": "resend",
      "method": "POST"
    }
  ]
}
```

### Step result

A successful request results in the following:

- If the payment completion by the payer is successful, the capture status changes to COMPLETED and you can ship the order.
- If the buyer is unable to complete the payment successfully, the capture status changes to DENIED .
- Send a confirmation email to the buyer.

## Next steps

### Test integration

Test the integration in the PayPal sandbox environment.

### Go live

Take your application live in the PayPal production environment once testing is successful.
