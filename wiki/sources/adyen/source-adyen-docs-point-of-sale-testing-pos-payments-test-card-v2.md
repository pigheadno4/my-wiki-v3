---
title: "Adyen blue-green POS physical test card v2"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/testing-pos-payments/test-card-v2"
raw_files:
  - "adyen/docs/point-of-sale/testing-pos-payments/test-card-v2/2026-09-15.md"
tags: [adyen, point-of-sale, test-card, cardholder-verification, offline-payments, declines]
---

## Overview

This Adyen Docs page describes the blue-green **physical POS test card v2** and its programmed applications for simulated payment method, locale, issuer country/region, currency, and cardholder verification (CVM) scenarios. It also gives offline and decline triggers for testing a POS app and terminal in the test environment. These are simulation fixtures; the page does not prove real issuer approval, live card acceptance, capture, or settlement.

## Key takeaways

- Choose a test-card application by the payment request's currency, or select it on the terminal after inserting the card at **Present card**. The chip applications shown are Mastercard or Maestro, and the table also contains an MSR Visa row; do not infer that every listed application supports every interface. The Brazil `mc pt bra brl` application is linked to installment testing. Test transactions can be inspected in test Customer Area. Contactless and mobile Tap to Pay testing with this card require physical card version **2.4 or later**, printed on its back.
- CVM selection depends on application, amount, and currency. The page's table uses strict thresholds above 100.00 and 200.00 in the application's currency for CVM 2 and CVM 1, respectively; after DCC, the converted amount must exceed the threshold. Online PIN accepts any entered code in the inserted-card test flow, while an invalid offline PIN declines. Contactless PIN depends on the terminal location's country/region reader limit, whose latest value is in test Customer Area; do not treat the table as a universal live limit.
- For offline EMV tests, ask Support to configure chip floor and offline refund limits, then force internet loss. Each application has a counter. The narrative says the first three in-limit offline transactions are accepted and the fourth declines, with reset by an online inserted-chip transaction; contactless cannot reset the shared UK Mastercard counter. **Qualification:** the application table separately marks `ms nl nld eur` as **Always decline** offline, so do not apply the general three-acceptance sentence to that application without resolving the discrepancy.
- Decline simulations use the **last three digits** of requested amount. The table maps triggers to `Result`, `ErrorCondition`, and additional-response context; the 139 trigger becomes a partial payment rather than failure when `AllowPartialAuthorisation` is used. Some triggers require terminal action (such as canceling PIN entry or contactless fallback); 156, 160, and 161 are marked for Adyen internal testing only. `refusalReason`, `message`, and raw issuer/acquirer responses are extra diagnostic context and must not be coded against. Classic-library integrations can show a generic `DECLINED_ONLINE` result for the same simulations.

## Detail locators

- Physical card purpose, version gate, test Customer Area route: `# Blue-green Adyen point-of-sale test card`, raw lines 15–34. Per-application method, country/region, currency, PAN, AID, and interface differences: `## Card applications`, lines 36–52, and CVM table, lines 76–86.
- CVM thresholds, DCC, online/offline PIN, and country/region contactless limit: `## Testing CVMs`, raw lines 54–93. Offline setup, per-application counter, and the Maestro table exception: `## Testing offline transactions`, lines 95–103, together with table line 82.
- Amount-ending decline map and conditional exceptions: `## Simulating declined payments`, raw lines 105–168. For 139 plus `AllowPartialAuthorisation`, see line 143; internal-only 156/160/161 at lines 157, 161–162. Raw response instability and optional routes: `## Raw responses`, lines 170–179.

## Related

- [[adyen]] — provider context.
- [[adyen-payment-testing]] — test-fixture and simulated-outcome boundary.
- [[adyen-terminal-api]] — request/response vocabulary; this card does not establish live Terminal API behavior.
- [[source-adyen-docs-point-of-sale-testing-pos-payments]] — broader POS testing overview.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/testing-pos-payments/test-card-v2/2026-09-15|Adyen Docs: Blue-green Adyen point-of-sale test card (2026-09-15 snapshot)]]
