---
title: "Braintree Elo Configuration"
type: source
date_ingested: 2026-10-08
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/elo/configuration"
raw_files:
  - "braintree/docs/guides/elo/configuration-2026-09-16.md"
tags: [braintree, elo, configuration, limited-release, enablement]
---

## Overview

This 2026-09-16 snapshot is an unversioned [[braintree|Braintree]] configuration notice for Elo, distinct from configuration for other payment methods. It says Elo was in limited release for select merchants using what the page calls the latest JavaScript v3 and server SDKs and directs merchants to contact Braintree to request access.

## Key takeaways

- Elo is not automatically enabled in either Sandbox or Production accounts; the page directs a merchant ready to integrate to contact Braintree.
- The notice supplies no Control Panel procedure, credentials, client/server implementation steps, environment-specific behavior, or successful-payment evidence.

> [!warning] Snapshot, account and implementation boundary
> The page-relative word "latest" does not identify an exact SDK package or version. This website snapshot does not establish current Elo availability, selection or approval of a merchant, enablement in either account environment, exact behavior in a retained GitHub SDK version, or a successful authorization, payment, settlement or funding outcome.

## Detail locators

- Limited-release, select-merchant, JavaScript v3/server-SDK and access-request conditions — `AVAILABILITY`, raw line 18.
- Nonautomatic Sandbox and Production enablement and integration contact action — `Braintree requirements`, raw line 23.

## Related

- [[braintree]] — provider context and website-versus-versioned-repository evidence boundary
- [[braintree-payment-methods]] — provider payment-method retrieval hub
- [[source-braintree-docs-guides-elo-client-side-javascript-v3]] — related Elo client-side route
- [[source-braintree-docs-guides-elo-server-side-node]] — related Elo server-side route
- [[source-braintree-docs-guides-elo-testing]] — related Elo testing route

## Raw Sources

- [[raw/braintree/docs/guides/elo/configuration-2026-09-16|Braintree Elo configuration notice (2026-09-16 snapshot)]]
