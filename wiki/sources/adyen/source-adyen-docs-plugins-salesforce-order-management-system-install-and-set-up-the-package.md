---
title: "Install and set up the Salesforce OMS package"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-order-management-system/install-and-set-up-the-package"
raw_files:
  - "adyen/docs/plugins/salesforce-order-management-system/install-and-set-up-the-package/2026-09-15.md"
tags: [adyen, salesforce-oms, setup, capture, credentials]
---

## Overview

Adyen's Salesforce OMS package setup guide (page metadata last modified 2023-12-12; captured 2026-09-15) addresses an OMS Org connected to a Salesforce Commerce Cloud storefront using the Adyen payments cartridge. It covers prerequisites, app installation, v3.3.0+ guided configuration, capture-mode safeguards and test-to-live credential changes. [[adyen-salesforce-order-management-system]] is the OMS concept; [[adyen-salesforce-commerce-cloud]] covers the separate storefront family. This guide is instructions, not proof that a gateway, webhook, capture or live payment was configured or completed.

## Key takeaways

- The prerequisite table calls for an SFCC storefront with the Adyen payments cartridge, Standard webhooks, a Salesforce OMS Org connected to SFCC, manual capture enabled in Adyen Customer Area, and the dependent **API Library Apex Adyen** package. Installation in the OMS Org also calls for multiple currencies and the **Adyen Payments for Salesforce Order Management** app (raw lines 19–38, 50–54). The page gives no gateway user-role matrix; the linked manual-setup guide owns its detailed credential/permission configuration.
- The page says guided configuration is included **from v3.3.0 onward** and reached through OMS **App Launcher → Adyen Config Page**. Manual setup remains an optional linked route. It then directs capture settings and go-live steps; none establishes which package version a merchant installed or that on-screen configuration succeeded (raw lines 40–64).
- Capture behavior depends on Adyen Customer Area settings: manual capture permits OMS capture after authorization; automatic capture occurs after authorization without a separate manual OMS capture. The later automatic-capture section explains the **Auto Capture Enabled** adapter setting to avoid duplicate requests, and a **Manual Capture Payment Methods** list for methods requiring manual capture even with automatic capture enabled (raw lines 68–108). This later branch sits alongside the earlier blanket manual-capture prerequisite; check the merchant's actual intended mode and relevant version rather than silently treating both as simultaneously required.
- Some methods capture immediately regardless of configured mode. The guide instructs listing those enabled methods in SFCC Business Manager's **Payment methods without separate capture**, so OMS does not send duplicate capture requests. The raw list is an example of variants, not a universal set for every merchant (raw lines 110–119).
- For live transition, the page directs applying for a live account and following the SFCC go-live checklist with a stated Business Manager exception. It then says to update the OMS HMAC key, live merchant-account name if different, Adyen Checkout named-credential URL using the live prefix, and its linked external-credential API key. These are environment-specific security/credential changes, not evidence of production readiness or successful processing (raw lines 121–145). Authorization-reversal and OOBO links are next-step navigation (raw lines 147–155).

## Detail locators

- SFCC cartridge/OMS prerequisites, webhooks, dependent package and installation: raw lines 19–54.
- Guided v3.3.0+ versus optional manual setup: raw lines 56–64.
- Manual/automatic capture and duplicate-capture safeguards: raw lines 68–119.
- Live HMAC, account, named URL and external API-key transition: raw lines 121–145.
- OOBO and reversal navigation: raw lines 147–155.

## Related

- [[adyen-salesforce-order-management-system]] — OMS concept and source route.
- [[source-adyen-docs-plugins-salesforce-order-management-system-install-and-set-up-the-package-manual-setup]] — separate manual gateway/credential setup authority.
- [[adyen-salesforce-commerce-cloud]] — connected SFCC storefront concept.
- [[adyen]] — provider page.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-order-management-system/install-and-set-up-the-package/2026-09-15|Salesforce OMS package setup, captured 2026-09-15]]
