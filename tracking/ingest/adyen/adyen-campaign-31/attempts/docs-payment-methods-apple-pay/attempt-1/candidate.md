---
title: "Adyen Apple Pay overview (web, app and in-person routes)"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/apple-pay"
raw_files:
  - "adyen/docs/payment-methods/apple-pay/2026-09-15.md"
tags: [adyen, apple-pay, wallets, payment-methods, certificates]
---

## Overview

This [[adyen]] Apple Pay overview is a payment-method and integration-route page, captured 2026-09-15. It describes shopper selection of a card and contact/shipping details in the Apple Pay sheet followed by Face ID or Touch ID authentication, and routes merchants to web, iOS, React Native, Flutter, API-only, and in-person guides. Authentication and a listed integration route do not establish payment authorization, capture, settlement, or merchant enablement. The page metadata says last modified 2023-05-08, though its body includes an Eftpos date of 5 Jan 2026; the snapshot does not explain that mismatch. See [[adyen-online-payments]].

## Key takeaways

- The overview describes Apple Pay as a network-tokenized wallet for in-app, in-store and web use. It states that a Europe implementation is PSD2 SCA-compliant; treat this as the page's dated provider claim, not a merchant-specific compliance determination. See raw lines 23–25.
- Its liability-shift statement is conditional: the named networks are American Express, Discover, JCB, Mastercard and Visa; for Visa, the page says global application at iOS 16.2+, versus cards issued in Europe at iOS 16.1 or below. It excludes Mexican-card transactions processed through Prosa. The page also says China UnionPay is not supported through Adyen Apple Pay in this snapshot. See raw lines 27–34.
- The support table marks recurring, refunds, partial/multiple refunds, separate/partial/multiple captures and chargebacks, but these are overview capability marks, not enabled merchant features or completed financial operations. Actual use depends on method, account and transaction conditions in the relevant guides. See raw lines 36–38.
- Shopper availability depends on supported issuer, device/browser and country/region, plus a card already added to the Apple Pay wallet. The network list has country-specific entries; Eftpos in Australia, Elo in Brazil and Interac in Canada additionally state local-business-entity conditions. The page says Eftpos and Interac are automatically captured at authorization, a named-network condition rather than a general Apple Pay capture rule. See raw lines 44–78.
- Processing requires an Apple Pay certificate. For a web integration, the page offers Adyen's certificate; for a mobile integration, it says the merchant needs its own Apple Developer account and certificate with extra configuration. This overview does not document live certificate creation or token-decryption responsibility. See raw lines 80–82; follow the linked certificate and channel guides for those tasks.

## Detail locators

- Shopper sheet/authentication and dated SCA statement: raw lines 23–25.
- Liability-shift conditions, Prosa exclusion and China UnionPay limitation: raw lines 27–34.
- Capability table and express Web Component navigation: raw lines 36–42.
- Compatibility and supported-network geography/entity/capture qualifications: raw lines 44–78.
- Certificate split and channel-specific guide routes: raw lines 80–120.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/apple-pay/2026-09-15|Apple Pay overview, 2026-09-15 capture]]
