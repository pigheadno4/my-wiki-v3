---
title: "PayCo for API only"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payco/api-only"
raw_files:
  - "adyen/docs/payment-methods/payco/api-only/2026-09-15.md"
tags: [adyen, payco, api-only, south-korea, redirect]
---

## Overview

Adyen's 2026-09-15 PAYCO API-only guide adds PayCo to an existing **Web API-only Advanced-flow** integration. It covers method discovery, a merchant-built form, server payment request and redirect action; the linked base guide owns the general redirect and result handling. This snapshot is not evidence of current merchant eligibility or an executed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Prerequisites and method discovery:** Requires an existing API-only integration set up for `action.type: redirect` and PayCo added in Customer Area. The `/paymentMethods` table gives `countryCode: KR` and `amount.currency: KRW`; its example response identifies `type: kcp_payco`. Examples also use `shopperLocale: kr-KR` and Checkout v72 TEST, but example response presence is not a guarantee that a particular merchant is enabled. [Raw lines 23–29, 44–53, 53–72, 329–340]
- **Shopper form and request:** The merchant-built form lists PayCo but needs no additional PayCo-specific fields. The payment examples submit `paymentMethod.type: kcp_payco`, KRW amount, reference, return URL and merchant account from the server. The page says no additional `/payments` parameters for PayCo, yet its “how it works” step tells the reader to include additional purchased-item information without naming a field or including items in its payment examples. Preserve that prose/example tension; do not infer an unconditional `lineItems` requirement or suppress the earlier statement. [Raw lines 31–42, 342–368, 492–523]
- **Redirect and outcome:** A `/payments` example returns `RedirectShopper` with an `action.type: redirect`, and the existing API-only integration handles that action. A redirect response or shopper return is not final authorization, capture, settlement or a successful transaction. This page does not specify a PayCo-specific result-code/webhook completion procedure. [Raw lines 660–676]
- **Testing/environment:** The page says there are no specific PayCo test credentials and directs testing assistance to Adyen Support. Server examples use TEST settings and some mention an additional live endpoint URL prefix for LIVE; they do not establish live merchant activation or a real payment. [Raw lines 53–327, 370–658, 678–682]

## Detail locators

- `/paymentMethods` examples by language: raw lines 53–327; payment examples: lines 346–658. The Node JavaScript/TypeScript snippets refer to `Config` and `EnvironmentEnum` without imports in the shown snippets, so they should not be assumed to be standalone runnable code. [Raw lines 180–208, 297–327, 492–523, 623–658]
- Country/currency and `kcp_payco` type are documented here; no recurring token route, 3DS step, cancellation/refund behavior, or final payment-status guarantee is defined.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payco/api-only/2026-09-15|PayCo for API only (2026-09-15)]]
