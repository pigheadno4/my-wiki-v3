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

- [[source-adyen-docs-payment-methods-pad-web-drop-in]] — PAD Canada Web Drop-in initial-payment token creation and recurring reuse in Sessions/Advanced; future recurring debits require shopper mandate and later requests omit mandate ID (2026-09-15).


- [[source-adyen-docs-payment-methods-pad-api-only]] — 2026-09-15 PAD initial-payment token fields, conditional token response, mandatory shopper agreement and later recurring-token route; initial `Authorised` remains bank-pending.


- [[source-adyen-docs-payment-methods-bacs-api-only]] — 2026-09-15 BACS API-only `/payments` shopper-reference/storage-flag token step, conditional `recurring.token.created` receipt and later `ContAuth` reuse; notice and funds outcomes remain source-qualified.


- [[source-adyen-docs-payment-methods-ach-direct-debit-verification-with-giact]] — ACH giact zero-value account check with optional stored method for a later real-amount payment; source scopes zero option to API-only and shows `/sessions`/`/payments` tabs (2026-09-15).


- [[source-adyen-docs-payment-methods-bacs-ios-drop-in]] — 2026-09-15 BACS iOS Drop-in initial `/payments` token fields, `recurring.token.created` ID and later stored-method `ContAuth` reuse; notice and `Received` limitations stay in source.


- [[source-adyen-docs-payment-methods-bacs-react-native-drop-in]] — 2026-09-15 BACS React Native Drop-in `/payments` token creation with shopper reference/storage flag, `recurring.token.created` ID and later `ContAuth` reuse; notice and webhook outcome remain source-qualified.


- [[source-adyen-docs-payment-methods-bacs-flutter-drop-in]] — BACS Flutter Drop-in initial `/payments` tokenization and recurring reuse; explicit permission is strongly recommended and changed date/amount requires advance notice per captured guide (2026-09-15).


- [[source-adyen-docs-payment-methods-bacs-web-component]] — BACS Web Component recurring-token creation/reuse through `/payments`; explicit permission is strongly recommended and changed collection date/amount requires advance notice per captured guide (2026-09-15).


- [[source-adyen-docs-payment-methods-sepa-direct-debit-ios-drop-in]] — 2026-09-15 iOS Drop-in guide for SEPA token-creation webhook and shopper-absent Subscription/UnscheduledCardOnFile `/payments` reuse; consent and mandate are separately qualified.


- [[source-adyen-docs-payment-methods-bacs-ios-component]] — 2026-09-15 BACS iOS Components initial `/payments` token fields, `recurring.token.created` ID and later stored-method `ContAuth` reuse; notice and Received limitations remain in source.


- [[source-adyen-docs-payment-methods-sepa-direct-debit-api-only]] — 2026-09-15 API-only SEPA token-creation webhook and shopper-absent Subscription/UnscheduledCardOnFile stored-method `/payments` reuse; permission recommendation and mandate duties are source-qualified.


- [[source-adyen-docs-payment-methods-sepa-direct-debit-web-component]] — 2026-09-15 Web Components guide for SEPA token creation webhook and shopper-absent Subscription/UnscheduledCardOnFile `/payments` reuse; source qualifies consent advice and mandate requirements.


- [[source-adyen-docs-payment-methods-sepa-direct-debit-react-native-drop-in]] — 2026-09-15 React Native Drop-in SEPA token-creation webhook and shopper-absent Subscription/UnscheduledCardOnFile `/payments` reuse; explicit permission is recommended here, while mandate requirements are in the method overview.


- [[source-adyen-docs-payment-methods-sepa-direct-debit-flutter-drop-in]] — Flutter Drop-in SEPA token creation through standard fields, lifecycle webhook and shopper-absent Subscription/UnscheduledCardOnFile reuse; explicit permission is strongly recommended, with sample limits in source (2026-09-15).


- [[source-adyen-docs-payment-methods-sepa-direct-debit-web-drop-in]] — Web Drop-in SEPA token creation and shopper-absent Subscription/UnscheduledCardOnFile stored-method reuse, with explicit-permission recommendation (2026-09-15 capture).


- [[source-adyen-docs-payment-methods-sepa-direct-debit-ios-component]] — iOS Components SEPA token creation via standard `/sessions` or `/payments` fields, lifecycle webhook, and shopper-absent Subscription/UnscheduledCardOnFile reuse; explicit permission is strongly recommended, not an asserted mandate rule here.


- [[source-adyen-docs-payment-methods-twint-flutter-component]] — TWINT Flutter Components `/payments` token-creation fields, `recurring.token.created` webhook and Subscription/UnscheduledCardOnFile `ContAuth` reuse; consent/outcome proof remains outside this guide.


