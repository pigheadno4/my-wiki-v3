<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/paypal-commerce-channel-api/obtaining-an-access-token -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Overview
slug: /docs/guides/paypal-commerce-channel-api/obtaining-an-access-token/
createTime: '2025-04-01T22:43:16.717Z'
updateTime: '2025-04-01T22:43:16.753Z'
---



# Overview

Before you can make requests to the Channel API, you'll need to obtain an access token which serves
as an authorization between the retailer and your channel.

To do this, pass your channel's client ID
and secret along with the retailer's domain from the[onboarding webhook](/braintree/docs/guides/paypal-commerce-channel-api/keeping-track-of-retailers#onboarding). In the sandbox, we'll automatically connect you to a retailer for testing with the domainYOUR_BRAINTREE_MERCHANT_ID.retailer.com.

Obtain an access token:
### bash
```bash
curl -X POST https://commerce.sandbox.braintreegateway.com/channel/token \
-H "Content-Type: application/json" \
-d '{
    "client_id": "'"$PARTNER_CLIENT_ID"'",
    "client_secret": "'"$PARTNER_CLIENT_SECRET"'",
    "retailer_domain": "'"$RETAILER_DOMAIN"'"
}'
```
Assuming the retailer has granted your integration permission to access their products, the API will
return a response containing an access token as well as how long the token will be valid (in
seconds):
### http
```http
HTTP/1.1 200 OK
Content-Type: application/json
{
    "access_token": "AAABBCCCDD...",
    "expires_in": 3600
}
```
We recommend caching this token. Once the token expires the API will begin returning a 403 HTTP
status, at which point your code should fetch a new access token and re-cache it.
## Unsuccessful requests

If the retailer has not granted their permission yet, the token request will result in a 400 HTTP
status. If the retailer has revoked the grant – which they may do at any time – any request you make
with the token after access has been revoked will result in a 403, and any request for a new token
will result in a 400.