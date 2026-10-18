---
title: "Bank account verification with open banking | Adyen"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/verify-account-holder"
raw_files:
  - "adyen/docs/business-accounts/verify-account-holder/2026-09-15.md"
tags: [adyen, business-accounts, open-banking, bank-account-verification, aisp]
---

## Overview

Despite its `verify-account-holder` URL, this [[adyen]] page describes **open-banking verification of an unregistered third-party individual's bank-account ownership** through Adyen's gateway and an Account Information Service Provider (AISP), not verification of a registered balance-platform account holder's capabilities. The captured page names Adyen for Platforms, Marketplaces and Classic integrations. A successful route, callback or report is not an Adyen Business Account opening, platform KYC approval, fund transfer or bank receipt. See [[adyen-business-accounts]] for product context.

## Key takeaways

- The actor is an **external, unregistered third-party individual** who authorizes a bank to share a verification report, potentially for a platform/merchant's pre-contract identity and account-ownership check. The page cites AISPs such as Plaid or Tink. Its report data can inform that check, but the source does not make the individual a registered platform account holder or establish a completed regulatory KYC decision. [Raw: lines 15–23]
- The documented integrations are Platforms, Marketplaces or Classic; the API requires an API key (recommended) or basic authentication and an Adyen-assigned **Role for OpenBanking account verification use case: EXTERNAL**. Optional widget customization collects company/application/legal-entity branding details. These are captured setup conditions, not proof of live access or currently supported banks/countries. [Raw: lines 25–33]
- The merchant calls `POST /accountVerification/routes` with the bank account's registered **country**, UI locale and redirect URL; optional per-session `state` supports callback correlation/CSRF protection and should avoid sensitive plain text. Adyen dynamically returns AISP/provider metadata and links based on the **bank's location**; redirect URL does not choose the provider. A route does not guarantee a report code: the individual must complete bank authentication and authorization. [Raw: lines 35–50, 54–102]
- The redirect can return a success `code` or error details, plus `state` and a JWS `signature` described as protecting callback integrity/authenticity. Retrieve the report with `GET /accountVerification/reports/{code}` only after a successful flow, and confirm the response `x-state` matches the request state. Error examples include user cancellation, connection errors and provider errors. A callback code is a retrieval handle, not the verification report itself. [Raw: lines 105–185]
- The report has a separate `id`, generation `country` and an `accounts` list that may contain more than one verified account; examples show IBAN, ACH, EFT and BSB identifiers and holder-party identity fields. These TEST/sample country and bank payloads are **not** a current coverage matrix or evidence of any actual individual's account ownership. Do not infer an Adyen balance account, capability state or completed payout from them. [Raw: lines 185–351]

## Detail locators

- Source identity and external-individual/AISP use case: raw lines 15–23.
- Integration/credential role and optional widget customization: raw lines 25–33.
- Route generation, bank-location selection, consent and code condition: raw lines 35–102.
- Redirect success/error, state/JWS fields and error codes: raw lines 105–155.
- Report retrieval, `x-state` check, response grain and illustrative TEST identifier types: raw lines 157–351.

## Related

- [[adyen-business-accounts]] — product navigation; this page's verification actor is an unregistered external individual
- [[adyen-platforms]] — one of the documented integration types
- [Open Banking API account verification](https://docs.adyen.com/api-explorer/open-banking/latest/post/accountVerification/routes) — linked endpoint reference
- [Open Banking](https://docs.adyen.com/business-accounts/) — page's related route

## Raw Sources

- [[raw/adyen/docs/business-accounts/verify-account-holder/2026-09-15|Adyen open-banking bank-account verification — collected 2026-09-15]]
