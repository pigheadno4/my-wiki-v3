---
title: Integrate Swish using the Orders API
slug: /docs/checkout/apm/swish/orders-api/
createTime: "2025-11-03T21:04:33.315Z"
updateTime: "2026-03-31T10:36:16.248Z"
---

# Integrate Swish using the Orders API

## Set up

Before you onboard Swish, verify you have completed the following PayPal integration steps:

- [Sign up for a PayPal developer account](https://developer.paypal.com/) . On successful signup, PayPal automatically creates your sandbox environment. The sandbox environment mimics real-world transactions and includes both business and personal accounts by default. Use the personal account to approve payments and the business account to receive money. You can create additional business and personal accounts as needed.
- [Set up the sandbox environment](https://developer.paypal.com/tools/sandbox/) .
- Configure a webhook listener for the app and subscribe to events: - In the app details page, go to **Sandbox Webhooks** .
- Select **Add Webhook** .
- Enter a Webhook URL (your server endpoint for PayPal notifications), select the events to subscribe to, and select **Save** .

  The webhook listener is now configured, and a Webhook ID is displayed. Store the ID for verification in your app code. For more information, see [Use webhooks](/limited-release/alternative-payment-methods/klarna/accept-klarna-payments/track-payment-status/#use-webhooks) .

- [Retrieve sandbox app credentials](https://developer.paypal.com/api/rest/#link-getsandboxaccountcredentials) **.**
- [Retrieve sandbox account credentials](https://developer.paypal.com/api/rest/#link-getsandboxaccountcredentials) .
- [Set up the development environment](https://developer.paypal.com/studio/checkout/advanced/getstarted#setup-dev-environment) .
- [Set up your production environment](https://developer.paypal.com/api/rest/production/) .

## Onboard Swish payments

After you complete your PayPal account setup, enable Swish as a payment method.

You can enable Swish using one of the following methods:

- [Enable Swish from your PayPal dashboard](enable-swish) .
- [Request approval to enable Swish](request-approval) .

### Enable Swish from your PayPal dashboard

If you have an eligible PayPal business account, you can enable Swish directly from your dashboard:

- Log in to your PayPal business account.
- Go to **Account Settings** &gt; **Products & Services** &gt; **Payment Methods** .
- Find **Swish** and select **Get Started** .
- Follow the on-screen prompts to complete onboarding and activate Swish payments.

After enabling, go to **Payment Options** to manage your Swish settings.

### Request approval to enable Swish

If you don't see Swish in your dashboard, request approval by visiting the links below:

- Sandbox:
- Live:

Swish payments are activated after PayPal verifies eligibility and completes a compliance review.

## Create order

Create an order to begin the Swish payment process. You can configure the order by following these steps:

- [Choose buyer flow](https://developer.paypal.com/docs/ecm/aKlUUHXf4XlbwLl3AlsVYn/#buyer-flows) : Select QR code flow for desktop or mobile app switch for mobile devices.
- **Set capture method** : Choose automatic for immediate capture or manual for delayed capture.
- **Create the order** : Make the POST call to /v2/checkout/orders endpoint with one of the following configurations: - [QR code flow with automatic capture](#qr-code-auto-capture)
- [QR code flow with manual capture](#qr-code-manual-capture)
- [Mobile app switch with automatic capture](#app-switch-automatic-capture)
- [Mobile app switch with manual capture](#app-switch-manual-capture)

- **Handle the response** : Use the order response based on your [integration pattern](https://developer.paypal.com/docs/ecm/aKlUUHXf4XlbwLl3AlsVYn/#integration-patterns) .

## Create order with QR code flow

Use this flow for desktop browsers where buyers scan a QR code with their mobile device. Use a valid access token and make the POST call to /v2/checkout/orders endpoint with request body parameters including intent set to CAPTURE , purchase_units with amount and currency_code , payment_source.swish object, and the PayPal-Request-Id header for idempotency.

### Automatic capture

Set processing_instruction to ORDER_COMPLETE_ON_PAYMENT_APPROVAL . Funds are captured immediately after buyer approval.

#### **`Sample request`**

```javascript
curl -v -L -s -X POST https://api.paypal.com/v2/checkout/orders \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -H 'PayPal-Request-Id: UNIQUE-REQUEST-ID' \
  -d '{
    "intent": "CAPTURE",
    "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
    "payment_source": {
      "swish": {
        "name": "Jhon Doe",
        "country_code": "SE",
        "experience_context": {
          "locale": "sv-SE",
          "return_url": "http://www.bing.com",
          "cancel_url": "http://www.google.com"
        }
      }
    },
    "payer": {
      "email_address": "aisjdi@paypal.com",
      "first_name": "John1",
      "last_name": "Doe1",
      "country_code": "SE",
      "phone": {
        "phone_type": "MOBILE",
        "phone_number": {
          "national_number": "1238712837"
        }
      }
    },
    "purchase_units": [
      {
        "invoice_id": "Invoice-123456",
        "custom_id": "Custom-12345",
        "amount": {
          "currency_code": "SEK",
          "value": "100"
        }
      }
    ]
  }'
```

#### **`Sample response`**

```javascript
{
  "id": "5SJ83317D1020641R",
  "intent": "CAPTURE",
  "status": "PAYER_ACTION_REQUIRED",
  "payment_source": {
    "swish": {
      "name": "Jhon Doe",
      "country_code": "SE",
      "qr_details": {
        "qr_image": "iVBORw0KGgoAAAANSUhEUgAAASwAAAEsCAYAAAB5fY51AAAsHElEQVR4Xu2d...",
        "qr_payload": "DAAAAAAAAAAAAABUBYSCZhfdFeowkFWSd"
      }
    }
  },
  "purchase_units": [
    {
      "reference_id": "default",
      "amount": {
        "currency_code": "SEK",
        "value": "100.00"
      },
      "payee": {
        "email_address": "merchant@example.com",
        "merchant_id": "MERCHANTID123"
      },
      "custom_id": "Custom-12345",
      "invoice_id": "Invoice-123456"
    }
  ],
  "links": [
    {
      "href": "https://api.paypal.com/v2/checkout/orders/5SJ83317D1020641R",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://www.paypal.com/payment/swish?token=5SJ83317D1020641R",
      "rel": "payer-action",
      "method": "GET"
    }
  ]
}
```

After receiving the response, redirect the buyer to complete payment approval. The payment captures automatically after buyer approval.

### Manual capture

For manual capture, exclude the processing_instruction parameter or set it to NO_INSTRUCTION . When the buyer approves the payment, [capture the payment](https://developer.paypal.com/docs/ecm/9sq0yTutQOXbfxdVSKoyIX/#capture-payment) to complete the transaction.

#### **`Sample request`**

```javascript
curl -v -L -s -X POST https://api.paypal.com/v2/checkout/orders \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -H 'PayPal-Request-Id: UNIQUE-REQUEST-ID' \
  -d '{
    "intent": "CAPTURE",
    "payment_source": {
      "swish": {
        "name": "Jhon Doe",
        "country_code": "SE",
        "experience_context": {
          "locale": "sv-SE",
          "return_url": "http://www.bing.com",
          "cancel_url": "http://www.google.com"
        }
      }
    },
    "payer": {
      "email_address": "aisjdi@paypal.com",
      "first_name": "John1",
      "last_name": "Doe1",
      "country_code": "SE",
      "phone": {
        "phone_type": "MOBILE",
        "phone_number": {
          "national_number": "1238712837"
        }
      }
    },
    "purchase_units": [
      {
        "invoice_id": "Invoice-123456",
        "custom_id": "Custom-12345",
        "amount": {
          "currency_code": "SEK",
          "value": "100"
        }
      }
    ]
  }'
```

#### **`Sample response`**

```javascript
{
  "id": "5SJ83317D1020641R",
  "intent": "CAPTURE",
  "status": "PAYER_ACTION_REQUIRED",
  "payment_source": {
    "swish": {
      "name": "Jhon Doe",
      "country_code": "SE",
      "qr_details": {
        "qr_image": "iVBORw0KGgoAAAANSUhEUgAAASwAAAEsCAYAAAB5fY51AAAsHElEQVR4Xu2d...",
        "qr_payload": "DAAAAAAAAAAAAABUBYSCZhfdFeowkFWSd"
      }
    }
  },
  "purchase_units": [
    {
      "reference_id": "default",
      "amount": {
        "currency_code": "SEK",
        "value": "100.00"
      },
      "payee": {
        "email_address": "merchant@example.com",
        "merchant_id": "MERCHANTID123"
      },
      "custom_id": "Custom-12345",
      "invoice_id": "Invoice-123456"
    }
  ],
  "links": [
    {
      "href": "https://api.paypal.com/v2/checkout/orders/5SJ83317D1020641R",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://www.paypal.com/payment/swish?token=5SJ83317D1020641R",
      "rel": "payer-action",
      "method": "GET"
    }
  ]
}
```

After receiving the response, redirect the buyer to complete payment approval, then capture the payment after buyer approval.

## Create order with mobile app switch flow

Use this flow for mobile browsers where buyers switch to the Swish app on the same device. Use a valid access token and make the POST call to /v2/checkout/orders with request body parameters including intent set to CAPTURE , purchase_units with amount and currency_code , payment_source.swish object with country_code set to SE and redirect_to_app set to true , and the PayPal-Request-Id header for idempotency.

### Automatic capture

Set processing_instruction to ORDER_COMPLETE_ON_PAYMENT_APPROVAL . Funds are captured immediately after buyer approval.

#### **`Sample request`**

```javascript
curl -v -L -s -X POST https://api.paypal.com/v2/checkout/orders \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -H 'PayPal-Request-Id: UNIQUE-REQUEST-ID' \
  -d '{
    "intent": "CAPTURE",
    "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
    "payment_source": {
      "swish": {
        "name": "Jhon Doe",
        "country_code": "SE",
        "experience_context": {
          "locale": "sv-SE",
          "return_url": "http://www.bing.com",
          "redirect_to_app": true
        }
      }
    },
    "payer": {
      "email_address": "aisjdi@paypal.com",
      "first_name": "John1",
      "last_name": "Doe1",
      "country_code": "SE",
      "phone": {
        "phone_type": "MOBILE",
        "phone_number": {
          "national_number": "1238712837"
        }
      }
    },
    "purchase_units": [
      {
        "invoice_id": "Invoice-123456",
        "custom_id": "Custom-12345",
        "amount": {
          "currency_code": "SEK",
          "value": "100"
        }
      }
    ]
  }'
```

#### **`Sample response`**

```javascript
{
  "id": "1KA50940BL2603246",
  "intent": "CAPTURE",
  "status": "PAYER_ACTION_REQUIRED",
  "payment_source": {
    "swish": {
      "name": "Jhon Doe",
      "country_code": "SE",
      "qr_details": {
        "qr_image": "iVBORw0KGgoAAAANSUhEUgAAASwAAAEsCAYAAAB5fY51AAAsHElEQVR4Xu2d...",
        "qr_payload": "DAAAAAAAAAAAAABUBYSCZhfdFeowkFWSd"
      }
    }
  },
  "purchase_units": [
    {
      "reference_id": "default",
      "amount": {
        "currency_code": "SEK",
        "value": "100.00"
      },
      "payee": {
        "email_address": "merchant@example.com",
        "merchant_id": "MERCHANTID123"
      },
      "custom_id": "Custom-12345",
      "invoice_id": "Invoice-123456"
    }
  ],
  "links": [
    {
      "href": "https://api.paypal.com/v2/checkout/orders/1KA50940BL2603246",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "swish://paymentrequest?token=AAAAAAAAAAAAABUBYSCZhfdFeowkFWSd&callbackurl=https%3A%2F%2Fexample.com%2Freturn",
      "rel": "payer-action",
      "method": "GET"
    }
  ]
}
```

After receiving the response, redirect the buyer to complete payment approval. The payment captures automatically after buyer approval.

### Manual capture

For manual capture, exclude the processing_instruction parameter or set it to NO_INSTRUCTION . When the buyer approves the payment, [capture the payment](https://developer.paypal.com/docs/ecm/9sq0yTutQOXbfxdVSKoyIX/#capture-payment) to complete the transaction.

#### **`Sample request`**

```javascript
curl -v -L -s -X POST https://api.paypal.com/v2/checkout/orders \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -H 'PayPal-Request-Id: UNIQUE-REQUEST-ID' \
  -d '{
    "intent": "CAPTURE",
    "payment_source": {
      "swish": {
        "name": "Jhon Doe",
        "country_code": "SE",
        "experience_context": {
          "locale": "sv-SE",
          "return_url": "http://www.bing.com",
          "redirect_to_app": true
        }
      }
    },
    "payer": {
      "email_address": "aisjdi@paypal.com",
      "first_name": "John1",
      "last_name": "Doe1",
      "country_code": "SE",
      "phone": {
        "phone_type": "MOBILE",
        "phone_number": {
          "national_number": "1238712837"
        }
      }
    },
    "purchase_units": [
      {
        "invoice_id": "Invoice-123456",
        "custom_id": "Custom-12345",
        "amount": {
          "currency_code": "SEK",
          "value": "100"
        }
      }
    ]
  }'
```

#### **`Sample response`**

```javascript
{
  "id": "1KA50940BL2603246",
  "intent": "CAPTURE",
  "status": "PAYER_ACTION_REQUIRED",
  "payment_source": {
    "swish": {
      "name": "Jhon Doe",
      "country_code": "SE",
      "qr_details": {
        "qr_image": "iVBORw0KGgoAAAANSUhEUgAAASwAAAEsCAYAAAB5fY51AAAsHElEQVR4Xu2d...",
        "qr_payload": "DAAAAAAAAAAAAABUBYSCZhfdFeowkFWSd"
      }
    }
  },
  "purchase_units": [
    {
      "reference_id": "default",
      "amount": {
        "currency_code": "SEK",
        "value": "100.00"
      },
      "payee": {
        "email_address": "merchant@example.com",
        "merchant_id": "MERCHANTID123"
      },
      "custom_id": "Custom-12345",
      "invoice_id": "Invoice-123456"
    }
  ],
  "links": [
    {
      "href": "https://api.paypal.com/v2/checkout/orders/1KA50940BL2603246",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "swish://paymentrequest?token=AAAAAAAAAAAAABUBYSCZhfdFeowkFWSd&callbackurl=https%3A%2F%2Fexample.com%2Freturn",
      "rel": "payer-action",
      "method": "GET"
    }
  ]
}
```

After receiving the response, redirect the buyer to complete payment approval, then capture the payment after buyer approval.

### Request body parameters

| Parameter name                                                     | Description                                                                                                                                                                |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| processing_instruction string                                      | Specifies how the order is processed. For automatic capture, set toORDER_COMPLETE_ON_PAYMENT_APPROVAL. For manual capture, exclude this parameter or set toNO_INSTRUCTION. |
| intent Required,string                                             | Indicates whether payment is captured immediately or authorized for later capture. For Swish payments, set toCAPTURE.                                                      |
| purchase_units Required,array                                      | Lists the items or services the buyer is purchasing in the order.                                                                                                          |
| purchase_units.amount Required,object                              | Amount of the order and the currency code. For Swish payments, useSEKcurrency.                                                                                             |
| payment_source Required,object                                     | Payment method used to fund the order. For Swish payments, include aswishobject with buyer and experience context information.                                             |
| payment_source.swish.country_code Required,string                  | Country code required for Swish payments, specified in the ISO 3166-1 format. For Swish payments, set toSE.                                                                |
| payment_source.swish.name Required,object                          | Name of the buyer.                                                                                                                                                         |
| payment_source.swish.experience_context object                     | Context information for the Swish payment experience including locale, return URL, and buyer flow settings.                                                                |
| payment_source.swish.experience_context.locale string              | Locale for buyer’s payment experience. For Swish payments, set tosv-SE.                                                                                                    |
| payment_source.swish.experience_context.return_url Required,string | URL to redirect the buyer after payment approval.                                                                                                                          |
| payment_source.swish.experience_context.cancel_url Required,string | URL to redirect the buyer if they cancel the payment.                                                                                                                      |
| payment_source.swish.experience_context.redirect_to_app boolean    | Indicates whether to use mobile app switch flow. Set totruefor mobile app switch. Omit or set tofalsefor QR code flow. Default isfalse.                                    |

,### Response parameters
A successful request returns 200 OK and the order ID and status. The response includes:

| Parameter name                             | Description                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                                         | Unique order ID. Use this to track or reference the order in future API calls.                                                                                                                                                                                                                                |
| status                                     | Order status. For newly created Swish orders, this value isPAYER_ACTION_REQUIRED.After buyer approval with automatic capture, this changes toCOMPLETED. For the complete list of possible status values, see the[status](https://developer.paypal.com/api/limited-release/orders/v2/#orders-create-response). |
| payment_source.swish.qr_details            | QR code details for the Swish payment. Used for merchant-hosted integration.                                                                                                                                                                                                                                  |
| payment_source.swish.qr_details.qr_image   | Base64-encoded QR code image. Display this image to buyers for scanning with their Swish mobile app.                                                                                                                                                                                                          |
| payment_source.swish.qr_details.qr_payload | QR code payload string.                                                                                                                                                                                                                                                                                       |
| links                                      | [HATEOAS](https://developer.paypal.com/api/limited-release/orders/v2/#orders-create-response)links for order actions. Use thepayer-actionlink to redirect the buyer for payment approval.                                                                                                                     |

## Redirect buyer

After creating an order, redirect the buyer to complete payment approval in the Swish app. The redirect method depends on your integration pattern and the buyer's device.

### Redirect using PayPal-hosted integration

For PayPal-hosted integration, redirect the buyer to PayPal's payment page using the payer-action link from the order response.

- Extract the payer-action link from the order creation response.
- Redirect the buyer to the link URL
- PayPal displays the payment page with QR code or triggers the Swish app based on the buyer flow.

PayPal handles the buyer experience and redirects the buyer back to your return_url after payment approval or to your cancel_url if the buyer cancels.

### Display QR code using Merchant-hosted integration

For Merchant-hosted integration, display the QR code from the order response on your own page.

- Extract the QR code image from qr_details.qr_image in the order response.
- Display the base64-encoded image on your checkout page.
- Show instructions for buyers to scan the QR code with the Swish app.

For mobile app switch flow with merchant-hosted integration, you can redirect using the payer-action link to trigger the Swish app directly.

After the buyer approves payment:

- **Automatic capture** : The payment is captured automatically. Track the payment using webhooks.
- **Manual capture** : Capture the payment after buyer approval.

For manual capture orders, call the capture endpoint after the buyer approves the payment. Use a valid access token and make the POST call to /v2/checkout/orders/{order_id}/capture endpoint to capture the authorized funds.

#### **`Sample request`**

```javascript
curl -v -L -s -X POST https://api.paypal.com/v2/checkout/orders/5SJ83317D1020641R/capture \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -H 'PayPal-Request-Id: UNIQUE-REQUEST-ID'
```

#### **`Sample response`**

```javascript
{
  "id": "5SJ83317D1020641R",
  "status": "COMPLETED",
  "payment_source": {
    "swish": {
      "name": "Jhon Doe",
      "country_code": "SE"
    }
  },
  "purchase_units": [
    {
      "reference_id": "default",
      "payments": {
        "captures": [
          {
            "id": "2AB12345CD678901E",
            "status": "COMPLETED",
            "amount": {
              "currency_code": "SEK",
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
            "create_time": "2025-01-15T10:30:00Z",
            "update_time": "2025-01-15T10:30:00Z"
          }
        ]
      }
    }
  ],
  "links": [
    {
      "href": "https://api.paypal.com/v2/checkout/orders/5SJ83317D1020641R",
      "rel": "self",
      "method": "GET"
    }
  ]
}
```

## Track payment

After creating the order, you can track the payment status in two ways:

- [Use webhooks](#use-webhooks)
- [Optional] [Poll for updates](#poll-for-updates)

**Note**: Use webhooks for real-time updates and poll the order status only if you cannot receive webhooks.

### Use webhooks

To track the payment status using webhooks, follow these steps:

- [Subscribe to webhook events](https://developer.paypal.com/api/rest/webhooks/event-names/) in your PayPal developer dashboard or through the Webhooks API. For example: - PAYMENT.CAPTURE.COMPLETED – Successful payment capture
- PAYMENT.CAPTURE.DENIED – Failed payment capture

- Define a webhook handler in your server-side application to: - [Listen for incoming webhook events](https://developer.paypal.com/api/rest/webhooks/rest/#link-subscribingalistenerurl) .
- [Confirm receipt of the event to PayPal](https://developer.paypal.com/api/rest/webhooks/#link-receivingthemessage) .
- [Verify the source of the event notification](https://developer.paypal.com/api/rest/webhooks/#link-verifyingthemessagereceived) .
- Complete further actions based on event data.

**Note** : If needed, use the [List event notifications](/docs/api/webhooks/v1/#webhooks-events_list) API to retrieve all webhook events or the [Show event notification details](/docs/api/webhooks/v1/#webhooks-events_get) API to get specific event details.

Extract the order ID from the "rel": "up" link in the webhook payload's resource.links array to correlate the capture to your original order.

### Poll for updates

**Note** : Be aware of PayPal's API rate limits when polling for order status. For best practices and details, see the [Rate limiting guideline]() .

To check the status of an order, you can poll the Orders API:

- Use a valid access token and send a GET request to the /v2/checkout/orders/{id} endpoint, replacing {id} with the order ID from your [Create order](https://developer.paypal.com/api/limited-release/orders/v2/#orders-create-response) response.
- Review the response to determine the current order status and take action as needed.

| Parameter name | Description                                                          |
| -------------- | -------------------------------------------------------------------- |
| id             | Unique order ID.                                                     |
| status         | Current status of the order.                                         |
| purchase_units | List of purchase units for the order, including amount and currency. |
| payer          | Information about the buyer, including name and payer ID.            |

For the comprehensive list of response parameters, see [Show order details](https://developer.paypal.com/api/limited-release/orders/v2/#orders_get) .

## Notify buyer of success

After a successful payment, notify the buyer of a successful transaction. You can do this by sending a confirmation email.

## Next steps

### Test integration

Test the integration in the PayPal sandbox environment.

### Go live

Take your application live in the PayPal production environment once testing is successful.
