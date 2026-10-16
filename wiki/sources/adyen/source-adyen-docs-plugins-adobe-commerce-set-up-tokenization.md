---
title: "Adyen Adobe Commerce tokenization setup"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/adobe-commerce/set-up-tokenization"
raw_files:
  - "adyen/docs/plugins/adobe-commerce/set-up-tokenization/2026-09-15.md"
tags: [adyen, adobe-commerce, tokenization, vault]
---

## Overview

This 2023-modified Adyen webpage snapshot describes saving a shopper's payment method through the Adobe Commerce plugin for later use. The shopper-facing **Save for my next payment** checkbox is the stated selection point; the plugin uses **Adobe Commerce Vault to store token information**. Setup and a stored token are not proof of shopper consent for a different use, a future charge, payment authorization, or successful subscription processing. See [[adyen]], [[adyen-magento2]], and [[recurring-payments]].

## Key takeaways

- The page lists card, Google Pay, Apple Pay, SEPA, Klarna, PayPal, iDEAL, Payconiq by Bancontact, and in-person payment tokenization; other methods are a feature-request route, not a supported guarantee (raw lines 19–21). It describes the checkbox during a shopper payment and an **Instant purchase** flow that asks for CVC (lines 23–27). The page provides no exact plugin-version applicability or merchant enablement proof.
- **RECURRING_CONTRACT webhooks** must be enabled in Customer Area (raw lines 29–31). In Adobe Commerce, configure tokenization **per payment method**, enable it, and select `CardOnFile`, `UnscheduledCardOnFile`, or `Subscription` according to intended use (lines 33–49). The page says a later transaction can specify another applicable recurring model; this is not blanket permission to repurpose a shopper credential.
- Stored-card payments default to requiring CVC. Setting **Require CVC for card payments** to **No** needs additional Adyen-side configuration for recurring card processing. **Allow multistore tokens** lets shoppers use tokenized details from a different Magento storefront when set to Yes (raw lines 41–47); the page does not say this crosses shopper or merchant-account identities.
- In the merchant-account Customer Area, the guide enables specified card additional-data fields and **Recurring details** (raw lines 51–68). The optional risk section recommends excluding recurring transactions from risk evaluation and turning off IP-based and velocity risk checks for recurring transactions (lines 70–77). Those changes affect fraud controls and are **optional**, not a tokenization prerequisite.
- Adobe Commerce has no native automatic shopper-not-present transaction functionality, so subscription billing requires additional integration effort (raw lines 79–88). The page maps Vault `shopperReference` to Adobe Commerce `customer_id` and `storedPaymentMethodId` to `gateway_token` (lines 83–86). These stored identifiers are not evidence of a completed or authorized later payment. In-person recurring setup is routed separately (lines 90–92).

## Detail locators

- Intro, `How it works`, and `Requirements`, raw lines 17–31: listed methods, shopper selection, CVC at instant purchase and webhook requirement.
- `Set up the Vault` and `Set up recurring contracts`, raw lines 33–68: per-method model/CVC/multistore settings and merchant-account additional data.
- Optional risk, subscription and in-person sections, raw lines 70–92: fraud-rule changes, non-native automatic subscriptions, Vault field mapping and separate POS route.

## Related

- [[adyen-magento2]] — exact package baseline and plugin lifecycle.
- [[recurring-payments]] — stored-credential use and consent context.

## Raw Sources

- [[raw/adyen/docs/plugins/adobe-commerce/set-up-tokenization/2026-09-15|Set up tokenization, fetched 2026-09-15]]
