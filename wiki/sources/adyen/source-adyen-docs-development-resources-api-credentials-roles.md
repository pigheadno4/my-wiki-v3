---
title: "Adyen API Credential Roles"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/api-credentials/roles"
raw_files:
  - "adyen/docs/development-resources/api-credentials/roles/2026-09-15.md"
tags: [adyen, api-credentials, roles, access-control]
---

## Overview

This unversioned Adyen documentation snapshot explains how roles govern what an API credential is allowed to do. It describes the company web-service credential as the source of roles that can be assigned to other company credentials and provides tables of frequently used payment and Management API roles.

## Key takeaways

- Roles express the actions an API credential is permitted to perform.
- The company `ws` credential starts with a set of default roles, marked in the page's tables. Roles held by that credential can be assigned to other credentials in the company through Customer Area or Management API; obtaining a role the company credential does not have requires contacting Adyen Support.
- The payment-role table is a selected catalog, not a complete role inventory. It maps roles to purposes including general transaction processing, Checkout API access, tokenization, encrypted card data, raw card data, unreferenced refunds, terminal assignment, Cloud Device API, and mobile POS SDK downloads.
- Disabling the Merchant PAL webservice role prevents that credential from processing transactions. The encrypted-cardholder-data and raw-card-data roles carry different PCI DSS assessment statements; enabling the API PCI Payments role also requires Adyen Support.
- The Management API table is likewise limited to frequently used roles and distinguishes read from read-and-write access for account, store, credential, certificate, user, webhook, payment-method, terminal, and split-configuration operations. Consult the raw table for exact role names, default markers, and action scope.

> [!warning] Evidence boundary
> This snapshot documents role purpose and assignment paths; it does not prove that a role is currently available to a particular account, that a credential has been granted it, that PCI DSS obligations have been satisfied, or that any API request or payment succeeded.

## Detail locators

- Credential-role purpose, company `ws` defaults, delegation paths, and Support escalation: `# Roles`, lines 17–23.
- Frequently used payment roles, default markers, purposes, transaction effect, PCI DSS qualifications, and Support-gated roles: `## Roles for payments`, lines 25–40.
- Frequently used Management API roles and their read/read-write operation scopes: `## Management API roles`, lines 42–66.

## Related

- Company: [[adyen]]
- Concept: [[adyen-api-access]]

## Raw Sources

- [[raw/adyen/docs/development-resources/api-credentials/roles/2026-09-15|Adyen API credential roles (2026-09-15)]] — complete collected role overview and frequently used payment and Management API role tables
