---
title: "Enable Currency Conversion Using the FX Quotes API"
type: source
date_ingested: 2026-04-21
date_updated: 2026-11-15
canonical_url: "https://docs.stripe.com/payments/custom/localize-prices/fx-quotes-api"
original_format: webpage
raw_files:
  - "stripe-payments-custom-localize-prices-fx-quotes-api-2026-11-07.md"
  - "stripe-fx-quotes-api-2025.md"
tags: [stripe, fx-quotes, currency-conversion, localization, payment-intents, exchange-rate, preview]
---

## Summary

[[stripe]] offers the FX Quotes API as a **preview** service to retrieve live exchange-rate information or extended rate quotes for currency pairs. A merchant can use `exchange_rate` to pass the Stripe FX fee into a localized price or `base_rate` to absorb it, then attach an eligible quote ID to a PaymentIntent or Transfer for supported usage. A quote is not an FX transaction offer, permanent lock guarantee, completed payment or settlement. It may be withdrawn or invalidated. The feature is limited by access, MCC, currency pair, region, usage type and lock duration.

## Access, examples and terms

Request access through Stripe's form; certain MCCs are unsupported. Use must relate to commercial goods and services sold on Stripe; selective use of extended quotes only when favorable is prohibited. Stripe may change supported currencies without notice. The page's **Ruby beta SDK example** uses `stripe 14.0.0-beta.1` and `2025-07-30.preview`; the **direct secret-key curl example** instead sends `Stripe-Version: 2025-03-31.preview`. These are separate documented examples, not proof that either version is interchangeable across interfaces or that the beta SDK is required for direct curl. Secret-key operations belong on a server.

The quote request example uses `POST /v1/fx_quotes` with `to_currency`, `from_currencies[]` and `lock_duration`. The returned `fx_quote` identity has `rates[currency].exchange_rate`, `rate_details.base_rate`, `fx_fee_rate`, `duration_premium`, `lock_expires_at`, `lock_status`, and a usage type. The US-merchant example divides 100 USD by EUR→USD `exchange_rate` 1.06053 to show 94.29 EUR with FX fee passed to the customer, or by `base_rate` 1.08295 to show 92.34 EUR while absorbing it. Cross-border payment-method fees can also apply separately.

## Locks, fees and usage

| `lock_duration` | Group 1 fee | Group 2 fee |
| --- | --- | --- |
| `none` | no extended-rate fee; current live informational quote | no extended-rate fee |
| `five_minutes` | 0.07% | 0.12% |
| `hour` | 0.10% | 0.15% |
| `day` | 0.20% | 0.30% |

A pair involving a Group 2 currency uses the Group 2 premium; same-group pairs use that group's premium. **INR is Group 1 in both captures**, alongside USD, EUR, GBP and others. BRL, CNY, KRW, MXN and PLN are Group 2 examples. The older source summary mistakenly put INR in Group 2. The table is a fee-group list, not proof that a given merchant may lock a given pair.

Use a locked quote before `lock_expires_at`; significant rate movement can invalidate it sooner and change `lock_status` to `expired`. `fx_quote.expired` covers natural expiry **or** significant drift. Attaching an expired quote to a PaymentIntent or Transfer returns HTTP 400 with `payment_intent_fx_quote_invalid` or `transfers_fx_quote_invalid`, respectively; create a new quote and update prices. A mid-market fallback applies in some non-card payment methods taking more than 24 hours when an extended quote expires or becomes unusable; it is not a general lock guarantee. Disputes and refunds use the **current** exchange rate, not the former locked rate.

### Example inconsistency and minor units

The UK/US sample prose asks for `hour` but its curl quote request sends `lock_duration=day`. It says 125 USD, while the PaymentIntent request sends `amount=125`, which is **125 minor units**, not 125 USD for a two-decimal currency. Stripe API `amount` requires integer minor units; convert and round for the target currency, including zero-decimal currencies, before using an example. The sample PaymentIntent attaches `fx_quote=fxq_...` but does not prove creation, confirmation or settlement.

## Preview availability by region and usage (2026-11-07)

The earlier **2026-04-21** capture listed 33 countries in one flat preview list. The newer capture uses the following region/usage/duration matrix; `EU` is an aggregate row and does not alone prove withdrawal of individual EU countries from the older list. A listed preview region is not merchant-specific approval. `none` informational quotes are available for a usage type wherever a lock for that usage type is listed.

| Region | Payment locks | Transfer locks |
| --- | --- | --- |
| AU | five minutes, hour | five minutes, hour |
| BR | five minutes, hour | unsupported |
| CA | five minutes, hour, day | five minutes, hour |
| EU | five minutes, hour, day | five minutes, hour |
| GI | five minutes, hour, day | five minutes, hour |
| HK | five minutes, hour | five minutes, hour |
| IN | five minutes, hour | unsupported |
| JP | five minutes, hour | unsupported |
| MY | five minutes, hour | unsupported |
| MX | five minutes, hour | five minutes, hour |
| NZ | five minutes, hour | five minutes, hour |
| NO | five minutes, hour, day | five minutes, hour |
| SG | five minutes, hour | five minutes, hour |
| CH | five minutes, hour, day | five minutes, hour |
| TH | five minutes, hour | unsupported |
| AE | five minutes, hour | five minutes, hour |
| GB | five minutes, hour, day | five minutes, hour |
| US | five minutes, hour, day | five minutes, hour |

The November wording says the two fee groups cover currencies **supported by the API**, while the earlier page described currencies **supported for locking**; their lists and fees otherwise match. This wording change does not by itself establish account-specific presentment or payment acceptance.

## Related

- [[stripe]] — Stripe company page.
- [[stripe-fx-quotes-api]] — concept overview.
- [[source-stripe-checkout-local-currency]] — local-currency options.
- [[stripe-adaptive-pricing]] — automatic localization alternative.

## Raw Sources

- [[raw/stripe-payments-custom-localize-prices-fx-quotes-api-2026-11-07]] — full webpage capture fetched 2026-11-07 (229 lines).
- [[raw/stripe-fx-quotes-api-2025]] — earlier full webpage capture fetched 2026-04-21 (229 lines); filename's year is not the fetch date.
