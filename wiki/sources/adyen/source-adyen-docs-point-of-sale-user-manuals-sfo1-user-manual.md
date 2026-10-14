---
title: "Adyen SFO1 payment terminal user manual"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/sfo1-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/sfo1-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminal, sfo1, hardware, boarding, diagnostics]
---

## Overview

This dated SFO1 manual covers physical setup and operation of Adyen's **SFO1 payment terminal**, which combines a customer-facing display and payment terminal. It is a countertop, pole- or wall-mountable device, separate from a merchant phone running Mobile POS and from an NYC1 reader paired to a phone. The separate Adyen Android-terminal catalog lists SFO1 as a Datecs Android 13 model in its 2026-09-15 snapshot; that catalog warns model availability varies by region. The manual is operational guidance, not proof of current supply, account eligibility, cardholder PIN support or payment success. See [[adyen-payment-terminals]] and [[adyen-android-terminals]].

## Key takeaways

- Before use, check that the box is unopened, match the device serial number to the box, and inspect for missing screws, extra wires or labels, holes, or attached objects. If Customer Area access is available, also match the box serial number to the order and check the carrier delivery record. The manual says to contact Adyen Support **immediately** if any check fails. See raw § Inspect the terminal (lines 59–74).
- Initial setup connects power through the adapter for Wi-Fi or through the separately ordered Ethernet-to-USB-C dongle for LAN, configures the network, and then follows either the Customer Area one-time-password route or **Board the terminal → select store → Confirm**. The manual says boarding can take up to 30 minutes; if the boarding option is absent, wait for a platform sync (stated average three hours) and try again. See raw §§ Supplied components, Get started and Connect to your network (lines 23–57, 76–117).
- Wi-Fi and Ethernet LAN are documented network routes. The manual describes preinstalled eSIM cellular failover when internet connectivity fails and says cellular can be used to board; it does not give a current coverage guarantee. After boarding, changing Wi-Fi under **Settings → Network** requires a passcode. See raw § Connect to your network (lines 76–117).
- The **PSP connection** diagnostic checks the terminal's link to Adyen. The manual says a red **Receiving data** cross paired with **No Error** can still mean a successful platform connection. For a POS system, run **Terminal API** and **Endpoints** diagnostics; the latter tests four URLs. A successful diagnostic is a point-in-time connectivity check, not an authorization, capture or settlement result. See raw §§ Test the payments platform connection and Test the POS system connection (lines 119–137).
- The dated menu table lists Device info and Diagnostics without passcodes, **Admin & Settings** for the separate Configuration, Network, Software and Power menus, and **Transactions** for History and Totals. Yet its Device info description also says software version can be updated there; the manual does not reconcile that no-passcode listing with the protected Software menu, so do not infer that every software-update path has the same passcode requirement. Totals includes viewing, printing **and resetting** transaction totals; History can reprint receipts for approved transactions. A remote troubleshooting session requires an operator to select **Start session** and enter a passcode, giving support screen visibility and interaction. See raw §§ Payment terminal menus and Troubleshooting (lines 158–183, 199–213).
- On power-up after a long idle period, a maintenance call may take 10–20 minutes. The contactless troubleshooting note says the original power adapter matters because NFC may malfunction with another adapter, and directs hardware diagnosis from the terminal. See raw §§ Turn on/off and Troubleshooting tips (lines 139–156, 215–225).

## Detail locators

- Raw §§ Supplied components, Get started and Inspect the terminal: SFO1 identity, mounts, boarding choices and tamper escalation (lines 23–74).
- Raw §§ Connect to your network and connection tests: power, dongle, Wi-Fi, eSIM and point-in-time diagnostics (lines 76–137).
- Raw §§ Payment terminal menus, Device info and Troubleshooting: protected settings, totals reset, store display and assisted session (lines 158–225).

## Related

- [[adyen-payment-terminals]] — model-specific physical-terminal route.
- [[adyen-android-terminals]] — dated Android-terminal model catalog and on-terminal app boundary.
- [[adyen-terminal-management]] — fleet assignment and configuration outside this manual.
- [[adyen-mobile-pos]] — merchant-phone in-person route, distinct from SFO1.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/sfo1-user-manual/2026-09-15|SFO1 user manual, fetched 2026-09-15]]
