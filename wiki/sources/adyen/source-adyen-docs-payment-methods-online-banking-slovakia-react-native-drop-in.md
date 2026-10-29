---
title: "Online banking Slovakia React Native Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-slovakia/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-slovakia/react-native-drop-in/2026-09-15.md"
tags: [adyen, online-banking-slovakia, react-native, drop-in, redirect]
---

## Overview

This 2026-09-15 guide gives Online banking Slovakia-specific additions to existing React Native Drop-in integrations for Sessions or Advanced server-side flow. It relies on the corresponding base integration for the rest of the payment lifecycle. The linked [[source-adyen-docs-payment-methods-online-banking-slovakia|method overview]] identifies this as an SK/EUR bank redirect method. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions flow:** requires existing React Native Drop-in Sessions integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and adding Online banking Slovakia in Customer Area. It says no additional method configuration is needed. The section provides no separate method-specific `/sessions` field table. See raw lines 25–42.
- **Advanced flow:** requires existing React Native Drop-in Advanced integration, the same redirect handling and Customer Area method setup. Its method-specific `/payments` table requires `paymentMethod.issuer`, the issuing bank selected by the shopper. The examples use `paymentMethod.type: onlineBanking_SK` and `issuer: cs`; `cs` is an example issuer, not an exhaustive bank list. No extra method configuration is needed. The Advanced requirements table does not state the Sessions v68 minimum. See raw lines 52–99 and language examples at 101–390.
- Both sections say to test with real payment details and small amounts, inspect test payments in Customer Area, and add the method in Customer Area for live acceptance. This is historical setup/test guidance, not evidence of live enablement or a completed payment. See raw lines 44–50 and 392–398.

> [!warning] Source links and sample version
> The Sessions requirement text points to a React Native **Sessions** integration, but its URL is `advanced-flow` (raw line 33); the redirect-handling link at line 35 uses `sessions-flow`. Follow the route matching the selected server-side flow. The Go example labels the API library **v10.4.0** while its imports use `/v9/` paths (lines 260–266); do not infer a copy-ready Go import/version combination from this snippet.

> [!warning] Issuer example qualification
> The React Native Advanced request examples use `issuer: cs` (this raw lines 95–99 and repeated language samples), while the approved [[source-adyen-docs-payment-methods-online-banking-slovakia-api-only|API-only guide]] lists six bank issuer IDs and does not include `cs` in its captured table (related raw lines 44–59). Neither snapshot establishes whether `cs` is currently valid or invalid, nor that the table is universal. Use the issuer ID returned in `/paymentMethods` for the bank the shopper selected, as that API-only guide describes (related raw lines 44–48).

## Detail locators

- Sessions prerequisites and no extra configuration: raw lines 25–42.
- Advanced prerequisites, required issuer and request examples: raw lines 52–99 and 101–390.
- Test and live setup: raw lines 44–50 and 392–398.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-slovakia]]
- [[source-adyen-docs-payment-methods-online-banking-slovakia-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-slovakia/react-native-drop-in/2026-09-15|Online banking Slovakia React Native Drop-in, captured 2026-09-15]]
