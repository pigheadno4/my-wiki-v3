---
title: "Adyen PHP API Library"
type: concept
category: technology
tags: [adyen, php, server-sdk, checkout-api, recurring-api, tokenization-webhooks]
---

## Adyen PHP API Library

The Adyen PHP API Library is a merchant-server SDK for typed access to Adyen APIs. It complements shopper-side Web and mobile SDKs; it does not render checkout UI or prove that a payment method is enabled for a merchant.

## Current baseline

Latest ingested release: `adyen/php-api-library@30.1.0` at `7eda6b3956a61d41a1fb87ab6d4ef30c7d6712cb`, additive full with approved focused reading. The original baseline and every 30.0.2 finding remain preserved below.

The first retained baseline is `adyen/php-api-library@30.0.2` at exact SHA `6ef96571834bc460201df8aea8c89882b2043cd8`. It requires PHP 7.3 or later and includes checkout-focused evidence for Checkout API v71, Payments API v68, Recurring API v68, and Tokenization Webhooks v1.

This is version-qualified implementation evidence. Merchant configuration, API credential roles, geography, shopper context, and backend responses remain authoritative for product and payment-method availability.

## Checkout server surface

Checkout services expose payment methods, payments, payment details, Sessions, modifications, orders, payment links, stored payment methods, donations, and utilities. Generated models cover payment methods, encrypted details, 3D Secure data, actions, recurring processing models, and result codes.

Test usage accepts the shared test endpoint. Live Checkout usage requires the merchant-specific live URL prefix; without it the client deliberately leaves the Checkout endpoint unset.

## Recurring and tokenization

Checkout v71 supports listing and deleting stored payment methods and uses `CardOnFile`, `Subscription`, and `UnscheduledCardOnFile` recurring-processing models. The classic Recurring v68 service remains available for listing or disabling recurring details, notifying shoppers, and scheduling Account Updater. Permit operations are marked deprecated.

Tokenization webhook models and a parser cover created, updated, disabled, and already-existing recurring-token events. Webhook parsing does not replace signature validation or merchant-side event handling.

## Transport and evidence boundary

The client supports API-key and basic authentication, test/live environment selection, timeouts, proxy configuration, custom CA verification, and regional Terminal cloud endpoints. Generated service classes serialize typed requests and deserialize responses.

The retained capsule deliberately focuses on checkout, payment, recurring, tokenization, transport, and signature helpers. The README inventories many other Adyen API families, but detailed questions about those domains require a focused recollection or their own repository evidence.

## Version and query boundary

### 30.1.0 Payments Fields and Client Region Setter

Classic Payments v68 adds `transactionLinkId` to request `AdditionalDataCommon` and response `ResponseAdditionalDataCommon`, including maps, constructor and getter/setter support. The request documentation describes Mastercard MIT chains when Adyen does not tokenize the card, using ContAuth and Subscription or UnscheduledCardOnFile; the response describes the Mastercard TLID. The setter stores the value without enforcing those conditions. This is not a new Checkout v71 field, proof of merchant enablement or a replacement for the existing networkTxReference field. [[source-github-adyen-php-api-library]]

`Client::setRegion(string): void` stores the region configuration and retrieveCloudEndpoint is deprecated, not removed. The setter alone does not update endpoints or validate region support. Full Terminal routing depends on the excluded PosPayment service; Foreign Exchange v1, Payments App and transfer/transaction webhook updates are release-note/README-level coverage, not retained implementation. Detailed non-checkout queries require separately approved exact-SHA collection. Runtime PHP floor remains >=7.3; PHP CodeSniffer 4.0.2 is a development dependency, not evidence of a payment-runtime security fix. Checkout services/models are unchanged. [[changelog-github-adyen-php-api-library]]

### Historical Baseline and Support Evidence

Release `30.0.2` is the first retained exact-SHA baseline, so cumulative behavior must not be described as newly introduced by that patch. Future releases append to the same source page and separate package-qualified changelog. Minor releases can use delta ingest when the changed evidence is bounded; major or broad upgrades use additive full ingest and preserve older version knowledge.

The retained `SECURITY.md` still names `6.x.x` as supported while the package and code identify `30.0.2`. Treat that table as stale contradictory evidence, not current support policy.

The same security table is hash-unchanged at 30.1.0 and remains stale. The deprecated client helper's comment says unsupported regions default to EU, but its live branch actually throws for an unmapped region; do not turn that comment into a fallback guarantee. These qualifications also appear in [[source-github-adyen-php-api-library]].

## Related

- [[source-github-adyen-php-api-library]] - cumulative exact-SHA repository evidence
- [[changelog-github-adyen-php-api-library]] - package-qualified release history
- [[adyen-node-api-library]] - independently versioned Node.js server SDK
- [[recurring-payments]] - cross-provider recurring and stored-credential concepts
- [[adyen]] - company and knowledge-status page
