---
title: "Card Drop-in integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/cards/react-native-drop-in/2026-09-15.md"
tags: [adyen, cards, react-native, drop-in, tokenization, checkout-api]
---

## Overview

This 2026-09-15 [[adyen]] page adds cards to an **existing React Native Drop-in integration**. It documents card-specific options and server Checkout API examples, so the main route is [[adyen-react-native-sdk]]. It does not itself pin a React Native wrapper or native iOS/Android SDK version, describe a complete Sessions flow, or establish payment outcome.

## Key takeaways

- First build the React Native Drop-in integration and add cards in the **test** Customer Area. The page says no extra card-specific API fields or required card-specific Drop-in integration are needed for the basic path; its examples use server-side `/paymentMethods` and `/payments` for additional card and tokenization use cases.
- Optional card settings include holder name, CVC display for new/stored cards, storage choice, address visibility, supported brands, country filters and Korean/Brazilian fields. Address `lookup` requires both `onUpdateAddress` and `onConfirmAddress` callbacks. BIN callbacks are scoped to minimum 11 entered digits for `onBinLookup` and a client key for the first-six-digit `onBinValue`.
- Separate debit/credit methods require Checkout API **v53 or later** and server `/paymentMethods` with `splitCardFundingSources: true`; the NL/EUR 47.00 request and split response are examples. For debit combo cards the page **recommends** 3D Secure and automatic capture because of some issuer restrictions. For Sweden it says `countryCode: SE` yields debit-first Drop-in ordering, which is dated source guidance rather than a current legal determination. Recognition and co-badged choice are client presentation behavior, not authorization.
- Card tokenization covers one-click, subscription and unscheduled card-on-file. It strongly recommends explicit shopper permission for future recurring payments. To show the storage switch, the prose requires `showStorePaymentField: true`, but the adjacent sample sets it to **`false`**, which the configuration table says hides that option. Follow the stated condition, and treat the snippet as conflicting illustration. The test `/payments` token request uses `test_` encrypted-card placeholders; a later `recurring.token.created` webhook carries a `storedPaymentMethodId` for subsequent use. The examples do not prove consent, token creation, successful payment or funds movement.
- Before live card payments, the page directs test-card testing and adding desired cards in the **live** Customer Area. It contains no card-specific PCI assessment or native SDK version pin in this raw; use separately versioned integration and PCI sources for those requirements. A 3DS recommendation is not evidence of authentication, and an API call or token webhook is not authorization, capture or settlement proof.

## Detail locators

- [[raw/adyen/docs/payment-methods/cards/react-native-drop-in/2026-09-15|Pinned raw]], lines 15–36: purpose, prior Drop-in/test Customer Area prerequisites and no-extra-card-field boundary.
- Same raw, lines 38–56: optional configuration, conditional address callbacks, BIN callback limits; lines 58–132: v53 funding-source split, combo-card recommendation, Sweden and brand choice.
- Same raw, lines 134–162: recurring consent, storage-switch prose/example conflict; lines 168–557: test-only token-request illustrations and token-created webhook.
- Same raw, lines 559–919: one-click stored-token examples; lines 920–1271: subscription; lines 1272–1622: unscheduled card-on-file.
- Same raw, lines 1624–1633: test and live Customer Area checklist.

## Related

- [[adyen-tokenization]] — stored credential lifecycle.
- [[adyen-online-payments]] — merchant server, client and payment-outcome context.
- [[adyen-pci-dss-compliance]] — PCI guidance outside this page.

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/react-native-drop-in/2026-09-15|Card Drop-in integration]]
