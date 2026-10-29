---
title: "Afterpay Flutter Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/afterpaytouch/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/afterpaytouch/flutter-drop-in/2026-09-15.md"
tags: [adyen, afterpay, flutter, drop-in, redirect, capture]
---

## Overview

This 2026-09-15-captured [[adyen]] guide adds Afterpay to an **existing Flutter Drop-in integration**, with separate Sessions and Advanced server-flow sections. It supplies method-specific additions, not a full base integration or proof of merchant enablement. The related [[source-adyen-docs-payment-methods-afterpaytouch]] overview gives the AU/CA/NZ Afterpay product scope; AUD/AU examples and a US sandbox-account option here do not establish wider live eligibility. See [[adyen-online-payments]].

## Key takeaways

- **Sessions prerequisites and source mismatch:** The Sessions section calls for an existing Flutter Drop-in Sessions flow, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and contacting Support to add Afterpay in Customer Area (raw lines 25–36). Its “Flutter Drop-in integration” prerequisite text links to an **Advanced** base guide (`advanced-flow?platform=Flutter&integration=Drop-in`) even though the section says Sessions (raw line 33). The redirect and create-session links point to Sessions. Choose the actual Sessions base flow rather than treating the mismatched prerequisite link as authority.
- **Sessions request:** The `/sessions` table marks `shopperName`, `shopperEmail`, `shopperReference` (minimum three characters), `countryCode`, `billingAddress`, `deliveryAddress` and `lineItems` required; `telephoneNumber` is optional if provided (raw lines 38–53). The AUD/AU TEST curl and API-library examples are sample request shapes, not live product or SDK guarantees (raw lines 55–737).
- **Advanced prerequisites and request:** The Advanced section calls for an existing Advanced Flutter Drop-in integration, redirect handling and adding Afterpay in Customer Area (raw lines 789–799). This setup wording differs from the Sessions section's **contact Support** instruction; neither text proves the method is already enabled. Its `/payments` table requires `paymentMethod: afterpaytouch` plus the same required shopper, country, address and line-item fields, with telephone optional (raw lines 807–823). The response example's `RedirectShopper`/`action.type: redirect` is a redirect step, not a final payment outcome (raw lines 1538–1552).
- **Drop-in configuration:** Both sections say no additional Afterpay-specific configuration parameters are needed (raw lines 739–743, 801–805). This does not remove the existing Drop-in, redirect or server-flow prerequisites.
- **Capture deadline and first installment:** Capture is automatic after authorisation or manual, depending on merchant-account configuration. Capture delay or manual capture is needed to capture after shipping, and partial capture requires **manual** capture (raw lines 747–749, 1554–1556). The guide says Afterpay payment capture must occur within **13 days** of authorisation. It says the first installment is charged during authorisation; if not captured by the deadline, Afterpay cancels and refunds it. In TEST, authorisations expire in **one day** and manual test capture must occur within that day (raw lines 751–755, 1558–1562).
- **Partial capture:** Manual `/payments/{paymentPspReference}/captures` requests specify full or partial `amount.value`; `lineItems` is optional. A partial capture normally cancels the unclaimed balance. When an account is enabled for **multiple partial captures**, the balance remains; setup requires contacting Support and each capture creates a new invoice (raw lines 757–766, 1564–1573). This page does not provide a refund procedure.
- **Test/live route:** Testing requires an Afterpay sandbox shopper account and test card; separate accounts are called for when testing multiple countries or regions (raw lines 768–785, 1575–1592). The sandbox selector includes US, while the linked overview's product table lists AU/CA/NZ; sandbox choice alone does not prove live US availability. Before live acceptance, the page instructs merchants to submit an Afterpay request in live Customer Area (raw lines 787, 1594). These are documentation steps, not evidence of approval or a completed live payment.

## Detail locators

- Sessions prerequisites, mismatched base-flow URL, Support gate and request table: pinned raw lines 25–53.
- Sessions TEST curl/API-library examples: pinned raw lines 55–737.
- Sessions configuration, capture and test/live sections: pinned raw lines 739–787.
- Advanced prerequisites, configuration and `/payments` field table: pinned raw lines 789–823.
- Advanced TEST examples and redirect response: pinned raw lines 825–1552.
- Advanced capture, multiple-partial Support gate and test/live instructions: pinned raw lines 1554–1594.

## Related

- [[adyen-online-payments]] — provider online checkout context.
- [[source-adyen-docs-payment-methods-afterpaytouch]] — Afterpay method and region overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/afterpaytouch/flutter-drop-in/2026-09-15|Afterpay Flutter Drop-in guide, captured 2026-09-15]]
