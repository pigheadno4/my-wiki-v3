<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/paypal-commerce-channel-api/keeping-track-of-retailers -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Keeping Track of Retailers
slug: /docs/guides/paypal-commerce-channel-api/keeping-track-of-retailers/
createTime: '2025-04-01T23:21:03.603Z'
updateTime: '2025-04-01T23:21:03.642Z'
---



# Keeping Track of Retailers

While you could attempt to get information about any product posted on your platform, it's not a
very good use of resources. Instead, we recommend only looking up products sold by retailers that
have granted your channel permission to access their products. You can tell which retailers have
granted or revoked access by listening for onboarding and offboarding webhook messages. We'll send
these messages to the destination URL you gave us during the Channel API setup process. You can use
these messages to keep track of which retailers have onboarded and keep this list up to date when
they offboard.
## Onboarding

When a retailer grants your channel authorization to query our API for their products and create
orders for their store, we'll send you an onboarding message that looks like this:
### http
```http
POST /paypalorders HTTP/1.1
Content-Type: application/json
Host: api.yourdomain.com

{
    "topic": "retailer",
    "action": "created",
    "retailer": {
        "domain": "shop.example.com"
    }
}
```

## Offboarding

If a retailer decides to revoke the authorization to your channel for whatever reason, we'll deliver
an offboarding message that looks like this:
### http
```http
POST /paypalorders HTTP/1.1
Content-Type: application/json
Host: api.yourdomain.com

{
    "topic": "retailer",
    "action": "deleted",
    "retailer": {
        "domain": "shop.example.com"
    }
}
```
Once a retailer has offboarded, any retailer-specific access tokens and client credentials will no
longer be valid.
## Retry and failure logic

We will attempt to deliver these messages to your destination URL immediately upon a successful
onboarding or offboarding event. If your server doesn't respond with a 200 HTTP status code in less
than 10 seconds, we will attempt to redeliver the message several times over the course of the next
12 hours. After each attempt, our servers will increase the delay before the next attempt.