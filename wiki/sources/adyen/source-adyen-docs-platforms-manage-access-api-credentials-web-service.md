---
title: "API credentials for an Adyen balance platform"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/manage-access/api-credentials-web-service"
raw_files:
  - "adyen/docs/platforms/manage-access/api-credentials-web-service/2026-09-15.md"
tags: [adyen, platforms, api-credentials, access-control, security]
---

## Overview

This Adyen for Platforms access guide, last modified 2023-09-07 and captured 2026-09-15, describes Customer Area management of API credentials for a balance platform. A credential identifies an integration for API authentication; its roles govern permitted actions. The page covers web service and Legal Entity Management (LEM) users, key/password rotation, permissions and deactivation. Creating a credential is not proof that a particular API action is permitted, an account holder is verified, or a financial operation succeeded.

## Key takeaways

- The guide requires an Adyen for Platforms integration and a Customer Area user with either the Manage API credentials or Merchant admin role. Balance-platform setup includes default credentials; additional credentials can isolate functions or sensitive permissions. The page says balance-platform credentials are configured at the company-account level.
- Web service credentials are for Configuration API, Transfers API, Session Authentication API for Platform Experience components and, with additional configuration, Capital API. LEM credentials are for Legal Entity Management API and Session Authentication API for Onboarding components. The table's displayed username formats differ from the general username example and the creation-step example; follow the credential's actual generated username rather than treating any printed example as a universal format.
- Each web service or LEM user has its own API key. The guide instructs the operator to copy and store the key securely; it cannot be copied again after leaving the page. A newly generated key is active immediately, and the previous key remains active for 24 hours unless its expiry is reset to 24 hours or accelerated to immediate expiry. Rotate dependent systems accordingly. A newly generated basic-auth password, by contrast, deactivates the previous password immediately; the guide suggests a separate credential if overlap is needed.
- Live credentials and API keys must be created separately in live Customer Area when switching environments; test credentials are not a live authorization. Permissions for web service credentials are defined by enabled roles, with at least one role required. The page shows role selection for Payments or Platforms tabs, but mere credential existence does not establish a specific role grant or resource access.
- API credentials cannot be deleted. Deactivation sets the credential inactive to prevent use of its API keys; this is a potentially disruptive access change. The page documents settings actions, not evidence that they were executed in an account.

## Detail locators

- `## Requirements`: integration and Customer Area role prerequisites.
- `## API credentials included with your balance platform`: web service versus LEM users, APIs and printed username formats.
- `## Create additional API credentials`, including Web service and LEM tabs: company-account scope, generated username/key and live-credential distinction.
- `## Generate an API key` and `## Reset the expiry time of a previous API key`: copy-once handling and key-overlap/expiry controls.
- `## Generate a basic authentication password`: immediate old-password deactivation and live credential requirement.
- `## Manage API permissions` and `## Deactivate an API credential`: role requirements and inactive state.

## Related

- [[adyen-platforms]] — platform integration and source route.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/manage-access/api-credentials-web-service/2026-09-15|Adyen API credentials for your balance platform (fetched 2026-09-15)]]
