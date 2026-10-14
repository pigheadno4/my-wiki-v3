---
title: "Adyen Payment Terminals"
type: concept
category: technology
tags: [adyen, point-of-sale, payment-terminals, hardware]
---

## Definition

Adyen payment terminals are physical in-person devices. This hub collects model-specific setup and maintenance guidance; the V400m with Bluetooth base has its own inspection, charging, networking and boarding sequence. The V400m manual describes a Bluetooth base station that supplies Ethernet LAN access while the terminal is docked or undocked and charges it while docked. This hardware setup is separate from [[adyen-terminal-management]] fleet administration, [[adyen-terminal-api]] POS messaging, [[adyen-android-terminals]] on-terminal app deployment, and [[adyen-mobile-card-readers]] paired mobile reader operation.

## Operating boundary

The 2026-09-15 V400m manual requires shipment and device tamper checks with immediate Adyen Support contact if they fail. Its initial sequence boards the terminal over temporary Wi-Fi before first docking/pairing because the base obtains software from the terminal and can become stuck if connected too early. For this V400m, a Successful PSP connection diagnostic reports connection to Adyen's platform at the time of that test. When used with a POS system, Successful Terminal API and Endpoints diagnostics report those checks at their test time. Those results do not prove continued connectivity, payment authorization or settlement. The manual's menu/software, cellular, battery and model details are a dated snapshot; confirm current model and account availability separately.

## Sources

- [[source-adyen-docs-point-of-sale-pos-troubleshooting]] — Adyen terminal troubleshooting directory (2025-04-24 modified; 2026-09-15 capture) routing power-on branches, lost/stolen reporting, manuals, connection/hardware tests and Android remote sessions to separate guides; it contains no diagnostic procedure or payment result.


- [[source-adyen-docs-point-of-sale-pos-troubleshooting-hardware-tests]] — Adyen Docs hardware-diagnostic guide captured 2026-09-15 for non-legacy terminal chip, swipe, NFC and conditional keypad checks, result handling and log submission.


- [[source-adyen-docs-point-of-sale-user-manuals-p400-plus-user-manual]] — P400 Plus physical-terminal manual (2026-09-15 snapshot) for dated order/repair notice, tamper inspection, safe dongle cabling, network/store boarding, diagnostics and version-qualified passcode menus.


- [[source-adyen-docs-point-of-sale-pos-troubleshooting-connection-tests]] — 2026-09-15 terminal-run PSP, Terminal API and Endpoints connection-test guide for non-legacy physical terminals, including local/cloud applicability, diagnostic stages and escalation.


- [[source-adyen-docs-point-of-sale-user-manuals-m400-user-manual]] — M400 physical-terminal manual captured 2026-09-15 for discontinued/repair notice, tamper inspection, dongle and network setup, store boarding, point-in-time diagnostics, and protected menus.


- [[source-adyen-docs-point-of-sale-user-manuals-s1u2-user-manual]] — S1U2 unattended Android physical-terminal manual (2020 last-modified; 2026-09-15 capture) for tamper inspection, store-first boarding, power/network, menus and support.


- [[source-adyen-docs-point-of-sale-user-manuals-sfo1-user-manual]] — SFO1 physical payment-terminal manual (2025-04-10 modified; 2026-09-15 capture) for combined customer display/payment device, tamper inspection, network/store boarding, diagnostics, protected menus and power/NFC care.


- [[source-adyen-docs-point-of-sale-user-manuals-ux300-user-manual]] — UX300 three-device unattended terminal manual (2026-09-15 snapshot) for dated discontinuation/repair notice, store-before-boarding setup, cable and ARS safety, UX100 Admin controls and software update.


- [[source-adyen-docs-point-of-sale-user-manuals-e280-user-manual]] — e280 physical-terminal manual captured 2026-09-15 for discontinued ordering, tamper inspection, charging, Wi-Fi/store boarding, diagnostics, battery precautions and version-qualified menus.


