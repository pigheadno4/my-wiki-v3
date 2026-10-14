---
title: "Adyen Docs: Manage battery power"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/managing-terminals/battery-management"
raw_files:
  - "adyen/docs/point-of-sale/managing-terminals/battery-management/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, batteries, maintenance]
---

## Overview

Adyen's battery-management guide, captured 2026-09-15, covers power behavior for battery-powered payment terminals in Terminal API integrations or standalone use: software-qualified sleep defaults, charge monitoring, replacement, charger requirements, network/app effects, and storage conditions. Battery life varies with age, sleep, connection, Android app/brightness, and environment; the guide gives no precise runtime guarantee. This is device maintenance guidance, not certification of a battery, current device eligibility, or payment outcome. [[adyen]] · [[adyen-payment-terminals]]

## Key takeaways

- Sleep defaults depend on software and terminal family: Verifone Engage from version 1.65 and Android from 1.118; older listed versions lack default sleep. Requests, keys, maintenance calls, and network events can wake a terminal, and Management API settings or Support can change timeouts. Continuous network packets can prevent sleep; Wi-Fi quality, cellular traffic, Bluetooth links, and Android app design affect drain. The raw's Android `up to 40 hours` language is not a guaranteed runtime.
- Below 5% charge, Verifone Engage terminals in this snapshot stop processing transactions; the guide says Adyen cannot enforce that threshold on Android. The battery icon, optional Support-configured non-Android Low Battery warning, and `batteryLevel` in payment or diagnosis `AdditionalResponse` are monitoring routes. Adyen recommends a 20% warning level; Android has its own automatic warning. Example response values are illustrations, not a device's current charge.
- Use the charger supplied with the terminal. For models without a charger, this guide lists 5V DC, 1A for e285 and e280. Adyen recommends charging near 15%. For battery failure, it routes to terminal return or replacement; spare batteries are listed only for V400m, e285, and Android terminals. This page does not specify faulty-battery disposal or return-package handling; consult the relevant model and return instructions.
- For stored batteries and terminals, the snapshot lists −20°C to 60°C, 5% to 95% non-condensing humidity, and 40% to 70% charge with a check at least every six months. These are source guidance for storage, not universal electrical or shipping approval.

## Detail locators

- **Scope and uncertainty:** opening text (lines 17–36) and “Requirements” (38–49) identify battery-powered Terminal API/standalone terminals, variables affecting life, software-version exceptions, and optional Support warning.
- **Sleep behavior:** “Sleep mode” (51–72), including “Engage terminals” (62–66) and “Android terminals” (68–72), describes wakes, timeout settings, default-version gates, and Android behavior.
- **Monitoring:** “Monitor the battery charge level” (74–151) gives family-specific thresholds and warning behavior, screen icon, payment-response and diagnosis `batteryLevel` examples. The example `AdditionalResponse` strings are not a reading from the reader's own terminal.
- **Physical maintenance:** “Battery replacement” (153–159) and “Battery charging” (161–170) distinguish terminal return/replace, named spare-battery models, supplied charger, model-specific voltage/current, and charge recommendation.
- **Operating and storage effects:** “Events and network connection” (172–190), “Android app design” (192–194), and “Storage conditions” (196–202) cover wake events and link-specific behavior, app impact, and storage ranges.

## Related

- [[adyen-payment-terminals]] — physical device setup and maintenance
- [[adyen-terminal-management]] — separate fleet administration and replacement routing
- [[adyen-terminal-api]] — payment/diagnosis message boundary
- [[adyen-android-terminals]] — on-terminal Android app behavior

## Related raw API references

The linked model manuals, terminal return/replacement process, Management API settings, diagnosis request, and connectivity guides were not read for this entry; use them as navigation only. This guide alone does not supply faulty-battery packaging or disposal instructions.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/managing-terminals/battery-management/2026-09-15|Adyen Manage battery power, fetched 2026-09-15]]
