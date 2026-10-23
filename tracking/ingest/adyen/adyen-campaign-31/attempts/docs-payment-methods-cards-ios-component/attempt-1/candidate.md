---
title: "Adyen Card Component for iOS"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/ios-component"
raw_files:
  - "adyen/docs/payment-methods/cards/ios-component/2026-09-15.md"
tags: [adyen, cards, ios, components, online-payments, tokenization]
---

## Overview

This [[adyen]] guide, modified and captured 2026-09-15, adds the Card Component to an **existing iOS Components integration**. It distinguishes server-side **Sessions** and **Advanced** flows; both require cards added in Customer Area. It covers card form configuration, debit/credit separation, brand choice, tokenization and installments. The examples are test-environment illustrations across multiple Checkout API and server-library versions, not a single verified integration or proof of live merchant eligibility, PCI status, authorization, capture or settlement. See [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- The page says no extra card-specific fields are needed for the basic API request. It calls `/sessions` the default with **iOS Components v5.0.0 or later** and routes additional-use-case `/payments` requests separately. Its v5+ card configuration object and v4.x no-required-card-specific-integration wording differ; optional cardholder, CVC, billing-address and regional fields are versioned form options, not an unconditional requirement to collect them. See raw lines 21–95.
- Debit and credit forms can be separated with server-side `splitCardFundingSources: true` in `/sessions`, or in Advanced `/paymentMethods` with **Checkout API v53+**. The Netherlands/EUR test requests are examples. For combo-card debit transactions the page **recommends** 3D Secure and automatic capture; its Sweden section says `countryCode: SE` displays Debit Card first. These are scoped page statements, not a legal determination or evidence of authentication or capture. See raw lines 97–197.
- While a shopper enters card details, the Component attempts brand recognition and renders the corresponding security-code field when successful. For applicable co-badged cards the page says it displays supported brands and lets the cardholder choose. This form behavior does not itself validate an authorization. See raw lines 199–205.
- Cards route to one-click, subscription and unscheduled card-on-file tokenization. The page **strongly recommends** explicit shopper permission for future recurring payments; it does not phrase that recommendation as a universal API rule. Sessions tokenization is stated as supported from Components v5.0.0; the example `/sessions` request uses `storePaymentMethodMode: askForConsent`, while several language-library examples use `enabled`. For Checkout API v69 or earlier it points to `enableStoreDetails` to show a storage checkbox. A created-token webhook supplies `storedPaymentMethodId`; token creation, shopper consent and later payment outcomes remain distinct. See raw lines 207–542.
- Advanced flow is described as default for Components v4.10.0 and earlier. Its instructions say set `showsStorePaymentMethodField` **true** to show a shopper checkbox, but the adjacent Swift example sets it **false**. Do not copy that snippet as proof of a consent-enabled UI. The `didSubmit` text says a selected checkbox contributes `data.storePaymentMethod` to the payment request. Advanced examples include `test_` encrypted-card placeholders and test endpoints; these are not production card-data handling instructions. See raw lines 847–888 and 1259–1282.
- The Advanced stored-card route uses the same `shopperReference` in `/paymentMethods`, takes `StoredCardPaymentMethod` from the response's `stored` array, and passes it into the Card Component. The later one-click, subscription and unscheduled examples distinguish `CardOnFile`, `Subscription` and `UnscheduledCardOnFile`; they show token IDs and server `/payments` requests, not successful payments. See raw lines 1264–2347.
- Installments differ by version: v5+ describes `/sessions` `installmentOptions` with a required `values` row and optional `preselectedValue`/`plans`; v4.x describes `InstallmentOptions` and `InstallmentConfiguration`. The v4 `maxInstallmentMonth` prose says options start at 2, then its example includes 1, so the minimum option is unresolved in this snapshot. See raw lines 2349–2409. Before live card payments the page calls for test-card testing, live Customer Area card setup, PCI DSS assessment and submission of Self-Assessment Questionnaire A. Test `test_` details or local validation do not establish those steps were completed. See raw lines 2411–2421.

## Detail locators

- **Flow prerequisites, API endpoint selection, iOS v5/v4 configuration and optional fields:** raw lines 21–95.
- **Funding-source split, combo cards, Sweden, brand and co-badged behavior:** raw lines 97–205.
- **Sessions token creation, shopper-permission recommendation, API-v69 checkbox path and one-click examples:** raw lines 207–846.
- **Advanced storage-checkbox conflict, test placeholders, token webhook and stored-card UI:** raw lines 847–1282.
- **Advanced token payment examples by recurring model and server-library versions:** raw lines 1284–2347.
- **Installment version branches, example conflict, testing and live prerequisites:** raw lines 2349–2421.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-pci-dss-compliance]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/ios-component/2026-09-15|Adyen iOS Card Component guide — captured 2026-09-15]]
