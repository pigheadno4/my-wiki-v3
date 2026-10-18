---
title: "Adyen Business Accounts: Receive funds from third parties"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/receive-funds"
raw_files:
  - "adyen/docs/business-accounts/receive-funds/2026-09-15.md"
tags: [adyen, business-accounts, incoming-transfers, direct-debit, sepa]
---

## Overview

Adyen's 2022-modified, 2026-09-15-captured Business Accounts guide distinguishes **incoming third-party payments**, credited to a user's business account and available in its balance account, from **incoming direct-debit requests**, which debit the business account. It describes the `receiveFromThirdParty` capability gate, sharing business-account details with a sender, incoming-transfer webhooks, and a separate SEPA direct-debit enablement path. This guide does not establish current account eligibility, a particular account's capability state, a completed transfer, or a live direct-debit mandate. [[adyen-business-accounts]] [[adyen]]

## Key takeaways

- To receive funds from an external sender, the user's `receiveFromThirdParty` capability must be **both allowed and enabled**. The sender uses the business account number returned when the account was created, and Adyen says it sends incoming bank-transfer webhooks to the platform server (raw lines 19–26, 109–115). A balance account is the credited funds resource; the sender is an external third party, not another Adyen balance account.
- The page also covers a different direction of money movement: third parties may collect payments by direct debit, **debiting** the user's business account. Its captured support statement is for external direct debits in SEPA. To accept those requests, it instructs the platform to inform users of the stated dispute rights and ask an Adyen contact to enable receipt of SEPA direct debits (raw lines 21–22, 117–128). The eight-week and thirteen-month periods are historical guide statements, not current legal advice or proof of a specific user's rights.
- The captured tables list incoming transfer priorities by currency and location, including Regular, Instant, Fast, Wire, Cross-border and Internal, with fee/delay cautions for Cross-border. Their rows should be read as **dated documentation**, not a current reachability, speed or pricing guarantee (raw lines 28–79). The text says Cross-border can involve intermediary delays/fees and the beneficiary may get less than instructed (raw lines 40–44).
- Account-details examples show sample US account/routing/BIC, NL IBAN/BIC and UK account/IBAN/sort/BIC fields that may be shared with senders (raw lines 81–107). Do not use the sample identifiers as live bank instructions. The NL table labels a Dutch BIC as “Adyen US BIC,” and the UK sample sort code matches the US routing-number sample; both are captured data-quality warnings (raw lines 89–107).
- The priority tables have uneven labels and results: USD table headers use US/EU/UK locations, EUR and GBP tables switch to USD/EUR/GBP account labels, and the GBP table marks UK Regular unavailable while UK Instant is available (raw lines 48–79). Verify present-day region/currency coverage independently before operational use. The priority descriptions mention setting a priority in a “request or schedule,” but this page does not define an incoming-transfer API for the sender (raw lines 28–46).

## Detail locators

- Capability and credit-versus-debit distinction: raw lines 19–26 and 109–119.
- Historical priority descriptions, Cross-border warning and availability matrices: raw lines 28–79.
- Sample third-party sharing fields and table-label issues: raw lines 81–107.
- Incoming webhook route, SEPA direct-debit enablement and historical dispute periods: raw lines 109–128.

## Related

- [[adyen-business-accounts]] — Business Accounts product and capability context.
- [[source-adyen-docs-business-accounts-create-business-accounts]] — account-number creation prerequisite.
- [[source-adyen-docs-business-accounts-verification-overview-capabilities]] — allowed/enabled capability states.
- [[source-adyen-docs-business-accounts-view-transfers-details]] — transfer-state retrieval.

## Raw Sources

- [[raw/adyen/docs/business-accounts/receive-funds/2026-09-15|Captured Receive funds from third parties guide]]
