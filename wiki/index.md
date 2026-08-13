# Wiki Index

> Layered catalog. Per-PSP pages live in the PSP indexes; cross-cutting pages (comparisons, analyses, generic concepts) live here. See `rules/lint.md` for the split rule.

## PSP Indexes

- [[stripe-index]] — Stripe sources, company page, and `stripe-*` concepts
- [[paypal-index]] — PayPal sources, company page, and `paypal-*` concepts
- [[metronome-index]] — Metronome sources, company page, and `metronome-*` concepts
- [[adyen-index]] — Adyen sources, company page, and versioned GitHub implementation knowledge
- [[braintree-index]] — Braintree sources, company page, server, Web, Android, and iOS SDK knowledge, and versioned GitHub implementation history

## Overview

- [[overview]] — high-level payments industry overview

## Companies

- [[paypal]] — PayPal: payment platform, JS SDK, Venmo, Orders API
- [[stripe]] — Stripe: developer-first payment APIs, PaymentIntents, Checkout, Subscriptions, Elements
- [[metronome]] — Stripe-owned usage-based billing provider capsule; collection complete, 50 sources ingested through reviewed serial and coordinator-controlled parallel campaigns
- [[adyen]] — Adyen: Web Drop-in and Components, Sessions, cards, 3DS2, and checkout actions
- [[braintree]] — Braintree: Node.js gateway operations, modular Web and native SDKs, Hosted Fields, 3DS, wallets, subscriptions, and nonce-based server handoff

## Comparisons

### Stripe vs PayPal
- [[stripe-vs-paypal-checkout-acceleration]] — Stripe Link vs PayPal Fastlane: UX architecture, token lifecycle, subscription two-step flow (verified sandbox API logs), integration fit

## Analyses

- [[analysis-paypal-pay-later-fr-integration-guide]] — PayPal Pay Later FR messaging + button integration for US merchant account (cross-border, limited release)
- [[analysis-paypal-radio-button-payment-wall]] — PayPal + Pay Later radio button payment wall: funding eligibility gating, marks, standalone buttons
- [[analysis-paypal-pay-later-ca-integration-guide]] — PayPal Pay Later CA button + message integration: biweekly Pay in 4, CAD, bilingual en_CA/fr_CA
- [[analysis-paypal-pay-later-multi-country-integration-guide]] — PayPal Pay Later button + message integration for US, FR, GB, IT, ES: per-country products, cross-border messaging, funding eligibility
- [[analysis-paypal-sdk-v5-vs-v6-multi-country]] — PayPal JS SDK v5 vs v6 multi-country switching: runtime config, React v8→v9, Pay Later messaging, performance patterns, SSR
- [[analysis-paypal-messages-ios-vs-android]] — PayPal Messages native mobile comparison: Braintree-only policy, separate release/ref histories, configuration traps, callback/state risks, and rollout guidance

## Concepts (generic)

- [[disputes]] — Disputes & Chargebacks: direct vs bank-chargeback paths, merchant implications, PayPal Disputes API
- [[recurring-payments]] — Recurring payments: generic concept — stored credentials standard, dunning/retry, SCA, platform comparison table (PayPal/Stripe/Adyen)
- [[agentic-commerce]] — Agentic Commerce: AI agents that discover products, manage carts, and complete purchases; inbound (Store Sync) vs outbound (Agent Ready) patterns
- [[ai-developer-tools]] — AI Developer Tools for Payments: MCP servers, agent skills, LLM SDKs, AI coding platforms — Stripe vs PayPal comparison
- [[payment-reconciliation-reporting]] — Payment Reconciliation & Reporting: Transaction Search API, Activity Download Report (87 fields), T-codes, settlement reports, 3-hour latency

## Concepts & protocols (generic / cross-network)

- [[acp]] — Agentic Commerce Protocol: open standard (Stripe+OpenAI+Meta), 5 capabilities, delegate payment/authentication, OpenAPI spec 2026-04-17
- [[ucp]] — Universal Commerce Protocol: open standard for agentic commerce interop, checkout/identity/order/payment token exchange, Stripe + OpenAI ACP context
- [[cit-mit]] — CIT/MIT: customer vs merchant-initiated transactions, MIT compliance requirements, card brand change rule
- [[cartes-bancaires]] — Cartes Bancaires: France local network, >95% co-badged, EEA choice requirement, 0 EUR dispute fee, cannot contest
- [[eftpos-australia]] — eftpos Australia: local debit network, LCR, no manual capture, hold→Visa/MC, disclosure requirement
- [[co-badged-cards]] — Co-badged cards compliance: EU 2015/751, EEA Cartes Bancaires + DE Girocard, 3 requirements, network selector integration
