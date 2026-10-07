---
title: "Braintree SEPA Direct Debit Configuration (iOS v7 Route)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/sepa-direct-debit/configuration/ios/v7"
raw_files:
  - "braintree/docs/guides/sepa-direct-debit/configuration/ios/v7-2026-09-16.md"
tags: [braintree, sepa, direct-debit, ios, configuration, client-token]
---

## Overview

This 2026-09-16 [[braintree]] website snapshot is an iOS v7-routed prerequisite checklist for accepting SEPA Direct Debit. It calls for a valid PayPal business account linked in the Braintree Control Panel, server-generated client authorization, a client integration, a server-side transaction integration, webhook configuration, and a successful transaction in either Sandbox or Production.

The retained body is a short cross-platform checklist rather than an iOS setup procedure. Its SDK statement records only that SEPA Direct Debit was introduced in JavaScript v3, iOS v5 and Android v4; it does not identify an exact installed iOS v7 package or establish current SDK support.

## Key takeaways

- Before processing SEPA Direct Debit, the page says the merchant must create, verify and link a valid PayPal business account in the Braintree Control Panel. This is a documented prerequisite, not evidence that a particular merchant is linked, eligible or enabled.
- The merchant server generates the client token, and the client uses that token when initializing its components. The page does not provide the iOS component API or an exact SDK package version.
- Client integration, server transaction creation and webhook configuration are separate checklist steps. The canonical route is iOS v7, while the only version detail in the body is historical introduction across JavaScript v3, iOS v5 and Android v4.
- The final step requires successfully processing a SEPA Direct Debit transaction in Sandbox or Production. Those are alternative environment routes in the checklist; the snapshot and preceding configuration steps are not proof that any transaction was initiated, completed, settled or funded.

> [!warning] Route, SDK and execution boundary
> The URL is an iOS v7 route, but the captured body is generic and includes sibling-platform SDK history. Do not infer an iOS v7 API, exact package compatibility or sibling-platform behavior from this page. Account linkage, token generation, integrations and webhooks are prerequisites; current SEPA availability, merchant eligibility or enablement, mandate acceptance and payment outcome require separate evidence.

## Detail locators

- Checklist purpose: `# Configuration`, raw lines 16-17.
- Valid PayPal business-account creation, verification and Control Panel linking prerequisite: `# Configuration`, raw line 18.
- Server-generated client token and component-initialization use: `# Configuration`, raw lines 19-20.
- Client integration and JavaScript v3, iOS v5 and Android v4 introduction history: `# Configuration`, raw lines 23-24.
- Server transaction creation, webhook configuration and successful Sandbox-or-Production transaction steps: `# Configuration`, raw lines 27-29.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Native SDK context: [[braintree-ios-sdk]] — separate exact-version GitHub implementation evidence; this website checklist does not establish the installed package or runtime behavior

## Related raw API references

The following collected files were not read as factual authority for this entry; they are exact-file navigation for the linked setup and lifecycle steps:

- [[raw/braintree/articles/guides/payment-methods/paypal/setup-guide-2026-09-16|Braintree PayPal business-account setup guide]]
- [[raw/braintree/docs/guides/sepa-direct-debit/client-side/ios/v7-2026-09-16|Braintree SEPA Direct Debit client-side implementation — iOS v7]]
- [[raw/braintree/docs/guides/sepa-direct-debit/server-side/node-2026-09-16|Braintree SEPA Direct Debit server-side implementation — Node.js]]
- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Braintree webhooks overview]]
- [[raw/braintree/docs/guides/sepa-direct-debit/testing-go-live/node-2026-09-16|Braintree SEPA Direct Debit testing and go-live — Node.js]]

## Raw Sources

- [[raw/braintree/docs/guides/sepa-direct-debit/configuration/ios/v7-2026-09-16|Braintree SEPA Direct Debit Configuration — iOS v7 route (captured 2026-09-16)]] - fully read pinned snapshot covering the generic prerequisite checklist and cross-platform introduction history
