---
title: "Adyen POS terminal diagnostics overview"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/diagnostics"
raw_files:
  - "adyen/docs/point-of-sale/diagnostics/2026-09-15.md"
tags: [adyen, point-of-sale, terminals, diagnostics, connectivity, terminal-api]
---

## Overview

This Adyen Docs page routes readers to remote and terminal-side checks for the state of a payment terminal. In a Terminal API integration, a remote `DiagnosisRequest` checks component condition and returns battery charge level when applicable plus an unconfirmed batch count. For **cloud** Terminal API, Customer Area or an API request can check whether a specific terminal has a live WebSocket connection to Terminal API. On-terminal checks cover connection to the Adyen payments platform and hardware components. This overview does not establish an individual payment's authorization, capture, or final status.

## Key takeaways

- The unconfirmed batch count is defined here as payments the terminal has not been able to send to the Adyen host. It indicates a delivery backlog, not whether any one payment ultimately succeeded or failed.
- A live cloud WebSocket check concerns a specific terminal's connection to Terminal API. It differs from the terminal-side check of connectivity with Adyen's payments platform and from a payment transaction-status request.
- The linked `DiagnosisRequest`, cloud-connection, connection-test, and hardware-test pages are next-step navigation. Their detailed request fields, error interpretation, and procedures are not established by this overview snapshot. No test/live environment guarantee is specified here.

## Detail locators

- Remote diagnosis, conditional battery result, and unconfirmed batch meaning: `#### Remote tests`, raw lines 21–23. Cloud WebSocket check and its Terminal API scope: line 25.
- On-terminal Adyen-platform connectivity and hardware checks: `#### Tests on the terminal`, raw lines 27–31. Four linked next-step routes: `## What do you want to do?`, raw lines 33–57.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — Terminal API communication and separate transaction-status recovery.
- [Make a diagnosis request](https://docs.adyen.com/point-of-sale/diagnostics/request-diagnosis) — detailed remote diagnostic route; not read as evidence here.
- [Check cloud connection](https://docs.adyen.com/point-of-sale/diagnostics/check-cloud-connection) — detailed WebSocket check route; not read as evidence here.
- [Run connection tests](https://docs.adyen.com/point-of-sale/pos-troubleshooting/connection-tests) and [run hardware tests](https://docs.adyen.com/point-of-sale/pos-troubleshooting/hardware-tests) — terminal-side procedure routes; not read as evidence here.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/diagnostics/2026-09-15|Adyen Docs: Run diagnostics (2026-09-15 snapshot)]]
