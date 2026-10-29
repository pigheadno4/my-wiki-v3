---
title: "PayTo Web Component integration"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payto/web-component"
raw_files:
  - "adyen/docs/payment-methods/payto/web-component/2026-09-15.md"
tags: [adyen, payto, web, components, agreements, subscriptions]
---

## Overview

This 2026-09-15-captured Adyen Docs page adds PayTo to an existing Web Components integration. It separates Sessions and Advanced server-side flows, one-time payments, subscription agreement setup with a first payment, and subsequent subscription payments. Its examples use AU/AUD. This is a historical integration source, not evidence of current account enablement, a shopper's bank consent, or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Prerequisites and flow boundary.** Both flows require an existing Web Components integration, Checkout API v70 or later, and PayTo added in Customer Area (raw lines 25–35, 308–317). The Advanced flow also requires handling an await action (line 316). Sessions /sessions covers one-time payment and subscription setup plus first payment; the page explicitly routes subsequent subscription payments to Advanced /payments or API-only, not a later /sessions request (lines 37–51, 221–224).
- **One-time versus agreement setup.** Sessions one-time requests require the shopper's first and last name; the returned mandate is described as adhoc, exact amount, count 1, with an end date defaulting to one day after the request (lines 53–101). Subscription setup adds stored-payment consent parameters and a mandate with frequency, end date, amount, amount rule and remarks; count is conditionally required for non-adhoc frequencies (lines 122–150). Advanced /payments adds the PayTo payment method and shopperAccountIdentifier, which is a bank detail or PayID reference, for the one-time or first subscription payment (lines 355–383, 432–458). The raw examples use AU/AUD, not a statement of universal availability.
- **Agreement, token and payment lifecycle.** The shopper's bank can authorize or decline the agreement (lines 217–219, 533–535). On acceptance, the page describes RECURRING_CONTRACT for a later subscription route; the subsequent /payments table instead points to recurring.token.created data.storedPaymentMethodId, requires shopperInteraction ContAuth, and limits stored-token use to the accepted agreement's conditions (lines 537–546). An Advanced initial response example is Pending with an await action; a subsequent response example is Received (lines 414–429, 515–530, 573–596). Neither example alone proves a final successful payment. AUTHORISATION can report authorized or rejected payment on an accepted agreement; OFFER_CLOSED reports agreement failure or cancellation, and refunds can later fail through REFUND_FAILED (lines 611–641).
- **Source cautions.** Token wording differs within this page: the acceptance prose names recurringDetailReference, the RECURRING_CONTRACT list says pspReference, and the subsequent-payment table names recurring.token.created data.storedPaymentMethodId (lines 219, 248–250, 535, 544, 633–635). Do not equate these fields or webhooks without the flow-specific payload. Several request examples omit commas and both initialization snippets show newPayTo despite importing PayTo (lines 87–88, 189–192, 284–292, 345–353, 507–511, 567–569); they are illustrative, not verified copy-pasteable requests. The email scenarios at lines 294–306 and 643–655 are test simulations, not live-payment evidence.

## Detail locators

- Sessions requirements, one-time and subscription request/mandate tables: raw lines 25–150; Sessions webhook and UI sections: lines 217–306.
- Advanced prerequisites, one-time and subscription setup /payments tables and examples: raw lines 308–535; subsequent subscription route: lines 537–597.
- Shopper account identifier patterns: raw lines 599–609; required webhook descriptions: lines 611–641; test email cases: lines 643–655.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payto/web-component/2026-09-15|PayTo Web Component guide, captured 2026-09-15]]
