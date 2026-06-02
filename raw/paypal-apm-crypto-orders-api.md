---
title: Integrate crypto payments using Orders API
slug: /docs/checkout/apm/crypto/orders-api/
createTime: "2026-01-13T21:23:21.913Z"
updateTime: "2026-01-29T20:33:42.313Z"
---

# Integrate crypto payments using Orders API

## Onboard crypto payments

- You can enable Pay with crypto using one of the following methods:
- **Enable Pay with crypto from your PayPal dashboard:** If you have an eligible PayPal business account, you can enable Pay with crypto directly from your dashboard: - Log in to your PayPal business account.
- Go to **Account Settings &gt; Products & Services &gt; Payment Methods** .
- Find **Pay with crypto** and select **Get Started** .
- Follow the on-screen prompts to complete onboarding and activate cryptocurrency payments on your accounts.
- Once enabled, go to **Payment Options** to manage your cryptocurrency settings or continue integration.

- **Request approval to enable Pay with crypto:** If you don't see Pay with crypto in your dashboard, request approval by visiting the links below: - **Sandbox:** [http://www.sandbox.paypal.com/bizsignup/add-product?product=CRYPTO_PYMTS](http://www.sandbox.paypal.com/bizsignup/add-product?product=CRYPTO_PYMTS)
- **Live:** [http://www.paypal.com/bizsignup/add-product?product=CRYPTO_PYMTS](http://www.paypal.com/bizsignup/add-product?product=CRYPTO_PYMTS)

- Cryptocurrency payments are activated after PayPal verifies eligibility and completes a compliance review.
  Ensure your account is configured to accept and convert payments to USD, as all cryptocurrency payments are converted and settled in USD.
- Subscribe to the following webhook events to track payment status: - PAYMENT.CAPTURE.COMPLETED - Successful crypto payment.
- PAYMENT.CAPTURE.DENIED - Failed capture.

## End-to-end workflow

![image](assets/paypal-crypto-e2e-workflow.png)

## Present Pay with crypto

Offer Pay with crypto alongside PayPal and other supported payment methods on your checkout page. When the buyer selects Pay with crypto, [create an order](#create-an-order) using the Orders API and [redirect the buyer](#redirect-buyer-for-payment-approval) to PayPal to approve the payment.

## Create an order

Use a valid [access token](https://developer.paypal.com/api/rest/#link-getaccesstoken) and make a POST call to the /v2/checkout/orders endpoint. Use a unique [PayPal-Request-Id](https://developer.paypal.com/api/rest/requests/#link-paypalrequestid) header to prevent duplicate order creation when retrying requests.

Include the following parameters:

| Parameter                                                           | Action                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| processing_instruction Required,string                              | Set toORDER_COMPLETE_ON_PAYMENT_APPROVAL. This value is required for Pay with crypto.                                                                                                                                                                                |
| intent Required,string                                              | Set toCAPTURE. Pay with crypto supports immediate capture only.                                                                                                                                                                                                      |
| purchase_units Required,array                                       | Include the order amount and currency code. The currency code must beUSD.                                                                                                                                                                                            |
| purchase_units.amount Required,object                               | Amount of the order and the currency code. **Note:**USDis the only currency code supported for Pay with crypto.                                                                                                                                                      |
| payment_source Required,object                                      | Include acryptoobjectto specify Pay with crypto as the payment method.                                                                                                                                                                                               |
| payment_source.crypto.country_code Required,string                  | Set toUS.                                                                                                                                                                                                                                                            |
| payment_source.crypto.name Required,object                          | Name of the buyer.                                                                                                                                                                                                                                                   |
| payment_source.crypto.name.given_name Required,string               | Provide the buyer’s first name.                                                                                                                                                                                                                                      |
| payment_source.crypto.name.surname Required,string                  | Provide the buyer’s last name.                                                                                                                                                                                                                                       |
| payment_source.crypto.experience_context.locale string              | Set toen-US.                                                                                                                                                                                                                                                         |
| payment_source.crypto.experience_context.return_url Required,string | Provide the URL to redirect the buyer after payment approval.                                                                                                                                                                                                        |
| payment_source.crypto.experience_context.cancel_url Required,string | Provide the URL to redirect the buyer if the payment is canceled or an error occurs. **Note:**Thecancel_urlis also used if an error occurs during the crypto payment experience, not just for buyer cancellations. Ensure your cancel URL can handle both scenarios. |

For information on all parameters, see the [Orders API](https://developer.paypal.com/docs/api/orders/v2/#orders_create) reference.

#### **`Sample request`**

```javascript
curl -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <ACCESS-TOKEN>' \
  -d '{
        "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
        "intent": "CAPTURE",
        "purchase_units": [
          {
            "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
            "description": "Description of PU1",
            "soft_descriptor": "SOFT-1001",
            "amount": {
              "currency_code": "USD",
              "value": "100.00",
              "breakdown": {
                "item_total": {
                  "currency_code": "USD",
                  "value": "100.00"
                },
                "shipping": {
                  "currency_code": "USD",
                  "value": "0"
                },
                "handling": {
                  "currency_code": "USD",
                  "value": "0"
                },
                "tax_total": {
                  "currency_code": "USD",
                  "value": "0"
                },
                "shipping_discount": {
                  "currency_code": "USD",
                  "value": "0"
                }
              }
            },
            "items": [
              {
                "name": "Item A",
                "category": "PHYSICAL_GOODS",
                "description": "Item A",
                "sku": "259483234816",
                "unit_amount": {
                  "currency_code": "USD",
                  "value": "100"
                },
                "tax": {
                  "currency_code": "USD",
                  "value": "0"
                },
                "quantity": "1"
              }
            ],
            "shipping": {
              "name": {
                "full_name": "John Doe"
              },
              "address": {
                "address_line_1": "2211 N First Street",
                "address_line_2": "Building 17",
                "admin_area_2": "San Jose",
                "admin_area_1": "CA",
                "postal_code": "95131",
                "country_code": "US"
              }
            }
          }
        ],
        "payment_source": {
          "crypto": {
            "country_code": "US",
            "name": {
              "given_name": "John",
              "surname": "Doe"
            },
            "experience_context": {
              "locale": "en-US",
              "return_url": "https://example.com/return",
              "cancel_url": "https://example.com/cancel"
            }
          }
        }
      }'
```

#### **`Sample response`**

```javascript
{
  "id": "5O190127TN364715T",
  "status": "PAYER_ACTION_REQUIRED",
  "links": [
    {
      "href": "https://api-m.paypal.com/v2/checkout/orders/5O190127TN364715T",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://www.paypal.com/payment/crypto?token=5O190127TN364715T",
      "rel": "payer-action",
      "method": "GET"
    }
  ]
}
```

A successful request returns 200 OK response.The response includes the following parameters:

| Parameter | Description                                | Further action                                                                    |
| --------- | ------------------------------------------ | --------------------------------------------------------------------------------- |
| id        | Unique order ID.                           | Store the order ID to track the transaction.                                      |
| status    | Current status of the order.               | When the status isPAYER_ACTION_REQUIRED, redirect the buyer for payment approval. |
| links     | HATEOAS links for available order actions. | Use thepayer-actionlink to redirect the buyer to PayPal to approve the payment.   |

## Redirect buyer for payment approval

- After you create the order, extract the payer-action link from the links array in the [Create order](https://developer.paypal.com/docs/api/orders/v2/#orders_create) response.
- When the buyer selects Pay with crypto, redirect the buyer to the payer-action URL. This opens the PayPal-hosted crypto approval experience. - If the buyer approves the payment: - PayPal automatically captures the payment.
- The buyer is redirected to your return_url .
- The PAYMENT.CAPTURE.COMPLETED webhook is triggered.

- If the buyer cancels or an error occurs: - The buyer is redirected to your cancel_url .
- The PAYMENT.CAPTURE.DENIED webhook is triggered for failed payments.

After creating the order, you can track the payment status in two ways:

- [Use webhooks](#use-webhooks)
- Optional: [Poll for updates](#poll-for-updates)

**Note** : Use webhooks for real-time updates, and poll the order status only if you cannot receive webhooks.

### Use webhooks

To track the payment status using webhooks, follow these steps:

- [Subscribe to webhook events](https://developer.paypal.com/api/rest/webhooks/event-names/) in your PayPal developer dashboard or through the Webhooks API. For example: - PAYMENT.CAPTURE.COMPLETED – Successful payment capture
- PAYMENT.CAPTURE.DENIED – Failed payment capture

- Define a webhook handler in your server-side application to: - [Listen for incoming webhook events](https://developer.paypal.com/api/rest/webhooks/rest/#link-subscribingalistenerurl) .
- [Confirm receipt of the event to PayPal](https://developer.paypal.com/api/rest/webhooks/#link-receivingthemessage) .
- [Verify the source of the event notification](https://developer.paypal.com/api/rest/webhooks/#link-verifyingthemessagereceived) .
- Complete further actions based on event data.

**Note** : If needed, use the [List event notifications](/docs/api/webhooks/v1/#webhooks-events_list) API to retrieve all webhook events or the [Show event notification details](/docs/api/webhooks/v1/#webhooks-events_get) API to get specific event details.

The following example shows a webhook payload for a completed crypto payment:

#### **`Sample PAYMENT.CAPTURE.COMPLETED`**

```javascript
{
  "id": "WH-2B342482FC0449155-12X09416XP387753C",
  "event_version": "1.0",
  "zts": 1481046241,
  "create_time": "2022-04-08T10:37:05Z",
  "resource_type": "capture",
  "resource_version": "2.0",
  "event_type": "PAYMENT.CAPTURE.COMPLETED",
  "summary": "Payment completed for USD 1.00 USD",
  "resource": {
    "amount": {
      "value": "1.00",
      "currency_code": "USD"
    },
    "create_time": "2022-04-08T10:37:05Z",
    "update_time": "2022-04-08T10:37:05Z",
    "final_capture": true,
    "seller_receivable_breakdown": {
      "paypal_fee": {
        "value": "0.20",
        "currency_code": "USD"
      },
      "gross_amount": {
        "value": "1.00",
        "currency_code": "USD"
      },
      "net_amount": {
        "value": "0.80",
        "currency_code": "USD"
      }
    },
    "links": [
      {
        "method": "GET",
        "rel": "self",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/8SS60826HT082593F"
      },
      {
        "method": "POST",
        "rel": "refund",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/8SS60826HT082593F/refund"
      },
      {
        "method": "GET",
        "rel": "up",
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5KP92830L1747245S"
      }
    ],
    "id": "8SS60826HT082593F",
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

This webhook provides real-time notifications to track and respond to crypto payment status changes.

Extract the order ID from the "rel": "up" link in the webhook payload's resource.links array to correlate the capture to your original order.

### Poll for updates (optional)

**Note** : Be aware of PayPal's API rate limits when polling for order status. For best practices and details, see the [Rate limiting guideline](https://developer.paypal.com/reference/guidelines/rate-limiting/) .

Use a valid [access token](https://developer.paypal.com/api/rest/#link-getaccesstoken) and make a GET call to the /v2/checkout/orders/{id} endpoint. Include the following path parameter:

| Parameter | Action                                                 |
| --------- | ------------------------------------------------------ |
| id        | Unique order ID returned in the Create order response. |

A successful call returns a 200 OK response. The response includes the following parameters:

| Parameter      | Description                                                          | Further action                                                     |
| -------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------ |
| id             | Unique order ID.                                                     | Use this value to correlate the response with your original order. |
| status         | Current status of the order.                                         | When the status isCOMPLETED, the payment capture is successful.    |
| purchase_units | List of purchase units for the order, including amount and currency. | Use as needed to reference order details.                          |
| payer          | Information about the buyer, including name and payer ID.            | Optional. Use for display or record-keeping if needed.             |

For information on all response parameters, see [Show order details](https://developer.paypal.com/docs/api/orders/v2/#orders_get) .

## Notify buyer of payment success

After a successful cryptocurrency (crypto) payment, notify the buyer of the completed transaction.
You can do this by sending a confirmation email or displaying a success message to the buyer.

### Issue a full refund

Use a valid [access token](https://developer.paypal.com/api/rest/#link-getaccesstoken) and make a POST call to the /v2/payments/captures/{capture_id}/refund with an empty request body.

| Parameter  | Action                                                                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| capture_id | Unique identifier for the payment capture. This value is available inpurchase_units[].payments.captures[].idfrom the completed order response. |

A successful call returns a 201 Created response with the refund details. For information on all response parameters, see the [Refunds API](https://developer.paypal.com/docs/api/payments/v2/#captures_refund) reference.

#### **`Full refund`**

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/payments/captures/{capture_id}/refund \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ACCESS-TOKEN" \
  -H "PayPal-Request-Id: YOUR-PAYPAL-REQUEST-ID" \
  -H "PayPal-Auth-Assertion: PAYPAL-AUTH-ASSERTION" \
  -H "PayPal-Partner-Attribution-Id: BN-CODE" \
  -d '{}'

```

### Issue a partial refund

Use a valid [access token](https://developer.paypal.com/api/rest/#link-getaccesstoken) and make a POST call to the /v2/payments/captures/{capture_id}/refund endpoint. Include the refund amount in the request body to issue a partial refund. You can issue multiple partial refunds for a single capture, as long as the total refunded amount does not exceed the original captured amount.

For information on all request and response parameters, see the [Refunds API](https://developer.paypal.com/docs/api/payments/v2/#captures_refund) reference.

#### **`Partial refund`**

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/payments/captures/{capture_id}/refund \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ACCESS-TOKEN" \
  -H "PayPal-Request-Id: YOUR-PAYPAL-REQUEST-ID" \
  -H "PayPal-Auth-Assertion: PAYPAL-AUTH-ASSERTION" \
  -H "PayPal-Partner-Attribution-Id: BN-CODE" \
  -d '{
    "amount": {
      "value": "10.99",
      "currency_code": "USD"
    }
  }'

```

When a crypto payment fails, PayPal sends webhook notifications to inform your system of the failure.

**Webhook events to subscribe to:**

- PAYMENT.CAPTURE.DENIED : Payment capture failed after buyer approval
- CHECKOUT.ORDER.DECLINED : Order declined during payment processing

### Sample webhook payloads

#### **`Sample PAYMENT.CAPTURE.DENIED`**

```javascript
{
  "id": "WH-2B342482FC0449155-12X09416XP387753C",
  "event_version": "1.0",
  "create_time": "2022-04-08T10:37:05Z",
  "resource_type": "capture",
  "resource_version": "2.0",
  "event_type": "PAYMENT.CAPTURE.DENIED",
  "summary": "Payment denied for USD 1.00 USD",
  "resource": {
    "amount": {
      "value": "1.00",
      "currency_code": "USD"
    },
    "supplementary_data": {
      "related_ids": {
        "order_id": "5KP92830L1747245S"
      }
    },
    "create_time": "2022-04-08T10:37:05Z",
    "update_time": "2022-04-08T10:37:05Z",
    "final_capture": true,
    "seller_receivable_breakdown": {
      "paypal_fee": {
        "value": "0.20",
        "currency_code": "USD"
      },
      "gross_amount": {
        "value": "1.00",
        "currency_code": "USD"
      },
      "net_amount": {
        "value": "0.80",
        "currency_code": "USD"
      }
    },
    "links": [
      {
        "method": "GET",
        "rel": "self",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/8SS60826HT082593F"
      },
      {
        "method": "POST",
        "rel": "refund",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/8SS60826HT082593F/refund"
      },
      {
        "method": "GET",
        "rel": "up",
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5KP92830L1747245S"
      }
    ],
    "id": "8SS60826HT082593F",
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
  "create_time": "2022-04-08T10:37:05Z",
  "resource_type": "checkout-order",
  "resource_version": "2.0",
  "event_type": "CHECKOUT.ORDER.DECLINED",
  "summary": "An order has been declined",
  "resource": {
    "create_time": "2022-04-08T10:37:05Z",
    "purchase_units": [
      {
        "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
        "amount": {
          "currency_code": "USD",
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
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5KP92830L1747245S",
        "rel": "self",
        "method": "GET"
      }
    ],
    "id": "5KP92830L1747245S",
    "payment_source": {
  "crypto":  {
    "name": {
      "given_name": "Firstname",
      "surname": "Lastname"
    },
    "country_code": "US"
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

**If a payment fails:**

- PayPal automatically redirects buyers to your cancel_url . When buyers are redirected to your cancel URL due to payment failures, PayPal appends error codes as query parameters. For more information on error codes, see [Error codes](/docs/checkout/apm/reference/error-codes/) reference.
- PayPal sends webhook notifications with failure details.
- Review the purchase_units[].most_recent_errors parameter in the webhook payload to identify the failure reason.
- Handle the error on your cancel page by displaying a relevant message or offering next steps.

## Next steps

### Test integration

Test the integration in the PayPal sandbox environment.

### Go live

Take your application live in the PayPal production environment once testing is successful.
