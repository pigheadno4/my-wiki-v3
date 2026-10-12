---
title: "Adyen Docs: Testing tokenization"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/testing/tokenization"
raw_files:
  - "adyen/docs/development-resources/testing/tokenization/2026-09-15.md"
tags: [adyen, tokenization, testing, stored-payment-methods, recurring-payments]
---

## Overview

This 2026-09-15 collected [[adyen|Adyen]] webpage is a pre-live test walkthrough for [[adyen-tokenization|Adyen tokenization]]. Using Adyen test card numbers, it routes an integration through storing and reusing payment details for one-off CardOnFile payments, optionally doing the same for Subscription payments, updating and removing stored details, and optionally exercising Real Time Account Updater scenarios.

The page is test guidance, not proof of current production availability, merchant or shopper eligibility, PCI compliance, webhook delivery, token creation, payment authorization, account updating, deletion, settlement, or funding.

## Key takeaways

- For the documented one-off test path, the guide creates a token with a zero-value authorization using `shopperInteraction: Ecommerce` and `recurringProcessingModel: CardOnFile`, then receives `recurring.token.created` and retains both the token and shopper reference. The reuse step changes `shopperInteraction` to `ContAuth`, keeps `CardOnFile`, and routes payment status through the server-side `AUTHORISATION` webhook.
- The optional subscription path similarly uses a zero-value authorization with `Ecommerce` and `Subscription`, followed by `recurring.token.created`; its later test-payment parameters are `ContAuth` and `Subscription`. However, the Step 4 heading and introduction call this a subscription payment while the numbered instruction says to make a "test one-off payment." This snapshot does not resolve that wording conflict, so do not silently generalize it into a production recurring-payment rule.
- The guide then routes token update and deletion tests to the stored-payment-details management documentation. Those navigation targets, rather than this short page, carry the detailed request contracts and lifecycle qualifications.
- Optional Real Time Account Updater fixtures return the simulated outcome in `additionalData.realtimeAccountUpdaterStatus`. The listed cards and statuses are test inputs, not evidence that a real account was updated.
- The page says integrations unable to process raw card data because they are not fully PCI compliant should prefix the documented test credentials with `test_` and use the encrypted-card-details testing route. This testing convention does not establish PCI compliance or authorize production raw-card handling.

## Detail locators

- **Purpose and scenario sequence** — tokenization test scope, test-card route, store/use/update/remove sequence, and optional Real Time Account Updater testing: raw lines 15-30.
- **Store one-off details** — zero-value authorization, `Ecommerce`, `CardOnFile`, token-created webhook, and token/shopper-reference retention: raw lines 32-45.
- **Reuse one-off details** — `ContAuth`, `CardOnFile`, and server-side `AUTHORISATION` webhook: raw lines 47-58.
- **Store subscription details** — optional scope, zero-value authorization, `Ecommerce`, `Subscription`, token-created webhook, and retained identifiers: raw lines 60-73.
- **Test a subscription payment** — `ContAuth` and `Subscription`, authorization webhook, and the internal "one-off payment" wording conflict: raw lines 75-86.
- **Update and remove details** — links to the separate stored-details update, lookup, and deletion procedures: raw lines 88-97.
- **Real Time Account Updater and PCI boundary** — fixture statuses, response field, test card values, and encrypted-test-credential prefix guidance: raw lines 99-110.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-tokenization]]
- Testing concept: [[adyen-payment-testing]]
- Cross-cutting concept: [[recurring-payments]]

## Raw Sources

- [[raw/adyen/docs/development-resources/testing/tokenization/2026-09-15|Adyen Docs — Testing tokenization (2026-09-15)]]
