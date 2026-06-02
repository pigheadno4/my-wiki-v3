<!-- Source URL: https://developer.paypal.com/docs/checkout/apm/ideal/orders-api/ -->
<!-- Fetched: 2026-04-14 -->
<!-- Last updated per source: Jul 28th (year not specified) -->

---
title: Integrate iDEAL using the Orders API
slug: /docs/checkout/apm/ideal/orders-api/
---

# Integrate iDEAL using the Orders API

Render payment buttons and process payments with the Orders API.

## Know before you code

- Request approval to enable iDEAL by visiting these sandbox and live links:
  - Sandbox: https://www.sandbox.paypal.com/bizsignup/entry?product=ideal&capabilities=IDEAL&country.x=<merchant's country>
  - Live: https://www.paypal.com/bizsignup/entry?product=ideal&capabilities=IDEAL&country.x=<merchant's country>
- Partners: Be sure to onboard your merchants upfront, before they accept payments. Onboarding after making payments, specifically Progressive Onboarding, isn't supported for alternative payment methods.
  - **Note:** The integration steps for implementing alternative payment methods are similar. If you've integrated another alternative payment method before, you can likely reuse that code with adjustments for this payment method.
- Make sure you're subscribed to the following webhook events:
  - PAYMENT.CAPTURE.COMPLETED - Listen for this webhook to get notified about a successful order capture.
  - PAYMENT.CAPTURE.DENIED - This webhook tells you when an order capture fails.
- Make sure your preference for receiving payments in your PayPal business or merchant account is set to accept and convert to the currency in your account. In your profile, select **Account Settings** > **Payment preferences** > **Block payments** and click **Update** to mark this preference.
- Request approval to enable iDEAL by visiting these sandbox and live links. Replace MERCHANT-COUNTRY in the URL with the 2-character country code for the merchant's country of operation:
  - Sandbox: https://www.sandbox.paypal.com/bizsignup/entry?product=ideal&capabilities=IDEAL&country.x=MERCHANT-COUNTRY
  - Live: https://www.paypal.com/bizsignup/entry?product=ideal&capabilities=IDEAL&country.x=MERCHANT-COUNTRY
- When processing iDEAL payments, you don't need to capture payment for the order.

## 1. Offer iDEAL on the checkout page

You'll need to create the user interface to offer banks through iDEAL and collect the buyer's information, then you'll use the API calls described in the remainder of this topic to:

- Create the order with buyer's full_name, country_code and iDEAL as the payment source.
- Redirect the buyer to iDEAL.

Refer to Payment method icons for icons you can use and download locations.

## 2. Create an order

Use the buyer information you captured from your user interface to create an order with iDEAL as the payment source.

API endpoint used in Sample request: Create order

### Sample request

```curl
curl -v -X POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders' \
-H "PayPal-Request-Id: PAYPAL-REQUEST-ID" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ACCESS-TOKEN" \
-d '{
    "intent": "CAPTURE",
    "purchase_units": [
        {
            "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
            "amount": {
                "currency_code": "EUR",
                "value": "1.00"
              }
          }
    ],
    "payment_source": {
        "ideal": {
            "country_code": "NL",
            "name": "Firstname Lastname"
        }
    }
}'
```

### Sample response

```javascript
{
  "id": "ORDER-ID",
  "status": "PAYER_ACTION_REQUIRED",
  "payment_source": {
    "ideal": {
      "name": "Firstname Lastname",
      "country_code": "NL"
    }
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/ORDER-ID",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://www.sandbox.paypal.com/payment/ideal?token=ORDER-ID",
      "rel": "payer-action",
      "method": "GET"
    }
  ]
}
```

### Modify the code

After you copy the code in the sample request, modify the following:

- ACCESS-TOKEN - Your access token.
- PayPal-Request-Id - Replace the sample ID with a unique ID you generate. This ID helps prevent duplicate authorizations in the event that the API call is disrupted. See also: API idempotency
- intent - To use an alternative payment method, this parameter must be set to CAPTURE as it is in this sample code.
- payment_source - Specify ideal as the payment method and include the country code and account holder's full name.
- purchase_units.amount - Pass the amount of the order and the currency code.
- processing_instruction - Set this value to ORDER_COMPLETE_ON_PAYMENT_APPROVAL as it is in this sample code.
- application_context - Specify the preferred language for returned errors, the URL the buyer is returned to after approving the purchase with their selected payment method, and the URL the buyer is returned to after canceling an approval with their selected payment method. While return_url and cancel_url are optional fields, this integration requires you specify them to handle the handoff from the payment method back to your site.

