---
title: "Stripe: Cards"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/cards"
raw_files:
  - "stripe-payments-cards-2026-11-07.md"
  - "stripe-cards-2025.md"
tags: [stripe, cards, card-brands, 3d-secure, sca, cartes-bancaires, interac, eftpos, apple-pay]
---

## Summary

Stripe's cards guide covers bank-linked debit and credit cards entered at online checkout, brand capability by Stripe account country and customer country, possible additional authentication, and regional card rules. Cards are enabled by default, but Stripe returns eligible methods according to amount, currency and payment flow; a listed brand capability does not establish eligibility or a completed charge for a particular account. Cards can also fund Link and wallets, whose payment-method presentation is distinct from the underlying card charge. See new raw lines 5-18.

## Brand Capabilities

The November online table lists Visa and Mastercard for all Stripe account countries; Amex excludes Brazil, Malaysia, Thailand and UAE and has a customer-country exception for India. Discover/Diners, China UnionPay, JCB and Cartes Bancaires have longer account-country lists; JCB 3DS support is qualified by a specific country list rather than global. Cartes Bancaires' wallet footnote remains Apple Pay. Consult new raw lines 36-61 for the full account-country, customer-country, 3DS and wallet matrix; these are separate axes.

| Brand | Stripe account-country summary | 3DS | Wallets in November table |
| --- | --- | --- | --- |
| Visa / Mastercard | All Stripe countries | Supported | Supported |
| American Express | All except BR, MY, TH, UAE | Supported | Supported |
| Discover / Diners | CA, JP, UK, US and listed EEA countries | Supported | Supported |
| China UnionPay | AU, CA, HK, MY, NZ, SG, UK, US, CH and EEA except Iceland | Supported | **UnionPay through Apple Pay on the web** per footnote 4 |
| JCB | AU, CA, HK, JP, NZ, SG, CH, UK, US and EEA except Iceland | Only listed countries | Supported |
| Cartes Bancaires | SEPA and listed additional countries | Supported | Apple Pay per footnote 2 |
| eftpos | Australia | Supported | **Apple Pay in AUD without manual capture** per footnote 3 |

**Dated wallet delta:** The 2026-05-01 table marked China UnionPay and eftpos wallets “Not supported” (old raw lines 49-52). The 2026-11-07 table changes those two cells to supported with the limited Apple Pay footnotes above (new raw lines 50-61). The UnionPay footnote documents support through Apple Pay **on the web**; it does not establish that every other wallet path is absent. The eftpos footnote documents Apple Pay in AUD without manual capture. Do not extrapolate either row to unlisted wallets, currencies, capture modes or integration paths. The older table remains valid as a dated record, not the current unqualified wallet answer. For separate eftpos routing and manual-capture context, see [[source-stripe-eftpos-australia]].

The guide describes most listed card brands as available without extra configuration, while Cartes Bancaires and Interac may need additional configuration. In integrations handling Link as card payments, a non-card method saved to Link can carry card brand `link`. See new raw lines 20-34.

## Brand Exclusion Controls

The guide lists three distinct options: a Stripe Radar rule to reject a brand, custom client code that checks card brand, and Payment Element filtering by brand **and funding type**. The Payment Element option was added in November; the May guide listed Radar and the client check only. A display/filter setting is different from Radar rejection and is not proof that a particular payment failed or was blocked. See old raw lines 58-63; new raw lines 63-69.

## Authentication and Regional Notes

A customer enters card details at checkout and may face extra verification depending on network and location. Some banks, especially in regulated regions such as Europe and India, may prompt authentication. The guide says Stripe Checkout, Payment Links and hosted invoice pages support 3DS by default; Payment Intents API, Setup Intents API, Elements and mobile SDKs are listed as configurable integration paths for Subscriptions and Connect. A SetupIntent concerns future-payment setup, not a successful charge. Neither capture says every European or Indian card transaction requires 3DS. See new raw lines 71-88; old raw lines 65-82.

Card-issuer-managed installments in some regions cannot be created by using Subscriptions or SetupIntents as installment products. For EU cards that have both a local network such as Cartes Bancaires and an affiliated network such as Visa or Mastercard, the guide says businesses are required to let cardholders choose which brand processes the transaction; it points to Elements or Payments APIs to enable that choice (old raw line 92; new raw line 98). The India section links RBI-related resources rather than specifying a universal card outcome. See new raw lines 90-102.

## Captured Asset

- `raw/assets/stripe-cards-payment-flow.svg` — payment-flow diagram linked from the May capture. The November capture uses a remote SVG URL; that asset-path change does not establish a payment behavior change.

## Related Pages

- [[stripe]] — Stripe company route.
- [[stripe-payment-methods]] — payment-method category and reciprocal cards source route.
- [[eftpos-australia]] — local network and qualified Apple Pay route.
- [[source-stripe-eftpos-australia]] — eftpos routing and manual-capture context; Apple Pay qualification is in this cards guide's November table.
- [[source-stripe-co-badged-cards-compliance]] — EU co-badged choice context.

## Raw Sources

- [[raw/stripe-payments-cards-2026-11-07|2026-11-07 cards guide]] — full newer capture with qualified Apple Pay rows and Payment Element filter option.
- [[raw/stripe-cards-2025|2026-05-01 cards guide]] — older full capture with unsupported UnionPay/eftpos wallet cells.
