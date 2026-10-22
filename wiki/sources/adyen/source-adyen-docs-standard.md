---
title: "Adyen Standard online payments integration checklist"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/standard"
raw_files:
  - "adyen/docs/standard/2026-09-15.md"
tags: [adyen, standard-integration, online-payments, checkout, checklist]
---

## Overview

This 2026-09-15-captured [[adyen]] page defines **Standard** as a self-contained, bounded **online payments integration path** for newcomers, using a standard single-request API flow with either website Drop-in or Adyen-hosted Hosted Checkout. It is a guide and configuration tier within [[adyen-online-payments]], not evidence of a separate financial product, a deployed checkout or a successful payment (raw lines 15–19, 47–49).

## Key takeaways

- The page positions Standard as minimal server-side implementation with prebuilt client UI, Customer Area account/transaction/report management, and essential risk and dispute tools. Its “compliant out-of-the-box” wording is a product claim in the snapshot, not proof of a merchant's actual compliance, eligibility or configuration (raw lines 19–26).
- The checklist explicitly recommends staying inside sections directly linked from `/standard`: it says documentation outside that path contains additional features and configurations **unavailable to this Standard integration**. Do not transfer capabilities from broader Adyen online-payment guides into this bounded path without a Standard-linked guide establishing them (raw lines 28–32).
- The account/setup path covers test account, live application requirements, account structure, users and roles, MFA/SSO and notifications. The integration path uses the single-request flow and offers **Drop-in on the merchant website** or **redirect to Hosted Checkout**; Drop-in has a separate best-practices route. These are alternative UI presentations, not two simultaneous requirements (raw lines 34–57).
- The remaining checklist routes to post-authorization payment management and result codes, risk/disputes, balances and payout accounts, transaction/reconciliation reports, test and go-live checks, and reference catalogs. A checklist link does not establish completion of authorization, capture, settlement, payout, bank receipt, testing or go-live; child guides own their prerequisites and outcomes (raw lines 59–126).

## Detail locators

- Standard identity, advertised capabilities and bounded-documentation warning: raw lines 15–32.
- Account setup and Drop-in/Hosted Checkout choice: raw lines 34–57.
- Payment management, risk and disputes: raw lines 59–78.
- Finance and reporting routes: raw lines 80–104.
- Test, go-live and reference routes: raw lines 106–126.

## Related

- [[adyen-payments]]
- [[source-adyen-docs-online-payments]]
- [[source-adyen-docs-online-payments-build-your-integration]]

## Raw Sources

- [[raw/adyen/docs/standard/2026-09-15|Pinned Standard integration checklist]]
