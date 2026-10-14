---
title: "Deploy apps to your terminals | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/android-terminals/deploy-apps"
raw_files:
  - "adyen/docs/point-of-sale/android-terminals/deploy-apps/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, app-deployment]
---

## Overview

This Adyen Docs overview, captured 2026-09-15, maps how a merchant-created Android app reaches an Adyen Android payment terminal: meet app requirements, upload through Customer Area for Adyen signing/conversion, optionally upload a required certificate, choose an availability route, then wait for the terminal's automatic maintenance call to install it. It is a process map, not evidence that any app was approved, installed, usable on a particular model, or able to run a payment. See [[adyen]] and [[adyen-android-terminals]].

## Key takeaways

- Android payment terminals can run merchant apps such as a POS app or inventory app in addition to accepting payments. The overview says to create the app and check the separate Android app requirements before upload. It does not itself specify APK/OS compatibility, permissions, third-party app ownership, account roles, release-version rules, or an approval decision; those questions belong to the linked detailed guides.
- Upload the app in Customer Area. Adyen says it signs the app, converts it to a terminal-compatible format and saves it. If the app requires a certificate, upload that separately; Adyen signs and saves the certificate. Signing and storage are distinct from making either item available or proving installation. The page does not state that every app needs a certificate.
- Once signed and ready, make the app and any applicable certificate available through **API requests** for automated install/uninstall, **Customer Area profiles** for installation under defined conditions, or **Customer Area scheduling** for planned install/uninstall. The three routes are alternatives or combinations; this overview does not specify their exact credential roles, targeting, version selection, override effects, approval states or failure handling.
- The overview says installation and on-terminal availability occur when the terminal makes an automatic maintenance call to Adyen. An upload, signed status, profile, API request or scheduled action alone does not establish that the maintenance call completed or the app is installed on a particular device.

## Detail locators

- `Deploy apps to your terminals`, lines 15–19: Android terminal app purpose and example app types.
- `How it works`, lines 21–40: requirements gate, upload/sign/convert sequence, conditional certificate, three availability routes and maintenance-call installation.
- `Next steps`, lines 42–70: links to detailed upload, Management API action, profile and Customer Area scheduling guides; these are navigation, not additional behavioral evidence.

## Related

- [[adyen-android-terminals]] — Android payment-terminal concept and detailed source routes.
- [[adyen-terminal-management]] — Management API fleet administration, separate from app runtime.
- [[adyen-payment-terminals]] — physical terminal setup and operating context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/android-terminals/deploy-apps/2026-09-15|Android terminal app-deployment overview (2026-09-15 snapshot)]]
