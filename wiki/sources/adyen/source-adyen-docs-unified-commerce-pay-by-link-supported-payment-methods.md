---
title: "Adyen Pay by Link supported payment methods"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/pay-by-link/supported-payment-methods"
raw_files:
  - "adyen/docs/unified-commerce/pay-by-link/supported-payment-methods/2026-09-15.md"
tags: [adyen, unified-commerce, pay-by-link, payment-methods, eligibility]
---

## Overview

This 2026-09-15 snapshot of Adyen's Pay by Link method matrix compares methods listed for payment links created in Customer Area with those listed for API creation. A listed method must first be added to the merchant account. The matrix is a dated navigation and channel-availability reference (page metadata last modified 2024-06-11), not proof of merchant enablement, country/currency/device eligibility, shopper presentation, or payment success.

> [!warning] Contradiction
> The supported-methods matrix captured 2026-09-15 marks Affirm, Alma, and Atome in the Customer Area column, while the Customer Area creation guide says these links exclude buy now, pay later methods. The difference is unresolved in these snapshots; verify applicable method, account, and product conditions before claiming Customer Area availability. [[source-adyen-docs-unified-commerce-pay-by-link-create-payment-links-customer-area]]

## Key takeaways

- The prerequisite is to add the needed method to the merchant account through Customer Area **Payments > Payment methods > Add payment methods**. The matrix then distinguishes Customer Area and API integration columns. Several rows have an API mark but a blank Customer Area cell, including Afterpay (labelled AU/NZ/US/CA), Clearpay (GB), Billie via Klarna, Klarna, Oney 3x4x, and stored card details. Read the exact row and the linked method documentation for further conditions. See `Add payment methods to your account` and `Available payment methods`.
- Apple Pay's row points to a note limiting support to Adyen's Apple Pay certificate. The Google Pay note says `eu.adyen.link` must be registered as a supported domain in Google Developer Console. These are additional method-specific prerequisites, not evidence that a given shopper's browser/device or currency is eligible. See table notes 1 and 2 below `Available payment methods`.
- The table has an unresolved scope conflict with [[source-adyen-docs-unified-commerce-pay-by-link-create-payment-links-customer-area]]: this matrix marks Affirm, Alma and Atome in the Customer Area column, while that creation guide says Customer Area payment links exclude buy now, pay later methods. Do not present the matrix as a blanket BNPL enablement guarantee; resolve the applicable product, account and method conditions before using that claim. See this raw table's Affirm/Alma/Atome rows and the other guide's opening paragraph.
- The ACH Direct Debit section warns that Pay by Link neither automatically validates the bank account nor supplies the mandated debit-authorization text. It calls B2C ACH payment links non-compliant and directs use only to B2B cases with accurate account details and separately collected/stored payer authorization. This warning materially qualifies the table's ACH check marks. See `Compliance of ACH Direct Debit payment links`.

## Detail locators

- `Available payment methods`, rows 38–102: exact method-by-creation-channel matrix and any region labels shown in a row. Method-name links are navigation to distinct product guides, not evidence reviewed here for current country, currency or device rules.
- Notes immediately after the matrix, lines 104–105: Apple Pay certificate and Google Pay domain prerequisites.
- `Compliance of ACH Direct Debit payment links`, lines 107–111: account-validation and authorization-text limitations, B2C warning, and qualified B2B use.

## Related

- [[adyen]]
- [[adyen-unified-commerce]]
- [[source-adyen-docs-unified-commerce-pay-by-link-create-payment-links-customer-area]]

## Raw Sources

- [[raw/adyen/docs/unified-commerce/pay-by-link/supported-payment-methods/2026-09-15|Adyen Pay by Link supported-methods matrix, 2026-09-15 snapshot]]
