---
title: "Adyen SoftPOS configuration API v3: create a communication session"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/softpos-configuration-api/latest/post/auth/certificate"
raw_files:
  - "adyen/api-explorer/softpos-configuration-api/latest/post/auth/certificate/2026-09-15.md"
tags: [adyen, softpos, mobile-pos, mobile-sdk, communication-session, api]
---

## Overview

This 2026-09-15 SoftPOS configuration API **v3** reference describes `POST /auth/certificate` creating a secure communication session between the Mobile SDK and Adyen payments platform through mutual authentication. The setup token identifies the SDK and device; returned SDK data supports authenticating platform responses. The page lists a TEST server and distinct live regional servers for Australia, Asia Pacific South East, Europe, North East Asia, and the United States. See [[adyen]] and [[adyen-mobile-pos]].

## Key takeaways

- The request body requires `merchantAccount` and the Mobile SDK-provided `setupToken`. The page names Android `MerchantAuthenticationService.authenticate(setupToken)` and iOS `PaymentServiceDelegate.register(with:)` callbacks as token routes. Optional `store` identifies the processing store, but must be omitted when merchant accounts are used as stores or the merchant is a registered payment facilitator.
- `subMerchantData` is marked optional in the table but its description makes it **required for a registered payment facilitator** and prohibited otherwise. Within a supplied object, `displayName`, `id`, `mcc`, and `name` are required. `email` and `phoneNumber` become required for American Express; `taxId` is required only in Brazil and for Cartes Bancaires in France, with country-specific format/length rules. The remaining address and contact fields are in raw lines 44–55.
- The header table marks `X-API-Key` **No** while describing it as the API key used to authenticate API requests. This is a schema requiredness versus security-description tension, not proof unauthenticated requests work. The `401` response explicitly says authentication is required.
- A `201 Success` means the session request succeeded. The response table marks all listed fields optional: communication-session `id`, SDK `installationId`, `merchantAccount`, `sdkData`, and `store`. If a backend creates a Terminal API transaction request, the page says to use `installationId` as `MessageHeader.POIID`; pass `sdkData` to the POS app for SDK response authentication. The introductory prose calls the return a “session token,” but the response schema does **not** expose a field by that name; it lists `sdkData` and `id` separately.
- Errors are `400` validation failure, `401` authentication required, `422` session request not processed, and `500` internal server error. Their problem-body fields are optional, with required `message`, `name`, and `value` only within a supplied `invalidFields` entry. The examples show placeholder identifiers and generic error codes; they do not prove a live session, transaction authorization, capture, settlement, or bank receipt. This page states no session expiry, renewal/revocation, retry timing, asynchronous outcome, or payment-result contract.

## Detail locators

- Purpose, token direction and server environments: raw lines 5–27.
- API-key header and request fields, SDK callback routes and conditional facilitator/store data: lines 29–55.
- Illustrative request: lines 57–66.
- 201 response fields and Terminal API installation-ID relationship: lines 67–79.
- Error meanings and problem schemas: lines 82–155.
- Illustrative 201 and 400/401/422/500 bodies: lines 157–218.

## Related

- [[adyen]] — provider route.
- [[adyen-mobile-pos]] — Mobile POS SDK and merchant-app context.
- [[adyen-pos-payment-facilitators]] — separate POS facilitator context for conditional sub-merchant data.
- [[source-adyen-docs-point-of-sale-mobile-ios-understand]] — separate iOS Mobile session guide.

## Raw Sources

- [[raw/adyen/api-explorer/softpos-configuration-api/latest/post/auth/certificate/2026-09-15|POST /auth/certificate API Explorer capture]]
