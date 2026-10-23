---
title: "Adyen VX690 historical terminal boarding guide"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/board-the-terminal-vx690"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/board-the-terminal-vx690/2026-09-15.md"
tags: [adyen, point-of-sale, vx690, boarding, legacy]
---

## Overview

This [[adyen]] VX690 guide, last modified in 2019 and captured 2026-09-15, describes historical ways to board the physical terminal to the Adyen payments platform. It requires an internet connection and device security inspection before boarding. Its integrated and standalone routes are distinct; see [[adyen-payment-terminals]] and [[adyen-standalone-terminals]].

The guide says that after boarding, reboot and application of the latest merchant configuration, payments can begin. The separately captured [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] page later lists VX690 as having **no more transactions from 29 March 2024** (that page's raw lines 32–35). The earlier guide's readiness wording is therefore a historical instruction, not evidence of current VX690 transaction support, successful boarding, authorization or settlement.

## Key takeaways

- **Prerequisites:** The page says to connect the device to the internet successfully and perform a device security inspection before boarding. Its linked VX690 quick start guide carries those procedures; this page does not establish that either check passed for a particular device. See pinned raw lines 16–20.
- **POS App integrated route:** The guide obtains the VX690 IP through the PIN-protected Admin menu, then gives separate Android and iOS POS App flows. Android calls for API-credential details and terminal IP; the app is described as identifying the terminal, synchronizing with Adyen and verifying configuration before restart. iOS takes hostname or IP, shows a Not Boarded status and a Board Device option, then restarts and updates configuration. The illustrated Admin-menu key and iOS icon should be identified from the raw images, not inferred from their filenames. See pinned raw lines 24–59.
- **Other integrated route:** The classic-library section links Java Native Interface, Windows COM, C, iOS and Android guides rather than supplying a VX690 boarding sequence. The separate deprecation page says transactions through a classic library would no longer be possible after 31 March 2024; linked guides alone do not establish continued support. See pinned raw lines 61–69 and the deprecation page's raw lines 50–54.
- **Customer Area section:** Under a heading marked Standalone, the guide describes merchant-account Point of Sale widget registration, terminal serial number and API credential, an on-terminal one-time password, possible repeated reboots and merchant-configuration update. Its Register Terminal step still asks whether the terminal is integrated with a POS system; the heading alone must not be taken as proof that this flow is exclusively standalone. See pinned raw lines 71–90.
- **Adyen Application standalone route:** The page says to use the POS App once to register and configure the VX690 for standalone mode, after which it describes terminal use without the POS App or integrations. It sends boarding issues to POS Troubleshooting. This is a 2019 procedural claim subject to the later device cutoff above. See pinned raw lines 92–96.

## Detail locators

- Admin-menu illustrated key, PIN/troubleshooting link, network menu and IP lookup: pinned raw lines 26–34.
- Android POS App credential, connection-choice prompt, IP entry and reboot/configuration sequence: pinned raw lines 36–46.
- iOS hostname/IP, Not Boarded status, Board Device and reboot/configuration sequence: pinned raw lines 48–59.
- Classic-library guide links: pinned raw lines 61–69.
- Customer Area widget, registration fields, OTP and reboot/configuration sequence: pinned raw lines 71–90.
- Standalone POS App once and troubleshooting route: pinned raw lines 92–96.

## Related

- [[adyen-payment-terminals]] — main physical-device context.
- [[adyen-standalone-terminals]] — standalone operating model, subject to model availability.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] — later published VX690 and classic-library transaction cutoffs.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/board-the-terminal-vx690/2026-09-15|VX690 boarding guide, captured 2026-09-15]]
