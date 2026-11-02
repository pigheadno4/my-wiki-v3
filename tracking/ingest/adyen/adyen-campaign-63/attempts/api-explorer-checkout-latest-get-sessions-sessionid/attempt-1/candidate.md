---
title: "Adyen Checkout API: GET /sessions/{sessionId}"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/get/sessions/(sessionId)"
raw_files:
  - "adyen/api-explorer/Checkout/latest/get/sessions/(sessionId)/2026-11-02.md"
tags: [adyen, checkout, sessions, api]
---

## Overview

The 2026-11-02 capture of the Checkout API Explorer GET /sessions/{sessionId} reference describes retrieving a payment session result. Its listed server is Checkout TEST v72. Supply the unique session ID as a path parameter and the Drop-in or Component's sessionResult as a required query parameter. The returned status is a session status; payment entries, if present, describe authorised payments for the session. [[adyen]] [[adyen-online-payments]]

> [!warning] Contradiction
> The introductory sentence says both sessionId and sessionResult are "specified in the path," but the parameter tables place sessionId in the path and sessionResult in the query. Follow the explicit parameter tables when reading this captured reference; this source does not establish runtime behavior.

## Key takeaways

- The response fields additionalData, id, payments, reference and status are all marked optional. additionalData can depend on Customer Area Additional data settings. The payment list is described as all authorised payments for this session, while its optional resultCode field also lists Received and Pending. Preserve that schema/description tension; do not infer that every list item is finally authorised.
- A payment entry may include an authorised amount (currency and minor-unit value required within that amount object), paymentMethod, pspReference and resultCode. paymentMethod is only returned for resultCode Authorised; brand is only returned for scheme. The merchant-provided reference comes from the original /sessions request, whereas pspReference is Adyen's transaction/request reference.
- Payment resultCode values listed here are Authorised, Received and Pending. Authorised is described as final authorisation; Received is initial receipt and Pending lacks a final payment status. These do not establish capture or settlement.
- Session status values are completed, paymentPending, refused, canceled and expired. The reference explicitly says the returned session status does not get updated and warns against repeating this request for payment status updates. Refused follows too many refused attempts; canceled is shopper cancellation; expired blocks further completion. The default expiry is one hour after session creation.
- This captured endpoint provides no authentication header, idempotency contract, error response schema, deletion behavior, payment modification or reversal contract. The single success example shows id CS12345678 and completed; it does not establish broader outcomes or live availability.

## Detail locators

- Server and required inputs: raw lines 9–23.
- Response fields and nested requiredness: raw lines 25–45.
- Payment and session enum meanings, immutable status warning and default expiry: raw lines 43–45.
- Success example: raw lines 47–56.

## Related

- [[source-adyen-api-explorer-checkout-latest-post-sessions]] — session creation, distinct operation.
- [[adyen-online-payments]] — main concept and source route.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/get/sessions/(sessionId)/2026-11-02|2026-11-02 Checkout API Explorer GET session result]]
