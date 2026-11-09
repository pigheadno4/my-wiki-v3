---
title: "Stripe Docs — Authenticate with 3D Secure"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/3d-secure/authentication-flow"
raw_files:
  - "stripe-payments-3d-secure-authentication-flow-2026-11-07.md"
  - "stripe-3d-secure-authentication-flow-2025.md"
tags: [stripe, 3d-secure, 3ds2, sca, payment-intents, liability-shift, radar, ios, android, react-native]
---

## Summary

Stripe's 3D Secure (3DS) authentication guide covers Web, iOS, Android, and React Native, with automatic and manual triggering, web display, mobile customization, test cases, and conditional fraud-dispute liability shift. Standalone 3DS can authenticate on Stripe while another PSP acquires the transaction. The November 2026 capture states support through 3DS protocol version 2.3.1. Both captures say major brands no longer support 3DS1 and recommend Payment Intents/Setup Intents, yet also describe fallback to 3DS1 if a bank lacks 3DS2; that captured tension is not proof of an available 3DS1 path for any present card or network. See [[stripe-3d-secure]]. [May capture](../../raw/stripe-3d-secure-authentication-flow-2025.md#L8-L15); [November capture](../../raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md#L9-L17).

## Authentication and payment outcomes

Stripe may trigger 3DS for regulation or guidelines, issuer soft declines, or its optimizations; Radar rules or `payment_method_options[card][request_three_d_secure]` can request it. Not every transaction supports 3DS; the guide gives wallets and off-session payments as examples, while its off-session test card describes a conditional authentication case. Manual `any` prefers frictionless and `challenge` prefers a challenge, but the issuer determines the final flow. The manual parameter overrides dynamic Radar 3DS rules for that Intent or Checkout Session, while mandatory authentication runs independently. The November capture expressly says Stripe APIs cannot manually turn off 3DS. Its custom-rule tier is named **Radar Plus**; the May capture used **Radar for Fraud Teams**. [May capture](../../raw/stripe-3d-secure-authentication-flow-2025.md#L55-L59), [May manual](../../raw/stripe-3d-secure-authentication-flow-2025.md#L87-L93), [May preferences](../../raw/stripe-3d-secure-authentication-flow-2025.md#L164-L172); [November triggers](../../raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md#L54-L58), [November manual](../../raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md#L86-L94), [November preferences](../../raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md#L137-L145), [off-session test](../../raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md#L441-L443).

In the described PaymentIntent flow, required 3DS leads to `requires_action`, and a successful authentication leads Stripe to attempt a charge and the Intent to `processing`. The subsequent payment outcome can be `succeeded`, `requires_capture`, or `requires_payment_method`. A `three_d_secure.result` of `authenticated` establishes authentication, not payment authorization, capture, or settlement; a test card in both captures authenticates and then declines. Read the Charge's `payment_method_details.card.three_d_secure` for authentication outcome. The before-2019-02-11 API aliases `requires_source` and `requires_source_action` are historical version names. [May flow](../../raw/stripe-3d-secure-authentication-flow-2025.md#L61-L81), [May test](../../raw/stripe-3d-secure-authentication-flow-2025.md#L485), [May alias](../../raw/stripe-3d-secure-authentication-flow-2025.md#L266); [November flow](../../raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md#L60-L80), [November test](../../raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md#L443), [November alias](../../raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md#L230).

## Display, mobile, and test locators

Web integrations can use Stripe's popup with `confirmCardPayment`/`handleCardAction`, a bank redirect, or an iframe. For a redirected iframe, the return page sends `postMessage` to the parent; the parent then retrieves the current PaymentIntent and checks its status. The return URL or message alone does not prove payment completion. The bank controls the web challenge UI, and the guide warns against the iframe `sandbox` attribute; see its supported sizes and CSP origins. [May web](../../raw/stripe-3d-secure-authentication-flow-2025.md#L176-L219), [May iframe](../../raw/stripe-3d-secure-authentication-flow-2025.md#L255-L294); [November web](../../raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md#L149-L192), [November iframe](../../raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md#L219-L258).

PaymentSheet/FlowController handle 3DS for the mobile paths cited; the separate custom integration guidance covers iOS `STPPaymentHandler`, Android `PaymentAuthConfig.Stripe3ds2Config`, and React Native `StripeProvider.threeDSecureParams`. The described custom authentication timeouts must be at least five minutes; iOS and React Native include return URL/webview handling. The sandbox tables distinguish required, supported, and unsupported cards and include a card that declines after authentication; mobile tables list four challenge screens. These are test cases, not live payment outcomes. [May mobile](../../raw/stripe-3d-secure-authentication-flow-2025.md#L328-L468), [May tests](../../raw/stripe-3d-secure-authentication-flow-2025.md#L471-L535); [November mobile](../../raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md#L287-L427), [November tests](../../raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md#L429-L493).

## Disputes and liability shift

Successful 3DS authentication does **not** guarantee liability shift for a particular payment or dispute. It can be expected for successfully authenticated payments later receiving eligible fraud disputes, subject to network rules and payment/dispute conditions. `charge.succeeded` confirms payment success only, `three_d_secure.result=authenticated` confirms authentication only, and an ECI in `three_d_secure.electronic_commerce_indicator` can help assess eligibility but guarantees no shift. The May guide already said shift *typically* applies and listed exceptions. Shift may occur when a network requires unavailable 3DS; conversely, monitoring-program or network/industry exclusions and post-authorization downgrades can prevent it even after successful authentication. Its Visa examples are Visa-specific, not general network rules. Non-fraud dispute reasons follow the standard process. [May liability](../../raw/stripe-3d-secure-authentication-flow-2025.md#L537-L557); [November guidance](../../raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md#L495-L513), [November exceptions/ECI](../../raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md#L521-L529).

A 3DS-authenticated payment can still receive an inquiry. Stripe says the merchant **must respond**: otherwise the bank can initiate a financial no-reply chargeback that could invalidate liability shift. An Early Fraud Warning or a low percentage of fraud disputes can also occur despite expected shift. Neither inquiry response nor supplying ECI proves a dispute will be won. [May capture](../../raw/stripe-3d-secure-authentication-flow-2025.md#L543-L547); [November capture](../../raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md#L515-L519).

## Historical assets

The May capture references ten local screenshots retained in that raw: Web `stripe-3ds-checkout-page.png`, `stripe-3ds-frictionless-flow.png`, `stripe-3ds-challenge-flow.png`; iOS `stripe-3ds-ios-checkout.png`, `stripe-3ds-ios-loading.png`, `stripe-3ds-ios-otp.png`, `stripe-3ds-ios-customization.png`; Android `stripe-3ds-android-confirm.png`, `stripe-3ds-android-processing.png`, `stripe-3ds-android-otp.png`. The November Markdown links to Stripe CDN images. The captures do not establish pixel-equivalent image bytes. [May assets](../../raw/stripe-3d-secure-authentication-flow-2025.md#L17-L49), [May customization](../../raw/stripe-3d-secure-authentication-flow-2025.md#L339); [November images](../../raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md#L19-L48), [November customization](../../raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md#L298).

## Related Pages

- [[stripe-3d-secure]] — main 3DS concept
- [[stripe-authorization-boost]] — recommendations on reducing 3DS challenges
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payments-3d-secure-authentication-flow-2026-11-07|November 7, 2026 3DS authentication-flow capture]] — full webpage content (540 lines)
- [[raw/stripe-3d-secure-authentication-flow-2025|May 8, 2026 3DS authentication-flow capture]] — historical webpage content (566 lines; includes ten local screenshot references)
