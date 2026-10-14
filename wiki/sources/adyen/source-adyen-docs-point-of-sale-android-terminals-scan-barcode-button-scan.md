---
title: "Adyen Android terminal barcode scan-button activation"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/android-terminals/scan-barcode/button-scan"
raw_files:
  - "adyen/docs/point-of-sale/android-terminals/scan-barcode/button-scan/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, barcode-scanner, device-settings]
---

## Overview

This Adyen guide describes enabling the physical barcode scan button on scanner-equipped S1E Barcode, S1E2L, S1F2L and S1U2 Android payment terminals. After Customer Area enablement, pressing the button activates the scanner; on a successful scan, the terminal pastes the barcode content into an input box in an Android app installed on the terminal. The page covers Terminal API or standalone terminal integrations, but this button-to-app path is separate from the linked single-scan and batch-scan Terminal API request flows. [[adyen]] [[adyen-android-terminals]]

## Key takeaways

- The guide names four supported scanner-equipped models: S1E Barcode, S1E2L, S1F2L and S1U2. An Android barcode-scanner app with an input text field must be installed on the terminal to process scanned content. The text goes to that on-terminal app; the page does not promise a POS app on another device receives a Terminal API scan response.
- In Customer Area under In-person payment > Device settings > Device > Barcode scanner, add the setting and enable the barcode scanner button. Configuration can be set at company, merchant account, store or terminal level. Merchant POS Terminal Management Admin can configure any level; Merchant POS Terminal Management can configure merchant level and lower. Save the change.
- Optional settings include a beep after successful scan and a separator after each scan. New line is the default separator; Custom lets the user provide a character. The guide does not specify further parsing or validation behavior for the receiving app.
- Adyen Support can enable a prefix, with merchant-supplied prefix characters, or a software-keyboard mode that emits barcode content as individual keyboard events. The receiving Android app must listen for software keyboard events for that optional mode. It is a distinct input path from ordinary paste into an app's text field.
- The model, role and enablement statements come from a page last modified 2025-02-06 and fetched 2026-09-15. They do not establish current model availability, configuration state, successful scan, app handling or payment execution.

## Detail locators

- Model-specific button, app-input and keyboard-event behavior: pinned raw lines 15–19.
- Integration scope, Customer Area roles, hardware and installed-app prerequisite: pinned raw lines 21–31.
- Customer Area setting, beep and separator options: pinned raw lines 33–50.
- Support-enabled prefix and keyboard-event mode: pinned raw lines 52–55.
- Separate Terminal API single- and batch-scan navigation: pinned raw lines 57–60.

## Related

- [[adyen-android-terminals]] — Android payment terminal hardware and on-device app hub.
- [[adyen-terminal-api]] — separate Terminal API scanner-request architecture.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/android-terminals/scan-barcode/button-scan/2026-09-15|Adyen scan-button activation guide, fetched 2026-09-15]]
