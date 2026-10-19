---
title: "Adyen Issuing payment authorisation"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/authorisation"
raw_files:
  - "adyen/docs/issuing/authorisation/2026-09-15.md"
tags: [adyen, issuing, authorisation, transaction-rules, relayed-authorisation]
---

## Overview

Adyen's Issuing authorization guide (last modified 2023-08-14, captured 2026-09-15) describes how an Adyen-issued-card payment attempt reaches an initial approved or refused decision. Adyen performs mandatory issuer validations and internal transaction rules; after successful internal checks, the platform can use transaction rules, relayed authorisation, or both for custom verification. The guide separately explains that later scheme advice can supersede the initial decision and change the final status and reserved balance. This is authorization-stage evidence, not evidence of capture or settlement. [[adyen-issuing]] [[adyen]]

## Key takeaways

- **Issuer checks first:** Adyen must authorize each issued-card payment and checks card/transaction legitimacy (examples: expiry, CVC, available balance) plus internal regulatory transaction rules (examples: missing payment-instrument capabilities, contactless limit and ecommerce CVC2). A failed validation refuses the attempt before custom verification. See raw lines 19–37 and 63–67.
- **Platform controls:** If internal checks succeed, configured transaction rules can automatically approve/decline based on conditions such as amount, transaction count or payment type; the rules apply to each payment attempt. Relayed authorisation sends each attempt to the platform server for its own decision. The server has **up to 2000 ms** to respond; without a response in that period, Adyen applies the configured default fallback. See raw lines 39–55.
- **Initial flow order:** Payment request → Adyen validations → configured transaction rules (refuse if noncompliant) → configured relayed-authorisation webhook (server response or fallback). If relayed authorisation is not configured after successful earlier checks, the initial flow approves. The flow diagram's endpoint is initial approval/refusal. See raw lines 57–71.
- **Later scheme advice:** A scheme may evaluate a payment after Adyen's initial flow, for example when real-time completion was not possible. If the scheme decision differs, Adyen defers to it; scheme advice sets the final payment status and reserved-balance change and produces a `balancePlatform.transfer.updated` webhook with a new booking event. Do not treat the initial response alone as final in that case. See raw lines 73–79.

## Detail locators

- Internal validation and regulatory-rule examples: raw lines 23–37.
- Automatic rules, relayed decision time budget and fallback: raw lines 39–55.
- Numbered initial payment flow: raw lines 57–71.
- Post-initial scheme precedence and update webhook: raw lines 73–79.

## Related

- [[adyen-issuing]] — Issuing concept.
- [[source-adyen-docs-issuing-authorisation-scheme-advice]] — detailed scheme-advice webhook and reconciliation behavior.

## Raw Sources

- [[raw/adyen/docs/issuing/authorisation/2026-09-15|Payment authorisation, captured 2026-09-15]]
