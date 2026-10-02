---
title: "Adyen Web Payment Disclaimers"
type: concept
category: technology
tags: [adyen, web-sdk, checkout, accessibility]
---

## Definition and version boundary

In `@adyen/adyen-web@6.46.0`, `disclaimerMessage` is a payment Component configuration for text above the shared SDK Pay button. The Card-specific configuration from earlier releases moves to the shared UIElement surface. This is informational presentation, not an acceptance checkbox, consent record, or legal-validity guarantee.

## Configuration and rendering

- Supply `message` and optionally `linkText`/`link`, each accepting a string or array. `%{placeholder}` slots consume entries in appearance order; placeholder names do not select keys.
- A link label without a URL becomes plain text; a slot without a string label disappears. Supplied link URLs must pass the renderer's HTTP URL validation or its label content is omitted.
- When the SDK button renders, PayButton merges its disclaimer ID into the existing description association. This is implementation evidence, not screen-reader verification.
- `showPayButton: false` hides the button but preserves the disclaimer when its parent renders PayButton. Card still gates that parent rendering on its card UI state. A merchant-supplied button does not automatically inherit the SDK description association.
- The retained configuration explicitly excludes express/wallet Components with branded buttons: PayPal, Apple Pay, Google Pay, Amazon Pay, and Cash App Pay. Do not promise universal payment-method support.

Configure the payment Component, or its `paymentMethodsConfiguration` entry in Drop-in, rather than assuming this is a global AdyenCheckout option. See [[source-github-adyen-web]] for an illustrative Card snippet and exact implementation links.

## Review and evidence limits

`onReview` remains a separate payment lifecycle in [[adyen-review-page-checkout]]. A displayed disclaimer does not submit or authorize a payment. The retained story documents configuration intent; no upstream build, browser, wallet, payment, or accessibility test was executed.

## Sources and related

- [[source-github-adyen-web]] - 6.46.0 shared disclaimer implementation, configuration, and boundaries
- [[changelog-github-adyen-web]] - version-qualified migration and preserved older Card history
- [[adyen]] - independent SDK and merchant eligibility boundaries
