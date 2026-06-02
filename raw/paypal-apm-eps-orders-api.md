---
title: Integrate EPS using the Orders API
slug: /docs/checkout/apm/eps/orders-api/
createTime: "2024-12-10T13:05:00.634Z"
updateTime: "2025-03-19T00:05:20.738Z"
---

# Integrate EPS using the Orders API

Render payment buttons and process payments with the Orders API.

## Know before you code

- Request approval to enable EPS by visiting these sandbox and live links: - Sandbox: [https://www.sandbox.paypal.com/bizsignup/entry?product=eps&capabilities=EPS&country.x=&lt;merchant's country&gt;](https://www.sandbox.paypal.com/bizsignup/entry?product=eps&capabilities=EPS&country.x=)
- Live: [https://www.paypal.com/bizsignup/add-product?product=eps&capabilities=EPS&country.x=&lt;merchant's country&gt;](https://www.paypal.com/bizsignup/add-product?product=eps&capabilities=EPS&country.x=)

- Partners: Be sure to onboard your merchants upfront, [before they accept payments](/docs/multiparty/seller-onboarding/before-payment/) . Onboarding after making payments, specifically Progressive Onboarding, isn't supported for alternative payment methods.

**Note:** The integration steps for implementing alternative payment methods are similar. If you've integrated another alternative payment method before, you can reuse that code with adjustments for this payment method.

- Make sure you're [subscribed to the following webhook events](/docs/checkout/apm/reference/subscribe-to-webhooks/) : - PAYMENT.CAPTURE.COMPLETED - This webhook notifies about a successful order capture.
- PAYMENT.CAPTURE.DENIED - This webhook tells you when an order capture fails.

- Make sure your preference for receiving payments in your PayPal business or merchant account is set to accept and convert to the currency in your account. In your profile, select **Account Settings** &gt; **Payment preferences** &gt; **Block payments** and click **Update** to mark this preference.

- When processing EPS payments, you don't need to capture payment for the order.

## Offer EPS on the checkout page

You'll need to create the user interface to offer EPS and collect the buyer's information, then you'll use the API calls described in the remainder of this topic to:

- Create the order withbuyer's full_name, country_code and EPS as the payment source.
- Redirect the buyer to EPS.

Refer to [Payment method icons](/docs/checkout/apm/reference/method-icons/) for icons you can use and download locations.

Use the buyer information you captured from your user interface to create an order with EPS as the payment source.

API endpoint used: [Create order](/docs/api/orders/v2/#orders_create)

#### **`Sample request`**

```javascript
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H 'PayPal-Request-Id: <PayPal-Request-Id>' \
-H 'Authorization: Bearer <Access-Token>' \
-H "Content-Type: application/json" \
-d '{
    "intent": "CAPTURE",
    "payment_source": {
        "eps": {
          "country_code": "AT",
          "name": "John Doe"
        }
    },
    "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
    "purchase_units": [
        {
            "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
            "amount": {
                "currency_code": "EUR",
                "value": "1.00"
              }
          }
      ],
      "application_context": {
      "locale": "en-AT",
      "return_url": "https://example.com/returnUrl",
      "cancel_url": "https://example.com/cancelUrl"
    }
  }'
```

#### **`Sample response`**

```javascript
{
    "id": "1BV95196WW992540E",
    "status": "PAYER_ACTION_REQUIRED",
    "payment_source": {
        "eps": {
            "name": "John Doe",
            "country_code": "AT"
        }
    },
    "links": [
        {
            "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/1BV95196WW992540E",
            "rel": "self",
            "method": "GET"
        },
        {
            "href": "https://www.sandbox.paypal.com/payment/eps?token=1BV95196WW992540E",
            "rel": "payer-action",
            "method": "GET"
        }
    ]
}
```

### Modify the code

After you copy the code in the sample request, modify the following:

- Access-Token - Your [access token](https://developer.paypal.com/api/rest/authentication/) .
- PayPal-Request-Id - Replace the sample ID with a unique ID you generate. This ID helps prevent duplicate authorizations in the event that the API call is disrupted. See also: [API idempotency](https://developer.paypal.com/reference/guidelines/idempotency/)
- intent - To use an alternative payment method, this parameter must be set to CAPTURE as it is in this sample code.
- payment_source - Specify eps as the payment method and include the country code and account holder's full name.
- purchase_units: amount - Pass the amount of the order and the currency code.
- processing_instruction - Set this value to ORDER_COMPLETE_ON_PAYMENT_APPROVAL as it is in this sample code.
- application_context - Specify the preferred language for returned errors, the URL the buyer is returned to after approving the purchase with their selected payment method, and the URL the buyer is returned to after canceling an approval with their selected payment method. While return_url and cancel_url are optional fields, this integration requires you specify them to handle the handoff from the payment method back to your site. You can use the cancel_url to redirect buyers when an error occurs while they're on the payment method's site, so make sure your cancel URL works for that situation as well as an actual cancellation by the buyer.

**Note:** Change or add other parameters in the [Create order request body](/docs/api/orders/v2/#orders_create) to create an order that reflects the actual order details.

### Step result

A successful request results in the following:

- A return status code of HTTP 200 OK .
- A JSON response body that contains the order ID. You'll use the order ID and payer-action HATEOAS URL in the next step. See also: [HATEOAS links](https://developer.paypal.com/api/rest/responses/#hateoas-links) .

####

## Redirect buyer for purchase approval

In your user interface, attach the payer-action redirect URL returned in the Create Order response to the EPS payment button. This sends the buyer to their bank to approve the purchase. Once the buyer approves the purchase, the payment is automatically captured.

In the sample, the redirect URL is: "https://www.sandbox.paypal.com/payment/eps?token=1BV95196WW992540E"

### Step result

After successfully completing the bank approval:

- The buyer is redirected to the return_url mentioned in the Create Order request.
- The PAYMENT.CAPTURE.COMPLETED webhook event is triggered, which indicates that payment capture was successful.

After unsuccessful bank approval:

- The buyer is redirected to the cancel_url mentioned in the Create Order request.

## Listen to webhooks for payment status

Listen to the following webhooks to get the result of order capture:

- The PAYMENT.CAPTURE.COMPLETED webhook event indicates a successful order capture.
- The PAYMENT.CAPTURE.DENIED webhook events indicate a failed order capture.
- Optional: Use [Show order details](/docs/api/orders/v2/#orders_get) endpoint to determine the status of an order. - The up HATEOAS link indicates the order associated with this capture.

See [Subscribe to checkout webhooks](/docs/checkout/apm/reference/subscribe-to-webhooks/) for more information.

Here are some additional resources as you create webhook handler code:

- [Webhook Management API](/docs/api/webhooks/v1/) - Manage webhooks, list event notifications, and more.
- Webhook events - [Checkout webhook events](https://developer.paypal.com/api/rest/webhooks/event-names/#checkout-buyer-approvall) - Checkout buyer approval-related webhooks.
- [Order webhook events](https://developer.paypal.com/api/rest/webhooks/event-names/) - Other order-related webhooks.

- [Show order details endpoint](/docs/api/orders/v2/#orders_get) - Determine the status of an order.

### Sample webhook payloads

#### **`Sample PAYMENT.CAPTURE.COMPLETED`**

```javascript
{
  "id": "WH-2B342482FC0449155-12X09416XP387753C",
  "event_version": "1.0",
  "create_time": "2022-04-05T10:37:05Z",
  "resource_type": "capture",
  "resource_version": "2.0",
  "event_type": "PAYMENT.CAPTURE.COMPLETED",
  "summary": "Payment completed for EUR 1.00 EUR",
  "resource": {
    "amount": {
      "value": "1.00",
      "currency_code": "EUR"
    },
    "supplementary_data": {
      "related_ids": {
        "order_id": "1BV95196WW992540E"
      }
    },
    "create_time": "2022-04-05T10:37:05Z",
    "update_time": "2022-04-05T10:37:05Z",
    "final_capture": true,
    "seller_receivable_breakdown": {
      "paypal_fee": {
        "value": "0.20",
        "currency_code": "EUR"
      },
      "gross_amount": {
        "value": "1.00",
        "currency_code": "EUR"
      },
      "net_amount": {
        "value": "0.80",
        "currency_code": "EUR"
      }
    },
    "custom_id": "Custom-1234",
    "invoice_id": "Invoice-12345",
    "links": [
      {
        "method": "GET",
        "rel": "self",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/56U00550J8319094C"
      },
      {
        "method": "POST",
        "rel": "refund",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/56U00550J8319094C/refund"
      },
      {
        "method": "GET",
        "rel": "up",
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/1BV95196WW992540E"
      }
    ],
    "id": "56U00550J8319094C",
    "status": "COMPLETED"
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-2B342482FC0449155-12X09416XP387753C",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-2B342482FC0449155-12X09416XP387753C/resend",
      "rel": "resend",
      "method": "POST"
    }
  ]
}
```

#### **`Sample PAYMENT.CAPTURE.DENIED`**

```javascript
{
  "id": "WH-2B342482FC0449155-12X09416XP387753C",
  "event_version": "1.0",
  "create_time": "2022-04-05T10:37:05Z",
  "resource_type": "capture",
  "resource_version": "2.0",
  "event_type": "PAYMENT.CAPTURE.DENIED",
  "summary": "Payment denied for EUR 1.00 EUR",
  "resource": {
    "amount": {
      "value": "1.00",
      "currency_code": "EUR"
    },
    "supplementary_data": {
      "related_ids": {
        "order_id": "1BV95196WW992540E"
      }
    },
    "create_time": "2022-04-05T10:37:05Z",
    "update_time": "2022-04-05T10:37:05Z",
    "final_capture": true,
    "seller_receivable_breakdown": {
      "paypal_fee": {
        "value": "0.20",
        "currency_code": "EUR"
      },
      "gross_amount": {
        "value": "1.00",
        "currency_code": "EUR"
      },
      "net_amount": {
        "value": "0.80",
        "currency_code": "EUR"
      }
    },
    "links": [
      {
        "method": "GET",
        "rel": "self",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/56U00550J8319094C"
      },
      {
        "method": "POST",
        "rel": "refund",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/56U00550J8319094C/refund"
      },
      {
        "method": "GET",
        "rel": "up",
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/1BV95196WW992540E"
      }
    ],
    "id": "56U00550J8319094C",
    "status": "DECLINED"
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-2B342482FC0449155-12X09416XP387753C",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-2B342482FC0449155-12X09416XP387753C/resend",
      "rel": "resend",
      "method": "POST"
    }
  ]
}
```

#### **`Sample CHECKOUT.ORDER.DECLINED`**

```javascript
{
  "id": "WH-1SW574877T049922Y-2X2706431J788111J",
  "event_version": "1.0",
  "create_time": "2022-04-08T09:20:19Z",
  "resource_type": "checkout-order",
  "resource_version": "2.0",
  "event_type": "CHECKOUT.ORDER.DECLINED",
  "summary": "An order has been declined",
  "resource": {
    "create_time": "2022-04-08T09:20:19Z",
    "purchase_units": [
      {
        "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
        "amount": {
          "currency_code": "EUR",
          "value": "1.00"
        },
        "most_recent_errors": [
          {
            "issue": "PAYMENT_SOURCE_CANNOT_BE_USED",
            "description": "The provided payment source cannot be used to pay for the order. Please try again with a different payment source by creating a new order."
          }
        ]
      }
    ],
    "links": [
      {
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/1BV95196WW992540E",
        "rel": "self",
        "method": "GET"
      }
    ],
    "id": "1BV95196WW992540E",
    "payment_source": {
      "eps": {
        "name": "John Doe",
        "country_code": "AT"
      }
    },
    "intent": "CAPTURE",
    "status": "PAYER_ACTION_REQUIRED"
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-1SW574877T049922Y-2X2706431J788111J",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-1SW574877T049922Y-2X2706431J788111J/resend",
      "rel": "resend",
      "method": "POST"
    }
  ]
}
```

**Note:**- The order ID from [Step 2](#create-an-order) should match the resource.supplementary_data.related_ids.order_id parameter in the webhook payload.

- When an order is declined, Sample CHECKOUT.ORDER.DECLINED webhook passes the error code and message in the most_recent_error parameter of the purchase_unit object.

Alternatively, if your app misses the webhook needed to capture the order, you can get the order capture result by sending a GET call to the [Show order details](/docs/api/orders/v2/#orders_get) endpoint of the Orders v2 API.

**Important:** Exercise caution when polling for order capture results using the [Show order details](/docs/api/orders/v2/#orders_get) endpoint. PayPal enforces rate limits on API requests.

#### **`Sample request`**

```javascript
curl -v -X GET https://api-m.sandbox.paypal.com/v2/checkout/orders/1BV95196WW992540E \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer <Access-Token>"
```

#### **`Sample response`**

```javascript
{
  "id": "1BV95196WW992540E",
  "intent": "CAPTURE",
  "status": "COMPLETED",
  "payment_source": {
    "eps": {
        "name": "John Doe",
        "country_code": "AT"
      }
  },
  "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
  "purchase_units": [
    {
      "reference_id": "default",
      "amount": {
        "currency_code": "EUR",
        "value": "1.00"
      },
      "payments": {
        "captures": [
          {
            "id": "56U00550J8319094C",
            "status": "COMPLETED",
              "amount": {
                "currency_code": "EUR",
                "value": "1.00"
              },
            "final_capture": true,
            "seller_receivable_breakdown": {
              "gross_amount": {
                "currency_code": "EUR",
                "value": "1.00"
              },
              "paypal_fee": {
                "currency_code": "EUR",
                "value": "0.20"
              },
              "net_amount": {
                "currency_code": "EUR",
                "value": "0.80"
              }
            },
            "links": [
              {
                "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/56U00550J8319094C",
                "rel": "self",
                "method": "GET"
              },
              {
                "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/56U00550J8319094C/refund",
                "rel": "refund",
                "method": "POST"
              },
              {
                "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/1BV95196WW992540E",
                "rel": "up",
                "method": "GET"
              }
            ],
            "create_time": "2022-04-08T09:20:19Z",
            "update_time": "2022-04-08T09:20:19Z"
          }
        ]
      }
    }
  ],
    "create_time": "2022-04-08T09:08:56Z",
    "update_time": "2022-04-08T09:20:19Z",
    "links": [
      {
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/1BV95196WW992540E",
        "rel": "self",
        "method": "GET"
      }
    ]
}
```

### Step result

A successful request returns the HTTP 200 OK status code with a JSON response body that returns a COMPLETED status.

A successfully captured order has the following:

- The order status as COMPLETED , which means the order was captured successfully.
- A capture with COMPLETED status is present in the response parameter purchase_units[0].payments.captures[0] .
- The up HATEOAS link indicates the order associated with this capture.

## Notify buyer of payment success

After a successful payment, notify the buyer of a successful transaction. You can do this by sending a confirmation email.

## Next steps

### Test integration

Test the integration in the PayPal sandbox environment.

### Go live

Take your application live in the PayPal production environment once testing is successful.
