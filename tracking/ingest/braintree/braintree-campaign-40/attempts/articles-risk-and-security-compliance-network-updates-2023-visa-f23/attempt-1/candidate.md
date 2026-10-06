---
title: "Braintree 2023 Visa Network Fee and Pricing Updates"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2023/visa-f23"
raw_files:
  - "braintree/articles/risk-and-security/compliance/network-updates/2023/visa-f23-2026-09-16.md"
tags: [braintree, visa, network-updates, fees, interchange, network-tokenization]
---

## Overview

This collected Braintree webpage, titled "Visa Networks," summarizes a set of Visa fee, pricing, interchange, credential-update, account-verification, and processing-integrity changes with stated effective dates from July 2023 through April 2024. Each item has its own merchant, region, transaction-channel, credential, timing, or currency conditions. The page is a historical Braintree-hosted summary, not current Visa network policy, a merchant-specific price schedule, account eligibility evidence, or proof that a fee was assessed.

## Key takeaways

- For the Visa Secure Credential Framework, the page places all European countries except Turkey and France in scope. From October 1, 2023, it describes a 2.5-basis-point fee on domestic and interregional ecommerce PAN-approved authorizations processed without a Visa EMV Payment Token or Visa Secure; the stated TRA and low-value SCA exemptions remain in scope when neither credential route is used. The page directs merchants seeking to avoid that fee to pass tokenized transactions or use 3DS.
- In the US, the page describes an October 1, 2023 Digital Commerce Fee on settled card-not-present transactions and says Visa would cease separate billing for AVS, CVV2, and the Merchant-Initiated Transaction Service. The exact per-transaction rate, minimum, and threshold remain in the raw locator.
- Merchants using Braintree's network-tokenization solution are described as automatically enrolled in Visa Digital Credential Updater. The page permits opt-out but warns that, after a PAN update, an unupdated token may become unusable and authorization declines and cart abandonment may increase. The regional fee dates and AP acquirer amount remain in the raw locator.
- For selected US Visa Infinite programs, the page lists rate changes effective CPD October 14, 2023. Separately, its global interregional update distinguishes card-present Base from card-absent Alternative transactions, requires authorization and clearing within three days (seven days for card-not-present airline transactions), and assigns the Downgrade rate when one or both requirements fail.
- For APAC excluding Japan, the account-verification section says the October 1, 2023 revision separates account-verification messages from authorization messages on client invoices and replaces a flat AP-country structure with country-specific fees. It says token-provisioning and transit account-verification transactions remain uncharged.
- The processing-integrity section gives separate effective dates for the EU, CEMEA, Canada, and APAC. It ties fees to authorization/clearing mismatches and settlement records that do not match previously approved or partially approved transactions, while encouraging valid authorizations, prompt reversals or cancellations, and timely clearing with relevant authorization data.
- For manual cash transactions in Australia, Singapore, Hong Kong/Macau, and Malaysia, the page describes an October 1, 2023 increase to an existing cross-border fee when the received transaction currency differs from the merchant's home-country currency. Exact tiered values remain in the raw locator.

> [!warning] Historical scope and table boundary
> Treat every date, fee, region, program, and action as part of this captured Braintree article, not as current or universal Visa policy. Several retained rate tables are structurally irregular in the collected Markdown, so this entry does not reconstruct ambiguous cells or transfer one row's value to another market, program, participant, or channel.

## Detail locators

- Visa Secure Credential Framework region, fee trigger, SCA-exemption treatment, and token-or-3DS action: `## What is the Visa Secure Credential Framework (SCF) mandate?`, raw lines 17-27.
- US Digital Commerce Fee basis, minimum, threshold, and discontinued separate AVS/CVV2/MIT Service billing: `## What is the Digital Commerce Services Fee mandate?`, raw lines 30-38.
- VDCU automatic enrollment, regional fee timing, opt-out consequence, suite composition, and AP pricing row: `## What is the Visa Account Updater Suite Pricing mandate?`, raw lines 41-55.
- Selected US Visa Infinite program and rate changes: `## What are the Modifications to Certain US Interchange Rates and Programs?`, raw lines 58-89.
- Global interregional Base/Alternative timing, downgrade condition, and consumer/commercial rate tables: `## What are the Revisions to interregional interchange structure and rates?`, raw lines 92-444.
- APAC-excluding-Japan account-verification invoicing, covered services, no-charge cases, and country/participant fee table: `## What is the Visa account verification fee structure revision in AP mandate?`, raw lines 447-495.
- Regional processing-integrity dates, recommended actions, mismatch conditions, named fees, and per-transaction amount: `## What are the New Visa Processing Integrity Fees?`, raw lines 498-519.
- Region- and currency-qualified manual-cash cross-border increase and tier table: `## What is the Visa Pricing for Sales and ATM Manual Cash Transactions will be Revised mandate?`, raw lines 522-538.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Related concepts: [[braintree-3d-secure]], [[braintree-account-updater]]
- Parent compliance route: [[source-braintree-articles-risk-and-security-compliance-overview]]

## Raw Sources

- [[raw/braintree/articles/risk-and-security/compliance/network-updates/2023/visa-f23-2026-09-16|Braintree Visa Networks historical update]] - complete collected snapshot for the dated and scope-qualified Visa network, fee, pricing, and processing-integrity changes
