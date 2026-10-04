---
title: "Braintree Wells IC+ Pricing and Fees"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-ic/pricing-fees"
raw_files:
  - "braintree/articles/wells-ic/pricing-fees-2026-09-16.md"
tags: [braintree, wells-ic, interchange-plus, pricing, fees, reconciliation]
---

## Overview

This collected Braintree-hosted article in the Wells IC path documents interchange-plus fee treatment for recipients whose account was linked to the page. It is a snapshot of that account-qualified Braintree article, not Wells Flat coverage, independent or current bank/processor policy, current merchant eligibility, a universal rate schedule, or a merchant-specific contract.

## Key takeaways

- The page says recipients of its link are on Braintree's interchange-plus, or IC+, pricing model. It separates charges into interchange fees from card associations and issuing banks and fees from Braintree; the article says the two sets are assessed on the third business day of the following month as separate debits.
- Braintree's processing fee applies only to successful sale transactions, not refunds, verifications, declines, gateway rejections, or voids. Interchange fees may apply to any transaction, so the successful-sale limitation must not be generalized to interchange.
- Interchange assessment depends primarily on card type and can also vary with merchant type, sale cost, processing technology, region, and other factors. Braintree's processing fee consists of a percentage discount rate and a static per-transaction fee. A merchant using its own Amex account is charged the Braintree per-transaction fee in addition to interchange and fees paid directly to Amex.
- The page says Braintree does not charge fees for PayPal transactions, while PayPal's processing fees still apply. This statement remains page- and snapshot-scoped rather than evidence of current PayPal or merchant-specific pricing.
- The Transaction-Level Fee report uses estimated interchange rates and must not be used for reconciliation. Merchant-specific discount and per-transaction rates are instead routed to the statement. The article also says original Braintree transaction fees are not returned after a full or partial refund; rounding and dispute-fee details remain at the raw locators below.

> [!warning] Account, region, and snapshot scope
> The page conditions IC+ status on having received its link, and transaction pricing varies with account and regional factors. The raw was fetched on 2026-09-16 and carries page metadata updated on 2025-04-01; it does not transfer its claims to Wells Flat, establish current bank policy, or prove current eligibility or rates for another merchant, account, or region.

## Detail locators

- PayPal transaction-fee exception: `## Transaction Fees > NOTE`, lines 20-21.
- Link-qualified IC+ model, the two fee sets, following-month assessment timing, separate debits, and transaction-type treatment: `## Transaction Fees`, lines 25-33.
- Estimated-interchange warning and prohibition on Transaction-Level Fee report reconciliation use: `### Transaction-level fees`, lines 36-38.
- Interchange definition, pass-through characterization, transaction-specific factors including region, and statement-detail timing: `### Interchange`, lines 41-47.
- Discount-rate and per-transaction components, own-Amex-account treatment, and merchant-specific statement route: `### Braintree processing fees`, lines 50-56.
- Transaction-level rounding-down rule, interchange exception, and monthly calculation discrepancy: `#### Rounding down`, lines 59-69.
- Original processing-fee retention after full or partial refunds: `### Refunds and credits`, lines 72-74.
- Snapshot-scoped chargeback and pre-arbitration amount, non-refundable treatment, and retrieval exclusion: `### Chargebacks, retrievals, and pre-arbitrations`, lines 77-79.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Administration context: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/control-panel/reporting/transaction-level-fee-report-2026-09-16|Braintree Transaction-Level Fee Report]] - unread navigation-only destination linked for report details; not used as factual evidence here
- [[raw/braintree/articles/wells-ic/statements-reconciliation-2026-09-16|Braintree Wells IC statements and reconciliation]] - unread navigation-only destination linked for statement and pass-through-fee details; not used as factual evidence here
- [[raw/braintree/articles/wells-ic/chargebacks-retrievals-prearbs-2026-09-16|Braintree Wells IC chargebacks, retrievals, and pre-arbitrations]] - unread navigation-only destination linked for dispute context; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/wells-ic/pricing-fees-2026-09-16|Braintree IC+ Pricing and Fees]] - fully read collected article covering link-qualified IC+ fees, account and regional factors, transaction treatment, reporting limits, refunds, rounding, and snapshot-scoped dispute fees
