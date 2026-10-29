---
title: "Online banking Czech Republic React Native Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-czech-republic/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/online-banking-czech-republic/react-native-component/2026-09-15.md"
tags: [adyen, online-payments, online-banking-czech-republic, react-native, components]
---

## Overview

This 2026-09-15-captured Adyen add-on describes Online banking Czech Republic for React Native Components. It explicitly says React Native Components do not support Sessions flow; its instructions cover an existing Advanced flow, redirect handling, method setup, and test/live steps. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-online-banking-czech-republic]] for method context. The snapshot does not prove current enablement or completed payment.

## Key takeaways

- Sessions is marked unavailable for React Native Components on this page. For Advanced, use an existing React Native Components integration, handle action.type redirect, and add the method in Customer Area. See raw lines 25–41.
- The guide says no additional Online banking Czech Republic configuration parameters and no additional method parameters in /payments. Those statements are scoped to this React Native Components Advanced add-on; the separate API-only guide describes selected-issuer handling for a custom bank-selection flow. See raw lines 43–53 and [[source-adyen-docs-payment-methods-online-banking-czech-republic-api-only]].
- Its test section says to use real payment details and small amounts, inspect the test Customer Area Payment list, and add the method in Customer Area to accept live payments. These are captured instructions, not proof of actual testing or live acceptance. See raw lines 55–61.

> [!warning] Base guide link
> The Advanced prerequisite names React Native Components but links to integration=Drop-in (raw line 39); the redirect and /payments links target Components (raw lines 40 and 53). Verify the React Native Components Advanced base guide instead of following the mismatched prerequisite link as a Components recipe.

## Detail locators

- Sessions unavailability: raw `## Sessions flow Component`, lines 25–29.
- Advanced prerequisites and redirect: raw `## Advanced flow Component`, lines 31–41.
- No extra configuration or /payments fields: raw lines 43–53.
- Test/live steps: raw `## Test and go live`, lines 55–61.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-czech-republic/react-native-component/2026-09-15|Online banking Czech Republic React Native Component, captured 2026-09-15]]
