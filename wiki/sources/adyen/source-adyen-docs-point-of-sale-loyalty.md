---
title: "Adyen Docs: Shopper loyalty at point of sale"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/loyalty"
raw_files:
  - "adyen/docs/point-of-sale/loyalty/2026-09-15.md"
tags: [adyen, point-of-sale, loyalty, shopper-recognition, customer-profiles]
---

## Overview

This Adyen POS loyalty overview describes recognizing shoppers from data returned in card-acquisition and payment responses, without requiring a physical loyalty card. A merchant can use that recognition to offer tailored benefits or recommendations and can enroll an unrecognized shopper at a payment terminal. The merchant creates and maintains customer profiles in its own backend. This dated overview does not define a complete identity, consent, security, account-permission, payment, or loyalty-program lifecycle. [[adyen]] [[adyen-pos-loyalty]]

## Key takeaways

- Recognition is based on data received in card-acquisition and payment responses. If a shopper is recognized, the page suggests on-the-spot discounts or recommendations based on purchase history; if not, it says the shopper can be enrolled at the terminal. These are possible merchant loyalty actions, not automatic terminal behavior or a guaranteed identification match. See **Shopper loyalty**, pinned raw lines 15–21.
- The merchant needs backend customer profiles containing whichever response data it uses for recognition and other use-case data, such as purchase history. The overview does not say Adyen hosts or synchronizes a unified customer profile across channels. See pinned raw line 23.
- The page routes to two distinct child topics. **Card and shopper identifiers** mentions shopper reference and email supplied with requests plus the payment card's **card alias**. **NFC wallet pass data** concerns loyalty account data linked to a merchant-created digital pass the shopper can add to an NFC wallet. The page does not equate a wallet pass with a payment token, raw PAN, or online-checkout identity. See **Next steps**, pinned raw lines 25–35.
- This hub does not describe consent collection, privacy or retention rules, card-data handling, SCA, account permissions, enrollment fields, identifier stability, response-field availability, discount application, or payment authorization. Those controls and behaviors require the relevant child guides and merchant-specific review before implementation. See complete pinned raw lines 15–35.

## Detail locators

- **Shopper loyalty** (pinned raw lines 15–23) — POS recognition source, conditional benefits/enrollment, and merchant backend profile responsibility.
- **Next steps → Card and shopper identifiers** (pinned raw lines 25–31) — navigation to request-supplied shopper reference/email and card-alias details.
- **Next steps → NFC wallet pass data** (pinned raw lines 33–35) — navigation to digital-pass-linked loyalty account data.

## Related

- [[adyen-pos-loyalty]] — primary POS loyalty and recognition route.
- [[adyen-terminal-api]] — separate terminal-message context; this overview does not specify request or response fields.

## Related raw API references

These child guides are navigation targets in this overview; their detailed behavior has not been read for this entry:

- Card and shopper identifiers — https://docs.adyen.com/point-of-sale/loyalty/payment-data
- NFC wallet pass data — https://docs.adyen.com/point-of-sale/loyalty/wallet-passes

## Raw Sources

- [[raw/adyen/docs/point-of-sale/loyalty/2026-09-15|Adyen POS shopper-loyalty overview, fetched 2026-09-15]]
