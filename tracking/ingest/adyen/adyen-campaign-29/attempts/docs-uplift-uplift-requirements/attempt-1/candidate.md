---
title: "Adyen Uplift integration and data requirements"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/uplift/uplift-requirements"
raw_files:
  - "adyen/docs/uplift/uplift-requirements/2026-09-15.md"
tags: [adyen, uplift, online-payments, risk, tokenization, authentication]
---

## Overview

This 2026-09-15-captured [[adyen]] page (metadata last modified 2019-09-06) maps **general, module-specific and payment-request data requirements or recommendations** for [[adyen-uplift]]. It covers Web online-payment integrations and the Protect, Tokenize, Authenticate, Optimize and Personalize modules. These are conditions for using or improving Uplift, not evidence that a merchant's module is enabled or has improved results (raw lines 15–25, 39–41, 93–97).

## Key takeaways

- **General Web gate and versioned routes:** The page asks for a Web online-payments integration and enabled/accepted webhooks. It recommends Web Drop-in or Components v6 with Sessions or Advanced flow and Checkout API v71 or later; it also lists Web API-only with encrypted or raw card data on v71+ as supported. Raw-card Web API-only processing carries additional PCI requirements (raw lines 23–37). These are the captured page's version statements, not a current support matrix.
- **Module gates differ:** Protect requires Adyen's risk engine; premium settings and fraud-data collection are recommended. Tokenize requires Adyen tokenization; network-token products, Real Time Account Updater and token-lifecycle webhooks are recommended. Authenticate requires 3D Secure 2 and gives Sessions versus Advanced implementation paths, including native/redirect choices and Web API-only additional-action handling (raw lines 39–64). Its EEA/UK regulatory language is a dated provider description, not current legal advice.
- **Optimize and Personalize conditions:** Optimize requires co-badged-card support, with Web Drop-in/Components minimum v6.16.0 and recommended v6.18.1; Web API-only raw-card integrations use `/cardDetails`. Auto Rescue and more payment methods are recommendations. Personalize requires the listed v6 Web Drop-in/Components or Web API-only routes, shopper data including at least `shopperEmail`, and for Advanced flows a shopper-conversion identifier tying `/paymentMethods` to `/payments`; Components must retain the returned payment-method order (raw lines 65–91).
- **Do not confuse API validity with Uplift conditions:** The text distinguishes fields required for a payment request to work (`amount`, `reference`, and table entries `merchantAccount`/`returnUrl`) from shopper fields that are not needed for the request to work but are recommended or marked “must be included” for Uplift/module/flow purposes (raw lines 93–117). Conditional examples include partner `applicationInfo`, Advanced-flow `browserInfo`/`checkoutAttemptId`/`paymentMethod`, API-only Protect `riskData.clientData`, Tokenize recurring/storage fields and Personalize `shopperConversionId`. The table's blanket “must be included” wording for `shopperEmail` and `shopperIP` should be read with the preceding API-functionality qualification and Sessions auto-collection note, not generalized into an unconditional API schema rule (raw lines 95–117).
- **Additional context remains qualified:** The table lists optional/contextual `accountInfo`, billing address, country, birth date, line items, order reference, holder name, locale and phone. Enhanced Scheme Data is limited to qualifying US domestic transactions and card schemes (raw lines 118–128). More submitted data is framed as improving recommendations, not a guaranteed conversion, fraud or authentication outcome (raw lines 19, 93–97).

## Detail locators

- General integration/webhook/PCI prerequisites: raw lines 23–37.
- Per-module Protect, Tokenize, Authenticate, Optimize and Personalize gates: raw lines 39–91.
- Payment-request versus Uplift data distinction and field-by-flow table: raw lines 93–128.

## Evidence boundary

This is a captured provider requirements/recommendations page with older modification metadata. It cannot establish a merchant's live module activation, PCI or regulatory compliance, payment authorization, or measured uplift. Preserve the difference between **required**, **recommended**, and flow-conditional fields; the page's own shopper-field prose and table use different senses of “must” (raw lines 93–117). Current product eligibility or legal obligations need fresh provider and appropriate legal review.

## Related

- [[adyen-uplift]] — five-module product route.
- [[adyen-online-payments]] — underlying Web integration.
- [[adyen-risk-management]] — Protect risk context.

## Raw Sources

- [[raw/adyen/docs/uplift/uplift-requirements/2026-09-15|Pinned Uplift requirements page, captured 2026-09-15]]
