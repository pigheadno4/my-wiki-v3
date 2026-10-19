---
title: "Adyen Issuing: Payment stages"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/payment-stages"
raw_files:
  - "adyen/docs/issuing/payment-stages/2026-09-15.md"
tags: [adyen, issuing, card-payments, authorisation, capture, webhooks]
---

## Overview

This Adyen Issuing guide (last modified 2019-12-06; captured 2026-09-15) describes stages of an issued-card payment and their effect on the cardholder's balance account. The **processing merchant** sends card-payment and later capture requests; Adyen is the card issuer and sends balance-platform transfer webhooks to the platform. A payment event or example does not prove a particular payment was authorised, captured, refunded or settled. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- **Request and authorisation:** On receiving the processing merchant's payment request, Adyen sends `balancePlatform.transfer.created` with request details. The authorisation decision uses the platform's relayed decision, transaction rules and other validations; `balancePlatform.transfer.updated` reports the request and result. An authorised amount is **reserved**, not yet deducted from the balance account. The merchant can then capture, cancel, or let the authorisation expire.
- **Changes to a hold:** A merchant may adjust the authorised amount. If an authorisation expires without capture, or is cancelled before capture, the reserved amount returns to available balance; the page says expiry varies by scheme and authorisation type and is seven days in most cases. These changes generate transfer-updated webhooks. A card scheme may later authorise or refuse after Adyen's initial decision; if the advice differs, Adyen defers to the scheme, which determines final payment status and reserved-balance changes, with a new transfer-updated booking event.
- **Capture and money flow:** At capture the processing merchant confirms the transaction and asks for funds. Adyen then deducts the captured amount from the cardholder's balance account and sends it to the processing merchant, reporting the event through `balancePlatform.transfer.updated`. Full capture is the default; partial, multiple partial, overcapture and forced capture are also described. A single partial capture can leave a remainder released after the expiry timeframe, while multiple partial captures can use an authorisation for separate later captures. These are possible processing patterns, not a promise that every merchant uses them.
- **Forced capture liability:** A forced capture has no valid authorisation because it was declined or never received. The card scheme sends the unmatched capture; the guide says Adyen cannot decline it and must debit funds. Its transfer webhook marks `categoryData.IssuedCard.authorisationType` as `syntheticAuthorisation`. Because authorisation's balance check was skipped, insufficient funds can produce a **negative balance**. If the linked balance account is inactive or blocked, Adyen debits the **platform's liable balance account**. A cardholder or platform can dispute an illegitimate forced capture, but a chargeback depends on authorisation requirements, transaction type and regional rules.
- **Refund signal:** When the processing merchant initiates a refund, a transfer-updated webhook reports the **refund request**. The page does not say that this webhook alone confirms money has been credited back.

## Detail locators

- Actors, balance effect, Customer Area Transfers view and webhook route: pinned raw lines 17–28.
- Request, authorisation hold, adjustment, expiration, cancellation and scheme advice: pinned raw lines 30–64.
- Capture, partial/multiple partial, overcapture and examples: pinned raw lines 66–113.
- Forced capture triggers, synthetic authorisation marker, dispute qualification, negative balance and liable-account debit: pinned raw lines 114–134.
- Refund request signal and linked next steps: pinned raw lines 136–160.

## Related

- [[source-adyen-docs-issuing-payment-stages-check-details-payment]] — payment/transfer lookup and status-history routes.
- [[source-adyen-docs-issuing-authorisation-transaction-rules]] — Issuing authorisation-decision context.

## Raw Sources

- [[raw/adyen/docs/issuing/payment-stages/2026-09-15|Adyen Issuing payment stages, captured 2026-09-15]]
