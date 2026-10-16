---
title: "Adyen Mirakl"
type: concept
category: technology
tags: [adyen, mirakl, marketplace, platforms, seller-onboarding]
---

## Definition

Adyen's Mirakl connector links a Mirakl Marketplace to Adyen for Platforms for seller onboarding/KYC, account-data synchronization, balance control and domestic seller payouts. The overview is a 2019-last-modified page captured 2026-09-15; it does not itself establish present availability, geographic eligibility, completed verification or payment execution. [[source-adyen-docs-plugins-mirakl]]

## Integration boundary

The overview broadly says the operator-implemented payment split routes seller funds and collects commission; this describes the pay-in side. The separate Mirakl payout guide says the connector transfers commission and subscription fees to the liable balance account **after a successful seller payout**, so a pay-in split with `type`: **Commission** is **not required for that connector payout flow**. Do not turn either source into a universal split rule or assume the split and later internal transfer are the same action. [[source-adyen-docs-plugins-mirakl]] [[source-adyen-docs-plugins-mirakl-payouts]]


The connector does **not** manage the pay-in flow. A marketplace needs its own ecommerce system to process payments on behalf of sellers, implement payment/refund/chargeback flows, and split payment funds among seller balance accounts and commission. Hosted onboarding and Transfers API references concern seller verification and balance movement, not an automatically integrated checkout or bank-received payout. The overview does not define which party is merchant of record or legal seller for a particular marketplace transaction.

## Sources

- [[source-adyen-docs-plugins-mirakl-troubleshooting]] — 2023-modified, 2026-09-15-captured Mirakl connector troubleshooting route for setup and release-note checks, Support evidence and account-schedule or exhausted-retry failed-payout assistance; it is not proof of a fix or completed payout.


- [[source-adyen-docs-plugins-mirakl-payouts]] — 2026-09-15 Mirakl connector guide for invoice-based seller payout attempts, subsequent liable-account commission transfers, failure retries and the separate operator bank-payout boundary.


- [[source-adyen-docs-plugins-mirakl-test-and-go-live]] — 2026-09-15 Mirakl connector test-to-live checklist for seller sync/KYC, split-pay-in and modification tests, invoice/payout checks, Adyen-configured live settings and pilot sellers; real bank payouts require live verification.


- [[source-adyen-docs-plugins-mirakl-reconciliation-and-invoices]] — 2026-09-15 Mirakl seller invoice and Adyen balance-account reconciliation guide: net seller payout, commission to platform liable balance, conditional Payment Confirmation, daily BPAR and transfer references; report/status records are not independent bank-receipt proof.


- [[source-adyen-docs-plugins-mirakl-onboard-sellers]] — 2026-09-15 Mirakl seller/shop legal-entity onboarding, HOP/security/KYC status sync and conditional bank-data mapping; statuses and emails are not seller payout or merchant-of-record proof.


- [[source-adyen-docs-plugins-mirakl-set-up-payment-flows]] — 2026-09-15 Mirakl connector payment-flow guide for operator-implemented pay-ins, balance-account splits, Mirakl-coordinated captures/refunds, webhook failure timing and chargeback allocation; seller payout/commission mechanics are separate.


- [[source-adyen-docs-plugins-mirakl-set-up-the-connector]] — 2026-09-15 Mirakl connector setup for Operator API token, non-required seller/KYC fields, Mirakl feature flags, Adyen Balance Platform/LEM credentials and test/live invoice-sync scheduling; settings are not seller or payout proof.


- [[source-adyen-docs-plugins-mirakl]] — 2019-modified, 2026-09-15-captured connector overview for hosted seller onboarding, account/balance features, pay-in exclusion and ecommerce split prerequisite.

## Related

- [[adyen]]
- [[adyen-payouts]]
