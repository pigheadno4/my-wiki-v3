---
title: "Adyen Docs: Two-step checkout"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/two-step-checkout"
raw_files:
  - "adyen/docs/online-payments/two-step-checkout/2026-09-15.md"
tags: [adyen, online-payments, two-step-checkout, web, advanced-flow]
---

## Overview

This Adyen Docs page describes a two-step checkout for Web Drop-in or Components using the Advanced flow: after the shopper supplies payment details, the merchant sends them to an additional review page and makes the `/payments` request only when they select **Pay** there. The review page is a pre-payment user-interface step, not evidence that a payment has already been submitted, authorized, captured, or completed. See [[adyen]] and [[adyen-online-payments]].

This unversioned page documents a merchant-built Advanced-flow pattern. [[adyen-review-page-checkout]] separately covers the version-qualified SDK `onReview` lifecycle, including Sessions submission through `processPayment`; the two mechanisms and their payment-method support must not be treated as equivalent.

The captured guide requires an Advanced-flow integration and a Checkout webservice role. It is an unversioned webpage snapshot, not proof of current payment-method support, merchant eligibility, account configuration, or successful execution.

## Key takeaways

- The checkout page hides the default Pay button with `showPayButton: false`, validates the shopper's input through a custom control, stores the selected Drop-in or Component payment data on the merchant server, and redirects the shopper to the review page. The raw includes separate stored-data expressions for Drop-in and Components and an `onEnterKeyPressed` example.
- Stored payment data expires after one hour. A later `/payments` request fails, and the shopper must restart checkout from the beginning.
- On the review page, selecting **Pay** triggers `/payments` with the stored data. Response handling must distinguish a response with an `action`, which requires additional front-end actions, from one without an `action`, for which the integration handles the final state; both routes then obtain the payment outcome through the integration.
- Creating the review-page checkout instance has a version/import qualification: only Web Drop-in v6 or later imported with individual payment methods requires registering the methods used in Drop-in.
- For cards, optional `onBrand` and `onFieldValid` events can provide the detected brand and last four digits for review-page display. Event details and examples remain at the raw locator below.

## Detail locators

- `## Requirements`, lines 21–29 — Advanced-flow Web Drop-in/Components prerequisite and Checkout webservice credential role.
- `## How it works`, lines 30–35 — four-step checkout-to-review-to-`/payments` sequence.
- `## Modify your checkout page`, lines 37–113 — `showPayButton`, custom validation, Drop-in/Component data selection, one-hour expiry, redirect, and Enter-key callback.
- `## Implement a review page`, lines 115–146 — checkout creation, conditional v6 method registration, `/payments`, and response handling with or without `action`.
- `## Show additional information for cards`, lines 148–157 — optional card-brand and last-four-digit events.

## Related

- [[adyen]] — provider page.
- [[adyen-online-payments]] — provider-level online-payments architecture and source routes.
- [[adyen-review-page-checkout]] — separately version-qualified SDK `onReview` and Sessions lifecycle; not an assertion that it is equivalent to this manual Advanced-flow pattern.
- [[source-adyen-docs-online-payments-web-best-practices]] — separate Web guidance, including payment-method-specific custom-button restrictions not stated on this two-step-checkout page.

## Raw Sources

- [[raw/adyen/docs/online-payments/two-step-checkout/2026-09-15|Adyen Docs — Two-step checkout (2026-09-15 snapshot)]]
