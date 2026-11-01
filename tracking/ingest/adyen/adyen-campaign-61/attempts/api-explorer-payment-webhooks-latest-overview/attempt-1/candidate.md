---
title: "Adyen Payment webhooks (deprecated) v1 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/payment-webhooks/latest/overview"
raw_files:
  - "adyen/api-explorer/payment-webhooks/latest/overview/2026-09-15.md"
tags: [adyen, platforms, payment-webhooks, deprecated]
---

## Overview

This 2026-09-15-captured API Explorer overview catalogs Adyen's **deprecated Payment webhooks v1**. It says Adyen sends these incoming notifications about creation of platform payment resources and money movements, and explicitly directs readers to “accounting webhooks,” linking the Transfer Webhooks overview, instead. The `latest` route in this capture displays v1; it does not establish current availability or an individual event contract. [[adyen]] [[adyen-webhooks]]

## Key takeaways

- The six listed POST event paths are `balancePlatform.incomingTransfer.created`, `.updated`, `balancePlatform.outgoingTransfer.created`, `.updated`, `balancePlatform.payment.created`, and `.updated`. The payment-created summary names initiation of payment authorisation, refund or funds transfer; the payment-updated summary names expired or cancelled payment authorisation. These are endpoint summaries, not payload or outcome schemas.
- The page suggests using notifications to update a platform's own dashboards or track incoming funds. It does not provide request fields, response or acknowledgement rules, ordering, retry, deduplication, signature, transfer status or financial-finality semantics. Use the individual event references for those details; do not apply newer Transfer or Transaction webhook contracts to these deprecated paths by analogy.

## Detail locators

- Version, deprecation and explicit migration link: pinned raw lines 5–7.
- Family purpose and illustrative use cases: raw lines 9–11.
- Six POST paths and their summaries: `## Endpoints > ### General`, raw lines 13–23.

## Related

- [[adyen-webhooks]] — provider webhook concepts and separate event references.
- [[adyen-platforms]] — platform resource context.
- [[adyen]] — provider context.

## Related raw API references

- [[raw/adyen/api-explorer/transfer-webhooks/latest/overview/2026-09-15|Transfer Webhooks overview named by the migration link]] — navigation only; this raw was not read for this entry.

## Raw Sources

- [[raw/adyen/api-explorer/payment-webhooks/latest/overview/2026-09-15|Payment webhooks v1 overview captured 2026-09-15]]
