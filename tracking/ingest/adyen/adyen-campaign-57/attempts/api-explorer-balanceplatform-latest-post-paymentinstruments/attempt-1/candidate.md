---
title: "Adyen Balance Platform API POST /paymentInstruments — create payment instrument"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/paymentInstruments/2026-09-15.md"
tags: [adyen, balance-platform-api, issuing, business-accounts, payment-instruments]
---

## Overview

This 2026-09-15 Balance Platform API Explorer capture describes `POST /paymentInstruments` on the `/bcl/v2` test server. The operation creates a payment instrument associated with a balance account: a physical or virtual card for [[adyen-issuing]], or a `bankAccount` business account for [[adyen-business-accounts]]. Its request schema marks `balanceAccountId`, `issuingCountryCode` and `type` (`card` or `bankAccount`) required; the `card` object is conditionally required for a card despite its `No` table flag. The page does not mark the request body itself required separately from its properties.

## Key takeaways

- For a card, `brand`, `brandVariant`, `cardholderName` and `formFactor` are marked required within `card`. The card brand options are `visa` and `mc`, and form factors are `virtual` and `physical`. Adyen contact guidance qualifies relevant brand variants and certain card settings. Authentication data is conditionally required for cards usable for online payments in the EEA/UK or digital wallets; the phone object has mobile-number requirements and an ownership-verification instruction. A provided `configuration` object requires `configurationProfileId`.
- The optional `bankAccount.formFactor` defaults to `physical` for NL, US and UK business accounts. The described virtual DE/FR local IBANs refer to a physical NL account and route funds through the NL central bank. These are schema descriptions and examples, not account-opening or funds-movement proof.
- Omitted `status` generally defaults to `active`, with exceptions by card form factor and issuing country; the page gives US physical cards defaulting to `inactive` as an example. `closed` is permanent and cannot be undone. If `statusReason` is `other`, `statusComment` must accompany it. Do not infer a universal active-card default.
- A 200 response documents a succeeded request and includes a payment-instrument `id`; `bankAccount` or `card` details are conditional on the requested type. The response says PAN is masked by default and PAN/CVC are returned only for single-use virtual cards in the POST response. The virtual-card success example includes full PAN/CVC but omits `usage`; it cannot establish that all virtual cards return these values. The physical-card example's masked PAN ends `5785` while `lastFour` says `2765`; preserve this sample inconsistency rather than using it as a matching invariant.
- Error classes are 400, 401, 403, 422 and 500. The generic 422 example describes changing `balanceAccountId` at certain statuses, which is not a creation rule for this POST. The capture names no credential role, live server, current `latest` version, verification approval, successful card payment, account funding or final transfer outcome.

## Detail locators

- `## Parameters` → request properties, conditional card authentication, configuration, country/form-factor behavior, status defaults and irreversible closure.
- `## Request examples` → NL/DE/FR/UK/US business-account and physical/virtual-card example requests.
- `## Responses` → success schema including conditional account/card fields, sensitive-card-data response limits, and generic error structures.
- `## Response examples` → illustrative success/error payloads and the card-example inconsistencies.

## Related

- [[adyen]] — provider.
- [[adyen-issuing]] — card product context.
- [[adyen-business-accounts]] — business-account product context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/paymentInstruments/2026-09-15|2026-09-15 captured API Explorer reference]]
