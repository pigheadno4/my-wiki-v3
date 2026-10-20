---
title: "Adyen Issuing: Manage card data"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/manage-card-data"
raw_files:
  - "adyen/docs/issuing/manage-card-data/2026-09-15.md"
tags: [adyen, issuing, card-data, pan, pin, encryption]
---

## Overview

This Adyen Issuing hub, modified and captured 2026-09-15, routes a platform to guides for letting its cardholders reveal issued-card details such as PAN or expiration date, reveal a PIN, or change a PIN. It concerns cardholder access to sensitive card data, not card creation or payment authorisation. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- The page says these processes transfer sensitive card data between the platform's servers and Adyen, and **all transferred data must be encrypted**, using methods such as AES and ISO format 4. It offers either an implementation of the encryption/decryption algorithms or the Adyen SDK for card management; the linked child guides own the operation-specific payloads and security steps.
- At this snapshot the card-management SDK is described as available **only for iOS apps**. The page says an Android SDK “will be released soon,” which is a dated forecast, not evidence of current Android availability. The child links label the iOS path “Adyen Card Reveal iOS” and separately offer standard-encryption paths.
- This page is a navigation hub. It does not specify SDK release versions, API credentials or roles, ciphertext format per operation, PCI scope, PIN-change completion, or whether a particular card transaction authenticated or succeeded. Follow the relevant child procedure and current product requirements before applying it.

## Detail locators

- Pinned raw lines 15–24: cardholder use case and reveal/change options.
- Pinned raw lines 26–30: mandatory encrypted transport, AES/ISO-4 examples, SDK option and iOS-only snapshot.
- Pinned raw lines 32–57: child routes for card details, PIN reveal and PIN change, each with iOS SDK and standard-encryption variants.

## Related

- [[adyen-issuing]] — card-program and payment-instrument context.

## Related raw API references

- [[raw/adyen/docs/issuing/manage-card-data/reveal-card-details-ios-sdk/2026-09-15|Card details with iOS SDK]]; [[raw/adyen/docs/issuing/manage-card-data/reveal-card-details/2026-09-15|card details with standard encryption]] — navigation only.
- [[raw/adyen/docs/issuing/manage-card-data/reveal-pin-ios-sdk/2026-09-15|PIN reveal with iOS SDK]]; [[raw/adyen/docs/issuing/manage-card-data/reveal-pin/2026-09-15|PIN reveal with standard encryption]] — navigation only.
- [[raw/adyen/docs/issuing/manage-card-data/change-pin-ios-sdk/2026-09-15|PIN change with iOS SDK]]; [[raw/adyen/docs/issuing/manage-card-data/change-pin/2026-09-15|PIN change with standard encryption]] — navigation only.

## Raw Sources

- [[raw/adyen/docs/issuing/manage-card-data/2026-09-15|Adyen Issuing manage-card-data hub, captured 2026-09-15]]
