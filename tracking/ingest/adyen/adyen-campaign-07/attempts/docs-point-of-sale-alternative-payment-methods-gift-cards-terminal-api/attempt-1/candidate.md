---
title: "Adyen Docs: Gift cards and other stored value cards at point of sale"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/alternative-payment-methods/gift-cards-terminal-api"
raw_files:
  - "adyen/docs/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/2026-09-15.md"
tags: [adyen, point-of-sale, gift-cards, stored-value, terminal-api]
---

## Overview

This Adyen POS overview covers Terminal API transactions with stored-value cards such as gift cards and mall cards. It introduces setup, card-entry and PIN options, the boundary between Terminal API and Stored Value API, mall-card issuer onboarding, and a provider-by-operation matrix that routes to individual lifecycle guides. The page was last modified in 2025 and captured on 2026-09-15; its support matrix and operational steps are historical documentation, not current provider/account enablement or payment proof. [[adyen]] [[adyen-pos-gift-cards]]

## Key takeaways

- The guide requires a Terminal API integration with payment terminals, adding the method to the Adyen account, completing gift-card-provider onboarding, and contacting Adyen Support to enable specific PIN options. It says Adyen may request more details before configuring gift-card functionality. These are POS requirements; the page does not establish online checkout payment behavior. See **Requirements**, pinned raw lines 21–31.
- Stored Value API can substitute for Terminal API requests whose `MessageCategory` is `StoredValue`, such as activation through `/changeStatus`; it cannot make payments. The page describes using Terminal API for gift-card payments, including cash-outs, and refunds while optionally using Stored Value API for management operations across POS and ecommerce channels. A shared management route does not make POS and ecommerce payment flows interchangeable. See **Terminal API or Stored Value API**, pinned raw lines 33–40.
- The POS card details may be obtained by scanning with a POS-linked barcode scanner, swiping on the terminal, or manually keying on the terminal. The request must identify the entry method; scanned details are supplied by the POS, whereas swipe/keyed details are collected after the terminal request. See **Card entry methods**, pinned raw lines 42–48.
- If a card has a PIN or other security code, the terminal prompts the shopper. Support-enabled **PIN entry override** can vary prompts by interaction, entry mode, and brand. **Store PIN** caches a PIN after first entry for a configured 25-second to 30-minute interval and clears it when another payment or gift card is presented. These are specific options, not universal PIN treatment or a recommendation to enable caching. See **PIN options**, pinned raw lines 50–55.
- Co-badged mall/one4all cards use their Mastercard or Visa scheme. The guide says to provide the issuer the scheme MID for each intended store so it can allow the store; the issuer may need more store details. Viewing MIDs in the live Customer Area requires the **View Acquiring Details** role, and MIDs are store- and scheme-specific. This onboarding statement does not prove that a particular card will be accepted. See **Mall cards / Send MIDs to the card issuer**, pinned raw lines 57–86.
- The snapshot matrix lists Givex, SVS, Fiserv (formerly ValueLink), Intersolve, and local gift cards. In its table, the four named global providers support activation, payment, balance, load, load reversal, refund and cash-out; **deactivation is shown only for Givex**. Local-provider cards are listed for payments only, in Denmark, France, the Netherlands, Norway, Sweden and the UK. These are dated table entries, not current support promises or method-specific transaction instructions. See **Supported gift cards and transactions**, pinned raw lines 88–103.

## Detail locators

- **Gift cards and other stored value cards / Requirements** (pinned raw lines 15–31) — stored-value scope, Terminal API integration, account/provider setup and PIN-support route.
- **Terminal API or Stored Value API** (pinned raw lines 33–40) — operation-category substitution and payment prohibition for Stored Value API.
- **Card entry methods / PIN options** (pinned raw lines 42–55) — scan/swipe/MKE ownership and PIN prompt/cache controls.
- **Mall cards / Send MIDs to the card issuer** (pinned raw lines 57–86) — scheme co-badging, per-store/scheme MID, live Customer Area role and issuer onboarding.
- **Supported gift cards and transactions** (pinned raw lines 88–103) — provider-operation matrix, Givex-only deactivation, and local-provider payment-only row.
- **Next steps** (pinned raw lines 105–123) — activation, payment, load and refund child-guide navigation.

## Related

- [[adyen-pos-gift-cards]] — POS gift-card lifecycle and provider boundary.
- [[adyen-terminal-api]] — terminal message categories and request context.
- [[adyen-pos-alternative-payment-methods]] — broader POS method-family route.

## Related raw API references

The following are child routes named by the overview; their behavior is not independently established by this entry:

- Gift-card activation — https://docs.adyen.com/point-of-sale/gift-cards-terminal-api/activate
- Gift-card payment — https://docs.adyen.com/point-of-sale/gift-cards-terminal-api/payment
- Load funds — https://docs.adyen.com/point-of-sale/gift-cards-terminal-api/load-a-balance
- Refund to a gift card — https://docs.adyen.com/point-of-sale/gift-cards-terminal-api/refund-gift-cards
- Stored Value API — https://docs.adyen.com/payment-methods/gift-cards/stored-value-api

## Raw Sources

- [[raw/adyen/docs/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/2026-09-15|Adyen POS stored-value card overview, fetched 2026-09-15]]
