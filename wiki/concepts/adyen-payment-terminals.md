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

- [[source-adyen-docs-point-of-sale-managing-terminals-security-inspection]] — 2026-09-15 Adyen physical-terminal security-inspection guide for delivery and regular tamper checks, stop-use escalation, suspicious activity, and lost/stolen reporting.


- [[source-adyen-docs-point-of-sale-managing-terminals-battery-management]] — 2026-09-15 Adyen battery-powered terminal guide for software-qualified sleep defaults, charge thresholds/monitoring, model-specific chargers and spares, network/app drain, and storage ranges.


- [[source-adyen-docs-point-of-sale-user-manuals]] — Adyen physical-terminal manuals directory (2026-09-15 snapshot) with per-model use case, region, suitability, connectivity, feature and PCI labels plus dated ordering exceptions.


- [[source-adyen-docs-point-of-sale-user-manuals-s1e4pro-user-manual]] — S1E4Pro manual captured 2026-09-15 for tamper inspection, on-device store confirmation, connectivity, charging/battery care, menu passcodes, kiosk/airplane modes and remote assistance.


- [[source-adyen-docs-point-of-sale-user-manuals-e285-user-manual]] — Adyen e285p/e285 physical-terminal user manual captured 2026-09-15 for discontinued-model notice, inspection, setup/boarding, connectivity, battery care, menus and diagnostics; model and safety claims are snapshot-qualified.


- [[source-adyen-docs-point-of-sale-user-manuals-v240m-user-manual]] — 2026-09-15 V240m Plus model manual for tamper inspection, power/network and store boarding, point-in-time diagnostics, no-4G cellular limit, battery precautions, menus, and totals.


- [[source-adyen-docs-point-of-sale-user-manuals-v210-user-manual]] — 2026-09-15 V210 device manual for inspection, network and store boarding, version-qualified menus, battery care, and local receipts.


- [[source-adyen-docs-point-of-sale-user-manuals-v400m-user-manual]] — 2026-09-15 V400m manual for discontinued-model notice, physical inspection, network/boarding and diagnostics, SIM/battery handling, menus and totals.


- [[source-adyen-docs-point-of-sale-user-manuals-v400m-with-bt-base]] — V400m Bluetooth base manual (2026-09-15 snapshot) for inspection, first boarding before docking, Ethernet/Bluetooth pairing, diagnostics, menu passcodes, totals and battery care.
