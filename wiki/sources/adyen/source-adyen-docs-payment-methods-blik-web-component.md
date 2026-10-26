---
title: "BLIK Web Component"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/blik/web-component"
raw_files:
  - "adyen/docs/payment-methods/blik/web-component/2026-09-15.md"
tags: [adyen, blik, poland, web, components, online-payments, tokenization]
---

## Overview

This BLIK guide (metadata last modified 2020-10-06, captured 2026-09-15) adds BLIK to an existing **Web Components** integration. It covers BLIK with a six-digit code and a distinct BLIK One Click consent/token path. The main payment response can be `Pending` with an await-style action while the shopper completes the payment in a BLIK app; an `AUTHORISATION` webhook supplies the outcome. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The prerequisite table says Web Components **v3.9.0 or later** and BLIK added in the **test** Customer Area. For Web Components v6 it shows a named `Blik` import and constructor; v5.x.x or earlier uses `checkout.create('blik')`. The v6 constructor sample is malformed (`const  = new Blik(...)`), and its import-guide URL is labeled Components but contains `integration=Drop-in`. The prerequisite URL also contains an encoded `/?target=_blank` fragment. Do not copy these snippets or links as verified setup instructions. See raw lines 21–66.
- The `/sessions` tab says no BLIK-specific extra fields; it calls Sessions the default with Components v5.0.0 or later. The separate `/payments` material does require BLIK fields for its API route. The page does not clearly map every version and server-side flow combination beyond those statements. See raw lines 68–92.
- For **BLIK with code**, `/paymentMethods` discovery uses `countryCode: PL`, `amount.currency: PLN` and minor-unit value. The form collects a six-digit `blikCode`; `/payments` sends `paymentMethod.type: blik` plus that code. A stored BLIK method is shown as conditional on the shopper having previously signed up for One Click. See raw lines 96–116 and 118–423.
- The shown `/payments` response has `resultCode: Pending` and an action intended for a waiting screen while the shopper completes payment in the BLIK app. The example embeds a documentation hint in `action.type` around `await`; treat the sample as annotated text, not a literal API enum. `Pending` and an app interaction are not final authorization. The guide says to use the `AUTHORISATION` webhook (`success: false` or `true`) for the outcome; `Refused` can be reported, including for an incorrect code. See raw lines 425–467.
- **BLIK One Click** describes a consent request for future payments without the six-digit code, with `shopperReference`, `storePaymentMethod: true`, and `recurringProcessingModel: CardOnFile`. The token lifecycle webhook `recurring.token.created` carries `storedPaymentMethodId`, `eventId`, and `shopperReference`; the merchant must enable that webhook. Discovery includes `shopperReference` and a linked issuer label. Yet this “without code” section repeats `paymentMethod.blikCode` as a `/payments` field, and its curl example has a missing comma after `CardOnFile` and quotes `storePaymentMethod` as a string. The prose names `additionalData.BLIK.APP_LABEL` but the example spells `Blik.APP_LABEL`. Preserve those inconsistencies; this page does not give a complete later code-free token-charge request. [[adyen-tokenization]] See raw lines 483–595.
- Testing both paths names BLIK code `999000`, guideline compliance and end-to-end testing. The with-code live step says to add BLIK in live Customer Area; the One Click live section additionally says to contact BLIK for certification and enablement before live acceptance. These are distinct statements, not proof of present account approval or a successful payment. See raw lines 78–88, 469–479 and 597–610.

## Detail locators

- Web Components version/setup and v6/v5 Component examples: raw lines 21–66.
- Sessions versus `/payments` branch: raw lines 68–92.
- BLIK-with-code PL/PLN discovery, six-digit code and request examples: raw lines 96–423.
- Pending/await waiting screen and AUTHORISATION webhook: raw lines 425–467.
- One Click discovery, consent request, token/issuer label and sample conflicts: raw lines 483–595.
- TEST codes and distinct live gates: raw lines 78–88, 469–479 and 597–610.

## Related

- [[adyen-online-payments]] — Web payment flow context.
- [[adyen-tokenization]] — shopper consent and stored-method lifecycle.
- [[source-adyen-docs-payment-methods-blik]] — BLIK method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/blik/web-component/2026-09-15|BLIK Web Component, captured 2026-09-15]]
