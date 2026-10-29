---
title: "Adyen co-badged Bancontact card processing issues"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-card/co-branded-cards"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-card/co-branded-cards/2026-09-15.md"
tags: [adyen, bancontact, card, co-badged, routing, web, version]
---

## Overview

Adyen's page, last modified in December 2022 and captured on 2026-09-15, diagnoses issues reported with new Bancontact/Visa Debit co-badged cards in some older integrations. Its historical 2021 circulation counts and 2022 forecast are period-specific, not current card-volume evidence. The affected path is **Bancontact card** with 3D Secure, not generic credit/debit processing or Payconiq by Bancontact (Bancontact mobile). See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The page says some shoppers using older Classic SDK, Drop-in or Components integrations may be unable to enter co-badged card details, seeing an “invalid card” front-end error before a payment starts; merchant and Adyen would not see that attempted payment. Another issue is missing shopper scheme choice, with a default scheme selected. These are distinct failure modes, not a general payment refusal diagnosis (raw lines 25-50).
- API-only and Classic API integrations *may* have the issue and should check with the special TEST card. Classic HPP, Pay by Link and in-person routes had no issues observed by the page's authors. These are source-period observations, not a current blanket guarantee (raw lines 52-70, 88-94).
- Web Drop-in and Web Components **below 4.2.0** *may* be affected. The page recommends upgrading to the then-latest Web version and corresponding Checkout API version. It reports no observed issue with newer Web versions or iOS/Android Drop-in and Components; this is not proof that all modern versions or merchant configurations work (raw lines 72-86).
- Use the provided Bancontact/Visa Debit co-badged card only in **TEST**, never LIVE. Its fixture lists no Bancontact CVC but Visa CVC 737. The page says a successful test indicates the integration is not impacted and a failed test merits contacting Adyen; interpret that diagnostic within the described issue and captured period rather than treating one test as broad production assurance (raw lines 96-106).

## Detail locators

- Historical context and affected Bancontact-card choice: raw lines 19-38.
- Front-end card-entry and routing symptoms: raw lines 40-50.
- Integration-specific possible/observed impact and pre-4.2.0 Web threshold: raw lines 52-94.
- TEST-only co-badged fixture and diagnostic action: raw lines 96-106.

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-card/co-branded-cards/2026-09-15|Co-badged Bancontact card issues (2022-modified, 2026-09-15 capture)]]
