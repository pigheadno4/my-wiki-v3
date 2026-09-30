---
title: "Braintree PayPal Pay Later Offers - JavaScript v3"
type: source
date_ingested: 2026-09-29
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/pay-later-offers/javascript/v3"
raw_files:
  - "braintree/docs/guides/paypal/pay-later-offers/javascript/v3-2026-09-16.md"
tags: [braintree, paypal, pay-later, javascript-v3, messaging, checkout]
---

## Overview

This Braintree guide is the JavaScript v3 implementation route for presenting PayPal Pay Later messaging and a standalone Pay Later button through an existing PayPal client-side integration. It preserves the version-scoped component, amount, funding-source and eligibility-check boundaries while leaving country offer terms and general availability to the separate broad Pay Later Offers support guide. It is not a generic PayPal Checkout setup guide, proof of current offer availability or evidence that messaging completes a payment.

## Key takeaways

- Before using this page, the merchant is directed to complete Braintree's PayPal client-side integration for JavaScript v3; the page separately routes full availability and benefit details to the broad Pay Later Offers support article.
- Pay Later messaging is dynamic based on what the customer is buying. The page requires the Pay Later button whenever that messaging is presented, prohibits merchant-created additional promotional content, and requires the PayPal messaging component plus a message container whose amount reflects the product price or cart amount.
- The standalone Pay Later button provides access to Pay Later offers in PayPal Checkout. The page specifies the Pay Later funding source, requires an amount when loading the PayPal SDK for the button to render, and adds an `enable-funding` query parameter for the named UK, AU, FR, DE, ES and IT Checkout with PayPal cases.
- Existing standalone PayPal buttons must each pass `isEligible()` before rendering. That client-side rendering check is not a promise of merchant enablement, buyer approval, authorization, tokenization or settlement.

## Evidence boundaries

> [!warning] JavaScript v3 and prerequisite scope
> Keep these instructions scoped to Braintree's JavaScript v3 PayPal client-side integration. Do not generalize the component-loading, button-rendering or callback/Promise examples to another SDK or treat the setup example as general Pay Later support.

> [!warning] Messaging and checkout are distinct
> Promotional messaging does not itself approve a buyer or complete a payment. Preserve the required Pay Later button, amount-driven messaging and the prohibition on merchant-created promotional material when routing presentation questions.

> [!warning] Conflicting same-date offer tables
> This JavaScript v3 snapshot lists different US Pay Monthly and Australian Pay in 4 ranges from the separately collected broad support article at [[source-braintree-payment-methods-paypal-pay-later-offers]]. Neither page resolves which terms are current. Use this source for JavaScript v3 setup and presentation boundaries, and verify current country terms and eligibility through the applicable product authority.

## Detail locators

- Page-level country table and merchant-versus-consumer availability context: `# Pay Later Offers`, lines 16-28.
- Broad support-article route and required JavaScript v3 PayPal client-side prerequisite: `## Before you get started`, lines 31-35.
- Dynamic messaging, required Pay Later button and prohibition on additional merchant-created promotion: `## Pay Later messaging`, lines 38-44.
- Messaging component callback and Promise setup examples: `### Callback` and `### Promise`, lines 45-61.
- Message container and amount-driven rendering example: `### HTML`, lines 62-73.
- Standalone button funding source, region-qualified `enable-funding`, amount requirement and customization routes: `## Pay Later button`, line 76.
- Per-button eligibility check plus callback and Promise examples: `## Pay Later button`, IMPORTANT notice and examples, lines 77-145.

## Related

- Company: [[braintree]]
- Main payment-method route: [[braintree-payment-methods]]
- Product concept: [[paypal-pay-later]]
- SDK concept: [[braintree-web-sdk]]
- Separate broad offer and availability guide: [[source-braintree-payment-methods-paypal-pay-later-offers]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal/pay-later-offers/javascript/v3-2026-09-16|Braintree PayPal Pay Later Offers - JavaScript v3]] - complete collected page covering the JavaScript v3 messaging and standalone-button integration
