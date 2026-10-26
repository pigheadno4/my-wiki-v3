---
title: "Adyen Trustly iOS Drop-in guide"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/trustly/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/trustly/ios-drop-in/2026-09-15.md"
tags: [adyen, trustly, ios, drop-in, sessions, advanced, online-banking]
---

## Overview

This 2026-09-15 Adyen page adds Trustly to an existing **iOS Drop-in** integration. It gives test-account setup, endpoint choice, version-tabbed Drop-in configuration statements and TEST/LIVE routes. It does not show a Trustly redirect action, shopper return, result code or webhook sequence; those belong to the base and other method guides. The related Trustly overview warns that successful `AUTHORISATION` means bank-transfer initiation, not received funds, and documents unfunded chargebacks. This source does not prove merchant enablement, payment execution or settlement. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-trustly]].

## Key takeaways

- **Base and endpoint scope:** requires an existing iOS Drop-in integration and Trustly added in the **test** Customer Area. The page says no additional Trustly-specific fields; it calls `/sessions` the default with Drop-in **v5.0.0 or later** and points to `/payments` if an additional use case was implemented. That v5 default does not exclude its separate v4.x.x configuration tab. (raw lines 21–43)
- **Drop-in configuration:** both v5.0.0-or-later and v4.x.x tabs state there is no required Trustly-specific Drop-in integration. This does not remove ordinary base-flow configuration or imply the two major versions use identical implementation. The See also iOS “Components integration guide” URL points to **Components**, despite this page being Drop-in; verify the correct main integration route. (raw lines 35–43, 53–57)
- **Outcome/funds boundary:** the page does not describe result handling. The related Trustly overview says successful `AUTHORISATION` confirms checks and transfer initiation only; funds can still fail to arrive, with a chargeback path that cannot be defended. Do not infer settlement from a base-flow authorization or a completed Drop-in view. (this page raw lines 28–57; related overview raw lines 38–53)
- **Environment:** the source points to a Trustly TEST environment, a `YYMMDD-XXXX` Login ID/Personal number test format and TEST Customer Area status check. Live acceptance requires a separate request in the **live** Customer Area. None of those instructions establishes actual test success or live activation. (raw lines 45–51)

## Detail locators

- iOS Drop-in identity, setup and endpoint choice: pinned raw lines 15–33.
- v5/v4 no Trustly-specific Drop-in steps and misrouted Components See also: pinned raw lines 35–57.
- TEST identity/status and LIVE request: pinned raw lines 45–51.
- Related overview's authorization-versus-funds and chargeback warning: [[source-adyen-docs-payment-methods-trustly]], raw lines 38–53.

## Related

- [[adyen-online-payments]] — main provider payment context
- [[source-adyen-docs-payment-methods-trustly]] — bank-transfer and chargeback qualification

## Raw Sources

- [[raw/adyen/docs/payment-methods/trustly/ios-drop-in/2026-09-15|Trustly iOS Drop-in guide, 2026-09-15]]
