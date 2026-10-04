---
title: "Braintree Adyen Change Your Bank Account"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/adyen/change-your-bank-account"
raw_files:
  - "braintree/articles/adyen/change-your-bank-account-2026-09-16.md"
tags: [braintree, adyen, bank-account, settlement, multi-currency, authorized-signer]
---

## Overview

This collected Braintree-hosted Adyen processor article explains how a merchant changes the business checking account used for payouts of settled transactions. The merchant uploads a recent statement for the new account through the Business Uploads Tool in the Braintree Control Panel; Braintree Support reviews it and follows up with the Braintree account's authorized signer.

The page documents account-change and settlement-account administration, not a procedure for an independent Adyen account. It names no broad region or fee rate: its geographic prerequisite is that the new business checking account be domiciled in the same country as the merchant's business, while its multi-currency section limits the documented Adyen fee-debit base currency to the GBP or EUR selected during the original application.

## Key takeaways

- The original application supplied a business-associated checking account, and the page says settled transactions pay out to that account according to a separate settlement-and-funding timeline. This is general routing documentation, not proof that any individual transaction settled or deposit arrived.
- To change the account, upload a recent bank statement for the new account using the Business Uploads Tool in the Control Panel. Screenshots of an online-banking profile are not accepted.
- The statement must identify the matching business account holder and provide the documented currency and bank identifiers. The submitted account must be a business checking account in the same country as the business; savings, deposit-only and prepaid debit accounts are not accepted.
- Braintree Support reviews the statement and follows up with the authorized signer. The authorized signer is the only person the page permits to request access or change sensitive account information; this is distinct from the Account Admin role and cannot be managed in the Control Panel.
- For multi-currency settlement, the page permits one checking account per configured settlement currency. It says deposits use the associated settlement currency, while Adyen debits fees in the original application's GBP-or-EUR base currency; it does not state fee amounts or rates.

> [!warning] Processor and account scope
> Apply this procedure only to the Braintree account and Adyen processor context documented by this page. Do not transfer its bank-document, signer, currency or fee-debit rules to another Braintree processor, region or independent Adyen relationship.

> [!warning] Snapshot and execution boundary
> This 2026-09-16 snapshot records documentation, not current merchant eligibility, acceptance of a submitted statement, completion of a bank-account change, settlement of a transaction or arrival of a deposit.

## Detail locators

- Existing payout-account context and settlement-timeline navigation: opening paragraph, raw line 13.
- Business Uploads Tool and Control Panel route: `## Updating bank account information`, raw line 18.
- Online-banking screenshot rejection: first `NOTE`, raw lines 21-22.
- Required statement details, including name match, currency, bank insignia, IBAN and BIC/SWIFT: raw lines 26-35.
- Same-country business-checking requirement and excluded account types: second `NOTE`, raw lines 38-39.
- Authorized-signer authority, distinction from Account Admin and signer-change contact route: `### Authorized signer`, raw lines 44-52.
- Per-settlement-currency checking accounts, settlement-currency deposits and GBP/EUR Adyen fee debits: `## Multi-currency settlement`, raw lines 57-59.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Related concept: [[braintree-currencies]]
- Administration context: [[braintree-control-panel]]

## Related raw documentation

- [[raw/braintree/articles/guides/account-information-2026-09-16|Braintree account information and Business Uploads Tool guide]] - linked navigation; not read as evidence for this entry
- [[raw/braintree/articles/adyen/transactions/settlement-funding-timeline-2026-09-16|Braintree Adyen settlement and funding timeline]] - linked navigation; not read as evidence for this entry

## Raw Sources

- [[raw/braintree/articles/adyen/change-your-bank-account-2026-09-16|Braintree Adyen Change Your Bank Account]] - complete collected snapshot for the bank-account update, business-account and authorized-signer prerequisites, and multi-currency settlement-account boundaries
