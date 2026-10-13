---
title: "POS MOTO AVS responses | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mail-and-telephone-order-moto/avs-responses-pos"
raw_files:
  - "adyen/docs/point-of-sale/mail-and-telephone-order-moto/avs-responses-pos/2026-09-15.md"
tags: [adyen, point-of-sale, moto, avs, risk-management]
---

## Overview

This Adyen point-of-sale page maps card-issuer Address Verification System (AVS) responses for Mail Order/Telephone Order (MOTO) payments to the `avsResult` values in a payment response's `AdditionalResponse`. It helps a merchant interpret the postal-code and house-number comparison after staff enter those details on a terminal. The AVS result is a risk signal for deciding whether to proceed or cancel an authorization; it is not itself the authorization result, a fraud guarantee, a liability shift, or a refund outcome.

## Key takeaways

- An optional MOTO AVS check prompts for shopper postal code and house number. The issuer compares the entered data and Adyen maps issuer responses into `avsResult`. If the issuing bank sends no AVS response, Adyen reports `Unknown`. The table separately distinguishes mismatch, unavailable, unsupported card type, no data provided, and fields not checked; absence or `Unknown` must not be treated as a confirmed match.
- The page applies to Terminal API integrations with payment terminals and standalone terminals. It lists American Express, Discover, Mastercard and Visa for AVS, and says all other issuers support it in the US, UK and Canada. It explicitly excludes Android and legacy payment terminals. It does not establish issuer support for Brazil or any other unlisted country, or current support for a specific merchant/card/device combination.
- The mapped codes have distinct meanings: for example, `2` is neither postal code nor address matching, `7` and `24` are both matching, while `0` is Unknown, `3` unavailable, `4` unsupported card type, and `5` no AVS data. Codes `6`, `14`, `15`, and `23` all map to postal-code match in this table. Inspect the full mapping before treating a code as a risk decision.
- The companion MOTO guide explains that an issuer may authorize despite an incomplete or inconclusive AVS match. With a configured capture delay, the merchant can review the result and cancel an authorization if it does not trust the transaction; standalone MOTO has an Approve/Decline step after issuer non-decline, where Decline may cancel or refund according to capture state. That guide also states MOTO has no fraud-chargeback liability shift and assigns that liability to the merchant. This AVS mapping page alone does not define the operational cancellation or refund API or transfer liability.
- These are 2026-09-15 website snapshots with older source modification dates. They do not prove present-day issuer, card-network, country, terminal-model or merchant eligibility, or the result of a particular payment.

## Detail locators

- `# AVS responses for point of sale` — entered address parts, issuer validation, `AdditionalResponse.avsResult`, and the no-response Unknown case.
- `Requirements` — Terminal API/standalone scope, named networks and US/UK/Canada issuer statement, Android/legacy-terminal exclusion.
- `AVS responses` — exact numeric-code-to-result mapping, including partial matches, unavailable and unchecked cases.
- Related [[source-adyen-docs-point-of-sale-mail-and-telephone-order-moto]] — separate MOTO authorization, merchant decision, capture-delay, cancellation/refund and fraud-liability qualifications.

## Related

- Company: [[adyen]]
- Concept: [[adyen-risk-management]]
- POS integration: [[adyen-terminal-api]]
- MOTO flow: [[source-adyen-docs-point-of-sale-mail-and-telephone-order-moto]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mail-and-telephone-order-moto/avs-responses-pos/2026-09-15|2026-09-15 Adyen POS AVS response mapping]]
