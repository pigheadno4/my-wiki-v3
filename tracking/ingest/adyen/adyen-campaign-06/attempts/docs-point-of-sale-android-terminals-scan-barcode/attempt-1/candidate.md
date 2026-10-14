---
title: "Barcode scanning | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/android-terminals/scan-barcode"
raw_files:
  - "adyen/docs/point-of-sale/android-terminals/scan-barcode/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, barcode-scanning, terminal-api]
---

## Overview

Adyen's barcode-scanning overview, captured 2026-09-15, identifies integrated scanner use on S1E Barcode, S1E2L, S1F2L and S1U2 Android payment terminals. It routes three interaction modes: on-device scan button to an Android input-field app, single scan by Terminal API request/response, and multiple scans by Terminal API with event notifications. Start at [[adyen-android-terminals]] for the device route; [[adyen-terminal-api]] is relevant only to the two API modes. The dated overview does not establish current hardware, firmware, app-configuration or account eligibility, successful scanning, or payment execution.

## Key takeaways

- The on-device button route pastes barcode content into an installed Android barcode-scanner app with an input text field. The overview does not define the app's installation/configuration steps; follow its linked button guide.
- A Terminal API request can activate a single scan and return barcode content in the response. A separate multi-scan path works while the scan button is held and sends content through event notifications. These are different delivery paths, not interchangeable proof of a completed transaction; the linked single- and batch-session guides own request format, session lifecycle and notification setup.
- Decoder support varies by model and barcode symbology. In this snapshot's matrix, S1U2 lacks CODE 128, MaxiCode and PDF417 while the other three named models list those formats. A successful scan can still return `Barcode.Data` with `Barcode.Symbology=UNKNOWN` if the symbology is not recognized.
- The overview gives no terminal-software minimum or universal scanner enablement rule. Use the model and per-mode guides for any version, button configuration or Terminal API event prerequisites; do not infer them from the overview's navigation labels.

## Detail locators

- [[raw/adyen/docs/point-of-sale/android-terminals/scan-barcode/2026-09-15#Barcode scanning|Barcode scanning]] — four named models and three button/API delivery modes (lines 15–25).
- [[raw/adyen/docs/point-of-sale/android-terminals/scan-barcode/2026-09-15#Barcode symbologies|Barcode symbologies]] — `Data`/`UNKNOWN` behavior and model-by-format support matrix (lines 27–47).
- [[raw/adyen/docs/point-of-sale/android-terminals/scan-barcode/2026-09-15#Next steps|Next steps]] — separate button, single-session and batch-session guides (lines 49–61).

## Related

- [[adyen]] — provider context and dated website-source catalog.
- [[adyen-android-terminals]] — primary Android scanner-device route.
- [[adyen-terminal-api]] — request/response and event-notification scan paths.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/android-terminals/scan-barcode/2026-09-15|Barcode scanning overview (fetched 2026-09-15)]]