- [[source-adyen-docs-payment-methods-twint-ios-drop-in]] — TWINT iOS Drop-in `/payments` token creation and `recurring.token.created` receipt, then `ContAuth` Subscription or UnscheduledCardOnFile stored-method reuse; duplicated guide block adds no second lifecycle (2026-09-15 capture).


- [[source-adyen-docs-payment-methods-twint-ios-component]] — TWINT iOS Components `/payments` storage fields, `recurring.token.created` webhook and later Subscription/UnscheduledCardOnFile `ContAuth` reuse; token/consent outcomes remain source-qualified.


- [[source-adyen-docs-payment-methods-pay-by-bank-us-ios-drop-in]] — iOS Drop-in guide notes recurring tokenization and strongly recommends explicit shopper permission; creation and reuse steps are delegated to the general guide (2026-09-15 capture).


- [[source-adyen-docs-payment-methods-pay-by-bank-us-web-drop-in]] — 2026-09-15 Web Drop-in guide says Pay by Bank (US) supports recurring tokenization and recommends explicit shopper permission; token request details remain in its linked general guide.


- [[source-adyen-docs-payment-methods-pay-by-bank-us-web-component]] — Pay by Bank (US) Web Components guide notes recurring tokenization and strongly recommends explicit shopper permission; method-specific token requests are delegated to the general guide (2026-09-15 capture).


- [[source-adyen-docs-payment-methods-twint-android-drop-in]] — TWINT Android Drop-in token-creation webhook and Subscription/UnscheduledCardOnFile `ContAuth` reuse, plus distinct Sessions/Advanced stored-method UI steps; source preserves `storedPaymentMethodMode` spelling caveat.


- [[source-adyen-docs-payment-methods-twint-android-component]] — TWINT Android Components token creation, recurring.token.created lifecycle and Subscription/UnscheduledCardOnFile ContAuth reuse with separate stored-method display paths; source flags a Sessions field spelling (2026-09-15).


- [[source-adyen-docs-payment-methods-blik-ios-drop-in]] — BLIK iOS guide's OneClick consent fields and `recurring.token.created` notification for later no-code use; the source does not provide a complete reuse request and the BLIK overview marks recurring unsupported.


- [[source-adyen-docs-payment-methods-blik-web-component]] — BLIK One Click shopper-consent and recurring.token.created stored-method route (2026-09-15 capture); conflicting code-free prose and request/example fields remain source-qualified.


- [[source-adyen-docs-payment-methods-gopay-api-only]] — GoPay API-only post-settlement recurring token webhook, later Subscription ContAuth and shopper-PIN CardOnFile redirect/details paths (2026-09-15 snapshot).


- [[source-adyen-docs-payment-methods-ideal-ios-drop-in]] — iDEAL | Wero iOS Drop-in guide routes recurring payments through SEPA Direct Debit `recurring.token.created` and shopper-absent Subscription or UnscheduledCardOnFile reuse; `Received` requires webhook outcome tracking.


- [[source-adyen-docs-payment-methods-ideal-flutter-component]] — Flutter iDEAL | Wero guide's separate SEPA Direct Debit token route for shopper-absent Subscription or UnscheduledCardOnFile payments, with webhook-qualified result (2026-09-15 snapshot).


- [[source-adyen-docs-payment-methods-ideal-react-native-drop-in]] — 2026-09-15 React Native Drop-in guide's SEPA Direct Debit token route for shopper-absent Subscription or UnscheduledCardOnFile payments; `Received` and request-example limits remain in the source.


- [[source-adyen-docs-payment-methods-ideal-web-drop-in]] — 2026-09-15 iDEAL | Wero Web Drop-in recurring route through SEPA Direct Debit token creation and shopper-absent stored-method payments; sample-field caveat in source.


- [[source-adyen-docs-payment-methods-gopay-android-drop-in]] — GoPay Android Drop-in token route: initial `/payments` fields, token webhook after settlement, then separate Subscription and shopper-PIN CardOnFile flows (2026-09-15 snapshot).


- [[source-adyen-docs-payment-methods-gopay-flutter-component]] — 2026-09-15 GoPay Flutter Components guide for post-settlement token webhook, later Subscription ContAuth and shopper-PIN CardOnFile redirect/details route; sample limitations remain in source.


- [[source-adyen-docs-payment-methods-gopay-react-native-drop-in]] — 2026-09-15 GoPay React Native Drop-in guide for post-settlement token webhook, later Subscription ContAuth and shopper-PIN CardOnFile redirect/details route; request examples need source-qualified reading.


- [[source-adyen-docs-payment-methods-ideal-web-component]] — 2026-09-15 Web Components iDEAL | Wero recurring route through SEPA Direct Debit token creation and shopper-absent stored-method payments.


- [[source-adyen-docs-payment-methods-gopay-android-component]] — GoPay Android Components token path: initial-payment settlement precedes `recurring.token.created`; later Subscription token payments differ from CardOnFile PIN-challenge redirects.


