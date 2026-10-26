---
title: "MobilePay React Native Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mobilepay/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/mobilepay/react-native-drop-in/2026-09-15.md"
tags: [adyen, mobilepay, react-native, drop-in, redirect, payout]
---

## Overview

This [[adyen]] page describes MobilePay-specific additions to an existing React Native Drop-in integration, separately for Sessions and Advanced server-side flows. Both call for redirect handling. It also describes an experimental payout-token path using `/payments`; the page's ordinary Sessions setup does not make that path a Sessions-only feature. See [[adyen-online-payments]]. This dated snapshot does not establish current merchant, country, currency or wallet eligibility, or a successful transaction.

## Key takeaways

- **Sessions:** Requires an existing React Native Drop-in Sessions integration, Checkout API v68 or later, `action.type: redirect` handling, and MobilePay added in Customer Area. It says no MobilePay-specific `/sessions` parameters or Drop-in configuration are needed. The Sessions prerequisite label points to an **Advanced-flow** URL, although the redirect and create-session links point to Sessions. Follow the stated flow and verify the intended base guide. See raw lines 25–48.
- **Advanced:** Requires an existing React Native Drop-in Advanced integration, redirect handling, and MobilePay added in Customer Area. It says no extra MobilePay configuration or ordinary `/payments` parameters are needed, except when a payment creates a future-payout token. The page gives no Advanced-flow Checkout API minimum or React Native package version. See raw lines 85–107.
- **Payment testing and status:** The page says ordinary MobilePay payments cannot be tested in the test environment. It directs a live Customer Area request and low-amount live payments, with payment status checked through the server's `AUTHORISATION` webhook and live Payment list. Redirect completion alone is not proof of authorization. See raw lines 50–60 and 327–337.
- **Experimental payout-token route:** The payout feature is labeled experimental and `/payments`-only. For a payment that creates a future MobilePay-wallet payout token, the page calls for a recurring lifecycle webhook and `telephoneNumber`, `shopperReference` and `enablePayout: true` in the payment request. The token arrives as `storedPaymentMethodId` in that webhook, associated with `shopperReference`; a later `/transfers` request places it in `counterparty.card.cardIdentification`. The separate payout-testing instructions use a Vipps MobilePay test app and do not negate the ordinary-payment live-only warning. See raw lines 62–83 and 293–360.

> [!warning] Payout examples and environment conflict
> The prose says `enablePayout`; the annotated curl example says `enablePayOut`. The Java, PHP, C#, Node, Python and Ruby snippets omit `shopperReference` and the enablement field, while sample currency, method type and return URL are blank. The curl example uses a TEST endpoint despite the page's statement that MobilePay payments cannot be tested in TEST. Read these as incomplete or conflicting examples, not a confirmed normal-payment TEST path or complete working token request. See raw lines 107–290 and 293–303.

## Detail locators

- Sessions requirements, mismatched base-guide URL and method-specific absence of fields/configuration: raw lines 25–48; Advanced equivalents: raw lines 85–107.
- Sample payout-token request snippets: raw lines 109–290; token creation, illustrative webhook and subsequent transfer field: raw lines 293–325.
- Separate ordinary-payment and experimental-payout test instructions: raw lines 50–83 and 327–360. This guide supplies no React Native initialization code, country/currency matrix, or full base-flow result contract.

## Related

- [[adyen-react-native-sdk]] — wrapper architecture and versioned repository evidence; this page pins no wrapper version.
- [[adyen-payouts]] — broader payout and transfer context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/mobilepay/react-native-drop-in/2026-09-15|MobilePay React Native Drop-in, 2026-09-15 snapshot]]
