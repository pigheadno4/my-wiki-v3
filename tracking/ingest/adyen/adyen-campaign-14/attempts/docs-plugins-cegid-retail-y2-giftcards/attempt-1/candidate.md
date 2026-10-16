---
title: "Adyen Cegid Retail Y2 gift card payment setup"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/cegid-retail-y2/giftcards"
raw_files:
  - "adyen/docs/plugins/cegid-retail-y2/giftcards/2026-09-15.md"
tags: [adyen, cegid-retail-y2, pos, gift-cards, stored-value]
---

## Overview

This Cegid Retail Y2 CPOS plugin guide, marked last modified 2023-04-17 and captured 2026-09-15, describes how to configure gift-card operations, keypad buttons, and a gift-card payment method in Cegid. It is a product-specific configuration procedure, not evidence of a completed activation, an authorized redemption, or merchant/provider availability. See [[adyen-cegid-retail-y2]] for the plugin and [[adyen-pos-gift-cards]] for the separately documented Terminal API gift-card payment flow.

## Key takeaways

- The guide lists activation (optionally loading an initial balance), balance inquiry, cash-out to a credit card, gift-card credit note via referenced or unreferenced refund, redemption for payment, and reloading an activated card. Activation or reloading value is distinct from redeeming it for a payment; this page does not provide a payment authorization result.
- For each desired gift-card operation other than Redemption, configure a Cegid Register Operation with the documented financial-item/credit-request fields and **Send amount to EPT** setting, then assign a keypad button to each operation. The operation table leaves some fields blank; the pinned table governs each operation’s exact configuration.
- To redeem a gift card, create a Cegid payment method using the general plugin setup flow, set its Front-Office **Type** to **Gift card**, add it to the plugin’s payment-method mapping table, then add a gift-card line in the EPT **Payment Configuration** field. The `GCD` code in the guide is an example tied to the code chosen for the Cegid payment method; `GC` denotes the gift-card operation.
- The example EPT line is `GCD:GC,MSE,StoredValueProvider{givex}`. The guide defines `MSE` as magnetic stripe, `SCA` as barcode scanning, and `MKE` as terminal manual key entry; if no entry mode is set, the cashier is prompted to choose one for each gift-card transaction. It lists `svs`, `givex`, and `valuelink` as provider values. These are configuration values, not a guarantee that each provider or entry mode is enabled for a given merchant.
- The page does not specify partial-tender authorization, balance-shortfall handling, gift-card refund eligibility limits, or a CPOS plugin package version. Do not import the generic POS gift-card flow or the separate Cegid setup page’s refund exceptions into this guide without their own evidence.

## Detail locators

- Page identity, snapshot age, supported operation descriptions and three setup stages: pinned raw lines 5–33.
- Register-operation field table and keypad-button setup: pinned raw lines 34–61.
- Gift-card payment method, mapping, EPT line, entry modes and provider values: pinned raw lines 63–97.
- Optional Tap to Pay and Pay by Link navigation: pinned raw lines 99–107.

## Related

- [[adyen]]
- [[adyen-cegid-retail-y2]]
- [[adyen-pos-gift-cards]]
- [[adyen-index]]

## Raw Sources

- [[raw/adyen/docs/plugins/cegid-retail-y2/giftcards/2026-09-15|Cegid Retail Y2 gift-card setup snapshot (2026-09-15)]]
