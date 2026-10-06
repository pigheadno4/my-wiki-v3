---
title: "Braintree In-Person Verifone V400m Hardware"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/hardware/verifone-v400m"
raw_files:
  - "braintree/in-person/hardware/verifone-v400m-2026-09-16.md"
tags: [braintree, in-person, card-reader, verifone-v400m, wifi, hardware]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website page is a hardware overview for the Verifone V400m in the Braintree In-Person solution. It describes the mobile reader, kit and optional bases, captured payment-entry modes and network support, and the workflow for requesting a custom idle-screen image. It is not evidence of current device availability, merchant/account eligibility, certification, reader pairing or online state, or a successful payment.

## Key takeaways

- The captured page describes the V400m as a wireless mobile payment terminal with WiFi connectivity and a touchscreen, suitable for mobile use or a fixed lane. The kit is listed as the reader, power adaptor and one roll of printing paper; positioning examples do not establish suitability, availability or approval for a particular deployment.
- The listed optional accessories include charging-only and charging-plus-Ethernet bases. Ethernet connectivity is described only while the reader is connected to the full-feature base, and the page warns that the charging-plus-Ethernet base does not automatically switch the reader between Ethernet and WiFi when it is connected or disconnected.
- The captured payment-entry-mode list is EMV chip, contactless, magstripe and QR-code scanning. The page separately states 2.4 GHz WiFi support with WPA 1/2 PSK using CCMP (AES) or TKIP. These are source-snapshot hardware claims, not current payment-method enablement, certification, account configuration, network reachability or transaction proof.
- For a V400m installed on a fixed stand, the accessories table marks the privacy shield as required for PCI compliance. The hardware page does not itself establish a complete PCI assessment or deployment approval.
- A custom reader idle-screen image can be configured at reader, location-ID or gateway-account level. The captured workflow asks for a conforming image plus reader serial numbers or location IDs to be sent to a PayPal Solutions Engineer or Integration Engineer; the page says readers refresh configuration within 12 hours or on the next reboot. Exact file constraints and post-go-live support routing remain at the locators below.

## Material warnings

> [!warning] Network-interface behavior
> The V400m charging-plus-Ethernet base does not automatically switch the reader between Ethernet and WiFi when docked or undocked. A deployment must account for the intended interface; the captured description does not prove present network connectivity or reader-online state.

> [!warning] Scope and proof boundary
> This is an unversioned Braintree website hardware snapshot for the V400m, not GitHub implementation evidence and not documentation for the Verifone E285, P400 or another reader. Listed entry modes, accessories, purchase language and customization steps do not establish current availability, certification, account enablement, pairing, production readiness or payment success.

## Detail locators

- Device identity, wireless/mobile positioning, WiFi connectivity and touchscreen: introduction and `## Overview`, lines 14-23.
- Terminal-kit contents and accessory table, including the fixed-stand privacy-shield condition: `## Verifone V400m Terminal Kit Contents` and `## Verifone V400m Accessories`, lines 24-34.
- Display, battery/power and printer specifications plus the external Verifone product route: `## V400m Hardware Specifications`, lines 37-47.
- Charging-only and full-feature base descriptions, Ethernet-while-docked scope, no-automatic-switch warning and captured purchase statement: `## Available Charging Bases for the Verifone V400m`, lines 50-66.
- Captured EMV chip, contactless, magstripe and QR-code-scanning entry-mode list and linked payment-method navigation: `## Supported Payment Entry Modes`, lines 69-72.
- 2.4 GHz band and WPA 1/2 PSK with CCMP (AES) or TKIP: `## Supported WiFi Connectivity`, lines 75-77.
- Reader-, location-ID- and gateway-account-level idle-screen configuration scope: `## Customize your Reader Idle Screen`, lines 80-82.
- Custom image constraints (320 by 464 pixels at 72 dpi; JPG, GIF or PNG; 2 MB maximum; GIF-only animation) and format tips: `### V400m Custom Image File Specs` and `### Tips for creating your image files`, lines 85-111.
- Image submission identifiers, Solutions Engineer or Integration Engineer handoff, 12-hour-or-reboot refresh statement and post-go-live support route: `### Process to Upload Custom Images`, lines 116-133.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Related raw API references

- [[raw/braintree/in-person/get-started-1/integration-checklist-2026-09-16|Integration Checklist]] - unread setup/integration navigation linked by the hardware page; it supplies no evidence in this entry
- [[raw/braintree/in-person/hardware/verifone-e285-2026-09-16|Verifone E285]] - unread other-reader navigation linked by the hardware page; V400m claims must not be generalized to it

## Raw Sources

- [[raw/braintree/in-person/hardware/verifone-v400m-2026-09-16|Braintree In-Person Verifone V400m]] - complete collected hardware overview for the V400m device, accessories, captured specifications, connectivity, entry modes and idle-screen customization
