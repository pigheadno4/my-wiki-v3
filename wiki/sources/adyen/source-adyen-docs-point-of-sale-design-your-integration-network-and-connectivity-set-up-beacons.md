---
title: "Adyen Bluetooth terminal beacons for POS routing"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/network-and-connectivity/set-up-beacons"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/set-up-beacons/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, bluetooth, ibeacon, terminal-routing]
---

## Overview

This Adyen Docs page describes Bluetooth/iBeacon advertisements from supported payment terminals that a mobile POS app can use to find a nearby terminal and route Terminal API requests. It covers Customer Area beacon values, cloud routing by serial number and `POIID`, and local routing by advertised IP address plus `POIID`. See [[adyen]] and [[adyen-terminal-api]]. The word “connect” in the page summary refers here to discovery and request routing; the body does not establish a Bluetooth payment transport, SDK pairing protocol, transaction success, or payment outcome.

## Key takeaways

- The stated scope is a Terminal API integration with payment terminals. The page explicitly excludes Android terminals and unattended non-Android terminals from beacon functionality. It does not give supported terminal model lists, mobile POS operating-system or SDK versions, regional availability, Bluetooth permission procedures, or security guarantees; those should not be inferred from its iBeacon examples.
- Supported terminals advertise an iBeacon UUID, Major and Minor. In Customer Area, the operator can choose the merchant account, store, or terminal scope, enable beacons under **Devices > Device settings > Device connectivity**, set those three values, and save. UUID is 32 hexadecimal digits; Major and Minor are each decimal values from 0 through 65535.
- Adyen's placeholders can encode the terminal serial number in Major/Minor for cloud communication or its IP address for local communication. The table gives serial placeholders `${SERIALH}`/`${SERIALL}` and interface-specific IP placeholders (for example `${IPH:ETH0}`/`${IPL:ETH0}`); the mobile POS app must decode the advertised values and select the relevant terminal details. These identifiers support routing, not authorization to use the terminal.
- In cloud mode, the POS derives the serial number from Major/Minor, looks up the full terminal `POIID` in a `/connectedTerminals` response for the applicable company, merchant, or store, then sends its Terminal API request with that `POIID`. The serial number alone is not presented as the full `POIID`; the page's `POIID` example combines model and serial number.
- In local mode, the POS derives the terminal IP address from Major/Minor and also needs the correct `POIID`. The page advises maintaining an IP-to-`POIID` mapping and describes a diagnosis-request method to populate it, then sending the Terminal API request to that IP using the matched `POIID`. Beacon discovery does not replace local network reachability or the Terminal API communication and security requirements documented elsewhere.

## Detail locators

- Purpose, iBeacon use and stated terminal exclusions: `# Bluetooth beacons` and `## Requirements`, raw lines 15–28.
- UUID/Major/Minor and architecture split: `## Advertised values and integration types`, raw lines 31–44. Customer Area setup and configuration scope: lines 46–62.
- Serial and interface-specific IP placeholders: `### Placeholders for the Major and Minor`, raw lines 64–84.
- Cloud serial decoding, `/connectedTerminals` lookup and `POIID` routing: `## Use beacons with cloud communications`, raw lines 86–122.
- Local IP and `POIID` mapping, diagnosis suggestion and IP decoding: `## Use beacons with local communications`, raw lines 124–177. Numeric values and terminal IDs are examples, not a support matrix.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — in-person Terminal API concept and separate versioned GitHub evidence.

## Related raw API references

- The raw page links to terminal integration, cloud/local architecture, `/connectedTerminals` diagnostics, diagnosis requests, and Apple's iBeacon documentation. Those linked targets are navigation until independently read; see raw lines 19, 27, 88–100, 126–138, and 179–182.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/set-up-beacons/2026-09-15|Adyen Docs: Bluetooth beacons (2026-09-15 snapshot)]]
