---
title: "Stripe Docs — Import 3D Secure results"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/payment-intents/three-d-secure-import"
raw_files:
  - "stripe-payments-payment-intents-three-d-secure-import-2026-11-07.md"
  - "stripe-3ds-import-2025.md"
tags: [stripe, 3d-secure, 3ds-import, travel, cryptogram, cartes-bancaires, pci-dss, exemption]
---

## Summary

The May 8 and November 7, 2026 guides cover importing external 3DS results into Stripe from a travel aggregator or third-party 3DS provider. Importing authentication and confirming an Intent do not establish authorization or payment success.

## Availability and access

- Both captures list AU, CA, CH, EU, GB, HK, MX, NZ, SG and US as available and exclude IN, MY and TH. The May 8 capture labels other Stripe card-payment locations **Beta**. The November 7 capture labels them **Private preview**.
- Raw-card API access requires validation of PCI DSS compliance, submission to Stripe review and agreement to maintain additional controls on top of Stripe's default security settings. For accounts with custom pricing, naming Stripe as acquirer in the 3DS request triggers applicable network-cost pass-through per the account agreement.

## Import paths

1. **PaymentIntent with raw card data.** The merchant server creates and confirms a PaymentIntent in one call with card details and external 3DS data.
2. **PaymentIntent with a PaymentMethod ID.** The merchant server creates and confirms in one call with the existing PaymentMethod ID and external 3DS data. Use raw card data instead if the payment is shortly after tokenization, subject to the raw-card access requirements above.
3. **SetupIntent for future payments.** Create and confirm a SetupIntent with a non-payment authentication cryptogram and either card details or a PaymentMethod ID. Both captures show `confirm=true` on this setup path.

The `three_d_secure` parameters must exactly match the external provider's values. The examples use `payment_method_options.card.three_d_secure` with version, ECI, cryptogram and transaction ID. The two PaymentIntent import directions specify `confirm=true` and `error_on_requires_action=true` to prevent Stripe from attempting 3DS during a soft decline. Both captures' PaymentIntent instructions link the `confirm` label to a SetupIntent reference, while the prose and examples identify PaymentIntent create-and-confirm. The SetupIntent example does not use the soft-decline flag. November changes example language from Node.js to cURL and includes sample return URLs, with no general parameter or payment-method-default change established by those examples.

## Exemption import

For an externally obtained low-risk SCA exemption, pass `exemption_indicator=low_risk`. Stripe requests the exemption from the issuer if its real-time transaction risk analysis determines it is appropriate. In the expanded `latest_charge`, inspect `payment_method_details.card.three_d_secure.exemption_indicator_applied` to learn whether Stripe requested the exemption. That signal does not establish issuer approval.

## Cartes Bancaires

For transactions that process on Cartes Bancaires, explicitly set the authenticated network to `cartes_bancaires`. The cryptogram guidance applies to PaymentIntent and SetupIntent imports. It requires `cb_avalgo` and recommends including ECI, `cb_exemption`, `cb_score`, `ares_trans_status` and `requestor_challenge_indicator` when available.

For an SCA exemption granted over 3DS, supply `cb_exemption`, `exemption_indicator` or both. Prefer `cb_exemption` alone if available. Stripe infers the exemption indicator from it. If both are supplied, they must agree on the exempted status. Stripe rejects the documented mismatch where `exemption_indicator=none` and the `cb_exemption` bitmap indicates low risk. If either indicates low risk due to acquirer transaction risk analysis, Stripe reassesses the transaction.

## Sandbox tests

- Authentication-required fixtures include `4000002760003184` and `pm_card_authenticationRequired`. The sandbox accepts correctly formatted 3DS results. The dated raw captures provide the v2.1.0 and v2.2.0 samples.
- The standard low-risk negative fixture uses card `4000000000016123` with `exemption_indicator=low_risk` to return `exemption_indicator_applied=false`. The same card is listed in the Cartes Bancaires tests, where the negative case is scoped to a low-risk `cb_exemption`.
- The Cartes Bancaires co-badged card fixtures also include `4000002500001001` (Visa) and `5555552500001001` (Mastercard). The raw guides have separate token and PaymentMethod tables.

## Detail locators

| Topic | May 8 raw lines | November 7 raw lines |
| --- | --- | --- |
| Availability and exclusions | 15–34 | 16–35 |
| PaymentIntent and SetupIntent examples, field matching and tokenization | 36–146 | 37–113 |
| Low-risk issuer request and Charge signal | 148–213 | 115–170 |
| Cartes Bancaires fields and exemption consistency | 215–279 | 172–222 |
| Sandbox fixtures and negative cases | 281–336 | 224–279 |
| Raw card access and pricing | 338–350 | 281–293 |

## Related Pages

- [[stripe-3d-secure]] — 3D Secure concept and external import route
- [[source-stripe-standalone-3ds]] — Standalone 3DS authentication on Stripe
- [[stripe]] — Stripe company page
- [PaymentIntent 3D Secure options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card-three_d_secure) — API reference linked by both guides

## Raw Sources

- [[raw/stripe-payments-payment-intents-three-d-secure-import-2026-11-07|November 7, 2026 full guide]]
- [[raw/stripe-3ds-import-2025|May 8, 2026 full guide]]
