---
title: "Adyen Android Terminals"
type: concept
category: technology
tags: [adyen, point-of-sale, android-terminals, terminal-apps]
---

## Definition

Adyen-provided Android payment terminals are in-person payment devices that can run Android apps. In the dated Android terminals overview, a payment may be initiated from a POS app on the terminal, a POS app on another device, or an eligible standalone terminal without a POS app. The overview applies to Terminal API and standalone integrations. App availability follows an app-requirements check, upload to Adyen, and distribution to terminals through a schedule, profiles or API requests. The linked guides own exact app, deployment and security conditions. [[source-adyen-docs-point-of-sale-android-terminals]]

## Evidence boundary

The 2026-09-15 overview's terminal-model and Android-version table is a snapshot. It warns that availability differs by region and points to the live Customer Area for regional checks. It does not establish current device or firmware support, app approval, certification, account eligibility, or successful deployment/payment execution. Adyen's merchant-phone Mobile SDK route and [[adyen-android-sdk]] native online-checkout SDK are separate from apps installed on these terminals.

## Sources

- [[source-adyen-docs-point-of-sale-user-manuals-s1u2-user-manual]] — S1U2 Android-terminal manual (2026-09-15 snapshot) for on-device software/menu, app-action and unattended kiosk context; physical setup and safety detail belongs in the source and [[adyen-payment-terminals]].


- [[source-adyen-docs-point-of-sale-user-manuals-sfo1-user-manual]] — SFO1 on-terminal operating manual (2026-09-15 capture): physical/network setup, store boarding, passcoded settings and assisted support; Android 13/model availability comes from the separate dated Android-terminal catalog, not this manual.


- [[source-adyen-docs-point-of-sale-user-manuals-p630-user-manual]] — P630 model manual (2026-09-15 capture) for its disabled menu icons and default kiosk mode; model-specific physical setup remains in the source.


- [[source-adyen-docs-point-of-sale-user-manuals-m450-user-manual]] — M450 on-device Apps/Settings/Transactions menu and passcode guidance (2026-09-15 snapshot); model hardware, diagnostics and safety detail resides in the source and payment-terminal hub.


- [[source-adyen-docs-point-of-sale-user-manuals-ams1-user-manual]] — AMS1 on-device menu, kiosk and airplane-mode operating guidance (2026-09-15 snapshot); physical hardware and safety detail resides in the source and payment-terminal hub.


- [[source-adyen-docs-point-of-sale-menu-access]] — 2026-09-15 Adyen menu/passcode guide for Android screen-lock warning, model/software-qualified Apps menu, and app control effects.


- [[source-adyen-docs-point-of-sale-android-terminals-accessibility-mode]] — 2026-09-15 Adyen Android-terminal accessibility overview for audio guidance and POS-app versus terminal activation routes, with enablement and detailed-guide limits.


- [[source-adyen-docs-point-of-sale-android-terminals-kiosk-mode]] — Adyen Customer Area kiosk-mode guide (2025-08-06 modified; 2026-09-15 capture) for dated model scope, role levels, default app and hidden screen controls.


- [[source-adyen-docs-point-of-sale-android-terminals-deploy-apps]] — Adyen Android-terminal deployment overview (2026-09-15 snapshot): requirements, app/optional-certificate upload and signing, API/profile/Customer Area availability routes, and maintenance-call installation.


- [[source-adyen-docs-point-of-sale-android-terminals-start-remote-session]] — Adyen Android-terminal Customer Area remote troubleshooting guide (2026-09-15 snapshot) for operator one-time-code participation, role/WebSocket/software gates, session end and reauthentication.


- [[source-adyen-docs-point-of-sale-android-terminals-scan-barcode-button-scan]] — Adyen 2026-09-15 snapshot of scan-button Customer Area enablement on four named Android scanner models, on-terminal app text input, and optional Support-enabled keyboard events.


- [[source-adyen-docs-point-of-sale-android-terminals-scan-barcode]] — Adyen barcode-scanning overview captured 2026-09-15 for four named Android scanner models, button versus single/batch Terminal API paths, and model-specific symbology matrix; detailed session and configuration rules remain in linked guides.


