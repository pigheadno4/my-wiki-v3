---
title: "Braintree Control Panel: Vault Card Verification"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/vault/card-verification"
raw_files:
  - "braintree/articles/control-panel/vault/card-verification-2026-09-16.md"
tags: [braintree, control-panel, vault, card-verification, avs, cvv]
---

## Overview

This collected Braintree article documents account-wide and individual verification of credit and debit card payment methods associated with the Vault, including Control Panel enablement, retry behavior and re-verification of an already vaulted card. The verified object is the card payment method, not the Vault customer's identity, and the page's verification authorizations are distinct from a purchase authorization intended to settle.

## Key takeaways

- The feature applies only to credit and debit card payment methods. When account-wide card verification is enabled in the Control Panel, the gateway checks a card before Vault storage and applies the merchant's configured AVS and CVV rules; a card found invalid is not stored.
- Braintree describes the verification mechanism as a $0 or $1 authorization followed by an automatic void. It normally tries $0 first and falls back to $1 where $0 is unsupported; a successful $1 verification is immediately followed by a void so the verification transaction does not settle. Some banks may not recognize that void immediately, leaving a temporary pending charge visible to the cardholder.
- The account-wide setting is under `Processing` > `Vaulting` > `Card Verification`. The page also routes individual card verification to developer documentation, so enabling the account-wide toggle is not presented as the only verification path. The collected page requires a Control Panel login for its UI steps but does not identify a required role or permission.
- A processor response that specifically signals unsupported $0 authorization causes an automatic $1 retry. A generic decline does not trigger that retry by default, but the separate `Retry All Failed $0` setting can retry all failed $0 authorizations as $1; failed Apple Pay verification must instead be retried manually according to the page.
- Re-verifying a card already stored in a customer Vault record requires collecting CVV again because Braintree says it never stores CVV. The Control Panel action is performed on the token-linked payment method, and the next page displays the verification result with CVV and AVS responses; this is card-payment-method verification, not verification of the customer record itself.

> [!warning] Verification and snapshot boundaries
> A card verification uses an authorization as a checking mechanism, but this page does not establish approval or settlement of a later purchase. A successful $1 verification is voided, and the void may remain temporarily visible as a pending charge. Treat the documented 2026-09-16 Control Panel paths, retry options and Apple Pay behavior as collected evidence rather than a guarantee of current support.

## Detail locators

- Eligible payment methods, verification purpose, checked fields and pre-Vault rejection behavior: `# Card Verification`, lines 17-32.
- $0/$1 authorization, automatic void and pending-charge warning: `## How it works`, lines 35-43.
- Account-wide Control Panel route and individual/API alternatives: `## Enabling card verification`, lines 48-69.
- Processor-specific fallback, generic-decline default and the optional retry-all setting: `## Retrying all failed $0 verifications`, lines 74-97.
- CVV recollection, Vault customer/payment-method navigation and displayed result: `## Verifying vaulted cards`, lines 102-125.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/guides/fraud-tools/basic/avs-cvv-rules-2026-09-16|Braintree AVS and CVV Rules article]] - unread navigation-only authority for configuring the rules applied during verification; not used as factual evidence here
- [[raw/braintree/articles/control-panel/transactions/refunds-voids-credits-2026-09-16|Braintree Refunds, Voids, and Credits article]] - unread navigation-only authority for general void behavior; not used as factual evidence here
- [[raw/braintree/docs/guides/credit-cards/server-side/node-2026-09-16|Braintree Credit Cards server-side guide for Node.js]] - unread navigation-only collected SDK route for individual card verification; not used as factual evidence here
- [[raw/braintree/docs/reference/request/payment-method/update/node-2026-09-16|Braintree Payment Method Update request reference for Node.js]] - unread navigation-only collected API route for re-verification; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/control-panel/vault/card-verification-2026-09-16|Braintree Control Panel Card Verification article]] - complete collected page covering card-verification purpose, account-wide access, authorization and retry outcomes, and vaulted-card re-verification boundaries
