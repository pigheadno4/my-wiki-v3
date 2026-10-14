---
title: "Adyen Mobile Card Readers"
type: concept
category: technology
tags: [adyen, point-of-sale, mobile-payments, card-readers]
---

## Definition

Adyen's NYC1 is a card reader paired with an Android or iOS mobile device running a POS app. The app starts and shows the transaction while the shopper uses the reader for tap, chip, swipe or wallet presentation. Bluetooth is the general device link; USB-C requires an Android device supporting USB host mode. This reader path is distinct from direct standalone-terminal initiation, apps installed on Adyen Android payment terminals, and native online-checkout SDK flows.

## Operating boundary

The dated NYC1 manual covers physical inspection, POS-app pairing, payment operation, PIN model differences, power, updates and device troubleshooting. A failed tamper check or tamper indicator calls for stopping use and contacting Adyen Support. US NYC1-SCR devices are marked unsuitable for PIN; current country, OS, merchant-account and SDK conditions require their own sources. The manual does not establish authorization, settlement or repair/return procedures.

## Related

- [[adyen-terminal-management]] — fleet ordering, assignment and configuration
- [[adyen-android-terminals]] — apps on Adyen Android payment terminals
- [[adyen-standalone-terminals]] — transactions initiated directly on a standalone terminal

## Sources

- [[source-adyen-docs-point-of-sale-user-manuals-nyc1-with-dock]] — Adyen NYC1 reader and dock user guide captured 2026-09-15 for Android/iOS mobile POS app connection, charging, pairing, PIN and update limits, and tamper checks; this mobile reader is separate from an Android payment terminal.


- [[source-adyen-docs-point-of-sale-user-manuals-nyc1]] — NYC1 mobile card-reader manual (2026-09-15 snapshot) for inspection, mobile POS pairing/USB, PIN model scope, charging, updates and tamper escalation.
