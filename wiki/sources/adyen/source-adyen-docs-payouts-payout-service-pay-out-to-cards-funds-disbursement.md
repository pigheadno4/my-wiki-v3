---
title: "Adyen Payout Service third-party card disbursement"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/pay-out-to-cards/funds-disbursement"
raw_files:
  - "adyen/docs/payouts/payout-service/pay-out-to-cards/funds-disbursement/2026-09-15.md"
tags: [adyen, payout-service, card-payouts, transfers-api, tokenization]
---

## Overview

This [[adyen]] Payout Service guide, last modified 2023-11-30 and captured 2026-09-15, describes Transfers API payout requests that debit a source balance account and send funds to a **third-party Mastercard or Visa card**. It belongs under [[adyen-payouts]]; it is not Issuing a card, an internal balance-account transfer, or the legacy Online Payout API. The guide offers one-off raw-card, one-off tokenized-card and recurring tokenized-card request paths, followed by separate webhook status tracking.

## Key takeaways

- Prerequisites are a Payout Service integration, Checkout API tokenization capability for the saved-card paths, a balance-platform Transfers API credential with **Bank Transfer Initiation Webservice** and **TransferService Webservice Initiate** roles, Transfer and Transaction webhook subscriptions with an accepting server, and Adyen-representative enablement. Checking card payout eligibility is recommended. If not fully PCI compliant **or** making recurring payouts, tokenization/saved card details are required; the page allows raw details for a fully PCI-compliant one-off route. See raw lines 23–39.
- POST `/transfers` with `amount`, debited source `balanceAccountId`, `category: card` and `counterparty.card`. The cardholder address/name/type and identification details are described in the route-specific tables; internal `reference` is not sent to the recipient. Raw-card examples provide number/expiry, while tokenized requests use `cardIdentification.storedPaymentMethodId`. The one-off tokenized route first stores the card with `recurringProcessingModel: CardOnFile`; recurring payouts require a saved card with `recurringProcessingModel: Subscription`. See raw lines 41–66, 709–735 and 1370–1396.
- The raw-card parameter table marks `cardHolder.reference` required and says it must equal the token-creation `shopperReference`, yet the immediately following raw-card curl example omits that reference (raw lines 58–107). Do not infer from the example that it is optional or that raw-card/token requirements are fully resolved. Card numbers and tokens in examples are TEST illustrations, not usable recipient credentials. Versioned SDK examples span several languages and versions; consult the pinned raw for syntax, not as execution proof. See raw lines 67–581 and 737–1905.
- The one-off and recurring HTTP 2XX response examples have `direction: outgoing`, `reason: approved`, `status: authorised` and `type: cardTransfer`; HTTP 2XX/`authorised` is not booked debit or a credited card outcome. The guide points to status webhooks for received, authorised and booked/deducted stages. See raw lines 583–633, 1246–1295, 1907–1956 and 2031–2035.
- `executionDate.date` can schedule processing within 30 days in YYYY-MM-DD format, with optional tz-database timezone. The guide says a successful future request stays `received`/`pending` until processing, with a one-time attempt after balance sufficiency and any optional team review are checked. Errors including insufficient funds end `failed` with a webhook. The prose says the 00:00–03:00 window uses the Balance Platform timezone by default, while the field table names `Europe/Amsterdam` as timezone default; do not assume these defaults coincide. See raw lines 637–707, 1299–1368 and 1960–2029.

## Evidence boundary

A card-payout request, eligible-card check, saved token, HTTP 2XX or `authorised` response does not establish a booked balance-account debit or cardholder receipt. Webhooks track later changes; the pinned guide does not document a final recipient-credit guarantee. The repeated future-date sections have the same one-attempt/no-automatic-retry boundary, not three different processing policies. Historical SDK and TEST examples do not prove present-day product enablement.

## Detail locators

- Requirements and raw-card route: raw lines 23–66 and 67–633.
- Future-date scheduling: raw lines 637–707, 1299–1368, 1960–2029.
- One-off CardOnFile token route: raw lines 709–1295.
- Subscription recurring route: raw lines 1370–1956.
- Webhook tracking and TEST cards: raw lines 2031–2043.

## Related

- [[adyen-payouts]]
- [[source-adyen-docs-payouts-payout-service-pay-out-to-cards-manage-card-details]]
- [[source-adyen-docs-payouts-payout-service-pay-out-to-cards-payout-webhooks]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/pay-out-to-cards/funds-disbursement/2026-09-15|Payout Service third-party card payout guide, 2026-09-15 capture]]
