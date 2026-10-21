---
title: "Payout Service balance-platform web service API credentials"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/manage-access/api-credentials-web-service"
raw_files:
  - "adyen/docs/payouts/payout-service/manage-access/api-credentials-web-service/2026-09-15.md"
tags: [adyen, payouts, payout-service, api-credentials, access-control]
---

## Overview

This Payout Service guide, last modified 2022-12-16 and captured 2026-09-15, describes web service API credentials for a balance platform. Credentials identify API integration requests and combine username, authentication secret and enabled roles; this is access configuration guidance, not evidence that a credential was created, an API request was authorized, or a payout succeeded. See [[adyen]], [[adyen-api-access]] and [[adyen-payouts]] (raw lines 5–31).

## Key takeaways

- The stated prerequisite is a Payout Service integration and a Customer Area user with **Manage API credentials** or **Merchant admin** role. The balance-platform setup includes default credentials; web service users authenticate Adyen API requests, while distinct LEM users authenticate Legal Entity Management API requests. The web service table names Configuration, Transfers and Session authentication APIs as routes; enabled roles determine actual permission (raw lines 36–52, 176–187).
- Additional balance-platform web service credentials may separate functions or sensitive reveal permissions. The page says these credentials are configured only at **company account** level in the Customer Area Platforms tab. A new credential's username and generated API key must be stored securely; the page requires **new live-environment credentials and keys** when switching from test to live (raw lines 54–93).
- Each web service user has its own API key. A newly generated key becomes active immediately and the previous key remains active for **24 hours**; the page describes resetting the previous key's expiry to 24 hours or expiring it immediately. The key cannot be copied again after leaving its generation page. These are key-rotation mechanics, not confirmation that dependent systems have changed keys (raw lines 95–143).
- Generating a new **basic-authentication password** deactivates the previous password immediately. For overlap while updating systems, the page suggests creating another API credential; live basic-authentication credentials come from the live Customer Area (raw lines 145–172).
- A web service credential must have at least one enabled role. Credentials cannot be deleted, but can be deactivated to prevent their API keys from being used. The page's workflow is documentation only; no credential, role or secret changes are performed by this ingest (raw lines 174–199).

## Detail locators

- Integration and Customer Area role prerequisites; default web service and LEM user scope: raw lines 36–52.
- Additional credential workflow, company-account scope and test/live separation: raw lines 54–93.
- API-key rotation and previous-key expiry controls: raw lines 95–143.
- Basic-authentication replacement and live credentials: raw lines 145–172.
- Enabled roles and deactivation: raw lines 174–199.

## Related

- [[adyen-payouts]]
- [[source-adyen-docs-payouts-payout-service-get-started]]
- [[source-adyen-docs-development-resources-api-credentials]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/manage-access/api-credentials-web-service/2026-09-15|Pinned Payout Service API-credentials guide]]
