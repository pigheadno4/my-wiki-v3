---
title: "Adyen Marketplaces balance-platform API credentials"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/manage-access/api-credentials-web-service"
raw_files:
  - "adyen/docs/marketplaces/manage-access/api-credentials-web-service/2026-09-15.md"
tags: [adyen, marketplaces, platforms, api-credentials, access-control]
---

## Overview

This 2023-modified guide, captured 2026-09-15 under the Marketplaces URL, explains Customer Area creation and management of balance-platform API credentials for [[adyen-platforms]] from [[adyen]]. A credential identifies the integration for API authentication; its enabled roles define permitted operations. The guide covers web service and Legal Entity Management (LEM) users, API keys, basic-auth passwords, permissions and deactivation. Possessing a credential is not proof of a specific role grant, authorized account access or a successful operation.

## Key takeaways

- The stated prerequisites are an Adyen for Platforms integration and a Customer Area user with **Manage API credentials** or **Merchant admin** role. Setup includes default balance-platform credentials; optional additional credentials can separate functions and sensitive permissions. The page limits balance-platform credential configuration to the company-account level. See raw lines 19–41 and 55–75.
- Web service users authenticate Configuration, Transfers and Session Authentication API requests for Platform Experience components; Capital API use needs additional configuration. LEM users authenticate Legal Entity Management API and Session Authentication API requests for Onboarding components. The guide prints different username-format examples in the introduction, user-type table and creation steps; use the actual generated username rather than treating an example as a universal format. See raw lines 21–25, 43–53 and 68–126.
- Each web service or LEM user has its own API key. A newly generated API key activates immediately while its predecessor remains active for 24 hours unless the operator resets its expiry to 24 hours or expires it immediately. The key cannot be copied again after leaving the page. A newly generated basic-auth password instead deactivates the previous password immediately; a separate credential provides an overlap option. See raw lines 130–185.
- Test and live are separate: the guide says to create new credentials and API keys in live Customer Area, and to use live basic-auth credentials when moving from test. Web-service permissions depend on enabled roles, with at least one role required; role selection can use Payments or Platforms tabs. Do not infer any particular API permission merely from credential creation. See raw lines 128, 156, 207 and 209–222.
- Credentials cannot be deleted. Deactivation changes the credential to inactive and prevents its API keys from being used. This is an access-disrupting lifecycle operation, not a routine key rotation. See raw lines 224–233.

## Detail locators

- Credential identity, defaults, prerequisites and web-service versus LEM API scope: raw lines 19–53.
- Additional credential creation and company-account scope: raw lines 55–128.
- API-key creation, previous-key expiry and copy-once handling: raw lines 130–177.
- Basic-auth password rotation and immediate old-password deactivation: raw lines 179–207.
- Role settings and credential deactivation: raw lines 209–233.

## Related

- [[adyen]] — provider profile.
- [[adyen-platforms]] — modern Platforms and Marketplaces route.
- [[source-adyen-docs-platforms-manage-access-api-credentials-web-service]] — separate Platforms URL with closely related guidance; retain distinct source provenance.
- [[adyen-classic-platforms]] — legacy Classic Platforms access model, distinct from this Balance Platform guide.

## Raw Sources

- [[raw/adyen/docs/marketplaces/manage-access/api-credentials-web-service/2026-09-15|API credentials for your balance platform — pinned 2026-09-15 raw snapshot]]
