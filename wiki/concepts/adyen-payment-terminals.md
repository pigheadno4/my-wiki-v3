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

- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-user-manual-troubleshooting-and-support-vx820]] — 2019-modified, 2026-09-15-captured historical VX820 non-Duet troubleshooting-first and Support escalation route, with merchant account, conditional transaction PSP reference and device serial; the separate eVo schedule ended VX820 transactions 29 March 2024, so this is not current service proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-user-manual-use-the-admin-menu-vx820]] — 2019-modified, 2026-09-15-captured historical VX820 non-Duet pictured-key-plus-9 and Admin-PIN menu access; listed removal/reset functions are not execution, and the separate eVo table gives the 29 March 2024 transaction cutoff.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-user-manual-view-terminal-information-vx820]] — 2019-modified, 2026-09-15-captured historical **VX820 non-Duet** Quick Info display guide for IP, terminal/software identifiers and QR contents; display is not connection, boarding or payment proof, and the eVo table lists no more VX820 transactions on 29 March 2024.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-user-manual-inspect-device-security-vx820]] — 2019-modified historical VX820 non-Duet weekly visual-security checklist with damaged/tampered-device stop-use and Support escalation; inspection guidance does not prove device safety or post-cutoff transaction support.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-user-manual-board-the-terminal-vx820]] — 2019-modified historical **VX820 non-Duet** internet/security-prechecked POS App boarding paths and classic-library links; the separate deprecation table ends VX820 transactions on 29 March 2024, so old ready-to-process wording is not current support proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-user-manual]] — 2021-modified, 2026-09-15-captured historical **VX820 non-Duet** PED/dongle quickstart and wrong-port damage warning; the separate eVo table lists VX820 "No more transactions" on 29 March 2024.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx675-user-manual-turn-on-and-turn-off-the-vx675]] — 2019-modified, 2026-09-15-captured historical VX675 image-led power-on/startup-screen and power-off/beep cues; power state does not establish boarding or transaction support after the separate 29 March 2024 model cutoff.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx680-user-manual-charge-the-vx680]] — 2019-modified, 2026-09-15-captured historical VX680 cradle/power-supply charging guide with at-least-six-hour and steady-LED condition; no battery-health or current transaction-support proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx690-user-manual-use-the-admin-menu-vx690]] — 2019-modified, 2026-09-15-captured historical VX690 image-key-plus-9/Admin-PIN menu guide listing configuration removal and totals reset purposes; displaying the menu is not execution or current support proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx680-user-manual-use-the-admin-menu-vx680]] — 2019-modified historical VX680 pictured-key-plus-9 Admin-menu access with PIN gate and listed network/installer/merchant/totals purposes; configuration removal and totals reset are not shown to occur.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx675-user-manual-use-the-admin-menu-vx675]] — 2019-modified, 2026-09-15-captured historical VX675 Admin-menu guide: simultaneous pictured key + 9, PIN gate, and listed configuration-removal and totals-reset purposes; no action outcome or current-support proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-duet-user-manual-use-the-admin-menu-vx820-duet]] — 2019-modified historical VX820 Duet pictured-key-plus-9 Admin-menu access with PIN gate and listed network/installer/merchant/totals purposes; listing configuration removal or totals reset is not execution proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx690-user-manual-connect-a-vx690-to-a-base-station-with-bluetooth-understand-the-bluetooth-base-station-led-colors]] — 2021-modified, 2026-09-15-captured historical VX690 Bluetooth-base LED table for power-on, slow-blue discover, quick-blue pairing and steady-blue connected labels; no payment or security proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx680-user-manual-turn-on-and-turn-off-the-vx680]] — 2019-modified, 2026-09-15-captured historical VX680 pictured-key power-on/off guide with conditional boot logo and repeated shutdown beeps; power or logo display is not boarding or payment proof, and the parent table lists no more VX680 transactions on 29 March 2024.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx690-user-manual-view-terminal-information-vx690]] — 2019-modified, 2026-09-15-captured historical VX690 Quick Info shortcut and IP/terminal/software/QR identifier list; displayed fields do not prove connectivity or current transaction support.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx675-user-manual-view-terminal-information-vx675]] — 2019-modified historical VX675 Quick Info shortcut and displayed IP, terminal ID, software and QR-encoded network/store/merchant identifiers; fields do not prove connectivity, current support or payment readiness.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-duet-user-manual-view-terminal-information-vx820-duet]] — 2019-modified, 2026-09-15-captured historical VX820 Duet Quick Info guide for IP, terminal ID, software version and QR-encoded device/store identifiers; display fields do not prove connectivity or current transaction support.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx680-user-manual-troubleshooting-and-support-vx680]] — 2019-modified, 2026-09-15-captured historical VX680 self-service-then-Support route with merchant account, serial number and conditional transaction PSP reference; no repair or current-support proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx690-user-manual-troubleshooting-and-support-vx690]] — 2019-modified, 2026-09-15-captured historical VX690 self-service-then-Support route requesting merchant account, serial and conditional transaction PSP reference; no repair or current-support proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx680-user-manual-print-shift-and-end-of-day-reports-vx680]] — 2020-modified, 2026-09-15-captured historical VX680 terminal-local since-last-reset totals printout with Admin-PIN-gated access and a Yes step to reset the totals counter; conditional periodic-reset advice differs from the numbered Yes-reset step, and the printout is not settlement or reconciliation proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-duet-user-manual-troubleshooting-and-support-vx820-duet]] — 2019-modified historical VX820 Duet self-service-then-Support route requesting merchant account, conditional transaction PSP reference and serial number; no repair, current channel or transaction-support proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx675-user-manual-troubleshooting-and-support-vx675]] — 2019-modified, 2026-09-15-captured historical VX675 self-service-then-Support route with merchant account, serial number and conditional transaction PSP reference; no repair or current-support proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx680-user-manual-view-terminal-information-vx680]] — 2019-modified, 2026-09-15-captured historical VX680 Quick Info route for IP address, terminal ID, software version and QR-encoded device/store identifiers; display fields do not prove connectivity or current transaction support.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx690-user-manual-print-shift-and-end-of-day-reports-vx690]] — 2019-modified, 2026-09-15-captured historical VX690 since-last-reset totals print guide with an explicit post-print counter reset step; not settlement or payout proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx675-user-manual-print-shift-and-end-of-day-reports-vx675]] — 2019-modified historical VX675 device-totals print guide: amount summary since last counter reset, Admin PIN, and separate post-print Yes action that resets later report windows; not settlement or bank reconciliation evidence.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx690-user-manual-make-special-payments-vx690]] — 2019-modified, 2026-09-15-captured historical VX690 PIN-protected, configuration-dependent Special Payments menu for normal/manual-entry screens and a separate refund route; menu access does not prove payment success or current support.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-duet-user-manual-make-special-payments-vx820-duet]] — 2019-modified historical VX820 Duet PIN-gated special-payment menu with merchant-configuration-dependent normal, manual-card-entry and refund routes; listed options and flow wording do not establish current availability or transaction outcomes.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx680-user-manual-make-special-payments-vx680]] — 2019-modified, 2026-09-15-captured historical VX680 PIN-gated Special Payments menu with configuration-dependent normal/manual-entry and refund routes; menu presence is not current availability or payment outcome proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx675-user-manual-make-special-payments-vx675]] — 2019-modified, 2026-09-15-captured historical VX675 Special Payments menu for configuration-dependent normal/manual entry and refund navigation, bounded by the later 29 March 2024 “No more transactions” date.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-duet-user-manual-print-shift-and-end-of-day-reports-vx820-duet]] — 2020-modified, 2026-09-15-captured historical VX820 Duet terminal-local totals print/reset procedure since last counter reset; conditional periodic-reset advice and numbered Yes-reset step differ, and the printout is not settlement or reconciliation proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx690-user-manual-perform-a-refund-vx690]] — 2019-modified, 2026-09-15-captured historical VX690 standalone refund guide with per-device enablement, password/PIN wording and unsynchronized-data warning; it gives no completed-refund proof and is bounded by the 29 March 2024 eVo transaction cutoff.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx680-user-manual-perform-a-refund-vx680]] — 2019-modified, 2026-09-15-captured historical VX680 standalone refund steps, conditional on per-device enablement and password/PIN prompts; no completed refund or current transaction support proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx675-user-manual-perform-a-refund-vx675]] — 2019-modified, 2026-09-15-captured historical VX675 standalone refund initiation guide with per-device enablement, unsynced-data warning and password/PIN wording; no completed refund or current transaction support proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-duet-user-manual-perform-a-refund-vx820-duet]] — 2019-modified, 2026-09-15-captured historical VX820 Duet standalone-refund initiation guide: per-device enablement, password/PIN wording and amount entry, plus unsynchronized-data icon warning; no refund completion proof, and the parent table lists no more VX820 Duet transactions on 29 March 2024.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-duet-user-manual-install-or-replace-paper-rolls-vx820-duet]] — 2019-modified historical VX820 Duet receipt-paper guide for specified thermal-roll dimensions, bottom-feed orientation and glue-residue clearance; its no-paper payment warning is model-specific and paper loading does not prove current transaction support.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx690-user-manual-install-or-replace-paper-rolls-vx690]] — 2019-modified, 2026-09-15-captured historical VX690 57 × 40 × 12 mm thermal-paper and top-latch loading guide; its no-paper payment statement is bounded by the eVo table's 29 March 2024 “No more transactions” date.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx690-user-manual-inspect-device-security-vx690]] — 2019-modified, 2026-09-15-captured historical VX690 staff tamper/PIN-privacy checklist, weekly visual checks and stop-use/Support escalation; inspection guidance is not certification or current transaction proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx680-user-manual-inspect-device-security-vx680]] — 2019-modified, 2026-09-15-captured historical VX680 staff device-integrity guide: inspect weekly for damage, skimmers and tampering, verify third-party access, report suspicions, and stop use/contact Support when in doubt; old “certified” wording does not establish present certification, and the parent eVo table lists no more VX680 transactions on 29 March 2024.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx675-user-manual-inspect-device-security-vx675]] — 2019-modified, 2026-09-15-captured historical VX675 staff tamper-inspection checklist with weekly checks, third-party verification, PIN privacy and stop-use/Support escalation; the page is not current certification or transaction-support proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx680-user-manual-install-or-replace-paper-rolls-vx680]] — 2019-modified, 2026-09-15-captured historical VX680 thermal-paper specification and roll-loading guide; its no-paper payment statement does not override the eVo table's 29 March 2024 “No more transactions” date.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx675-user-manual-connect-the-vx675-to-your-wireless-network]] — 2019-modified, 2026-09-15-captured historical VX675 Wi-Fi setup guide for charged-device/Admin-menu preconditions and scan/manual SSID routes; legacy WPA/TKIP options and expected connection wording do not establish current security, connectivity or transaction support after the separate 29 March 2024 model cutoff.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-duet-user-manual-inspect-device-security-vx820-duet]] — 2019-modified historical VX820 Duet staff integrity checklist covering visual/tamper and third-party checks, weekly inspection, stop-use and Support escalation; inspection does not establish current certification or transaction support.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx675-user-manual-install-or-replace-paper-rolls-vx675]] — 2019-modified, 2026-09-15-captured historical VX675 receipt-paper dimensions and roll-loading procedure; its no-paper/no-payment wording does not override the later 29 March 2024 “No more transactions” date.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx690-user-manual-connect-the-vx690-to-your-wireless-network]] — 2021-modified historical VX690 Wi-Fi guide with charged-device and conditional Admin-PIN prerequisites, scan/manual SSID branches and dated WPA/WPA-2/TKIP/CCMP menus; setup does not prove boarding, current support or payment processing.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx690-user-manual-connect-a-vx690-to-a-base-station-with-bluetooth]] — 2019-modified, 2026-09-15-captured historical VX690 Bluetooth-base pairing guide with DHCP, Wi-Fi-profile reset/restart, powered Ethernet base and local connection-status check; no current device or payment proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-duet-user-manual]] — 2021-modified, 2026-09-15-captured historical VX820 Duet PED/printer-base quickstart and cabling warning; its separate eVo deprecation table lists VX820 Duet "No more transactions" on 29 March 2024.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx680-user-manual-connect-the-vx680-to-your-wi-fi-network]] — 2019-modified, 2026-09-15-captured historical VX680 Wi-Fi menu guide for charging, Admin access and scan/manual SSID setup; its pictured key and WPA/TKIP-era choices are source-bound, while the related deprecation table lists VX680 ‘No more transactions’ on 29 March 2024.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx680-user-manual-board-the-terminal-vx680]] — 2019-modified, 2026-09-15-captured historical VX680 integrated and standalone boarding guide; network/security prechecks and POS App or Customer Area routes, bounded by the eVo table's 29 March 2024 ‘No more transactions’ date.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx675-user-manual-board-the-terminal-vx675]] — 2019-modified, 2026-09-15-captured historical VX675 POS App, Customer Area and classic-library boarding guide; its payment-ready wording is limited by the related deprecation table's VX675 "No more transactions" date of 29 March 2024.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-duet-user-manual-board-the-terminal-vx820-duet]] — 2019-modified, 2026-09-15-captured historical VX820 Duet integrated/standalone boarding guide for internet/security prechecks, POS App or Customer Area credentials and configuration update; parent deprecation table lists “No more transactions” on 29 March 2024, so old payment-ready wording is not current support or execution proof.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx690-user-manual-board-the-terminal-vx690]] — 2019-modified, 2026-09-15-captured historical VX690 boarding guide for prerequisite inspection/network checks and integrated or standalone routes; its readiness wording is superseded by the later 29 March 2024 VX690 transaction cutoff.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx690-user-manual]] — 2021-modified, 2026-09-15-captured historical VX690 manual hub for no-new-orders, no-4G limitation, setup routes and package contents; its old quickstart does not override the separate 29 March 2024 terminal transaction cutoff.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx680-user-manual]] — 2021-modified, 2026-09-15-captured historical VX680 manual overview: no new orders, unsynchronized-data exclamation, quickstart links and component list; the separate deprecation schedule lists no more VX680 transactions on 29 March 2024.


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx675-user-manual]] — 2021-modified, 2026-09-15-captured historical VX675 manual hub for charging, inspection, paper, Wi-Fi and boarding guides; no new orders, with the separate eVo table listing 29 March 2024 as “No more transactions.”


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-use-the-admin-menu-e355]] — 2019-modified, 2026-09-15-captured historical e355 Admin-menu guide: illustrated key plus 9, PIN gate, and listed configuration-removal and totals-reset purposes; no action outcome or current support proof.


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


- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-mx925-user-manual-board-the-terminal-mx925]] — 2019-modified, 2026-09-15-captured historical MX925 boarding guide for security/network prerequisites, merchant-account OTP and POS App paths; the deprecation table lists MX925 “No more transactions” on 29 March 2024.


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
