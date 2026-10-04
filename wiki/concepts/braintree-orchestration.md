---
title: "Braintree Orchestration"
type: concept
category: technology
tags: [braintree, paypal-orchestration, payment-processing, processor-connections, transaction-lifecycle]
---

## Braintree Orchestration

A collected 2026-09-16 overview defines PayPal Payment Orchestration as a Braintree-facing layer for connecting multiple PSPs, acquirers and value-added services through one integration, allowing merchants to route and manage transactions while retaining their existing client-side tokenization and SDK code. It requires authorization, capture, void and refund operations to go through Braintree to avoid reconciliation and synchronization problems from direct connector calls. This provider-level definition does not establish connector-specific capabilities or prerequisites, does not prove enablement, execution, settlement or funding, and does not make Orchestration a [[braintree-forward-api]] flow. [[source-braintree-orchestration-overview]]

A collected Braintree Adyen integration guide documents a PayPal Orchestration route in which merchants keep their existing Braintree integration while transactions are processed through an Adyen processor connection. For this connection, transaction operations remain on Braintree; performing operations directly with Adyen can cause synchronization issues and data inconsistencies. The guide assigns settlement, chargebacks, reporting and reconciliation to the merchant's Adyen portal. This is distinct from [[braintree-forward-api]], which is the documented outbound request-construction and forwarding route. [[source-braintree-orchestration-adyen]]

## Adyen-qualified route

The collected Adyen route requires currency-specific Braintree merchant accounts, an Adyen account for each merchant, Braintree-assisted processor-connection configuration and an Adyen API user with the `API PCI Payments` role. Its core transaction path uses authorization followed by capture rather than a single-step charge. Capture and refund are asynchronous: `SETTLING` awaits an Adyen webhook and can become `SETTLED` or `SETTLEMENT_DECLINED`, so fulfillment waits for `SETTLED` and pending or uncertain results require status lookup rather than blind duplication. These are Adyen-integration facts from the 2026-09-16 snapshot, not universal behavior for every orchestration destination or proof of current eligibility, transaction success, settlement or funding. [[source-braintree-orchestration-adyen]]

The guide's country scope is unresolved: its introduction says the connection supports transactions in most Adyen-supported countries, while its later supported-countries section says all. Confirm current merchant, country, currency and account eligibility rather than selecting either statement as authoritative.

## Sources
- [[source-braintree-orchestration-dlocal]] - 2026-09-16 Braintree-hosted dLocal Payment Orchestration route covering Braintree-owned transaction operations, dual-provider setup, reconciliation and duplicate-retry cautions, and the unresolved Turkey decimal-format conflict
- [[source-braintree-orchestration-flexfactor]] - Braintree-hosted FlexFactor route through PayPal Orchestration Platform with currency-specific merchant-account and securely shared FlexFactor-credential prerequisites, merchant-triggered initial retries, integration-scoped automatic retries, and `SETTLING` fulfillment guardrails; not independent FlexFactor provider authority or proof of enablement, execution, recovery, settlement, dispute outcome, or funding

- [[source-braintree-orchestration-adyen]] - 2026-09-16 Braintree-hosted Adyen processor-connection guide covering setup, Braintree-owned transaction operations, authorization/capture support, asynchronous status handling and an unresolved country-scope conflict
