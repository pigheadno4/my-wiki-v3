---
title: "Braintree Auth Multi-Currency (Node.js)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-auth/multi-currency/node"
raw_files:
  - "braintree/docs/guides/braintree-auth/multi-currency/node-2026-09-16.md"
tags: [braintree, braintree-auth, multi-currency, merchant-accounts, node-js]
---

## Overview

This collected closed-beta Braintree Auth Node.js guide covers adding and listing presentment currencies for a connected merchant when the platform supports new Braintree signups. Currency addition is limited to merchants whose Braintree account was created through Braintree Auth; connecting an existing non-OAuth account to an OAuth application does not satisfy that condition. The page also preserves payment-method currency-support conditions and an Amex-specific outcome that is not fully reconciled with its general rule.

## Key takeaways

- After the OAuth flow yields a merchant access token, the guide routes the platform to the Merchant API to add a currency. Its callback and Promise examples use `gateway.merchantAccount.createForCurrency()`, while listing the merchant's existing currency support uses `gateway.merchantAccount.all()`; exact example details remain at the raw locators below.
- Adding a currency is supported only for merchants who signed up through Braintree Auth. The guide says an attempt for a merchant who instead connects an existing non-OAuth Braintree account to an OAuth application produces a validation error.
- The page generally says all payment methods accepted by the merchant must support the new currency. It states that if any accepted payment method does not, a validation error is returned and no new merchant account is created.

> [!warning] Closed-beta and account scope
> This 2026-09-16 snapshot marks Braintree Auth as closed beta. Its multi-currency route applies to connected merchants who signed up through Braintree Auth and does not establish current product availability, platform or merchant eligibility, account enablement, or support for a particular currency.

> [!warning] Amex-specific qualification versus the general rule
> The guide's general text requires every accepted payment method to support the new currency and says failure prevents creation of a new merchant account. Its Amex note separately says an unsupported Amex currency can succeed for other cards while not enabling Amex presentment, and that a later Amex transaction produces a transaction validation error. The snapshot does not reconcile those statements; preserve both and use the exact raw locators rather than generalizing either outcome.

## Detail locators

- Closed-beta availability, platform support for new signups and eligible merchant-account origin: `# Multi-Currency`, lines 17-22.
- OAuth/access-token prerequisite and callback/Promise currency-add examples: `## Adding a currency`, lines 27-54.
- Unsupported accepted-payment-method validation and merchant-account creation outcome: `## Adding a currency`, line 55.
- Merchant-account listing example and displayed `currencyIsoCode`: `## Adding a currency > ### Node`, lines 56-66.
- General all-payment-method currency-support condition and dedicated support references: `## Currency support`, lines 68-72.
- Amex currency subset, other-card success qualification and later Amex transaction validation error: `## Currency support > **NOTE**`, lines 75-76.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-auth]]
- Supporting concept: [[braintree-currencies]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-auth/oauth-flow/node-2026-09-16|Braintree Auth OAuth Flow (Node.js)]] - navigation-only route for obtaining the merchant access token; not used as factual evidence here
- [[raw/braintree/docs/guides/braintree-auth/reference/node-2026-09-16|Braintree Auth Node.js reference]] - navigation-only route for merchant-account validation errors; not used as factual evidence here
- [[raw/braintree/docs/reference/request/merchant-account/create-for-currency/node-2026-09-16|Merchant Account: Create For Currency (Node.js)]] - navigation-only dedicated operation route; not used as factual evidence here
- [[raw/braintree/docs/reference/request/merchant-account/all/node-2026-09-16|Merchant Account: All (Node.js)]] - navigation-only dedicated listing route; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/guides/braintree-auth/multi-currency/node-2026-09-16|Braintree Auth Multi-Currency (Node.js)]] - complete collected guide covering eligible connected merchants, access-token-based currency creation and listing, payment-method support conditions and the Amex qualification
