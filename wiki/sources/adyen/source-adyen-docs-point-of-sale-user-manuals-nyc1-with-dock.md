---
title: "Adyen NYC1 card reader with dock user guide"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/nyc1-with-dock"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/nyc1-with-dock/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, nyc1, card-reader, dock]
---

## Overview

Adyen's NYC1 with dock user guide covers a separate NYC1 card reader used with an Android or iOS POS app on a mobile device. The shopper taps, inserts or swipes a card, or uses a digital wallet, at the reader; transaction screens appear on the mobile device. The reader and mobile device communicate through USB via the NYC1 dock or directly through Bluetooth. The dock charges the reader and can establish the USB connection. This is a mobile-device-and-reader setup, distinct from an Android payment terminal running apps on the terminal and from the GitHub native Android online-checkout SDK. [[adyen]] [[adyen-mobile-card-readers]]

## Key takeaways

- Before use, inspect both reader and dock for correct delivery and tampering. Check intact security tape, match the box and reader serial numbers, and, if Customer Area access is available, compare the order serial and delivery record. Contact Adyen Support immediately if a check fails. A tamper indication on the reader also requires stopping use and contacting Support.
- Start by charging the reader in the dock for at least 1.5 hours using the supplied region-specific 12V/1.5A PD adapter. The dock must use that adapter. Away from the dock, the reader has a non-replaceable rechargeable battery; use the Adyen-supplied USB-C charging cable and a 5V DC, 1A charger, which is not included, for charging.
- With USB through the dock, connect the dock's power port to the adapter and its data port to the mobile device; the dock charges both reader and mobile device. With Bluetooth, the reader charges in the dock but the mobile device does not. Pair through the POS app, identify the reader by its serial number, and confirm on the reader by pressing the power button twice. The POS app examples differ for Android and iOS; iOS also offers barcode selection. A mobile device can have several paired readers but connect to only one at a time. Use the mobile device's Bluetooth settings to forget an existing pair, not to initiate pairing.
- Start the transaction in the mobile POS app, then present the reader. The mobile device needs Wi-Fi or cellular network connectivity for payments. In Bluetooth mode the devices disconnect after five minutes of inactivity but remain paired and reconnect on a new payment; the reader can take longer to wake. The separate troubleshooting section says the reader times out after ten minutes of inactivity. These statements describe different connection and reader states.
- PIN entry, when supported, appears on the mobile device in a randomized screen position. In the US, not all NYC1 readers support PIN: device details show name NYC1 without a model for a PIN-capable reader, whereas NYC1-SCR identifies a reader without PIN support. Do not infer PIN support merely from the NYC1 name.
- Mandatory software updates can cover the reader, Bluetooth functionality and dock. Keep the POS app open and the mobile device available until completion; Bluetooth updates are available only over an active Bluetooth connection. The guide's update-time table is estimated, not a guaranteed duration. If a Bluetooth-dependent update fails for lack of an active connection, follow the displayed reset instructions before retrying.

## Detail locators

- Reader, dock, supplied parts and mobile-app role: pinned raw lines 15–43.
- First charge and physical inspection, including serial/delivery/tamper checks: pinned raw lines 53–79.
- USB and Bluetooth connection instructions, pairing identity and limits: pinned raw lines 81–169.
- Payment flow, sleep/reconnect behavior, PIN and US NYC1-SCR distinction: pinned raw lines 171–217.
- Dock versus reader-only power, charger and battery care: pinned raw lines 219–257.
- Update availability, mode and estimates, app-open requirement and failure recovery: pinned raw lines 259–311.
- LED meanings, pairing/network/battery troubleshooting and tamper stop-use action: pinned raw lines 313–377.

## Related

- [[adyen-mobile-card-readers]] — mobile reader hardware and POS app relationship.
- [[adyen-terminal-api]] — broader Adyen in-person solution route; this guide specifically uses a mobile POS app with an NYC1 reader.
- [[adyen-android-terminals]] — separate Adyen Android payment terminals that run apps on the terminal itself.
- [[adyen-android-sdk]] — separate native online-checkout SDK baseline.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/nyc1-with-dock/2026-09-15|NYC1 card reader with NYC1 dock user guide, fetched 2026-09-15]]
