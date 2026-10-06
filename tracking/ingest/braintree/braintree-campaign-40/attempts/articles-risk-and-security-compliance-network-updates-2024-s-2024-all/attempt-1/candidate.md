---
title: "Braintree Spring 2024 Network Updates"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2024/s-2024-all"
raw_files:
  - "braintree/articles/risk-and-security/compliance/network-updates/2024/s-2024-all-2026-09-16.md"
tags: [braintree, card-networks, visa, mastercard, fees, compliance, 3d-secure]
---

## Overview

This collected [[braintree]] webpage identifies itself in its title and body as the Spring 2024 release guide and summarizes selected Mastercard and Visa fee, mandate, and feature changes, with body-stated effective dates, markets, transaction or account conditions, and merchant or acquirer actions. Treat it as historical Braintree-hosted retrieval evidence for that stated release, not as current law, independent card-network policy, a merchant-specific price schedule, account eligibility, compliance proof, or proof that any fee or processing change applied to an individual transaction.

## Key takeaways

- The guide says network updates can introduce or change fees, mandates, and features; some require no merchant action, while others can require integration changes or service adoption. Its overview table identifies five Mastercard items and seven Visa items, each with a stated update type and geographic impact.
- For Mastercard, the body dates the US Digital Enablement Fee revision to April 15, 2024 and qualifies it to card-not-present transactions by amount. It dates the Canada Excessive Authorization Attempts threshold change to April 1, with first billing stated for May 5; the page recommends that acquirers stop repeated authorizations after the stated decline patterns and tells merchants to review statements and adjust behavior. The APAC CVV2 change is dated April 8 and scoped to Mastercard Digital Enablement Service tokenized card-on-file and guest-checkout transactions; the page says no immediate merchant action was required but merchants should plan for issuer readiness. Separate US sections date the expanded Network Access and Brand Usage fee and the revised Acquirer Brand Volume fee to April 15.
- For Visa, the page gives region-specific Processing Integrity Program dates for APAC excluding Japan, CEMEA, Europe, Latin America and the Caribbean excluding Brazil and Chile, and Canada; it describes fees for approved authorizations without matching clearing or reversal and for clearing without a matching approved authorization. Other body-stated dates are April 13 for selected US interchange and intra-Europe EEA commercial-card changes, April 1 for Canadian CVV2 pricing, European VROL pricing, and the non-domestic currency settlement fee, and August 12 for the global Visa Secure data-field change.
- The Canadian CVV2 fee is stated per match or no-match result and excluded when 3DS succeeds or the transaction is a zero-amount account-verification message. The European non-domestic settlement fee is limited by cross-border identification plus issuer and acquirer settlement-currency conditions; the body separately lists the covered EEA and named non-EEA merchant locations.
- The Visa Secure section distinguishes browser fields from an in-app/SDK device-IP field, says transaction processing would not be impacted, strongly advises merchants to provide the fields, and describes a possible later compliance deadline or non-compliance fees rather than a present deadline or assessed fee.

> [!warning] Visa Secure field-count mismatch
> The prose says Visa reduced the required fields to three, but Table 6 and the later status table visibly list Browser IP Address, Browser Screen Height, Browser Screen Width, and Common Device Identification Parameters (Device IP Address) for in-app/SDK transactions. Preserve that mismatch; this snapshot does not resolve whether the device-channel rows represent three or four distinct required fields.

> [!warning] Embedded interchange-table comment
> After the US interchange table, the captured raw contains the sentence `I think the new rate here should be 2.52%` with an internal anchor. This entry does not treat that editorial-looking comment as an approved correction or independent Visa rate authority; consult the raw table and current account/network sources before relying on a rate.

## Detail locators

- Guide purpose, update categories, merchant-action framing, and explicit Spring 2024 identity: `## SPRING 2024 RELEASE GUIDE`, raw lines 17-25.
- Scheme, item, type, and geographic-impact overview: `## KEY SPRING 2024 NETWORK RELEASES`, raw lines 30-46.
- Mastercard US Digital Enablement Fee date, CNP threshold, and rates: `# What is the Expansion of the Digital Enablement Fee in the US mandate?`, raw lines 52-62.
- Mastercard Canada excessive-authorization threshold, first-billing date, acquirer stop recommendations, merchant statement action, and per-decline fee: `# What is the Revised Excessive Authorization Attempts (CA) mandate?`, raw lines 65-85.
- Mastercard APAC MDES-tokenized card-on-file and guest-checkout CVV2 change, date, authentication context, and planning action: `# What is the CVV2 Compliance Requirements mandate?`, raw lines 88-100.
- Mastercard US NABU transaction/account conditions and rates: `# What is the Extending Network Access and Brand Usage Fee change?`, raw lines 103-118.
- Mastercard US Acquirer Brand Volume fee and acquirer-tool summary: `# What is the Revising Acquirer Brand Volume Fee change?`, raw lines 121-131.
- Visa Processing Integrity regions, dates, matching conditions, and fee table: `# What are the Visa Processing Integrity Fees?`, raw lines 137-159.
- Visa selected US interchange date, tokenized-transaction statement, detailed rates, and embedded editorial-looking comment: `# What are the Modifications to Certain US Interchange Rates and Programs?`, raw lines 162-239.
- Visa intra-Europe EEA commercial-card scope, date, product/category table, and footnotes: `# What is the Intra-Europe EEA Commercial Interchange Fees Mandate?`, raw lines 244-378.
- Visa Canada CVV2 date, per-result pricing, 3DS and zero-amount exclusions, and acquirer billing line: `# What is the Visa Introduction to CVV2 Pricing in Canada?`, raw lines 381-397.
- Visa Secure effective date, claimed field count, browser-versus-SDK channel table, transaction-impact statement, advice, possible future deadline/fees, and recommendation qualifications: `# What are the Updates to Visa Secure Data Fields mandate?`, raw lines 400-458.
- Visa Resolve Online Europe date, acquirer/issuer request types, May invoicing, and merchant-versus-internal cost framing: `# What are the Visa Resolve Online Pricing Changes for Europe?`, raw lines 461-473.
- Visa non-domestic currency settlement date, cross-border and issuer/acquirer settlement conditions, covered merchant locations, and geographic definitions: `# What is the Non-Domestic Currency Settlement Fee mandate?`, raw lines 476-502.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/articles/risk-and-security/compliance/network-updates/2024/s-2024-all-2026-09-16|Braintree All Spring 2024 Network Updates]] - complete collected historical guide for the stated Mastercard and Visa changes, dates, regions, conditions, actions, tables, and source-internal mismatches
