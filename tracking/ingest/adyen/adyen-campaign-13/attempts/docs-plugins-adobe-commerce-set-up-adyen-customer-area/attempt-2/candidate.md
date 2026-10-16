---
title: "Set up Adyen Customer Area for Adobe Commerce | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/adobe-commerce/set-up-adyen-customer-area"
raw_files:
  - "adyen/docs/plugins/adobe-commerce/set-up-adyen-customer-area/2026-09-15.md"
tags: [adyen, adobe-commerce, customer-area, credentials, webhooks]
---

## Overview

This 2026-09-15 [[adyen]] Docs snapshot describes Customer Area preparation for the Adobe Commerce plugin. It separates automated setup, available from plugin v8.4.0, from manual setup for all versions. It is an instruction page, not evidence that a merchant's keys, webhooks, capture setting or payment processing have actually been configured. [[adyen-magento2]]

## Key takeaways

- Automated setup uses an API key to configure required settings and is recommended for new plugin users. Reconfiguring this way loses the older configuration. Manual setup has the user generate credentials and configure the integration; it is the guide's recommendation for prior Adobe Commerce plugin users. These are documented version-scoped choices, not proof that an exact deployed release is compatible.
- Both paths instruct generation of a server API key and a client key, and explicitly require secure storage of the API key. The manual path also adds allowed domains as client-key origins. The page shows the test Customer Area, but does not specify a role grant for the operator or prove live-environment credentials; setup and live readiness remain separate. Do not expose key values in wiki evidence.
- The manual path instructs a Standard webhook for payment-status changes with `OFFER_CLOSED` so expired payments can be closed. The raw gives default expiry examples of 12 hours for cards and up to 28 days for other methods, with Support required for a custom date. It recommends company-account webhook configuration to avoid duplicates; the webhook can cover all, selected or excluded merchant accounts. The guide specifies JSON, TLS 1.2, Basic authentication and HMAC key handling, and version-dependent endpoints: plugin v9+ `/adyen/webhook`, v8 `/adyen/process/json`. These instructions are not webhook-delivery or signature-verification proof.
- The webhook-response CSP warning is scoped to the response header Adyen receives: Adobe Commerce's CSP header can exceed Adyen's 8192-byte response-header limit. It should not be generalized into disabling storefront CSP.
- Each path has a capture-delay step at merchant-account level: `manual` for manual capture in Adobe Commerce or `immediate` after authorization, shown as the default. Authorization, capture setting and actual capture outcome are distinct. Subsequent plugin installation and payment-method configuration are linked next steps, not completed by this page.

## Detail locators

- **Automated/manual choice, version floor and reconfiguration loss:** raw lines 17–32.
- **Automated credentials and capture delay:** raw lines 34–68.
- **Manual credentials, origins, webhook/expiry/CSP and endpoint/HMAC settings:** raw lines 70–136.
- **Manual capture delay and next setup routes:** raw lines 138–176.

## Related

- [[adyen]]
- [[adyen-magento2]]
- [[adyen-api-access]] — separate API-credential and access context
- [[adyen-webhooks]] — separate webhook lifecycle context

## Raw Sources

- [[raw/adyen/docs/plugins/adobe-commerce/set-up-adyen-customer-area/2026-09-15|Adyen Adobe Commerce Customer Area setup — collected 2026-09-15]]
