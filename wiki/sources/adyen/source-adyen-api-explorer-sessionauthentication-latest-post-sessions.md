---
title: "Session Authentication API v1 component session token | Adyen API Explorer"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/sessionauthentication/latest/post/sessions"
raw_files:
  - "adyen/api-explorer/sessionauthentication/latest/post/sessions/2026-09-15.md"
tags: [adyen, session-authentication, platforms, components, api-explorer]
---

## Overview

This 2026-09-15 API Explorer snapshot documents Session Authentication `POST /sessions` to create a token for Adyen for Platforms **Onboarding** or **Platform Experience** UI components. It lists Test `https://test.adyen.com/authe/api/v1` and Live `https://authe-live.adyen.com/authe/api/v1` server bases. The component front end uses the returned session data to make component-related server calls. This is a component authorization session, distinct from the Checkout API `POST /sessions` payment-session contract.

## Key takeaways

- The request-body table requires `allowOrigin`, `policy`, and `product`. `allowOrigin` is the URL where the component appears; in live, the page requires an SSL-protected `https://` URL. `product` is `onboarding` for Onboarding components or `platform` for Platform Experience components. The page says requirements vary by component type and routes to their guides.
- `policy` describes allowed resources and roles. Its `resources` and `roles` arrays, and resource `type`, are marked **No** in the table; do not rewrite those marks as universal schema-required fields. The prose says the relevant resource has a type and corresponding unique identifier. For Onboarding, use the legal entity with a contractual platform relationship (the individual owner's legal entity for sole proprietorships); for Platform Experience, use the account holder associated with the balance account shown. Examples pair `legalEntity`/`legalEntityId` and `accountHolder`/`accountHolderId` with component roles. The ID keys are visible in examples but absent from the table's listed property rows.
- HTTP `200 Success` is a successful token-creation operation. The response body lists `id` (session identifier) and `token` as **not required** properties, while both success examples contain them. Introductory prose describes encrypted session data in the response. Token/session creation alone does not establish completed onboarding, legal-entity verification, a payment, transfer, payout, or bank receipt.
- The page documents `400` bad request, `401` unauthorized, and `403` forbidden error bodies. The 400 example reports invalid `product`; the 403 example says the user lacks access to all token-policy resources. Error bodies have optional `requestId` and conditional `invalidFields` data. The table marks `invalidFields.value` required inside an item, but the 400 example's item omits it; treat that example/schema mismatch as unresolved. The page gives no token expiry, renewal/revocation, authentication header, idempotency, async outcome, reversal, deprecation, or current component-version rule.

## Detail locators

- Component-token purpose, server bases, and component-specific prerequisite route: raw lines 5–19.
- Request `allowOrigin`, product/policy resource types and examples: raw lines 21–73.
- 200 token response properties and 400/401/403 error schemas: raw lines 74–140.
- Success and error examples, including missing `invalidFields.value` and policy-access denial: raw lines 142–206.

## Related

- [[adyen]] — provider context.
- [[adyen-platform-components]] — embedded Platforms component context and outcome boundary.
- [[source-adyen-api-explorer-checkout-latest-post-sessions]] — separate Checkout API payment-session operation; same path name does not mean the same product contract.

## Raw Sources

- [[raw/adyen/api-explorer/sessionauthentication/latest/post/sessions/2026-09-15|Adyen API Explorer Session Authentication POST /sessions (2026-09-15 snapshot)]]
