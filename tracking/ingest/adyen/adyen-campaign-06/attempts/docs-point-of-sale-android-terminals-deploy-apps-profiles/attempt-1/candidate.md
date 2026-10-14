---
title: "Adyen Android terminal app deployment using profiles"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/android-terminals/deploy-apps/profiles"
raw_files:
  - "adyen/docs/point-of-sale/android-terminals/deploy-apps/profiles/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, app-deployment, profiles]
---

## Overview

Adyen's Android profile guide describes Customer Area rules for automatically installing uploaded app versions on matching Adyen Android payment terminals. The guide applies to Android terminal hardware in a Terminal API or standalone integration, with Merchant POS Terminal Management Admin role for Customer Area profile management. This concerns apps installed on payment terminals, not the merchant-phone Mobile SDK or the GitHub native Android checkout SDK. [[adyen]] [[adyen-android-terminals]]

## Key takeaways

- Upload apps to the company account first. A profile pairs applicability conditions with selected app versions; only uploaded apps in Ready status appear for selection. The detailed condition editor offers stores, countries/regions, models and merchants. The page's opening list names only stores, countries/regions and models; the detailed editor also names merchants.
- A profile with no conditions applies to all terminals in the company account. Two Android profiles cannot have exactly the same conditions. The example with S1E terminals in selected US stores illustrates a scoped rule; it does not imply that every model or region has the same app support.
- Profiles are terminal configuration. A not-yet-boarded terminal installs its matching profile apps when boarded. A boarded terminal implements profile changes after its maintenance call; apps can then be installed or uninstalled. Updating an installed app that is open closes that app. Selecting a new app version in a profile causes applicable terminals to install that version when the profile takes effect.
- The guide says deployment of apps and certificates using API calls or manually in Customer Area overwrites the apps installed on a terminal based on a profile. Do not treat profile selection alone as proof of current installed state, execution time, approval or payment behavior; check the actual terminal and the separate deployment guides.
- Customer Area profile management supports editing name, description and conditions; selecting Edit app version; removing an app; and adding apps, followed by Save. Because a matching boarded terminal reconciles profile changes after maintenance, removing or changing an app is an operational change that may uninstall or close software in use.

## Detail locators

- Purpose, example matching behavior and new-version rollout: pinned raw lines 15–25.
- Integration, role and Android hardware requirements: pinned raw lines 27–35.
- Boarding, maintenance, install/uninstall, open-app closure and API/manual overwrite: pinned raw lines 53–62.
- Duplicate-condition limit and scope selectors including company-wide default: pinned raw lines 64–89.
- Ready-state app selection, explicit version and profile application timing: pinned raw lines 91–105.
- Edit, version change, removal and Save controls: pinned raw lines 107–122.

## Related

- [[adyen-android-terminals]] — on-terminal app deployment and model hub.
- [[adyen-terminal-management]] — boarding and maintenance are physical-terminal management transitions.
- [[adyen-terminal-api]] — in-person payment messaging, distinct from profile configuration.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/android-terminals/deploy-apps/profiles/2026-09-15|Adyen deploy using profiles guide, fetched 2026-09-15]]
