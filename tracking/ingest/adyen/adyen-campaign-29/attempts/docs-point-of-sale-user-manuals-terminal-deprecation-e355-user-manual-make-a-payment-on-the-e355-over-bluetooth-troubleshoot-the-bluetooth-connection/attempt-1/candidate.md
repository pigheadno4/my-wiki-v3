---
title: "Adyen e355 Bluetooth connection troubleshooting"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth/troubleshoot-the-bluetooth-connection"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth/troubleshoot-the-bluetooth-connection/2026-09-15.md"
tags: [adyen, point-of-sale, e355, bluetooth, troubleshooting, terminal-deprecation]
---

## Overview

This 2026-09-15-captured [[adyen]] e355 manual page gives short Bluetooth troubleshooting branches for an app stuck at “initializing,” a missing Bluetooth icon and other pairing issues. It is filed under terminal deprecation in [[adyen-payment-terminals]], so its e355-specific guidance is historical rather than a present-day support or security certification claim (raw lines 14–28).

## Key takeaways

- **Initializing state:** The guide says the most likely cause is that the app and terminal do not support the same protocol version and directs checking that compatibility (raw lines 16–18). It does not name a version matrix or prescribe a firmware update.
- **Missing icon sequence:** Check app/terminal proximity first. It describes a theoretical 60 m open-space maximum, around 30 m in an office, and advises being within 10 m for troubleshooting. If both devices are paired and no icon appears within 20 seconds, restart the app first; if that fails, restart the terminal (raw lines 20–24). These distances are the manual's estimates, not a guaranteed connection radius.
- **Other issues and pairing state:** The guide recommends a clean Bluetooth configuration and links a separate unpair procedure for removing **other paired devices unless necessary** (raw lines 26–28). Do not read this as a blanket instruction to remove necessary pairings or as a factory reset. The detailed unpair operation belongs to the linked step-1 guide, not this short page.

## Detail locators

- Initializing/protocol compatibility: raw lines 16–18.
- Distance, 20-second threshold, app-first then terminal restart: raw lines 20–24.
- Conditional removal of other unnecessary paired devices via separate guide: raw lines 26–28.

## Evidence boundary

This historical page provides troubleshooting order and hypotheses, not proof of a diagnosed cause, restored Bluetooth link, successful boarding, live terminal availability or payment authorization. Restarting the app or terminal is a separate action from unpairing devices; the latter can change connection state and is only referenced here with a qualifier.

## Related

- [[adyen-payment-terminals]] — physical-terminal route.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-make-a-payment-on-the-e355-over-bluetooth-step-2-pair-the-e355-with-a-mobile-device]] — separate e355 pairing and boarding step.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth/troubleshoot-the-bluetooth-connection/2026-09-15|Pinned e355 Bluetooth troubleshooting page, captured 2026-09-15]]
