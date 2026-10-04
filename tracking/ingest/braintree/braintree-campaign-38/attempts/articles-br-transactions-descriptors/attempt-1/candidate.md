---
title: "Braintree Brazil Transaction Descriptors"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/br/transactions/descriptors"
raw_files:
  - "braintree/articles/br/transactions/descriptors-2026-09-16.md"
tags: [braintree, brazil, transactions, descriptors, statements]
---

## Overview

This 2026-09-16 Braintree webpage snapshot, filed under the Brazil (`br`) documentation path, describes the identifying information customers may see on statements for purchases through a mobile app or website. It documents an account-level descriptor format and application-derived configuration, while stating that the customer's bank ultimately determines the exact statement presentation. Use [[braintree-control-panel]] for the provider-level administration route and [[braintree]] for company context.

> [!warning] Snapshot and scope boundary
> The Brazil path and captured article do not prove current regional availability, a particular merchant account's configuration or eligibility, card-brand or payment-method support, exact bank rendering, or successful authorization, settlement, posting, or payment. The body does not identify a processor, environment, card brand, or account-funding model; do not transfer these rules to sibling processor, account, or regional articles.

## Key takeaways

- The page says the descriptor appears after a transaction has been authorized and after it has settled, becoming permanent once the customer's bank finalizes the transaction status. This is the article's statement-display sequence, not proof that any particular transaction completed or a guarantee of bank-posting timing.
- The account descriptor allows 22 characters. The first eight are described as hardcoded and common to all transactions; content after those characters is prefixed with `*`, and the page allows up to 13 following characters for a merchant-account-level descriptor. The raw states that only numbers and letters are allowed after the first eight characters.
- The page says Braintree configures the descriptor from application-process information and routes later changes through its contact path. That does not establish a merchant-specific configured value or acceptance of a requested change.
- The page's examples do not cleanly match its stated restrictions: one labeled-valid example has fewer than eight characters before `*`, and another contains a space despite the stated numbers-and-letters-only rule. This snapshot does not resolve those conflicts, so preserve the raw examples and requirements rather than treating either as validated input rules.

## Detail locators

- Descriptor purpose, bank-controlled rendering and illustrative `COMPNAME*TXNDESCRIPTOR` format: `# Descriptors`, raw lines 14-18.
- Post-authorization, post-settlement and bank-finalization display wording: `# Descriptors`, raw line 20.
- Total length, hardcoded prefix, `*` separator, character restriction and merchant-account-level suffix length: `## Descriptor requirements`, raw lines 23-30.
- Labeled-valid examples, including the unresolved prefix-length and space conflicts: raw lines 32-37.
- Application-derived configuration and contact-based change route: raw line 39.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Brazil account-navigation context: [[source-braintree-articles-br-overview]]
- General descriptor route: [[source-braintree-control-panel-descriptors]]

## Raw Sources

- [[raw/braintree/articles/br/transactions/descriptors-2026-09-16|Braintree Brazil transaction descriptors snapshot (2026-09-16)]]
