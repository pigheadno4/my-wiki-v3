---
title: "Adyen Issuing: Transaction rule examples"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/authorisation/transaction-rules/examples"
raw_files:
  - "adyen/docs/issuing/authorisation/transaction-rules/examples/2026-09-15.md"
tags: [adyen, issuing, authorisation, transaction-rules, examples]
---

## Overview

This Adyen Issuing example collection (last modified 2022-04-04; captured 2026-09-15) shows illustrative JSON transaction rules for card-payment channel, country/MCC, amount/count, international, ATM and scoring conditions. The examples illustrate `blockList` or `velocity` rules and `hardBlock` or `scoreBased` outcomes at per-transaction, rolling or sliding intervals. They are examples of configured criteria, not proof that a rule was created, active, evaluated, or that a payment was authorized, declined, captured or settled. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The processing-type blocklist examples use `noneMatch: ["pos"]` to decline an ecommerce payment while allowing POS, and `anyMatch: ["pos"]` for the inverse POS block (raw lines 21-67). The US/MCC example combines `countries` `anyMatch: ["US"]` with `mccs` `noneMatch` for grocery, restaurant and fast-food MCCs to illustrate blocking other US categories (raw lines 69-97). Do not derive general multi-condition rule-evaluation semantics from these examples: the linked general and creation guides disagree on whether all versus any specified condition triggers a rule.
- Velocity examples show a per-transaction USD 100 amount threshold (`greaterThan` 10000 minor units), a one-month transaction count threshold of 50 resetting on day 15, and two distinct rolling rules for US/Canada fuel-related MCCs: monthly USD 500 amount and monthly count 10. The guide says meeting either fuel rule leads to a decline (raw lines 99-229). Exact IDs, MCCs, amounts and dates are example inputs.
- Entity scope matters: the international daily EUR 50 example targets one `PaymentInstrument`; a last-12-hours EUR 2000 example targets the whole `BalancePlatform`; a daily EUR 1000 example targets all payment instruments in one `BalanceAccount`; and the two-week EUR 2000 ATM example targets a balance platform (raw lines 231-396). The weekly-limit heading for that ATM section should be read with its explicit **every two weeks** prose and `duration: 2 weeks`.
- Two `scoreBased` examples target a payment instrument: a time-of-day condition with `score: 30`, and token processing with `score: -25` (raw lines 398-461). The prose says **11 AM–6 PM Europe/Amsterdam**, while the JSON time window is **10:00–17:00 +01:00** (raw lines 404, 418-428); the source does not reconcile these times. Do not convert this example into an exact local-hour implementation without checking the intended timezone/offset behavior.

## Example and evidence cautions

- The balance-account daily-limit JSON appears structurally incomplete around closing braces (raw lines 323-353). The ATM example omits `outcomeType` even though the heading/prose describes a decline (raw lines 355-396). Treat those snippets as illustrative, not directly deployable validated payloads.
- For actual rule creation, allowed condition combinations, hierarchy and outcomes, consult [[source-adyen-docs-issuing-authorisation-transaction-rules]] and [[source-adyen-docs-issuing-authorisation-transaction-rules-create-and-manage]]. Those two captured guides conflict over all-versus-any condition matching; this example page does not resolve the conflict.

## Detail locators

- Channel and country/MCC examples: raw lines 21-97. Velocity amount/count and combined fuel rules: raw lines 99-229. Scoped international, balance-platform, balance-account and ATM limit examples: raw lines 231-396. Scoring examples: raw lines 398-461.

## Related

- [[adyen]] — provider.
- [[adyen-issuing]] — Issuing concept.
- [[source-adyen-docs-issuing-authorisation-transaction-rules]] — rule behavior and scope.
- [[source-adyen-docs-issuing-authorisation-transaction-rules-create-and-manage]] — creation and management.

## Raw Sources

- [[raw/adyen/docs/issuing/authorisation/transaction-rules/examples/2026-09-15|2026-09-15 capture of Adyen Issuing transaction-rule examples]]
