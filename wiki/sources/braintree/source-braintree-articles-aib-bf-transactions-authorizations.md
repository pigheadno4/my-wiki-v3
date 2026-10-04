---
title: "Braintree AIB BF Authorizations"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-bf/transactions/authorizations"
raw_files:
  - "braintree/articles/aib-bf/transactions/authorizations-2026-09-16.md"
tags: [braintree, aib-bf, transactions, authorizations, voids, gateway-rejections]
---

## Overview

This pinned Braintree-hosted AIB BF article describes the hold associated with an Authorized transaction and what the article says happens when the authorization is later submitted for settlement, expires, is voided, or is followed by a gateway rejection. Authorization is a pre-settlement state: the hold is not evidence that settlement occurred, funds were debited, or the merchant was funded.

Treat this as a 2026-09-16 snapshot of the AIB BF route. It is not AIB AF documentation, current independent bank policy, account-specific eligibility, or proof of any transaction outcome.

## Key takeaways

- In the Authorized status, the customer's bank puts a hold on the funds needed for the transaction. If the transaction is later submitted for settlement, the article says those funds will be debited from the customer's bank account and routed to the merchant account.
- A pending authorization that is not submitted for settlement in time expires and the customer's bank releases the hold; the expiration timeline differs by card type. In void and gateway-rejection cases, customers may still have to wait for expiration before seeing held funds released.
- A void cancels the transfer of held funds before settlement. The article says a transaction can typically be voided only while Authorized or Submitted for Settlement; for an Authorized transaction, the authorization should disappear and held funds should be released within 24 to 48 hours. These are qualified expectations, not a bank-release guarantee.
- If all authorized transactions are automatically submitted for settlement, the article says voiding is available only after the transaction enters Submitted for Settlement. Voiding in that status does not automatically release the original hold: the pending authorization remains until expiration, after which the customer can contact the bank.
- A gateway rejection can occur after the transaction becomes Authorized and the bank has placed a hold. The gateway then voids the original authorization; under automatic settlement submission, this void happens after the transaction has already entered Submitted for Settlement.

> [!warning] Authorization is not settlement or funding
> An authorization hold does not show that funds were debited, settled, routed to the merchant account, or deposited. The article makes debit and routing conditional on later settlement submission, and release behavior can depend on expiration, transaction status, gateway handling, and the customer's bank.

> [!warning] Captured AIB BF scope
> Keep these lifecycle statements within the captured AIB BF article. Do not transfer them to AIB AF or treat them as current independent bank policy, account-specific terms, or evidence that an individual authorization, void, release, settlement, or funding event occurred.

## Detail locators

- Authorized-state hold and later-settlement debit/routing condition: `# Authorizations`, raw line 16.
- Expiration when not submitted for settlement, card-type variability, and bank release: `# Authorizations`, raw line 18.
- Possible wait for expiration after voids and gateway rejections: `# Authorizations`, raw line 20.
- Void meaning, typical eligible statuses, and qualified 24-to-48-hour Authorized-void release: `## Voids`, raw line 25.
- Automatic settlement-submission condition for void timing: `## Voids`, raw line 27.
- Submitted-for-Settlement void behavior, non-automatic release, expiration, and bank-contact route: `### VoidingSubmitted for Settlementtransactions`, raw line 32.
- Gateway-rejection trigger, possible post-authorization timing, original-authorization void, and release: `## Gateway Rejections`, raw line 37.
- Automatic settlement-submission condition for gateway-rejection void timing: `## Gateway Rejections`, raw line 39.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/articles/aib-bf/transactions/authorizations-2026-09-16|Braintree AIB BF Authorizations article]] - complete captured page covering authorization holds, expiration, void behavior and gateway-rejection effects
