---
title: Handle uncaptured payments
slug: /docs/checkout/apm/reference/handle-uncaptured-payments/
createTime: "2024-05-13T17:58:32.976Z"
updateTime: "2025-04-24T00:02:14.433Z"
---

# Handle uncaptured payments

When a transaction is not captured within a specified amount of time after the buyer approves it through the payment method, PayPal sends CHECKOUT.PAYMENT-APPROVAL.REVERSED webhook event, initiates a cancellation of the order, and refunds the buyer's account. The time window for capturing the payment is controlled by the merchant, but the default is 3 hours.

Listen for the CHECKOUT.PAYMENT-APPROVAL.REVERSED webhook event so you can send a customized notification, branded to your company, to your buyer that provides them with possible next steps, like contacting customer support.

## Know before you code

### Get started

- Complete the steps in [Get started](/api/rest/) to get your sandbox account information from the Developer Dashboard: - Client ID
- Access token

- [Subscribe to the CHECKOUT.PAYMENT-APPROVAL.REVERSED webhook event](/docs/checkout/apm/reference/subscribe-to-webhooks/) .
- This task uses [Webhooks](/docs/api-basics/notifications/webhooks/) .
- Use Postman to explore and test PayPal APIs.

A webhook handler is a script you create on your server that completes specific actions on webhooks that hit your listener URL. Each handler script implementation is different, but for this task, make sure you have logic in your handler script that listens for the CHECKOUT.PAYMENT-APPROVAL.REVERSED event. You'll need to notify the buyer of the canceled transaction and you might need logic that updates records in your systems to show the order was canceled. The following resources might be useful as you create webhook handler code:

- [Webhook Management API](/docs/api/webhooks/v1/#webhooks) - Manage webhooks, list event notifications, and more.
- Webhook events - [Checkout webhook events](/api/rest/webhooks/event-names/#checkout-buyer-approval) - Checkout buyer approval-related webhooks.
- [Order webhook events](https://developer.paypal.com/api/rest/webhooks/event-names/#link-orders) - Other order-related webhooks.

- [Show order details endpoint](/docs/api/orders/v2/#orders_get) - Determine the status of an order.

**Sample CHECKOUT.PAYMENT-APPROVAL.REVERSED webhook event**

#### **`Sample CHECKOUT.PAYMENT-APPROVAL.REVERSED webhook event`**

```curl
{
  "id": "WH-COC11055RA711503B-4YM959094A144403T",
  "create_time": "2020-01-25T21:21:49.000Z",
  "event_type": "CHECKOUT.PAYMENT-APPROVAL.REVERSED",
  "summary": "A payment has been reversed after approval.",
  "resource": {
    "order_id": "5O190127TN364715T",
    "purchase_units": [
      {
        "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
        "custom_id": "MERCHANT_CUSTOM_ID",
        "invoice_id": "MERCHANT_INVOICE_ID"
      }
    ],
    "payment_source": {
      "ideal": {
        "name": "John Doe",
        "country_code": "NL"
      }
    }
  }
  "event_version": "1.0"
}
```

## Notify buyer of cancellation

Send a notification to your buyer to let them know there was a problem and what possible next steps they can take, like reaching out to customer support. Integrating alternative payment methods with the Orders API allows you complete customization of the checkout experience, including any error situations that occur.
