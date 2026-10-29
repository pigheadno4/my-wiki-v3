---
title: "Online banking Poland Flutter Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-poland/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-poland/flutter-drop-in/2026-09-15.md"
tags: [adyen, online-payments, online-banking-poland, flutter, drop-in]
---

## Overview

This 2026-09-15-captured Adyen add-on describes Online banking Poland for an existing Flutter Drop-in integration, separately for Sessions and Advanced flows. It covers request fields, redirect handling, and test/live setup. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-online-banking-poland]] for method context. This snapshot does not establish current merchant eligibility or final payment success.

## Key takeaways

- Sessions requires an existing Flutter Drop-in Sessions integration, Checkout API v68 or later, and handling for action.type redirect. Its setup instruction says to contact Support to add Online banking Poland in Customer Area. The /sessions table marks shopperEmail required with a 50-character maximum. The PL/PLN 1000 and app-style returnUrl are sample values. See raw lines 25–68.
- Advanced requires an existing Flutter Drop-in Advanced integration, redirect handling and method setup. Its setup instruction says to add the method in Customer Area. The /payments table marks shopperEmail required with a 50-character maximum and lists paymentMethod.issuer for the selected bank without marking it required. The example uses type onlineBanking_PL, issuer 141, PLN 1000 and a web returnUrl; those are example values, not a Flutter return URL prescription. The illustrated RedirectShopper response carries a redirect action, not a final paid outcome. See raw lines 282–331 and 643–657.
- Both flows say no additional Online banking Poland configuration parameters are needed. Test statuses are checked in the test Customer Area Payment list; before live acceptance the page calls for a request for the method in the live Customer Area. See raw lines 270–280, 294–298 and 659–663.

> [!warning] Source link and setup discrepancy
> The Sessions prerequisite names a Flutter Drop-in Sessions integration but its link points to the Advanced flow (raw line 33). The Sessions setup row says to contact Support to add the method, whereas the Advanced setup row says to add it in Customer Area (raw lines 36 and 292). Use the verified flow-specific Flutter base route and confirm the method enablement path for the account; this snapshot does not reconcile the two instructions.

## Detail locators

- Sessions requirements, redirect and setup: raw `## Sessions flow Drop-in`, lines 25–36.
- Required Sessions shopperEmail and sample request: raw `## Add additional parameters to your /sessions request`, lines 40–68.
- No extra configuration and Sessions test/live: raw lines 270–280.
- Advanced requirements, setup and no extra configuration: raw lines 282–298.
- Advanced shopperEmail/issuer table and example request: raw `## Add additional parameters to your /payments request`, lines 302–331.
- Redirect example and Advanced test/live: raw lines 643–663.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-poland]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-poland/flutter-drop-in/2026-09-15|Online banking Poland Flutter Drop-in, captured 2026-09-15]]
