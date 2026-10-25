---
title: "Online banking Thailand Android Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-thailand/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-thailand/android-drop-in/2026-09-15.md"
tags: [adyen, online-banking, thailand, android, drop-in, redirect]
---

## Overview

This [[adyen]] page, captured 2026-09-15, gives **Online banking Thailand-specific additions** to an existing Android Drop-in integration, split by Sessions and Advanced server-side flows. It is not a complete base integration or evidence of current merchant eligibility or a completed payment. The method overview supplies the TH/THB, bank-redirect and asynchronous-result context; see [[source-adyen-docs-payment-methods-online-banking-thailand]] and [[adyen-online-payments]]. See raw lines 15–23.

## Key takeaways

- **Sessions:** start with an existing Android Sessions Drop-in integration using Checkout API **v68+**, then add Online banking Thailand in Customer Area. The page says no method-specific parameters are needed when creating a `/sessions` payment session. This v68+ requirement is given for Sessions; the Advanced section does not state it. See raw lines 25–40.
- **Advanced:** start with an existing Android Advanced Drop-in integration configured to handle `action.type: redirect`, and add the method in Customer Area. The page says no additional parameters are needed on `/payments`. These statements concern extra **method-specific** fields in an existing flow; they do not remove the base flow's ordinary requirements. See raw lines 74–82 and 106–110.
- **Drop-in display:** both flow sections list optional `setSubmitButtonVisible`; `false` hides the submit button and the documented default is `true`. Their Kotlin code fences show placeholders and a malformed nested-brace structure, so use the parameter table and base integration guide rather than treating those snippets as copy-ready code. See raw lines 42–62 and 84–104.
- **Test/live boundary:** the page suggests using an issuer ID available for the Online banking Thailand Component for the relevant country/region to make test payments and checking their status in the TEST Customer Area. It does not list issuer IDs or prove any one is available. Before accepting live payments, it directs a separate Online banking Thailand request in the **live Customer Area**. Testing or redirect initiation is not evidence of final authorization or settlement; the method overview describes asynchronous results. See raw lines 64–72 and 112–118.

## Detail locators

- Sessions integration and Checkout API version, Customer Area setup and no extra `/sessions` fields: raw lines 25–40.
- Sessions optional visibility setting and illustrative Kotlin: raw lines 42–62.
- Advanced base flow, redirect handling and Customer Area setup: raw lines 74–82.
- Advanced optional visibility setting, illustrative Kotlin and no extra `/payments` fields: raw lines 84–110.
- TEST issuer/status advice and separate live request: raw lines 64–72 and 112–118.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-thailand]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-thailand/android-drop-in/2026-09-15|Online banking Thailand Android Drop-in guide — captured 2026-09-15]]
