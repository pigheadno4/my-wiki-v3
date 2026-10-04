---
title: "Braintree AIB AF Change Your Bank Account"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-af/change-your-bank-account"
raw_files:
  - "braintree/articles/aib-af/change-your-bank-account-2026-09-16.md"
tags: [braintree, aib-af, bank-account, payouts, control-panel, business-documents]
---

## Overview

This collected [[braintree]]-hosted AIB AF article documents the checking account supplied with the original application and the Control Panel upload route for changing that business bank account. It accepts either a qualifying bank statement or a signed bank letter for the new account.

The page says settled transactions are paid out to the original checking account according to a linked settlement-and-funding timeline. That is a snapshot-scoped description of the payout destination, not proof that an individual transaction settled or that a deposit arrived. The article does not identify a geographic region or pricing model, define the AF label, establish current account eligibility, or serve as independent current bank policy.

## Key takeaways

- To update the bank account information, the page directs the merchant to use the Business Uploads Tool in the Control Panel and upload either a bank statement or a signed bank letter for the new account. This documented user-interface route neither proves nor disproves that an API route exists, and an upload does not establish acceptance or completion of the requested change.
- Screenshots of an online-banking profile are not accepted.
- A bank statement must identify the account holder using the business's legal name, include the IBAN and BIC/SWIFT Code, state the account currency, use only letters and characters from the English alphabet, and carry a clearly stated issue date within the prior three months.
- A bank letter must be on official bank letterhead; identify the legal business account holder; include the IBAN, BIC/SWIFT Code, and account currency; be signed by a bank representative; use only letters and characters from the English alphabet; and carry a clearly stated issue date within the prior six months.
- The submitted account must be a business checking account. The page rejects savings, deposit-only, and prepaid debit accounts.

> [!warning] Captured AIB AF scope
> Keep the account and document conditions within this captured AIB AF article. Do not transfer them to AIB BF or another processor, account, region, or pricing configuration, and do not present them as current independent bank policy, current merchant eligibility, or proof that a bank-account change or payout completed.

> [!warning] UI and linked-authority boundaries
> The Business Uploads Tool is the procedure documented here; that does not establish the presence or absence of an API route. Links to the account-information guide and settlement-and-funding timeline provide navigation only and do not prove that those unread targets agree with this snapshot.

## Detail locators

- Original-application checking account, settled-transaction payout destination, and settlement-timeline navigation: opening paragraph, raw line 16.
- Business Uploads Tool, Control Panel route, and bank-statement-or-signed-bank-letter alternatives: opening section, raw line 18.
- Online-banking-profile screenshot rejection: first `NOTE`, raw lines 21-22.
- Bank-statement name, IBAN, BIC/SWIFT, currency, character-set, and three-month recency requirements: `## Bank Statement`, raw lines 29-36.
- Bank-letter letterhead, name, IBAN, BIC/SWIFT, currency, signature, character-set, and six-month recency requirements: `## Bank Letter`, raw lines 39-48.
- Business-checking requirement and rejected account types: final `NOTE`, raw lines 51-52.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Administration context: [[braintree-control-panel]]

## Related raw documentation

- [[raw/braintree/articles/aib-af/transactions/settlement-funding-timeline-2026-09-16|Braintree AIB AF settlement and funding timeline]] - unread navigation-only destination linked for payout timing; not used as factual evidence here
- [[raw/braintree/articles/guides/account-information-2026-09-16|Braintree account information guide]] - unread navigation-only destination linked for the Business Uploads Tool; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/aib-af/change-your-bank-account-2026-09-16|Braintree AIB AF Change Your Bank Account]] - complete collected snapshot covering the documented bank-account update route, accepted document alternatives and their requirements, and rejected documents and account types
