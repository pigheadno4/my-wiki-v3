---
title: "Adyen PayPo React Native Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypo/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paypo/react-native-drop-in/2026-09-15.md"
tags: [adyen, paypo, react-native, drop-in, redirect, capture]
---

## Overview

This 2026-09-15-captured Adyen guide describes PayPo-specific additions to an existing React Native Drop-in integration, with Sessions and Advanced server-side flows. Its examples use PL/PLN and the Advanced request uses `paymentMethod.type=paypo`. The page does not establish current merchant eligibility, a completed payment or live activation. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions flow:** Requires an existing React Native Sessions Drop-in integration, Checkout API v68 or later, and PayPo added in Customer Area. The `/sessions` table marks shopperName with first and last names and shopperEmail required; billing and delivery addresses are listed without required marks. The requirement's base-flow link is inconsistent with its Sessions label, as noted below (pinned raw lines 25–48).
- **Advanced flow:** Requires an existing React Native Advanced Drop-in integration, handling an additional `action.type=redirect`, and PayPo added in Customer Area. Its `/payments` table marks method type `paypo`, shopperName and shopperEmail required, while billing and delivery addresses have no required marks. The sample response is `RedirectShopper` with a redirect action, a next shopper step rather than final authorization (lines 443–473, 845–859).
- Both sections say no PayPo-specific Drop-in configuration parameters are needed (lines 423–427, 455–459). This does not waive the main integration's configuration.
- Before authorization, the PayPo offer/link remains available for up to **72 hours**. When the shopper accepts, status becomes Authorised and the shopper's **30-day** payment term begins at authorization. The merchant then must capture; only the **full authorized amount** may be captured. The page says automatic capture can be configured immediately after authorization in live Customer Area and merchant funding follows capture without waiting for shopper repayment to PayPo (lines 391–421, repeated 861–891).
- Testing uses the guide's sample name/email and verification code 123456. Before live acceptance, a PayPo request must be submitted in the live Customer Area (lines 429–441, 893–905).

> [!warning] Sessions link and return URL examples
> The Sessions requirement names a Sessions React Native Drop-in integration but links to `advanced-flow` (raw line 33); its create-session link points to `sessions-flow` (line 41). The Sessions examples use an app-scheme returnUrl, while Advanced examples use an HTTPS checkout returnUrl (lines 66, 494). Treat these as example values and follow the chosen React Native base flow for actual redirect-return configuration.

## Detail locators

- Sessions prerequisites and request fields/examples: pinned raw lines 15–389.
- Sessions capture lifecycle, configuration and test/live: lines 391–441.
- Advanced prerequisites, fields and examples: lines 443–859.
- Advanced capture lifecycle and test/live: lines 861–905.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-paypo]] — PayPo method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypo/react-native-drop-in/2026-09-15|PayPo React Native Drop-in guide, captured 2026-09-15]]
