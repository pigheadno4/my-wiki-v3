---
title: Subscribe to checkout webhooks
slug: /docs/checkout/apm/reference/subscribe-to-webhooks/
createTime: "2024-05-13T18:15:21.662Z"
updateTime: "2025-05-13T09:20:03.504Z"
---

# Subscribe to checkout webhooks

To complete an end-to-end integration of alternative payment methods with the Orders API, subscribe to the following webhooks:

- CHECKOUT.ORDER.APPROVED - Listen for this webhook and then capture the payment. Step 5 of the integration instructions for each APM describe what action to take when you receive this event. See also - [Webhook event names for Orders API](/api/rest/webhooks/event-names/) .
- CHECKOUT.PAYMENT-APPROVAL.REVERSED - Listen for this webhook as an indication that a problem occurred after the buyer approved the transaction and before you captured the payment. Then notify your buyer of the problem and the reversed order. [Handle Uncaptured Payments](/docs/checkout/apm/reference/handle-uncaptured-payments/) describes what action to take when you receive this event.
- PAYMENT.CAPTURE.PENDING - Listen for this webhook as an indication that payment initiation was successful but payment completion is still pending. Do not fulfill the order until payment completion is successful. See [Payments webhooks](/api/rest/webhooks/event-names/#link-payments) .
- PAYMENT.CAPTURE.COMPLETED - Listen for this webhook and then fulfill the order. Step 5 of the integration instructions for each APM describe what action to take when you receive this event. See [Payments webhooks](/api/rest/webhooks/event-names/#link-payments) .
- PAYMENT.CAPTURE.DENIED - Listen for this webhook and then cancel fulfilling the order. Step 5 of the integration instructions for each APM describe what action to take when you receive this event. See [Payments webhooks](/api/rest/webhooks/event-names/#link-payments) .

The rest of this topic walks you through subscribing to these webhook events.

## Know before you code

- Complete the steps in [Get started](/api/rest/) to get your sandbox account information from the Developer Dashboard: - Client ID
- Access token

- This task uses the [Webhooks Management REST API](/docs/api/webhooks/v1/) .
- Use Postman to explore and test PayPal APIs.

To subscribe to the CHECKOUT.ORDER.APPROVED , CHECKOUT.PAYMENT-APPROVAL.REVERSED , PAYMENT.CAPTURE.PENDING , PAYMENT.CAPTURE.COMPLETED , and PAYMENT.CAPTURE.DENIED events, copy the following code and modify it.

### Sample request

API endpoint used: [Create webhook](/docs/api/webhooks/v1/#webhooks_post)

#### **`Sample request`**

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v1/notifications/webhooks \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <Access-Token>" \
-d '{
  "url": "https://example.com/example_webhook",
  "event_types": [
    {
      "name": "CHECKOUT.ORDER.APPROVED",
    },
    {
      "name": "CHECKOUT.PAYMENT-APPROVAL.REVERSED"
    },
    {
      "name": "PAYMENT.CAPTURE.PENDING"
    },
    {
      "name": "PAYMENT.CAPTURE.COMPLETED"
    },
    {
      "name": "PAYMENT.CAPTURE.DENIED"
    }
  ]
}'
```

#### **`Sample response`**

```curl
{
    "id": "2CJ781045X895601X",
    "url": "https://example.com/example_webhook",
    "event_types": [
      {
        "name": "CHECKOUT.ORDER.APPROVED",
        "description": "An order has been approved by buyer."
      },
      {
        "name": "CHECKOUT.PAYMENT-APPROVAL.REVERSED",
        "description": "An order has been reversed."
      },
      {
        "name": "PAYMENT.CAPTURE.PENDING",
        "description": "The state of a payment capture changes to pending."
      },
      {
        "name": "PAYMENT.CAPTURE.COMPLETED",
        "description": "A payment capture completes."
      },
      {
        "name": "PAYMENT.CAPTURE.DENIED",
        "description": "A payment capture is denied."
      }
    ],
    "links": [{
            "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks/2CJ781045X895601X",
            "rel": "self",
            "method": "GET"
        },
        {
            "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks/2CJ781045X895601X",
            "rel": "update",
            "method": "PATCH"
        },
        {
            "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks/2CJ781045X895601X",
            "rel": "delete",
            "method": "DELETE"
        }
    ]
}
```

### Modify the code

After you copy the code in the sample request, modify the following:

- Access-Token - Your [access token](https://developer.paypal.com/api/rest/authentication) .
- url - The URL of your webhook handler that listens for webhooks you're subscribed to.

### Step result

A successful request results in the following:

- A return status code of HTTP 201 Created .
- A JSON response body that contains the webhook ID.
- An entry for the webhook in the REST API app you're using for development. Open then app you're using and scroll to the webhooks section to confirm the webhook appears with the same ID returned in this call.
