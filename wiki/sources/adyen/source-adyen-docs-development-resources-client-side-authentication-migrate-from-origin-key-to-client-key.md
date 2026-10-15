---
title: "Migrate to client key | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/client-side-authentication/migrate-from-origin-key-to-client-key"
raw_files:
  - "adyen/docs/development-resources/client-side-authentication/migrate-from-origin-key-to-client-key/2026-09-15.md"
tags: [adyen, client-key, origin-key, client-side-authentication, migration]
---

## Overview

This Adyen migration guide was collected on 2026-09-15; its raw metadata says last modified 2020-05-29. It explains moving supported Web integrations from an origin key and supported iOS/Android integrations from a client-encryption public key to a client key. It is historical, product-version-specific migration guidance, not evidence that a current installation has been migrated, can authenticate, or can process a payment. See [[adyen]], [[adyen-api-access]], and [[source-adyen-docs-development-resources-client-side-authentication]].

## Key takeaways

- The page describes one client key for all allowed origins within an environment, with origins addable or removable without regenerating the key. Its `test`/`live` prefix distinguishes environments. The Customer Area steps select the integration's API credential, generate the client key, store it securely, add allowed-origin domains, and save. The guide names no required Customer Area user role; the related client-side authentication source provides the fuller origin and live-environment constraints.
- The compatibility table says Web Drop-in/Components support client key from 3.10.1 and require it from 4.0.0; iOS and Android Drop-in/Components support it from 3.7.0 and require it from 4.0.0. Earlier listed versions use their respective origin or client-encryption public keys. The table also lists POS Mobile SDK iOS/Android solutions without version thresholds. These are statements about the listed integrations and versions in this dated guide, not a blanket SDK migration rule.
- Generating a client key does not invalidate a pre-existing origin key or client-encryption public key, according to this guide. This coexistence claim is distinct from rotation of an existing client key, for which the separate [[source-adyen-docs-development-resources-client-side-authentication]] documents a 24-hour old-client-key window.
- For Web, replace the configuration's `originKey` with `clientKey` after reaching a supported version. For iOS, create `APIContext` with `clientKey` and an explicit environment, then use it instead of `publicKey`; its example uses test and says to select a live environment for live payments. For Android, pass `clientKey` to the listed Drop-in or Component configuration builder. See the platform tabs for exact sample code.

## Detail locators

- `## Availability and compatibility`: version thresholds, old-key coexistence, and POS Mobile SDK availability list.
- `## Switch to using the client key`: Customer Area credential selection, key generation, allowed-origin entry, and save action.
- `### Tab: Web`, `### Tab: iOS`, and `### Tab: Android`: platform-specific minimum versions, configuration substitutions, and sample code.

## Related

- [[adyen]]
- [[adyen-api-access]]
- [[source-adyen-docs-development-resources-client-side-authentication]] — companion 2026-09-15 snapshot for client key, allowed origins, environment, and existing-client-key rotation.

## Raw Sources

- [[raw/adyen/docs/development-resources/client-side-authentication/migrate-from-origin-key-to-client-key/2026-09-15|Adyen origin/public-key to client-key migration, 2026-09-15]]
