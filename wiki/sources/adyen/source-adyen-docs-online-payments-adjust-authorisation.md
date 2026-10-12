---
title: "Adyen Docs: Authorization adjustment"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/adjust-authorisation"
raw_files:
  - "adyen/docs/online-payments/adjust-authorisation/2026-09-15.md"
tags: [adyen, authorization-adjustment, pre-authorization, webhooks, mcc]
---

## Overview

This Adyen online-payments overview explains [[adyen-authorization-adjustment]]: using a pre-authorization to change an authorized amount or extend an authorization before manual capture. It contrasts pre-authorization with final authorization, describes asynchronous and synchronous adjustment models, and catalogs payment-method, Merchant Category Code (MCC), issuer and validity boundaries.

The page is an unversioned website snapshot collected on 2026-09-15. It does not prove current payment-method or MCC support, issuer approval, merchant eligibility, account configuration, adjustment success, capture success, or the present status of a scheme feature.

## Key takeaways

- A pre-authorization can support a later increase or decrease to the initially authorized amount. A final authorization assumes the amount is agreed up front and does not support later adjustment; Adyen documents final authorization as the default for card payment requests on this page.
- Asynchronous adjustment reuses the first PSP reference in adjustment and final-capture requests. Because its result is not immediately clear, the page requires webhook updates to establish whether the final amount was authorized before capture.
- Synchronous adjustment carries the latest `adjustAuthorisationData` blob from one request to the next and returns an adjustment result synchronously. If the blob is omitted at any point, that payment falls back to asynchronous adjustment and cannot return to the synchronous path.
- The documented support boundary is an online-payments integration for payments acquired by Adyen, with required webhook event handling. Availability is limited by payment method and MCC and ultimately depends on the issuer. Apple Pay and Google Pay support follows the associated card scheme; the page separately documents Klarna as asynchronous-only while a payment has not been cancelled, expired or fully captured.
- Only an unexpired pre-authorization can be adjusted. For global card schemes, the page states an Adyen default expiry of 28 days while allowing merchant-account and scheme-specific custom validity; scheme rules can expire an authorization before or after the scheme's stated period. Manual capture of a remaining balance after scheme-side expiry can increase capture-failure, fee and chargeback risk.

## Material boundaries

> [!warning] Eligibility and outcomes
> Documentation of the flow is not evidence that a particular merchant, payment method, MCC or issuer supports an adjustment, or that an adjustment or capture succeeded. The required webhook events and the linked procedural guide remain necessary for operational outcome handling.

> [!warning] Dated scheme rules
> The MCC and validity tables are snapshot evidence, not a current scheme-rule guarantee. They contain scheme-, environment-, authorization-type- and MCC-specific conditions; the page also labels Visa Extended-Auth as pilot-only. Verify current Adyen and scheme guidance before relying on a listed period or eligibility row.

## Detail locators

- Opening definition and manual-capture framing: raw lines 17-19.
- Integration, webhook, payment-method/MCC, issuer, expiry and Adyen-acquisition requirements: `## Requirements`, raw lines 21-33.
- Hospitality, pre-order and high-value/long-delivery examples: `## Use cases`, raw lines 35-52.
- Pre-authorization versus final authorization and the card-request default: `## Authorization type`, raw lines 54-62.
- Original-PSP-reference asynchronous model, webhook dependency, blob-chaining synchronous model and irreversible fallback: `## Asynchronous or synchronous adjustment`, raw lines 64-76.
- Card, Apple Pay, Google Pay and Klarna availability plus the card-scheme MCC table: `## Availability`, raw lines 78-107.
- Default and scheme-side expiry, issuer-dependent partial-capture count, post-expiry capture risks and scheme validity tables: `## Expiration of pre-authorizations`, raw lines 109-199.
- Procedural implementation route: `## Next steps`, raw lines 201-207.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-authorization-adjustment]]
- Procedure: [[source-adyen-docs-online-payments-adjust-authorisation-adjust-with-preauth]]

## Raw Sources

- [[raw/adyen/docs/online-payments/adjust-authorisation/2026-09-15|Adyen Docs: Authorization adjustment]] - complete collected overview for authorization types, adjustment models, availability and validity
