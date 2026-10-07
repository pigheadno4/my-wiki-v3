---
title: "Braintree PayPal Commerce Channel API — Obtaining an Access Token"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal-commerce-channel-api/obtaining-an-access-token"
raw_files:
  - "braintree/docs/guides/paypal-commerce-channel-api/obtaining-an-access-token-2026-09-16.md"
tags: [braintree, paypal-commerce-channel-api, access-token, authorization, retailer]
---

## Overview

This collected, unversioned Braintree website guide describes obtaining the retailer-scoped access token that authorizes requests between a retailer and a PayPal Commerce Channel API channel. It covers the channel credentials and retailer domain used in the token request, the sandbox-only example environment, returned validity duration, expiry refresh, and permission or revocation failures. The 2026-09-16 snapshot does not establish current API availability, production endpoints, channel or retailer eligibility, credential issuance, an active grant, or successful request or payment execution. See [[braintree]] and the provider-level route [[braintree-payment-platform]].

## Key takeaways

- The token request combines the channel's client ID and secret with the retailer domain received through onboarding. The page's request example targets the Braintree Commerce sandbox endpoint and uses credential placeholders; it does not document a production endpoint or authorize exposing credential values.
- In sandbox, the guide says the channel is automatically connected to a test retailer at `YOUR_BRAINTREE_MERCHANT_ID.retailer.com`; this is an environment-qualified example, not evidence of a production retailer relationship or grant.
- If the retailer has granted the integration permission to access its products, the response contains an access token and its validity duration in seconds. The shown token and `3600` duration are example values, not credentials or a universal lifetime.
- The guide recommends caching the token. After expiry, Channel API requests begin returning HTTP 403, at which point the code should obtain and cache a new token. This expiry path is distinct from missing permission, which produces HTTP 400 on the token request.
- A retailer may revoke its grant at any time. After revocation, requests using the existing token return HTTP 403 and requests for a new token return HTTP 400; refreshing is therefore not stated to restore revoked authorization.

## Detail locators

- **Token purpose, channel credentials, retailer domain, and sandbox retailer:** `Overview` (raw lines 16–20).
- **Sandbox token request shape and credential placeholders:** `Obtain an access token` (raw lines 22–32).
- **Grant condition, returned token, and validity duration:** raw lines 33–44.
- **Cache recommendation and expiry-conditioned HTTP 403 refresh action:** raw lines 45–46.
- **Missing-permission and revoked-grant outcomes:** `Unsuccessful requests` (raw lines 47–52).

## Related

- [[braintree]]
- [[braintree-payment-platform]]
- [[source-braintree-docs-guides-paypal-commerce-channel-api-overview|Braintree PayPal Commerce Channel API Overview]]
- [[source-braintree-docs-guides-paypal-commerce-channel-api-keeping-track-of-retailers|Braintree PayPal Commerce Channel API — Keeping Track of Retailers]]
- [[source-braintree-docs-guides-paypal-commerce-channel-api-getting-product-information|Braintree PayPal Commerce Channel API — Getting Product Information]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal-commerce-channel-api/obtaining-an-access-token-2026-09-16|Braintree PayPal Commerce Channel API — Obtaining an Access Token (2026-09-16 snapshot)]]
