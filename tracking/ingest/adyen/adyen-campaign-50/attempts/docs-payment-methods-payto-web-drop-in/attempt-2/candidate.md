---
title: "PayTo Web Drop-in integration"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payto/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/payto/web-drop-in/2026-09-15.md"
tags: [adyen, payto, web, drop-in, mandate, subscription]
---

## Overview

This 2026-09-15-captured guide adds PayTo to an existing Web Drop-in integration, split between Sessions and Advanced flows. It covers one-time payments, setting up a bank agreement with the first subscription payment, subsequent subscription charges, status webhooks and test identifiers. Checkout API **v70 or later** and PayTo setup in Customer Area are stated for both flows. This is a method-specific add-on and dated example set, not proof that a merchant is enabled, an agreement was accepted, or a payment succeeded. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** The one-time `/sessions` table requires shopper first and last name. It lists statement, line-item and reference fields as optional, with a PayTo reference maximum of **35 characters**. The described one-time response has an `adhoc` mandate, default end date one day after the request, exact amount rule and count 1. For subscription setup plus first payment, the Sessions table additionally requires `storePaymentMethod: true`, `recurringProcessingModel: Subscription`, `shopperInteraction: Ecommerce`, and mandate frequency, end date, amount, amount rule and remarks. `mandate.count` is conditionally needed for non-`adhoc` frequency, despite its unmarked Required column; `mandate.startsAt` is optional. The example of AUD 30 first payment and up to AUD 90 weekly is illustrative. Subsequent subscription payments are routed to **Advanced or API-only**, not Sessions. See raw lines 25–51, 53–101, 122–160 and 217–224.
- **Advanced:** The `/payments` one-time table requires `paymentMethod: payto`, `paymentMethod.shopperAccountIdentifier` and shopper first/last name. Subscription setup adds stored-payment, Subscription/Ecommerce and mandate fields analogous to Sessions. The captured v72 examples use AU/AUD and a PayID email; they do not define current bank acceptance or a higher minimum than the stated v70. Example responses show `resultCode: Pending` with `action.type: await`, meaning the shopper still needs to authorize or decline the bank agreement and the payment outcome remains unresolved. See raw lines 292–303, 323–398 and 400–503.
- **Subsequent subscription charge:** The Advanced table requires `paymentMethod: payto`, `paymentMethod.storedPaymentMethodId` associated with the shopper, and `shopperInteraction: ContAuth`. Use of that stored method is restricted to the accepted agreement's conditions. The guide identifies `data.storedPaymentMethodId` from `recurring.token.created` for this request. Its illustrative subsequent response is `Received`, not final authorization. See raw lines 505–565.
- **Agreement and payment notifications:** The shopper receives a bank notification to authorize or decline the agreement. The guide says accepted subscription agreements yield a `RECURRING_CONTRACT` webhook; `OFFER_CLOSED` signals agreement failure/cancellation and includes `refusalReasonRaw`. An `AUTHORISATION` notification for payment on an accepted agreement may report **authorized or rejected**, so agreement acceptance does not prove payment success. Refunds are asynchronous and can later produce `REFUND_FAILED`; `DISABLE_RECURRING` reports an ended/cancelled agreement and token deletion. See raw lines 217–256 and 579–609.
- **Web UI and tests:** Optional tree shaking prose says `PayTo`, while both import snippets spell the export `Payto`; verify the actual package export before copying. No extra PayTo Drop-in configuration is stated. The test tables provide `shopperAccountIdentifier` email values for agreement expiry/refusal and payment refusal/error, alongside success cases; these are simulated scenarios, not financial execution evidence. See raw lines 258–290 and 305–321, 611–625.

> [!warning] Captured example and identifier discrepancies
> The Sessions subscription table marks `storePaymentMethod: true` required (raw line 130), but its example request omits that field (lines 162–193); do not treat that sample as a complete subscription request. The Sessions one-time and subscription request examples omit commas before `returnUrl` or other following properties (raw lines 87–89 and 189–193); the Advanced subscription example similarly omits a comma after `shopperReference` (lines 475–479). The page labels several curl request-shaped blocks as “example response” (lines 103–120, 198–215, 384–398, 485–499, 543–565). The Advanced base link contains an unresolved encoded platform template and its `await` action points to a redirect-named anchor (lines 300–302). For token retrieval, the subscription prose says `RECURRING_CONTRACT` includes `recurringDetailReference` (lines 217–219, 501–503), the required-webhook section says its token is in `pspReference` (lines 248–250, 601–603), and the subsequent-payment table instructs use of `data.storedPaymentMethodId` from `recurring.token.created` (lines 511–513). Keep the webhook payload paths distinct and verify the identifier used for the request rather than treating them as interchangeable.

## Detail locators

- Sessions prerequisites, one-time and first-subscription tables/examples: pinned raw lines 25–224.
- Sessions webhooks, import/configuration and test matrix: raw lines 226–290.
- Advanced prerequisites, one-time and first-subscription tables/examples: raw lines 292–503.
- Subsequent charge, account identifier formats, webhooks and tests: raw lines 505–625.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payto/web-drop-in/2026-09-15|PayTo Web Drop-in guide, captured 2026-09-15]]
