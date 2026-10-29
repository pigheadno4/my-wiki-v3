---
title: "Gift cards Android Drop-in integration"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gift-cards/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/gift-cards/android-drop-in/2026-09-15.md"
tags: [adyen, gift-cards, android, drop-in, sessions, advanced]
---

## Overview

This 2026-09-15-captured Adyen guide adds gift cards to an **existing Android Drop-in integration using version 5.0.0 or later**. It separates Sessions and Advanced server-side flows. Its short add-on instructions do not establish a complete gift-card balance, order, callback or partial-payment implementation; follow the underlying Android Drop-in flow and the [[source-adyen-docs-payment-methods-gift-cards|gift-card overview]] for those subjects. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Version and setup:** this page explicitly applies to v5.0.0, released October 2023, and directs earlier SDK versions to a separate guide. Both Sessions and Advanced tabs require an existing Android Drop-in integration on at least v5.0.0 and adding gift cards in Customer Area before beginning (raw lines 19–39). The earlier-version guide is navigation, not evidence for this version's behavior.
- **Flow-specific add-on:** for Sessions, the page says gift cards need no *additional* fields in the `/sessions` request and no additional Drop-in configuration. For Advanced, it says the same for `/payments` and Drop-in configuration. These statements are scoped to gift-card additions to the existing flow; the base requests and setup remain necessary. After configuration, the Sessions tab routes to creating the checkout session, whereas Advanced routes to launching and showing Drop-in (raw lines 41–67).
- **Payment-flow boundary:** this page does not specify gift-card balance checks, `/orders` partial-payment routing, result callbacks or webhook behavior. The method overview says insufficient card balance can lead to a partial payment with another method and that added steps depend on integration. Use the relevant base Android Drop-in flow and partial-payments guide for implementation detail; do not transfer Web or API-only gift-card steps to Android from this short add-on (this raw lines 23–67; [[source-adyen-docs-payment-methods-gift-cards]] raw lines 23–27).
- **Testing versus live:** the test path uses provider-dependent test card numbers and an Adyen simulator, with amount-ending examples for Authorised, Refused and Error, including `Invalid Pin` and `Pin tries exceeded` as simulated *refusalReason* labels. Those labels are not sample credential fields. Check test status in test Customer Area. For live use, the page directs provider onboarding, adding the variant in live Customer Area and contacting Support to add the card there; its small-amount real-card test suggestion presupposes that live setup. A simulator outcome does not prove live eligibility or payment success (raw lines 69–98).

## Detail locators

- Scope, October 2023 v5 release and earlier-version route: raw lines 15–21.
- Sessions/Advanced prerequisites and Customer Area setup: raw lines 23–39.
- Flow-specific request and configuration statements, then session/launch routing: raw lines 41–67.
- Provider-dependent simulator amount endings, refusal labels and test status: raw lines 69–90.
- Live provider, variant and Support steps: raw lines 92–98.
- General partial-payment and provider context: [[source-adyen-docs-payment-methods-gift-cards]] with its own pinned raw lines 19–27; this entry's raw_files remains child-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-gift-cards]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gift-cards/android-drop-in/2026-09-15|Gift cards Android Drop-in guide, captured 2026-09-15]]
