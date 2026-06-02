---
title: "PayPal REST API — Getting Started"
type: source
date_ingested: 2026-04-19
original_format: webpage
raw_files:
  - "paypal-rest-api-get-started-2025.md"
  - "paypal-rest-api-making-requests-2025.md"
  - "paypal-rest-api-handling-responses-2025.md"
  - "paypal-rest-api-rate-limiting-2025.md"
  - "paypal-rest-api-apps-scopes-2025.md"
tags: [paypal, rest-api, oauth, authentication, sandbox, developer-platform]
---

## Summary

Foundational guide for PayPal REST API access — how to obtain credentials, exchange them for an OAuth 2.0 access token, and set up sandbox test accounts.

## HTTP Headers Reference

| Header | Required | Purpose |
| --- | --- | --- |
| `Authorization: Bearer TOKEN` | Always | OAuth 2.0 access token |
| `PayPal-Request-Id` | Recommended (POST/PUT) | Idempotency key — stored 45 days; retries safe |
| `PayPal-Auth-Assertion` | Platforms only | JWT identifying merchant (`iss`=platform client_id, `payer_id`=merchant); unsigned OK |
| `PayPal-Partner-Attribution-Id` | Platforms only | BN code tracking platform transactions |
| `PayPal-Mock-Response` | Optional (sandbox) | Simulate errors via `mock_application_codes` |

**JWT format** for `PayPal-Auth-Assertion`: `base64(header).base64(payload).` — header: `{"alg":"none"}`, payload: `{"iss":"PLATFORM_CLIENT_ID","payer_id":"MERCHANT_PAYER_ID"}`, empty signature.

## Error Response Shape

```json
{"name": "VALIDATION_ERROR", "message": "...", "debug_id": "...", "details": [{"field": "...", "issue": "..."}]}
```

## Common Error Codes

| Code | Meaning | Fix |
| --- | --- | --- |
| `VALIDATION_ERROR` | Missing/invalid fields | Check field requirements |
| `DUPLICATE_INVOICE_ID` | Invoice ID reused | Use unique ID per transaction |
| `CARD_EXPIRED` | Expired card | Ask buyer for new card |
| `ORDER_ALREADY_CAPTURED` | Already processed | Check records |
| `PAYER_ACTION_REQUIRED` | Customer action needed | Redirect to link in response |

**Security**: NEVER send API keys or tokens from frontend — frontend calls your backend, backend calls PayPal.

**Common problems**: 401 repeatedly → set up token refresh before expiry; webhooks not working → URL must be public; test payments fail → check sandbox buyer account funds.

## Key Takeaways

- **Auth flow**: exchange `CLIENT_ID:CLIENT_SECRET` (Basic Auth) for an access token via `POST /v1/oauth2/token`
- **Token lifetime**: `expires_in: 31668` seconds (~8.8 hours); request a new one when expired
- **Business account required** to go live or test outside the US
- **Sandbox**: 2 default accounts per developer account (personal buyer + business seller); login at `sandbox.paypal.com/signin/`
- **OpenAPI specs**: `github.com/paypal/paypal-rest-api-specifications`

## OAuth Token Request

```bash
curl -v -X POST "https://api-m.sandbox.paypal.com/v1/oauth2/token" \
  -u "CLIENT_ID:CLIENT_SECRET" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials"
```

Use the returned `access_token` as `Authorization: Bearer ACCESS-TOKEN` on all API calls.

## Related Pages

- [[paypal]] — company page

## Raw Sources

- [[paypal-rest-api-get-started-2025]] — verbatim REST API getting started guide from docs.paypal.ai
- [[paypal-rest-api-making-requests-2025]] — Making API requests: base URLs, 1st vs 3rd-party calls, 4 HTTP headers (Auth-Assertion JWT, Partner-Attribution-Id BN code, Mock-Response, Request-Id 45-day idempotency), pagination params, common auth errors (401/400/403)
- [[paypal-rest-api-apps-scopes-2025]] — Apps, scopes, credentials: 15 OAuth scopes by category (payment/vault/business/dispute/system); Client ID = public/client-safe; Client Secret = private/server-only; Default Application for new accounts
- [[paypal-rest-api-rate-limiting-2025]] — Rate limiting: 429 = rate limited; exact limits not published; 4 causes (polling, spikes, token misuse, suspicious patterns); fix: read Retry-After header (default 30s), exponential backoff, use webhooks instead of polling, cache OAuth tokens
- [[paypal-rest-api-handling-responses-2025]] — Handling responses: HTTP status → error name table (400/401/403/404/422/500); 5 common error codes; error response shape {name/message/debug_id/details}; NEVER expose API keys in frontend; common problems (401→refresh, webhooks→public URL, test fails→buyer funds)
