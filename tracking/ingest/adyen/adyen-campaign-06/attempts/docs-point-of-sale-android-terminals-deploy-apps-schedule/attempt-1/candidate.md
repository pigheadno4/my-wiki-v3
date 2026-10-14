---
title: "Adyen Docs: Schedule Android app deployment in Customer Area"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/android-terminals/deploy-apps/schedule"
raw_files:
  - "adyen/docs/point-of-sale/android-terminals/deploy-apps/schedule/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, app-deployment, customer-area]
---

## Overview

Adyen's 2026-09-15 snapshot explains how a Customer Area user schedules installation or removal of uploaded Android apps and certificates on selected Adyen-provided Android payment terminals. The terminal performs the action during an automatic maintenance call, subject to power and network connection. This is on-terminal deployment administration, not a Terminal API payment operation or proof that an app or certificate is currently installed. [[adyen]] · [[adyen-android-terminals]]

## Key takeaways

- The page applies to Android terminals in a Terminal API integration or standalone solution. Apps and certificates must first be uploaded to Customer Area; its role table names **Merchant POS Terminal Management Admin** for Customer Area upload. For an app action, verify **Ready** status before selecting the app. The raw does not extend that explicit Ready check to the separate certificate flow.
- In **Devices > Terminal apps > Apps**, select Install or Uninstall, the app version, and a schedule, then select target terminals and review the plan. `Schedule now` means the next maintenance call; a specified date/time means the first maintenance call after that time. Terminal selection can filter by ID or categories such as model and country/region. A plan across selected terminals is scheduling, not evidence every terminal completed the action.
- Certificate install/removal uses the **Certificates** tab, the chosen certificate and target terminals. Both app and certificate actions require the terminal to be turned on and connected to the network to succeed at maintenance. Removal is a consequential terminal change; check the intended app/version, certificate, and target list before scheduling.
- Opening **Settings > Apps** on a terminal requires a passcode and, according to this guide, immediately carries out an app action already scheduled for installation or removal. Checking the Apps menu can therefore trigger a pending change. This page gives no cancellation procedure or per-terminal completion receipt; use the linked deployment/status guidance before treating a scheduled plan as completed.

## Detail locators

- **Scope and prerequisite:** opening (lines 15–19) and raw heading “Requirements” (21–30) identify Android hardware, Terminal API/standalone integration scope, uploaded assets, and the Customer Area role statement.
- **App scheduling:** “Install or uninstall apps” (32–62) gives the Ready gate, Install/Uninstall and version selection, immediate/date scheduling semantics, terminal ID/model/region filtering, plan review, and maintenance-call requirement.
- **Certificate scheduling:** “Install or uninstall certificates” (64–81) gives separate tab/action/asset/terminal selection and the same powered/network-connected maintenance condition; it does not state an app-style Ready check.
- **On-device check and trigger:** “Check apps on a terminal” (83–91) gives the passcode route and immediate execution of an already scheduled app change when the Apps menu is opened.

## Related

- [[adyen-android-terminals]] — Android terminal app-deployment concept
- [[adyen-terminal-management]] — separate fleet administration and terminal actions
- [[adyen-terminal-api]] — separate POS payment messaging

## Related raw API references

The linked upload, app-requirements, profile-deployment, Management API terminal-actions, and maintenance-call guides were not read for this entry; use them as navigation only. This page itself does not specify cancellation or a per-terminal completion protocol.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/android-terminals/deploy-apps/schedule/2026-09-15|Adyen Customer Area Android app deployment scheduling, fetched 2026-09-15]]
