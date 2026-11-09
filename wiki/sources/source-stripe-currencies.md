---
title: "Stripe Docs — Supported currencies"
type: source
date_ingested: 2026-11-09
canonical_url: https://docs.stripe.com/currencies
original_format: webpage
raw_files:
  - "stripe-currencies-2026-11-07.md"
  - "stripe-currencies-2025.md"
tags: [stripe, currencies, presentment, settlement, integration-currency, minor-units, zero-decimal, isk, huf, twd, ugx, eea, minimum-charge]
---

## Summary

Stripe's supported-currencies guide describes 135+ charge currencies, payment-method/presentment/settlement currencies, API amount formatting, special currency rules, charge minima and maxima, and its EEA card-pricing grouping. Currency and payment-method availability still depend on the Stripe account's country and applicable method. This is a documentation snapshot, not proof of account eligibility or payment authorization. [November 2026 capture](../../raw/stripe-currencies-2026-11-07.md#L5-L54)

## Currency roles and API amounts

- **Payment method currency** is the currency of the customer's card or bank account; **presentment currency** is the charge currency; **settlement currency** is the currency accepted by the destination bank account or debit card. An issuer might charge the customer an FX fee when payment-method and charge currencies differ, or when the payment method and business are in different countries. Stripe converts a charge when presentment and settlement currencies differ. Additional settlement currencies are supported in certain countries; conversion costs are covered by Stripe pricing. [November capture](../../raw/stripe-currencies-2026-11-07.md#L13-L25)
- **Integration currency** is the currency set on a Price or PaymentIntent. It appears in the Dashboard and is the currency Stripe Tax uses to record tax liability in Stripe Tax reports. [November capture](../../raw/stripe-currencies-2026-11-07.md#L27-L29)
- API `amount` uses integer minor units: `1000` means 10 USD and `10` means 10 JPY. Presentment currencies are two-decimal unless identified as zero-decimal; use lowercase three-letter ISO codes in payment requests. The zero-decimal list expresses general API support, not availability in every account country. [November capture](../../raw/stripe-currencies-2026-11-07.md#L35-L54)
- **American Express:** an asterisk-marked currency is unsupported in every Stripe account country. An unmarked currency might still be unavailable for Amex in a particular account country. [November capture](../../raw/stripe-currencies-2026-11-07.md#L39-L41)

## Special currency rules

| Currency | Rule |
| --- | --- |
| ISK | Zero-decimal currency represented in the API as a two-decimal amount ending `00`; 5 ISK = `500`, with no fractional ISK charge. |
| HUF | Charges can use two decimals; manual payout `amount` must be divisible by 100. |
| TWD | Charges can use two decimals; manual payout `amount` must be divisible by 100. |
| UGX | Zero-decimal currency represented in the API as a two-decimal amount ending `00`; 5 UGX = `500`, with no fractional UGX charge. Fractional invoice amounts resulting from prorations, coupons or taxes are rounded to the nearest multiple of 100, with the difference credited or debited to the customer balance. |

These conditions are present in both the May and November captures. [November capture](../../raw/stripe-currencies-2026-11-07.md#L56-L65); [May capture](../../raw/stripe-currencies-2025.md#L49-L58)

## Minimum charge amounts (selected)

The minimum depends on the payout bank account's settlement currency. A charge converted into the account's default settlement currency must meet that currency's equivalent minimum. Subscription charges can be zero for coupons or free trials; a nonzero amount still faces the applicable minimum. Selected listed amounts: 0.50 USD / 0.30 GBP / 0.50 EUR / 0.50 AUD / 0.50 CAD / 50 JPY / 50 KRW / 175 HUF / 4.00 HKD. Some payment methods have exceptions: iDEAL permits `amount` as low as `1`. [November capture](../../raw/stripe-currencies-2026-11-07.md#L67-L113)

## Maximum charge amounts

> [!warning] Contradiction
> The May 2026 capture grouped maximums chiefly by currency and described eight digits for most currencies plus LBP/COP/HUF/JPY card exceptions. The November 2026 capture instead separates card-network and non-card limits. Use the applicable network, method, currency and region rules for an operational limit; omission of an older example does not establish discontinued support. The May COP/HUF/JPY examples also have inconsistent stated digit counts and numeric values. [May capture](../../raw/stripe-currencies-2025.md#L108-L126); [November capture](../../raw/stripe-currencies-2026-11-07.md#L115-L140)

- **Cards, November capture:** most card payments support up to 12 minor-unit digits (`999999999999`); Cartes Bancaires supports 10 (`9999999999`); American Express supports 9 (`999999999`) in most currencies. Networks may set tighter limits by currency or region. JCB, Diners Club and Discover processed from Japanese Stripe accounts have an 8-digit JPY maximum (`99999999`). [November capture](../../raw/stripe-currencies-2026-11-07.md#L119-L129)
- **Other payment methods, November capture:** IDR supports 12 minor-unit digits (`999999999999`), COP 10 (`9999999999`), INR 9 (`999999999`), and all other currencies 8 (`99999999`), subject to tighter payment-method-specific limits. These are API amount ceilings in the captured guide, not guaranteed accepted charges. [November capture](../../raw/stripe-currencies-2026-11-07.md#L131-L140)

## Card examples and EEA pricing grouping

The May capture gives a Singapore card example; the November capture gives a Japan card example. The change of example does not establish that Singapore card support ended. Additional payment methods depend on the account country. [May capture](../../raw/stripe-currencies-2025.md#L128-L132); [November capture](../../raw/stripe-currencies-2026-11-07.md#L142-L146)

Stripe's captured EEA card-pricing list contains 43 country or territory entries in both captures, including the UK, Türkiye, Faroe Islands and Greenland. It is Stripe's fee-classification inventory in this guide, not an independent legal EEA definition or a fixed fee quote. EEA-issued card fees can vary with issuing region and transaction currency. [November capture](../../raw/stripe-currencies-2026-11-07.md#L148-L196); [May capture](../../raw/stripe-currencies-2025.md#L134-L182)

For countries with foreign-exchange controls, including Brazil, the guide says remittance uses authorized channels under applicable law. Connect platforms have additional currency-conversion considerations. [November capture](../../raw/stripe-currencies-2026-11-07.md#L31-L33); [November capture](../../raw/stripe-currencies-2026-11-07.md#L198-L200)

## Related Pages

- [[stripe-currencies]] — currency concept and reciprocal source route
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-currencies-2026-11-07|November 2026 webpage capture]] — verbatim content (205 lines)
- [[raw/stripe-currencies-2025|May 2026 webpage capture]] — verbatim content (191 lines)
