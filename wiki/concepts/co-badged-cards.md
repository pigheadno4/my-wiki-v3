---
title: "Co-badged Cards Compliance (EU Regulation 2015/751)"
type: concept
category: regulation
tags: [co-badged, cartes-bancaires, girocard, eftpos, eu-regulation, psd2, card-brand-choice]
---

## Definition

Regulation (EU) 2015/751 requires EEA businesses to let cardholders choose which network processes their co-badged card payment (e.g. a Cartes Bancaires card co-badged with Visa).

## Applicability

**Online**: EEA businesses that can process Cartes Bancaires; EUR transactions only.

**In-person**: France (Cartes Bancaires) and Germany (Girocard).

**Countries**: AT, BE, BG, CY, CZ, DE, DK, EE, ES, FI, FR, GR, HR, HU, IE, IS, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK.

## Three Requirements

1. **Display all network logos** clearly and consistently at checkout
2. **Honor the cardholder's choice** — use selected network for confirmation and saving credentials
3. **Allow network updates** — when cardholder updates saved payment method, offer option to change preferred network

## Stripe Integration

Stripe-hosted UIs (Checkout, Payment Links, Elements, Terminal) auto-display network selector when applicable. Connect platforms using `on_behalf_of` must pass `onBehalfOf` to establish merchant of record.

**Web Elements** (`preferredNetwork` / `defaultValues.card.network`): set default network if customer doesn't choose.

**Mobile SDKs** (`preferredNetworks`): iOS 23.22.1+ / Android 20.37.4+ required. For connect: `onBehalfOf` in `IntentConfiguration`.

**Terminal**: WisePad 3, S700/S710 auto-support; Tap to Pay on iPhone requires manual `requested_priority` integration.

## Adyen Web implementation evidence

The retained `@adyen/adyen-web@6.41.0` source includes an accessible dual-brand selector whose options are keyboard-operable buttons with `aria-pressed`. Its Card and Drop-in stories also exercise `splitCardFundingSources`, with separate credit, debit, and prepaid presentation. Credit permits Click to Pay and installments, debit permits Click to Pay without installments, and prepaid permits neither in the retained scenario.

This is version-qualified SDK implementation evidence. It does not independently establish regulatory scope, merchant enablement, or the current Adyen integration procedure.

## Adyen Android implementation evidence

The retained `adyen-android@5.20.0` Card Component performs BIN lookup, exposes detected brand information, and uses `DualBrandData.selectedBrand` when constructing the submitted card payment method. Its retained card delegate also suppresses installment options when the selected funding source is debit.

This proves a version-qualified Android selection and submission path, not current regulatory scope or merchant enablement. The backend response, supported brands, configuration, and shopper card still determine whether the dual-brand path is available.

## Test Cards

| Number | Brand |
| --- | --- |
| 4000 0025 0000 1001 | Cartes Bancaires / Visa |
| 5555 5525 0000 1001 | Cartes Bancaires / Mastercard |

Tokens: `tok_visa_cartesBancaires`, `tok_mastercard_cartesBancaires`

## Sources

- [[source-stripe-co-badged-cards-compliance]] — primary source: regulation scope, integration guides (all Elements, mobile, Terminal), test cards
- [[source-github-adyen-web]] — Adyen Web `6.41.0` dual-brand selector and split-funding-source implementation evidence
- [[source-github-adyen-android]] — Adyen Android `5.20.0` dual-brand selection and submitted-brand evidence
