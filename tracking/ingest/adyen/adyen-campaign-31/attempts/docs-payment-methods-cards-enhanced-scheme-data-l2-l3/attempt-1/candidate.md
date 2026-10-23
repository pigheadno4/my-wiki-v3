---
title: "Adyen Level 2/3 enhanced scheme data for card payments"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/l2-l3"
raw_files:
  - "adyen/docs/payment-methods/cards/enhanced-scheme-data/l2-l3/2026-09-15.md"
tags: [adyen, cards, enhanced-scheme-data, level-2, level-3]
---

## Overview

This [[adyen]] page describes sending Level 2/3 enhanced scheme data (ESD) for eligible **US Mastercard and Visa** card payments or captures. Level 2 contains purchase and tax details; Level 3 adds line-item details. The page says eligible Mastercard/Visa transactions may benefit from lower interchange rates, while American Express has no financial incentive here but may receive the data for fraud prevention and reporting. Eligibility and rate benefit are conditional, not established by the presence of fields or a sample response. [[adyen-online-payments]]

## Key takeaways

- The guide inherits ESD eligibility and general requirements from its parent guide. Its additional limitations say that **from April 1, 2026**, Visa supports Level 3 only and Mastercard supports Levels 2 and 3; the eligible card types are business, purchasing, and corporate cards, with most business cards limited to Level 2. The Level 2 minimum total tax amount is 0.1%; the maximum is 30% for Mastercard and 22% for Visa. These are the page's dated rules, not independently verified current scheme rules. See raw lines 17–44.
- ESD goes in a payment request for automatic or delayed automatic capture, and in a capture request for manual single or multiple partial capture. The top-level flow names `enhancedSchemeData.levelTwoThree` for `/payments` and `enhancedSchemeData` for captures, but the later field instructions and examples instead put payment ESD under `additionalData.enhancedSchemeData` and capture ESD under `enhancedSchemeData.levelTwoThree`. This is a material **within-page field-path conflict**; use the applicable API/version reference before implementation. See raw lines 46–64, 116–121, and 152–280.
- Validation requires correct format and accurate data; Visa amount calculations must reconcile line totals with quantities, unit prices, discounts, freight, taxes, and capture total. The page says to send ESD in the capture request if payment and capture totals differ. Missing or malformed required fields can cause Adyen to drop all ESD; Level 3-only errors or a Level 2-only card can lead to Level 2 submission; malformed optional fields can be dropped. These are **data-submission** outcomes, not payment authorization, capture, or settlement outcomes. See raw lines 66–90.
- The field table distinguishes required Level 2/3 customer reference and tax amount, required Level 3 line-item details, and shipping/destination fields mandatory only when **all** of these hold: corporate card, US acquisition, and shipped goods. Keep the payment-versus-capture field names distinct. See raw lines 116–149.
- ESD validation feedback is optional and requires webhook configuration; AUTHORISATION feedback for automatic capture or ESD sent in the payment request additionally calls for Support enablement. The page distinguishes `enhancedSchemeDataReceived`, `enhancedSchemeDataSubmitted`, refusal reasons, and warning reasons. It maps automatic capture to AUTHORISATION and manual or delayed automatic capture to CAPTURE, but the later instruction says AUTHORISATION may apply when ESD was sent in the payment request. Feedback shows what ESD Adyen submitted to a scheme after validation; it does not prove a favorable interchange rate or a settled payment. See raw lines 48–64 and 92–114, 284–370.
- The generalized Level 3-error fallback to Level 2 and the examples mentioning submission to “Visa or Mastercard” are not reconciled with the page's **April 2026 Visa Level 3-only** rule. The webhook field table lists `null` among values, whereas the ineligible and invalid examples use empty strings; the monitoring prose uses singular `enhancedSchemeDataRefusalReason`/`enhancedSchemeDataWarningReason` while the table and examples use plural `...Reasons`. Preserve these inconsistencies rather than treating example payloads as a complete schema. See raw lines 32–39, 76–78, 105–114, 284–370.

## Detail locators

- Level 2/3 validation and Visa calculation formulas: raw lines 66–90.
- Complete payment/capture field comparison, including conditional shipping destination fields: raw lines 116–149.
- Illustrative v72 TEST requests/responses: raw lines 152–280. The payment example includes raw test card number and CVC and an `Authorised` response; it is not a safe live card-data-handling pattern or evidence of an actual payment. Both shell samples show `-X POST` without a joining backslash before `-d`, and the capture example's line-item object name differs from the field table; these examples need validation against the applicable API reference.
- Example webhook payloads for valid L3, valid L2, downgraded L3, ineligible card, and invalid ESD: raw lines 284–370. Test card numbers are at raw lines 372–379.

## Related

- [[adyen-online-payments]]
- [[adyen-payment-capture]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/enhanced-scheme-data/l2-l3/2026-09-15|Adyen Level 2/3 ESD snapshot]]