- [[source-adyen-docs-point-of-sale-android-terminals-deploy-apps-schedule]] — 2026-09-15 Customer Area guide to schedule Android app/version or certificate install/removal for selected terminals, with Ready, maintenance, power/network, and Apps-menu trigger boundaries.


- [[source-adyen-docs-point-of-sale-android-terminals-accessibility-mode-accessibility-from-pos]] — 2026-09-15 Adyen Android-terminal guide to Support-enabled, per-payment Terminal API accessibility mode requested by a POS app through Base64 `Operation` data; includes model/software and feature limits.


- [[source-adyen-docs-point-of-sale-android-terminals-scan-barcode-single-session]] — Adyen 2025-04-24 guide captured 2026-09-15 for one-scan Terminal API Admin sessions on named Android scanner terminals, response/cancel handling, and conflicting request examples.


- [[source-adyen-docs-point-of-sale-android-terminals-accessibility-mode-accessibility-from-terminal]] — 2026-09-15 Adyen terminal-side audio-accessibility guide for model/software gates, activation methods, PIN-screen and headphone limits, and payment/language exclusions.


- [[source-adyen-docs-point-of-sale-android-terminals-deploy-apps-profiles]] — Adyen Customer Area Android app-profile guide captured 2026-09-15 for matching conditions, Ready version selection, boarding/maintenance application, install/uninstall effects, and API/manual overwrite.


- [[source-adyen-docs-point-of-sale-android-terminals-themes]] — Adyen 2026-09-15 Customer Area guide to Android-terminal new-UI themes, role and 1.120+ conditions, media/screen limits, application levels and configuration timing.


- [[source-adyen-docs-point-of-sale-android-terminals-app-requirements]] — 2026-09-15 Adyen Android-terminal app requirements for APK/OS/ABI compatibility, permissions, restrictions, WebView and test guidance, subject to regional/model scope.


- [[source-adyen-docs-point-of-sale-android-terminals-scan-barcode-batch-session]] — Adyen batch-scanner Terminal API Admin and event-notification guide (2025-08-19 modified; 2026-09-15 capture) for four named Android scanner models.


- [[source-adyen-docs-point-of-sale-user-manuals-s1e4pro-user-manual]] — 2026-09-15 S1E4Pro Android-terminal device manual for first setup, Apps menu action, kiosk and Support-enabled airplane modes; current availability and app permissions require separate verification.


- [[source-adyen-docs-point-of-sale-android-terminals-deploy-apps-upload]] — Adyen Android-terminal APK and optional certificate upload guide captured 2026-09-15, covering Customer Area and Management API roles, signed files, processing states, device/size limits and automatic app deletion; upload precedes separate installation.


- [[source-adyen-docs-point-of-sale-user-manuals-s1e2l-user-manual]] — S1E2L device manual (2026-09-15 snapshot) for first boarding, network/SIM caveat, physical inspection, battery return hazard, menus and operating modes.


- [[source-adyen-docs-point-of-sale-user-manuals-s1f4pro-user-manual]] — S1F4Pro physical Android-terminal manual captured 2026-09-15 for inspection, boarding/store confirmation, networking, battery care, menus, and model-specific feature limits.


- [[source-adyen-docs-point-of-sale-user-manuals-s1e-user-manual]] — S1E/S1E Barcode user manual (2026-09-15 snapshot) for device inspection, first setup, connectivity, battery/cable care, menus and support routes.


- [[source-adyen-docs-point-of-sale-user-manuals-s1f2-user-manual]] — 2026-09-15 S1F2/S1F2L device manual for physical inspection, initial store confirmation, network and power care, menus, and passcode boundaries.


- [[source-adyen-docs-point-of-sale-android-terminals-deploy-apps-terminal-actions-api]] — Adyen Management API guide (2026-09-15 raw snapshot) for scheduling Android terminal app and certificate installation or removal, and checking planned-action status.


- [[source-adyen-docs-point-of-sale-android-terminals]] — Adyen website overview fetched 2026-09-15; Android terminal identity, integration scope, app-deployment routes, model table and regional warning.
