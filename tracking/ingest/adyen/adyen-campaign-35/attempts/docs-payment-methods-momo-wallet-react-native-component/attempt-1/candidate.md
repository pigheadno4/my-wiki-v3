---
title: "MoMo React Native Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/momo-wallet/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/momo-wallet/react-native-component/2026-09-15.md"
tags: [adyen, momo, react-native, components, online-payments, recurring-payments]
---

## Overview

This [[adyen]] snapshot, captured 2026-09-15, gives MoMo-specific additions for an **existing React Native Components** integration on the **Advanced flow**. Its frontmatter and H1 say "MoMo React Component," but the canonical path and integration requirement specify React Native; this source entry uses the narrower React Native identity. It is a method-specific add-on, not a complete app integration or proof of current Vietnam/VND eligibility, live enablement, authorization, capture, settlement or token creation. See [[adyen-online-payments]] and raw lines 6–23, 25–41.

## Key takeaways

- **Sessions flow is explicitly unavailable** for React Native Components on this page. For **Advanced**, prerequisites are an existing React Native Components integration, redirect handling for `action.type: redirect`, and adding MoMo in Customer Area. The Advanced "Components" integration-type link itself uses `integration=Drop-in`, while the redirect and make-payment links use `integration=Components`; verify the base guide rather than treating the Drop-in URL as Components instructions. See raw lines 25–41, 49–53.
- The guide states no additional MoMo-specific configuration or **base** `/payments` parameters. It does not show a React Native Component constructor or a minimum React Native SDK version. Its recurring-token path below is a separate use case with explicit additional request fields, so the base no-extra-parameter sentence does not cancel those fields. See raw lines 43–69.
- To create a recurring token, the page specifies `storePaymentMethod: true` and unique `shopperReference` in `/payments` and a merchant server able to receive recurring token lifecycle webhooks. It says `recurring.token.created` delivers `storedPaymentMethodId` **when the initial payment has settled**. The page does not describe shopper-consent mechanics. A request, callback or shown token ID is not evidence that settlement or token creation occurred. See raw lines 55–78.
- Later token requests use `paymentMethod.storedPaymentMethodId` (or `/listRecurringDetails` lookup), the same shopper reference, `shopperInteraction: ContAuth`, and `Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. TEST snippets use `momo_wallet` and VND as examples, not evidence of successful future charges or general currency eligibility. The Java example calls `setRecurringDetailReference` where prose and most other examples use `storedPaymentMethodId`; its VND 15000 amount also differs from cURL's VND 1000. Review the applicable API-library model before copying. The cURL `/v68/payments` is an example path, not a stated API-version minimum for this Advanced-only guide. See raw lines 80–146.
- For testing, the guide points to the MoMo test app and scenario-specific provider test credentials, with payment status in Adyen's **test** Customer Area. It separately requires a MoMo request in the **live** Customer Area before live acceptance. Mobile-browser app download and desktop-browser QR scanning are testing directions on this page; they do not establish React Native Component desktop-QR behavior or a completed payment. See raw lines 293–302.

## Detail locators

- Page identity, explicit no-Sessions boundary, Advanced prerequisites and base method additions: raw lines 6–53.
- Recurring token creation and settlement-gated webhook: raw lines 55–78.
- Later token request fields and cURL/Java field and amount differences: raw lines 80–146.
- Other language-specific TEST examples: raw lines 149–290.
- Provider test app/credentials, test Customer Area status and separate live request: raw lines 293–302.

## Related

- [[adyen-online-payments]]
- [[adyen-react-native-sdk]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/momo-wallet/react-native-component/2026-09-15|MoMo React Native Component guide — captured 2026-09-15]]
