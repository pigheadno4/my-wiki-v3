---
title: "Top up a balance account on demand | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/top-up-balance-account/on-demand-top-ups"
raw_files:
  - "adyen/docs/platforms/top-up-balance-account/on-demand-top-ups/2026-09-15.md"
tags: [adyen, platforms, top-ups, checkout-api, direct-debit, balance-accounts]
---

## Overview

This 2026-09-15 [[adyen]] for Platforms guide describes a manual, one-off **user-funded payment** intended to increase that user's balance-account balance. The funding source is the user's verified bank-account transfer instrument through a supported direct-debit route, or another payment method; a `TopUp` split identifies the balance account to credit. This is neither a platform-liable-to-user internal transfer nor a payout from the balance account to a bank, and an authorized payment response alone is not proof that the balance account was credited. [[adyen-platforms]]

## Eligibility and request route

- The page calls for an Adyen for Platforms integration, Checkout API credentials, a server able to accept Standard webhooks plus Transfer and Transaction webhooks, and Support enablement of on-demand top-ups for the platform. For a verified bank transfer instrument, the user's `receiveFromPlatformPayments` and `receiveFromTransferInstrument` capabilities must be **allowed** with **valid** verification status; bank accounts are limited to the SEPA zone, UK or US. For another payment method, the user's `receiveFromPlatformPayments` capability must be allowed and verification-valid. These are route conditions, not evidence that any particular account or payment method is enabled. See raw lines 21–52.
- The one-off top-up uses Checkout POST `/payments`; the page expressly excludes `/sessions` for initiation. For verified bank funding, the method values listed are US `ach` in USD, SEPA `sepadirectdebit` in EUR and UK `directdebit_GB` in GBP, with the user's verified `transferInstrumentId`. The request tables list merchant account, unique reference, return URL, payment method and amount value, with `amount.currency` marked conditionally required for currency conversion. The examples use Checkout test v72 and versioned client libraries; they are request shapes, not current provider acceptance or live booking. See raw lines 63–96 and 114–722.
- To identify the payment as a top-up and direct booking, the `splits` array carries a `TopUp` item with the top-up amount and target balance-account ID, plus fee-type item(s) for transaction fees; fee amounts need not be specified at payment time because they are then unknown. The tables mark `splits` required in the illustrated top-up route, yet also state that **without** `splits` the funds book to the platform liable account and are classified as a regular payment. Do not read the table as saying an omitted array still tops up the user. Defining top-ups separately supports report reconciliation and, for US users as the page states, excludes top-ups from 1099-K revenue filings. See raw lines 54–61, 95–112 and 180–209.

## Outcome and direct-debit warnings

- The illustrated `/payments` responses return `resultCode: Authorised`, but the guide directs readers to top-up webhooks for the incoming request's progression from received and authorized to funds added to the balance account, including failure. A request/authorization is not a booked credit; the page provides no proof of a particular live credit, payout or external bank receipt. See raw lines 155–178, 724–748.
- Funding from the user's verified bank account requires regional direct-debit compliance. For SEPA, the user must first accept a debit mandate; the page says acceptance is needed once and offers recommended text. For UK BACS, each top-up requires the user's confirmations about authorization, account ownership and sole signatory, plus advance email notice containing amount, due date, recurring detail reference and platform contact details. The page says users may charge back without notice at least **10 days before a charge**, while it also describes a due date **2 business days after initiation**; these lines must be reconciled in the actual notice/initiation plan, not treated as permission to notify only when initiating. It does not state an equivalent US mandate procedure here. See raw lines 750–795.

## Detail locators

- **User-funded purpose, credentials, webhooks, capabilities, geography and Support enablement:** raw lines 15–52.
- **Top-up classification and US reporting statement:** raw lines 54–70.
- **`/payments` versus `/sessions`, bank method/transfer-instrument fields and no-splits liable fallback:** raw lines 72–112.
- **SEPA direct-debit test request/authorization sample:** raw lines 114–178.
- **Other-method fields, split rules and versioned test examples:** raw lines 180–722.
- **Authorized response, top-up status-webhook route and SEPA/UK mandates and notice:** raw lines 724–795.

## Related

- [[adyen-platforms]]
- [[adyen-platform-internal-transfers]] — separate balance-account-to-balance-account route

## Raw Sources

- [[raw/adyen/docs/platforms/top-up-balance-account/on-demand-top-ups/2026-09-15|Adyen Platforms on-demand top-up guide — collected 2026-09-15]]
