---
title: "Adyen NYC1 mobile card reader user guide"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/nyc1"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/nyc1/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-card-reader, nyc1, user-manual]
---

## Overview

Adyen's NYC1 guide covers a separate mobile card reader used with an Android or iOS POS app: the app starts the transaction and displays transaction screens; the customer taps, inserts or swipes a card, or uses a wallet, at the reader. The reader connects to the mobile device over Bluetooth, or by USB-C only for Android devices supporting USB host mode. This is a device operation guide, not a standalone-terminal flow, an Android app installed on an Adyen terminal, an online-checkout Android SDK guide, or proof of payment outcome. The raw webpage was fetched 2026-09-15. [[adyen]] · [[adyen-mobile-card-readers]]

## Key takeaways

- **Security before use:** Inspect the unopened box and tamper-evident tape, verify box/reader serial numbers and, if Customer Area is available, compare the order serial and delivery tracking. Check the reader for physical tampering. Contact Adyen Support immediately if a check fails; a tampered-reader indicator means stop use and contact Support.
- **Connection and pairing:** Pair Bluetooth from the POS app on the mobile device and confirm by pressing the reader's power button twice, then accepting the pairing prompt. Android selects the reader by serial from a list; iOS can select nearby by serial or scan its barcode. A mobile device connects to only one reader at a time, though it can retain multiple pairings. Do not use the mobile OS settings to create the pairing; those settings are used to forget an existing pairing. USB-C operation requires Android USB host mode and the POS app's USB permission.
- **Payment and network:** Start the payment in the mobile POS app, present the reader, then send a receipt or print it on an external printer when completed. The guide's troubleshooting says the mobile device needs Wi-Fi or cellular network access if the reader does not take payments. A Bluetooth reader disconnects after five minutes idle while remaining paired and can reconnect/wake when a payment starts; USB-connected use is described as always ready. These device states are not evidence that any particular payment authorized or settled.
- **PIN is model and region qualified:** In the US, not every NYC1 reader supports PIN. In the app's device details, `NYC1` without a model denotes a PIN-capable reader; `NYC1-SCR` denotes one unsuitable for PIN. When supported and required, the PIN pad appears on the mobile device in a random screen position. Do not infer PIN capability for every NYC1 or every country.
- **Power and updates:** The setup asks for at least 1.5 hours' charge while continuing setup. The guide specifies Adyen's supplied USB-C cable with a 5V DC, 1A charger (charger not supplied); the battery is not replaceable. Mandatory reader/Bluetooth updates can take minutes, need the POS app open and the mobile device unavailable for other use, and reboot/reconnect the reader afterward. Bluetooth updates require an active Bluetooth connection. The table's durations are estimates, not service-level guarantees.

## Detail locators

- **Reader identity, components and start sequence:** raw lines 15–45, including initial charge and dock navigation.
- **Inspection and Support escalation:** raw lines 47–62; tamper LED and stop-use warning at 287–291 and 322–324.
- **Bluetooth/USB setup and pairing distinctions:** raw lines 64–126; troubleshooting's POS-app pairing versus OS settings at 297–308.
- **Payment, idle behavior and receipts:** raw lines 128–145; mobile-network troubleshooting at 310–316.
- **PIN, US model labels and device UI:** raw lines 147–174.
- **Battery, cable and mandatory update constraints:** raw lines 176–258; LED patterns at 260–291.
- **Related solution routes:** raw lines 326–331 link Mobile in-person payments, Android/iOS card-reader build guides and NYC1 dock instructions; those pages are navigation from this manual. This raw does not define a return/repair procedure, all-country availability, mobile OS minimums, SDK version, or current account enablement.

## Related

- [[adyen-mobile-card-readers]] — mobile POS app and NYC1 device boundary
- [[adyen-terminal-management]] — separate fleet administration through Customer Area or Management API
- [[adyen-android-terminals]] — separate Android payment terminals and terminal-app deployment

## Related raw API references

The linked Mobile in-person, Android/iOS card-reader build and NYC1 dock guides were not read for this entry. Use their raw pages for integration, device compatibility and dock-specific claims.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/nyc1/2026-09-15|NYC1 card reader user guide, fetched 2026-09-15]]
