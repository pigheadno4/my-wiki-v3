---
title: "Stripe: Stablecoin Payments"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/stablecoin-payments"
raw_files:
  - "stripe-payments-stablecoin-payments-2026-11-07.md"
  - "stripe-stablecoin-payments-2025.md"
tags: [stripe, stablecoin, crypto, usdc, usdp, usdg, connect, billing, wallets]
---

## Overview

The May 1 and November 7, 2026 overviews describe direct Stripe Crypto checkout. A customer selects Crypto, opens Stripe’s hosted page at `crypto.stripe.com`, connects a wallet, chooses a token and network, and completes the customer-authenticated payment. Stripe shows a completion notification and may return the customer to the merchant’s site. In the separate [Clover API changelog](../../raw/stripe-changelog-clover-2025-09-30-stablecoin-payments-processing-status-2026-11-07.md#L5-L22), a `crypto` PaymentIntent on `2025-09-30.clover` enters `processing` after blockchain submission. Stripe rejects cancellation in that state with `payment_intent_invalid_cancellation_state` and waits until payment finalization before redirecting. Check the actual Intent outcome separately. Stripe-balance settlement and external payout are separate steps.

## Buyer eligibility, business eligibility and currencies

Both product overviews describe global customer coverage excluding sanctioned countries. May limits acceptance to US businesses and states that completed payments settle in USD in the merchant’s Stripe balance. November lists the US and names the European Union, Hong Kong, Mexico and Switzerland in its private-preview prose. Its [detailed business-location list](../../raw/stripe-payments-stablecoin-payments-2026-11-07.md#L61-L100) also includes GI, LI and NO. The prose supplies no additional access label for those three bullets. Account eligibility and activation remain account-specific.

The November overview lists USD presentment and other presentment currencies in private preview. It describes completed payments settling in the merchant’s local currency in their Stripe balance. Both the [May](../../raw/stripe-payment-method-support-2025.md#L30-L68) and [November](../../raw/stripe-payments-payment-methods-payment-method-support-2026-11-07.md#L31-L71) cross-method eligibility matrices give the same direct method’s row as USD, US businesses and worldwide customers. Those rows report a currency column and business/customer geography. The dedicated overview provides the separate settlement wording and preview qualifications. Payout timing varies by network in both product overviews.

## Direct checkout tokens and networks

| Token | May 1, 2026 overview | November 7, 2026 overview |
| --- | --- | --- |
| USDC | Ethereum, Solana, Polygon, Base | Tempo, Ethereum, Solana, Polygon, Base |
| USDP | Ethereum, Solana | Ethereum, Solana. US only. |
| USDG | Ethereum | Ethereum. US only. |

The November glossary separately names OUSD and USDC for stablecoin balances and USDC.e for transfers on Tempo. [[source-stripe-stablecoins-on-link|Stablecoins on Link]] is a separate funding path for eligible US businesses with one-time, on-session USD payments. The [Dahlia API changelog](../../raw/stripe-changelog-dahlia-2026-04-22-stablecoin-payments-phantom-cash-and-usdt-2026-11-07.md#L5-L23) documents `phantom_cash` and `usdt` read-side `token_currency` values on `2026-04-22.dahlia`. These values are reporting evidence. Review the direct accepted-token table for the dated checkout list.

## Limit, refunds and disputes

The customer limit is USD 10,000 per transaction. Both overviews list full and partial refunds and say refunds go back as stablecoins to the customer’s original wallet. They list disputes as unsupported and say there is no dispute-to-chargeback withdrawal from the Stripe balance. Payment confirmation is customer-authenticated through the documented wallet flow.

## Products and capability differences

The product overviews cover Checkout, Elements, Connect and Stripe Billing for invoices and subscriptions. They also list Payment Links and Invoicing in Dashboard guidance. The overviews mark manual capture unsupported. Enable the method in Payment methods settings if using a supported front end. See [[source-stripe-accept-stablecoin-payments]] for the distinct direct acceptance guide and [[source-stripe-subscriptions-stablecoins]] for subscription integration.

The May and November cross-method captures each contain two sets of product and API rows that link this same direct stablecoin method. Preserve their differing labels.

| Capability | Dedicated stablecoin rows | Wallets rows |
| --- | --- | --- |
| Manual capture | Supported | Unsupported |
| SetupIntents and `setup_future_usage` | Private preview | Invite only |
| Subscriptions | Private preview | Invite only |
| Invoicing | Supported with the Invoicing cell’s `send_invoice` collection-method footnote for subscriptions | Supported |
| Customer Portal | Private preview | Supported |

The dedicated overview’s manual-capture exclusion and Billing coverage remain separately attributed. The [November dedicated product](../../raw/stripe-payments-payment-methods-payment-method-support-2026-11-07.md#L169-L173), [Wallets product](../../raw/stripe-payments-payment-methods-payment-method-support-2026-11-07.md#L188-L204), [dedicated API](../../raw/stripe-payments-payment-methods-payment-method-support-2026-11-07.md#L305-L307) and [Wallets API](../../raw/stripe-payments-payment-methods-payment-method-support-2026-11-07.md#L322-L338) rows retain those differences. The corresponding May rows carry the same distinctions. Account access, manual capture behavior and recurring execution remain unverified by these labels.

## Connect

Stripe documents all Connect charge types, provided each connected account has the crypto payment method enabled. Connected accounts with full Dashboard access, including Standard accounts, can enable it there. For accounts without that access, request `crypto_payments` from the account’s page in the platform Dashboard or through the API. Check the connected account’s `capabilities.crypto_payments` for `active`.

## Related

- [[stripe-stablecoin-payments]] — direct and Link payment evidence
- [[source-stripe-crypto-onramp]] — separate fiat-to-crypto purchase flow
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payments-stablecoin-payments-2026-11-07|November 7, 2026 direct Stablecoin Payments overview]] — full capture with dated eligibility, presentment, settlement, token and Connect scope.
- [[raw/stripe-stablecoin-payments-2025|May 1, 2026 direct Stablecoin Payments overview]] — earlier eligibility and settlement wording, supported token networks and retained hosted flow diagrams.
