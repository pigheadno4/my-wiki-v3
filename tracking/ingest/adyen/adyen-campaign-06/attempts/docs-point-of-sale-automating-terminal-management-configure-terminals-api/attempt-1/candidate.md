---
title: "Adyen Docs: Configure terminal features with Management API"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api"
raw_files:
  - "adyen/docs/point-of-sale/automating-terminal-management/configure-terminals-api/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-management, management-api, terminal-settings]
---

## Overview

Adyen's 2026-09-15 POS guide describes configuring terminal features through the Management API instead of Customer Area. It covers terminal settings and logos at company, merchant, store, and terminal levels. This is fleet configuration, not a Terminal API payment request or evidence that settings are currently available for a merchant. [[adyen]] · [[adyen-pos-store-management]] · [[adyen-terminal-api]]

## Key takeaways

- The guide requires a POS integration and an API credential with an API key and Management API Terminal settings read/read-and-write roles. Sensitive settings that can affect Terminal API communications require the additional Terminal Advanced settings read-and-write role. A cloud-communications Terminal API integration may reuse its API key. Live terminal-settings Management API endpoints are rate limited; consult the linked rate-limit page for current limits.
- Settings inherit downward from company to merchant to store to terminal. A setting at a lower level replaces an inherited higher-level value; Adyen's PSP level sits above company and cannot be configured by this API. Choose the level by the desired affected terminals and inspect its current configuration and inherited values before removing anything.
- GET and PATCH use `/terminalSettings` for settings and the separate `/terminalLogos` route for standby logos. Both route families have company, merchant, store, and terminal variants. Company, merchant, and store logo requests specify the terminal model; terminal-level logo requests infer it from terminal ID. Only one logo is retrieved or updated per request.
- For `/terminalSettings` PATCH, provide the full object for each setting group being changed. Omitted objects remain unchanged, but an omitted parameter inside a supplied object is removed at that level; an empty value is also documented for restoring an inherited value. Read the existing object and higher-level fallback first. The guide does not establish a general `null` removal rule.
- For `/terminalLogos` PATCH, `data` is a Base64-encoded model-appropriate image; an empty string removes that level's logo and returns an inherited higher-level logo. The raw model table gives dimensions and size limits and says mismatched BMP/JPG/JPEG/PNG images are resized while GIFs become a single frame.
- Existing terminals download changes on an automatic maintenance call every 180 minutes; the changes take effect after a restart, normally at the configured restart hour (usually 6:00 AM). The guide gives a manual configuration update for an immediate passcode switch. Newly shipped terminals can be configured at terminal level and take those settings when boarded.

## Detail locators

- **Prerequisites and scope:** raw `Requirements` (lines 21–32) and `Configurable features` (lines 34–77). The table identifies available setting groups and exceptions: SIM status is terminal-only; Tap to Pay settings are unavailable at terminal level. Sensitive groups include `nexo`, passcodes, and Wi-Fi profiles. More settings require Customer Area. The raw's API Explorer links use `Management/latest` and examples use `management-test.adyen.com/v3`; neither proves a current live version or account entitlement.
- **Inheritance and reads:** `Inheritance of settings` (lines 79–92), then `Get current settings` (lines 94–694). Discover company, merchant, store, or terminal IDs through the respective list routes. Logo GET needs a model query above terminal level and returns Base64 `data`; settings GET returns current configuration.
- **Update semantics:** `Update settings` (lines 695–708) and `Update other settings` (lines 1181–1479). PATCH routes exist at each of the four levels. The raw's store example is illustrative and mixes `signatureSettings` with the table/GET example's `signature`; consult the current API schema before building a payload. Its empty gratuity fields are an example of removal, not proof that every field accepts an empty string or `null`.
- **Logo conditions:** `Update terminal logo` (lines 710–1179) has the per-model dimensions, file formats, size table, Base64 upload and empty-`data` removal examples. Consult that table before uploading.
- **Propagation:** `When new settings take effect` (lines 1481–1503) distinguishes API update, terminal download, restart, and boarding.

## Related

- [[adyen-pos-store-management]] — company, merchant, and store administration context
- [[adyen-terminal-api]] — payment messaging and communications boundary
- [[adyen-api-access]] — API credential and role context

## Related raw API references

The linked Management API Explorer schemas, rate-limit page, Customer Area, network/Wi-Fi guidance, and boarding guidance were not read for this entry. Use them as navigation only.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/automating-terminal-management/configure-terminals-api/2026-09-15|Adyen Configure terminal features with Management API, fetched 2026-09-15]]
