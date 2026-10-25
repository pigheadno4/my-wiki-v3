---
title: "Napas card for API only"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/napas-card/api-only"
raw_files:
  - "adyen/docs/payment-methods/napas-card/api-only/2026-09-15.md"
tags: [adyen, napas-card, vietnam, api-only, redirect, online-payments]
---

## Overview

This [[adyen]] page, metadata-modified 2019-09-06 and captured 2026-09-15, describes a **NAPAS card API-only** add-on to an existing integration with a merchant-built payment form. The shopper is redirected to the NAPAS website or app, then the merchant checks `/payments/details` after return or waits for webhooks if the shopper does not return. The page is a historical guide, not proof of current VN/VND merchant eligibility or successful authorization, capture, settlement or refund. See [[adyen-online-payments]] and raw lines 15–26, 150–228.

## Key takeaways

- Prerequisites are an existing API-only integration and adding NAPAS card in the **test Customer Area**. The merchant form may show NAPAS card without collecting shopper information on that form; the subsequent NAPAS redirect handles the shopper's payment step. If using `/paymentMethods` discovery, the guide specifies `countryCode: VN`, `amount.currency: VND`, payment amount, and channel `Web`, `iOS`, or `Android`. Those are this page's discovery parameters, not general merchant approval or a complete native SDK integration. See raw lines 21–41.
- **Material identifier conflict:** despite the NAPAS card title and flow prose, the page says `/paymentMethods` returns `paymentMethod.type: momo_atm` and repeats `momo_atm` in `/payments` requests and the redirect action. This may be a copied or shared identifier, but the snapshot does not resolve why a NAPAS-labeled guide uses a MoMo-prefixed type. Verify the method mapping from the applicable current provider response before implementing; do not silently relabel `momo_atm` as a NAPAS-specific code. See raw lines 15–19, 41–47, 62–65 and 154–164.
- The merchant server sends `/payments` with the returned method type and a `returnUrl`; the illustrated response is `RedirectShopper` with `action.type: redirect`, GET method and an `action.url`. Redirect the shopper to that returned URL, with the guide recommending system/default-browser approaches for mobile compatibility rather than in-app WebView. The cURL `/v68/payments` and `/v72/payments/details` paths are separate **examples**, not a stated cross-version requirement. Request/action and shopper redirect are not authorization. See raw lines 43–67, 150–176 and 182–193.
- After the shopper returns, the page instructs POST `/payments/details` with URL-decoded `redirectResult`; use its `resultCode` to present a shopper status and `pspReference` as Adyen's transaction identifier. The `Authorised` sample is illustrative, not observed outcome. `Cancelled` and `Refused` call for different shopper follow-up, while `Pending`/`Received` explicitly require waiting for the **AUTHORISATION webhook** for the final result. If the browser closes without returning, rely on webhooks: `AUTHORISATION` false/true distinguishes failed versus successful payment, and `OFFER_CLOSED` true indicates the shopper did not complete the payment and the order timed out. None of these statements alone proves capture, settlement or refund. See raw lines 178–228.
- Test directions give scenario-specific NAPAS card/OTP fixtures and test Customer Area status lookup; they do not show a real transaction or authorize use of live credentials. A separate request for NAPAS card in the **live Customer Area** is required before live acceptance. This page does not provide recurring-token, capture or refund procedure. See raw lines 230–249.

## Detail locators

- API-only prerequisite, form scope, VN/VND/channels and `momo_atm` discovery mismatch: raw lines 21–41.
- TEST `/payments` request examples and return URL: raw lines 43–148.
- Redirect action, mobile browser advice, `/payments/details` and illustrative `Authorised` response: raw lines 150–207.
- Shopper-facing result states and browser-close webhook outcomes: raw lines 209–228.
- Test scenarios, test-status lookup and separate live request: raw lines 230–243.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/napas-card/api-only/2026-09-15|NAPAS card API-only guide — captured 2026-09-15]]
