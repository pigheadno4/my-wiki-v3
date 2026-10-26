---
title: "Adyen iDEAL | Wero API-only integration"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ideal/api-only"
raw_files:
  - "adyen/docs/payment-methods/ideal/api-only/2026-09-15.md"
tags: [adyen, ideal, wero, api-only, online-payments, sepa-direct-debit]
---

## Overview

Adyen's 2026-09-15 iDEAL | Wero page describes method-specific additions to an existing API-only Advanced-flow integration. It covers co-branding, availability lookup, redirect completion, SEPA Direct Debit-based recurring payments, a stored preferred-bank route, and TEST/live guidance. See [[adyen]], [[adyen-online-payments]], and [[adyen-tokenization]].

## Key takeaways

- The page says iDEAL is evolving into Wero and sets a **January 29–March 31, 2026** window for API-only merchants to change the displayed name to **iDEAL | Wero** and the logo to the co-branded logo. This is a dated instruction in the snapshot, not proof of current branding or completion. Its later sample `/paymentMethods` response still names the method `iDEAL` with type `ideal`; preserve that example/prose mismatch instead of assuming the response label has been updated.
- The page requires an existing API-only integration, redirect handling for `action.type: redirect`, and iDEAL | Wero added in Customer Area. To request its availability, it specifies `/paymentMethods` with `countryCode: NL`, `amount.currency: EUR`, and an amount value. These are the page's request conditions, not a complete account-eligibility guarantee.
- Its additional `/payments` parameters are `paymentMethod.type: ideal` and a `returnUrl` of at most 1024 characters. Redirect the shopper to `action.url`; after return, send URL-decoded `redirectResult` in `/payments/details` and use `resultCode` for shopper presentation. The `Authorised` details response is an example, not a guaranteed outcome. The page recommends SFSafariViewController or Chrome Custom Tabs over WebView for an in-app GET redirect and strongly recommends the device default browser for mobile integrations; those are recommendations with their stated scope.
- Recurring payments described here use **SEPA Direct Debit** tokens, not an iDEAL `ideal` token. The page says standard SEPA tokenization parameters need no extra SEPA-specific fields, then identifies `storedPaymentMethodId` in a `recurring.token.created` webhook. It restricts tokenised payments to shopper-not-present `Subscription` or `UnscheduledCardOnFile` scenarios. Subsequent requests use `sepadirectdebit`, the stored ID, shopper reference and `ContAuth`; a `Received` response only confirms receipt, with webhooks used to track payment success. The language samples vary in fields, amount/country, processing model and library version; follow the prose and relevant versioned API guide rather than treating all samples as one validated request.
- For a preferred bank, the page says to enable bank-account details on the webhook, store the BIC from an **Authorised** iDEAL | Wero webhook, display that bank, and send it as `paymentMethod.issuer` in a later `ideal` payment. Omit `issuer` if the shopper chooses another bank. Its BIC partner list may change, so the captured list is not current bank eligibility.
- The page calls the iDEAL | Wero TEST environment unreliable and recommends live penny tests. Live acceptance requires adding the method in live Customer Area; the live test path uses a live issuer account, shopper QR/bank selection and authorization, then Customer Area status checking. When TEST is available, `TESTNL2A` offers documented success, cancellation, expiration and failure simulations; expiration may yield `Pending` or `Received`, so it is not final success. The page's high-level four-step outline says to fulfill after the payment request, but the later redirect/details and webhook sections make that outline insufficient as payment-success evidence.

## Detail locators

- Dated co-branding, API-only prerequisites, four-step outline, and `/paymentMethods` NL/EUR request and response-name discrepancy: raw lines 15-91.
- `/payments` fields, redirect, mobile recommendations, `/payments/details`, and example result: raw lines 93-142.
- SEPA recurring overview, token-creation prose and examples, and token-created webhook: raw lines 143-504.
- Shopper-not-present restriction and subscription/unscheduled token-payment examples: raw lines 506-1399.
- Preferred-bank BIC webhook route, `issuer`, and changeable bank list: raw lines 1401-1460.
- Unreliable TEST environment, live gating, penny tests, and conditional `TESTNL2A` simulations: raw lines 1462-1500.

## Raw Sources

- [[raw/adyen/docs/payment-methods/ideal/api-only/2026-09-15|iDEAL | Wero API-only (2026-09-15 snapshot)]]
