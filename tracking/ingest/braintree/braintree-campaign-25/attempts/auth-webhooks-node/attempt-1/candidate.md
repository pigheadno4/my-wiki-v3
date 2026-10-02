---
title: "Braintree Auth Webhooks Guide (Node.js)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-auth/webhooks/node"
raw_files:
  - "braintree/docs/guides/braintree-auth/webhooks/node-2026-09-16.md"
tags: [braintree, braintree-auth, node-js, webhooks, connected-merchants, oauth, beta]
---

## Overview

This collected Node.js guide documents webhook handling for new Braintree merchant accounts connected through Braintree Auth. It covers connected-merchant underwriting or application events, PayPal account link-status changes, disputes, and OAuth access revocation; it is distinct from generic transaction authorization and from the separate event-reference pages.

The page labels Braintree Auth closed beta. Its examples parse notifications with the Node server SDK, but the page does not name an SDK version, establish current eligibility, or give a separate sandbox-versus-production availability rule.

## Key takeaways

- A Braintree Auth integration that supports new Braintree account signups can subscribe to four documented connected-merchant event areas: underwriting status or application submission, PayPal account linking status, disputes, and OAuth access revocation. Existing webhook users are routed to general configuration and parsing authorities; this page does not define delivery timing, ordering, retries, duplicate handling, or endpoint authentication.
- The underwriting table makes consequential distinctions. `approved` says settled funds will be disbursed to the merchant's bank account; `denied` says all settled transactions will be refunded; `application_submitted` permits up to 25 transactions or $2,500 while withholding disbursement until approval; and `inactive` can include a trial merchant that did not apply within 30 days after its first payment. Use the exact table for all five status definitions.
- For PayPal account status, `link` means the connected merchant has connected a PayPal account and can accept PayPal payments. After `unlink`, the page says the merchant cannot accept PayPal payments until another PayPal account is linked. The guide reports these changes; it does not document how linking or unlinking is performed.
- A connected merchant's transaction dispute can trigger the dispute webhook only after the integration requests the `oauth_app_receive_dispute_webhooks` scope. The linked scope and dispute-reference pages own their detailed authority.
- The OAuth access-revoked section reports when the connected merchant has revoked account access. Its callback and Promise examples parse `bt_signature` and `bt_payload`; they do not revoke access themselves or prove delivery.

> [!warning] Closed-beta, connected-merchant scope
> Keep this guide limited to new merchant accounts connected through Braintree Auth. Its unqualified closed-beta notice and sandbox-configured examples do not establish current support, merchant eligibility, production enablement, or a sandbox-only rule. Do not broaden these notifications into generic transaction-authorization or general Braintree webhook behavior.

## Detail locators

- Closed-beta availability: `# Webhooks > AVAILABILITY`, lines 17-18.
- Connected-merchant signup scope and the four webhook areas: `# Webhooks`, lines 22-30.
- General configuration route and webhook POST parsing parameters: `## Before you get started`, lines 33-39.
- Underwriting/application trigger, Node parsing examples, and five status definitions: `## Connected merchant underwriting status`, lines 42-96.
- PayPal link-status trigger, Node parsing examples, and link/unlink effects: `## PayPal account status changed`, lines 99-140.
- Connected-merchant dispute trigger, required OAuth scope, Node parsing examples, and dispute-reference route: `## Disputes`, lines 143-181.
- Connected-merchant account-access revocation and Node parsing examples: `## OAuth access revoked`, lines 184-221.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-webhooks]]
- Separate Braintree Auth event and payload reference: [[source-braintree-webhooks-braintree-auth-node]]
- Separate OAuth access-revocation event reference: [[source-braintree-webhooks-oauth-node]]
- Separate dispute event reference: [[source-braintree-webhooks-dispute-node]]

## Related raw API references

- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Braintree general webhooks overview]] - navigation-only setup route linked by this guide; not read or used as factual evidence here
- [[raw/braintree/docs/guides/webhooks/parse/node-2026-09-16|Braintree Node.js webhook parsing guide]] - navigation-only parsing route linked by this guide; not read or used as factual evidence here
- [[raw/braintree/docs/guides/braintree-auth/server-side/node-2026-09-16|Braintree Auth Node.js server-side guide]] - navigation-only authority for the dispute-webhook OAuth scope; not read or used as factual evidence here
- [[raw/braintree/docs/reference/general/webhooks/braintree-auth/node-2026-09-16|Braintree Auth webhook reference for Node.js]] - navigation-only event-reference route; not read or used as factual evidence here
- [[raw/braintree/docs/reference/general/webhooks/oauth/node-2026-09-16|Braintree OAuth webhook reference for Node.js]] - navigation-only OAuth event-reference route; not read or used as factual evidence here
- [[raw/braintree/docs/reference/general/webhooks/dispute/node-2026-09-16|Braintree dispute webhook reference for Node.js]] - navigation-only dispute-object and event-reference route; not read or used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/guides/braintree-auth/webhooks/node-2026-09-16|Braintree Auth webhooks guide for Node.js]] - complete collected page covering closed-beta availability, connected-merchant notification scope, consequential underwriting and PayPal-link boundaries, the dispute-scope prerequisite, OAuth access revocation, and Node parsing examples
