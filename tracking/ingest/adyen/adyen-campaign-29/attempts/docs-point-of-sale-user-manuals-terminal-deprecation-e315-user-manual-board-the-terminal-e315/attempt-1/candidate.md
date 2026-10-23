---
title: "Board the terminal - e315 | Adyen Docs"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/e315-user-manual/board-the-terminal-e315"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e315-user-manual/board-the-terminal-e315/2026-09-15.md"
tags: [adyen, point-of-sale, e315, terminal-boarding, historical]
---

## Overview

This 2019-last-modified e315 manual page, captured 2026-09-15 under Adyen's terminal-deprecation path, describes boarding an e315 attached to an iOS device in the Adyen App. It is historical model-specific procedure, not evidence of current e315 availability, current credential practice, a particular device's board state, payment execution, or security certification. See [[adyen]] and [[adyen-payment-terminals]].

## Key takeaways

- The page requires a working internet connection and a device security inspection **before** boarding, referring readers to the e315 quick-start guide for those prerequisites (raw lines 14–20).
- For this e315/iOS setup, the procedure says to install the iOS device in the e315, power both devices, log in to the iOS App with API credentials, open **Payment Device**, and select the reader shown as **PAYWare Mobile Reader** and **Not boarded**. The e315 reboots during boarding; after reboot, the user selects the reader shown as ready for use (raw lines 22–32). These steps describe the guide's UI flow, not a live account entitlement or independently verified outcome.
- If the reader is absent from the App or integration device count is zero, the guide attributes that symptom to the Made for iPhone (MFI) connection. It sequences an e315 restart, physical separation/reassembly of iOS device and e315, then cross-testing each device with another counterpart and replacement of the device causing the connection issue; it allows that both devices or their particular combination may be responsible (raw lines 34–46). Do not treat this historical diagnostic as proof that every missing-device case has the same cause.

## Detail locators

- Purpose and boarding prerequisites: raw lines 14–20.
- iOS App and PAYWare Mobile Reader boarding sequence: raw lines 22–32.
- Missing-reader/MFI troubleshooting sequence: raw lines 34–46.

## Related

- [[adyen-payment-terminals]]
- [[adyen-terminal-management]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e315-user-manual/board-the-terminal-e315/2026-09-15|Pinned historical e315 boarding guide]]
