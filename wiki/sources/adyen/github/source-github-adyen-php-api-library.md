---
title: "GitHub: Adyen/adyen-php-api-library"
type: source
date_ingested: 2026-08-20
date_updated: 2026-10-29
original_format: github-repo
raw_files:
  - "github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/manifest.json"
  - "github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/manifest.json"
tags: [adyen, php, server-sdk, checkout-api, recurring-api, tokenization-webhooks, github-repository]
---

## Overview

`Adyen/adyen-php-api-library` is Adyen's official PHP server library. This cumulative page begins with package-qualified release `adyen/php-api-library@30.0.2` at exact SHA `6ef96571834bc460201df8aea8c89882b2043cd8`. The checkout-focused capsule provides detailed evidence for Checkout API v71, Payments API v68, Recurring API v68, tokenization webhooks, transport, and signature helpers.

Repository: <https://github.com/Adyen/adyen-php-api-library>

Latest ingested Composer release is `adyen/php-api-library@30.1.0` at `7eda6b3956a61d41a1fb87ab6d4ef30c7d6712cb`. Its additive full baseline below preserves every 30.0.2 section and boundary above/below; the collection alias is `adyen-php-api-library@30.1.0`, not a second independently versioned package.

## Evidence boundary

- The approved 30.1.0 full ingest uses focused reading: all six changed retained files, affected prior comparison context, release notes and cumulative wiki history; unchanged source/generated manifests/duplicated inventories were mechanically verified. Current/prior capsules each retain 447 files, six modified/441 unchanged; all 894 sizes/SHA-256/Git blob identities pass. Effective full assignment is 456 paths/7,513,409 bytes. All 45 upstream changes have dispositions (six retained/39 exclusions), with no packet gaps/unclassified changes. Excluded Foreign Exchange, Payments App, transfer/transaction/management webhook and PosPayment implementation is not full-file evidence. No Composer install, PHP/Terminal/payment execution, supplement or future-policy expansion.
- The snapshot proves implementation retained at `adyen/php-api-library@30.0.2`; it does not prove merchant eligibility, credential roles, geography, or payment-method availability.
- The 447-file capsule retains checkout, payment, recurring, tokenization-webhook, client, transport, validation, and utility implementation. Tests and fixtures are intentionally excluded.
- The README inventories broader API and webhook families whose generated model trees were not retained. Detailed non-checkout questions require focused recollection.
- This is server-library evidence. Shopper presentation and action behavior remain in independently versioned Web, iOS, Android, or React Native SDK histories.

## Grounding excerpts

> "This is the officially supported PHP library for using Adyen's APIs."
>
> `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/files/README.md:5`

> "PHP 7.3 or later"
>
> `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/files/README.md:56`

> "For live please specify the unique identifier."
>
> `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/files/src/Adyen/Client.php:124-129`

> "Adyen sends webhooks to inform you about the creation and changes to the recurring tokens."
>
> `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/files/README.md:48`

## Package and client setup

The Composer package is `adyen/php-api-library@30.0.2`. It requires PHP 7.3 or later plus `ctype`, `curl`, `json`, `mbstring`, and `openssl`; the README also calls for cURL with SSL support. Version `6.3.0` is named only as the legacy choice for PHP 7.2 or lower.

A merchant configures `Client` with an API key or basic credentials, environment, request and connection timeouts, proxy, custom CA path, application identity, and optional regional Terminal cloud routing. The cURL transport verifies peer and hostname certificates, serializes JSON requests, supports GET, POST, PATCH, and DELETE, and promotes `requestOptions.idempotencyKey` to the `Idempotency-Key` header.

Test Checkout requests use the shared test endpoint. Live Checkout requests require the merchant-specific live URL prefix from the Customer Area. If live is selected without that prefix, the client sets the Checkout endpoint to `null` rather than falling back to a generic live Checkout URL.

## Checkout API v71

The generated Checkout service exposes these groups:

| Group | Retained operations |
| --- | --- |
| Payments | payment methods, payments, payment details, Sessions and session result, card details |
| Modifications | cancel, capture, refund, reversal, and authorization amount update |
| Orders | create, cancel, and gift-card balance check |
| Payment links | create, retrieve, and update |
| Recurring | list and delete stored payment methods, plus forwarding |
| Donations | list campaigns and submit donations |
| Utility | Apple Pay session, origin keys, PayPal order update, and shopper validation |

Generated models cover cards and many alternative payment methods, encrypted payment details, 3D Secure and authentication data, shopper actions, payment responses, orders, links, installments, recurring processing, and modifications. Model presence proves a typed request or response contract, not merchant enablement or that the method will appear for a shopper.

The merchant backend still owns trusted amount and order state, idempotency strategy, response persistence, action continuation, and final fulfillment decisions. A payment response or action model alone is not proof of final payment success.

