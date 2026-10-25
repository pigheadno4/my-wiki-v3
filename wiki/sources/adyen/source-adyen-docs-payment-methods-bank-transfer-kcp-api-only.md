---
title: "Bank Transfer via KCP for API only"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bank-transfer-kcp/api-only"
raw_files:
  - "adyen/docs/payment-methods/bank-transfer-kcp/api-only/2026-09-15.md"
tags: [adyen, bank-transfer, kcp, korea, api-only]
---

## Overview

This 2026-09-15 snapshot describes the Bank Transfer via KCP add-on for an existing Adyen Web API-only integration, with South Korea (`KR`) and Korean won (`KRW`) in the method-discovery request. It is a method-specific supplement to the main Advanced-flow API-only guide, not a complete standalone integration. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The merchant must have an existing API-only integration that handles `action.type: redirect` and add Bank Transfer via KCP in Customer Area. The merchant-built form includes the method but no additional method-specific fields. See raw lines 23–40.
- The `/paymentMethods` request specifies `countryCode: KR` and `amount.currency: KRW`; the example response identifies type `kcp_banktransfer`. The example uses Checkout test v72, but that example version is not a stated minimum. See raw lines 44–72 and 329–340.
- The example `/payments` request sends `paymentMethod.type: kcp_banktransfer`, amount, reference, return URL and merchant account; the example response has `RedirectShopper` and a `redirect` action. The existing integration handles that redirect. A redirect response or shopper return is not evidence of final payment authorization or settlement. See raw lines 342–368 and 660–676.
- The page's How it works step says to include additional information about items intended for purchase, but its `/payments` section says no additional parameters are needed and its sample contains no item fields. Preserve this on-page conflict; do not infer a required item schema from it. See raw lines 31–36 and 342–368.
- The Test and go live section says there are no KCP bank-transfer testing credentials because authorization requires a Public Identification Certificate, described as a digital signature for individuals. The TEST examples do not establish a runnable successful test payment, live readiness or current availability. See raw lines 678–680.

## Detail locators

- Requirements, flow and form: raw lines 23–42.
- Method discovery and request/response examples: raw lines 44–340.
- `/payments` examples, redirect response and handling: raw lines 342–676.
- Testing limitation: raw lines 678–680.

## Related

- [[adyen-online-payments]] — main online-payments concept.
- [[adyen]] — provider entry.

## Raw Sources

- [[raw/adyen/docs/payment-methods/bank-transfer-kcp/api-only/2026-09-15|Bank Transfer via KCP for API only (2026-09-15)]]
