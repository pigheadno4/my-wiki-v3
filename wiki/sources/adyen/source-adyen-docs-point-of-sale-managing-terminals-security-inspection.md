---
title: "Adyen Docs: Payment terminal security inspection"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/managing-terminals/security-inspection"
raw_files:
  - "adyen/docs/point-of-sale/managing-terminals/security-inspection/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, hardware-security, inspection]
---

## Overview

Adyen's security-inspection guide, captured 2026-09-15 and marked last modified 2020-05-27, tells in-person operators how to inspect delivered and deployed payment hardware for tampering, watch for suspicious activity, and report a missing terminal. It names Adyen payment terminals or card readers in its hardware scope; its detailed checks refer mainly to terminals. The page is procedural guidance, not a certification of any particular device's safety or PCI compliance. [[adyen]] · [[adyen-payment-terminals]]

## Key takeaways

- Before using a delivered terminal, verify that the box is unopened and its tamper tape intact. If Customer Area order access is available, compare its serial number to the box and check carrier delivery via track-and-trace; compare the device serial number to the box and inspect for missing screws, extra wires or labels, holes, attachments, or insertions. If any delivery check fails, contact Adyen Support immediately. When unsure about a terminal's integrity, stop using it and contact Support.
- Continue inspections after deployment. Adyen recommends checking every week; that frequency is a recommendation, while the guide says checks should be regular. A display showing **TAMPER**, **TAMPERED**, or a localized equivalent triggers immediate stop-use and Support contact.
- Recurring visual and integrity checks include comparing the unit to its model manual, confirming an Adyen or company logo appears after startup, checking the card reader, ports, display, and keypad for cameras, skimmers, or other attachments, and looking for physical damage or added labels/wires. Review camera footage for suspicious activity and ensure neither staff nor camera footage can see customers' PIN entry.
- Verify the identity of people claiming to repair or maintain terminals before granting access. Report suspicious behavior to Adyen through a manager or security officer, or contact Support directly when in doubt.
- For a lost or stolen terminal, contact Support with its model and serial number, location, circumstances, discovery, prior active-use or packaged state, and preventive actions. The guide asks about a police report when theft is suspected; if filed, attach it, otherwise file one and send it as soon as possible. Copy terminals@adyen.com in the support form's indicated field. These reporting steps do not establish recovery or compromise status.

## Detail locators

- **Scope and delivery:** raw `Requirements` (lines 23–30) limits hardware scope; `Delivery inspection` (32–47) gives packaging, Customer Area order, carrier, serial, and physical-tamper checks. The Customer Area comparison is conditional on access.
- **Ongoing inspection:** `Regular inspection` (49–65), including `Visual inspection` and `Device integrity inspection`, gives recommended weekly cadence, tamper-message stop-use rule, card-reader/port/keypad checks, camera footage, and PIN-visibility check.
- **People and loss:** `Awareness of suspicious activity` (67–71) covers third-party identity checks and reporting. `Lost or stolen terminal` (73–97) gives the questions to answer, conditional police-report step, and support-form copy address. Its serial-number-by-exclusion option is for when direct serial identification is necessary.
- The raw has Customer Area and Support links; this dated snapshot does not verify current contact routes, an individual device's integrity, a PCI assessment, or successful reporting.

## Related

- [[adyen-payment-terminals]] — physical model and operating guidance
- [[adyen-terminal-management]] — fleet administration and device lifecycle
- [[adyen-android-terminals]] — Android terminal apps, a separate topic

## Related raw API references

Linked model manuals, ordering, and troubleshooting pages were not read for this entry; use them as navigation only.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/managing-terminals/security-inspection/2026-09-15|Adyen payment terminal security inspection, fetched 2026-09-15]]
