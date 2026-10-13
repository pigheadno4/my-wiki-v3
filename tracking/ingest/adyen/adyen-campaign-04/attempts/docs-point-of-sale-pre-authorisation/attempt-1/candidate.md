---
title: "Adyen POS pre-authorization and authorization adjustment"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/pre-authorisation"
raw_files:
  - "adyen/docs/point-of-sale/pre-authorisation/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, pre-authorization, authorization-adjustment, capture]
---

## Overview

This unversioned Adyen website guide, captured on 2026-09-15, describes the **merchant's in-person Terminal API pre-authorization**, later backend authorization adjustment, and manual capture. It belongs to [[adyen-authorization-adjustment]] and [[adyen-terminal-api]]. It does not establish current scheme rules, merchant eligibility, issuer acceptance, or a completed adjustment or capture.

## Key takeaways

- The merchant starts with a Terminal API payment request using `authorisationType=PreAuth`; final authorization is the documented default and cannot be adjusted later. The terminal handles the shopper's card presentation and initial payment. Subsequent amount adjustments go **directly to Adyen's backend**, not to the terminal or its Cloud endpoint; capture is another backend modification.
- Each amount update specifies the **new total authorized amount in minor units**, not just the increment. The request uses the original pre-authorization PSP reference; its own modification PSP reference is distinct. The merchant calculates the new amount and decides when to adjust.
- The asynchronous path returns `received` and requires the `AUTHORISATION_ADJUSTMENT` webhook to determine whether the new amount was authorized before capture. The optional synchronous path requires account enablement and passing the latest `adjustAuthorisationData` blob through every adjustment; omitting it irreversibly switches that payment to asynchronous adjustment.
- Manual capture must be enabled for the account or individual pre-authorization. After **all intended adjustments**, the merchant requests capture against the original payment PSP reference and awaits the `CAPTURE` webhook. Capture is asynchronous: an apparent remaining authorization after the capture request does not make another adjustment safe. If the shopper instead pays another way, the guide directs cancellation of the pre-authorization.
- This flow requires a terminal integration, API key and payment roles, payment-method configuration with Adyen Support, and Standard webhooks for `AUTHORISATION_ADJUSTMENT`, `CAPTURE`, and `CAPTURE_FAILED`. When building or testing, the page directs at least a five-second gap between pre-authorization and adjustment.

## Material boundaries

> [!warning] Eligibility and expiry
> Adjustment depends on payment method, card scheme, merchant category code and issuer acceptance. Wallet availability follows the associated card scheme. Only an unexpired pre-authorization can be adjusted. Adyen's stated 28-day default expiry for global schemes and the scheme-side validity tables are distinct; scheme, region, environment, authorization type and MCC affect the listed periods. Scheme-side expiry can precede Adyen expiry, and capture afterward raises failure, fee and chargeback risk. China UnionPay's section says an adjustment does not extend its validity period.

> [!warning] Source table conflict and outcome boundary
> The snapshot's MCC table says Visa adjustment excludes MCC 5542, while its Visa validity table includes a Pre-Auth 5542 row (two hours). Do not infer eligibility from that validity row. This dated page and its test examples do not prove present eligibility or successful processing; confirm current scheme guidance and actual webhook outcomes.

## Detail locators

- Requirements, setup, webhook events, method/MCC and issuer limits: raw `## Requirements`, lines 21-37.
- Pre-authorization versus final authorization and default type: raw `## Authorization type`, lines 69-80; optional account configuration: lines 96-106.
- Optional smart pre-authorization checks card brand/funding source; QR, MOTO and MKE are excluded: raw lines 33-35 and `## Enable smart pre-authorization (Optional)`, lines 108-126.
- Initial terminal request fields, shopper presentation, response identifiers and optional initial blob: raw `## 1. Pre-authorize a payment`, lines 128-251.
- Backend amount updates, new-total amount, asynchronous webhook and synchronous blob result: raw `## 2. Adjust the pre-authorized amount`, lines 253-831. The synchronous tab's language-library examples include older Payments API shapes; use the guide's Checkout `/amountUpdates` procedure and verify current API contracts before implementation.
- Same-amount extension and capture/cancel lifecycle: raw `### Extending the authorization`, lines 832-841, and `## 3. Capture the payment`, lines 842-905.
- Test delay, payment-method/MCC availability, expiry risks and scheme-specific validity tables: raw `## Testing`, lines 907-911; `## Availability`, lines 913-941; `## Expiration of pre-authorizations`, lines 943-1033.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-authorization-adjustment]]
- Terminal API boundary: [[adyen-terminal-api]]
- Online-payment adjustment: [[source-adyen-docs-online-payments-adjust-authorisation-adjust-with-preauth]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/pre-authorisation/2026-09-15|Adyen POS pre-authorization and authorization adjustment]] — full captured guide and dated scheme tables
