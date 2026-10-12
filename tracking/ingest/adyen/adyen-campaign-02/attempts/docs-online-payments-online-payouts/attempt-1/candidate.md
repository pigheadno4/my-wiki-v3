---
title: "Adyen Online Payouts"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/online-payouts"
raw_files:
  - "adyen/docs/online-payments/online-payouts/2026-09-15.md"
tags: [adyen, payouts, payout-api, transfers-api, disbursements]
---

## Overview

This Adyen webpage snapshot describes sending funds to suppliers, partners, or customers through the legacy Payout API. It distinguishes instant card payouts from staged payouts to bank accounts or PayPal wallets and routes new integrations to the Transfers API. This is an outbound disbursement topic, separate from accepting online shopper payments.

## Key takeaways

- Adyen says it no longer accepts new Payout API integrations. New integrations should use the Transfers API via Adyen's Payouts documentation; existing Payout API integrators are directed to their Adyen contact for migration information. The Transfers API is described as supporting multiple payout use cases, instant payouts, and more detailed webhooks with defined transfer states.
- The legacy Payout API requires additional Adyen approval and configuration. Its instant card payout path uses a single API request, immediately returns the payout-attempt result, and is limited here to Visa and Mastercard debit or credit cards.
- The staged path uses two API requests and a four-eye review: someone other than the submitter must confirm and check each payout. It assigns separate credentials for submission/storage and confirmation/decline. This snapshot lists bank transfers and PayPal wallets under staged payouts.
- The snapshot's recipient-region table is method-specific. It says payouts can be made only in local currency and that a local entity is required in most cases. Treat its country/method entries as snapshot evidence, not a current eligibility or account-approval determination.

## Detail locators

- Opening and migration notice (raw lines 15–34): payout purpose, Payout API sunset for new integrations, Transfers API route, two payout types, and additional approval/configuration.
- `## Instant card payouts` (raw lines 36–47): immediate attempt result, card brands, enabled credential capabilities, and linked instant-card detail page.
- `## Payouts in stages` (raw lines 49–64): four-eye review, two credential roles, bank-account and PayPal-wallet destinations, and linked detail/example pages.
- `## Supported countries/regions` (raw lines 66–108): local-currency and local-entity qualifications plus recipient-region support matrix by instant card, bank, and PayPal method.

## Related

- Company: [[adyen]]
- Concept: [[adyen-payouts]]

## Raw Sources

- [[raw/adyen/docs/online-payments/online-payouts/2026-09-15|2026-09-15 Adyen Online payouts snapshot]]
