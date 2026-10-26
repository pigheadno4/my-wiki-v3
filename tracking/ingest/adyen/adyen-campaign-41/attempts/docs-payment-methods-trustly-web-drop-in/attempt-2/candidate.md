---
title: "Trustly Web Drop-in integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/trustly/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/trustly/web-drop-in/2026-09-15.md"
tags: [adyen, trustly, web, drop-in, online-banking, redirect]
---

## Overview

This 2026-09-15 Trustly Web Drop-in guide describes adding Trustly to an **existing** Web Drop-in integration, with Customer Area setup, a conditional v6 import, ordinary request-field guidance, and TEST/LIVE entry points. It does not provide a redirect or payment-outcome procedure and does not establish receipt of bank funds. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Start with an existing Web Drop-in integration and add Trustly in the **test Customer Area** before beginning. For **Web Drop-in v6**, the guide imports `AdyenCheckout` and `Trustly` from `@adyen/adyen-web`; it does not state that this import is required for earlier versions. See raw lines 21–34.
- The ordinary Trustly request needs **no additional method-specific fields**, according to the page. It points to `/sessions` as the Drop-in v5.0.0-or-later default and `/payments` for an additional use case, and says there are no Trustly-specific Drop-in configuration steps. These statements do not specify optional universal fields or a full server flow. See raw lines 36–45.
- For TEST, the page links Trustly's test environment, gives a `YYMMDD-XXXX` Login ID/Personal number format with an example, and directs status checks to the test Customer Area. Before accepting live Trustly payments, the merchant must submit a Trustly request in **live Customer Area**. Neither a test-status lookup nor a submitted request proves current live activation or completed payment. See raw lines 47–53.
- **Related overview qualification:** the approved [[source-adyen-docs-payment-methods-trustly]] says that a successful `AUTHORISATION` webhook means verification passed and a bank transfer was initiated, **not that Adyen received funds**. Later cancellation or delayed bank processing can cause failure; its chargeback path is nondefensible. The Drop-in page gives no contrary outcome guarantee. See the overview's raw lines 38–53; this primary raw supplies only TEST status and live-request guidance at lines 47–53.

## Detail locators

- Existing Web Drop-in, test Customer Area and v6 import: raw lines 21–34.
- Ordinary `/sessions` or `/payments` reference and no-extra-field/configuration guidance: raw lines 36–45.
- TEST login fixture, status lookup and live request: raw lines 47–53.
- Cross-page authorized-but-unfunded warning: [[source-adyen-docs-payment-methods-trustly]], overview raw lines 38–53.

## Related

- [[adyen-online-payments]] — main Drop-in route.
- [[source-adyen-docs-payment-methods-trustly]] — method overview and bank-transfer funding warning.
- [[source-adyen-docs-payment-methods-trustly-api-only]] — separate API-only redirect/outcome guide.

## Raw Sources

- [[raw/adyen/docs/payment-methods/trustly/web-drop-in/2026-09-15|Trustly Web Drop-in, captured 2026-09-15]]
