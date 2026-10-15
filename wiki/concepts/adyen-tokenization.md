---
title: "Adyen Tokenization"
type: concept
category: technology
tags: [adyen, tokenization, recurring-payments, stored-payment-methods]
---

## Definition

Adyen tokenization replaces sensitive payment details with a token. The 2026-09-15 guide calls Tokenize an Adyen Uplift module. With shopper consent, Adyen stores the details in the Adyen Vault; the merchant uses the token for later one-click, subscription, or non-fixed-schedule payments. Sessions and Advanced are distinct server-side implementation routes, and a Sessions integration still uses `/payments` for shopper-not-present token payments. [[source-adyen-docs-online-payments-tokenization]]

## Scope boundaries

A token must be associated with a shopper-unique reference. References and tokens are limited to one merchant account by default; cross-merchant-account sharing requires Support-enabled Token Groups. Collecting raw card data requires full PCI DSS compliance. The documentation snapshot does not prove current eligibility, enablement, compliance status, payment-method availability, or successful execution.

## Sources

- [[source-adyen-docs-development-resources-migrating-payment-data]] — 2026-09-15 capture of a 2019-modified, provider-assisted old-PSP data/card migration overview covering shopper-reference mapping, encrypted transfer and staged recurring-charge cutover.


- [[source-adyen-docs-development-resources-data-protection-api]] — 2026-09-15 Data Protection API guide for payment-reference-scoped shopper erasure requests, asynchronous acceptance and recurring-transaction force flag; separate from Checkout stored-token deletion.


- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-authorise-using-details-stored-with-a-third-party]] — inactive Classic authorisation guide for initial and subsequent card payments using details stored by a third party, with Ecommerce/ContAuth and fixed-schedule distinctions (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-disable-stored-details]] — inactive Classic `/disable` guide for one stored detail versus all shopper details, with an all-details example that conflicts with its selector prose (2026-09-15 webpage snapshot).


- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization]] — 2019-modified Classic recurring-contract overview for shopper/merchant identity, 16-character detail references, one-click versus subscription descriptions, cross-account qualification, and inactive endpoint scope (2026-09-15 snapshot).


- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-retrieve-stored-details]] — inactive Classic Recurring API `/listRecurringDetails` guide for shopper-scoped stored-detail lookup and `recurringDetailReference` response cases (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-update-stored-details]] — 2026-09-15 inactive Classic API guide for updating stored credit-card details on a successful recurring `/authorise`, with old-reference invalidation and separate retrieval of the new reference.


- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-authorise-a-recurring-payment]] — inactive Classic `/authorise` guide for subsequent stored-detail one-click `CardOnFile` versus recurring `Subscription` requests (2026-09-15 webpage snapshot).


- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-store-payment-details]] — inactive Classic `/authorise` guide for storing a shopper-linked recurring detail after successful payment and selecting it for later use (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-point-of-sale-recurring-payments]] — Adyen Docs website guide to consented Terminal API POS token creation and later online Checkout token charges (2026-09-15 snapshot).


- [[source-adyen-docs-online-payments-account-updater-batch-account-updater]] — Adyen Batch Account Updater guide (webpage snapshot, 2026-09-15) for SFTP or scheduled single-card requests, encrypted batch result files, and follow-up stored-card actions.


- [[source-adyen-docs-online-payments-account-updater-real-time-account-updater]] — Adyen Real Time Account Updater guide for eligible in-processing card updates and retry, optional response data, statuses, and test scenarios (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-development-resources-migrating-payment-data-import-payment-details-for-recurring-payments]] — 2026-09-15 Adyen webpage guide to provider-assisted encrypted CSV import of recurring payment details, method-specific input and output-result handling.


- [[source-adyen-docs-online-payments-tokenization-forward-payment-details]] — 2026-09-15 Adyen webpage guide to Checkout API v70-or-later forwarding of stored card details or network tokens to a PCI-compliant third party, including setup and fallback conditions.


- [[source-adyen-docs-online-payments-account-updater]] — 2026-09-15 Adyen webpage overview of Account Updater as a tokenization extension, distinguishing synchronous Real Time payment processing from asynchronous merchant-file Batch updates.


- [[source-adyen-docs-development-resources-testing-tokenization]] — 2026-09-15 pre-live test guide for one-off CardOnFile and optional Subscription token storage/reuse, stored-detail update and removal routes, and Real Time Account Updater fixtures; preserves the Step 4 one-off/subscription wording conflict and PCI/encrypted-test credential boundary

- [[source-adyen-docs-online-payments-tokenization-managing-tokens]] — 2026-09-15 guide to listing tokens, CardOnFile-only and API v70-or-later eligibility-gated updates, deletion with merchant-side cleanup, and recurring-token lifecycle webhooks

- [[source-adyen-docs-online-payments-tokenization-make-token-payments]] — Adyen webpage guide, last modified 2023-07-28 and snapshotted 2026-09-15, for reusing online-payment tokens in shopper-initiated one-click and merchant-initiated subscription or unscheduled card-on-file payments, with endpoint, SCA, lifecycle-webhook, and CVC/PCI qualifications.

- [[source-adyen-docs-online-payments-tokenization-create-tokens]] — Adyen guide to creating online-payment tokens, including consent, endpoint and API-version choices, authorization and webhook timing, SCA, and import conditions (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-tokenization]] - 2026-09-15 guide to tokenization purpose, implementation routes, recurring types, shopper-reference scope, and PCI DSS boundary
