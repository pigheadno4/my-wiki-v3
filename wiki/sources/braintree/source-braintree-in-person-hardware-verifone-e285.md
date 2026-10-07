---
title: "Braintree In-Person Verifone E285 Hardware"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/hardware/verifone-e285"
raw_files:
  - "braintree/in-person/hardware/verifone-e285-2026-09-16.md"
tags: [braintree, in-person, card-reader, verifone-e285, wifi, hardware]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website page is a hardware overview for the Verifone E285 in the Braintree In-Person solution. It describes the wireless mobile reader, captured specifications, payment-entry modes and WiFi support, and the workflow for requesting a custom idle-screen image. It is not GitHub implementation evidence and does not establish current procurement or device availability, merchant/account eligibility, certification, reader pairing or online state, or a successful payment.

## Key takeaways

- The captured page describes the E285 as a wireless mobile payment terminal with WiFi connectivity and a touchscreen, positioned for line-busting or checkout around a store. That positioning does not establish suitability, availability or approval for a particular deployment.
- The terminal-kit section lists an E285 reader and a USB-A-to-USB-C cable. The hardware table describes a 2.8-inch color capacitive touchscreen and an 1800 mAh rechargeable, field-replaceable battery with USB-C charging; these snapshot specifications do not establish current procurement, certification or device condition.
- The captured payment-entry-mode list is EMV chip, contactless, magstripe and QR-code scanning. The page separately states 2.4 GHz WiFi support with WPA 1/2 PSK using CCMP (AES) or TKIP. These are hardware-page claims, not current payment-method enablement, network reachability, reader-online state or transaction proof.
- A custom reader idle-screen image can be configured at reader, location-ID or gateway-account level. The captured workflow asks for a conforming image plus reader serial numbers or location IDs to be sent to a PayPal Solutions Engineer or Integration Engineer; the page says readers refresh configuration within a 12-hour interval or on the next reboot. Exact file constraints and the post-go-live support route remain at the locators below.

## Material warnings

> [!warning] Scope and proof boundary
> This is an unversioned Braintree website hardware snapshot for the Verifone E285, not GitHub implementation evidence and not documentation for another reader model. Listed specifications, entry modes, connectivity and customization steps do not establish current procurement or device availability, certification, account enablement, pairing, reader-online state, production readiness or payment success.

## Detail locators

- Device identity, wireless/mobile positioning, WiFi connectivity and touchscreen: introduction and `## Overview`, lines 14-23.
- Terminal-kit contents: `## E285 Terminal Kit Contents`, lines 24-26.
- Integrated-mPOS description, 2.8-inch 320 by 240 color capacitive touchscreen, 1800 mAh rechargeable field-replaceable battery, USB-C charging and external Verifone product route: `## E285 Hardware Specifications`, lines 27-35.
- Captured EMV chip, contactless, magstripe and QR-code-scanning entry-mode list and linked payment-method navigation: `## Supported Payment Entry Modes`, lines 37-40.
- 2.4 GHz band and WPA 1/2 PSK with CCMP (AES) or TKIP: `## Supported WiFi Connectivity`, lines 43-45.
- Reader-, location-ID- and gateway-account-level idle-screen configuration scope: `## Customize your Reader Idle Screen`, lines 48-50.
- Custom image constraints (240 by 304 pixels at 72 dpi; JPG, GIF or PNG; 2 MB maximum; GIF-only animation) and format tips: `### E285 Custom Image File Specs` and `### Tips for creating your image files`, lines 53-79.
- Image submission identifiers, Solutions Engineer or Integration Engineer handoff, 12-hour-or-reboot refresh statement and post-go-live support route: `### Process to Upload Custom Images`, lines 84-101.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Related raw API references

- [[raw/braintree/in-person/about/solution-coverage-2026-09-16|Solution Coverage]] - unread payment-method navigation linked by the hardware page; it supplies no behavioral evidence in this entry
- [[raw/braintree/in-person/hardware/verifone-m400-2026-09-16|Verifone M400]] - unread other-reader navigation linked by the hardware page; E285 claims must not be generalized to it
- [[raw/braintree/in-person/hardware/verifone-v400m-2026-09-16|Verifone V400m]] - unread other-reader navigation linked by the hardware page; E285 claims must not be generalized to it

## Raw Sources

- [[raw/braintree/in-person/hardware/verifone-e285-2026-09-16|Braintree In-Person Verifone E285]] - complete collected hardware overview for the E285 device, captured specifications, connectivity, entry modes and idle-screen customization
