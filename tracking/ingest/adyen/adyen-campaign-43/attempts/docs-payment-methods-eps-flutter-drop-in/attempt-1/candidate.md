---
title: "Adyen EPS Flutter Drop-in"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/eps/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/eps/flutter-drop-in/2026-09-15.md"
tags: [adyen, eps, flutter, drop-in, redirect, recurring]
---

## Overview

This 2026-09-15 EPS Flutter Drop-in guide supplies method-specific additions to an existing Sessions or Advanced Flutter Drop-in integration. It requires redirect readiness and EPS setup, says the ordinary flow needs no EPS-specific request or configuration parameters, and describes future recurring payments through SEPA Direct Debit. It is not a standalone Flutter integration or evidence of current EPS enablement or payment success. See [[adyen]], [[adyen-online-payments]], [[adyen-tokenization]] and [[source-adyen-docs-payment-methods-eps|the EPS overview]].

## Key takeaways

- For Sessions, the page requires an existing Flutter Drop-in Sessions flow, Checkout API v68 or later, redirect handling for `action.type=redirect`, and contacting Adyen Support to add EPS in Customer Area. It says to add no EPS-specific `/sessions` parameters or Drop-in configuration. Its Sessions integration-type cell links to an Advanced-flow URL even though the row and redirect link say Sessions; follow the named flow and check the linked base integration before implementing.
- For Advanced, the page requires an existing Flutter Drop-in Advanced flow, redirect handling and EPS added in Customer Area. It says to add no EPS-specific Drop-in configuration or ordinary `/payments` parameters; the base guide owns general request construction and redirect handling. The Advanced setup row links to the add-payment-methods route, whereas the Sessions setup row directs the reader to Support. The capture does not resolve whether one setup path supersedes the other.
- EPS recurring is described through SEPA Direct Debit, not repeat EPS redirects. The guide strongly recommends explicit shopper permission and transparency about the schedule and amount. To create a token, send `storePaymentMethod=true` and a unique `shopperReference` of at least three characters in `/payments`. After settlement, a configured recurring-token lifecycle webhook delivers `recurring.token.created` with `storedPaymentMethodId` and an `eventId` equal to the initial payment's `pspReference`. Later `/payments` requests use `paymentMethod.storedPaymentMethodId`, the same shopper reference, `shopperInteraction=ContAuth`, and `recurringProcessingModel=Subscription` or `UnscheduledCardOnFile`. The token operations are server-side `/payments` steps even when the initial Drop-in checkout uses Sessions.
- Check test payment statuses in the test Customer Area. Before accepting live EPS, the guide requires a request in the live Customer Area. These setup and status instructions do not prove live entitlement, current coverage, settlement or recurring success.

## Detail locators

- Scope and Sessions prerequisites, including the mismatched Advanced-flow link in its Sessions integration-type cell: pinned raw lines 15–36. No added `/sessions` or Drop-in configuration fields: lines 38–48.
- Sessions SEPA recurring permission, token-creation fields, post-settlement webhook and later stored-token payment: pinned raw lines 50–89. Test/live Customer Area instructions: lines 91–95.
- Advanced prerequisites and add-payment-methods setup: pinned raw lines 97–107; no extra configuration or ordinary `/payments` parameters: lines 109–119. Repeated recurring detail: lines 121–160; repeated test/live gate: lines 162–166.

## Related

- [[adyen-online-payments]] — primary provider integration route
- [[adyen-tokenization]] — recurring stored-payment concepts
- [[source-adyen-docs-payment-methods-eps]] — method overview
- [[source-adyen-docs-payment-methods-eps-api-only]] — server API-only issuer details

## Raw Sources

- [[raw/adyen/docs/payment-methods/eps/flutter-drop-in/2026-09-15|EPS Flutter Drop-in guide, captured 2026-09-15]]
