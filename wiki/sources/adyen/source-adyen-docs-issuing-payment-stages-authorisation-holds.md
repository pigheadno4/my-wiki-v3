---
title: "Adyen Issuing authorisation holds"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/payment-stages/authorisation-holds"
raw_files:
  - "adyen/docs/issuing/payment-stages/authorisation-holds/2026-09-15.md"
tags: [adyen, issuing, authorization, holds, cards]
---

## Overview

This 2026-09-15-captured Adyen Issuing page explains holds on a cardholder's balance account after an Adyen-issued-card authorisation, who may reverse a hold, scheme-specific expiry, and the continued capture risk after expiry. A hold reserves the authorized amount until capture or release; release follows merchant cancellation or expiry. It is guidance for explaining held but uncaptured funds, not evidence of a particular card payment or balance. [[adyen]] [[adyen-issuing]]

## Key takeaways

- **Only the processing merchant** can request an authorisation cancellation/reversal; Adyen, acting as issuer, and the platform cannot cancel an existing authorisation or change its expiry timeline on their own. Adyen releases the hold to the cardholder's available balance after the merchant request. Transaction rules can prevent unwanted *future* authorisations, not reverse an existing one. A merchant may cancel even after Adyen approved, and cardholders should ask the merchant why it cancelled. See raw lines 21-27.
- Expiry happens automatically. On expiry Adyen returns the reserved amount to available balance and sends `balancePlatform.transfer.updated`. The initial `balancePlatform.transfer.created` includes `authorisationType` and merchant category code (MCC), which help determine the expiry period. See raw lines 29-38.
- For Visa, the dated table says cruise/lodging/vehicle rental authorisations expire after 31 days; US commuter/bus/railway after 3 days; otherwise after 7 days, based on MCC and merchant location. A separate card-not-present provision allows Visa to extend an authorisation up to 30 days when the acquirer requests it; it is not limited to the table's MCCs. See raw lines 40-50.
- For Mastercard, a pre-authorisation expires after 30 days and the merchant can adjust its value or extend it for another 30 days at the same value; final/default authorisations expire after 7 days. See raw lines 52-62. These are the source snapshot's scheme timelines, not live guarantees.
- **Expiry is not a promise that the returned amount is safe from later capture.** The processing merchant can still submit a capture after expiry, and the page says Adyen as issuer must honor/process each capture request regardless of authorisation status. See raw lines 64-68.

## Detail locators

- Cancellation ownership and examples: raw lines 21-27.
- Expiry webhook and source fields: raw lines 29-38.
- Visa MCC/location and conditional card-not-present timing: raw lines 40-50.
- Mastercard pre/final/default timing and adjustment: raw lines 52-62.

## Related

- [[adyen-issuing]] — main Issuing concept.
- [[source-adyen-docs-issuing-payment-stages]] — card payment lifecycle and funds stages.
- [[source-adyen-docs-issuing-authorisation-transaction-rules]] — future authorisation decisions.

## Raw Sources

- [[raw/adyen/docs/issuing/payment-stages/authorisation-holds/2026-09-15|Adyen Authorisation holds, captured 2026-09-15]]
