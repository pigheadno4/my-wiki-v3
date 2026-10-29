---
title: "Online banking Czech Republic Flutter Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-czech-republic/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-czech-republic/flutter-drop-in/2026-09-15.md"
tags: [adyen, online-payments, online-banking-czech-republic, flutter, drop-in]
---

## Overview

This 2026-09-15-captured Adyen add-on describes Online banking Czech Republic for an existing Flutter Drop-in integration in Sessions and Advanced flows. It covers redirect prerequisites, method setup, and test/live guidance. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-online-banking-czech-republic]] for CZ/CZK method context. The page is not evidence of current account enablement or completed payment.

## Key takeaways

- Sessions requires an existing Flutter Drop-in Sessions integration, Checkout API v68 or later, handling for action.type redirect, and method setup. Its setup row says to contact Support to add the method in Customer Area. The page says no extra method parameters are needed in /sessions and no extra configuration parameters are needed. See raw lines 25–48.
- Advanced requires an existing Flutter Drop-in Advanced integration, handling for action.type redirect, and method setup in Customer Area. The page says no extra method configuration or /payments parameters are needed. These statements are scoped to this Flutter Drop-in guide; the separate API-only guide describes selected-bank issuer handling. See raw lines 58–80 and [[source-adyen-docs-payment-methods-online-banking-czech-republic-api-only]].
- Both test sections instruct testing with real payment details and small amounts, checking status in the test Customer Area Payment list, and adding the method in Customer Area for live acceptance. These are captured instructions, not proof of tests or live transactions. See raw lines 50–56 and 82–88.

> [!warning] Source link and setup discrepancy
> The Sessions prerequisite names Flutter Drop-in Sessions but links to the Advanced flow (raw line 33); the Sessions redirect and request links point to Sessions (raw lines 35 and 42). Sessions says to contact Support to add the method, while Advanced says to add it in Customer Area (raw lines 36 and 68). Verify the actual Flutter Sessions base guide and account-specific enablement path; this snapshot does not reconcile the wording.

## Detail locators

- Sessions prerequisites and setup: raw `## Sessions flow Drop-in`, lines 25–36.
- No extra Sessions request/configuration parameters: raw lines 38–48.
- Sessions test/live: raw `## Test and go live`, lines 50–56.
- Advanced prerequisites, request/configuration and test/live: raw `## Advanced flow Drop-in`, lines 58–88.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-czech-republic/flutter-drop-in/2026-09-15|Online banking Czech Republic Flutter Drop-in, captured 2026-09-15]]
