---
title: "Adyen Tokenization webhooks v1 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Tokenization-webhooks/latest/overview"
raw_files:
  - "adyen/api-explorer/Tokenization-webhooks/latest/overview/2026-09-15.md"
tags: [adyen, tokenization, webhooks, api-explorer]
---

## Overview

Captured API Explorer overview for **Tokenization webhooks v1**. Adyen describes saved payment details as tokens, stored with shopper consent, and says these webhooks inform the recipient about token lifecycle events. This is an incoming-event directory, not a token-management API operation or a network-token contract.

## Key takeaways

- The General endpoint table lists four POST event routes: `recurring.token.alreadyExisting`, `recurring.token.created`, `recurring.token.disabled`, and `recurring.token.updated`.
- This overview supplies event names and summaries only. It does not define event payload fields, token or payment outcome semantics, webhook acknowledgment, delivery, ordering, retry, deduplication, or signature rules. Use each event reference and the linked tokenization documentation for those details.

## Detail locators

- Shopper consent, stored payment details and token meaning: raw lines 5–9.
- Exact POST event names and summary labels: raw lines 11–19.

## Related

- [[adyen]]
- [[adyen-tokenization]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/api-explorer/Tokenization-webhooks/latest/overview/2026-09-15|Tokenization webhooks v1 overview, captured 2026-09-15]]

## Related raw API references

- `Tokenization-webhooks/latest/post/recurring.token.alreadyExisting`
- `Tokenization-webhooks/latest/post/recurring.token.created`
- `Tokenization-webhooks/latest/post/recurring.token.disabled`
- `Tokenization-webhooks/latest/post/recurring.token.updated`
