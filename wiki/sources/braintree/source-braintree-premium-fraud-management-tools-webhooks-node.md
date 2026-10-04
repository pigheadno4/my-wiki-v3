---
title: "Braintree Premium Fraud Management Tools Webhooks (Node.js)"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/premium-fraud-management-tools/webhooks/node"
raw_files:
  - "braintree/docs/guides/premium-fraud-management-tools/webhooks/node-2026-09-16.md"
tags: [braintree, node-js, webhooks, fraud-protection-advanced, transaction-review]
---

## Overview

This collected Braintree Node.js guide describes the webhook step for merchants using **Fraud Protection Advanced**. After a transaction is formally reviewed in the Fraud Protection Advanced dashboard, Braintree sends a `TRANSACTION_REVIEWED` webhook whose parsed notification can identify the review event and reviewed transaction. This is a server-side notification-handling route, not evidence that client-side checkout, fraud evaluation, payment processing, or a consequential transaction action succeeded.

## Key takeaways

- The page says these Fraud Protection webhooks are available only to merchants using **Fraud Protection Advanced**. Merchants using the distinct standard **Fraud Protection** product are told to skip this webhook step and continue to Testing & Go Live. The 2026-09-16 snapshot does not establish current merchant eligibility, account enablement, or SDK-version support.
- The general workflow is to configure at least one destination URL, parse incoming notifications, and store details from `WebhookNotification` objects for selected trigger kinds. The setup, parsing and trigger links own their respective requirements; this guide does not establish delivery timing, ordering, retry, duplicate-delivery, signature-validation, or acknowledgement semantics.
- The documented fraud event occurs only after a transaction has been formally reviewed in the Fraud Protection Advanced dashboard. The guide names the event as `TRANSACTION_REVIEWED`; its Node callback and Promise snippets illustrate parsing `bt_signature` and `bt_payload`, then reading example `kind`, transaction ID and timestamp values. Example values are not guarantees of universal payload coverage or runtime success.
- The webhook's transaction ID can be passed to `gateway.transaction.find` to request additional transaction information if needed. That optional lookup is separate from receiving the webhook and does not prove that the lookup succeeded or that any payment, void, refund, settlement, or other consequential transaction action was requested or completed.

> [!warning] Product, event and lifecycle boundary
> Keep the named **Fraud Protection Advanced** eligibility condition distinct from standard **Fraud Protection** and other fraud products. A reviewed-transaction notification reports a dashboard review outcome; this guide does not define or prove downstream void/refund behavior, transaction finality, processor approval, settlement, or current availability. The dedicated event reference owns any more specific action qualification.

## Detail locators

- Product availability and standard-versus-Advanced branch: `**AVAILABILITY**`, lines 16-17.
- Report examples and generic destination/parse/store workflow: lines 19-32.
- Formally reviewed transaction condition and `TRANSACTION_REVIEWED` event: `## Fraud Protection`, lines 35-37.
- Node callback parsing and example notification properties: `### Callbacks`, lines 38-55.
- Node Promise parsing and example notification properties: `### Promises`, lines 57-73.
- Optional transaction-ID lookup in callback and Promise forms: lines 74-83.
- Dedicated references for fraud-protection webhooks, general webhooks and Transaction Find: `## See also`, lines 86-91.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-webhooks]]
- Product concept: [[braintree-fraud-protection-advanced]]
- Dedicated reviewed-event reference: [[source-braintree-webhooks-fraud-protection-node]]

## Related raw API references

- [[raw/braintree/docs/reference/general/webhooks/fraud-protection/node-2026-09-16|Braintree Node.js Fraud Protection webhook reference]] - navigation only; this guide's linked event reference, not read as raw evidence for this source
- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Braintree webhooks overview]] - navigation only; linked general webhook setup context, not read as factual evidence for this source
- [[raw/braintree/docs/guides/webhooks/create/node-2026-09-16|Braintree Node.js webhook creation guide]] - navigation only; linked destination setup route, not read as factual evidence for this source
- [[raw/braintree/docs/guides/webhooks/parse/node-2026-09-16|Braintree Node.js webhook parsing guide]] - navigation only; linked parsing route, not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/transaction/find/node-2026-09-16|Braintree Node.js Transaction Find reference]] - navigation only; linked lookup route, not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/premium-fraud-management-tools/webhooks/node-2026-09-16|Braintree Premium Fraud Management Tools webhooks guide (Node.js)]] - complete collected page covering Advanced-only availability, the reviewed-transaction event, Node parsing examples and optional Transaction Find lookup
