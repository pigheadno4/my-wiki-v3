---
title: "Braintree In-Person Verifone M400 Hardware"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/hardware/verifone-m400"
raw_files:
  - "braintree/in-person/hardware/verifone-m400-2026-09-16.md"
tags: [braintree, in-person, card-reader, verifone-m400, ethernet, wifi, hardware]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website page is a hardware overview for the Verifone M400 in the Braintree In-Person solution. It describes the fixed-lane reader, kit and accessories, captured payment-entry modes and network support, and the workflow for requesting a custom idle-screen image. It is not GitHub implementation evidence and does not establish current device availability, merchant/account eligibility, certification, reader pairing or online state, or a successful payment.

## Key takeaways

- The captured page describes the M400 as a fixed-lane terminal with Ethernet and WiFi connectivity, a 5-inch color LCD and a capacitive touchscreen. The kit is listed as the reader, power-and-Ethernet cable, power adaptor and stylus; these snapshot descriptions do not establish suitability, availability or approval for a particular deployment.
- For an M400 installed on a fixed stand, the accessories table marks the privacy shield as required for PCI compliance. The same table says the stylus pen and holder are included by default. This hardware page does not itself establish a complete PCI assessment, certification or deployment approval.
- The captured payment-entry-mode list is EMV chip, contactless, magstripe and QR-code scanning. The page separately states support for 2.4 and 5 GHz WiFi with WPA 1/2 PSK using CCMP (AES) or TKIP, and recommends 5 GHz when available while qualifying that behavior can vary with the merchant's network environment. These are source-snapshot hardware and network claims, not current payment-method enablement, network reachability, reader-online state or transaction proof.
- A custom reader idle-screen image can be configured at reader, location-ID or gateway-account level. The captured workflow asks for a conforming image plus reader serial numbers or location IDs to be sent to a PayPal Solutions Engineer or Integration Engineer; the page says readers refresh configuration within 12 hours or on the next reboot and directs post-go-live image changes to the support team. Exact file constraints and the captured support address remain at the locators below.

## Material warnings

> [!warning] Fixed-stand privacy condition
> The page marks the privacy shield as required for PCI compliance only when the M400 is installed on a fixed stand. This conditional accessory statement is not a complete PCI assessment, device certification or deployment approval.

> [!warning] Scope and proof boundary
> This is an unversioned Braintree website hardware snapshot for the M400, not GitHub implementation evidence and not documentation for the Verifone P400, E285 or another reader. Listed entry modes, accessories, connectivity and customization steps do not establish current availability, certification, account enablement, pairing, production readiness or payment success.

## Detail locators

- Device identity, fixed-lane positioning, Ethernet and WiFi connectivity and touchscreen: introduction and `## Overview`, lines 14-23.
- Terminal-kit contents and accessory table, including the fixed-stand privacy-shield condition and included stylus: `## Verifone M400 Terminal Kit Contents` and `## Available accessories for the M400`, lines 24-31.
- Display and power specifications plus the external Verifone product route and Braintree engagement/support-role note: `## Verifone M400 Hardware Specifications`, lines 34-44.
- Captured EMV chip, contactless, magstripe and QR-code-scanning entry-mode list and linked payment-method navigation: `## Supported Payment Entry Modes`, lines 47-50.
- 2.4 and 5 GHz bands, WPA 1/2 PSK with CCMP (AES) or TKIP, and the qualified 5 GHz recommendation: `## Supported WiFi Connectivity`, lines 53-58.
- Reader-, location-ID- and gateway-account-level idle-screen configuration scope: `## Customize your Reader Idle Screen`, lines 61-63.
- Custom image constraints (854 by 464 pixels at 72 dpi; JPG, GIF or PNG; 2 MB maximum; GIF-only animation) and format tips: `### M400 Custom Image File Specs` and `### Tips for creating your image files`, lines 66-92.
- Image submission identifiers, Solutions Engineer or Integration Engineer handoff, 12-hour-or-reboot refresh statement and post-go-live support route: `### Process to Upload Custom Images`, lines 97-114.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Related raw API references

- [[raw/braintree/in-person/hardware/verifone-p400-2026-09-16|Verifone P400]] - unread other-reader navigation linked by the hardware page; M400 claims must not be generalized to it
- [[raw/braintree/in-person/hardware/verifone-e285-2026-09-16|Verifone E285]] - unread other-reader navigation linked by the hardware page; M400 claims must not be generalized to it

## Raw Sources

- [[raw/braintree/in-person/hardware/verifone-m400-2026-09-16|Braintree In-Person Verifone M400]] - complete collected hardware overview for the M400 device, accessories, captured specifications, connectivity, entry modes and idle-screen customization
