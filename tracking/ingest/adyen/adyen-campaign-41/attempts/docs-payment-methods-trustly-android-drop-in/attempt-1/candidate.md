---
title: "Adyen Trustly Android Drop-in v5 guide"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/trustly/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/trustly/android-drop-in/2026-09-15.md"
tags: [adyen, trustly, android, drop-in, sessions, advanced, redirect]
---

## Overview

This 2026-09-15 captured Adyen page adds Trustly to an existing Android Drop-in integration. It identifies the guide as for Drop-in v5.0.0, released in October 2023, sets v5.0.0 as the minimum for both Sessions and Advanced routes, and points earlier-version users to a separate guide. It supplies a method add-on rather than a full redirect, authorization or settlement procedure. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-trustly]].

## Key takeaways

- Both Sessions and Advanced paths require an existing Android Drop-in integration at minimum version 5.0.0 and Trustly added in Customer Area. The Sessions `/sessions` and Advanced `/payments` sections say Trustly needs no additional method fields. Both Drop-in configuration tabs say no additional Trustly configuration; the page then links to the respective base-guide checkout-session or Drop-in launch step. No Checkout API minimum, request example, bank handoff detail, return callback or result-code sequence is specified here.
- The guide points to a Trustly test environment, gives `YYMMDD-XXXX` as the Login ID/Personal number format with example digits, directs test-payment status checks to Customer Area, and says to submit a request for Trustly in the live Customer Area before accepting live payments. These instructions do not prove current test/live enablement or a payment outcome.
- This add-on does not discuss funds arrival. The linked Trustly overview warns that even a successful `AUTHORISATION` webhook means a bank transfer was initiated and may still fail before funds arrive; subsequent chargeback handling matters. Do not use the short no-extra-fields guide to infer that Drop-in success, authorization, capture or settlement are equivalent.

## Detail locators

- Android scope, v5.0.0/October 2023 boundary and earlier-version route: pinned raw lines 15–21.
- Sessions/Advanced integration and Customer Area prerequisites: pinned raw lines 23–39.
- No-extra-fields API sections and no-extra-configuration Drop-in sections: pinned raw lines 41–59; base integration continuations: lines 61–67.
- Test ID format, test Customer Area and live request: pinned raw lines 69–75.
- Related authorized-but-unfunded qualification: Trustly overview pinned raw `raw/adyen/docs/payment-methods/trustly/2026-09-15.md` lines 38–53.

## Related

- [[adyen-online-payments]] — main provider online-payment concept
- [[source-adyen-docs-payment-methods-trustly]] — shopper redirect and authorized-but-unfunded risk

## Raw Sources

- [[raw/adyen/docs/payment-methods/trustly/android-drop-in/2026-09-15|Trustly Android Drop-in v5 guide, 2026-09-15]]
