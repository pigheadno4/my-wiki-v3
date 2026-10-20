---
title: "Adyen Issuing: Webhooks for payment events"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/webhook-types/payment-events"
raw_files:
  - "adyen/docs/issuing/webhook-types/payment-events/2026-09-15.md"
tags: [adyen, issuing, webhooks, payment-events]
---

## Overview

This 2020-modified Adyen Issuing guide, captured 2026-09-15, maps Adyen-issued-card payment stages to balance-platform webhooks sent to the platform's server. A merchant initiates the card payment; its transfer is `category: issuedCard`, `type: payment`, and outgoing relative to the card-linked balance account. A merchant refund is incoming. The page describes webhook reporting, not a way to initiate a payment or proof that a payment settled. See [[adyen-issuing]] and [[adyen]].

## Key takeaways

- A payment request produces `balancePlatform.transfer.created` with `status: received`; authorisation, refusal, adjusted authorisation, cancellation and expiry are `balancePlatform.transfer.updated` states. `authorised` reports reserved funds; `refused` can follow a transaction-rule violation. An adjusted amount can produce `authAdjustmentAuthorised`, `authAdjustmentRefused` or `authAdjustmentError`.
- Scheme advice can add a `transfer.updated` event with `data.reason: schemeAdvice` and an `adviceAuthorised` or `adviceRefused` event. The guide says to use that webhook's `data.status` as the final payment outcome and whether the authorisation reserve stays or is released. This does not establish capture.
- Before capture, the merchant can cancel an authorisation. On capture, funds are deducted from the balance account and Adyen sends both `transfer.updated` (`captured`) and `balancePlatform.transaction.created`. The examples distinguish full, partial, multiple partial and overcapture. Uncaptured authorised remainder expires; `expired` is reported by `transfer.updated`.
- A forced capture can be processed and deducted without a prior valid authorisation under card-network rules. Its `captured` payload has `categoryData.authorisationType: syntheticAuthorisation`; near-simultaneous received/authorised/captured entries are retrospective accounting, not evidence of an earlier valid authorisation.
- For a merchant refund, Adyen sends `transfer.updated` (`refunded`) and `transaction.created`. The guide explicitly says the refund is not linked to the original payment. Treat example IDs and balances as illustrations, not a matching rule or live outcome.

## Detail locators

- Pinned raw lines 19–29: webhook purpose and `issuedCard` / outgoing-payment versus incoming-refund classifiers.
- Pinned raw lines 31–112, 300–406: received, authorised, adjustment and refusal states; examples show `environment: test`.
- Pinned raw lines 495–505: scheme-advice reason, event status and precedence; lines 740–742: pre-capture cancellation.
- Pinned raw lines 844–1001: capture and transaction webhooks; lines 1004–1390: partial and multiple partial examples; lines 1392–1644: overcapture and forced-capture examples.
- Pinned raw lines 1646–1648: expiry; lines 1766–1779: refund webhooks and unlinked-original warning.
- Example caution: the multiple-partial-capture prose uses EUR while its JSON uses USD (raw lines 1178–1183, 1241–1281), and the refund examples show different transfer IDs in `transfer.updated` and `transaction.created` (lines 1788, 1895–1903). Do not infer an exact identifier reconciliation rule from these examples.

## Related

- [[adyen-issuing]] — Issuing resource and funds context.
- [[source-adyen-docs-issuing-payment-stages]] — payment-stage overview (navigation only).
- [[source-adyen-docs-issuing-authorisation-scheme-advice]] — scheme-advice guide (navigation only).

## Raw Sources

- [[raw/adyen/docs/issuing/webhook-types/payment-events/2026-09-15|Adyen Issuing payment-event webhooks, captured 2026-09-15]]
