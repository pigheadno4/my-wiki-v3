---
title: "Online banking Thailand React Native Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-thailand/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-thailand/react-native-drop-in/2026-09-15.md"
tags: [adyen, online-banking, thailand, react-native, drop-in]
---

## Overview

This 2026-09-15 guide gives Online banking Thailand additions to an existing React Native Drop-in integration, separating Sessions and Advanced server-side flows. Both sections require redirect handling and method setup; this is not a complete standalone integration. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Sessions requires an existing React Native Drop-in Sessions flow, Checkout API v68 or later, `action.type: redirect` handling and Customer Area method setup. The Sessions integration-type link unexpectedly points to an Advanced-flow URL, while the redirect and session-creation links point to Sessions; retain the prose's Sessions scope without treating the misrouted link as a requirement change. See raw lines 25–42.
- Sessions states no extra `/sessions` parameters or Online banking Thailand configuration parameters. Advanced requires an existing React Native Drop-in Advanced flow, redirect handling and Customer Area setup, and states no extra method-specific configuration or `/payments` parameters. The v68 statement appears only in the Sessions section. See raw lines 38–48 and 58–80.
- Both test sections say to use an available issuer ID and inspect test payment status in Customer Area Payment list, but call it an Online banking Thailand Component on this Drop-in page and provide no issuer-ID list. They require a separate request in live Customer Area before live acceptance. This text does not prove a tested outcome, current availability or a final payment after redirect. See raw lines 50–56 and 82–88.

## Detail locators

- Sessions prerequisites, link mismatch and no-extra-parameter statements: raw lines 25–48.
- Advanced prerequisites and no-extra-parameter statements: raw lines 58–80.
- TEST issuer wording and separate live request: raw lines 50–56 and 82–88.

## Related

- [[adyen-online-payments]] — main online-payments concept.
- [[source-adyen-docs-payment-methods-online-banking-thailand]] — separate method overview.
- [[adyen]] — provider entry.

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-thailand/react-native-drop-in/2026-09-15|Online banking Thailand React Native Drop-in (2026-09-15)]]
