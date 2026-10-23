---
title: "Adyen API-only encrypted card integration guide"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/custom-card-integration"
raw_files:
  - "adyen/docs/payment-methods/cards/custom-card-integration/2026-09-15.md"
tags: [adyen, cards, online-payments, api-only, encryption, tokenization]
---

## Overview

This [[adyen]] guide, last modified and captured 2026-09-15, covers an **API-only card integration with encrypted card details** across Web and mobile examples. A merchant builds its card-form UI. On Web, Adyen's Custom Card Component collects, validates and encrypts the sensitive inputs inside Adyen-served iframes; the iOS, Android, React Native and Flutter examples collect card details in the merchant app and call client-side encryption. The encrypted payload goes to the merchant server, which calls Checkout `/payments`. These collection architectures have different card-data and PCI implications. See [[adyen-online-payments]], [[adyen-card-encryption]] and [[adyen-pci-dss-compliance]].

## Key takeaways

- **Prerequisites and card selection:** The page calls for an API-only integration and adding intended cards in the **test** Customer Area before starting. It uses `/paymentMethods` with `countryCode` and `amount.currency` to determine cards shown to a shopper; this is a request/response selection step, not proof of live country, currency or merchant eligibility. See pinned raw lines 31–44.
- **Client boundaries:** Web uses the Custom Card iframe fields and a public `clientKey`; the page shows version-specific `AdyenCheckout` initialization (asynchronous in v5.0.0+) and callbacks, then sends `state.data` to the merchant server only when `state.isValid`. It recommends version-matched SRI for script/CSS delivery. Web v5.20.0+ JWE input fields require a secure local or HTTPS test context and allowed origin. The mobile tabs instead show public-key/client-side encryption after the merchant app collects raw card inputs. Neither path makes a copied code snippet a complete, tested card-data integration. See pinned raw lines 21–27, 46–246, 417–627 and 2754–2758.
- **Server request and outcomes:** The server-side `/payments` section lists amount in minor units, unique reference, encrypted `paymentMethod` type `scheme`, merchant account, return URL and risk-data fields. Its return URL must omit personally identifiable information. The illustrated curl request uses the **test** v72 endpoint and `test_` card placeholders; language snippets pin differing API-library versions and show example idempotency keys. A `/payments` resultCode is for shopper presentation, while payment outcome also arrives asynchronously by webhook. `Authorised`, `Cancelled`, `Error` and `Refused` are distinguished; 3DS can add other result codes. Manual capture still requires a separate capture step. Neither response example nor a 3DS authentication step proves capture, settlement or payout. See pinned raw lines 629–1060.
- **Card presentation:** In some regions the page describes co-badged brand choice, including Web `onBinLookup`/selected-brand handling; it separately describes debit/credit presentation with Checkout API v53+ and `splitCardFundingSources`. The Netherlands EUR 47 example is illustrative, while Sweden ordering and Brazil debit 3DS/automatic-capture advice are source-dated regional statements, not a present legal or issuer determination. See pinned raw lines 1062–1230.
- **Stored cards:** The page routes CardOnFile, Subscription and UnscheduledCardOnFile through standard tokenization parameters, recommends explicit shopper permission for future recurring charges, and says token creation yields a `recurring.token.created` webhook containing `storedPaymentMethodId`. A shopper-reference lookup can return stored methods; the one-click branch collects a fresh CVC. The zero-value token-creation and subsequent `/payments` examples are illustrative; a submitted request does not prove token creation or a future charge. Its one-click example combines fresh CVC collection with `shopperInteraction: ContAuth`, while token creation uses `Ecommerce`; keep that sample wording separate from a general rule for shopper-initiated reuse. See pinned raw lines 1231–1705 and 2036–2738.
- **Fraud collection and go-live boundary:** Optional cross-page fraud-data collection is described for Web Drop-in/Components and passed by Custom Card at checkout; its script affects pages where installed. The page separately lists test-card checks, adding cards in the live Customer Area and a PCI assessment/SAQ A submission before live cards. Do **not** apply its broad SAQ A sentence to every architecture: the separately retained [[source-adyen-docs-development-resources-pci-dss-compliance-guide]] distinguishes Web Custom Card SAQ A from raw-card API-only SAQ D and gives a separate mobile API-only scope. Exact merchant architecture and assessment remain necessary; this snapshot does not attest compliance or live enablement. See pinned raw lines 2740–2766 and PCI guide raw lines 135–153, 247–259.

## Detail locators

- Web installation, SRI, environment/client key, callbacks, iframe fields and version gates: pinned raw lines 46–246; styling/brands: lines 248–416.
- iOS/Android/React Native/Flutter collection, public keys and encryption examples: pinned raw lines 417–627.
- `/payments` request fields, test curl and language-specific SDK examples: pinned raw lines 629–1024; response/result/webhook: lines 1026–1060. The Go example labels v12.2.0 but imports `/v9/` packages at lines 859–867; use snippets as illustrations, not verified compatible implementations.
- Co-badging, debit/credit splitting and regional notes: pinned raw lines 1062–1230.
- Token creation, webhook, stored-card lookup, one-click, subscription and unscheduled card-on-file examples: pinned raw lines 1231–2738.
- Optional fraud collection, v5.20.0+ secure-context condition and live checklist: pinned raw lines 2740–2766.

## Related

- [[adyen-online-payments]] — main client/server online-payment route.
- [[adyen-tokenization]] — stored-card lifecycle and shopper permission.
- [[adyen-3d-secure]] — authentication route separate from authorization and capture.
- [[adyen-pci-dss-compliance]] — architecture-specific merchant assessment; no certification inferred here.
- [[adyen-card-encryption]] — distinct custom Web JWE/raw-card route; do not merge it with Adyen-hosted Custom Card iframes.

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/custom-card-integration/2026-09-15|API-only encrypted card integration, captured 2026-09-15]]
