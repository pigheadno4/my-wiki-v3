---
title: "Braintree Currencies"
type: concept
category: technology
tags: [braintree, currencies, presentment, settlement, multi-currency, merchant-accounts]
---

## Braintree Currencies

Braintree's collected currency guide distinguishes presentment currency, which relates to the currency displayed to and charged to a customer, from settlement currency, which is deposited into the merchant's business bank account. Account setup determines whether either context can use multiple currencies, and available settlement currencies are typically limited to major currencies in the merchant's region. [[source-braintree-get-started-currencies]]

## Setup and live-processing boundary

Single-currency accounts present and settle in the merchant's home currency by default. Multi-currency acceptance is not automatic: it is subject to relevant banking-partner approval and successful integration of the required multi-currency accounts. Additional presentment currencies use additional merchant accounts; after an additional currency is configured, the integration must specify its merchant account ID. The guide recommends sandbox transactions to confirm configuration and says that, without the documented onboarding choices, approvals and integration, live transactions process only in the home currency regardless of checkout pricing.

The page states support for more than 130 local currencies in 44 countries but does not enumerate or map them. It also warns that displaying a converted price while charging in the home currency can produce a charged amount different from the display as rates move, and that exchange-rate movement can make an international customer's refund differ from the original amount paid. Treat the collected snapshot as a retrieval route, not proof of current currency coverage or merchant eligibility.

## Sources

- [[source-braintree-docs-reference-general-currencies]] - 2026-09-16 Braintree general-reference snapshot for account/country-qualified API currencies, zero-decimal markers, the Bulgaria BGN-to-EUR transition and Braintree-defined settlement-source categories; not current eligibility or independent ISO/network authority
- [[source-braintree-articles-risk-and-security-compliance-network-updates-2023-all-networks-s23]] - historical Spring 2023 Visa/Mastercard notice describing an expected ISK shift from two minor units to zero on April 15 and an earlier April 10 merchant cutoff recommendation; not current currency metadata or network policy
- [[source-braintree-articles-nab-transactions-accepted-payment-methods]] - 2026-09-16 Braintree-hosted NAB-path account article routing to merchant-account currency processing, customer-bank conversion and possible fee/refund/chargeback risk, additional-currency merchant-account setup, applicable presentment and settlement guidance, and merchant-account-ID selection

- [[source-braintree-articles-moneris-transactions-accepted-payment-methods]] - 2026-09-16 Braintree-hosted Moneris-path account article routing to merchant-account currency processing, customer-bank conversion, USD-or-CAD presentment and settlement, and the requirement that presentment and settlement use the same selected currency
- [[source-braintree-articles-br-transactions-accepted-payment-methods]] - 2026-09-16 Braintree-hosted BR-path account article routing to Brazil BRL presentment, merchant-account-currency processing, customer-bank conversion and possible fees, plus refund-difficulty and chargeback-risk warnings; its modal purchase wording is not a current eligibility, exchange-rate, fee, refund or execution guarantee

- [[source-braintree-articles-apac-transactions-accepted-payment-methods]] - 2026-09-16 Braintree-hosted APAC-path article routing to merchant-account currency processing, customer-bank conversion and possible fee/refund risk, additional-currency merchant-account setup, applicable presentment and settlement guidance, and merchant-account-ID selection

- [[source-braintree-articles-wells-ic-transactions-accepted-payment-methods]] - 2026-09-16 Braintree-hosted Wells IC account article routing to merchant-account currency processing, customer-bank conversion and possible fee/refund risk, additional-currency merchant-account setup, applicable presentment and settlement guidance, and merchant-account-ID selection

- [[source-braintree-articles-wells-flat-transactions-accepted-payment-methods]] - 2026-09-16 Braintree-hosted Wells Flat account article routing to merchant-account currency processing, customer-bank conversion and fee/refund risk, additional-currency account setup, applicable presentment and settlement guidance, and merchant-account-ID selection
- [[source-braintree-articles-adyen-transactions-accepted-payment-methods]] - 2026-09-16 Braintree-hosted Adyen-processor article routing to merchant-account currency processing, customer-bank conversion and fee/refund risk, additional-currency account setup, applicable presentment and settlement guidance, and merchant-account-ID selection
- [[source-braintree-articles-chase-transactions-accepted-payment-methods]] - 2026-09-16 Braintree-hosted Chase article routing to merchant-account-currency processing, customer-bank conversion and fee/refund risk, additional-currency account setup, merchant-account-ID selection, and the snapshot's Canada CAD-only boundary
- [[source-braintree-articles-adyen-change-your-bank-account]] - 2026-09-16 Braintree-hosted Adyen processor article for per-settlement-currency checking accounts and settlement-currency deposits, with original-application GBP/EUR fee-debit scope and same-country business-checking prerequisites

- [[source-braintree-auth-multi-currency-node]] - connected-merchant presentment-currency creation and listing route limited to Braintree Auth signups, with all-payment-method support conditions and a preserved Amex-specific qualification
- [[source-braintree-payment-methods-paypal-setup-guide]] - PayPal-specific multi-currency setup route requiring a Braintree merchant account per accepted currency, PayPal foreign-currency configuration and merchant-account selection during processing, with blocking and fee tradeoffs

- [[source-braintree-get-started-currencies]] - presentment and settlement definitions, single- and multi-currency setup choices, account and approval prerequisites, conversion effects, live-processing fallback and exact raw-detail routes
