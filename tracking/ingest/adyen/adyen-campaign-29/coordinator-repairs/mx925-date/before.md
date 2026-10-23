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

- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-charge-the-e355]] — 2019-modified, 2026-09-15-captured historical e355 charging page for supplied Micro-USB cable, external power and side port; physical charging guidance does not establish current transaction support or payment readiness.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-mx925-user-manual-use-the-admin-menu-mx925]] — 2019-modified, 2026-09-15-captured historical MX925 PIN-gated Admin-menu key sequence and separate unknown-PIN troubleshooting route; no current support or payment proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-attach-and-use-the-e355-frame-attach-the-e355-to-the-frame]] — 2019-modified e355 user-manual frame-attachment steps, captured 2026-09-15 under terminal deprecation; mechanical fit does not establish a tablet connection, boarding or payment readiness.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-attach-and-use-the-e355-frame]] — 2026-09-15-captured historical e355 frame overview linking tablet/terminal attachment, power and removal guides; physical mounting and charging purpose do not establish current transaction support.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-mx925-user-manual-view-terminal-information-mx925]] — 2019-modified, 2026-09-15-captured historical MX925 device-info keypress and screen/QR identifier list; display is not connectivity, credential or payment-readiness proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-make-a-payment-on-the-e355-over-bluetooth-step-3-start-a-transaction]] — 2026-09-15-captured historical e355 boarded/connected Bluetooth POS-app amount, card-prompt and PIN transaction-start sequence; simplified correct-PIN approval wording is not actual authorization or current device proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-view-terminal-information-e355]] — 2019-modified, 2026-09-15-captured historical e355 device-info shortcut and IP/terminal/software/QR identifier list; displayed fields do not establish connectivity, current support or payment outcome.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-attach-and-use-the-e355-frame-remove-the-e355-from-the-frame]] — 2019-modified, 2026-09-15-captured historical e355 frame-removal sequence: unlock screws, press Eject, relock screws, with flat-surface tablet precaution.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-mx925-user-manual]] — 2021-modified, 2026-09-15-captured historical MX925 quickstart with no-new-orders notice, PED power/ETH cabling and damage warning; the linked eVo deprecation table lists MX925 “No more transactions” on 29 March 2024.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-attach-and-use-the-e355-frame-connect-the-e355-frame-to-a-power-source]] — 2019-modified historical e355 frame-power steps specifying a Verifone-certified wall charger and front-panel barrel port for tablet/device charging; no observed charge or payment readiness.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-make-a-payment-on-the-e355-over-bluetooth-remove-configuration-and-reboard]] — 2026-09-15-captured historical e355 Bluetooth-manual procedure for conditionally skipping or destructively erasing merchant configuration before separate reboarding; reboot is not recovery, current support or payment proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-mx925-user-manual-troubleshooting-and-support-mx925]] — 2019-modified, 2026-09-15-captured historical MX925 support route: self-service troubleshooting then email Support if unresolved with merchant account, serial and conditional transaction PSP reference; no repair or current-availability proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-make-a-payment-on-the-e355-over-bluetooth-step-1-clean-the-bluetooth-configuration]] — 2026-09-15-captured deprecated e355 paired-device cleanup path; unpairing requires disconnection, while “unless necessary” opening advice conflicts with the final “all devices” step.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e315-user-manual-turn-on-and-turn-off-the-e315]] — 2019-modified, 2026-09-15-captured historical e315 iPod/iPhone-coupled power-on and iOS-off/disconnect/>5-second pictured-key power-off sequence; not device support or payment-readiness proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-troubleshooting-and-support-e355]] — 2019-modified, 2026-09-15-captured historical e355 support route: linked self-service troubleshooting, then email Support if unresolved with merchant account, terminal serial and conditional transaction PSP reference; no repair proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e315-user-manual-troubleshooting-and-support-e315]] — 2019-modified, 2026-09-15-captured historical e315 self-service-then-Support escalation route requesting merchant account, applicable PSP reference and serial number; no reset, repair or current support proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e315-user-manual]] — 2021-modified, 2026-09-15-captured historical e315 manual overview: no new terminal orders, charge/security-inspect/iOS-network/board quickstart and POS App or own-app routes; “ready to process payments” is not current availability or outcome proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e315-user-manual-use-the-admin-menu-e315]] — 2019-modified, 2026-09-15-captured historical e315 Admin-menu access guide with illustrated version-specific sequences, PIN gate and an unaddressed 1.12–1.13 gap.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-attach-and-use-the-e355-frame-attach-a-tablet-to-the-frame]] — 2019-modified historical e355 frame guide for removable-module, connector-alignment and locking-screw tablet attachment; mechanical fitting does not establish connection, boarding or current transaction support.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual]] — 2021-modified, 2026-09-15-captured historical e355 manual hub for charging, inspection, Wi-Fi and boarding; it says no new orders, while its parent deprecation page lists a 2024 transaction cutoff.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-attach-and-use-the-e355-frame-remove-a-tablet-from-the-frame]] — 2019-modified, 2026-09-15-captured historical e355 tablet-frame removal sequence: release module, lift tablet, reseat/lock module, and use a smooth flat surface to protect the screen.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-understand-the-led-colors-e355]] — 2021-modified, 2026-09-15-captured historical e355 LED status table for sleep, battery, charging, timer fault and gang-charger LED-off behavior; indicator labels are not current support, health or payment proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e315-user-manual-understand-the-led-colors-e315]] — 2019-modified, 2026-09-15-captured historical e315 LED behavior/status table for sleep, low battery, charging, timer fault, normal operation and gang-charger Off condition.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-turn-on-and-off-the-e355]] — 2019-modified, 2026-09-15-captured historical e355 fully-charged power-on/logo cue and >5-second beeping power-off procedure; not boarding or payment-readiness proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e315-user-manual-install-an-ipod-or-iphone-into-the-e315]] — 2019-modified historical e315 iPod/iPhone casing, Lightning-connector and iPod-spacer installation guide; mechanical fit only, not boarding or current device support.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-make-a-payment-on-the-e355-over-bluetooth-troubleshoot-the-bluetooth-connection]] — 2026-09-15-captured historical e355 Bluetooth troubleshooting for protocol mismatch, range/20-second icon check, app-then-terminal restart and conditional unpairing of unnecessary devices; no fix or current support proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-make-a-payment-on-the-e355-over-bluetooth]] — 2019-modified historical e355 Bluetooth pair/reboard/transaction-start navigation and POS App protocol-v2 mismatch warning; successful pairing is not successful boarding or payment, and later deprecation limits device use.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e315-user-manual-charge-the-e315]] — 2019-modified, 2026-09-15-captured historical e315 charging guide for certified wall charger/Micro-USB, eight-hour initial charge without iPod/iPhone, and five-slot-plus-USB gang charger; not current device support or battery-condition proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-mx925-user-manual-inspect-device-security-mx925]] — 2019-modified, 2026-09-15-captured historical MX925 staff inspection guide for weekly tamper checks, third-party identity verification and stop-use/Support escalation.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-inspect-device-security-e355]] — 2019-modified, 2026-09-15-captured historical e355 manual for staff visual tamper checks, weekly inspection and stop-use/Support escalation; not current model or certification proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e315-user-manual-inspect-device-security-e315]] — 2019-modified, 2026-09-15-captured historical e315 visual-tamper, third-party access, PIN-privacy and weekly inspection checklist; stop use and contact Support when in doubt, with no current device eligibility or certification proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-connect-the-e355-to-your-wireless-network]] — 2019-modified, 2026-09-15-captured historical e355 Wi-Fi setup for pre-boarding scan/manual SSID and menu security selections; connection claims and WPA/TKIP-era options do not establish present support or security compliance.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e315-user-manual-board-the-terminal-e315]] — 2019-modified historical e315/iOS boarding and MFI missing-reader troubleshooting guide, captured 2026-09-15 under terminal deprecation.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-make-a-payment-on-the-e355-over-bluetooth-step-2-pair-the-e355-with-a-mobile-device]] — 2026-09-15-captured historical e355 Bluetooth pairing/boarding step for iOS or Android, including frame exception, OS-mismatch escalation and through-v36 iOS restart behavior; no current support or payment-outcome proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-mx925-user-manual-board-the-terminal-mx925]] — 2019-modified, 2026-09-15-captured historical MX925 boarding guide for security/network prerequisites, merchant-account OTP and POS App paths; later deprecation lists no transactions after 29 March 2024.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-board-the-terminal-e355]] — 2019-modified, 2026-09-15-captured historical e355 POS App boarding guide for security/network prechecks, frame, Android/iOS and classic-library routes; its quick-start link points to VX675 and current e355 support is not established.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] — 2021-modified, 2026-09-15-captured historical eVo/Verix terminal retirement and VOS/Android replacement table, with separate 29 March 2024 device and 31 March 2024 classic-library transaction cutoffs; not current model or PCI eligibility proof.


- [[source-adyen-docs-industries-major-sports-event]] — 2026-09-15 Adyen in-person sports-event planning guide for international visitors, conditional connectivity/offline options and terminal preparation; recommendations do not establish device support, merchant enablement, live resilience or payment outcomes.


- [[source-adyen-docs-point-of-sale-sneak-preview]] — 2026-09-15 captured Adyen POS software-preview pointer naming v1.135 as then-next release without feature details; links release notes and manual/LTS update guidance, with no current availability or deployment proof.


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
