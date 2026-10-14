---
title: "Adyen Mobile Card Readers"
type: concept
category: technology
tags: [adyen, point-of-sale, mobile-payments, card-readers]
---

## Definition

Adyen's NYC1 is a card reader paired with an Android or iOS mobile device running a POS app. The app starts and shows the transaction while the shopper uses the reader for tap, chip, swipe or wallet presentation. Bluetooth is the general device link. The NYC1 manual limits a **direct USB-C cable from mobile device to reader** to Android devices supporting USB host mode; the separate iOS Mobile SDK path connects the mobile device by USB-C **through an NYC1 dock with the reader seated**. A docked reader can also charge while the mobile device still connects over Bluetooth without a USB-C device-to-dock connection. See [[source-adyen-docs-point-of-sale-user-manuals-nyc1]] and [[source-adyen-docs-point-of-sale-mobile-ios-understand]]. This reader path is distinct from direct standalone-terminal initiation, apps installed on Adyen Android payment terminals, and native online-checkout SDK flows.

## Operating boundary

The dated NYC1 manual covers physical inspection, POS-app pairing, payment operation, PIN model differences, power, updates and device troubleshooting. A failed tamper check or tamper indicator calls for stopping use and contacting Adyen Support. US NYC1-SCR devices are marked unsuitable for PIN; current country, OS, merchant-account and SDK conditions require their own sources. The manual does not establish authorization, settlement or repair/return procedures.

## Related

- [[adyen-terminal-management]] — fleet ordering, assignment and configuration
- [[adyen-android-terminals]] — apps on Adyen Android payment terminals
- [[adyen-standalone-terminals]] — transactions initiated directly on a standalone terminal

## Sources

- [[source-adyen-docs-point-of-sale-mobile-ios-understand]] — iOS NYC1 reader/dock operations guide (2026-09-15 snapshot) for US PIN model/SDK distinction, Bluetooth versus USB dock connection, and reader/dock firmware UI obligations.


- [[source-adyen-docs-point-of-sale-mobile-android-checklists]] — 2026-09-15 Android Mobile checklist route for test NYC1, live reader forecast/firmware alerts and optional dock adapter, version, connection-UI and update requirements.


- [[source-adyen-docs-point-of-sale-mobile-ios-troubleshooting]] — iOS Mobile SDK error guide (2026-09-15 snapshot) with NYC1 connection, pairing, firmware and dock error routes; shared device-security and transaction cases remain at [[adyen-mobile-pos]].


- [[source-adyen-docs-point-of-sale-mobile-android-understand]] — Android Mobile solution comparison (2026-09-15 webpage snapshot) for NYC1 reader PIN model/SDK qualification, built-in versus custom reader/dock UI, and firmware operations; the broader solution map belongs to [[adyen-mobile-pos]].


- [[source-adyen-docs-point-of-sale-mobile-ios-build-card-reader]] — iOS POS Mobile SDK card-reader integration guide (2026-09-15 snapshot): NYC1 pairing/dock, device firmware, Terminal API transaction and session setup; the broader mobile POS flow belongs under [[adyen-mobile-pos]].


- [[source-adyen-docs-point-of-sale-user-manuals-nyc1-with-dock]] — Adyen NYC1 reader and dock user guide captured 2026-09-15 for Android/iOS mobile POS app connection, charging, pairing, PIN and update limits, and tamper checks; this mobile reader is separate from an Android payment terminal.


- [[source-adyen-docs-point-of-sale-user-manuals-nyc1]] — NYC1 mobile card-reader manual (2026-09-15 snapshot) for inspection, mobile POS pairing/USB, PIN model scope, charging, updates and tamper escalation.
