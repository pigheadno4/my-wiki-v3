---
title: "Stripe Collection and Ingest Log"
type: log
tags: [stripe, github-repository, operations]
---

> Stripe-specific collection and ingest history. The root [[log]] keeps a concise cross-provider chronology.

## [2026-08-13] ingest | stripe/ai `main@1953b6c`

- Full-ingested work item `github-39ab9debac014faec1c5` at exact SHA `1953b6cce7344d880a054c42b8dd21ca3e50ebd5` after serial full reading of all 212 required evidence paths.
- Added an independently package-qualified baseline for `@stripe/ai-sdk@0.1.3`, `@stripe/token-meter@0.1.0`, `@stripe/mcp@0.3.3`, `@stripe/agent-toolkit@0.9.1`, and `stripe-agent-toolkit@0.7.0`, plus skills, provider manifests, and benchmarks.
- Recorded private-preview access, proxy tool-calling limits, fire-and-forget meter-delivery risk, remote MCP dependency, toolkit migration requirements, and benchmark methodology.
- Preserved contradictions between runtime source and examples/readmes instead of promoting stale guidance as package behavior.

## [2026-08-08] ingest | stripe/stripe-node `22.4.0`

- Approved and processed work item `github-e923ffd86b6fd634a620` in full mode at exact SHA `57626dcdfb94164fc9f112dfaa3c57aec5130e4f`.
- Read the retained release records and exact-SHA source capsule, including repository metadata, runtime and transport implementation, generated checkout/payment/billing resources, webhook examples, and complete upstream version inventory.
- Migrated the legacy `wiki/sources/source-github-stripe-node.md` page to `wiki/sources/stripe/github/source-github-stripe-node.md`, preserving the validated `stripe@22.1.1` baseline rather than overwriting it.
- Added [[changelog-github-stripe-node]] and advanced the retained package/API baseline to `stripe@22.4.0`, Stripe API `2026-07-29.dahlia`, and OpenAPI marker `v2349`.
- Recorded server-versus-browser responsibility, runtime exports, typed resource methods, retries/idempotency, webhook and V2 event verification, pagination/search boundaries, TypeScript versioning, and release-specific Checkout, PaymentIntent, SetupIntent, Payment Link, subscription, invoice, and refund changes.
- Corrected stale concept claims and preserved the v22.4.0 contradiction between the README's one-retry default and the constructor source's fallback value of two; deterministic integrations should configure the value explicitly.

## [2026-05-08] ingest | stripe/stripe-node `22.1.1`

- Cloned exact SHA `1899375db06ae1e102a93637e193f8c9cb1de831` and retained 14 key files under `raw/github-stripe-node/` plus navigation record `raw/github-stripe-node.md`.
- Established the initial Stripe Node source and [[stripe-node-sdk]] concept against OpenAPI marker `v2252`.
- Recorded the resource pattern, seven common error classes, V1 webhook verification, automatic pagination, retry/idempotency behavior, and PaymentIntent and Checkout Session methods.
