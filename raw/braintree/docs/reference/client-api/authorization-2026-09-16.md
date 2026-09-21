<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/client-api/authorization -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Authorization
slug: /docs/reference/client-api/authorization/
createTime: '2025-04-02T01:35:51.899Z'
updateTime: '2025-04-02T01:35:51.938Z'
---



# Authorization

All Client API requests must include anauthorizationFingerprintparameter that authorizes action. For
example, to authorize a request to get a list of payment methods:
### Bash
```bash
curl -G https://api.braintreegateway.com/merchants/MERCHANT_ID/client_api/v1/payment_methods \
  --data-urlencode 'authorizationFingerprint=AUTHORIZATION_FINGERPRINT'
```
The authorization fingerprint is a signed collection of the merchant's public ID and values
specified during[client token generation](/braintree/docs/reference/request/client-token/generate).
## Get an Authorization Fingerprint

The authorization fingerprint is a string included in the Client Token returned by themethod. See[Generate a Client Token](/braintree/docs/start/hello-server/ruby#generate-a-client-token)for details on obtaining a client token. Client tokens are JSON-encoded data. For client token
versions 2 and up, the JSON string is base64-encoded. The contents of a decoded and parsed client
token vary by what version was requested. At its most minimal, it contains anauthorizationFingerprintfield:
### JSON
```json
{
  "authorizationFingerprint": "AUTHORIZATION_FINGERPRINT",
  "version": 3,
  "configUrl": ""
}
```
