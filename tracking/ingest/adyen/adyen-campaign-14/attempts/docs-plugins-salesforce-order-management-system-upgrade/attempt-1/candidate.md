---
title: "Adyen Salesforce OMS package upgrade"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-order-management-system/upgrade"
raw_files:
  - "adyen/docs/plugins/salesforce-order-management-system/upgrade/2026-09-15.md"
tags: [adyen, salesforce-oms, upgrade, webhooks]
---

## Overview

This Adyen webpage snapshot has two **Salesforce Order Management System package** migration branches: **v2 to v3** and **v1 directly to v3.2.0**. It describes gateway, credential, webhook, account-routing, site-access, data-migration, and old-package removal steps. These are instructions for an OMS integration, not a Salesforce Commerce Cloud storefront upgrade or proof of a successful deployment, capture, refund, reversal, order, or payout. See [[adyen]] and [[adyen-salesforce-order-management-system]].

## Key takeaways

- **From v2 to v3:** update the existing **Adyen Payment Gateway** record to the package-provided `Adyen OMS Provider` and `AdyenCheckout` Merchant Credential, then retain the provider ID for the webhook URL (raw lines 21–45). V3 makes **HMAC signature verification mandatory** and enables `REFUND_FAILED` and `CAPTURE_FAILED` webhooks. The page instructs updating the existing webhook endpoint using that provider ID, generating/storing an HMAC key, adding it to Salesforce metadata, and testing the new configuration (lines 47–115). A saved configuration or test instruction is not evidence that notifications were delivered or verified.
- V3 changes sales-channel merchant-account selection: leave the channel's field empty to use the **Adyen Default** metadata merchant account, or link a specific merchant account to the channel (raw lines 117–145). The included Named Credential uses **API keys instead of basic authentication** and needs a Principal Credential setup (lines 147–151). These are account/credential routing rules, not proof of access to a particular merchant account.
- **From v1:** Adyen strongly recommends going directly to **v3.2.0**, whose separate namespace allows installation alongside the existing integration (raw lines 153–163). The setup path reuses/updates the existing gateway and Salesforce site instead of creating new ones. For the existing site, it calls for **Guest Access to the Payments API** and `Adyen Adapter` in enabled Custom Metadata Type Access (lines 165–188). This is a narrowly described site-access configuration, not a general permission grant.
- The v1 path's `BatchAdyenOMSMigration.cls` script copies **payment-method custom attribute values** into new custom fields; the page does not say it migrates tokens or prove any record was copied (raw lines 190–207). After upgrade steps, it instructs testing **before uninstalling the older package**, and says to remove the migration script if uninstalling has issues (lines 209–213). Uninstall is a consequential change, not a rollback or a guarantee of preserved functionality.
- The page routes the migrated version to separate **go-live** instructions (raw lines 215–217). It does not specify payment retries, capture/refund reversal behavior, or financial outcome semantics in these upgrade steps; those require the relevant operational and result evidence.

## Detail locators

- `Migrate from v2`, raw lines 21–151: gateway/provider ID, HMAC and failure webhooks, sales-channel account selection and API-key Named Credential.
- `Migrate from v1`, raw lines 153–213: v3.2.0 side-by-side install, existing gateway/site updates, migration script and old-package uninstall sequence.
- `Go live`, raw lines 215–217: separate version-specific live route.

## Related

- [[adyen-salesforce-order-management-system]] — OMS product and package context.
- [[adyen-salesforce-commerce-cloud]] — distinct storefront integration family.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-order-management-system/upgrade/2026-09-15|Salesforce OMS upgrade, fetched 2026-09-15]]
