---
title: "Adyen partner OAuth scopes"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/partners/oauth/scopes"
raw_files:
  - "adyen/docs/partners/oauth/scopes/2026-09-15.md"
tags: [adyen, partners, oauth, scopes, delegated-access]
---

## Overview

Adyen's partner OAuth scopes page (last modified and captured 2026-09-15) maps delegated access-token scopes to specific customer merchant-account resources and API actions. The token has a scope; the page says an existing OAuth client's scope cannot currently be changed, so requests beyond it require a newly registered OAuth client and renewed customer-resource access. Scopes are one boundary of partner delegation, not universal merchant-account access or proof of consent, live configuration or payment success. See [[adyen-partner-oauth]] for the authorization-code/PKCE and account-grant lifecycle.

## Key takeaways

- `psp.webhook:read` permits viewing webhook configurations and lists two GET operations **plus a POST test**. `psp.webhook:write` lists viewing, creation, editing and deletion, with GET/test POST/create POST/PATCH/DELETE operations. Do not infer the exact allowed methods only from the read/write suffix (raw lines 47–72).
- `psp.onlinepayment:write` permits online payments on a customer's behalf and lists Checkout Payments, Modifications, Orders and Utility request groups, plus Recurring **only GET `/storedPaymentMethods`** with Checkout v70 required. It also lists Management `/me/allowedOrigins` and `/me/generateClientKey` POST actions. Tokenization, raw-card handling and payment-link management require separate scopes (raw lines 74–99).
- For OAuth online payments, ordinary online-payment documentation still applies; OAuth changes API authentication, not payment-flow requirements. Because OAuth does not grant the partner Customer Area access, the page directs allowed-origin creation and client-key generation via Management API, and retrieval of the customer's account-specific live prefix using `/merchants/{merchantId}`; the merchant ID comes from the code-exchange `accounts` response. These are customer/account-scoped setup actions, not a generic live endpoint for all merchants (raw lines 101–145).
- `psp.onlinepayment.tokenization:write` extends online-payment scope for storing shopper details for recurring use and Checkout Recurring list/delete operations, **not** tokenization through the separate Recurring API. `psp.rawcarddata:write` extends online-payment scope for raw-card submission, is disabled by default, requires PCI DSS SAQ D, and needs account-manager enablement (raw lines 147–163).
- `psp:paybylink:write` creates/updates payment links; tokenizing through a payment link also needs online-payment and tokenization scopes for subsequent recurring payments. `psp.accountsettings:write` is described as modifying merchant settings but its displayed operation list contains only GET `/merchants/{merchantId}`; do not infer a write endpoint from this page. `psp.clouddeviceapi:write` lists Cloud device API Terminal API sync/async and device-status/connection requests, not an in-person payment outcome (raw lines 165–199).

## Detail locators

- Token-scope immutability and re-registration: raw lines 19–45.
- Webhook read/write identifiers and exact methods: raw lines 47–72.
- Online-payment scope exclusions and Checkout v70 condition: raw lines 74–99.
- Allowed origins, client key and merchant-specific live prefix: raw lines 101–145.
- Tokenization, raw card and PCI prerequisite: raw lines 147–163.
- Payment links, account-settings list and Cloud device operations: raw lines 165–199.

## Related

- [[adyen-partner-oauth]] — delegated authorization concept and source route.
- [[adyen]] — provider page.

## Raw Sources

- [[raw/adyen/docs/partners/oauth/scopes/2026-09-15|Partner OAuth scopes, captured 2026-09-15]]