**Note:** Change or add other parameters in the Create order request body to create an order that reflects the actual order details.

### Step result

A successful request results in the following:

- A return status code of HTTP 200 OK.
- A JSON response body that contains the order ID. You'll use the order ID and payer-action HATEOAS URL in the next step.

### Merchant onboarding payment error

Partners need to onboard merchants upfront before they accept payments. iDEAL doesn't support onboarding after making payments, specifically Progressive Onboarding.

When you submit an order with ideal as the payment_source, and the merchant isn't onboarded, you get the following error message:

The 'API caller' and/or 'payee' is not set up to be able to process the selected payment source. If you have already completed the required steps, please allow 2 business days for PayPal to complete the setup. If you continue to receive this error, please contact your Account Manager or check status at https://www.paypal.com/businessmanage/account/payments.

### Unsuccessful confirm order request

This code sample shows an unsuccessful attempt to confirm an order without a properly onboarded merchant.

API endpoint used in the sample request: Create order

#### Sample request

```curl
curl -v -X POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders/ORDER-ID/confirm-payment-source' \
-H "PayPal-Request-Id: PAYPAL-REQUEST-ID" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ACCESS-TOKEN" \
-d '{
    "payment_source": {
        "ideal": {
            "country_code": "NL",
            "name": "Firstname Lastname",
            "experience_context": {
                "return_url": "https://example.com/return",
                "cancel_url": "https://example.com/cancel"
            }
        }
    }
}'
```

#### Sample response

```javascript
{
  "name": "UNPROCESSABLE_ENTITY",
  "details": [
    {
      "issue": "NOT_ENABLED_FOR_PAYMENT_SOURCE",
      "description": "The 'API caller' and/or 'payee' is not setup to be able to process the selected payment source. If you have already completed the required steps, please allow 2 business days for PayPal to complete the setup. If you continue to receive this error, please contact your Account Manager or check status at https://www.paypal.com/businessmanage/account/payments.",
      "fields": [
        {
          "field": "/payment_source/ideal"
        }
      ]
    }
  ],
  "message": "The requested action could not be performed, semantically incorrect, or failed business validation.",
  "debug_id": "90957fca61718",
  "links": [
    {
      "href": "https://developer.paypal.com/api/orders/v2/#error-NOT_ENABLED_FOR_PAYMENT_SOURCE",
      "rel": "information_link",
      "method": "GET"
    }
  ]
}
```

Step result: HTTP 422 Unprocessable Entity — NOT_ENABLED_FOR_PAYMENT_SOURCE.

### Unsuccessful single-shot create order request

This code sample shows an unsuccessful attempt to create a new order and capture the payment without a properly onboarded merchant.

#### Sample request

```curl
curl -v -X POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders' \
-H "PayPal-Request-Id: PAYPAL-REQUEST-ID" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ACCESS-TOKEN" \
-d '{
        "intent": "CAPTURE",
        "payment_source": {
            "ideal": {
                "country_code": "NL",
                "name": "Firstname Lastname",
                "experience_context": {
                    "return_url": "https://example.com/return",
                    "cancel_url": "https://example.com/cancel"
                }
            }
        },
        "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
        "purchase_units": [
            {
                "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
                "amount": {
                    "currency_code": "EUR",
                    "value": "100"
                }
            }
        ]
    }'
```

Step result: HTTP 422 Unprocessable Entity — NOT_ENABLED_FOR_PAYMENT_SOURCE.

## 3. Redirect buyer for purchase approval

In your user interface, attach the payer-action redirect URL returned in the Create Order response to the iDEAL payment button. This sends the buyer to their bank to approve the purchase. Once the buyer approves the purchase, the payment is automatically captured.

In the sample, the redirect URL is: "https://www.sandbox.paypal.com/payment/ideal?token=5KP92830L1747245S".

### Step result

After successfully completing the bank approval:

- The buyer is redirected to the return_url mentioned in the Create Order request.
- The PAYMENT.CAPTURE.COMPLETED webhook event is triggered, which indicates that payment capture was successful.

After unsuccessful bank approval:

- The buyer is redirected to the cancel_url mentioned in the Create Order request.

## 4. Listen to webhooks for payment status

Listen to the following webhooks to get the result of order capture:

- The PAYMENT.CAPTURE.COMPLETED webhook event indicates a successful order capture.
- The PAYMENT.CAPTURE.DENIED webhook events indicate a failed order capture.
- Optional: Use Show order details endpoint to determine the status of an order. The up HATEOAS link indicates the order associated with this capture.

