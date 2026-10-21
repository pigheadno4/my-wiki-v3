---
title: "Top up a Marketplace balance account on demand"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/top-up-balance-account/on-demand-top-ups"
raw_files:
  - "adyen/docs/marketplaces/top-up-balance-account/on-demand-top-ups/2026-09-15.md"
tags: [adyen, marketplaces, top-ups, balance-accounts, checkout-api, direct-debit]
---

## Overview

This 2026-09-15 [[adyen]] Marketplace guide describes a manually requested, one-off payment funded by a user to increase that user's balance-account balance. Funding may use the user's verified bank-account transfer instrument or another payment method. A Checkout payment request and its illustrated authorization response are distinct from the later balance-account credit, whose progress and failure the guide routes to top-up webhooks. This is a user-funded top-up, not a platform-liable internal transfer or a payout. [[adyen-platforms]]

## Key takeaways

- The guide requires Checkout API credentials, webhook reception, and Support enablement for on-demand top-ups. For verified-bank funding, the user's `receiveFromPlatformPayments` and `receiveFromTransferInstrument` capabilities must be allowed with valid verification status, and the bank account must be in the SEPA zone, UK, or US. Other methods require allowed, verification-valid `receiveFromPlatformPayments`. These stated conditions do not establish an individual user's eligibility. See raw lines 21–52.
- Initiate the one-off payment with Checkout POST `/payments`, not `/sessions`. The verified-bank route lists US `ach`/USD, SEPA `sepadirectdebit`/EUR, and UK `directdebit_GB`/GBP, using the verified `transferInstrumentId`. The test request uses Checkout v72; it is illustrative rather than evidence of live acceptance. See raw lines 110–133 and 152–216.
- The `splits` array identifies a `TopUp` amount and target balance-account ID, with separate transaction-fee split item(s). Fee amounts need not be specified when the payment is made because they are not yet known. The request tables mark `splits` required for this top-up route, while explicitly saying omission books funds to the platform liable account and classifies them as a regular payment. Top-up classification supports separate reconciliation and the guide's US-user 1099-K treatment statement. See raw lines 54–61, 122–150, and 220–247.
- Verified-bank direct debit has regional conditions: the SEPA user first accepts a mandate; for each UK BACS top-up the user confirms debit authorization, ownership and sole signatory status, and receives advance email notice. The marketplace must email advance notice for each top-up; the page says a user may file a chargeback if they did not receive notification at least 10 days before the charge. Its notice field separately describes a due date two business days after initiation. Treat both as source statements requiring operational reconciliation; the page gives no parallel US mandate procedure. See raw lines 63–108.
- Both illustrated payment responses show `resultCode: Authorised`; the guide directs status tracking through top-up webhooks from request receipt and authorization through funds added or failure. Authorization alone is not booked-credit proof. See raw lines 193–216, 762–786.

## Detail locators

- **Purpose, credential/webhook/capability gates and regional bank limit:** raw lines 15–52.
- **Reporting classification and booking instructions:** raw lines 54–61, 122–150, 220–247.
- **SEPA mandate and UK BACS confirmation/notice:** raw lines 63–108.
- **Payment routes and examples:** raw lines 110–216, 218–782.
- **Asynchronous tracking:** raw lines 784–786.

## Related

- [[adyen-platforms]]
- [[source-adyen-docs-platforms-top-up-balance-account-on-demand-top-ups|Parallel Platforms-path on-demand top-up guide]]
- [[adyen-platform-internal-transfers|Internal fund transfers are a separate route]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/top-up-balance-account/on-demand-top-ups/2026-09-15|Adyen Marketplace on-demand top-up guide — collected 2026-09-15]]
