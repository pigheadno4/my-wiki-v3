---
title: "Braintree AIB AF Authorizations"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-af/transactions/authorizations"
raw_files:
  - "braintree/articles/aib-af/transactions/authorizations-2026-09-16.md"
tags: [braintree, aib-af, transactions, authorizations, voids, gateway-rejections]
---

## Overview

This pinned Braintree-hosted AIB AF article explains the authorization hold on a customer's funds, the later settlement step that debits those funds and routes them into the merchant account, and how expiration, voids, and gateway rejections affect release of the hold. It is snapshot evidence for this exact AIB AF route; the page does not define the AIB AF label or establish a region, current account eligibility, independent bank policy, successful settlement, merchant funding, or arrival of a bank deposit.

## Key takeaways

- `Authorized` means the customer's bank has placed a hold for the transaction amount. Only if the transaction is later submitted for settlement does the article describe those funds as being debited from the customer's bank account and routed into the merchant account; authorization itself is not settlement or funding proof.
- An authorization that is not submitted for settlement in time expires and the bank releases the held funds. The expiration timeline varies by card type.
- The article says a void cancels transfer of held funds before settlement and is typically available for `Authorized` or `Submitted for Settlement` transactions. For a void while `Authorized`, it says the authorization should disappear and held funds will be released within 24–48 hours; this wording is not a guarantee of immediate bank-side release.
- Automatic settlement submission changes the voiding point: the merchant can void only after the transaction reaches `Submitted for Settlement`. Voiding in that state does not automatically release the original hold; the pending authorization remains until expiry, and the article routes the customer to their bank, which should be able to see the void request and update the statement.
- A gateway rejection can occur after authorization and after the bank has already placed a hold. The gateway then voids the original authorization, but the article separately warns that customers may have to wait until authorization expiry to see held funds released. With automatic settlement submission, the gateway rejection is voided only after the transaction has entered `Submitted for Settlement`.

> [!warning] Authorization, settlement, and funding are distinct
> This snapshot documents a bank hold and qualified release behavior. It does not prove that a transaction was submitted for settlement, settled successfully, reached a merchant account, or funded a bank account. Do not transfer its AIB AF wording to AIB BF or treat it as current independent bank policy.

## Detail locators

- Authorization hold and later settlement-dependent debit and merchant-account routing: `# Authorizations`, raw line 16.
- Expiry when not submitted in time, bank release, and card-type timing variation: `# Authorizations`, raw line 18.
- Possible release delay after voids and gateway rejections: `# Authorizations`, raw line 20.
- Void meaning, typical eligible statuses, and the qualified 24–48-hour Authorized-void statement: `## Voids`, raw line 25.
- Automatic-submission constraint: `## Voids`, raw line 27.
- Submitted-for-settlement void behavior, expiry, and customer-bank route: `### Voiding Submitted for Settlement transactions`, raw line 32.
- Post-authorization gateway rejection, gateway void, and bank release wording: `## Gateway Rejections`, raw line 37.
- Automatic-submission gateway-rejection timing: `## Gateway Rejections`, raw line 39.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- General lifecycle route: [[source-braintree-transaction-lifecycle]]
- Control Panel gateway-rejection route: [[source-braintree-control-panel-gateway-rejections]]

## Raw Sources

- [[raw/braintree/articles/aib-af/transactions/authorizations-2026-09-16|Braintree AIB AF Authorizations article]] - complete captured page covering authorization holds, expiration, void timing and post-authorization gateway rejection behavior
