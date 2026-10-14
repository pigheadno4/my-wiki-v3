---
title: "Adyen Android Mobile POS security guidance"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-android/security"
raw_files:
  - "adyen/docs/point-of-sale/mobile-android/security/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, android, security, pci-mpoc]
---

## Overview

This 2026-09-15 Adyen webpage snapshot describes built-in protections, merchant integration practices, Wi-Fi restrictions and PCI MPoC responsibilities for Android Mobile payment solutions. It distinguishes the Android Mobile SDK's Tap to Pay and card-reader integrations from the separate Adyen Payments app. See [[adyen]], [[adyen-mobile-pos]] and [[adyen-api-access]]. The page states Adyen product protections and certification claims; it does not certify a particular merchant app, device fleet, network or implementation.

## Key takeaways

- Adyen says the Mobile SDK does not retain card or wallet payment details locally, exchanges encrypted payment messages, and uses code obfuscation plus OS/device/app/SDK monitoring and attestation. For the separate card-reader payment interface, it calls the reader a PCI PTS-approved Secure Card Reader that encrypts payment details immediately. These are product claims in the captured page, not proof that a specific integration is secure.
- The page's **must** practices are to keep Adyen API keys secret on the server, never call Adyen APIs directly from the mobile POS app, and set a device passcode. It additionally **recommends** mutual authentication such as mTLS for POS-app/server communication so Terminal API requests cannot be modified in transit; POS-app user authentication; current SDK and OS/security patches; trusted SDK distribution and integrity checks where possible; and using the TEST SDK for internal development/testing only. It warns that transaction requests from older SDK versions stop being accepted after a short grace period, without specifying a fixed duration.
- For Wi-Fi, the page recommends WPA3, WPA2/WPA3 or WPA2 with a strong password. It says the Mobile SDK displays a security warning and **cancels the transaction** on deprecated/insecure network settings, including WPA/WPA2 mixed mode, WPA Personal, WEP, TKIP, and open or unsecured networks. This is a transaction behavior stated for the Mobile SDK, not a general claim about all Android payment paths.
- Adyen claims PCI MPoC certification for its Tap to Pay on Android SDK and Android Payments app, and certified vendor status. The page says the fully certified **Payments app** carries no additional PCI compliance obligations for the user. By contrast, a company integrating the **Android SDK** for Tap to Pay or Card reader must complete a PCI vendor verification assessment; Adyen submits it to PCI SSC to validate the combined integration with Adyen's MPoC-certified SDK. Contact Adyen for the assessment process. This source does not establish that any merchant's combined solution has passed that assessment.
- The integrating company remains responsible for the assessment even if it sells the solution to merchants and does not physically possess devices. The page recommends a shared-responsibility approach and merchant device inventory. It advises wildcard app-version notation because a single version in the assessment limits the published certification to that version.

## Detail locators

- `## Security of the solution`: encrypted messages, no local retention claim, monitoring/attestation and PCI PTS reader claim.
- `## Security best practices`, `## Device passcode`: server-held keys, no direct app-to-Adyen API calls, device passcode, recommended mTLS/app login and SDK/OS maintenance. The passcode appears under **must** in the first section and as **strongly recommend** in the later section; preserve that wording distinction.
- `## Wi-Fi security best practices`, `### Insecure Wi-Fi settings`: permitted settings and SDK warning/cancellation examples.
- `## PCI MPoC compliance requirements`, `### Assessment guidelines`: distinct Payments-app certification claim and Android-SDK integrator assessment duties, merchant responsibility and version guidance.

## Related

- [[adyen-mobile-pos]] — Android Mobile solution routes and implementation guides.
- [[adyen-mobile-card-readers]] — physical reader context for the card-reader route.
- [[adyen-api-access]] — API credentials and security context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-android/security/2026-09-15|Adyen Security of the Android Mobile solutions, captured 2026-09-15]]
