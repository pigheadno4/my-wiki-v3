---
title: "Adyen Issuing: Manage cards"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/manage-cards"
raw_files:
  - "adyen/docs/issuing/manage-cards/2026-09-15.md"
tags: [adyen, issuing, cards, payment-instruments, lifecycle]
---

## Overview

This captured Adyen Issuing guide describes managing a card's `paymentInstrument` after creation: changing its linked balance account, activating or suspending payment processing, permanently closing it, and viewing its payments in Customer Area. The raw page was captured 2026-09-15 and marked last modified 2019-12-18; the API and SDK snippets are examples, not evidence that a card exists or a live status transition or payment succeeded. See [[adyen-issuing]].

## Key takeaways

- The linked `balanceAccountId` can be changed only while the card is `inactive`, using a Balance Platform `PATCH /paymentInstruments/{id}` request; the response contains the `paymentInstrument` with its updated `balanceAccountId` (raw lines 27–31, 223).
- Activation is available in Customer Area or through that PATCH endpoint with `status: active`. Adyen recommends keeping physical cards inactive until the user receives them. An activated card can start processing payments; this does not assert any particular payment was authorized or settled (raw lines 225–244, 436).
- Suspension temporarily prevents payment processing and can be reversed by setting the card back to `active`; closing is permanent and cannot be reversed. Customer Area offers both status changes. In the API, suspension uses `status: suspended` plus a `statusReason` from `lost`, `stolen`, `damaged`, `suspectedFraud`, or `other`; `statusComment` is required when the reason is `other` (raw lines 438–463, 664). Closing uses `status: closed` and a reason from `lost`, `stolen`, `damaged`, `suspectedFraud`, `endOfLife`, or `accountClosure` (raw lines 666–689).
- Customer Area's **View payments** displays payments made with the card and defaults to the last six months (raw lines 894–903). This is a viewing instruction, not proof of transaction outcomes.

## Detail locators

- `Update the balance account linked to a card` (raw lines 27–223): inactive-only condition, endpoint, response, and test/SDK examples.
- `Activate a card` (raw lines 225–436): Customer Area and API steps, plus sample client-library versions.
- `Suspend a card` (raw lines 438–664): reversible status, required reason and conditional comment, Customer Area and API steps.
- `Close a card` (raw lines 666–892): irreversible status, permitted API reasons, Customer Area and API steps.
- `View card payments` (raw lines 894–903): Customer Area path and default six-month filter.

## Related

- [[adyen]] — provider context.
- [[adyen-issuing]] — Issuing concept.
- [[source-adyen-docs-issuing-get-started]] — initial setup and separate live-account transition.

## Raw Sources

- [[raw/adyen/docs/issuing/manage-cards/2026-09-15|Adyen Issuing manage cards, captured 2026-09-15]]
