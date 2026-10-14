---
title: "Run hardware tests | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/pos-troubleshooting/hardware-tests"
raw_files:
  - "adyen/docs/point-of-sale/pos-troubleshooting/hardware-tests/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, hardware-diagnostics, troubleshooting]
---

## Overview

This Adyen Docs troubleshooting page explains on-terminal hardware tests for the chip-card reader, magnetic-swipe reader, NFC antenna and, on models with a physical keypad, the keypad. It applies to Adyen payment terminals in a Terminal API integration or standalone solution and says the feature is available on non-legacy terminal models. It is an operator diagnostic procedure, not certification of a particular device or proof that its payment path works. See [[adyen]] and [[adyen-payment-terminals]].

## Key takeaways

- Open **Settings > Diagnostics > Hardware** on the terminal. Older non-Android menu structures use a star-key/Confirm path when a keypad is present or a Menu button then **Hardware diagnostics** when one is absent. On non-Android models, select the arrow to start a chosen test. The guide gives no Admin-passcode or exact model/software-version rule for these paths; use the model's menu guidance where needed.
- The terminal displays instructions and animated steps for each test. A circle beside a test initially reflects its **previous** result; run the test before relying on it for the current check. The guide says green indicates the tested component is fine and red indicates test failure. If the operator is sure the test was done correctly, report a failed test to Adyen Support. These are component-test results, not a whole-device health, tamper, network, authorization or PCI-compliance conclusion.
- If the terminal becomes unresponsive during a test, **Report issue** logs the issue on the terminal, stops the test and returns to the menu. That instruction concerns stopping the hardware test, not canceling a payment. After ordinary completion, the display shows the result and returns to the menu. Keypad test beeps use standard volume only during that test, then the configured volume resumes.
- Results go into the terminal log and are sent to Adyen's back end during an automatic maintenance call. For a malfunctioning terminal, **Diagnostic report > Send report** creates and sends a log file. The guide says the terminal prevents a second report for five minutes; sending a log is not a remote repair or confirmation that Adyen resolved the fault.
- The page does not cover battery, printer or scanner tests, and its embedded NFC test video is an example. Those components and model-specific limits require their own evidence.

## Detail locators

- `Run hardware tests`, pinned raw lines 15–28: component list, keypad qualification, on-screen instructions/temporary beep volume, log/maintenance-call handling.
- `Requirements`, lines 30–37: Terminal API or standalone Adyen-terminal scope and non-legacy hardware limit.
- `Test the terminal hardware`, lines 39–62: modern/old-menu routes, prior-result indicator, non-Android start arrow, Report issue behavior and red/green result handling.
- `Example test`, lines 64–68: embedded NFC antenna video, without an added hardware guarantee.
- `Send a diagnostic report`, lines 70–83: malfunction-log submission path and five-minute repeat limit.

## Related

- [[adyen-payment-terminals]] — physical-terminal model and maintenance hub.
- [[adyen-terminal-management]] — maintenance-call context; this page does not give fleet configuration steps.
- [[source-adyen-docs-point-of-sale-menu-access]] — model/software-specific terminal menu guidance.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/pos-troubleshooting/hardware-tests/2026-09-15|Adyen hardware-test guide, fetched 2026-09-15]]
