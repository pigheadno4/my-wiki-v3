---
title: "Stripe: Customer Balance Funding Instructions"
type: source
date_ingested: 2026-05-05
date_updated: 2026-11-15
original_format: webpage
canonical_url: https://docs.stripe.com/payments/customer-balance/funding-instructions
raw_files:
  - "stripe-payments-customer-balance-funding-instructions-2026-11-07.md"
  - "stripe-customer-balance-funding-instructions-2025.md"
tags: [stripe, customer-balance, bank-transfers, funding-instructions, virtual-bank-account]
---

## Summary

This guide shows how to give a customer bank-transfer funding details before their first payment **without creating a PaymentIntent**. In Dashboard, a business adds a bank-transfer account to the customer's cash balance and views its funding instructions. Through the Customers funding-instructions API, a server requests region and currency and receives `financial_addresses` with `supported_networks` for the customer to use. Creating or displaying instructions is not an incoming transfer, reconciliation, available funds, or payment success. [November raw lines 5-33; May raw lines 4-32]

## Key details

**Dashboard and API identity.** The Dashboard flow selects a Customer, country and currency, creates the relevant cash balance, then opens its bank-transfer funding instructions. The server-side API examples use `/v1/customers/{CUSTOMER_ID}/funding_instructions` with `funding_type=bank_transfer`, a regional `bank_transfer[type]`, and matching currency. May shows the same route in Node.js `stripe.customers.createFundingInstructions`; November shows curl. That example-language switch does not imply SDK deprecation or a changed funding lifecycle. [November raw lines 15-90; May raw lines 14-136]

**Accounts v2 qualification (November).** For a **customer-configured Account**, the November guide says to call the v1 Customers funding-instructions endpoint with its `Account` ID in the path, such as `/v1/customers/acct_xxxxx/funding_instructions`. It says Accounts v2 is generally available for Connect users and in public preview for other Stripe users; participants in that preview need a preview version. This is a route for a specific Account configuration, not a claim that an Account ID and a Customer object are interchangeable in all contexts or that an account has access. [November raw lines 92-97]

**Regional request and response shapes.** The captured examples use US `us_bank_transfer`/USD with ABA and SWIFT address hashes, UK `gb_bank_transfer`/GBP with a sort-code hash, EU `eu_bank_transfer`/EUR with an IBAN/BIC and requested country, JP `jp_bank_transfer`/JPY with a zengin hash, and MX `mx_bank_transfer`/MXN with a SPEI/CLABE hash. `supported_networks` belongs to each returned financial address; these examples do not guarantee a particular customer's response. [November raw lines 35-90, 98-301; May raw lines 34-136, 138-346]

| Captured address | May 5, 2026 networks | November 7, 2026 networks |
| --- | --- | --- |
| US ABA | ACH, domestic US wire | ACH, domestic US wire |
| US SWIFT | SWIFT | SWIFT |
| UK sort code | Bacs, FPS | Bacs, **CHAPS**, FPS |
| EU IBAN | SEPA | SEPA |
| JP zengin | zengin | zengin |
| MX SPEI | SPEI | SPEI |

The UK CHAPS entry is a documented addition to the November sort-code response table, not proof that every returned address supports CHAPS or that a transfer completed. [May raw lines 152-158, 178-183, 214-222, 250-255, 286-291, 324-329; November raw lines 112-118, 137-142, 172-181, 208-214, 243-248, 280-285]

**EU VBAN conditions.** The SEPA bank-transfer pricing description includes up to 1,000 virtual bank account numbers and says to contact Stripe for more; neither capture states a “per account” denominator. The restriction for Spain is specifically on **creating new localized VBANs**, so use another listed EU VBAN country for that purpose. The captured sentence for the allowed country list is incomplete; the NL request is an example, not a complete country list. [May raw lines 72-98; November raw lines 55-70]

**Live versus sandbox details.** In live mode Stripe says it supplies each customer a **unique set of bank-transfer details**, which may contain multiple financial-address types; it does not promise exactly one unique VBAN per customer. In sandboxes/test environments, the bank details are invalid and **might not always be unique**. The example account numbers in the tables are illustrative, not live details to send funds to. [May raw lines 28-32, 138-201; November raw lines 29-33, 98-159]

**Ownership letter provenance.** The May guide described a Dashboard PDF letter that confirms the merchant owns the virtual account when bank details appear Stripe-owned. The November parent page instead links to a separate bank-account-ownership-letter page. That child page was not captured here, so the May Dashboard/PDF steps remain historical rather than a verified current workflow. [May raw lines 348-363; November raw lines 303-305]

## Related

- [[stripe]] — Stripe company context.
- [[stripe-customer-balance]] — Customer cash-balance and funding concept.

## Raw Sources

- [[raw/stripe-payments-customer-balance-funding-instructions-2026-11-07|November 7, 2026 funding-instructions guide]] — full capture with curl examples, Accounts v2 note and UK CHAPS address-table entry.
- [[raw/stripe-customer-balance-funding-instructions-2025|May 5, 2026 funding-instructions guide]] — historical full capture with Node.js examples and Dashboard ownership-letter steps; filename follows its earlier convention.
