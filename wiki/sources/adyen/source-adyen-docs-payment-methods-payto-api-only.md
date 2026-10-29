---
title: "PayTo API-only integration"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payto/api-only"
raw_files:
  - "adyen/docs/payment-methods/payto/api-only/2026-09-15.md"
tags: [adyen, payto, api-only, australia, mandate, subscription]
---

## Overview

This 2026-09-15-captured Adyen guide adds **PayTo to an existing API-only integration**. It covers AU/AUD method discovery, one-time and subscription-agreement requests, later stored-method payments, `await` actions and asynchronous webhook outcomes. Agreement approval, a `Pending` or `Received` response, token creation and payment authorization are distinct events. This method add-on does not prove current merchant enablement, bank consent, or a successful live payment. See [[adyen]], [[adyen-online-payments]] and the [[source-adyen-docs-payment-methods-payto|PayTo overview]].

## Key takeaways

- **Prerequisites and discovery:** use an existing API-only integration with Checkout API **v70 or later**, handle `action.type: await`, and add PayTo in Customer Area. For `/paymentMethods`, the guide specifies `countryCode: AU` and `amount.currency: AUD`; `shopperReference` is optional there to retrieve stored methods (raw lines 23–40). The overview separately says merchant-method setup can be asynchronous and must be confirmed by its payment-method webhook; Customer Area selection alone is not evidence of an enabled usable method (overview pinned raw lines 29–95).
- **Form/field tension:** the page says the merchant payment form need not collect any information from the shopper, yet its one-time and first-subscription `/payments` tables mark `paymentMethod.shopperAccountIdentifier` (bank details or PayID) and shopper first/last name **required**. The page does not say where those required values come from if the merchant form does not collect them. Preserve both statements and verify a complete data path before implementing; do not interpret “no form collection” as “no shopper data required” (raw lines 42–46, 58–74, 123–149).
- **One-time:** add `paymentMethod: payto`, `shopperAccountIdentifier` and shopper name. Statement and line-item fields are optional; the payment reference is recommended unique but not formally required, with a PayTo **35-character maximum**. The example returns `resultCode: Pending` plus `action.type: await`; these indicate a waiting state, not successful authorization. The sample AU/AUD request is an example, not proof of a real bank account or transaction (raw lines 58–121).
- **Subscription setup and first payment:** the `/payments` table additionally marks `storePaymentMethod: true`, `recurringProcessingModel: Subscription`, `shopperInteraction: Ecommerce`, and mandate frequency, end date, amount, amount rule and remarks required. `mandate.count` is shown optional but its description requires a count of at least 1 for non-`adhoc` frequency; `startsAt` is optional. `amountRule` can be `max` or `exact`, and scheduled frequencies are described for Subscription. The weekly 30 AUD first payment and up-to-90 AUD later payment is a worked example, not a universal bank limit. The shopper receives a bank notification to authorize or decline the agreement (raw lines 123–226).
- **Subsequent subscription payment:** use `paymentMethod: payto`, required `paymentMethod.storedPaymentMethodId` from a shopper-associated `recurring.token.created` webhook's `data.storedPaymentMethodId`, and `shopperInteraction: ContAuth`, within the agreement's conditions. The later-payment example returns `Received`, not final success. Token-reference wording is inconsistent across the page: subscription prose names `recurringDetailReference` in `RECURRING_CONTRACT`, the webhook section says its token is in `pspReference`, and the later-payment table points to `storedPaymentMethodId`; do not assume the values or webhook types are interchangeable (raw lines 224–288, 324–332).
- **Webhooks, tests and example cautions:** `OFFER_CLOSED` reports failed/cancelled agreements; `AUTHORISATION` on an accepted agreement can report **authorized or rejected** payment; `REFUND_FAILED` can follow a received refund; and `DISABLE_RECURRING` reports token deletion when an agreement ends or is cancelled. The test identifiers simulate agreement and payment outcomes, not live-operation proof. Subscription and subsequent-charge request examples omit a comma after `shopperReference`, and “response” snippets are rendered as `curl` requests; the account-identifier regex table also contains syntax that needs validation before reuse. Follow the field descriptions and current API schema rather than copying these snippets as validated recipes (raw lines 166–222, 239–300, 302–351).

## Detail locators

- API-only prerequisites and AU/AUD method discovery: raw lines 15–40.
- Form/no-collection statement versus required shopper fields: raw lines 42–74 and 123–149.
- One-time request and Pending/await response: raw lines 58–121.
- Subscription mandate requirements, count condition, sample and bank approval: raw lines 123–226.
- Subsequent tokenized charge, Received example and identifier formats: raw lines 228–300.
- Agreement/payment/refund/token webhooks and test simulations: raw lines 302–351.
- Method-level AU/AUD, setup confirmation, bank agreement and final webhook sequencing: [[source-adyen-docs-payment-methods-payto]] and its pinned raw lines 23–107; this entry's raw_files remains child-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-payto]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payto/api-only/2026-09-15|PayTo API-only guide, captured 2026-09-15]]
