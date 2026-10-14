---
title: "Menus and passcodes | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/menu-access"
raw_files:
  - "adyen/docs/point-of-sale/menu-access/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, passcodes, terminal-management]
---

## Overview

Adyen's Menus and passcodes guide (last modified 2024-04-19; captured 2026-09-15) explains protected Settings/Admin and Transactions controls, Customer Area and Management API passcode management, and Android versus non-Android terminal menus for Terminal API or standalone integrations. Its stated hardware scope is Android terminals and Verifone Engage non-Android terminals. This historical guide is operating documentation, not proof of current device features, account permissions, passcode state, security posture, or payment execution. See [[adyen]], [[adyen-payment-terminals]], and [[adyen-terminal-management]].

## Key takeaways

- Four passcode purposes are distinguished: Admin & Settings for protected configuration and app/network/power controls; Transactions for history/totals and standalone special transactions; Refunds for standalone refunds; and Android-only Screen lock after inactivity. A passcode boundary is not a claim that the underlying transaction or device feature is enabled.
- Passcodes can be viewed or updated at company, merchant, store, or terminal level in Customer Area or by Management API `/terminalSettings` GET/PATCH. Lower-level values replace inherited values. Customer Area changes require **Merchant POS Terminal Management Admin**; API passcode management requires **Management API—Terminal Advanced settings read and write** because passcodes are sensitive settings. The raw PATCH property table names `adminMenuPin`, `txMenuPin`, `refundPin`, and `screenLockPin`; consult the current API schema before sending a request.
- Adyen says unattended Android terminals must have screen lock disabled. A higher-level setting can propagate to them; the guide specifically calls for checking individual unattended terminals. Company-level screen-lock enablement is described as requiring a passcode on all Android terminals, attended or unattended.
- New passcodes download at maintenance calls described as automatic every 180 minutes and take effect at terminal restart, usually the configured 6:00 AM restart hour in this snapshot. The documented immediate switch uses the **old** passcode at **Settings > Configuration > Update**; saving or PATCHing alone is not evidence that a terminal is already using the new code.
- Airplane mode requires Adyen Support enablement. The protected **Settings > Network** toggle turns off Wi-Fi, Bluetooth, and cellular connections and restores prior connections when turned off. On the eligible Android Apps menu, **Force quit** stops an app, **Clear cache** deletes temporary files, and **Clear storage** deletes all app data and resets the app's settings. Opening the Android Settings Apps listing can also carry out a scheduled app installation or removal.
- The Requirements table limits the Apps menu to **S1U2 and S1E2L on software 1.103+**, while the same snapshot's general Android menu table lists Apps and the separate S1E4Pro manual also lists it. Treat the narrow gate and broader menu descriptions as a source conflict; verify model, software, and actual device state before relying on Apps actions. The guide describes shared Android/non-Android menu structure from software 1.90; earlier non-Android menus differ, and versions 1.85–1.90 have a Customer Area route to enable newer controls.

## Detail locators

- Requirements, model/software gate, roles, and four passcode purposes: [[raw/adyen/docs/point-of-sale/menu-access/2026-09-15#Requirements|Requirements]] and [[raw/adyen/docs/point-of-sale/menu-access/2026-09-15#Passcodes|Passcodes]].
- Customer Area scope, inheritance, unattended screen-lock warning, maintenance/restart delay, and immediate update: [[raw/adyen/docs/point-of-sale/menu-access/2026-09-15#View and update passcodes|View and update passcodes]] (raw lines 51–109).
- API GET/PATCH endpoint variants, passcode properties, and illustrative TEST examples: raw lines 105–635. The examples do not prove live API version or account entitlement.
- Support enablement and network effects: [[raw/adyen/docs/point-of-sale/menu-access/2026-09-15#Use Airplane mode|Use Airplane mode]] (raw lines 638–662).
- App action effects and Android menu passcode boundaries: [[raw/adyen/docs/point-of-sale/menu-access/2026-09-15#Use the Android App menu|Use the Android App menu]] and [[raw/adyen/docs/point-of-sale/menu-access/2026-09-15#Android terminal menus|Android terminal menus]] (raw lines 664–711).
- Version-qualified non-Android menus, legacy Admin/standalone payment paths, and newer-menu toggle: [[raw/adyen/docs/point-of-sale/menu-access/2026-09-15#Non-Android terminal menus|Non-Android terminal menus]] and [[raw/adyen/docs/point-of-sale/menu-access/2026-09-15#Old non-Android terminal menus|Old non-Android terminal menus]] (raw lines 713–818). The standalone special menu can include refunds, MOTO, manual key entry, bypass controls, and cashback; the separate Refunds passcode can be requested for refund or MOTO refund.

## Related

- [[adyen-payment-terminals]] — physical terminal operations and model manuals.
- [[adyen-android-terminals]] — Android terminal features and app deployment context.
- [[adyen-terminal-management]] — fleet settings and propagation context.
- [[adyen-standalone-terminals]] — scope of standalone transaction controls.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/menu-access/2026-09-15|Adyen Menus and passcodes, captured 2026-09-15]]
