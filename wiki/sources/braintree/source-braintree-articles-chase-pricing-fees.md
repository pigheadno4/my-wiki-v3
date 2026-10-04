---
title: "Braintree Chase Pricing and Fees"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/chase/pricing-fees"
raw_files:
  - "braintree/articles/chase/pricing-fees-2026-09-16.md"
tags: [braintree, chase, paymentech, pricing, transaction-fees, chargebacks]
---

## Overview

This collected Braintree-owned Chase article documents fee treatment for the page's Paymentech processing context. It distinguishes account-selected blended and IC+ pricing models, explains when listed transaction fees are deducted, and routes Chase-managed reporting to Paymentech Online. It is a snapshot of this Braintree article, not independent Chase authority or a universal/current Chase rate schedule.

## Key takeaways

- The listed transaction-fee categories are discount rate, per-transaction fee, combined Paymentech processing fees, interchange fees, and a processing-bank chargeback fee. The article says the listed transaction fees are deducted from daily disbursements and applied only to successful sale transactions, not refunds, verifications, declines, gateway rejections, or voids.
- The merchant's pricing model was set when the account was opened. Blended pricing uses fixed Braintree processing rates, with possible debit-versus-credit differences depending on account setup. IC+ combines Braintree processing fees with variable interchange; the exact transaction assessment depends primarily on card type and also on factors including merchant type, sale cost, processing technology, and region.
- A merchant using its own American Express account is outside the article's Braintree discount-rate treatment for those transactions, but the article says Braintree's per-transaction fee still applies in addition to interchange and direct Amex fees.
- Chase manages reporting directly through Paymentech Online. The article describes more than 125 customizable reports and links to a separate Chase reporting and reconciliation article for details.
- In this collected page, a $15 non-refundable chargeback fee applies to chargebacks and pre-arbitrations regardless of outcome, while retrievals do not produce that fee "at this time." This snapshot-scoped amount and treatment should not be presented as a current or universal Chase rate.

> [!warning] Account, model, and snapshot scope
> Pricing-model assignment is account-specific, debit and credit rates can depend on account setup, and IC+ assessments vary with transaction and regional factors. The raw page was fetched on 2026-09-16 and carries page metadata dated 2025-04-02; those dates preserve provenance but do not establish current rates, current account eligibility, or independent Chase policy.

## Detail locators

- Fee types and the pricing-model qualification for interchange: `## Transaction fees`, lines 17-26.
- Successful-sale-only application, daily-disbursement deduction, exclusions, and Paymentech Online reporting: `## Transaction fees`, line 28.
- Own-American-Express-account fee treatment: `## Transaction fees > IMPORTANT`, lines 31-32.
- Account-time pricing-model selection and the support route: `## Pricing models`, lines 37-39.
- Blended fixed-rate composition and account-dependent debit/credit rates: `### Blended`, lines 42-44.
- IC+ composition, interchange variability, and transaction-specific factors including region: `### IC+`, lines 47-49.
- Chase reporting ownership and the separate reconciliation route: `### Reporting`, lines 52-54.
- Outcome-independent chargeback/pre-arbitration fee and time-qualified retrieval treatment: `## Chargebacks, retrievals, and pre-arbitrations`, lines 57-59.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/articles/chase/pricing-fees-2026-09-16|Braintree Chase Pricing and Fees article]] - complete collected page covering Paymentech fee categories, account-selected pricing models, Amex-account treatment, Chase reporting ownership, and snapshot-scoped chargeback-fee treatment
