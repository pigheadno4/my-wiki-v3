---
title: "Adyen Korean Card Payments via redirect for API-only integrations"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/korean-cards/api-only"
raw_files:
  - "adyen/docs/payment-methods/cards/korean-cards/api-only/2026-09-15.md"
tags: [adyen, cards, korean-cards, api-only, redirect]
---

## Overview

This 2026-09-15 Adyen guide describes adding **Korean Card Payments via redirect** to an existing **API-only Advanced online-payments integration**. It covers only method-specific additions, and delegates the rest of the payment, redirect, and outcome handling to the main integration guide. It is a dated setup guide, not evidence that a particular merchant is enabled or a payment succeeded. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The prerequisites are an existing API-only integration that handles `action.type: redirect` and adding this method in Customer Area. These steps are conditional on merchant setup; merely sending discovery parameters does not establish availability. (raw lines 19–29)
- For `/paymentMethods`, the guide specifies `countryCode: KR` and `amount.currency: KRW`. Its sample response lists `type: kcp_creditcard`. The `kr-KR` locale and KRW 1000 amount appear in TEST examples rather than as universal requirements. (raw lines 46–53, 55–74, 331–342)
- The shopper selects the method, the merchant uses a payment form, `/payments` is sent, and the existing integration handles the returned redirect. The example response has `resultCode: RedirectShopper` and a GET `action.type: redirect` URL; this is a next action, not authorization, capture, or settlement proof. (raw lines 31–42, 682–696)
- The guide directs merchants to contact Support to set up the test environment. Before live card acceptance, it says to assess PCI DSS compliance and submit a required Self-Assessment Questionnaire A document. This dated statement is not a PCI compliance determination or safe handling authorization for raw card data. (raw lines 698–702)

## Material guide and example conflicts

- The flow overview says to include additional information about intended purchase items in the payment request, but the dedicated `/payments` section says **no additional parameters** are needed and its shown requests do not include item data. Resolve this with current provider guidance before implementation. (raw lines 31–36, 344–346, 348–679)
- The payment-form section says no other shopper information must be collected, yet curl, Node, Python and Ruby `/payments` examples include raw card number, expiry, CVC and holder name. Java, PHP, C#, Go and TypeScript examples provide only `kcp_creditcard` in `paymentMethod`. These divergent test snippets do not define a complete, safe live card-data collection or PCI model. (raw lines 38–44, 352–375, 397–409, 436–452, 480–496, 513–535, 559–575, 588–609, 622–643, 665–679, 698–702)
- Language samples name distinct API-library versions and TEST endpoints/environments; their request structure, SDK calls, and values are illustrative for those examples. A LIVE endpoint prefix is noted separately in library snippets. (raw lines 59–74, 76–329, 350–679)

## Detail locators

- Prerequisites, flow and payment-form text: raw lines 15–44.
- Payment-method discovery parameters and test examples: raw lines 46–342.
- Payment request examples and redirect response: raw lines 344–696.
- Test and live qualifications: raw lines 698–702.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/korean-cards/api-only/2026-09-15|Adyen Korean Card Payments via redirect API-only guide, 2026-09-15 snapshot]]
