---
title: "Adyen e355 historical terminal boarding guide"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/board-the-terminal-e355"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/board-the-terminal-e355/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, e355, boarding, historical]
---

## Overview

This [[adyen]] e355 boarding guide was last modified **2019-04-23** and captured 2026-09-15 under the **terminal-deprecation** manual tree. It describes registering an e355 with the payments platform via the historical Adyen POS App, including separate Android/iOS screens, plus links to other boarding modes and classic-library integrations. Read it with [[adyen-payment-terminals]] and the dated [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] cutoff: the guide's “begin processing payments” wording is not current e355 support, account enablement, completed boarding or payment proof.

## Key takeaways

- **Before boarding**, the guide requires successful internet connection and device security inspection. Its “quick start guide” link points to the **VX675** manual path rather than e355, so do not treat that link as e355-specific inspection instructions. It lists POS App, POS App with e355 frame, Customer Area, standalone and custom-integration methods, but gives detailed app procedures only for Android/iOS; the other choices are not demonstrated here. See raw lines 19–30.
- Its preparatory menu steps use the e355 confirm-key image plus **9**, Admin PIN, Network → Wi-Fi → TCP/IP settings to note the terminal IP, then point to mobile app installation. The page does not establish a present-day Admin PIN, app availability or network connection. See raw lines 32–45.
- For the **e355 frame** branch, the page links tablet attachment, says to turn off the e355 before insertion, then power it on and open the POS App. The frame branch mentions downloading the app from iTunes while the following section includes Android steps; treat these as historical platform-specific directions rather than a unified cross-platform install path. See raw lines 47–56.
- On **Android**, the app flow asks for API credential details, exposes a Bluetooth/Wi-Fi choice, then instructs entry of terminal IP and **Add Device**. It says the app identifies/synchronizes/verifies configuration, the terminal boards and restarts, and merchant configuration updates after reboot. On **iOS**, the app uses the Bluetooth-menu icon, hostname or IP, “Not Boarded” listing, **Board Device**, restart and update. The described UI states and post-reboot claims are procedure expectations, not independently observed security or payment outcomes. See raw lines 57–80.
- For custom systems the guide routes to Java Native Interface, Windows COM, C, iOS and Android **classic-library integration** guides; it does not supply a Terminal API boarding procedure. Its parent deprecation page later stated e355 transactions and classic-library transactions had separate 2024 cutoffs. Do not apply these old library links as a current migration recommendation. See raw lines 82–92 and [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]].

## Detail locators

- **Security/network prerequisite, methods and mismatched VX675 link:** raw lines 19–30.
- **e355 IP lookup and app download:** raw lines 32–45.
- **Frame power/attachment order:** raw lines 47–56.
- **Android and iOS app boarding branches:** raw lines 57–80.
- **Historical library-integrations navigation:** raw lines 82–92.

## Related

- [[adyen-payment-terminals]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]]
- [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/board-the-terminal-e355/2026-09-15|e355 boarding guide — collected 2026-09-15]]