## Classic Payments and Recurring APIs

The retained Payments API v68 supports authorization, 3D Secure and 3DS2 authorization, authentication-result retrieval, capture, cancel, refund, cancel-or-refund, donation, technical cancel, and authorization adjustment. These classic operations coexist with Checkout v71 and should not be confused with the Checkout endpoint family.

Recurring API v68 supports listing and disabling recurring details, shopper notification, and Account Updater scheduling. Create-permit and disable-permit methods are explicitly deprecated at v68. Checkout's stored-payment-method operations and recurring processing models are the stronger evidence for current checkout-oriented token use, while the classic service remains relevant to legacy recurring details.

## Tokenization webhooks and signatures

Tokenization Webhooks v1 models cover created, updated, disabled, and already-existing recurring-token events with merchant account, shopper reference, stored payment method ID, event ID, environment, and timestamp data. `TokenizationWebhookParser` maps payloads into the corresponding typed notification model.

`HmacSignature` validates full-payload signatures for banking and management webhooks and field-based signatures for payment notifications. `WebhookReceiver` can enforce payment-notification HMAC and basic authentication using constant-time comparisons. The merchant must still verify the correct signature mode, acknowledge accepted events, make processing idempotent, and avoid treating receipt as business completion.

## Broader API inventory

The README also lists account, balance-platform, BIN lookup, disputes, fund, hosted onboarding, legal-entity, management, payout, stored-value, transfer, and multiple webhook families. This capsule preserves their existence and README-listed versions only. Implementation-level queries outside the retained checkout focus should trigger a temporary clone or focused immutable supplement.

## `30.0.2` release finding

Release `30.0.2` updates generated Stored Value services and models, removes a PHP 8.5 `curl_close()` deprecation path, converts deprecations to errors in project quality checks, and updates development dependencies. A generated Payments update was reverted before release, so the release notes do not establish a net new Payments API behavior.

> [!warning] Contradiction
> The package metadata, `VERSION`, and `Client::LIB_VERSION` identify `30.0.2`, but the retained `SECURITY.md` says only `6.x.x` is supported and `5.x.x` is not. That table is stale relative to the exact release and must not be used as current support-policy evidence.

This is the first retained exact-SHA baseline. All broader sections above describe cumulative implementation present at `30.0.2`, not features introduced by that patch.

## `30.1.0` Additive Full Ingest

**Identity and preservation:** Composer package `adyen/php-api-library@30.1.0`, collection ID `adyen-php-api-library@30.1.0`, tag v30.1.0, SHA `7eda6b3956a61d41a1fb87ab6d4ef30c7d6712cb`. Published September 24, 2026 at 11:38:44 UTC; collected and ingested October 29. All 30.0.2 architecture, implementation, release attribution and stale-security-table findings remain intact. Full mode was explicitly approved; a generated security-review flag is not proof of an exploitable payment-runtime vulnerability.

### Classic Payments Transaction Link Identifier

`Adyen\Model\Payments\AdditionalDataCommon` and `ResponseAdditionalDataCommon` add string `transactionLinkId`, with attribute/type/nullable maps, constructor initialization and getters/setters. The wire key is transactionLinkId. The request documentation describes linking Mastercard subscription/card-on-file transactions when Adyen does not tokenize the card: submit the original contract transaction identifier for subsequent MIT charges, with shopperInteraction=ContAuth and recurringProcessingModel=Subscription or UnscheduledCardOnFile. The response documents Mastercard's Transaction Link Identifier (TLID).

The field's setter only assigns the container value; it does not validate the identifier, enforce those business conditions or make the field mandatory on every request. The generator marks it non-nullable, initializes missing values to null and omits null entries from toArray; this is not a universal required-field check. Existing networkTxReference remains with its Mastercard Trace ID/Visa Transaction ID description. Do not equate the identifiers, infer replacement/removal or project this addition onto Checkout API v71. The exact retained Checkout service/model files are unchanged.

### Client Region Configuration and Its Limit

`Client::setRegion(string $region): void` is new and writes config key region. Config is a plain key-value store; this setter neither validates supported regions nor rewrites endpoints. retrieveCloudEndpoint is deprecated, not removed; its duplicate live-environment condition is simplified without changing the existing throw for unmapped live regions. setEnvironment still consults terminalApiRegion and writes terminalApiCloudEndpoint, whereas the release notes describe PosPayment consuming region and setting endpointTerminalCloud. The latter service is excluded from the capsule. These distinct keys/path responsibilities are not enough to prove the complete new routing flow or prescribe call ordering; obtain an approved exact-SHA supplement for a detailed Terminal integration. This is not a change to merchant-specific live Checkout URL prefixes.

