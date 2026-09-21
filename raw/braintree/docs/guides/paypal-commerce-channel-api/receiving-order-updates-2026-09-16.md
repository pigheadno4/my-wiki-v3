<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/paypal-commerce-channel-api/receiving-order-updates -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Receiving Order Updates
slug: /docs/guides/paypal-commerce-channel-api/receiving-order-updates/
createTime: '2025-04-01T21:38:34.027Z'
updateTime: '2025-04-01T21:38:34.057Z'
---



# Receiving Order Updates

When we receive an update about an order from the retailer's ecommerce system, we'll send a webhook
message to the same destination URL we use for[retailer onboarding and offboarding messages](/braintree/docs/guides/paypal-commerce-channel-api/keeping-track-of-retailers). You can use these webhooks to provide updated order information to your users. Once the retailer
fulfills a channel-initiated purchase, we will deliver a webhook message that looks something like
this:
### http
```http
POST /paypal_notifications HTTP/1.1
Content-Type: application/json
Host: api.yourdomain.com

{
    "topic": "order",
    "action": "update",
    "order": {
        "partner_order_id": "or_2293",
        "status": "fulfilled"
    }
}
```
We will attempt to deliver this message to your destination URL immediately upon receiving
confirmation from the retailer that they've fulfilled the order. We'll handle retries and failures
the same way we do in[Keeping Track of Retailers](/braintree/docs/guides/paypal-commerce-channel-api/keeping-track-of-retailers#retry-and-failure-logic).