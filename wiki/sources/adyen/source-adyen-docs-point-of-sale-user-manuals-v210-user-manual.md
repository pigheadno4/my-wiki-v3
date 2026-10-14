---
title: "Adyen Docs: V210 user manual"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/v210-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/v210-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, v210, terminal-manual]
---

## Overview

Adyen's 2026-09-15 V210 user manual covers physical setup and local operation of the V210 payment terminal: receipt paper, power, network, boarding, connection diagnostics, menus, battery care, totals, and receipts. The V210 is also listed in the dated standalone-terminal route; this manual does not prove current model availability, regional eligibility, device security, or a successful transaction. See [[adyen-payment-terminals]], [[adyen-standalone-terminals]], and [[adyen]].

## Key takeaways

- Inspect the tamper-evident box seal and check the box and terminal serial numbers against each other and, when accessible, the Customer Area order. Inspect for physical tampering and contact Adyen Support immediately if a check fails. This is a required receipt inspection procedure, not a security certification.
- Initial setup is paper roll, power and at least four hours of charging, network configuration, boarding to the selected store, then a payments-platform connection test. Boarding can take up to 30 minutes; if the boarding prompt is absent, the manual says to wait for the next platform synchronization (on average three hours) and retry. Test the POS-system connection only for an integrated POS setup; standalone operation skips that test.
- Wi-Fi can be configured during setup; changing it after boarding uses Settings > Network with a passcode. The manual describes cellular failover with a preinstalled eSIM but says terminals boarded before 2022 may lack activation if no SIM subscription was configured then. Physical SIM replacement requires powering off and removing the battery; do not use metal tools in the slot.
- The PSP diagnostic has a specific `Receiving data` red-cross/`No Error` exception that the manual says still indicates a successful platform connection. For a POS-system connection, check Terminal API diagnostics and four endpoint URL tests. These tests are connection checks, not proof of payment processing.
- The V210 menu table is qualified by terminal software version: from 1.90, Adyen says Android and non-Android terminals share its menu structure; earlier non-Android versions may use the old menu. Device info and Diagnostics need no menu passcode; Configuration, Network, Software and Power need Admin & Settings; standalone normal and special transactions need Transactions, with Refunds additionally required for Refund and MOTO refund. The special menu lists `Bypass PIN`, but the listing alone does not establish when bypass is allowed or a payment's outcome. The standalone Payment button starts a normal payment without a menu passcode.
- Long-term battery storage should avoid heat and charge levels above 70% or below 40%; inspect for leakage or swelling every six months. Dispose of faulty batteries under local rules and do not include them with returned terminals. Totals reset starts a new reporting period; the manual also describes receipt reprinting.

## Detail locators

- Keypad, supplied power/SIM/57 x 40 mm paper, and startup: [[raw/adyen/docs/point-of-sale/user-manuals/v210-user-manual/2026-09-15#Keypad keys|Keypad keys]], [[raw/adyen/docs/point-of-sale/user-manuals/v210-user-manual/2026-09-15#Supplied components|Supplied components]], and [[raw/adyen/docs/point-of-sale/user-manuals/v210-user-manual/2026-09-15#Get started|Get started]].
- Serial and tamper inspection: [[raw/adyen/docs/point-of-sale/user-manuals/v210-user-manual/2026-09-15#Inspect the terminal|Inspect the terminal]]. Wi-Fi, cellular caveat and SIM handling: [[raw/adyen/docs/point-of-sale/user-manuals/v210-user-manual/2026-09-15#Connect to your network|Connect to your network]], [[raw/adyen/docs/point-of-sale/user-manuals/v210-user-manual/2026-09-15#Cellular failover|Cellular failover]], and [[raw/adyen/docs/point-of-sale/user-manuals/v210-user-manual/2026-09-15#Replace physical SIM card|Replace physical SIM card]].
- Platform and integrated-POS diagnostic conditions: [[raw/adyen/docs/point-of-sale/user-manuals/v210-user-manual/2026-09-15#Test the payments platform connection|Test the payments platform connection]] and [[raw/adyen/docs/point-of-sale/user-manuals/v210-user-manual/2026-09-15#Test the POS system connection|Test the POS system connection]].
- Passcodes, version 1.90 menu qualification and Bypass PIN menu label: [[raw/adyen/docs/point-of-sale/user-manuals/v210-user-manual/2026-09-15#Payment terminal menus|Payment terminal menus]]. Power and battery warnings: [[raw/adyen/docs/point-of-sale/user-manuals/v210-user-manual/2026-09-15#Turn on/off|Turn on/off]] and [[raw/adyen/docs/point-of-sale/user-manuals/v210-user-manual/2026-09-15#Maintain battery performance|Maintain battery performance]].
- Totals reset, receipt reprint and standalone route: [[raw/adyen/docs/point-of-sale/user-manuals/v210-user-manual/2026-09-15#View, print, and reset totals|View, print, and reset totals]], [[raw/adyen/docs/point-of-sale/user-manuals/v210-user-manual/2026-09-15#Reprint transaction receipt|Reprint transaction receipt]], and [[raw/adyen/docs/point-of-sale/user-manuals/v210-user-manual/2026-09-15#Standalone solution|Standalone solution]].

## Related

- [[adyen-payment-terminals]] — physical payment-terminal model and safety route, pending coordinator promotion.
- [[adyen-standalone-terminals]] — standalone solution scope; its feature procedures are separate from this hardware manual.
- [[adyen-terminal-api]] — integrated POS-to-terminal messaging boundary.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/v210-user-manual/2026-09-15|Adyen V210 user manual, 2026-09-15 snapshot]]
