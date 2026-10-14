---
title: "Adyen Docs: S1F2 user manual"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/s1f2-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/s1f2-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, s1f2, terminal-manual]
---

## Overview

Adyen's S1F2 user manual explains first setup and local operation of the S1F2 payment terminal, including physical inspection, receipt paper, charging, network connection, store confirmation, menus, and device care. The S1F2L variant adds a barcode-scanning camera. This model manual is a dated operational snapshot; it does not state an Android OS version, current model or account eligibility, US-specific PIN conditions, or prove a device is safe, boarded, or ready for successful payments. See [[adyen-android-terminals]], [[adyen-terminal-management]], and [[adyen]].

## Key takeaways

- Before use, inspect the shipping seal and match the box serial number against the Customer Area order when accessible, then match the device serial number to the box and inspect for tampering. Contact Adyen Support immediately if a check fails. This is an inspection procedure, not a guarantee that any individual device is secure.
- First setup is inspect, insert the paper roll, connect the supplied power equipment and charge for at least four hours, select language, connect to a network, then confirm or change the shown store. If the store screen does not appear, the guide says to wait for the next platform synchronization (on average three hours) and try again. Completion of these steps is the manual's setup claim, not evidence of a particular terminal's actual boarding state.
- Wi-Fi setup and later changes use the terminal menus; later Network settings require a passcode. The guide describes automatic 3G/4G cellular failover and a preinstalled eSIM for boarding, with a caveat that some terminals boarded before 2022 may lack an activated SIM if there was no SIM subscription. The physical-SIM replacement section warns against metal tools in the slot.
- For long storage, keep batteries cool and dry, avoid storing above 70% or below 40% charge, and inspect for leakage or swelling every six months. Do not put a faulty battery in a terminal return package; follow local disposal rules. Use the supplied Adyen USB-C charging cable and regional plug.
- The Settings menu shows device details, network, configuration, diagnostics, apps and power. Admin & Settings passcode protects Apps, Configuration, Network, software-version changes, and Power; Transactions passcode protects history, totals and new transactions, with an additional Refunds passcode for a new refund. A standalone terminal can start a normal payment from the Payment button without a menu passcode. These are local menu access descriptions, not payment or refund outcome guarantees.
- The Apps menu can show installed apps and certificates and carry out scheduled install or removal when opened. Kiosk mode and airline airplane mode are separate features; airplane mode needs Adyen Support enablement and disables Wi-Fi, Bluetooth, and cellular while on.

## Detail locators

- Included model variants and components: [[raw/adyen/docs/point-of-sale/user-manuals/s1f2-user-manual/2026-09-15#Supplied components|Supplied components]]. Inspection, paper, store confirmation and startup timing: [[raw/adyen/docs/point-of-sale/user-manuals/s1f2-user-manual/2026-09-15#Get started|Get started]] and [[raw/adyen/docs/point-of-sale/user-manuals/s1f2-user-manual/2026-09-15#Inspect the terminal|Inspect the terminal]].
- Wi-Fi setup, cellular failover and the older-SIM exception: [[raw/adyen/docs/point-of-sale/user-manuals/s1f2-user-manual/2026-09-15#Connect to your network|Connect to your network]], [[raw/adyen/docs/point-of-sale/user-manuals/s1f2-user-manual/2026-09-15#Cellular 3G/4G failover|Cellular 3G/4G failover]], and [[raw/adyen/docs/point-of-sale/user-manuals/s1f2-user-manual/2026-09-15#Replace physical SIM card|Replace physical SIM card]].
- Battery storage/return warnings and charging cable handling: [[raw/adyen/docs/point-of-sale/user-manuals/s1f2-user-manual/2026-09-15#Maintain battery performance|Maintain battery performance]] and [[raw/adyen/docs/point-of-sale/user-manuals/s1f2-user-manual/2026-09-15#Use the USB-C charging cable|Use the USB-C charging cable]].
- Menu functions, apps and exact passcode boundary: [[raw/adyen/docs/point-of-sale/user-manuals/s1f2-user-manual/2026-09-15#Payment terminal menus|Payment terminal menus]]. Totals reporting: [[raw/adyen/docs/point-of-sale/user-manuals/s1f2-user-manual/2026-09-15#View, print, and reset totals|View, print, and reset totals]].
- Standalone payments, kiosk, airline airplane mode, and support route: [[raw/adyen/docs/point-of-sale/user-manuals/s1f2-user-manual/2026-09-15#Standalone solution|Standalone solution]], [[raw/adyen/docs/point-of-sale/user-manuals/s1f2-user-manual/2026-09-15#Kiosk mode|Kiosk mode]], [[raw/adyen/docs/point-of-sale/user-manuals/s1f2-user-manual/2026-09-15#Airplane mode|Airplane mode]], and [[raw/adyen/docs/point-of-sale/user-manuals/s1f2-user-manual/2026-09-15#Troubleshooting|Troubleshooting]].

## Related

- [[adyen-android-terminals]] — Android-terminal family and app routes; consult its version-qualified overview for model/OS claims.
- [[adyen-terminal-management]] — fleet assignment and boarding boundary.
- [[adyen-standalone-terminals]] — standalone transaction flow beyond this device manual.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/s1f2-user-manual/2026-09-15|Adyen S1F2 user manual, 2026-09-15 snapshot]]
