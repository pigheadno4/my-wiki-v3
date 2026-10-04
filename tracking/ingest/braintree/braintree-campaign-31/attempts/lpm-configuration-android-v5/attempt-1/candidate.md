---
title: "Braintree Local Payment Methods Configuration (Android v5)"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/configuration/android/v5"
raw_files:
  - "braintree/docs/guides/local-payment-methods/configuration/android/v5-2026-09-16.md"
tags: [braintree, local-payment-methods, android, android-v5, configuration]
---

## Overview

This [[braintree]] website-guide snapshot, collected 2026-09-16 and routed as Android v5, is a prerequisite checklist for accepting Local Payment Methods. It calls for a valid PayPal business account created, verified and linked in the Braintree Control Panel; a server-generated client token used to initialize components; a client integration; a server-side local-payment transaction integration; Braintree webhooks; and successful processing in either Sandbox or Production.

These are documented configuration responsibilities, not evidence that an account was linked, a merchant or buyer is eligible, a particular environment was configured, or a payment was successfully executed. Follow [[braintree-payment-methods]] for the main provider payment-method context.

## Key takeaways

- The PayPal business account is a stated prerequisite and must be linked through the Braintree Control Panel.
- The client token is generated on the server and then used when initializing client components, preserving the client/server responsibility boundary.
- Client integration, server-side transaction creation and webhook configuration are all separate checklist items.
- Successful Sandbox or Production processing appears as a prerequisite/checklist item; this snapshot does not itself prove successful processing in either environment.
- The page says Local Payment Methods support was introduced in Android SDK v2, while this captured route is specifically the Android v5 documentation view.

> [!warning] Historical mobile-certificate notice
> The captured page says Braintree Mobile iOS and Android SDK certificates were due to expire on March 30, 2026, advises Android SDK `4.45.0+` or `5.0.0+`, and warns that all customer traffic for affected app versions would fail if those versions were neither decommissioned nor force-upgraded by that date. Because the snapshot was collected after the stated deadline, this is historical page evidence, not confirmation of current certificate state, current SDK support or compatibility for a particular app.

## Detail locators

- Dated mobile-certificate expiry, Android version floors and stated total-traffic consequence: `# Configuration > **IMPORTANT**`, raw lines 17-20.
- Configuration checklist introduction: `# Configuration`, raw line 24.
- PayPal business-account creation, verification, linking and validity prerequisite: raw line 27.
- Server-generated client token and component initialization: raw lines 28-29.
- Client integration and the platform-version introduction note: raw lines 32-33.
- Server-side transaction, webhook and Sandbox-or-Production processing checklist items: raw lines 36-38.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]

## Related raw API references

- [[raw/braintree/articles/guides/payment-methods/paypal/setup-guide-2026-09-16|PayPal business-account setup guide]] - linked account-setup navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/authorization/client-token-2026-09-16|Braintree client-token guide]] - related client-token navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/local-payment-methods/client-side-custom/android/v5-2026-09-16|Braintree Local Payment Methods custom client-side implementation (Android v5)]] - linked client-integration navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/local-payment-methods/server-side/node-2026-09-16|Braintree Local Payment Methods server-side implementation for Node.js]] - linked server-integration navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Braintree webhooks overview]] - linked webhook navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/local-payment-methods/testing-go-live/node-2026-09-16|Braintree Local Payment Methods testing and go-live for Node.js]] - linked environment-testing navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/configuration/android/v5-2026-09-16|Braintree Local Payment Methods configuration (Android v5)]] - fully read pinned website snapshot covering the acceptance checklist and historical mobile-certificate warning
