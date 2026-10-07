---
title: "Braintree UnionPay Client-Side Implementation for Android v5"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/unionpay/client-side/android/v5"
raw_files:
  - "braintree/docs/guides/unionpay/client-side/android/v5-2026-09-16.md"
tags: [braintree, unionpay, android, client-sdk, enrollment, tokenization]
---

## Overview

This 2026-09-16 snapshot of a [[braintree]] Android v5-routed client-side guide documents checking a UnionPay card's capabilities, enrolling the card and, when required, collecting an SMS authorization code before tokenization through [[braintree-android-sdk]]. It is snapshot guidance, not evidence of current SDK support, merchant or card eligibility, enrollment success, server transaction completion, or payment execution.

## Key takeaways

- For a business outside China, the page says checkout must let the customer select the processing brand for a dual-branded UnionPay card. It directs the merchant to use the UnionPay network only when the customer chooses it; otherwise the other card-brand network is used.
- The page says this UnionPay path supports authorization only through a client token. It directs the client to check card capabilities after card-number entry so the form can respond to whether the card is credit or debit. Credit cards require CVV and expiration date and support immediate or delayed settlement; debit cards do not always require those fields and support only immediate settlement. These server-processing descriptions are not proof of a particular transaction outcome.
- A UnionPay card must be enrolled before tokenization. Enrollment may cause UnionPay to send an SMS authorization code, which the integration collects and supplies with the enrollment ID during tokenization; when enrollment says no SMS code is required, tokenization can proceed immediately.

> [!warning] Post-enrollment and validation conditions
> Once enrollment is completed, the page says the card number and expiration fields can no longer be updated. It also says UnionPay validation occurs during enrollment, so the `validate` property should not be passed during tokenization; enabled AVS and CVV rules are ignored because enrollment handles card validation.

> [!warning] Snapshot scope
> Although the URL and slug route this page as Android v5, the collected raw does not state a dependency version, runtime/environment prerequisite, or mobile-certificate condition. Do not import such conditions from sibling guides or treat this page as proof of current package compatibility, environment readiness, certificate state, enrollment eligibility, or payment success.

## Detail locators

- Dual-branded card-network selection for businesses outside China: `## Checkout form > ### Dual-branded cards`, raw lines 20-31.
- Credit/debit form fields and settlement distinctions: `## Checkout form > ### Card capabilities`, raw lines 34-49.
- Client-token-only authorization and card-capability check timing: `## Check card capabilities`, raw lines 57-62.
- Enrollment, conditional SMS collection, enrollment ID, post-enrollment field immutability and omitted `validate` property: `## Enrollment and tokenization`, raw lines 65-84.
- AVS/CVV rule behavior: `## Special considerations > ### AVS and CVV validation does not apply`, raw lines 89-96.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-android-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/unionpay/client-side/android/v5-2026-09-16|Braintree UnionPay client-side implementation (Android v5)]] - complete collected snapshot for checkout brand selection, card-capability checks, enrollment, conditional SMS authorization and tokenization conditions
