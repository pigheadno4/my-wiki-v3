---
title: "Online banking Czech Republic iOS Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-czech-republic/ios-component"
raw_files:
  - "adyen/docs/payment-methods/online-banking-czech-republic/ios-component/2026-09-15.md"
tags: [adyen, online-payments, online-banking-czech-republic, ios, components]
---

## Overview

This 2026-09-15-captured Adyen add-on describes Online banking Czech Republic for an existing iOS Components integration in Sessions and Advanced flows. It covers request additions, Component initialization, redirect handling, and test/live setup. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-online-banking-czech-republic]] for CZ/CZK method context. It does not establish current account enablement or final payment success.

## Key takeaways

- Sessions requires an existing iOS Components Sessions integration, Checkout API v68 or later, handling for action.type redirect, and Customer Area method setup. The page says no extra method parameters are needed in /sessions and no extra configuration parameters are needed. See raw lines 25–48.
- Advanced requires an existing iOS Components Advanced integration, handling for action.type redirect, and Customer Area method setup. The page says no extra method configuration or /payments parameters are needed. These no-extra-field statements belong to this iOS Components guide and do not override the selected-issuer handling described in the separate custom API-only guide. See raw lines 83–99 and 125–129; compare [[source-adyen-docs-payment-methods-online-banking-czech-republic-api-only]].
- The initialization prose names OnlineBankingComponent, with the session as delegate in Sessions and the Component delegate set to self in Advanced. The Swift snippets also use None.self to look up the payment method and pass an onlineBankingCzechRepublicConfiguration object despite the no-extra-configuration prose. They are not a verified executable recipe. See raw lines 50–73 and 101–123.
- The test section instructs testing with real payment details and small amounts, checking test payment status in the test Customer Area Payment list, and adding the method in Customer Area for live acceptance. These are captured instructions, not evidence of actual test or live payments. See raw lines 75–81 and 131–137.

> [!warning] Source inconsistency
> Both Swift snippets look up None.self while the prose names OnlineBankingComponent, and both pass a configuration object although the page says no extra configuration is needed (raw lines 46–73 and 97–123). The Advanced prerequisite names iOS Components but links to integration=Drop-in (raw line 91); its redirect link does target Components (raw line 92). Verify the actual iOS Components base guide, SDK type and setup before implementing.

## Detail locators

- Sessions prerequisites, redirect and no extra /sessions fields: raw `## Sessions flow Component`, lines 25–42.
- Sessions configuration and initialization: raw lines 44–73.
- Advanced prerequisites, redirect and no extra configuration: raw `## Advanced flow Component`, lines 83–99.
- Advanced initialization and no extra /payments fields: raw lines 101–129.
- Test/live guidance: raw `## Test and go live`, lines 75–81 and 131–137.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-czech-republic/ios-component/2026-09-15|Online banking Czech Republic iOS Component, captured 2026-09-15]]
