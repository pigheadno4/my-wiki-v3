---
title: "Configure your invoice settings | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/account/invoice-settings"
raw_files:
  - "adyen/docs/account/invoice-settings/2026-09-15.md"
tags: [adyen, invoice-settings, company-account, merchant-account, customer-area]
---

## Overview

This 2026-09-15 snapshot of an Adyen page last modified 2021-12-29 explains Customer Area settings for **Adyen invoices** for payment processing, terminal orders, and other Adyen services. It covers a selected merchant account or batch editing from a company account. Invoice currency, delivery contact, charged merchant account, and invoice-payment-method labels here concern charges on Adyen invoices; the page does not define the seller or merchant of record, customer-payment funds flow, settlement, payout routing, or a completed financial outcome. See [[adyen]] and [[adyen-account-structure]].

## Key takeaways

- For one merchant account, switch to that merchant account and open **Reconciliation > Invoices > Settings**. The **Merchant invoicing** section is visible in a merchant account and provides invoice-type toggles; if the merchant account's legal entity differs from the company account's legal entity, the page says those invoices cannot be disabled. The guide does not state a Customer Area user role for making these changes.
- General settings apply across invoice types: invoice currency and decimal display, month-end email delivery, an optional alternative charged merchant account on a merchant account, a charged merchant account on a company account, and invoice address. The charged-account and address changes are directed to Adyen Support; changing an invoice setting is not evidence that a payout or shopper payment moved accounts.
- Invoice-type-specific settings cover the method used to pay invoice charges, an invoice email address conditional on general email delivery being enabled, and an optional order number for payment-processing and terminal-services invoices. The invoice-payment method change goes through the Adyen contact. The email field is an invoice-delivery contact, not a shopper payment or identity field.
- To edit more than one account, switch to the company account and use **Batch edit**. Select an invoice type, choose accounts, set general or type-specific values, then **Apply changes**. This bulk settings path does not establish a shared legal entity or combined balances among selected merchant accounts.

## Detail locators

- `## Configure settings for one account`: merchant-account selection and Customer Area navigation.
- `### Merchant invoicing`: invoice-type toggles and different-legal-entity disablement limit.
- `### General`: invoice currency/display/email, charged merchant account, and invoice address with Support qualifications.
- `### Invoice-specific settings`: invoice-payment method, conditional email delivery address, and optional order number.
- `## Configure settings for multiple accounts`: company-account Batch edit, account selection, setting selection, and final Apply changes action.

## Related

- [[adyen]]
- [[adyen-account-structure]]

## Raw Sources

- [[raw/adyen/docs/account/invoice-settings/2026-09-15|Adyen invoice settings guide, 2026-09-15]]
