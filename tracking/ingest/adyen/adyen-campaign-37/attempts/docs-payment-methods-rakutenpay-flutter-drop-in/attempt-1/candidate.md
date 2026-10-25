---
title: "Adyen Rakuten Pay Flutter Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/rakutenpay/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/rakutenpay/flutter-drop-in/2026-09-15.md"
tags: [adyen, rakutenpay, flutter, drop-in, recurring, japan]
---

## Overview

This [[adyen]] guide adds Rakuten Pay to an **existing Flutter Drop-in** Sessions or Advanced flow. It gives redirect and Customer Area prerequisites, method-specific request/configuration scope, a conditional recurring policy, and TEST simulator instructions. See [[adyen-online-payments]] and [[adyen-tokenization]]. It is a 2026-09-15 documentation snapshot, not proof of current merchant eligibility or a completed payment.

## Key takeaways

- **Sessions** requires an existing Flutter Drop-in Sessions flow, **Checkout API v68 or later**, redirect handling for `action.type: redirect`, and contacting Support to add Rakuten Pay in Customer Area. Its integration-type link is anomalous: it says Sessions but points to an **Advanced-flow** URL; the redirect and session-creation links point to Sessions. Use the stated Sessions requirement with this link discrepancy visible. The page says no extra Rakuten Pay `/sessions` parameters or configuration. See raw lines 25–48.
- **Advanced** requires an existing Flutter Drop-in Advanced flow, redirect handling and adding Rakuten Pay in Customer Area. It says no extra method-specific `/payments` parameters or configuration. The page does not state an Advanced Checkout API minimum or a full return/details/webhook result procedure. See raw lines 66–88.
- Both flow sections repeat a conditional **recurring** policy: for a business model based on subscriptions and unscheduled card-on-file payments, Rakuten Pay permits **one-off card-on-file transactions only after review**. Without a periodic charging cadence it prohibits initiating the card-on-file Recurring Processing Model, described as primarily allowed for Food & Beverage; merchants must apply for **every Recurring Processing Model** when requesting Rakuten Pay. The page links token creation separately and **strongly recommends** explicit shopper permission and transparent schedule/amount; it does not phrase that advice as an unconditional integration requirement. No token creation or future charge is proven by the link. See raw lines 50–56 and 90–96.
- For TEST, the page names acquirer account `DGFT_AcquirerAccount_RakutenPay_closedLoop`, a DGFT simulator redirect, and Customer Area test payment-list status checks; it says the Rakuten Pay app is unnecessary for that simulator path. The page provides no distinct live enablement procedure despite the “Test and go live” heading. Simulator completion and status lookup are not evidence of live authorization, capture or settlement. See raw lines 58–64 and 98–104.

## Detail locators

- **Sessions prerequisite/link mismatch, v68+, redirect and no-extra-fields/config:** raw lines 25–48.
- **Advanced prerequisite and no-extra-fields/config:** raw lines 66–88.
- **Recurring review, prohibition, per-model application and consent advice:** raw lines 50–56 and 90–96.
- **TEST account, simulator and status lookup:** raw lines 58–64 and 98–104.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-rakutenpay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/rakutenpay/flutter-drop-in/2026-09-15|Rakuten Pay Flutter Drop-in guide — captured 2026-09-15]]
