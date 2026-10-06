---
title: "Braintree Visa Spring 2023 Network Updates"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2023/visa-s23"
raw_files:
  - "braintree/articles/risk-and-security/compliance/network-updates/2023/visa-s23-2026-09-16.md"
  - "braintree/articles/risk-and-security/compliance/network-updates/2023/s-2023-all-2026-09-16.md"
tags: [braintree, visa, network-updates, fees, mandates, compliance]
---

## Overview

This Braintree-hosted Visa Networks page records fee, mandate and feature notices that its body dates to 2023, with separate Canada, global, U.S./Europe, EMEA and Europe scopes. It is a historical [[braintree]] documentation route for [[braintree-payment-platform]], not current Visa policy, pricing, merchant-account applicability, legal authority or proof that any fee, field mapping or transaction treatment applies now.

## Key takeaways

- For Canada, the page says Visa introduced account-verification-message pricing effective April 1, 2023: $0.01 USD for domestic account verification and $0.02 USD for foreign account verification. Separately, it says Visa expanded estimated and incremental authorization eligibility globally to all merchant category codes from April 17, 2023 and charged 0.02% for approved estimated and incremental authorizations. The latter notice says existing fields, processing rules and interchange programs did not change and excludes the listed account-funding, installment, advance-payment, cash-disbursement, quasi-cash, cryptocurrency and recurring transactions.
- For the U.S. and Europe, the page says an April 1, 2023 CVV2 fee of $0.0025 applied when a match or no-match result was provided. It states that the fee was not incurred for unverified CVV2, an acquirer result withheld because of error, successful 3DS or a zero-amount account-verification authorization.
- The page describes two separately scoped regional fee changes: an EMEA non-domestic-currency-settlement fee increasing from 0.02% to 0.05% beginning in April 2023, and a Europe secure-credential fee effective October 1, 2023 for domestic or intraregional ecommerce PAN authorization approvals processed without Visa EMV Payment Tokens or Visa Secure. The secure-credential table excludes qualifying authorizations using either technology and those with merchant locations in Turkey or France.
- For the global Visa Marketplace Program, the page says that from April 15, 2023 merchant participants had to include five named indicators in clearing records for domestic marketplace transactions completed with a foreign marketplace retailer. It states that Visa would assess a 0.10% incremental manual-reporting per-transaction fee on foreign retail volume reported without those indicators.
- The page also records a global AVS result-code consolidation, saying the identified redundant codes would no longer be returned and that there was no AVS-fee impact. Its separate account-name-inquiry update adds first-, middle- and last-name match decisions, renames the existing decision as Full Name Account Match Decision, and states an opt-in per-usable-result fee of $0.05 from April 2023, systemic billing from June 2023 and an increase to $0.10 from April 2024.

> [!warning] Historical authority boundary
> The effective dates, rates, scopes, exclusions, fields and code mappings above are claims in this Braintree-hosted historical page. The page does not establish current Visa rules or prices, an individual merchant's account terms or eligibility, implementation state, legal compliance, or transaction-level fee application. Confirm present requirements and account-specific action through current Visa and Braintree authority.

> [!warning] Source-internal label conflicts
> The linked combined Spring 2023 guide's at-a-glance table labels the Account Verification Fee Update as Mastercard / Canada, while its detailed body and this Visa-only page label it Visa / Canada. That table labels Non-Domestic Currency Settlement as Visa / Global, while its detailed body and this page label it Visa / EMEA. This entry preserves both pairs without resolving them; use the exact raw passages and current Visa and Braintree authority for decisions.

## Detail locators

- Canada account-verification fee, rates and descriptors: `## What is the new Account Verification Fee update?`, raw lines 17-27.
- Global estimated and incremental authorization eligibility, fees, definitions, unchanged processing statement and exclusions: `## What is the Estimated and Incremental Authorization fee update?`, raw lines 30-43.
- U.S./Europe CVV2 fee and no-fee conditions: `## What is the Card Verification Value 2 (CVV2) pricing change fee change?`, raw lines 46-56.
- EMEA non-domestic currency settlement fee and phased table: `## What is the Non-Domestic Currency Settlement fee change?`, raw lines 59-67.
- Europe secure-credential fee scope, exclusions, rate and date: `## What is the Secure Credential Framework Will Be Expanded in Europe change?`, raw lines 70-83.
- Global marketplace-reporting condition, required indicators and incomplete-reporting fee: `## What is the Visa Marketplace Reporting mandate?`, raw lines 86-99.
- Global AVS code retirement and exact old-to-new mappings: `## What is the Address Verification Service update?`, raw lines 102-128.
- Global account-name inquiry fields, renamed decision and opt-in historical fee schedule: `## What is the Account Verification Messages update?`, raw lines 131-148.
- Combined-guide at-a-glance labels and conflicting detailed-body labels: combined raw lines 31-46, 133-143 and 175-183.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Broader historical guide: [[source-braintree-articles-risk-and-security-compliance-network-updates-2023-s-2023-all]] - combined Spring 2023 Visa, Mastercard and all-network route that includes these Visa topics.

## Raw Sources

- [[raw/braintree/articles/risk-and-security/compliance/network-updates/2023/visa-s23-2026-09-16|Braintree Visa Spring 2023 Network Updates]] - complete collected historical Visa notice page
- [[raw/braintree/articles/risk-and-security/compliance/network-updates/2023/s-2023-all-2026-09-16|Braintree All Spring 2023 Network Updates]] - complete combined guide supporting the preserved at-a-glance and detailed-body label conflicts
