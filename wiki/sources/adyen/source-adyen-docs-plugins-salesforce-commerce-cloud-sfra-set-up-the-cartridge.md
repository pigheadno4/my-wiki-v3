---
title: "Set up the SFRA cartridge | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-commerce-cloud/sfra/set-up-the-cartridge"
raw_files:
  - "adyen/docs/plugins/salesforce-commerce-cloud/sfra/set-up-the-cartridge/2026-09-15.md"
tags: [adyen, salesforce-commerce-cloud, sfra, cartridge, webhooks, configuration]
---

## Overview

This 2026-09-15 [[adyen]] Docs snapshot is the setup guide for Adyen's **Salesforce Commerce Cloud Storefront Reference Architecture (SFRA) cartridge**, with configuration in Adyen Customer Area and Salesforce Business Manager. It is a setup path for a storefront using one Adyen merchant account, not evidence of an installed cartridge, approved live account, delivered webhook, completed order or successful payment. [[adyen-salesforce-commerce-cloud]]

## Key takeaways

- Before setup, the guide calls for an Adyen test account, completed cartridge metadata import, and HTTPS enforced across SFCC sites for Chrome v80 cookie compatibility. It says Salesforce allows only one Adyen merchant account per storefront. The guide gives separate storefront and Business Manager cartridge paths and an Administrator Business Manager Modules permission step to show Adyen Settings. See raw lines 23–68.
- Connection uses an Adyen **API key** for API access and a **client key** for the payment environment, generated against the integration credential in Customer Area and entered in Business Manager. Store the API key securely because the page says it cannot be copied again after leaving; the client-key setup adds allowed origins. The Account settings use **Test** during setup, **Live** when following the separate go-live checklist, and an SFRA v6/v7 enablement switch only for those SFRA versions. Live prefix and front-end resource region are deferred to go-live. No universal cartridge package version is specified here; Level 2/3 data and system-integrator-info features are separately marked as supported from v20.1.3. See raw lines 70–131, 355–385.
- Payment-status updates use a configured **Standard webhook** with a server URL ending `/Adyen-Notify`, HTTP POST and TLS 1.3; the guide maps Basic authentication credentials into Business Manager and strongly recommends HMAC signatures. It requires a successful HTTP acknowledgement such as 202. SFCC stores received webhooks as custom objects; the imported `Process` job processes events to update order payment status, then `Clean` deletes processed objects. Running that job every minute is a recommendation, not a required interval. A configuration test or HTTP acknowledgement alone does not prove an order was updated. See raw lines 133–216.
- Optional branches include tokenization and saved shopper details (with Support-assisted deletion setup), in-person endless aisle and Terminal API store mapping, Giving campaigns/method eligibility and test-to-live webhook setup, premium RevenueProtect case management, Level 2/3 data, localization, and opt-in performance analytics. The source contains separate prerequisites and platform/store conditions for each; follow the raw locators before enabling them. See raw lines 218–431.
- Customer Service Center orders use Adyen payment links. The described **pending payment** state requires the shopper to fulfill the link before the order can be processed; the guide routes status inspection to Customer Area and the link to SFCC Order Notes. It gives no proof that any particular shopper paid or that an order was processed. Payment-method setup and live configuration remain separate next-step guides. See raw lines 433–465.

## Detail locators

- **Prerequisites, SFRA/storefront account limit, cartridge paths and Business Manager roles:** raw lines 23–68.
- **Keys, allowed origins, environment and version-qualified settings:** raw lines 70–131, 355–385.
- **Webhook endpoint/security, testing, acknowledgements and scheduled order-status job:** raw lines 133–216.
- **Optional tokenization, POS, Giving, risk, localization and analytics:** raw lines 218–431.
- **Customer Service Center pending-link/order path and separate next steps:** raw lines 433–465.

## Related

- [[adyen]]
- [[adyen-salesforce-commerce-cloud]]
- [[source-adyen-docs-plugins-salesforce-commerce-cloud]]

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-commerce-cloud/sfra/set-up-the-cartridge/2026-09-15|Adyen SFRA cartridge setup — collected 2026-09-15]]
