---
title: "Adyen Docs: Android terminal kiosk mode"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/android-terminals/kiosk-mode"
raw_files:
  - "adyen/docs/point-of-sale/android-terminals/kiosk-mode/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, kiosk-mode, customer-area]
---

## Overview

Adyen's kiosk-mode guide, last modified 2025-08-06 and captured 2026-09-15, explains Customer Area configuration for Android payment terminals in unattended settings. Kiosk mode hides the navigation bar and the Settings and Transactions buttons so customers cannot use those screen controls to change or minimize the default app or power off the terminal. It describes a user-interface configuration for Terminal API or standalone solutions; it does not establish physical tamper resistance, a universal device lockdown, payment success, or present model eligibility. See [[adyen-android-terminals]] and [[adyen]].

## Key takeaways

- The snapshot names **AMS1, S1E2L, S1E, S1E4Pro, S1F2, S1F4Pro, and S1U2** as Android models on which kiosk mode can be enabled. It separately says kiosk mode is enabled by default on **P630**. The guide gives no software-version minimum, current-region list, or account-specific enablement status.
- Customer Area configuration requires **Merchant POS Terminal Management Admin** for settings at any level, or **Merchant POS Terminal Management** for merchant-account level and lower. The displayed path is **Devices > Device settings > Device**.
- The documented setup selects an uploaded Android app as **Default start app**, turns on **Hide navigation bar**, optionally chooses **Apps allowed in kiosk mode**, turns off **Settings menu** and **Transactions menu** under Home screen, then saves. The guide does not claim that this uploads an app, deploys it, or validates its payments.
- The page gives no exit sequence or passcode/PIN rule for leaving kiosk mode. Hiding Settings and Transactions buttons is not evidence that every other device or admin control is blocked. Consult the current device and menu-access guides before relying on kiosk mode for unattended security or recovery operations.

## Detail locators

- Purpose, integration types, Customer Area roles and model list: [[raw/adyen/docs/point-of-sale/android-terminals/kiosk-mode/2026-09-15#Kiosk mode|Kiosk mode]] and [[raw/adyen/docs/point-of-sale/android-terminals/kiosk-mode/2026-09-15#Requirements|Requirements]].
- Default app, allowed apps, hidden controls and save sequence: [[raw/adyen/docs/point-of-sale/android-terminals/kiosk-mode/2026-09-15#Enable kiosk mode|Enable kiosk mode]].

## Related

- [[adyen-android-terminals]] — Android-terminal model and app deployment route.
- [[adyen-terminal-api]] — integrated payment messaging, separate from this Customer Area UI setting.
- [[adyen-standalone-terminals]] — standalone solution option named in the requirements.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/android-terminals/kiosk-mode/2026-09-15|Adyen kiosk-mode guide, 2026-09-15 snapshot]]
