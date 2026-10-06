---
title: "Braintree In-Person Verifone P400 Hardware"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/hardware/verifone-p400"
raw_files:
  - "braintree/in-person/hardware/verifone-p400-2026-09-16.md"
tags: [braintree, in-person, card-reader, verifone-p400, wifi, ethernet, hardware]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website page is a hardware overview for the Verifone P400 in the Braintree In-Person solution. It describes the fixed-lane device, kit and accessory conditions, captured entry modes and network support, and the workflow for requesting a custom idle-screen image. It is not GitHub implementation evidence and does not document reader setup or pairing; it is not evidence of current device availability, merchant/account eligibility, reader-online state, or a successful payment.

## Key takeaways

- The captured page describes the P400 as a fixed-lane payment terminal tethered to a power source, with WiFi or Ethernet connectivity and a touchscreen. The P400 Plus kit is listed as the reader, power cable and multi-port cable; this description does not establish suitability, availability or approval for a particular deployment.
- The accessories table marks the privacy shield as required for PCI compliance when the P400 is installed on a fixed stand. The hardware page does not itself establish a complete PCI assessment or deployment approval.
- The captured payment-entry-mode list is EMV chip, contactless, magstripe and QR-code scanning. These are source-snapshot hardware claims, not current payment-method enablement, certification, account configuration, network reachability or transaction proof.
- The page states support for 2.4 and 5 GHz WiFi using WPA 1/2 PSK with CCMP (AES) or TKIP. It recommends 5 GHz when available but qualifies that recommendation by the merchant-specific network environment. The page does not provide Ethernet configuration or reader-pairing steps.
- A custom reader idle-screen image can be configured at reader, location-ID or gateway-account level. The captured workflow asks for a conforming image and reader serial numbers or location IDs to be sent to a PayPal Solutions Engineer or Integration Engineer; the page says readers refresh configuration within 12 hours or on the next reboot. Exact file constraints and post-go-live support routing remain at the locators below.

## Material warnings

> [!warning] Network and setup boundary
> The page lists supported WiFi bands and security algorithms and identifies Ethernet as a connectivity option, but it does not document Ethernet configuration, network reachability, device setup or reader pairing. Consult the separate [[source-braintree-in-person-guides-setup-reader|Dev Kit P400 setup guide]] for its Sandbox-scoped setup and pairing route; neither document by itself proves reader-online state or production enablement.

> [!warning] Scope and proof boundary
> This is an unversioned Braintree website hardware snapshot for the Verifone P400, not GitHub implementation evidence and not documentation for another reader model. Listed entry modes, accessories, connectivity and customization steps do not establish current availability, certification, account eligibility, production readiness or payment success.

## Detail locators

- Device identity, fixed-lane positioning, tethered-power condition, WiFi or Ethernet connectivity and touchscreen: introduction and `## Overview`, lines 14-23.
- P400 Plus terminal-kit contents and accessory table, including the fixed-stand privacy-shield condition: `## Verifone P400 Plus Terminal Kit Contents` and `## Available accessories for the Verifone P400 Plus`, lines 24-31.
- Display and power specifications plus the external Verifone product route: `## Verifone P400 Plus Hardware Specifications`, lines 34-46.
- Captured EMV chip, contactless, magstripe and QR-code-scanning entry-mode list and linked payment-method navigation: `## Supported Payment Entry Modes`, lines 51-54.
- 2.4 and 5 GHz bands, WPA 1/2 PSK with CCMP (AES) or TKIP, and the merchant-environment-qualified 5 GHz recommendation: `## Supported WiFi Connectivity`, lines 57-62.
- Reader-, location-ID- and gateway-account-level idle-screen configuration scope: `## Customize your Reader Idle Screen`, lines 65-67.
- Custom image constraints (320 by 464 pixels at 72 dpi; JPG, GIF or PNG; 2 MB maximum; GIF-only animation) and format tips: `### P400 Custom Image File Specs` and `### Tips for creating your image files`, lines 70-96.
- Image submission identifiers, Solutions Engineer or Integration Engineer handoff, 12-hour-or-reboot refresh statement and post-go-live support route: `### Process to Upload Custom Images`, lines 101-118.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]
- Setup and pairing route: [[source-braintree-in-person-guides-setup-reader]] - separate Dev Kit P400 and Sandbox-scoped setup guide

## Related raw API references

- [[raw/braintree/in-person/about/solution-coverage-2026-09-16|Solution Coverage]] - unread payment-method navigation linked by the hardware page; it supplies no behavioral evidence in this entry
- [[raw/braintree/in-person/hardware/verifone-m400-2026-09-16|Verifone M400]] - unread other-reader navigation linked by the hardware page; P400 claims must not be generalized to it

## Raw Sources

- [[raw/braintree/in-person/hardware/verifone-p400-2026-09-16|Braintree In-Person Verifone P400]] - complete collected hardware overview for the P400 device, kit and accessory conditions, captured specifications, connectivity, entry modes and idle-screen customization
