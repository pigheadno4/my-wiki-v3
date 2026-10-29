---
title: "PayPo Flutter Component integration add-on"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypo/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/paypo/flutter-component/2026-09-15.md"
tags: [adyen, paypo, flutter, components, redirect]
---

## Overview

This 2026-09-15-captured PayPo Flutter Component page gives **PayPo-specific additions** for an existing Flutter Components integration, separately for Sessions and Advanced server-side flows. It relies on the main integration guides for base setup and action handling. It is not evidence of current PayPo enablement or a successfully executed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions flow:** the requirements say existing Sessions-flow Flutter Components, Checkout API **v68 or later**, and PayPo added in Customer Area. The PayPo-specific `/sessions` table marks `shopperName` (first and last name) and `shopperEmail` required; billing and delivery addresses have no required mark. The PLN/PL amount, return URL, reference, and merchant account are shown in a **test** example, not as a complete standalone request contract. The page says no additional PayPo Component configuration is needed (raw lines 25–46, 48–73, 421–425).
- **Advanced flow:** the requirements say existing Advanced-flow Flutter Components, handling of the additional `redirect` action, and PayPo added in Customer Area. The PayPo-specific `/payments` table marks `paymentMethod.type: paypo`, `shopperName` (first and last), and `shopperEmail` required; billing and delivery addresses are unmarked. No additional PayPo Component configuration is needed. The response example contains `resultCode: RedirectShopper` and an `action.type: redirect`; redirect handling belongs to the linked main flow (raw lines 441–471, 843–857).
- In both flow sections, the page says a pre-authorization offer/payment link remains available for **up to 72 hours**. Once the shopper accepts and the payment becomes `Authorised`, the shopper's **30-day PayPo term starts at authorization**. The merchant must capture the payment, and **only full-amount capture** is possible. Immediate automatic capture can be configured when adding PayPo in the live Customer Area. The page says the merchant is funded after capture without waiting for the shopper to complete payment to PayPo; treat that as its conditional statement, not a guaranteed payout time (raw lines 389–419 and 859–889).
- The testing values and verification code are for the **test environment**. Before live PayPo acceptance, the page says to submit a PayPo request in the live Customer Area (raw lines 427–439 and 891–903).

> [!warning] Source route and sample limits
> The Sessions requirement calls for a Sessions-flow Flutter Components integration, but its linked URL contains `advanced-flow?platform=Flutter&integration=Drop-in` (raw line 31); do not use that link label as proof that Advanced Drop-in is the Sessions Components route. The Advanced-flow requirement's integration URL likewise names `Drop-in` while the page is titled Component (raw line 449). The Sessions and Advanced curl examples omit a continuation between `-X POST` and `-d` (raw lines 57–58, 482–483), so they are illustrative rather than commands ready to paste.

## Detail locators

- Scope and flow split: raw `# PayPo Flutter Component` lines 15–25.
- Sessions requirements, method-specific fields, and examples: raw lines 27–387.
- Sessions capture/configuration/test-live: raw lines 389–439.
- Advanced requirements, configuration, payment fields, and examples: raw lines 441–841.
- Advanced redirect response, capture, and test-live: raw lines 843–903.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypo/flutter-component/2026-09-15|PayPo Flutter Component guide, captured 2026-09-15]]
