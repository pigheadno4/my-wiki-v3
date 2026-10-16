---
title: "Adyen NetSuite Pay by Link setup"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/netsuite/set-up-pay-by-link"
raw_files:
  - "adyen/docs/plugins/netsuite/set-up-pay-by-link/2026-09-15.md"
tags: [adyen, netsuite, pay-by-link, hosted-checkout, customer-deposits]
---

## Overview

This Adyen guide configures Pay by Link in NetSuite so an invoice, sales order or Customer Deposit record can carry a URL to an Adyen-hosted payment page. It covers required bundle and Customer Area setup, a payment-method instance, processing-profile fields, company custom preferences and a record configuration that connects the subsidiary and profile. Link creation or sharing is a request for the shopper to pay, not evidence that payment, settlement or bank receipt occurred. See [[adyen]] and [[adyen-netsuite]] for provider and NetSuite integration context.

## Key takeaways

- The page requires the Adyen SuitePayments Bundle and Adyen Customer Area setup. Create a Pay by Link payment-method instance; Pay by Link invoice transactions additionally require a Pay by Reference instance. The processing profile selects the link method, default timeout and blocked/allowed payment codes or brands. CHECKOUT API KEY ENTRY is required only for Pay by Link invoices in NetSuite. The page names no separate NetSuite user role; linked setup guides own account and credential permissions.
- Tokenization is optional. PAY BY LINK: TOKENIZATION controls whether shopper payment details used in a link transaction are tokenized; DEFAULT VIA TOKENIZATION saves tokenized details as the shopper's default only when tokenization is also enabled. These settings do not prove a token was created. Company Custom Preferences include a separate PAY BY LINK TEST MODE switch; an invoice preference chooses URL generation before versus after submit. The configuration record binds a named record to the processing-profile internal ID, its subsidiary and SuitePayment Config ID.
- For an invoice, save the record with ADYEN PAY BY LINK CONFIG, retrieve its generated URL from Billing, then give it to the customer. The page says a payment record takes approximately 15 minutes to be created after the shopper completes payment; a generated invoice URL is not that record. Putting the URL on an invoice PDF requires adding its field to the template.
- For a sales order, select the Pay by Link payment method and Process handling mode; if Payment Instruments are off, the guide also says to select Get Authorization. The order remains in Payment Hold until the customer pays through the link. Saving the order or seeing its URL does not clear that hold.
- Customer Deposit links can collect full or partial payments and allow shoppers to modify the transaction amount, but this path is supported only for cards, alternative payment methods and ACH. The record selects Pay by Link, the processing profile and Process handling mode; a return URL is optional. After successful shopper payment, the deposit can be applied to an open invoice, and the guide directs checking the Customer Deposit's Applied to tab for amount and invoice. A saved Customer Deposit record or link is not proof that an amount was paid or applied.

## Detail locators

- Purpose, hosted URL and prerequisites: raw lines 17–24. Four setup steps and invoice Pay by Reference condition: `## Set up Pay by Link in NetSuite`, lines 26–35.
- Processing-profile payment method, timeout, method restrictions, invoice-only API key and conditional tokenization: lines 37–62. Test mode, invoice URL timing, token-method and profile preferences: lines 64–78. Profile/subsidiary/config-ID record mapping: lines 80–96.
- Invoice URL and approximate payment-record delay: `### Generate a payment link on the Invoice record`, lines 102–116. PDF template field: lines 118–146. Sales-order Payment Instruments condition and Payment Hold: lines 148–166.
- Customer Deposit amount, supported methods, optional return URL, successful-payment condition and invoice application check: lines 168–200.

## Related

- [[adyen]] — provider context.
- [[adyen-netsuite]] — NetSuite bundle, setup and ERP record context.
- [[source-adyen-docs-plugins-netsuite-set-up-netsuite-customer-center]] — NetSuite bundle, method-instance and processing-profile setup.

## Related raw API references

- The raw page links to Adyen Customer Area setup, the NetSuite glossary, the general Pay by Link guide and the Customer Center setup guide. Those linked destinations own their detailed eligibility and behavior until read separately.

## Raw Sources

- [[raw/adyen/docs/plugins/netsuite/set-up-pay-by-link/2026-09-15|Adyen Docs: Set up Pay by Link with NetSuite (2026-09-15 snapshot; page last modified 2023-05-16)]]
