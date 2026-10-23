---
title: "Adyen React Native Card Component integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/cards/react-native-component/2026-09-15.md"
tags: [adyen, cards, react-native, components, tokenization]
---

## Overview

This [[adyen]] page, captured and last modified 2026-09-15, explains adding cards to an **existing React Native Components** integration. It is a payment-method-specific supplement, not a complete Sessions or Advanced integration guide. Its examples use the `@adyen/react-native` wrapper but do not pin that package's version; see [[adyen-react-native-sdk]] for separately versioned wrapper architecture. The page does not document final payment-result handling, 3DS action callbacks, or PCI assessment for the whole integration.

## Key takeaways

- **Prerequisite and basic start:** The merchant must first build a React Native Components integration and add cards in the **test** Customer Area. The page says cards require no additional card-specific `/payments` fields or required Components integration. Optional `AdyenCheckout` configuration includes holder name, CVC visibility, billing address and lookup callbacks, card brands, region-specific inputs, storage switch, and BIN callbacks. A button example calls `useAdyenCheckout().start('card')`; it depends on the `/paymentMethods` method type and broader integration wiring. See pinned raw lines 19–76.
- **Card presentation:** Checkout API v53+ `splitCardFundingSources: true` in the server-side `/paymentMethods` request can return separate credit and debit card objects; the Netherlands EUR 47 / v72 request is illustrative. Card brand recognition changes icon and security-code field. Co-badged card presentation is described as showing supported brands and shopper choice. The source recommends 3D Secure and automatic capture for debit transactions because of some issuer restrictions and gives a Sweden debit-before-credit note. These are dated, conditional regional recommendations, not proof of current legal or merchant eligibility. See pinned raw lines 79–153.
- **Stored cards and a source conflict:** The page supports one-click, subscription, and unscheduled card-on-file tokenization and strongly recommends explicit shopper permission for future recurring payments. Its prose says to set `showStorePaymentField: true` so the shopper sees a storage switch, while the immediately following configuration snippet sets it to `false`—which the option table says hides that switch. Follow the prose only after checking the intended flow and exact SDK behavior; the snippet is internally inconsistent. The zero-value card-token request uses test-prefixed card placeholders, `storePaymentMethod`, `CardOnFile`, `Ecommerce`, a shopper reference, and server-side `/payments`; token creation is evidenced through a `recurring.token.created` webhook carrying `storedPaymentMethodId`, not the example request alone. See pinned raw lines 155–578.
- **Token-use examples and limits:** The one-click sample supplies a stored-method ID plus encrypted security code, yet uses `shopperInteraction: ContAuth`; keep this as sample wording rather than a general shopper-initiated rule. Subscription and unscheduled examples use the same stored-method ID with their respective `recurringProcessingModel` values. Illustrations use Checkout **test** v72 and several language-library versions; some `storePaymentMethod` samples use string values where typed examples use booleans. These examples do not establish a compatible complete implementation, successful 3DS, authorization, capture, settlement, or payout. See pinned raw lines 185–1643.
- **Test versus LIVE:** The page permits `test_`-prefixed test card details for testing API requests while the client integration is unfinished. Before live card payments it says to test with test cards and add desired cards in the **live** Customer Area. Those steps are not evidence that cards are currently enabled for a merchant or that any live payment succeeded. This page does not set out a full PCI scope or production credential-handling procedure; consult [[adyen-pci-dss-compliance]] for architecture-specific assessment. See pinned raw lines 1645–1653.

## Detail locators

- Requirements, optional Card Component settings and `start('card')` example: pinned raw lines 19–77. Address lookup requires `onUpdateAddress` and `onConfirmAddress` when `addressVisibility=lookup`; `onBinLookup` has an 11-digit minimum, while `onBinValue` returns the first six digits and requires a client key (lines 48–56).
- Debit/credit split, Netherlands example, regional guidance, brand recognition and co-badging: pinned raw lines 79–153.
- Consent advice, storage-switch conflict, zero-value `/payments` token-creation samples and token webhook: pinned raw lines 155–578.
- One-click, subscription and unscheduled stored-card examples: pinned raw lines 580–1643. The one-click curl shows encrypted CVC with `ContAuth` (lines 585–608); no action callback or payment-result sequence is given here.
- Test and live checklist: pinned raw lines 1645–1653.

## Related

- [[adyen-react-native-sdk]] — wrapper and independently versioned native SDK boundaries.
- [[adyen-online-payments]] — broader client/server/webhook integration architecture.
- [[adyen-tokenization]] — consent, shopper reference and token lifecycle.
- [[adyen-3d-secure]] — authentication route; this page only recommends it for some debit cases.
- [[adyen-pci-dss-compliance]] — merchant assessment by actual card-data architecture.

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/react-native-component/2026-09-15|React Native Card Component integration, captured 2026-09-15]]
