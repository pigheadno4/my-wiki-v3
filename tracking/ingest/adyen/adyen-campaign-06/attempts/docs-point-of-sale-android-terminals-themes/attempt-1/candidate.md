---
title: "Customize your Android payment terminals with themes | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/android-terminals/themes"
raw_files:
  - "adyen/docs/point-of-sale/android-terminals/themes/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, terminal-themes, branding]
---

## Overview

Adyen's 2026-09-15 webpage snapshot describes Customer Area creation, application and management of visual themes for the new payment-flow UI on Android payment terminals. It covers Terminal API and standalone integrations. Route through [[adyen-android-terminals]] for the Android-device context; [[adyen-terminal-management]] is related for device-configuration timing. The page does not establish that a specific terminal has eligible software, a theme has downloaded, or a payment UI has rendered successfully.

## Key takeaways

- Creating themes requires the **Merchant POS Terminal Management Admin** Customer Area role. The guide limits customization to Android payment terminals on terminal software **1.120 or later** and the new UI introduced in that version. It does not establish current model availability or merchant eligibility.
- A theme can set light/dark appearance and model-specific media, with previews for each model and screen type. JPG, PNG and GIF images are listed for all terminals; MP4 and MOV video is limited to SFO1 and M450. The listed upload maximum is 100 MB, and the listed video resolution limit is 1280 × 800, or 574 × 634 for shopper-engagement screens.
- The documented surfaces are Home, Idle, After payment and Shopper engagement. Idle content is only for countertop terminals without battery power; shopper-engagement content is only for larger screens. After-payment content lengthens transaction time, but a new payment request bypasses it. This guide does not document altering cardholder/PIN entry or other security-sensitive payment screens.
- Creation occurs at company or merchant account level; applying a created theme is a separate Customer Area action at company, merchant, store or terminal level. The page does not state an inheritance or conflict-precedence rule between levels. Without a custom theme applied, Adyen's dark-mode theme remains the default.
- Applied changes take effect when the terminal downloads configuration during a maintenance call. With WebSockets enabled, the page says changes apply almost immediately; a manual terminal configuration update is another option. Theme creation or saving alone is not proof of applied device state. The page permits modifying or deleting themes, without describing the device-state result of deleting one that is in use.

## Detail locators

- [[raw/adyen/docs/point-of-sale/android-terminals/themes/2026-09-15#Requirements|Requirements]] — integration type, role, 1.120/new-UI hardware condition and media formats, model and size limits (lines 23–39).
- [[raw/adyen/docs/point-of-sale/android-terminals/themes/2026-09-15#How it works|How it works]] — company/merchant theme creation and separate multi-level application (lines 41–50).
- [[raw/adyen/docs/point-of-sale/android-terminals/themes/2026-09-15#Create a theme|Create a theme]] — appearance, model previews and Home/Idle/After payment/Shopper engagement screen conditions (lines 52–92).
- [[raw/adyen/docs/point-of-sale/android-terminals/themes/2026-09-15#Apply a theme|Apply a theme]] — level selection, default theme and maintenance/WebSocket/manual-update timing (lines 94–106).
- [[raw/adyen/docs/point-of-sale/android-terminals/themes/2026-09-15#Manage themes|Manage themes]] — modification and deletion controls (lines 108–115).

## Related

- [[adyen]] — provider context and dated website-source catalog.
- [[adyen-android-terminals]] — primary Android terminal and app context.
- [[adyen-terminal-management]] — related terminal configuration and maintenance route.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/android-terminals/themes/2026-09-15|Android terminal themes (fetched 2026-09-15)]]