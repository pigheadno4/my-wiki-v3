---
title: "Braintree April 2025 Network Release Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2024/f-2024-all"
raw_files:
  - "braintree/articles/risk-and-security/compliance/network-updates/2024/f-2024-all-2026-09-16.md"
tags: [braintree, card-networks, visa, mastercard, fees, authorization, compliance, 2025]
---

## Overview

This collected Braintree webpage is an April 2025 release guide summarizing dated Visa and Mastercard network changes involving fees, monitoring programs, authorization responses and retries, enhanced commercial data, merchant category coding, and regional processing rules. Although its canonical path contains `2024/f-2024-all`, the page title, April 2025 release heading, 2025 creation metadata, and body effective dates control this entry's identity. It is a Braintree-hosted historical summary, not present Visa or Mastercard authority, current law, merchant-specific account terms, or proof that a merchant implemented or completed any stated action.

## Key takeaways

- The guide says network releases can require no merchant action, integration or service changes, or awareness of new or changed fees. Its introduction says the chart identifies ten updates, while the displayed Visa and Mastercard tables contain fourteen named rows; use the individual sections rather than the stated count as the detail route.
- The Visa sections are separately scoped. The US arbitration-review fee change and EU cyber-protection authorization fee were dated April 1, 2025, with Visa Direct OCTs and AFTs excluded from the latter. The VAMP section is labeled global, but specifically says VDMP and VFMP retirement occurred in Europe on March 31 and describes consolidation from April 1, revised methodology, thresholds and fines from June 1, an advisory period through October 1, 2025, fines passed through via acquirers, and a remediation plan expected within 15 days after program notification. Preserve those date and region distinctions rather than treating the page as a timeless or universal threshold schedule.
- For authorization handling, the guide dated Visa's global response-code changes April 11, 2025 and its retry change May 25, 2025. It says CNP issuer responses `12` and `15` would be converted to `05`, while Category 2, 3, or 4 retry allowance would rise from 15 to 20 in 30 days with separate CIT and MIT System Integrity Fee counters; that bulletin says it introduced no new fee. These collected limits do not override other response-code, payment-method, account, or current-network restrictions.
- Other Visa changes retain their stated markets and rollout dates: the US Commercial Enhanced Data Program uses April 2025, October 2025 and April 2026 stages for merchants passing Level 2 or 3 data, including a CEDP flag that the page says requires no merchant action to pass; the Digital Commerce Fee was dated July 1, 2025 only for named AP territories; and the Secure Credential Framework increase was dated October 1, 2025 for the EU, September 30 for Israel, with Turkey out of scope. Exact rates, exclusions, fields, services and staged phase-out details remain at the raw locators.
- Mastercard sections likewise retain their own scope: global changes add MCC 5262 only where no other MCC better describes the marketplace and add decline codes `46` and `72`; the MAC 03/21 TPE criteria are dated May 1, 2025 in Europe and January 1, 2026 in the US and say the card should not be retried regardless of amount; intra-European and UK fee sections are qualified by merchant and consumer domicile; and the undefined-authorization fee is dated July 1, 2025 in the US and October 1, 2025 in Canada. For the last item, the guide says Mastercard would charge rather than block approved undefined authorizations and instructs merchants to use only Final authorization or Pre-authorization requests.

> [!warning] Historical snapshot and authority boundary
> All dates, rates, thresholds, programs, response handling and actions above are what this Braintree snapshot reported for its April 2025 release cycle. The page does not prove present network rules, current merchant applicability, an account's fee treatment, compliance, notification, remediation, integration completion, or transaction outcome. Confirm current network and account-specific requirements with the responsible authorities and provider.

## Detail locators

- Page identity, 2025 metadata, release purpose and ten-versus-fourteen item mismatch: frontmatter and `## OVERVIEW` through the Visa/Mastercard summary tables, raw lines 5-50.
- Visa US arbitration, EU cyber fee and excluded transaction types: the first two Visa update sections, raw lines 56-79.
- VAMP retirement, consolidation, revised criteria, thresholds, exclusions, fines, advisory period and remediation timing: `## VAMP Enhancements and Retirement of VDMP and VFMP` through `## Program Threshold Fines`, raw lines 82-140.
- Visa response-code conversion and authorization-retry changes: `## Update to Changes to Authorization Response Codes` through the retry section, raw lines 143-182.
- US CEDP purpose, monitoring, flag, fee and staged rollout: `## Update to Changes to Support Visa Commercial Enhanced Data Program Processing in the US`, raw lines 185-258.
- AP Digital Commerce Fee territory/service scope and EU Secure Credential Framework rate, token/3DS route, Israel date and Turkey exclusion: raw lines 261-324.
- Mastercard MCC 5262 qualification, MAC 03/21 regional dates and do-not-retry action, and decline-code additions: raw lines 327-389.
- Mastercard intra-European country rates and UK domicile/consumer-region fee qualifications: raw lines 392-466.
- Mastercard US/Canada undefined-authorization dates, fee schedules, non-blocking statement and Final/Pre-authorization direction: raw lines 469-499.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Monitoring-program context: [[source-braintree-articles-risk-and-security-card-brand-monitoring-programs-overview]]
- Authorization-response and retry context: [[source-braintree-authorization-responses]]
- Merchant Advice Code context: [[source-braintree-merchant-advice-codes]]

## Raw Sources

- [[raw/braintree/articles/risk-and-security/compliance/network-updates/2024/f-2024-all-2026-09-16|Braintree April 2025 Network Release Guide (collected 2026-09-16)]] - complete collected page containing the dated Visa and Mastercard update sections, qualifications, tables and warnings
