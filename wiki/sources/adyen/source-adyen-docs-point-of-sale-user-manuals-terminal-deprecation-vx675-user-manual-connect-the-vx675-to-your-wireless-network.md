---
title: "Adyen VX675 wireless-network setup (historical guide)"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx675-user-manual/connect-the-vx675-to-your-wireless-network"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx675-user-manual/connect-the-vx675-to-your-wireless-network/2026-09-15.md"
tags: [adyen, point-of-sale, vx675, payment-terminals, wifi, terminal-deprecation]
---

## Overview

This [[adyen]] VX675 manual page gives a historical menu procedure for connecting the terminal to a wireless network so it can communicate with Adyen's payments platform and the merchant's back end. It was last modified 2019-04-18 and captured 2026-09-15 under terminal deprecation. It describes setup for a now-deprecated model, not observed connectivity, successful boarding, current network-security advice or payment readiness. See [[adyen-payment-terminals]].

## Key takeaways

- The guide starts with a fully charged VX675, then opens the Admin menu. It states an admin PIN is **not required if the terminal is not yet boarded**. See raw lines 18–26.
- Under `1.Network` → `2.Wi-Fi` → `2.Networks`, the guide offers a scan route that chooses a network and enters its wireless password, or a manual route that enters the SSID, chooses authentication and wireless-security types, and enters the password. Its claimed connection/default-network result is an expected procedure outcome, not a measured result for a device. See raw lines 28–57.
- The manual's WPA/WPA-2 and TKIP/CCMP choices are dated menu options (raw lines 50–56). They do not establish modern network compatibility or security suitability; the confirm button is shown as an image in raw lines 50 and 56, so its label should not be inferred.
- The related [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] overview lists VX675 under PTS PCI 3 and gives **29 March 2024** as “No more transactions” for the model (that overview's raw lines 32–35). The old setup instructions do not override that cutoff or prove present device eligibility, PCI status or payment processing.

## Detail locators

- Network purpose: raw lines 14–16.
- Power precondition and conditional Admin PIN: raw lines 18–26, `## Steps`.
- Scan and manual SSID/security/password branches: raw lines 28–57, `## Steps`.

## Related

- [[adyen]]
- [[adyen-payment-terminals]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] — historical model cutoff and migration overview.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx675-user-manual/connect-the-vx675-to-your-wireless-network/2026-09-15|Connect the VX675 to your wireless network, 2026-09-15 capture]]
