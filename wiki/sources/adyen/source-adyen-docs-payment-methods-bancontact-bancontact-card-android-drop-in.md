---
title: "Adyen Bancontact card Android Drop-in"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-card/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-card/android-drop-in/2026-09-15.md"
tags: [adyen, bancontact, card, android, drop-in, tokenization]
---

## Overview

Adyen's Bancontact card guide explains adding the card method to an existing Android Drop-in integration, in either Sessions or Advanced flow, with a minimum Drop-in version of 5.0.0. It points earlier versions to a separate guide. This is Bancontact *card* guidance, not the Bancontact mobile app or QR route. See [[adyen]] and [[adyen-android-sdk]].

## Key takeaways

- Both Sessions and Advanced flows require Android Drop-in v5.0.0 or later and Bancontact card enabled in Customer Area. For a base Bancontact card payment, the page requires no additional method-specific fields in `/sessions` or `/payments`, and no extra Drop-in configuration. The Sessions flow creates a checkout session; Advanced launches and shows Drop-in after configuration. These statements do not remove the parent flow's usual request requirements (raw lines 21-67).
- Recurring use is a separate, conditional Bancontact Wallet Initiated Program (WIP) path. The page recommends explicit shopper permission. WIP requires signup, is not available to every company, needs Support enablement and has transaction amount limits. The page describes first-transaction consent and SCA followed by later transactions without SCA, with an issuer-liability statement; treat these as WIP-scoped source claims rather than general or current guarantees (raw lines 69-88).
- For WIP token creation, send `storePaymentMethod: true` and a unique `shopperReference` of at least three characters in `/sessions` or `/payments`. After the initial payment has settled, the `recurring.token.created` lifecycle webhook provides `storedPaymentMethodId`; the server must receive those events. A later `/payments` request uses the stored ID, the same shopper reference, `ContAuth`, and `Subscription` or `UnscheduledCardOnFile`. Support configures the test environment for recurring tests. These tokenization fields are conditional additions, not a contradiction of the base payment's no-additional-fields statement (raw lines 90-124).
- The page supplies TEST co-badged BCMC/Mastercard Debit, BCMC/Maestro and BCMC/Visa Debit cards. The Visa fixture may route to Bancontact or Visa depending on payment-method setup, and a `holderName: "DECLINED"` fixture forces refusal. Bancontact card must be added separately in live Customer Area. Fixtures and captured instructions do not prove current eligibility or a live payment result (raw lines 465-498).

## Detail locators

- Version, flow prerequisites, base API and Drop-in configuration: raw lines 15-67.
- WIP eligibility, consent, SCA and amount-limit qualifications: raw lines 69-88.
- Token creation, after-settlement webhook and later recurring request: raw lines 90-124; language examples continue through line 463.
- Co-badged TEST cards, routing caveat, forced decline and live setup: raw lines 465-498.

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-card/android-drop-in/2026-09-15|Bancontact card Android Drop-in guide (2026-09-15 capture)]]
