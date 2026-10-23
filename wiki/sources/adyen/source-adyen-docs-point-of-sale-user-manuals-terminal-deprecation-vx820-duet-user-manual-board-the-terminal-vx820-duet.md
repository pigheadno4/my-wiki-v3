---
title: "Board the terminal - VX820 Duet"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx820-duet-user-manual/board-the-terminal-vx820-duet"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx820-duet-user-manual/board-the-terminal-vx820-duet/2026-09-15.md"
tags: [adyen, point-of-sale, vx820-duet, terminal-boarding, deprecated-terminals]
---

## Overview

This 2019-modified VX820 Duet manual page, captured 2026-09-15, describes historical ways to register and configure the terminal on the [[adyen]] payments platform: integrated boarding through the Adyen POS App or classic library integrations, and standalone boarding through Customer Area or one-time POS App use. It belongs with [[adyen-payment-terminals]].

## Key takeaways

- Before boarding, the guide requires a successful internet connection and device security inspection. The Admin-menu path to the terminal IP address is PIN-gated; the pictured first key is an image, so use the raw image locator rather than an inferred key name.
- For Android POS App boarding, the guide calls for an API credential and terminal IP address. It says the app identifies and synchronizes the device, then the terminal boards, restarts and applies merchant configuration. The iOS path uses the device hostname or IP, shows "Not Boarded", then offers "Board device" before restart and configuration update.
- The Customer Area standalone path uses a merchant-account page, a terminal serial number and selected API credential, then a shown one-time password entered on a powered-on terminal. The terminal may reboot more than once. The page also describes a single POS App boarding step before standalone use.
- The guide's "begin processing payments" language describes its historical expected state after configuration, not an observed transaction. The parent [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] lists VX820 Duet under "No more transactions" on **March 29, 2024**; it separately says transactions through classic libraries become impossible after **31 March 2024**. These later cutoffs supersede the old readiness wording for present-use decisions.

## Detail locators

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx820-duet-user-manual/board-the-terminal-vx820-duet/2026-09-15|Pinned raw]], lines 18–31: internet/security prerequisites, Admin PIN, illustrated key and IP-address menu.
- Same raw, lines 34–57: Android API-credential/IP route and iOS hostname/IP route, including app prompts, expected restart and configuration update.
- Same raw, lines 59–67: classic-library integration guide links; these are routes, not evidence that the libraries remain usable.
- Same raw, lines 69–92: Customer Area standalone registration, terminal serial/API credential, one-time password and possible repeated reboot; one-time POS App boarding for standalone mode.
- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/2026-09-15|Parent deprecation raw]], lines 32–35 and 50–54: VX820 Duet transaction cutoff and separate classic-library cutoff.

## Related

- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-duet-user-manual]] — VX820 Duet manual hub and quickstart.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] — eVo model deprecation dates and migration context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx820-duet-user-manual/board-the-terminal-vx820-duet/2026-09-15|Board the terminal - VX820 Duet]]
