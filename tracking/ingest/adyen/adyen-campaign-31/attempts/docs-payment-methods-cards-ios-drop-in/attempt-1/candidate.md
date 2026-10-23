---
title: "Adyen iOS Card Drop-in integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/cards/ios-drop-in/2026-09-15.md"
tags: [adyen, cards, ios, drop-in, online-payments]
---

## Overview

Adyen guide for adding cards to an existing iOS Drop-in integration. It branches by Sessions versus Advanced server-side flow and iOS Drop-in version. Both flow tabs require the corresponding iOS Drop-in integration and adding cards in Customer Area before starting. The guide says cards need no additional card-specific API fields for the basic integration; optional/use-case fields have separate conditions. This is a 2026-09-15 webpage snapshot, not evidence of present merchant enablement or a successful payment.

## Key takeaways

- Sessions is the default path described for Drop-in v5.0.0 or later; the Advanced section calls itself the default for Drop-in v4.10.0 and earlier. The configuration tables separately name v4.10.3 or earlier. Do not merge those version statements into a new cutoff (raw lines 39–95, 847–849).
- Optional card fields cover cardholder name, security code visibility, allowed card types, billing address and market-specific fields. Separate debit and credit forms use server-sent `splitCardFundingSources: true` on Sessions `/sessions` or Advanced `/paymentMethods` (the latter says Checkout API v53+). The Netherlands amount is an example; Sweden ordering, co-badged selection and combo-card advice have their own qualifications (raw lines 65–205).
- Card tokenization is presented for one-click, subscription and unscheduled card-on-file use. The page strongly recommends explicit shopper permission for future recurring charges. Sessions token examples use `/sessions` and API/library versions and show `askForConsent` in curl/Node/Go but `enabled` in other library samples; these examples do not establish one universal consent setting. Advanced creation uses `/payments` and refers to `recurring.token.created` for the stored payment method ID (raw lines 207–540, 847–1259).
- The Advanced text says `showsStorePaymentMethodField` must be true to show a storage checkbox, while its immediately following Swift sample sets it to false. Treat that sample as contradictory, not a verified checkbox implementation. The Checkout API v69-or-earlier Sessions note instead names `enableStoreDetails` (raw lines 536–540, 851–864).
- The sections labelled “one-click” show `shopperInteraction: ContAuth` in their request examples; preserve that exact example without assuming it settles shopper-present versus shopper-not-present semantics. Subscription and unscheduled examples also use `ContAuth` with their respective `recurringProcessingModel`. Token creation/reuse, 3D Secure, authorization, capture and settlement are distinct events; no example proves any outcome (raw lines 542–846, 1261–2325).
- Live-card prerequisites in this guide include test-card testing, adding desired cards in the live Customer Area, assessing PCI DSS compliance, and submitting the required SAQ A. Its `test_` encrypted-card values and checkout-test URLs are test illustrations, not live credentials or a PCI determination (raw lines 2388–2398).

## Detail locators

- Requirements, API endpoints and v5/v4 card configuration: raw lines 21–95.
- Debit/credit separation, Sweden, combo/co-badged cards: raw lines 97–205.
- Sessions token creation and reuse with illustrative, versioned language samples: raw lines 207–846.
- Advanced token creation, stored-payment-method webhook and one-click/subscription/unscheduled examples: raw lines 847–2325.
- v5 Sessions versus v4 client-side installment options: raw lines 2326–2387.
- Test and go-live checklist: raw lines 2388–2398.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-3d-secure]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/ios-drop-in/2026-09-15|Adyen iOS Card Drop-in integration snapshot]]
