---
title: "Adyen Card Payouts"
type: concept
category: technology
tags: [adyen, payouts, cards]
---

## Overview

Adyen card payouts send funds to eligible recipient cards for disbursements or money transfers. The 2026-09-15 instant card payouts guide documents a legacy Payout API `/payout` flow, but states Adyen no longer accepts new Payout API integrations and directs new integrations to the Transfers API. Existing Payout API integrators are directed to contact Adyen about migration. The legacy guide is subject to Adyen enablement, compliance approval, card eligibility, data validation and domestic payout limits; cross-border cases require contacting Adyen.

## Sources

- [[source-adyen-api-explorer-payout-latest-post-payout]] — 2026-09-15-captured, deprecated Payout API v68 TEST `POST /payout` instant Visa/Mastercard card-payout reference; issuer-dependent 30-minute availability and payment-style result codes do not prove cardholder receipt.


- [[source-adyen-docs-payouts-payout-service-pay-out-to-cards-manage-card-details]] — 2023-modified Payout Service guide to PCI-gated third-party card collection, zero-auth eligibility and post-authorization tokenization before a separate Transfers API card payout; distinct from the legacy Payout API flow.


- [[source-adyen-docs-online-payments-online-payouts-instant-payouts]] — Adyen instant card payouts webpage, legacy Payout API guide with Transfers API migration direction, use cases and eligibility/region limits (webpage snapshot, 2026-09-15).
