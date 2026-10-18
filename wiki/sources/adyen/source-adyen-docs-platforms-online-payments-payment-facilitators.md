---
title: "Adyen Platforms online payment-facilitator transaction data"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments/payment-facilitators"
raw_files:
  - "adyen/docs/platforms/online-payments/payment-facilitators/2026-09-15.md"
tags: [adyen, platforms, online-payments, payment-facilitators, sub-merchants]
---

## Overview

This 2026-09-15 Adyen for Platforms guide describes the extra user or sub-merchant data a payment facilitator sends with online Checkout authorization. It says that, for a transaction facilitated by the platform, the user is considered Merchant of Record for the card-scheme data requirement. That statement is scoped to facilitated transactions in this guide; it does not by itself establish the legal seller, payee, funds owner, or settlement terms for another platform model or transaction.

## Key takeaways

- The stated prerequisites are an Adyen online payments integration with a checkout UI and Checkout API credentials. For each `/sessions` or `/payments` authorization, the card-scheme data identifies the user by a unique platform-assigned ID, an accurate name for the shopper statement (including a Mastercard aggregator prefix), and the user's transaction location. The page says Adyen repopulates user details from the initial payment for later cancellations, captures, and refunds.
- Send `AdditionalDataSubMerchant` under `additionalData.subMerchant.subSeller1.[parameter]`; this page fixes `subSellerNr` and `subMerchant.numberOfSubSellers` to 1. Its required-parameters table covers ID, name, street, postal code, city, state where applicable, three-letter country code, email, and phone. Postal code is specified only for Canada and the United States. The displayed request examples omit email and phone despite their appearance in that table; use the relevant current Checkout contract and Adyen configuration guidance for an actual integration.
- Before live use, confirm with an Adyen contact that `paymentFacilitatorIds`, `aggregatorPrefix`, and `amexCapnSubmitterId` are configured for the platform. The guide says most payment methods permit ecommerce facilitation under an aggregated MID, which does not imply every method or account is eligible.
- The `/payments` split example routes an illustrated sale amount to a user balance account, commission to the platform, and `PaymentFee` to a named balance account. It is a request example, not authorization, booking, payout, or legal-ownership evidence. The curl sample uses Checkout v72 on the test endpoint; SDK samples name language-specific versions and test environments, with live endpoint prefix called out. The Node JavaScript sample uses EUR where the other displayed amount examples use USD, so do not treat the examples as one reconciled transaction.
- For shopper statement recognition, the page recommends a recognizable platform brand or merchant name. If the platform does not use stores, it says to configure the transaction description; a transaction-specific `shopperStatement` may additionally be supplied depending on that configuration. This guide does not itself define the store configuration or prove a displayed descriptor.

## Detail locators

- `## Requirements` and `## Send user data points with a transaction`: integration and credential prerequisites, scoped Merchant-of-Record statement, authorization timing, required user identity/location.
- `### Required parameters`: `AdditionalDataSubMerchant` names, `subSeller1` and one-sub-seller values, country-specific postal code, later-modification population, and pre-live account configuration.
- `Here is an example of a split payment request facilitated on behalf of your user`: Checkout v72 test curl and versioned SDK request samples, split fields, sample omissions and currency discrepancy.
- `## Shopper statement`: descriptor risk, recognizable-name guidance, no-store configuration, optional per-request `shopperStatement`.

## Related

- [[adyen-platforms]] — main Platforms concept and source route.
- [[adyen-pos-payment-facilitators]] — separate in-person facilitator guide with different store and Terminal API data paths.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/payment-facilitators/2026-09-15|Adyen payment facilitators (fetched 2026-09-15)]]
