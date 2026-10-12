---
title: "Adyen Docs: Partial authorizations"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/partial-authorizations"
raw_files:
  - "adyen/docs/online-payments/partial-authorizations/2026-09-15.md"
tags: [adyen, online-payments, partial-authorizations, checkout-api, cards]
---

## Overview

This Adyen guide explains partial authorizations for [[adyen-online-payments]]: when the requested card amount exceeds the shopper's available balance, an issuer can authorize the available amount instead of declining the payment, after which the merchant can collect the remainder or cancel the transaction. It is a Checkout API Advanced-flow feature with material integration, scheme, issuer-support, and account-enablement conditions.

The page is a dated documentation snapshot, not proof of current account eligibility, issuer support, successful authorization, capture, or release of a particular hold.

## Key takeaways

- The integration uses the `/payments` endpoint with Checkout API v69 or later and is limited here to API-only integrations or Web Drop-in/Components using the Advanced flow. Sessions flow is not supported.
- The page lists Visa and Mastercard, but explicitly says issuer support is not guaranteed; Adyen Support must enable the feature before use.
- Set `additionalData.allowPartialAuth` to `true`. If another payment method is used for the outstanding balance, use the same order `reference` to connect the payments for reconciliation.
- A response `resultCode` of `PartiallyAuthorised` indicates the full amount was not authorized; `additionalData.authorisedAmountValue` supplies the authorized amount for calculating the outstanding balance.
- Follow-up choices include starting another `/payments` transaction for the outstanding amount, canceling, capturing the partial amount, or—only for tokenized payments—retrying the original method later. Cancellation removes the hold only when delayed or manual capture is in use; the options can also be combined.

## Detail locators

- **Requirements** — supported integration shapes and API floor; Visa/Mastercard and issuer-support limitation; Sessions incompatibility; Support enablement.
- **How it works** — initial request, issuer decision, response, follow-up choices, and use of a shared `reference`.
- **Make the initial payment** — request fields, versioned SDK examples, response fields, and example payload.
- **Follow up a partial authorization** — outstanding-balance payment and the conditional cancellation, capture, tokenized-retry, and combined-option routes.
- **Testing** — test-environment simulation, amount suffix, test cards, and expected response values.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/online-payments/partial-authorizations/2026-09-15|Adyen Docs — Partial authorizations (2026-09-15)]]
