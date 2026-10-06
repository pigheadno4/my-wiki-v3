---
title: "Braintree Visa Network Updates (2024 v-su24)"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2024/v-su24"
raw_files:
  - "braintree/articles/risk-and-security/compliance/network-updates/2024/v-su24-2026-09-16.md"
tags: [braintree, visa, card-networks, compliance, disputes, fees]
---

## Overview

This collected [[braintree]] webpage is a historical Visa network-update snapshot under the `2024/v-su24` route. It records body-stated effective dates for dispute and pre-arbitration changes, monitoring-program changes, authorization-response-code treatment, and region- or transaction-qualified fee and interchange changes. Treat it as Braintree-hosted retrieval evidence for the page's historical statements, not as current Visa policy, independent network authority, a merchant-specific price schedule, account eligibility, compliance proof, or evidence that a change applied to an individual transaction.

## Key takeaways

- The page dates updated dispute-rule language and new pre-arbitration attempt requirements to October 19, 2024, while saying further information would be shared later and routing readers to Braintree dispute support articles for guidance.
- The monitoring-program section says VDMP and VFMP would retire in Europe on March 31, 2025 and consolidate into an enhanced VAMP starting April 1, with updated dispute and enumeration criteria, a grace-period statement, a per-dispute fee, transition thresholds, and a monthly combined-count limit. Exact calculations, dates, thresholds, and fees remain in the raw locator.
- The authorization-response-code section says Visa would change the categories of codes 39, 52, 53, and 14 and introduce Z5. Its consequential merchant instruction is that Category 1 declines cannot be retried and retries should stop for decline code 14.
- Other sections cover arbitration case-review fees, AVS pricing, a Europe-acquirer cyber-threat-protection fee, Australia's Secure Credential Integrity Fee, an APAC Digital Commerce Fee bundle, and a Canadian small-merchant interchange program. Their stated markets, actor and transaction conditions, dates, eligibility threshold, and numeric tables remain in the raw locators rather than serving as a current or merchant-specific schedule.

> [!warning] VAMP region scope is unresolved
> The VAMP section labels the change `Global`, but its retirement sentence specifically says VDMP and VFMP would retire `in Europe`. This snapshot does not establish whether every VAMP statement has global scope or which parts are Europe-only; preserve the body-level qualification and consult current authoritative Visa and account-specific guidance before acting.

## Detail locators

- Dispute-rule revisions, pre-arbitration attempt requirements, date, and forward-looking guidance: `### Updates to Fraud and Consumer Dispute Rules and New Pre-Arbitration Attempt Requirements`, raw lines 17-30.
- Arbitration case-review fee regions, outcome-independent assessment statement, rate table, and recommendation: `### Arbitration Case Review Fees Will Be Revised in AP, Canada, CEMEA and LAC.`, raw lines 33-51.
- VDMP/VFMP retirement, VAMP start, header/body region wording, calculation definitions, grace period, fee, transition thresholds, and monthly limit: `### VAMP Enhancements and Retirement of VDMP and VFMP`, raw lines 54-81.
- APAC/Australia/New Zealand AVS fee date and rate table: `### AVS Fees Will Be Revised`, raw lines 84-99.
- Europe-acquirer cyber-threat-protection authorization-fee scope: `### Cyber Threat Protection Will Be Introduced in April 2025 as Risk Capabilities Are Further Enhanced.`, raw lines 102-111.
- Australia Secure Credential Integrity Fee transaction conditions and SCF orientation: `### Secure Credential Framework in AU.`, raw lines 114-130.
- Authorization response-code reclassification, Z5 introduction, and code-14 no-retry instruction: `### What is the Authorization Response Code Update?`, raw lines 133-147.
- APAC Digital Commerce Fee market and CNP scope, rate, bundled-services list, and merchant advice: `### What is the Digital Commerce Fee in APAC?`, raw lines 150-171.
- Canada small-merchant qualification and interchange-rate table: `### What is the Introduction to Small Merchant Interchange Program Mandate?`, raw lines 174-195.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/articles/risk-and-security/compliance/network-updates/2024/v-su24-2026-09-16|Braintree Visa 2024 v-su24 network updates]] - complete collected historical page with the stated dates, regions, actions, qualifications, warnings, and numeric tables
