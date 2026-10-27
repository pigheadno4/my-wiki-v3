---
title: "Pre-Authorized Debit Canada Web Component | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pad/web-component"
raw_files:
  - "adyen/docs/payment-methods/pad/web-component/2026-09-15.md"
tags: [adyen, pad, canada, web, components, mandates, tokenization]
---

## Overview

This 2026-09-15 Adyen page adds Pre-Authorized Debit Canada (PADs Canada) to an existing Web Components integration. It gives separate Sessions and Advanced flow instructions, not a complete base integration or a substitute for the PAD mandate requirements in the related [[source-adyen-docs-payment-methods-pad|PAD overview]] (raw lines 15–25, 29–37, 194–204).

## Key takeaways

- Both flows require Checkout API v69 or later, a method setup request to Support, a way to obtain shopper mandate consent, and subscription to `DIRECT_DEBIT_NOTICE_OF_CHANGE_NOTIFICATION` for outdated banking details (raw lines 29–37, 196–204). The requirement to get a mandate applies to the payment or recurring series; token creation and a returned mandate ID do not themselves establish that the merchant obtained and retained the shopper's agreement (raw lines 83, 272, 312–321; PAD overview raw lines 29–60).
- Both flows import and initialize `PreAuthorizedDebitCanada`. Sessions says no extra Component configuration and adds optional billing address plus the standard four tokenization parameters to `/sessions`. Advanced shows optional `enableStoreDetails: true` to display a save-details checkbox from Web v5.24.0, and requires `eft_directdebit_CA`, bank account number, five-digit branch code, three-digit bank code, and owner name in `/payments`; its billing address and tokenization fields are listed separately (raw lines 43–83, 206–272).
- The guide recommends tokenizing an initial payment for subsequent recurring PADs and discourages one-off PADs due to chargeback risk. It requires a shopper mandate for future recurring payments, directs merchants to enable the recurring token lifecycle webhook, and says the mandate ID need not be included in a later token payment request. `storedPaymentMethodId` arrives through `recurring.token.created` and must be saved with the shopper reference (raw lines 81–83, 123, 129–140, 270–272, 353, 359–370). Advanced `/payments` also describes conditional tokenization fields in `additionalData`: they require both token-creation request parameters and Customer Area **Developers > Additional data > Recurring details** (raw lines 312–321).
- An Advanced sample response has `resultCode: Authorised`, yet both outcome sections say it can take up to five business days to learn whether the bank authorized the debit. Successful payments appear in Settlement details; failed ones may produce `CHARGEBACK`. Do not equate the synchronous sample status, token webhook or request submission with final bank authorization or settled funds (raw lines 119–125, 323–355).
- TEST accepts real Canadian bank details without debiting that account or the listed test credentials. Setting `ownerName` to `chargeback:<reason>` tests a return; in TEST the return goes directly to Chargeback. The return table allows codes 01 and 08 at most one retry within 30 days of original authorization, forbids retry for the listed other codes, and tells merchants to suspend recurring debits and resolve mandate or notification disputes for codes 15–21. Code 03 requires a new PAD agreement for a new transaction (raw lines 142–188, 376–418). Contact Support before adding PADs Canada in the live Customer Area; this source snapshot does not prove live activation or a real debit (raw lines 190–192, 420–422).

## Source cautions

- The two curl examples place `-d` on a new line after `-X POST` without a continuation, and show `storePaymentMethod` as the string `"true"`; verify syntax and field types against the linked Checkout API before copying them (raw lines 87–115, 276–310). Their sample Canadian billing address includes `city: Amsterdam`, so it is illustrative rather than validated Canadian address data (raw lines 102–108, 297–303).
- Advanced calls `eft_directdebit_CA.mandateId` an Adyen-generated ID for the agreement and treats the initial request date as `dateOfSignature`; neither statement documents the customer's actual consent record. Follow the linked PAD mandate authority for what must be obtained and retained (raw lines 312–321; PAD overview raw lines 29–60).

## Detail locators

- Sessions prerequisites, Component import, no additional configuration and `/sessions` fields: raw lines 25–83.
- Sessions token outcome, delayed bank result, recurring and TEST/return behavior: raw lines 117–192.
- Advanced prerequisites, optional save-details checkbox and required `/payments` bank fields: raw lines 194–272.
- Advanced sample request/response, conditional additional data and delayed result: raw lines 274–355.
- Advanced recurring, TEST/return codes and live gate: raw lines 359–422.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-pad|PAD overview (mandate and chargeback context)]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pad/web-component/2026-09-15|PAD Web Component, fetched 2026-09-15]]
