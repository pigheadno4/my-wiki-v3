---
title: "Adyen Google Pay overview (historical snapshot)"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/google-pay"
raw_files:
  - "adyen/docs/payment-methods/google-pay/2026-09-15.md"
tags: [adyen, google-pay, wallets, online-payments, historical]
---

## Overview

This [[adyen]] Google Pay overview, last modified **2023-09-22** and captured 2026-09-15, describes shoppers selecting a stored credit/debit card in Google's payment sheet for app or website checkout; it also mentions in-store POS use (raw lines 15–25). Its main retrieval route is [[adyen-online-payments]]. The page is a method and integration chooser, not evidence that a merchant is enabled, that a wallet token was processed, or that a payment was authorized, captured or settled.

## Key takeaways

- The snapshot table labels the method **Wallets / Direct / International / Multiple** and checks recurring, refunds and their partial variants, capture variants and chargebacks (raw lines 27–29). Those are catalog marks, not universal country, currency, merchant, network or transaction eligibility. The page separately links Google compatibility lists for payment methods, countries/regions and browsers (raw lines 35–41).
- Supported-network text carries specific conditions: **American Express except India**; **Elo in Brazil** only with a local Brazilian business entity; **Interac in Canada** only with a local Canadian business entity. The page says Interac is automatically captured at authorization (raw lines 43–58). That is this historical method rule, not proof of settlement or an account's capture configuration. The same list also gives region scopes for Accel, Discover, Maestro, Maestro USA, Mastercard, NYCE, PULSE, STAR and Visa (raw lines 47–58).
- The liability-shift section distinguishes **DPAN**, containing a cryptographic value, from **FPAN**, for which the page says Adyen has raw card data after decryption and **recommends** 3D Secure (raw lines 60–66). It attributes a liability-shift guarantee to Google Pay for Mastercard issued globally and Visa issued in the EU/UK **when tokenized as DPAN**; it says FPAN has no Google Pay guarantee and Adyen's API suggests a 3DS redirect for FPAN but not DPAN (raw lines 68–73). For Visa cards issued outside the EU/UK, the page also describes an **opt-in upgrade** that requires additional transaction data and says Adyen APIs support sending those data points (raw lines 72–73). This is a historical option, not universal eligibility or a guaranteed shift. These conditional 2023-modified provider statements do not promise authorization, fraud immunity or present-day chargeback outcomes.
- The liability paragraph names **JCB** among brands without guaranteed shift, though JCB is **not in this page's supported-network list** (raw lines 43–58, 72). The mention cannot be used as evidence of JCB support. Merchant-side Google Pay token decryption is presented only as an option for a **PCI DSS Level 1 compliant merchant**, with detail delegated to a separate guide (raw line 75).
- The page routes to Web, Android, React Native, Flutter, API-only website/Android and in-person guides (raw lines 77–113). It also links a Google Pay Web Component express-payment configuration route (raw lines 31–33). These are navigation links, not child-guide prerequisites, API behavior, current enablement or completed payment evidence.

## Detail locators

- Google Pay card and payment-sheet description: raw lines 15–25.
- Capability marks, express route and compatibility links: raw lines 27–41.
- Network/region/entity conditions and Interac capture statement: raw lines 43–58.
- DPAN/FPAN, 3DS, liability-shift qualifications and Level 1 decryption route: raw lines 60–75.
- Web/mobile/API-only/in-person integration navigation: raw lines 77–113.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods]]
- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-classic-google-pay]] — older inactive Classic route, distinct from this overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/google-pay/2026-09-15|Full pinned Google Pay overview]]