See Subscribe to checkout webhooks for more information.

Additional resources:

- Webhook Management API - Manage webhooks, list event notifications, and more.
- Checkout webhook events - Checkout buyer approval-related webhooks.
- Order webhook events - Other order-related webhooks.
- Show order details endpoint - Determine the status of an order.

### Sample PAYMENT.CAPTURE.COMPLETED webhook

```javascript
{
  "id": "WH-2B342482FC0449155-12X09416XP387753C",
  "event_version": "1.0",
  "zts": 1481046241,
  "create_time": "2022-04-08T10:37:05Z",
  "resource_type": "capture",
  "resource_version": "2.0",
  "event_type": "PAYMENT.CAPTURE.COMPLETED",
  "summary": "Payment completed for EUR 1.00 EUR",
  "resource": {
    "amount": { "value": "1.00", "currency_code": "EUR" },
    "create_time": "2022-04-08T10:37:05Z",
    "update_time": "2022-04-08T10:37:05Z",
    "final_capture": true,
    "seller_receivable_breakdown": {
      "paypal_fee": { "value": "0.20", "currency_code": "EUR" },
      "gross_amount": { "value": "1.00", "currency_code": "EUR" },
      "net_amount": { "value": "0.80", "currency_code": "EUR" }
    },
    "links": [
      { "method": "GET", "rel": "self", "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/8SS60826HT082593F" },
      { "method": "POST", "rel": "refund", "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/8SS60826HT082593F/refund" },
      { "method": "GET", "rel": "up", "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5KP92830L1747245S" }
    ],
    "id": "8SS60826HT082593F",
    "status": "COMPLETED"
  },
  "links": [
    { "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-2B342482FC0449155-12X09416XP387753C", "rel": "self", "method": "GET" },
    { "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-2B342482FC0449155-12X09416XP387753C/resend", "rel": "resend", "method": "POST" }
  ]
}
```

### Sample PAYMENT.CAPTURE.DENIED webhook

```javascript
{
  "id": "WH-2B342482FC0449155-12X09416XP387753C",
  "event_type": "PAYMENT.CAPTURE.DENIED",
  "summary": "Payment denied for EUR 1.00 EUR",
  "resource": {
    "amount": { "value": "1.00", "currency_code": "EUR" },
    "supplementary_data": { "related_ids": { "order_id": "5KP92830L1747245S" } },
    "id": "8SS60826HT082593F",
    "status": "DECLINED"
  }
}
```

### Sample CHECKOUT.ORDER.DECLINED webhook

```javascript
{
  "event_type": "CHECKOUT.ORDER.DECLINED",
  "summary": "An order has been declined",
  "resource": {
    "purchase_units": [
      {
        "most_recent_errors": [
          {
            "issue": "PAYMENT_SOURCE_CANNOT_BE_USED",
            "description": "The provided payment source cannot be used to pay for the order. Please try again with a different payment source by creating a new order."
          }
        ]
      }
    ],
    "payment_source": { "ideal": { "name": "Firstname Lastname", "country_code": "NL" } },
    "id": "5KP92830L1747245S",
    "status": "PAYER_ACTION_REQUIRED"
  }
}
```

**Notes:**

- order ID from Step 2 should match resource.supplementary_data.related_ids.order_id parameter in the webhook payload.
- When an order is declined, the CHECKOUT.ORDER.DECLINED webhook passes the error code and message in the most_recent_error parameter of the purchase_unit object.

Alternatively, if your app misses the webhook, you can poll using GET /v2/checkout/orders/{id}. **Important:** PayPal enforces rate limits on API requests.

### Sample polling request

```curl
curl -v -X GET https://api-m.sandbox.paypal.com/v2/checkout/orders/5KP92830L1747245S \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer <Access-Token>"
```

### Sample polling response

```javascript
{
  "id": "5KP92830L1747245S",
  "intent": "CAPTURE",
  "status": "COMPLETED",
  "payment_source": {
    "ideal": { "name": "Firstname Lastname", "country_code": "NL" }
  },
  "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
  "purchase_units": [
    {
      "payments": {
        "captures": [
          {
            "id": "8SS60826HT082593F",
            "status": "COMPLETED",
            "amount": { "currency_code": "EUR", "value": "1.00" },
            "final_capture": true
          }
        ]
      }
    }
  ]
}
```

## 5. Notify buyer of payment success

After a successful payment, notify the buyer of a successful transaction. You can do this by sending a confirmation email.
