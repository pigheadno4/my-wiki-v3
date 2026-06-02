---
title: Integrate Trustly using the Orders API
slug: /docs/checkout/apm/trustly/orders-api/
createTime: "2024-12-11T03:46:50.515Z"
updateTime: "2025-05-06T02:50:44.764Z"
---

# Integrate Trustly using the Orders API

## Know before you code

- Request approval to enable Trustly by visiting these sandbox and live links: - Sandbox: [https://www.sandbox.paypal.com/bizsignup/entry?product=trustly&capabilities=TRUSTLY&country.x=&lt;merchant's country&gt;](https://www.sandbox.paypal.com/bizsignup/entry?product=trustly&capabilities=TRUSTLY&country.x=)
- Live: [https://www.paypal.com/bizsignup/add-product?product=trustly&capabilities=TRUSTLY&country.x=&lt;merchant's country&gt;](https://www.sandbox.paypal.com/bizsignup/entry?product=trustly&capabilities=TRUSTLY&country.x=)

- Partners: Be sure to onboard your merchants upfront, [before they accept payments](/docs/multiparty/checkout/apm/reference/seller-onboarding-before-payment) . Onboarding after making payments, specifically Progressive Onboarding, isn't supported for alternative payment methods.

**Note:**The integration steps for implementing alternative payment methods are similar. If you've integrated another alternative payment method before, you can likely reuse that code with adjustments for this payment method.- Make sure you're [subscribed to the following webhook events](/docs/checkout/apm/reference/subscribe-to-webhooks/) : - PAYMENT.CAPTURE.PENDING – Listen for this webhook as an indication that payment initiation was successful, the payment is in a pending state, and is waiting for the buyer to complete the payment. You'll act on this webhook in the [Redirect buyer for purchase approval](#redirect-buyer-for-purchase-approval) step.

- PAYMENT.CAPTURE.COMPLETED – Listen for this webhook as an indication that the buyer has completed the payment, which can take up to seven days. You can ship the order to the buyer at this point. You'll act on this webhook in the [Fulfill the order](#fulfill-the-order) step.
- PAYMENT.CAPTURE.DENIED - Listen for this webhook as an indication that the Multibanco payment instruction has expired or the payer didn't complete the payment on time. You can cancel the order at this point. You'll act on this webhook in the [Fulfill the order](#fulfill-the-order) step. After you receive each webhook, fetch the latest order details using [Show order details](/docs/api/orders/v2/#orders_get) . The up HATEOAS link in the webhook payload indicates the order associated with the capture.

- Make sure your preference for receiving payments in your PayPal business or merchant account is set to accept and convert to the currency in your account. In your profile, select **Account Settings** &gt; **Payment preferences** &gt; **Block payments** and click **Update** to mark this preference.
- When processing Trustly payments, you don't need a call to capture payment for the order.

## Offer Trustly on the checkout page

You'll need to create the user interface to offer Trustly and collect the buyer's information, then you'll use the API calls described in the remainder of this topic to:

- Create the order with thebuyer's full_name , country_code , and trustly as the payment source.
- Redirect the buyer to Trustly.

Refer to [Payment method icons](/docs/checkout/apm/reference/method-icons/) for icons you can use and download locations.

Use the buyer information you captured from your user interface to create an order with Trustly as the payment source.

API endpoint used: [Create order](/docs/api/orders/v2/#orders_create)

#### **`Sample request`**

```javascript
curl -v -X POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer ACCESS-TOKEN' \
-H 'PayPal-Request-Id: PAYPAL-REQUESTID' \
-d '{
  "intent": "CAPTURE",
  "purchase_units": [
    {
      "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
      "amount": {
        "currency_code": "EUR",
        "value": "100.00"
      }
    }
  ],
  "payment_source": {
    "trustly": {
      "country_code": "NL",
      "name": "Firstname Lastname"
    }
  },
  "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
  "application_context": {
    "locale": "en-NL",
    "return_url": "https://example.com/returnUrl",
    "cancel_url": "https://example.com/cancelUrl"
  }
}'
```

#### **`Sample response`**

```javascript
{
  "id": "5O190127TN364715T",
  "status": "PAYER_ACTION_REQUIRED",
  "payment_source": {
    "trustly": {
      "country_code": "NL",
      "name": "Firstname Lastname"
    }
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://www.sandbox.paypal.com/payment/trustly?token=5O190127TN364715T",
      "rel": "payer-action",
      "method": "GET"
    }
  ]
}
```

### Modify the code

After you copy the code in the sample request, modify the following:

- ACCESS-TOKEN - Your [access token](https://developer.paypal.com/api/rest/authentication/) .
- PayPal-Request-Id - Replace the sample ID with a unique ID you generate. This ID helps prevent duplicate authorizations in the event that the API call is disrupted. See also: [API idempotency](https://developer.paypal.com/reference/guidelines/idempotency/) .
- intent - Set this value to CAPTURE .
- payment_source - Specify trustly as the payment method, and include the following: - country_code - the [2-character country code](https://developer.paypal.com/api/rest/reference/country-codes/) for the payer's location.
- name - The payer's full name.
- email - The payer's email.

- application_context - Specify the following: - locale - The preferred language for returned errors.
- return_url - The URL the buyer is returned to after approving or canceling the purchase with their selected payment method.
- cancel_url - The URL is a placeholder for future reference for now.

- processing_instruction - Set this value to ORDER_COMPLETE_ON_PAYMENT_APPROVAL .
- purchase_units: amount - Pass the value of the order and the currency code .

**Note:**Change or add other parameters in the[Create order request body](/docs/api/orders/v2/#orders_create)to create an order that reflects the actual order details.

### Step result

A successful request results in the following:

- A return status code of HTTP 200 OK .
- A JSON response body that contains the order ID. You'll use the order ID and payer-action HATEOAS URL in the next step, [Redirect buyer for purchase approval](#redirect-buyer-for-purchase-approval) . See also: [HATEOAS links](https://developer.paypal.com/api/rest/responses/#hateoas-links) .

In your user interface, attach the payer-action redirect URL returned in the Create order response to the Trustly payment button.

In the sample, the redirect URL is: "https://www.sandbox.paypal.com/payment/trustly?token=5O190127TN364715T" .

### Step result

- The order status changes to COMPLETED , which means the order was created successfully.
- A capture with PENDING status is present in the response parameter purchase_units[0].payments.captures[0] . The up HATEOAS link indicates the order associated with this capture.
- The PAYMENT.CAPTURE.PENDING webhook event is triggered, which indicates that payment initiation was successful, the payment is in a pending state, and is waiting for the buyer to complete the payment.
- This sends the buyer to their bank to approve the purchase.
- Wait for the buyer to authorize the payment. Payment completion happens within 7 days of the payment authorization.

#### Sample PAYMENT.CAPTURE.PENDING webhook

#### **`Sample PAYMENT.CAPTURE.PENDING webhook`**

```javascript
{
  "id": "WH-4TV11484PJ0099250-1WB8208433136945G",
  "event_version": "1.0",
  "create_time": "2023-10-19T11:50:35.619Z",
  "resource_type": "capture",
  "resource_version": "2.0",
  "event_type": "PAYMENT.CAPTURE.PENDING",
  "summary": "Payment pending for EUR 15.39 EUR",
  "resource": {
    "id": "892032536L382192T",
    "amount": {
      "currency_code": "EUR",
      "value": "15.39"
    },
    "final_capture": true,
    "invoice_id": "Invoice-12345",
    "custom_id": "Custom-1234",
    "status": "PENDING",
    "status_details": {
      "reason": "OTHER"
    },
    "supplementary_data": {
      "related_ids": {
        "order_id": "5O190127TN364715T"
      }
    },
    "payee": {
      "email_address": "payee@example.com",
      "merchant_id": "1111111111111"
    },
    "create_time": "2023-10-19T11:50:31Z",
    "update_time": "2023-10-19T11:50:31Z",
    "links": [
      {
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/892032536L382192T",
        "rel": "self",
        "method": "GET"
      },
      {
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/892032536L382192T/refund",
        "rel": "refund",
        "method": "POST"
      },
      {
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",
        "rel": "up",
        "method": "GET"
      }
    ]
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-4TV11484PJ0099250-1WB8208433136945G",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-4TV11484PJ0099250-1WB8208433136945G/resend",
      "rel": "resend",
      "method": "POST"
    }
  ]
}
```

After the buyer authorizes the payment, and the payment completes:

- The buyer is redirected to the return_url mentioned in the Create order request.
- The capture status changes to COMPLETED .
- The PAYMENT.CAPTURE.COMPLETED webhook event is triggered, which indicates that payment capture was successful. You can ship the order to the buyer at this point.

**Note:** Once the buyer authorizes the payment, payment completion happens within 7 days, depending on the bank used for the payment. You should wait until payment completion to ship the goods.

If the payment is not successful:

- The buyer is redirected to the cancel_url mentioned in the Create order request.
- The capture status changes to DENIED .
- The PAYMENT.CAPTURE.DENIED webhook event is triggered, which indicates that the payment capture wasn't successful. You shouldn't fulfill the order.

See [Subscribe to checkout webhooks](/docs/checkout/apm/reference/subscribe-to-webhooks/) for more information.

Here are some additional resources as you create webhook handler code:

- [Webhook Management API](/docs/api/webhooks/v1/) - Manage webhooks, list event notifications, and more.
- Webhook events: - [Checkout webhook events](https://developer.paypal.com/api/rest/webhooks/event-names/#checkout-buyer-approval) - Checkout buyer approval-related webhooks.
- [Order webhook events](https://developer.paypal.com/api/rest/webhooks/event-names/) - Other order-related webhooks.

#### **`Sample PAYMENT.CAPTURE.COMPLETED webhook`**

```javascript
{
  "id": "WH-81H706078A5332206-4WN94402WA949352E",
  "event_version": "1.0",
  "zts": 1481046241,
  "create_time": "2023-10-19T12:18:27.538Z",
  "resource_type": "capture",
  "resource_version": "2.0",
  "event_type": "PAYMENT.CAPTURE.COMPLETED",
  "summary": "Payment completed for EUR 15.39 EUR",
  "resource": {
    "id": "892032536L382192T",
    "amount": {
      "currency_code": "EUR",
      "value": "15.39"
    },
    "final_capture": true,
    "status": "COMPLETED",
    "status_details": {
      "reason": "OTHER"
    },
    "payee": {
      "email_address": "payee@example.com",
      "merchant_id": "1111111111111"
    },
    "create_time": "2023-10-19T11:50:31Z",
    "update_time": "2023-10-19T12:18:22Z",
    "links": [
      {
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/892032536L382192T",
        "rel": "self",
        "method": "GET"
      },
      {
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/892032536L382192T/refund",
        "rel": "refund",
        "method": "POST"
      },
      {
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",
        "rel": "up",
        "method": "GET"
      }
    ]
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-81H706078A5332206-4WN94402WA949352E",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-81H706078A5332206-4WN94402WA949352E/resend",
      "rel": "resend",
      "method": "POST"
    }
  ]
}
```

#### **`Sample PAYMENT.CAPTURE.DENIED webhook`**

```javascript
{
  "id": "WH-1W932300CU741650D-26E32915YU381323H",
  "event_version": "1.0",
  "create_time": "2023-10-19T12:44:23.339Z",
  "resource_type": "capture",
  "resource_version": "2.0",
  "event_type": "PAYMENT.CAPTURE.DENIED",
  "summary": "Payment denied for EUR15.39 EUR",
  "resource": {
    "id": "55X2488039624323N",
    "amount": {
      "currency_code": "EUR",
      "value": "15.39"
    },
    "final_capture": true,
    "invoice_id": "Invoice-12345",
    "custom_id": "Custom-1234",
    "status": "DECLINED",
    "status_details": {
      "reason": "OTHER"
    },
    "supplementary_data": {
      "related_ids": {
        "order_id": "9R480625CB7539041"
      }
    },
    "payee": {
      "email_address": "payee@example.com",
      "merchant_id": "1111111111111"
    },
    "create_time": "2023-10-19T12:43:41Z",
    "update_time": "2023-10-19T12:44:18Z",
    "links": [
      {
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/55X2488039624323N",
        "rel": "self",
        "method": "GET"
      },
      {
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/55X2488039624323N/refund",
        "rel": "refund",
        "method": "POST"
      },
      {
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/9R480625CB7539041",
        "rel": "up",
        "method": "GET"
      }
    ]
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-1W932300CU741650D-26E32915YU381323H",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-1W932300CU741650D-26E32915YU381323H/resend",
      "rel": "resend",
      "method": "POST"
    }
  ]
}
```

**Notes:**- The order ID from [Step 2](#create-an-order) should match the resource.supplementary_data.related_ids.order_id parameter in the webhook payload.

Alternatively, if your app misses the webhook needed to capture the order, you can get the order capture result by sending a GET call to the [Show order details](/docs/api/orders/v2/#orders_get) endpoint of the Orders v2 API.

**Important:** Exercise caution when polling for order capture results using the [Show order details](/docs/api/orders/v2/#orders_get) endpoint. PayPal enforces rate limits on API requests.

A successful request returns the HTTP 200 OK status code with a JSON response body that returns a COMPLETED status.

#### **`Sample request`**

```javascript
curl -v -X GET https://api-m.sandbox.paypal.com/v2/checkout/orders/9R480625CB7539041 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ACCESS-TOKEN"
```

#### **`Sample response`**

```javascript
{
  "id": "5V159329PV571861D",
  "intent": "CAPTURE",
  "status": "COMPLETED",
  "payment_source": {
    "trustly": {
      "name": "Firstname Lastname",
      "country_code": "NL"
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
      "payments": {
        "captures": [
          {
            "id": "5R102774VL663561J",
            "status": "COMPLETED",
            "amount": {
              "currency_code": "EUR",
              "value": "100.00"
            },
            "final_capture": true,
            "seller_receivable_breakdown": {
              "gross_amount": {
                "currency_code": "EUR",
                "value": "100.00"
              },
              "paypal_fee": {
                "currency_code": "EUR",
                "value": "3.80"
              },
              "net_amount": {
                "currency_code": "EUR",
                "value": "96.20"
              }
            },
            "links": [
              {
                "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/55X2488039624323N",
                "rel": "self",
                "method": "GET"
              },
              {
                "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/55X2488039624323N/refund",
                "rel": "refund",
                "method": "POST"
              },
              {
                "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/9R480625CB7539041",
                "rel": "up",
                "method": "GET"
              }
            ]
          }
        ]
      }
    }
  ],
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/55X2488039624323N",
      "rel": "self",
      "method": "GET"
    }
  ]
}
```

#### Step result

A successfully captured order has the following:

- The order status as COMPLETED , which means the order was captured successfully.
- A capture with COMPLETED status is present in the response parameter purchase_units[0].payments.captures[0] .
- The up HATEOAS link indicates the order associated with this capture.

This section shows how to handle payment responses.

### Successful payment

After a successful payment, notify the buyer of a successful transaction. You can do this by sending a confirmation email.

### Unsuccessful payment

If [Step 2](#create-an-order) is unsuccessful and returns an HTTP 422 UNPROCESSABLE_ENTITY status code, the JSON response body should contain an error code in the issue parameter. Use this information to display the appropriate error message to the buyer.

API endpoint used: [Create order](/docs/api/orders/v2/#orders_create)

​

#### **`Sample request`**

```curl
curl -L -X POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer ACCESS-TOKEN' \
-H 'PayPal-Request-Id: PAYPAL-REQUESTID' \
--data-raw '{
  "intent": "CAPTURE",
  "purchase_units": [
    {
      "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
      "amount": {
        "currency_code": "SEK",
        "value": "100.00"
      }
    }
  ],
  "payment_source": {
    "trustly": {
      "country_code": "NL",
      "name": "Firstname Lastname"
    }
  },
  "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
  "application_context": {
    "locale": "en-NL",
    "return_url": "https://example.com/returnUrl",
    "cancel_url": "https://example.com/cancelUrl"
  }
}'
```

#### **`Sample response`**

```javascript
{
  "name": "UNPROCESSABLE_ENTITY",
  "details": [
    {
      "issue": "CURRENCY_NOT_SUPPORTED_BY_PAYMENT_SOURCE",
      "description": "The currency_code provided in the order cannot be processed by the provided payment source."
    }
  ],
  "message": "The requested action could not be performed, semantically incorrect, or failed business validation.",
  "debug_id": "eccdbdf073eea",
  "links": [
    {
      "href": "https://developer.paypal.com/docs/api/orders/v2/#error-CURRENCY_NOT_SUPPORTED_BY_PAYMENT_SOURCE",
      "rel": "information_link",
      "method": "GET"
    }
  ]
}
```

### Step result

An unsuccessful request returns a JSON response body that includes:

- A return status code of 422 Unprocessable Entity .
- An error code in the details.issue parameter.
- An error description in the details.description parameter.

## Next steps

- [Handle uncaptured payments](/docs/checkout/apm/reference/handle-uncaptured-payments/) - Listen for the CHECKOUT.PAYMENT-APPROVAL.REVERSED webhook as an indication that an approved order wasn't captured for certain reasons resulting in a cancellation of the order and a refund the buyer's account. Then notify your buyer of the problem and the reversed order.
- [Test in PayPal sandbox](https://developer.paypal.com/api/rest/sandbox/) .
- [Go live in PayPal's production environment](https://developer.paypal.com/reference/production/) .
