---
title: "Stripe Docs — Import 3D Secure results"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-3ds-import-2025.md"
tags: [stripe, 3d-secure, 3ds-import, travel, cryptogram, cartes-bancaires, pci-dss, exemption]
---

## Summary

Integration guide for importing external 3DS authentication results into Stripe's Payment Intents API. Used by travel industry (aggregators like Expedia/Sabre) or businesses using third-party 3DS providers.

## Key Facts

- **Availability**: AU/CA/CH/EU/GB/HK/MX/NZ/SG/US (GA); beta elsewhere; excluded: IN/MY/TH
- **Raw card data**: requires PCI DSS validation + Stripe review process
- **Always required**: `confirm: true` + `error_on_requires_action: true`
- **3DS params**: `payment_method_options.card.three_d_secure: { version, electronic_commerce_indicator, cryptogram, transaction_id }`

## Three Integration Paths

1. **Raw card data**: `payment_method_data.card` + `three_d_secure` in one PaymentIntent
2. **PaymentMethod ID**: existing `payment_method` + `three_d_secure`
3. **SetupIntent** (future payments): non-payment authentication cryptogram

## Exemption Import

Set `exemption_indicator: 'low_risk'` → Stripe re-assesses via TRA. Check `exemption_indicator_applied` on Charge via `expand: ['latest_charge']`.

## Cartes Bancaires

Must add `network: 'cartes_bancaires'` plus:

| Field | Required |
| --- | --- |
| `cb_avalgo` | Required |
| `cb_exemption` | Optional |
| `cb_score` | Optional |
| `ares_trans_status` | Optional |
| `requestor_challenge_indicator` | Optional |
| `electronic_commerce_indicator` | Optional |

## Test Values

Card: `4000002760003184` or `pm_card_authenticationRequired`

Sample (v2.1.0): ECI=`02`, cryptogram=`M6+990I6FLD8Y6rZz9d5QbfrMNY=`, txn_id=`5f5d08f2-...`

Sample (v2.2.0): ECI=`05`, cryptogram=`4BQwsg4yuKt0S1LI1nDZTcO9vUM=`, txn_id=`f879ea1c-...`

Cartes Bancaires test cards: `4000002500001001` (CB/Visa), `5555552500001001` (CB/MC), `4000000000016123` (exempt not applied)

## Related Pages

- [[stripe-3d-secure]] — 3D Secure concept page (Import 3DS section)
- [[source-stripe-standalone-3ds]] — Standalone 3DS (run auth on Stripe for any PSP)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-3ds-import-2025]] — verbatim webpage content (354 lines; standard linter reformatting)
