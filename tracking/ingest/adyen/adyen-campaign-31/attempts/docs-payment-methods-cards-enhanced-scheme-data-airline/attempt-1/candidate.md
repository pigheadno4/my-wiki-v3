---
title: "Adyen airline enhanced scheme data"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/airline"
raw_files:
  - "adyen/docs/payment-methods/cards/enhanced-scheme-data/airline/2026-09-15.md"
tags: [adyen, cards, airline, enhanced-scheme-data]
---

## Overview

Adyen guide for adding airline enhanced scheme data (ESD) to eligible US domestic card transactions by merchants with specified travel MCCs, aiming for scheme-specific interchange treatment. It was last modified 2023-04-06 and captured 2026-09-15. The page says its own limits supplement the parent ESD requirements, which must be checked separately. The historical eligibility and interchange statements are not proof of merchant qualification, a discounted rate, authorization, capture or settlement.

## Key takeaways

- Eligible MCCs listed for Mastercard and Visa are 3000–3350 and 4511; the page says airline data may be sent for commercial and consumer cards. MCC 4722 is limited: Mastercard consumer transactions automatically get a discount and commercial ones can instead submit Level 2/3 data; Visa card-present consumer/commercial transactions must send airline data for a discount, card-not-present transactions need not, and Visa commercial transactions cannot send Level 2/3 data. Preserve scheme, card and channel conditions; a payment or POS link does not broaden the rule (raw lines 26–54).
- Capture setting determines endpoint and field container: automatic or delayed automatic capture sends `additionalData.airline` with `/payments`, while manual single or multiple partial capture sends `enhancedSchemeData.airline` with `/payments/{paymentPspReference}/captures`. The page gives no API minimum; v72 appears in examples, not as a stated requirement (raw lines 56–68, 92–212).
- Its payment/capture mapping marks airline code, ticket number, passenger name, carrier code, class of travel, destination, travel date, departure airport, flight number and issue date as required; stopover/fare/tax/reservation/travel-agency fields are shown without that mark. The capture-column table spells the required departure airport field `legs.depatureAirportCode`, but the capture sample uses `departureAirportCode`; verify the authoritative schema before implementation. The `/payments` example also omits the table’s required `issue_date`. Do not treat either example as a complete validated payload (raw lines 69–88, 96–148, 154–212).
- The `/payments` example includes plain card number/CVC values and a test endpoint, and the testing section lists test cards. This is illustrative source material, not authorization to handle live raw card data or evidence of PCI compliance. The examples have idempotency-key placeholders but show no result, webhook, interchange assessment or funds receipt (raw lines 94–147, 150–221).

## Detail locators

- MCC/scheme/card-present eligibility and parent-requirements boundary: raw lines 19–54.
- Capture-mode endpoint selection and required/optional field mapping: raw lines 56–88.
- Versioned test request illustrations and field-name discrepancy: raw lines 90–212.
- Test-card fixtures: raw lines 214–221.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/enhanced-scheme-data/airline/2026-09-15|Adyen airline ESD guide snapshot]]