- [[source-adyen-docs-point-of-sale-user-manuals-p630-user-manual]] — P630 physical-terminal manual (2026-09-15 capture) for tamper inspection, interference clearance, store boarding, network/power, keypad menus, passcodes and local totals.


- [[source-adyen-docs-point-of-sale-user-manuals-m450-user-manual]] — M450 physical-terminal manual (2026-09-15 snapshot) for tamper checks, store confirmation, Ethernet/Wi-Fi and diagnostics, menu passcodes, power and 30.5 cm deactivator separation.


- [[source-adyen-docs-point-of-sale-user-manuals-ux410-user-manual]] — UX410 unattended two-unit contactless terminal manual (2026-09-15 snapshot) for installation, mandatory store assignment, LED boarding/error cues, tamper escalation and dated availability/repair notice.


- [[source-adyen-docs-point-of-sale-user-manuals-v400c-user-manual]] — V400c Plus physical-terminal manual (2026-09-15 snapshot) for discontinued-model and repair notice, inspection, dongle cabling, store boarding, diagnostics, menu passcodes and totals.


- [[source-adyen-docs-point-of-sale-user-manuals-ams1-user-manual]] — AMS1 physical-terminal manual (2026-09-15 snapshot) for tamper inspection, first charge/store confirmation, network/eSIM caveat, battery/USB safety, protected menus, totals and remote support.


- [[source-adyen-docs-point-of-sale-menu-access]] — Adyen Menus and passcodes guide (2026-09-15 snapshot) for protected terminal controls, passcode management, software-qualified Android and non-Android menus, and action effects.


- [[source-adyen-docs-point-of-sale-classic-library-deprecation]] — Adyen Docs deprecation notice captured 2026-09-15 for dated eVo PCI/repair/transaction deadlines and example VOS replacement models.


- [[source-adyen-docs-point-of-sale-managing-terminals-security-inspection]] — 2026-09-15 Adyen physical-terminal security-inspection guide for delivery and regular tamper checks, stop-use escalation, suspicious activity, and lost/stolen reporting.


- [[source-adyen-docs-point-of-sale-managing-terminals-battery-management]] — 2026-09-15 Adyen battery-powered terminal guide for software-qualified sleep defaults, charge thresholds/monitoring, model-specific chargers and spares, network/app drain, and storage ranges.


- [[source-adyen-docs-point-of-sale-user-manuals]] — Adyen physical-terminal manuals directory (2026-09-15 snapshot) with per-model use case, region, suitability, connectivity, feature and PCI labels plus dated ordering exceptions.


- [[source-adyen-docs-point-of-sale-user-manuals-s1e4pro-user-manual]] — S1E4Pro manual captured 2026-09-15 for tamper inspection, on-device store confirmation, connectivity, charging/battery care, menu passcodes, kiosk/airplane modes and remote assistance.


- [[source-adyen-docs-point-of-sale-user-manuals-e285-user-manual]] — Adyen e285p/e285 physical-terminal user manual captured 2026-09-15 for discontinued-model notice, inspection, setup/boarding, connectivity, battery care, menus and diagnostics; model and safety claims are snapshot-qualified.


- [[source-adyen-docs-point-of-sale-user-manuals-v240m-user-manual]] — 2026-09-15 V240m Plus model manual for tamper inspection, power/network and store boarding, point-in-time diagnostics, no-4G cellular limit, battery precautions, menus, and totals.


- [[source-adyen-docs-point-of-sale-user-manuals-v210-user-manual]] — 2026-09-15 V210 device manual for inspection, network and store boarding, version-qualified menus, battery care, and local receipts.


- [[source-adyen-docs-point-of-sale-user-manuals-v400m-user-manual]] — 2026-09-15 V400m manual for discontinued-model notice, physical inspection, network/boarding and diagnostics, SIM/battery handling, menus and totals.


- [[source-adyen-docs-point-of-sale-user-manuals-v400m-with-bt-base]] — V400m Bluetooth base manual (2026-09-15 snapshot) for inspection, first boarding before docking, Ethernet/Bluetooth pairing, diagnostics, menu passcodes, totals and battery care.
