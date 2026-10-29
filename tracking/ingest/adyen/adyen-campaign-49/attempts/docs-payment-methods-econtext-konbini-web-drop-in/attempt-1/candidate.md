---
title: "Japanese convenience stores Web Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/econtext-konbini/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/econtext-konbini/web-drop-in/2026-09-15.md"
tags: [adyen, econtext, konbini, japan, web-drop-in, voucher]
---

## Overview

This 2026-09-15-captured Adyen page adds **Japanese convenience-store payments through econtext** to an existing Web Drop-in integration. It distinguishes store and Pay-easy Customer Area additions, optional shopper-detail configuration, simulator testing, and pending versus paid voucher status. See [[adyen]], [[adyen-online-payments]], and the method overview [[source-adyen-docs-payment-methods-econtext-konbini]] for the **7-Eleven local-entity condition**, redirect/native voucher distinction, and offer-expiry context.

## Key takeaways

- The guide requires an existing Web Drop-in integration and separate Customer Area additions: **eContext Convenience Stores** for Lawson, Mini Stop, Family Mart and Seicomart; **eContext PayEasy ATM** for ATM; **eContext PayEasy Online Banking** for online banking; and **eContext 7Eleven** for 7-Eleven (raw lines 21–29). These setup routes do not establish current merchant entitlement; the linked overview states a 7-Eleven local-entity condition.
- For **Web Drop-in v6**, the page imports `Econtext` from `@adyen/adyen-web`. It says Japanese convenience stores need **no additional request fields** or required Drop-in-specific configuration. The API reference points to `/sessions` as the default with Drop-in v5.0.0 or later and to `/payments` for an additional use case (raw lines 31–50).
- Optional `personalDetailsRequired: false` hides shopper name, email and telephone input fields; the table says it was added in **v5.2.0** and defaults to `true`. The example places it under `paymentMethodsConfiguration.econtext_stores` (raw lines 52–79). The sample's inline comment contains HTML/Markdown markup, and its mount line has an unquoted `#konbini-container`; treat it as illustrative, not copy-ready JavaScript (raw lines 62–90).
- The test section says **7-Eleven voucher payments can only be tested in the live environment**, with Support setup for penny testing (raw line 95). Yet the subsequent econtext simulator procedure offers a **7-Eleven** selection (raw lines 97–115). This is an unresolved source-level testing conflict; do not infer that the test simulator can complete a 7-Eleven payment. The raw gives simulator access details and a reference format derived from an `AUTHORISATION` webhook; use the pinned raw for those operational details rather than repeating credentials here (raw lines 97–121).
- The page says to wait **15 minutes for the webhook** during simulator testing. In test Customer Area, pending or expired vouchers are under **Offers** and paid vouchers under **Payment list**. A voucher/reference or an `AUTHORISATION` webhook reference alone is not equivalent to the later paid status. Live acceptance requires a request to add 7-Eleven or other Japanese convenience stores in live Customer Area (raw lines 109–128).

> [!warning] Conflicting 7-Eleven test instructions
> Raw line 95 says 7-Eleven voucher payments can only be tested live with Support-assisted penny testing, while raw lines 111–115 include a 7-Eleven simulator choice. The captured page does not resolve which path applies. Verify with Adyen before using that option to infer test coverage.

## Detail locators

- Web Drop-in and separate econtext method setup: raw `## Requirements`, lines 21–29.
- Web v6 import, endpoint references and no-required-configuration claim: raw lines 31–50.
- Optional shopper-detail fields and illustrative configuration: raw lines 52–90.
- 7-Eleven testing conflict and simulator/webhook steps: raw `## Test and go live`, lines 93–121.
- Pending versus paid test status and live request: raw lines 123–128.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-econtext-konbini]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/econtext-konbini/web-drop-in/2026-09-15|Japanese convenience stores Web Drop-in, captured 2026-09-15]]
