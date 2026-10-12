---
title: "Adyen Docs: Account Updater"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/account-updater"
raw_files:
  - "adyen/docs/online-payments/account-updater/2026-09-15.md"
tags: [adyen, account-updater, tokenization, cards, recurring-payments]
---

## Overview

This 2026-09-15 snapshot of an [[adyen|Adyen]] documentation overview introduces Account Updater as an extension of [[adyen-tokenization|Adyen tokenization]] for receiving card-account changes from Visa, Mastercard, and Cartes Bancaires. It distinguishes synchronous Real Time Account Updater during payment processing from asynchronous Batch Account Updater using merchant-submitted files. The overview does not establish a particular merchant's service enablement or a successful live update.

## Key takeaways

- Account changes described here include a new expiry date or replacement card, loss or theft reported by the shopper, and a shopper telling the issuer that the merchant is no longer authorized to charge the card automatically. These are possible update notices; the overview does not describe a single uniform card-detail replacement for all of them.
- For Real Time Account Updater, Adyen asks for updates while a payment is processed. If a payment is declined, Adyen sends an account-update request and immediately retries the payment with updated details. Updated card information is returned synchronously in the payment response; when Adyen tokenization is used, the token storing the details is updated automatically.
- For Batch Account Updater, the merchant sends batch request files, Adyen obtains updates from the card schemes, and Adyen returns a batch result file. The merchant then needs to make a `/payments` request to update the card details. The overview presents batch control over which cards are updated and when, and availability of updated details at a chosen time or on the initial transaction attempt, as use-case benefits.

## Detail locators

- **Service purpose and update notices** — `# Account Updater` and `What is Real Time Account Updater?`, raw lines 15-30.
- **Mode selection** — `## Choose your Account Updater`, raw lines 32-34.
- **Real Time flow** — `### Real Time Account Updater`, raw lines 36-40.
- **Batch flow and stated benefits** — `### Batch Account Updater`, raw lines 42-50.
- **Further integration guides** — `## Next steps`, raw lines 52-60.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/online-payments/account-updater/2026-09-15|Adyen Docs — Account Updater (2026-09-15)]]
