---
title: "Adyen EPS Web Drop-in"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/eps/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/eps/web-drop-in/2026-09-15.md"
tags: [adyen, eps, web, drop-in, redirect, recurring]
---

## Overview

Adyen's EPS Web Drop-in guide covers EPS-specific additions to an existing Sessions or Advanced Web Drop-in integration. Both flows require EPS enabled in Customer Area and handling a `redirect` action. The guide is an add-on to the parent Web Drop-in flow, not a complete payment-outcome or bank-selection procedure. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Sessions flow specifically requires Checkout API v68 or later, an existing Web Drop-in integration, and redirect handling. Advanced flow requires its existing Web Drop-in integration and redirect handling; this page does not repeat the v68 minimum in its Advanced requirements. Both require EPS added in Customer Area. The Advanced integration-type link contains an encoded template placeholder for `platform`, while its redirect link specifies Web; use the parent flow guide carefully rather than treating the placeholder URL as a valid resolved Web guide (raw lines 25-36, 105-115).
- For the ordinary EPS payment, no additional parameters are needed in Sessions `/sessions` or Advanced `/payments`. Importing `EPS` from `@adyen/adyen-web` is optional for tree shaking, not a required Drop-in setup step. The parent's normal request and redirect flow still apply (raw lines 38-54, 117-133).
- EPS recurring is via **SEPA Direct Debit**, not a claim that the initial EPS bank redirect repeats. The page recommends explicit permission for future SEPA payments and transparent schedule/amount to reduce chargeback risk. For token creation it instructs adding `storePaymentMethod: true` and a unique `shopperReference` of at least three characters in a `/payments` request—even under the Sessions section—so do not merge this conditional token route with the no-extra-fields ordinary `/sessions` statement (raw lines 56-74, 135-153).
- Once the initial payment has settled, a `recurring.token.created` webhook supplies `storedPaymentMethodId`; the server must receive recurring-token lifecycle events. Future `/payments` use the stored ID, same shopper reference, `ContAuth`, and `Subscription` or `UnscheduledCardOnFile`. A redirect action alone is not a settled payment or an available token (raw lines 74-95, 153-174).
- Test EPS payment status is checked in test Customer Area. Live acceptance requires submitting an EPS request in live Customer Area; the captured guide and setup instructions do not establish current eligibility or a successful live payment (raw lines 97-103, 176-182).

## Detail locators

- Sessions prerequisites, no extra request parameters, optional import: raw lines 25-54.
- Sessions recurring/SEPA token lifecycle and live gate: raw lines 56-103.
- Advanced prerequisites, encoded integration-link placeholder, no extra request parameters, optional import: raw lines 105-133.
- Advanced recurring/SEPA token lifecycle and live gate: raw lines 135-182.

## Raw Sources

- [[raw/adyen/docs/payment-methods/eps/web-drop-in/2026-09-15|EPS Web Drop-in guide (2026-09-15 capture)]]
