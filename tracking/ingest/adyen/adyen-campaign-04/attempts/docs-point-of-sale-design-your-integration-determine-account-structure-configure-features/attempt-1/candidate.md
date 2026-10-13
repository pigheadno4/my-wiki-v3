---
title: "Adyen Configure POS Terminal Features"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/determine-account-structure/configure-features"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/determine-account-structure/configure-features/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, customer-area, device-settings, terminal-management]
---

## Overview

Adyen's POS feature-configuration guide explains which payment-terminal features need account or device settings and where to find those settings in the Customer Area. It applies to Adyen-terminal Terminal API and standalone solutions. It describes company, merchant account, store and terminal inheritance, when changes reach terminals, the Device settings categories, feature-specific enablement, and a Customer Area UI rename/move map. It also points to API-call configuration but is not an API schema or a proof that a feature is enabled for a given account. This source is a 2026-09-15 webpage snapshot with `last_modified` 2026-05-19.

## Key takeaways

- Settings are defined from company through merchant account and store to terminal; merchant/store/terminal values replace inherited higher-level values for their descendants. Adyen PSP is above company, but merchants cannot define settings there. Adyen recommends configuring at merchant-account level. Customer Area inheritance labels and grey toggles show where a value is controlled; inspect the applicable level before changing a setting.
- For Customer Area access, `Merchant POS standard` or `Merchant POS Terminal View` can view terminal features; `Merchant POS Terminal Management Admin` can view and configure them. The guide links API-call configuration separately and does not state that these Customer Area roles are API credential roles.
- Settings changes take effect when the terminal updates its configuration during the next reboot hour; the guide links a manual configuration update for immediate use. Payment-method acceptance is separate account setup: the snapshot says terminals accept global credit cards and Maestro out of the box, while local cards, wallets and gift cards need addition to the account. Check current method availability before relying on that dated catalog statement.
- Device settings are grouped into **Device**, **Device connectivity**, **Payment features** and **Integrations**. Some connectivity fields (Wi-Fi, Ethernet, Cellular, V400m base station) are terminal-only; the table routes remote Wi-Fi profile details to their dedicated guide. For a Terminal API integration, a feature also depends on POS app compatibility. Several payment features require contacting Adyen Support and/or configuring limits, including MKE, offline processing/refunds, store-and-forward and MOTO/AVS; the table does not grant account eligibility merely by showing a toggle.
- Under Integrations, **Enable Terminal API** is required for both local and cloud Terminal API architectures, and **Enable WebSockets** is required for cloud Terminal API. The standalone setting is for the standalone solution, with built-in-printer hardware qualification. The OPI row says Support must enable OPI. Keep these integration paths separate.
- The Customer Area map says **Terminal settings** became **Device settings**, with specific moved/renamed fields; its deprecated table says certain entries were removed from *Device settings*, unless noted. That is a UI placement statement, not proof that each underlying capability has ceased to exist.

## Detail locators

- `## Requirements`, `## Inheritance of settings`, `## When new settings take effect` — solution type, Customer Area view/admin roles, company-to-terminal propagation, PSP boundary and configuration update timing.
- `## Payment methods`, `## Find and edit settings` — separate method addition and Customer Area route, including individual-terminal Device list.
- `## Device category`, `## Device connectivity category` — regional, display, sound, hardware, maintenance and network setting tables; model-specific and terminal-only qualifications.
- `## Payment features category` — POS-app compatibility and rows for application selection, tipping, transaction limits, MKE, refunds, offline processing, store-and-forward, contactless, MOTO, receipts, pre-authorization, signatures and accessible audio. Follow each linked feature guide for its actual contract.
- `## Integrations category` — OPI, Standalone, wallet passes/keys and Terminal API/WebSockets/AdditionalResponse setting scope.
- `## Customer Area UI change mapping` — moved/renamed Device, Payment features and Integrations categories; entries removed from Device settings in the deprecated table.

## Related

- Company: [[adyen]]
- Terminal API message and integration boundary: [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/determine-account-structure/configure-features/2026-09-15|2026-09-15 Adyen Configure features guide snapshot]]
