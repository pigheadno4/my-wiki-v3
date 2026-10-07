---
title: "Braintree In-Person Verifone P400 Device Reference"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/reference/verifone-p400-reference"
raw_files:
  - "braintree/in-person/reference/verifone-p400-reference-2026-09-16.md"
tags: [braintree, in-person, verifone, p400, card-reader, keypad]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website device-reference page documents keypad character entry and navigation for a Verifone reader used with the Braintree Verifone Reader app. It includes button functions, utility shortcuts and the page's stated meaning for the default PayPal screensaver. Although the URL is P400-specific, one shortcut row separately assigns deep sleep to the e285; the page must not be generalized across reader models. This snapshot is not evidence of current device availability, merchant or account eligibility, feature enablement, device health, live runtime state, or a successful test or production payment.

## Key takeaways

- Repeated presses of a numeric keypad key cycle through the character choices captured in the key map. The exact per-key character table remains at the locator below.
- The page says some functions are unavailable on-screen and maps reader buttons to closing the current screen or application, going back, and accepting or returning. These are documented controls, not proof that a particular reader, application version or session currently exposes or successfully performs them.
- In the Braintree Verifone Reader app, the captured shortcut table maps `2 + 8` to reader settings from the screensaver. A separate `Hold X` row, qualified as eight seconds in the captured rendering, enters the Power Panel; that row mentions reboot or shutdown for the P400 and deep sleep for the e285, so those device-specific actions should not be conflated.
- The page says the default PayPal screensaver indicates that the reader is connected and ready for test transactions. That documented indicator is not an independent device-health check, live connectivity observation, completed transaction, or production-readiness signal.

## Material warnings

> [!warning] Device and rendering scope
> The URL names the P400, while the raw page title is broader and the Power Panel shortcut row includes a separate e285 deep-sleep action. The captured `Hold X` label and eight-second qualification are preserved as rendered; do not infer the physical button identity or apply either device's action to other reader models.

> [!warning] Snapshot and proof boundary
> This is an unversioned website snapshot of reference UI behavior. A screensaver's documented meaning does not prove current reader connectivity, health, application or firmware compatibility, merchant eligibility, account or feature enablement, runtime behavior, or any test or live payment outcome.

## Detail locators

- Numeric-key cycling behavior and exact character choices for `0` through `9`, `*` and `#`: `### Key Map`, lines 17-33.
- Off-screen-function qualification and the button-function table for close, back, and accept or return: `### Keyboard Navigation`, lines 39-46.
- Braintree Verifone Reader app utility-shortcut scope, `2 + 8` settings action, and the multiline `Hold X`/eight-second Power Panel row with distinct P400 and e285 actions: `### Keyboard Shortcuts`, lines 49-61.
- Connectivity-screen statement and the default PayPal screensaver's documented connected-and-ready-for-test-transactions meaning: line 63.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Related raw API references

- [[raw/braintree/in-person/reference/app-version-release-notes-2026-09-16|Firmware Version Release Notes]] - unread navigation linked by this page; it supplies no version or behavior evidence here
- [[raw/braintree/in-person/reference/emv-receipt-reference-2026-09-16|EMV Receipt Reference]] - unread navigation linked by this page; it supplies no receipt or transaction evidence here

## Raw Sources

- [[raw/braintree/in-person/reference/verifone-p400-reference-2026-09-16|Braintree Verifone Device Reference]] - complete collected page for the keypad character map, keyboard navigation, utility shortcuts and screensaver statement