- [[source-adyen-docs-payment-methods-gopay-web-component]] — GoPay Web Components token route: initial `/payments` fields, token webhook after settlement, and separate later Subscription and PIN-redirect CardOnFile flows (2026-09-15 snapshot).


- [[source-adyen-docs-payment-methods-ideal-ios-component]] — 2026-09-15 iDEAL | Wero iOS guide's separate SEPA Direct Debit token route for shopper-absent Subscription or UnscheduledCardOnFile payments; token/result and sample boundaries remain in the source.


- [[source-adyen-docs-payment-methods-ideal-android-component]] — 2026-09-15 Android Components guide for iDEAL | Wero recurring through SEPA Direct Debit token creation and shopper-absent Subscription/UnscheduledCardOnFile payments; `Received` still needs webhook outcome.


- [[source-adyen-docs-payment-methods-gcash-api-only]] — GCash API-only recurring route: shopper reference (minimum three characters), token-creation fields and post-settlement recurring.token.created webhook precede later stored-method ContAuth payments.


- [[source-adyen-docs-payment-methods-dana-flutter-component]] — DANA Flutter Components recurring route: initial settlement precedes recurring.token.created, then stored-method ContAuth and interval-specific processing-model requests; base no-extra-fields wording excludes recurring.


- [[source-adyen-docs-payment-methods-gcash-web-drop-in]] — GCash Web Drop-in guide for `/payments` token fields, settlement-gated recurring-token webhook and subsequent stored-method requests (2026-09-15 snapshot).


- [[source-adyen-docs-payment-methods-momo-wallet-ios-drop-in]] — MoMo iOS Drop-in recurring-token creation, settlement-gated lifecycle webhook and later ContAuth token payment route (2026-09-15 snapshot).


- [[source-adyen-docs-payment-methods-dana-web-component]] — DANA Web Component recurring route: settled initial payment precedes recurring.token.created, then specified stored-method ContAuth requests; base no-extra-fields claim excludes recurring.


- [[source-adyen-docs-payment-methods-gcash-ios-component]] — GCash iOS Components Sessions/Advanced guide with `/payments` token-creation fields, settlement-gated `recurring.token.created` webhook and subsequent stored-method requests (2026-09-15 snapshot).


- [[source-adyen-docs-payment-methods-dana-android-component]] — DANA Android Component recurring route: token ID arrives by recurring.token.created after initial settlement, then specified ContAuth Subscription or UnscheduledCardOnFile payments; examples vary.


- [[source-adyen-docs-payment-methods-upi-upi-autopay-web]] — 2026-09-15 UPI Autopay Web signup and mandate-display guide for Web SDK v6.22.0, Sessions/Advanced mandate fields, Collect/QR/Intent and test/live gates; full recurring backend remains in the API-only guide and examples omit prose-listed fields.


- [[source-adyen-docs-payment-methods-kakaopay-android-component]] — KakaoPay Android Component recurring route: shopper confirms, token ID arrives in recurring.token.created after initial settlement, then specified ContAuth token payments; request examples vary.


- [[source-adyen-docs-payment-methods-upi-upi-autopay-api-only]] — 2026-09-15 UPI Autopay API-only mandate/token, initial approval, 24-hour pre-debit, recurring charge, webhook, retry and cancellation guide; Collect transition, conflicting rule text and sample faults are qualified in the source.


- [[source-adyen-docs-payment-methods-cards-cards-recurring-india]] — 2021-modified India locally acquired recurring-card guide for issuer mandate, pre-debit notification and later token charge; mixed v66/v72 examples, later 48-hour cooling guidance and broad /disable omission effect are qualified in the source.


- [[source-adyen-docs-payment-methods-cards-flutter-drop-in]] — 2026-09-15 Flutter card Drop-in Sessions/Advanced token creation and one-click, subscription and unscheduled examples; explicit-permission advice and storage-setting/mode conflicts remain source-qualified.


- [[source-adyen-docs-payment-methods-cards-android-component]] — Android Card Component v5.0.0+ card-token creation, stored-card display and one-click/subscription/unscheduled example routes; shopper-permission advice and the Advanced storage-switch example conflict remain source-qualified.


- [[source-adyen-docs-standard-integration-drop-in-tokenization]] — 2026-09-15 Standard Drop-in shopper-consented token creation and one-click CardOnFile reuse via Sessions/webhooks, with recurring-role/method gates, zero-value limits and unresolved Ecommerce-versus-ContAuth one-click example.


- [[source-adyen-docs-standard-integration-hosted-checkout-tokenization]] — 2026-09-15 Standard Hosted Checkout CardOnFile token creation and shopper-initiated reuse guide, including consent, lifecycle-webhook token receipt, zero-value limits and an unresolved Ecommerce-versus-ContAuth one-click example conflict.


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
