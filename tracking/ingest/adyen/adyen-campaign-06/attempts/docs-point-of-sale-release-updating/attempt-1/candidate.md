---
title: "Update to a new release | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/release-updating"
raw_files:
  - "adyen/docs/point-of-sale/release-updating/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, terminal-software, software-updates]
---

## Overview

This 2026-09-15 Adyen Docs snapshot explains software-release strategies for Adyen payment terminals used with a Terminal API integration or a standalone solution: default automatic rollout, approved manual Long Term Support (LTS) updating, and beta testing. It describes terminal software and fleet maintenance, not a version of Adyen's POS SDKs or a report of any merchant's current terminal state. See [[adyen]] and [[adyen-terminal-api]] for provider and integration context.

## Key takeaways

- Adyen says its standard strategy is a gradual, monitored automatic rollout of new terminal software each month after testing. It describes new software availability about every four weeks, with seasonal schedule adjustments in November and December. The page says automatic updating applies across Terminal API integration types and standalone terminals, regardless of terminal model or fleet size.
- The manual strategy requires Adyen approval and permits updates only to LTS terminal software. The page instructs merchants to request a manual LTS update in Customer Area at least two business days ahead; unlike the automatic strategy, Adyen says it does not actively monitor manually updated terminals. Contact Support to learn or change the strategy. A request and schedule are not proof that a device updated.
- After an update request, installation occurs after the terminal reboots at its configurable restart hour (default 6:00 AM local time). Success requires the terminal to be on and network-connected for at least one maintenance interval before then (default 180 minutes). If installation fails, the terminal continues on the previous version. These are device and network conditions, not POS application deployment steps.
- An LTS release receives critical fixes for an extended period. The page says Adyen typically maintains one for about four to five months; terminals may update to any of the three latest LTS releases, but new issues are fixed only in the latest LTS version. Its listed versions and planned dates are dated, explicitly changeable plans; use current release notes to assess present support.
- Beta terminals receive the latest software near the beginning of automatic rollout. Adyen handles setup and monitoring, but the merchant is expected to keep beta terminals active, brief staff, and report issues. Enrollment is through an Adyen contact. The page describes Adyen's attempt to select stores with two other active terminals and its ability to pause or revert an update if issues occur; neither is a guarantee against disruption.

## Detail locators

- `Update to a new release`, lines 19–29: Support route, release cadence, strategy approval, restart-hour and connectivity conditions.
- `Requirements`, lines 31–39: Terminal API or standalone scope, manual LTS restriction, beta enrollment.
- `Release testing`, lines 41–48: robot, lab, Test environment and live beta stages.
- `Automatic updating`, lines 50–65: applicability, gradual rollout, business-hour scheduling, seasonal variation, monitoring and pause/revert route.
- `Manual updating`, lines 67–77: advance Customer Area request, monitoring distinction and installation conditions.
- `Long Term Support version`, lines 79–93: maintenance policy, latest-three choice, latest-only new fixes and changeable planned release table.
- `Beta testing`, lines 95–131: rollout position, mitigation, merchant expectations and Adyen-contact enrollment.

## Related

- [[adyen]] — provider page.
- [[adyen-terminal-api]] — POS integration context; terminal software rollout also covers standalone terminals.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/release-updating/2026-09-15|Terminal software release and update strategy (2026-09-15 snapshot)]]
