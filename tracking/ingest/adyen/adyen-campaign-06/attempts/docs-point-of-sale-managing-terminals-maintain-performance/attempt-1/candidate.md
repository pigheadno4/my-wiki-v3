---
title: "Maintain performance | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/managing-terminals/maintain-performance"
raw_files:
  - "adyen/docs/point-of-sale/managing-terminals/maintain-performance/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-management, maintenance, software-updates]
---

## Overview

Adyen's 2026-09-15 webpage snapshot describes scheduled maintenance calls, daily terminal reboots, configuration application and software installation for Terminal API or standalone payment terminals. [[adyen-terminal-management]] is the main operational route; [[adyen-payment-terminals]] is related for model-specific hardware guidance. A scheduled call or update instruction does not prove that a particular terminal received a change, rebooted, installed software, or stayed available.

## Key takeaways

- Maintenance calls normally check Adyen's platform for configuration and available software changes rather than installing them. The guide says the default interval is three hours, and a busy terminal postpones the call and retries. Calls do not run during payments or other operations.
- The terminal normally reboots once per 24 hours at its restart hour, defaulting to 6:00 AM in the terminal's timezone, to clear its cache. Configuration changes learned during a call and, when automatic updating is enabled, software updates generally apply at that reboot. The page estimates a reboot at about two minutes and software installation at up to 30 minutes; neither is an availability guarantee.
- Exceptions to restart-hour application include urgent Adyen-initiated changes that trigger an application restart after a maintenance call, immediate Android app install/uninstall, and a manual terminal configuration update. The manual **Config > Update** action fetches configuration and restarts the terminal. A separate `terminalInstructions.adyenAppRestart` Management API setting enables an Adyen-application restart on configuration update without restarting other terminal apps; this is an optional configuration, not the default path.
- Changing the restart hour in Customer Area requires an **admin** user and can be scoped to merchant account, store or terminal after login. Plan it around opening hours and operational events. The examples for `/terminalSettings` are test-environment, library-version-specific illustrations; use the linked current API contract for exact request behavior.
- The guide requires the terminal to be on and network-connected for at least one three-hour maintenance interval before restart hour, and on at restart hour. Network access is also needed when downloading software at reboot. It recommends keeping terminals on and connected overnight; those conditions support the maintenance flow but do not attest to completion or current installed version.

## Detail locators

- [[raw/adyen/docs/point-of-sale/managing-terminals/maintain-performance/2026-09-15#Requirements|Requirements]] — Terminal API/standalone scope and maintenance-window preparation (lines 28–35).
- [[raw/adyen/docs/point-of-sale/managing-terminals/maintain-performance/2026-09-15#Maintenance calls|Maintenance calls]] — discovery, timing, busy-terminal retry and payment-operation exclusion (lines 37–47).
- [[raw/adyen/docs/point-of-sale/managing-terminals/maintain-performance/2026-09-15#Rebooting at the restart hour|Rebooting at the restart hour]] — cache, duration, update installation and default local restart time (lines 49–55).
- [[raw/adyen/docs/point-of-sale/managing-terminals/maintain-performance/2026-09-15#Set the restart hour|Set the restart hour]] — admin role, Customer Area scope and setting path (lines 57–72).
- [[raw/adyen/docs/point-of-sale/managing-terminals/maintain-performance/2026-09-15#Configuration changes|Configuration changes]] — normal timing and three exceptions (lines 74–84).
- [[raw/adyen/docs/point-of-sale/managing-terminals/maintain-performance/2026-09-15#Update the configuration manually|Update the configuration manually]] — Admin menu and terminal restart (lines 86–93).
- [[raw/adyen/docs/point-of-sale/managing-terminals/maintain-performance/2026-09-15#Automatic configuration update|Automatic configuration update]] — optional `adyenAppRestart` terminal setting and versioned Management API examples (lines 95–325).
- [[raw/adyen/docs/point-of-sale/managing-terminals/maintain-performance/2026-09-15#Software updates|Software updates]] and [[raw/adyen/docs/point-of-sale/managing-terminals/maintain-performance/2026-09-15#What you need to do|What you need to do]] — default automatic release behavior, background-download qualification, power/network prerequisites (lines 327–346).

## Related

- [[adyen]] — provider context and dated website-source catalog.
- [[adyen-terminal-management]] — fleet operation and configuration route.
- [[adyen-payment-terminals]] — model-specific physical terminal guidance.
- [[adyen-terminal-api]] — in-person POS messaging; one integration type within this guide's scope.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/managing-terminals/maintain-performance/2026-09-15|Maintain performance (fetched 2026-09-15)]]