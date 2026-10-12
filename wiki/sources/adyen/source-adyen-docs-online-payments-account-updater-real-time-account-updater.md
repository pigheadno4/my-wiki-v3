---
title: "Adyen Real Time Account Updater"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/account-updater/real-time-account-updater"
raw_files:
  - "adyen/docs/online-payments/account-updater/real-time-account-updater/2026-09-15.md"
tags: [adyen, account-updater, cards, tokenization, recurring-payments]
---

## Overview

This Adyen guide describes Real Time Account Updater for Visa, Mastercard, and Cartes Bancaires cards. During processing of a refused eligible payment, Adyen checks for updated card details and, if available, retries with them as part of the same transaction. It explains service enablement, response-data options, updater statuses, reporting, and test fixtures.

## Key takeaways

- The guide requires an online-payments Advanced flow and Adyen Support enablement. Eligibility also requires a nonzero payment amount, `shopperInteraction: ContAuth`, and no security code in the payment. This snapshot does not prove that a specific account is enabled or that an update exists for a particular card.
- Updated-card information in the payment response is optional and requires Customer Area additional-data configuration. If Adyen Tokenization is used, the stored card details are updated automatically while `storedPaymentMethodId` stays the same. Do not equate this in-processing retry with a later, separate rescue attempt or assume that the payment ultimately authorizes.
- Receiving a full updated PAN is a separate, Support-enabled path for fully PCI-compliant merchants. Adyen requires a 2048-bit RSA public key and returns the number in JWE-encrypted `realtimeAccountUpdaterSecureData`; the merchant decrypts it with its private key. The guide distinguishes this from selected card summary, expiry, and updater-status response data.
- `additionalData.realtimeAccountUpdaterStatus` distinguishes card-number change, expiry change, closed account, Visa-only request to contact the cardholder, and no change. For `CloseAccount`, Adyen says it does not automatically remove card details; the merchant should disable them and request new shopper details.
- The test scenarios provide specific card numbers and expiry dates, plus a `test_` credential route for integrations unable to process raw card data. The examples use Adyen's test environment and pinned SDK versions; they do not prove live account-updater behavior.

## Detail locators

- Opening through `## Requirements` (raw lines 14–33): supported schemes, in-processing retry, token behavior, Advanced-flow prerequisite, eligibility limitations, and Support setup.
- `## How it works` and `## Receive card updates in payment responses` (raw lines 35–85): processing steps, optional additional-data configuration, and response example.
- `## Receive updated card numbers` (raw lines 87–137): fully PCI-compliant PAN path, RSA public-key setup, JWE response field, and decryption details.
- `## Get account update statuses` and reporting (raw lines 139–157): status table, closed-account handling, and report routes.
- `## Testing` (raw lines 159–502): test card/expiry matrix, `test_` convention, and version- and environment-qualified API examples.

## Related

- Company: [[adyen]]
- Concept: [[adyen-tokenization]]
- Overview source: [[source-adyen-docs-online-payments-account-updater]]

## Raw Sources

- [[raw/adyen/docs/online-payments/account-updater/real-time-account-updater/2026-09-15|2026-09-15 Adyen Real Time Account Updater guide]]
