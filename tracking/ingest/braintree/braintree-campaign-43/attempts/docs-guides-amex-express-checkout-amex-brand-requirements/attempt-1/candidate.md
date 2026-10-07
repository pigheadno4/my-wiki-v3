---
title: "Braintree Amex Express Checkout Brand Requirements"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/amex-express-checkout/amex-brand-requirements"
raw_files:
  - "braintree/docs/guides/amex-express-checkout/amex-brand-requirements-2026-09-16.md"
tags: [braintree, amex-express-checkout, branding, secure-remote-commerce]
---

## Overview

This 2026-09-16 Braintree website snapshot records American Express brand-presentation requirements for the legacy Amex Express Checkout button and mark. The same page says Amex Express Checkout was replaced by Visa Secure Remote Commerce (SRC), describes SRC as limited release for eligible merchants with an API subject to change, names Android v2, iOS v4 and JavaScript v3 as its introduction points, and directs merchants to contact Braintree for access. It is historical website evidence, not proof of current Amex Express Checkout or SRC support, a complete migration path, merchant or buyer eligibility, account enablement, exact SDK/runtime behavior, or payment execution.

## Key takeaways

- Merchants implementing Amex Express Checkout must use the supplied button graphics as presented and must not resize, recolor or modify them.
- For radio-button presentation, the page gives a primary payment-mark-plus-label form, a secondary button-plus-label form and a tertiary label-only form. The label must remain exactly "Amex Express Checkout" in spelling, capitalization and style.
- Other Amex trademarks or graphics cannot substitute for the approved Amex Express Checkout button. Separately, payment-acceptance marks should use the Amex blue box logo.
- Where implemented, the Amex Express Checkout button must remain clickable and cannot replace a payment-acceptance mark or blue box logo.
- Placing the button before most manual-entry fields is presented as an Amex suggestion intended to benefit autofill, not as a mandatory requirement.

## Availability and evidence boundary

The captured replacement notice does not establish present-day SRC availability or a safe migration outcome: it expressly limits SRC to eligible merchants, says the API can change and instructs merchants to request access. Consult [[braintree-payment-methods]] for the provider-wide payment-method route and its preserved SRC support-status conflict. This page contains brand guidance only; it does not document account configuration, tokenization, transaction creation, lifecycle outcomes, settlement or funding.

## Detail locators

- Replacement by SRC, limited-release eligibility, API-change warning, SDK-generation labels and access request: raw line 18.
- Requirement to use supplied graphics without resizing, recoloring or modification: raw lines 20–22.
- Radio-button presentation hierarchy and exact naming constraints: raw line 23.
- Trademark, acceptance-mark and clickable-button distinctions: raw lines 24–25.
- Suggested placement before manual-entry fields: raw line 26.

## Related

- [[braintree]]
- [[braintree-payment-methods]]

## Raw Sources

- [[raw/braintree/docs/guides/amex-express-checkout/amex-brand-requirements-2026-09-16|Amex Brand Requirements — fetched 2026-09-16]]
