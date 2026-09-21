---
title: "Braintree OAuth Webhooks (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/webhooks/oauth/node"
raw_files:
  - "braintree/docs/reference/general/webhooks/oauth/node-2026-09-16.md"
tags: [braintree, node-js, webhooks, oauth, beta]
---

## Overview

This Braintree Node.js reference documents the OAuth access-revocation webhook for a connected merchant. OAuth is qualified as closed beta in production and open beta in sandbox; the page's callback and Promise examples parse the notification rather than performing revocation or triggering webhook delivery.

## Key takeaways

- The documented `oauth_access_revocation` notification is triggered when a connected merchant revokes API access. The page does not describe other OAuth event kinds.
- The attribute categories are the webhook kind, UTC trigger time, connected merchant ID, and OAuth application client ID. The callback and Promise examples show `notification.kind` as `OAuthAccessRevoked` and access the connected merchant ID through `notification.oauthAccessRevocation.merchantId`.
- Both examples configure the displayed gateway for `Sandbox`, but the availability notice separately states open beta in sandbox and closed beta in production. The example environment must not be generalized into a sandbox-only availability claim.

## Detail locators

- Production closed-beta and sandbox open-beta qualification: `# OAuth > AVAILABILITY`, lines 17-18.
- Notification-kind semantics and the sole documented event condition: `# OAuth > ### Notification kinds`, lines 23-33.
- Payload categories: `# OAuth > ### Attributes`, lines 36-38.
- Callback parsing and nested merchant-ID access: `# OAuth > ### OAuth access revoked > ### Callback`, lines 39-62.
- Promise parsing and nested merchant-ID access: `# OAuth > ### OAuth access revoked > ### Promise`, lines 64-82.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-webhooks]]

## Related raw API references

- [[raw/braintree/docs/guides/webhooks/parse/node-2026-09-16|Braintree Node.js webhook parsing guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/extend/oauth/overview-2026-09-16|Braintree OAuth overview]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/extend/oauth/access-tokens/node-2026-09-16|Braintree Node.js OAuth access-token guide]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/general/webhooks/oauth/node-2026-09-16|Braintree Node.js OAuth webhook reference]] - complete collected page covering beta availability, connected-merchant access revocation, payload categories, and callback and Promise parsing examples
