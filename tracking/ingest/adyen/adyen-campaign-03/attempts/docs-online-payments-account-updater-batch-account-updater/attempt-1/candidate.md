---
title: "Adyen Docs: Batch Account Updater"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/account-updater/batch-account-updater"
raw_files:
  - "adyen/docs/online-payments/account-updater/batch-account-updater/2026-09-15.md"
tags: [adyen, account-updater, batch, tokenization, recurring-cards]
---

## Overview

This Adyen Batch Account Updater guide describes an asynchronous merchant-initiated route for obtaining Visa and Mastercard card-detail updates, then acting on the result. Merchants submit an SFTP batch file or schedule one card through `/scheduleAccountUpdater`; Adyen sends the request to the schemes and returns an update in a **batch result file**. This is distinct from Real Time Account Updater during payment processing and routes through [[adyen-tokenization]].

## Key takeaways

- Adyen says Batch Account Updater needs additional Support configuration before integration. Batch files need an SFTP directory arranged with Support, including the merchant's IP address and SSH/PGP keys. Adyen validates the request file and emits an ACK; after successful validation, scheme update processing takes a **minimum of two days from receipt of the ACK** before the result file. The ACK is a validation checkpoint, not an updated-card or payment result.
- The one-card API route accepts card data or Adyen token references in a POST `/scheduleAccountUpdater` request. Its immediate `Success` response indicates **receipt of the request**, after which Adyen forwards it to Visa and Mastercard. The merchant still retrieves an **encrypted batch result file** for the actual update outcome; this is not a synchronous per-card update response.
- Result statuses include unchanged, changed PAN, changed expiry, permanently closed account, Visa-only `ContactCardAccountHolder` when the shopper withheld updated details, and error states. The raw status table gives detailed alternative values. A result file can require different merchant actions; it does not itself rewrite the merchant's stored card.
- If the merchant tokenizes with Adyen, the guide says the token remains the same, but changed card details must be updated through a **payment request**. That update flow also requires Support enablement; otherwise Adyen says the update attempt returns an API error. A merchant not tokenizing with Adyen updates its own stored details. The sample payment requests are examples of an update route, not evidence of a successful charge or guaranteed credential update.
- For a disabled card, Adyen says it **does not delete** the `storedPaymentMethodId` or `recurringDetailReference`; the merchant receives the update and must delete the card details. The Account Updater results report summarizes both Batch and Real Time outcomes and fees, but a shared report does not make their processing flows identical.

## Detail locators

- **Introduction / Set up an SFTP server, raw lines 17–33** — Visa/Mastercard purpose, Support prerequisite, actor sequence, and SFTP inputs.
- **Use batch request files, raw lines 35–99** — example file structure, validation ACK, minimum two-day scheme step, result file, and tokenized versus merchant-owned update action.
- **Use API calls, raw lines 100–161** — one-card request shapes, receipt-only response, encrypted batch result file, and subsequent card-detail action.
- **Account Updater statuses, raw lines 162–190** — status and alternative-value table, including Visa-only withheld-details state and error.
- **Update old card details, raw lines 192–271** — Support enablement, no-change handling, changed PAN/expiry payment examples, and merchant deletion after disabled-card notification.
- **Get a report on card updates, raw lines 273–275** — combined Batch and Real Time results/fee report.

## Related

- [[adyen]]
- [[adyen-tokenization]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/online-payments/account-updater/batch-account-updater/2026-09-15|Adyen Docs — Batch Account Updater (2026-09-15)]]
