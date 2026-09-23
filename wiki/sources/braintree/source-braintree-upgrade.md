---
title: "Upgrade to Braintree SDKs"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/upgrade"
raw_files:
  - "braintree/docs/reference/general/upgrade-2026-09-16.md"
tags: [braintree, sdk, migration, payment-method-nonce, vault, legacy-integration]
---

## Overview

This Braintree page documents historical upgrade routes from Server-to-Server, Transparent Redirect, and the old Braintree.js integration toward Braintree SDK-based client tokenization and server-side payment-method nonce handling. It also preserves a collected integration-feature comparison and a Vault-continuity statement, but names no SDK versions or migration date and does not establish current product support or availability.

## Key takeaways

- The page frames the three named paths as previous or legacy Braintree integrations and presents an upgrade to Braintree SDKs as a way to support additional features. Its feature-support table is evidence of this collected page, not a current compatibility matrix.
- For an existing Server-to-Server integration, the documented route adds Braintree client SDKs to the app or site and changes the server integration to accept a payment-method nonce instead of credit-card details.
- For Transparent Redirect, the page says Braintree Drop-in replaces that integration; its route adds the Drop-in payment form and changes the server to accept a payment-method nonce instead of confirming the redirect. This is historical migration guidance, not proof that Drop-in is the current recommended target.
- For the old Braintree.js integration, the documented route adds Braintree client SDKs and changes the server to accept a payment-method nonce instead of encrypted card fields.
- The page says merchants using the Vault can upgrade while retaining access to previously vaulted customer and payment information. It does not define migration mechanics, SDK-version compatibility, or current payment-method availability.

> [!warning] Historical upgrade scope
> The collected page does not identify SDK versions or an effective date for its feature table and migration recommendations. Treat the named legacy paths and replacement routes as historical documentation, verify current lifecycle and availability before planning an upgrade, and use [[braintree-web-drop-in]] for the separately retained Drop-in lifecycle evidence.

## Detail locators

- Collected feature comparison across Server-to-Server, Transparent Redirect, Braintree.js and Braintree SDKs: `# Upgrade to Braintree SDKs > ## Integration features`, lines 17-27.
- Upgrade section scope and Vault-continuity statement: `## How to upgrade`, lines 30-34.
- Server-to-Server client-SDK and payment-method-nonce route: `## How to upgrade > ### Server-to-Server`, lines 37-43.
- Transparent Redirect replacement and nonce-handoff route: `## How to upgrade > ### Transparent Redirect`, lines 46-52.
- Old Braintree.js replacement and nonce-handoff route: `## How to upgrade > ### Braintree.js`, lines 55-61.

## Related

- Company: [[braintree]]
- Server integration concept: [[braintree-server-sdk]]
- Browser SDK concept: [[braintree-web-sdk]]
- Drop-in lifecycle route: [[braintree-web-drop-in]]
- Current integration-flow route: [[source-braintree-get-started]]

## Related raw API references

- [[raw/braintree/docs/start/overview-2026-09-16|Braintree SDK overview]] - navigation-only route linked by the collected feature table; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/reference/general/upgrade-2026-09-16|Upgrade to Braintree SDKs]] - complete collected page covering historical integration comparisons, Vault continuity, and nonce-based upgrade routes for Server-to-Server, Transparent Redirect, and Braintree.js
