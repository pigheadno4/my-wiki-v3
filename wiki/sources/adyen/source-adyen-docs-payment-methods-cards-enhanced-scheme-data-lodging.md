---
title: "Adyen lodging enhanced scheme data for US domestic cards"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/lodging"
raw_files:
  - "adyen/docs/payment-methods/cards/enhanced-scheme-data/lodging/2026-09-15.md"
tags: [adyen, cards, lodging, enhanced-scheme-data, interchange]
---

## Overview

This [[adyen]] guide, last modified 2023-03-09 and captured 2026-09-15, covers **lodging enhanced scheme data (ESD)** for eligible **US domestic** Visa and Mastercard card transactions. It describes check-in/out and other lodging details that may help a merchant avoid a Visa downgrade or qualify for Mastercard's industry-specific interchange. These are scheme- and eligibility-dependent purposes, not a guaranteed rate reduction, authorization, capture or settlement. It inherits the requirements of [[source-adyen-docs-payment-methods-cards-enhanced-scheme-data]]; see [[adyen-online-payments]].

## Key takeaways

- **Eligibility and inherited controls:** The lodging guide lists MCC **3501–3999** and **7011** for Visa and Mastercard and says it applies to commercial and consumer cards. Its parent ESD guide requires an **Advanced-flow online payments integration** listening for AUTHORISATION and CAPTURE webhooks, excludes certain MCCs from ESD, says invalid/incomplete or ineligible ESD can be omitted while payment processing continues, and does not allow ESD to be fixed after processing. This page alone does not establish a merchant's actual MCC, scheme acceptance or interchange benefit. See pinned raw lines 17–50 and parent ESD source for its broader requirements.
- **Capture route matters:** For automatic or delayed automatic capture, the page sends lodging ESD in Checkout `/payments`. For manual single or multiple partial capture, it directs an **existing Classic API** integration to `/capture`. It explicitly says Checkout API capture requests do **not** support lodging ESD in this snapshot. The separate paths must not be blended or read as a general Checkout `/captures` capability. It names `travelEntertainmentAuthData.market` and `.duration` as payment-request-only fields. See pinned raw lines 32–41 and 52–57.
- **Field requirements and path conflict:** The field table marks check-in date, check-out date, folio number, room rate, number of nights, customer-service toll-free number and property phone number as required; tax, no-show, food/beverage and other fields are not marked required there. Prose names `additionalData.lodging` for `/payments` and `additionalData.enhancedSchemeData.lodging` for Classic `/capture`, but both example JSON bodies instead put flattened `lodging.*` keys directly inside `additionalData`. The page also says “car rental specific” in the lodging flow and “airline data” above the lodging field table. These are material wording/shape inconsistencies; verify the relevant API and version before implementing. See pinned raw lines 52–82, 84–164.
- **Example limits:** The test `/payments` curl uses Checkout v72 and includes clear card `number` and `cvc` test values; this is an illustrative test fixture, not a safe live card-data-handling pattern or PCI-compliance evidence. The capture example targets the Classic Payment API `/capture` path despite its section heading saying `/captures`. Both shell examples put `-X POST` immediately before `-d` without a line-continuation backslash; treat them as non-executable illustrations until repaired and version-checked. The page provides two test card numbers but no response, ESD validation feedback, successful capture or fee outcome. See pinned raw lines 84–173.

## Detail locators

- Stated Visa/Mastercard ESD purposes, inherited requirements, eligible MCCs and card types: pinned raw lines 17–50.
- Capture-mode choice and payment-only travel-entertainment fields: pinned raw lines 32–41 and 52–57.
- Full required/optional lodging field table: pinned raw lines 59–82.
- Checkout test v72 `/payments` example with raw test card fields and flattened `additionalData`: pinned raw lines 84–129.
- Classic Payment API capture illustration, plural heading versus singular path and flattened keys: pinned raw lines 131–164.
- Test Visa/Mastercard fixture numbers: pinned raw lines 166–173.

## Related

- [[adyen-online-payments]] — main online card-payment route.
- [[adyen-payment-capture]] — authorization versus capture and capture modes.
- [[source-adyen-docs-payment-methods-cards-enhanced-scheme-data]] — parent ESD eligibility, feedback and immutable-data boundaries.
- [[adyen-pci-dss-compliance]] — merchant card-data handling is architecture-specific.

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/enhanced-scheme-data/lodging/2026-09-15|Lodging enhanced scheme data guide, captured 2026-09-15]]