> [!warning] Contradiction
> The deprecated helper's comment says null or unsupported regions default to EU. Its actual live branch defaults null to EU but throws for an unmapped non-null region. This discrepancy predates 30.1.0 in the affected prior code; preserve it rather than advertise a new fallback behavior. The related concept [[adyen-php-api-library]] carries the same qualification. The unchanged SECURITY.md support table remains stale at 30.1.0 as described in the historical baseline.

### Broader Announcements and Security Scope

Release notes and the README add Foreign Exchange API v1 for amount/rate calculation; notes name ForeignExchange RatesApi::calculate. Notes also describe Payments App subMerchantData; transfer networkReason/tracing data, reversalReceived/fxSell/fxBuy and removal of adviceAuthorised/adviceRefused; card networkVariant additions to transfer/transaction webhooks; and a Management Webhooks documentation clarification. These are explicitly announcement/inventory-level findings: their excluded implementations, detailed validation and compatibility are not established by this capsule. They are separate API families, not additions to retained Tokenization Webhooks or checkout presentation.

composer.json changes only development PHP CodeSniffer 4.0.1 -> 4.0.2; the notes attribute it to a security fix. Runtime requirements remain PHP >=7.3 and the same extensions. No production dependency upgrade, resolved dependency graph, exploit analysis or payment-runtime security fix is proven. SECURITY.md is unchanged. Existing source coverage, API families, signatures and merchant-fulfillment responsibilities remain version-qualified rather than rewritten as newly introduced features.

### Located Grounding Excerpts

All locations are under `raw/github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/files/`:

- `src/Adyen/Client.php:182`: `public function setRegion(string $region): void`
- `src/Adyen/Client.php:184`: `$this->config->set('region', $region);`
- `src/Adyen/Model/Payments/AdditionalDataCommon.php:977`: `public function setTransactionLinkId($transactionLinkId)`
- `src/Adyen/Model/Payments/ResponseAdditionalDataCommon.php:2373`: "This contains the Mastercard Transaction Link Identifier (TLID)."
- `composer.json:23`: `"squizlabs/php_codesniffer": "4.0.2"`

**Ingest scope:** changed retained files fully read, including both complete generated Payments models; affected prior code reviewed through the retained old/new comparison, plus unchanged Config/Region dependencies read for the client boundary. Full mode remains additive under the approved focused exception, not a fresh 447-file semantic read. Existing PHP concept updated first; no new source/concept or cross-company comparison. All older raw references and source_count remain unchanged. No SDK/API/Terminal/payment execution, commit or push.

## Related

- [[changelog-github-adyen-php-api-library]] - package-qualified release ledger
- [[adyen-php-api-library]] - PHP server SDK concept and query boundary
- [[adyen-node-api-library]] - independent Node.js server SDK evidence
- [[source-github-adyen-web]] - browser checkout implementation
- [[recurring-payments]] - cross-provider recurring concepts
- [[adyen]] - company and knowledge-status page

## Raw sources

- Snapshot manifest: `raw/github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/manifest.json`
- Release manifest: `raw/github/adyen/adyen-php-api-library/releases/adyen-php-api-library/30.1.0/2026-10-29/manifest.json`
- Release notes: `raw/github/adyen/adyen-php-api-library/releases/adyen-php-api-library/30.1.0/2026-10-29/release-notes.md`
- Comparison: `tracking/github/repos/adyen/adyen-php-api-library/comparisons/adyen-php-api-library/30.0.2--30.1.0/comparison.json` - adjacent comparison.md/diff.patch
- Client: `raw/github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/files/src/Adyen/Client.php`
- Configuration/region dependencies: `raw/github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/files/src/Adyen/Config.php` and `raw/github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/files/src/Adyen/Region.php`
- Request model: `raw/github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/files/src/Adyen/Model/Payments/AdditionalDataCommon.php`
- Response model: `raw/github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/files/src/Adyen/Model/Payments/ResponseAdditionalDataCommon.php`
- Package metadata: `raw/github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/files/composer.json`
- Snapshot manifest: `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/manifest.json`
- Release manifest: `raw/github/adyen/adyen-php-api-library/releases/adyen-php-api-library/30.0.2/2026-08-19/manifest.json`
- Release notes: `raw/github/adyen/adyen-php-api-library/releases/adyen-php-api-library/30.0.2/2026-08-19/release-notes.md`
- README: `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/files/README.md`
- Client: `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/files/src/Adyen/Client.php`
- cURL transport: `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/files/src/Adyen/HttpClient/CurlClient.php`
- Checkout services: `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/files/src/Adyen/Service/Checkout/`
- Payments services: `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/files/src/Adyen/Service/Payments/`
- Recurring service: `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/files/src/Adyen/Service/RecurringApi.php`
- Tokenization parser: `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/files/src/Adyen/Service/TokenizationWebhookParser.php`
- HMAC helper: `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/files/src/Adyen/Util/HmacSignature.php`
- Security policy: `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/files/SECURITY.md`
