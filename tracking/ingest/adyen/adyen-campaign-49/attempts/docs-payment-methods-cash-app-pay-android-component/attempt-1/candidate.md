---
title: "Cash App Pay Android Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-pay/android-component"
raw_files:
  - "adyen/docs/payment-methods/cash-app-pay/android-component/2026-09-15.md"
tags: [adyen, cash-app-pay, android, component, tokenization]
---

## Overview

This 2026-09-15-captured Adyen guide adds Cash App Pay to an existing Android Components integration. It addresses Sessions and Advanced flows, asynchronous payment results, optional future payments, and test/live setup. The page says it is for Android Components **v5.0.0**, released in October 2023, and routes older versions to a separate guide. It is a method-specific supplement to [[adyen-online-payments]], not evidence of current merchant enablement or a completed payment. See [[adyen]] and [[source-adyen-docs-payment-methods-cash-app-pay]] for the method overview.

## Key takeaways

- **Prerequisites and additions:** Both Sessions and Advanced require an existing Android Components integration at minimum **v5.0.0** and Cash App Pay added in Customer Area. The guide says Cash App Pay needs no additional method-specific fields in the respective `/sessions` or `/payments` request and no additional Component configuration. It still points to the base flow's session creation or Component launch; “no additional” does not remove base integration requirements. See pinned raw lines 18–64.
- **Payment result is asynchronous:** The page tells merchants to show the `/payments/details` `resultCode` and also receive the outcome by webhook. `Received` means the shopper completed the payment step but the final result is unknown; an `AUTHORISATION` webhook updates status. `Authorised` indicates success, with a separate capture needed if manual capture is used. `Cancelled`, `Error`, and `Refused` have distinct recovery guidance; Error/Refused point to `refusalReason`. Do not treat `Received` as authorization or captured funds. See raw lines 66–78.
- **Future payments:** The page says Cash App Pay supports tokenization for recurring and card-on-file payments. It describes bypassing shopper approval for those future token payments **when the shopper gave permission to save payment details at token creation**. Adyen strongly recommends explicit permission and transparency about recurring schedule and amount to reduce chargeback risk; this recommendation is not a claim that every subsequent payment will succeed. See raw lines 80–84.
- **Test and live:** Test in the test environment with Cash App Pay sandbox magic values and inspect test payments in Customer Area under **Payments > Payment list**. Live use requires adding Cash App Pay in the **live Customer Area**. These are provider instructions, not evidence that a test or live transaction ran for a particular merchant. See raw lines 86–90.

## Detail locators

- Page version and earlier-version route: pinned raw lines 14–18.
- Sessions/Advanced prerequisites and no-extra-field/configuration statements: raw lines 20–64.
- Result codes, webhooks and manual capture: raw lines 66–78.
- Token permission and recurring/card-on-file guidance: raw lines 80–84.
- Test magic values, status lookup and live setup: raw lines 86–90.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-cash-app-pay]]
- [[source-adyen-docs-payment-methods-cash-app-pay-android-component-earlier-versions]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-pay/android-component/2026-09-15|Cash App Pay Android Component guide, captured 2026-09-15]]
