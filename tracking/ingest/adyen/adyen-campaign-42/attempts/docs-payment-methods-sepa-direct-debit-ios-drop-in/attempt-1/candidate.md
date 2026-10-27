---
title: "Adyen SEPA Direct Debit iOS Drop-in"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/sepa-direct-debit/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/sepa-direct-debit/ios-drop-in/2026-09-15.md"
tags: [adyen, sepa-direct-debit, ios, drop-in, sessions, advanced-flow, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds SEPA Direct Debit to an existing iOS Drop-in integration using either the Sessions or Advanced server-side flow. It gives method-specific additions, not a complete native integration, current merchant eligibility, mandate validity or proof of a settled debit. See [[adyen]], [[adyen-online-payments]], [[adyen-tokenization]] and the method overview [[source-adyen-docs-payment-methods-sepa-direct-debit]] for mandate, pre-debit notification, chargeback and refund conditions.

## Key takeaways

- Sessions requires an existing iOS Drop-in Sessions integration, Checkout API v68 or later, and SEPA Direct Debit added in Customer Area. The ordinary `/sessions` payment needs no additional method-specific request parameters or Drop-in configuration. The guide's separate token-creation example is not an exception to those ordinary-payment instructions.
- Advanced requires an existing iOS Drop-in Advanced integration, SEPA setup in Customer Area, and handling for the documented additional `action.type: direct` action. It says no extra Drop-in configuration is needed. Its `/payments` fields require account-holder name and IBAN, which the guide says not to encrypt; billing address is conditional on the IBAN being from its listed non-EEA SEPA countries or territories. The v72 request example is a test-environment sample; its `resultCode: Received` response is not evidence that funds have cleared. The displayed curl sample lacks a line continuation after `-X POST`, so copy it with care rather than assuming it executes as printed.
- If automatic capture is not used, the guide instructs delayed automatic or manual capture. It says SEPA authorizations do not expire and that multiple partial capture requires Support enablement. Capture instructions do not waive the mandate and advance-notice duties in the method overview.
- Both flows describe SEPA tokenization for Subscription and UnscheduledCardOnFile. Adyen strongly recommends explicit shopper permission for future recurring use; the separate method-level mandate acceptance is a requirement. Token creation is reported by `recurring.token.created` with `storedPaymentMethodId`; later shopper-absent payments use `/payments` with stored method, shopper reference, `shopperInteraction: ContAuth` and the selected recurring model. A Sessions integration also uses `/payments` for these later charges. Examples do not prove a token was created or a payment succeeded.
- The guide provides sample test names/IBANs and a test Customer Area status route. Live SEPA Direct Debit acceptance needs a request submitted in the live Customer Area. The source does not establish that a particular merchant is approved.

## Detail locators

- Sessions prerequisite and no-extra-request/configuration statements: pinned raw lines 25–46.
- Sessions token scope, permission advice, v71 `/sessions` token-creation example and later webhook/`/payments` boundary: pinned raw lines 48–80, 257–289; UnscheduledCardOnFile sample: lines 570–598.
- Advanced prerequisites, `direct` action, configuration, required name/IBAN, conditional billing address and unencrypted IBAN instruction: pinned raw lines 893–923. The v72 sample and `Received` response are at lines 925–957, including the missing shell line continuation at lines 932–933.
- Capture choices, no-expiry statement and multiple-partial-capture enablement: pinned raw lines 959–968. Advanced token lifecycle and stored-method reuse: lines 970–980 and 1329–1361; unscheduled sample: lines 1640–1668.
- Test data and live request: pinned raw lines 877–891 and 1947–1961. Mandate and pre-debit-notice requirements: [[source-adyen-docs-payment-methods-sepa-direct-debit]].

## Related

- [[adyen-online-payments]] — main integration concept
- [[adyen-tokenization]] — recurring-token concept
- [[source-adyen-docs-payment-methods-sepa-direct-debit]] — method-level mandate and funds-risk authority

## Raw Sources

- [[raw/adyen/docs/payment-methods/sepa-direct-debit/ios-drop-in/2026-09-15|SEPA Direct Debit iOS Drop-in, 2026-09-15]]
