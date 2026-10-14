---
title: "Adyen iOS Mobile solutions concepts and reader operations"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-ios/understand"
raw_files:
  - "adyen/docs/point-of-sale/mobile-ios/understand/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, ios, mobile-sdk, tap-to-pay, card-reader]
---

## Overview

Adyen's iOS Mobile solutions concept guide explains how a merchant iOS POS app, the Adyen Mobile SDK, a merchant backend and the Adyen payments platform participate in an in-person Terminal API transaction. It then covers on-device PIN presentation and, for the separate NYC1 card-reader path, Bluetooth or USB dock connection and firmware UI. It is not an iOS online-checkout SDK guide or a claim that a particular iPhone, reader, account or region is currently eligible. [[adyen]] [[adyen-mobile-pos]] [[adyen-mobile-card-readers]]

## Key takeaways

- The iOS Mobile SDK needs a secure communication session. The POS app calls its own backend, which makes a server-to-server POST `/auth/certificate` request and returns session data; the SDK uses that data to authenticate with Adyen and checks whether an expired session must be renewed. The page gives the concept, while linked build guides own credential, parameter and environment details. See `## Communication session`.
- In the shared SDK transaction flow, the POS app optionally warms up the SDK, creates a JSON-serialized Terminal API request or receives one from its backend, passes it to the SDK, and receives a Terminal API response. The SDK checks/renews the session and starts the transaction on the mobile device. The linked TerminalAPIKit for iOS is a request-building aid, not a separate transaction processor. See `## SDK transaction flow`.
- The page says PIN transactions are possible in both Tap to Pay and card-reader solutions. For on-mobile-device PIN entry, the PIN pad can appear in a random screen position as a security measure; do not assume a centered PIN UI. For a **card reader in the US**, secure PIN requires an NYC1 with PIN support and Mobile SDK **3.8.0+**. The guide distinguishes `connectedDevice.type=nyc1` (PIN support) from `nyc1SCR` (no PIN support), with an alternative built-in Device Info Model-field check. It states NYC1-SCR would no longer be orderable after **2026-02-01**; that is a dated guide claim, not current ordering proof. See `## PIN transactions` and `### PIN transaction with a card reader in the US`.
- In the NYC1 reader path, operators need UI to pair the mobile device over Bluetooth, see and switch readers, inspect reader details/battery and update reader firmware. Adyen provides built-in UI, or the app can build custom UI. Reader firmware must be checked regularly and updated; a firmware update may fail without an active Bluetooth connection when required. A custom UI must implement the update check and flow. These reader tasks do not apply merely because the Tap to Pay phone interface is used. See `## UI for card reader operations`.
- With an NYC1 dock, the mobile device can connect by USB-C to the dock while the reader sits in it, and dock firmware also needs updating. A reader may instead sit in the dock for charging while the mobile device still connects by Bluetooth and has **no USB-C device-to-dock connection**. Built-in and custom UI options exist; custom UI must implement dock firmware-update checks/flow. See `## UI for dock operations`.

## Detail locators

- `## Communication session` and `## SDK transaction flow`: backend session role, expiry check, optional warm-up, Terminal API request/response sequence and TerminalAPIKit navigation.
- `## PIN transactions`–`### PIN transaction with a card reader in the US`: random mobile PIN-pad placement, US NYC1/NYC1-SCR distinction, SDK 3.8.0 floor and dated ordering statement.
- `## UI for card reader operations`: Bluetooth pairing, device list/info, firmware indicator, update failure condition and custom-UI obligation.
- `## UI for dock operations`: USB-C/dock connection versus Bluetooth while docked, dock firmware and custom-UI obligation.

## Related

- [[adyen-mobile-pos]] — merchant iOS/Android Mobile POS routes.
- [[adyen-mobile-card-readers]] — NYC1 external-reader hardware and operation.
- [[adyen-terminal-api]] — in-person request/response message model.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-ios/understand/2026-09-15|Adyen iOS Mobile concepts guide, fetched 2026-09-15]]
