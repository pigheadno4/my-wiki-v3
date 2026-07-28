---
title: "Braintree"
type: company
tags: [braintree, payments, checkout, javascript-sdk]
source_count: 1
---

## Overview

Braintree is represented in this wiki by the independently versioned Braintree Web browser SDK. The first retained source covers modular card, wallet, local-payment, bank, fraud-data, and payment-recommendation components that produce or support Braintree payment-method nonces for server processing.

## Web SDK Surface

- Hosted Fields provides merchant-styled, Braintree-hosted card inputs.
- 3D Secure verifies card nonces and reports liability-shift outcomes.
- PayPal Checkout v6, Venmo, Fastlane, Apple Pay, and Google Pay connect external wallet experiences to Braintree processing.
- Local Payment, SEPA, US bank account, and Instant Verification cover additional payment and bank-verification paths.
- Data Collector, Payment Ready, and preferred-method signals support risk and presentation decisions but do not themselves prove eligibility.

## Versioned Implementation Knowledge

The retained `braintree-web@3.143.0` baseline records 23 exported components at exact SHA `bae582d791026c143abb91c3bdcada92b8c060f6`. The exact patch updates card-type data and changes the Fastlane loader dependency; broader source findings are cumulative behavior present at that version.

Repository evidence is not current enablement guidance. PayPal and Fastlane modules also have delegated-runtime boundaries, and legacy source modules should not be treated as recommendations for new integrations.

## Knowledge Status

- Ingested cumulative GitHub repository sources: 1
- Ingested package releases: 1
- Latest retained package release: `braintree-web@3.143.0`
- Latest retained exact SHA: `bae582d791026c143abb91c3bdcada92b8c060f6`

## Sources

- [[source-github-braintree-web]] — cumulative Braintree Web implementation baseline
- [[changelog-github-braintree-web]] — package-qualified release ledger

## Related

- [[braintree-index]] — Braintree catalog and operations links
- [[braintree-log]] — collection and ingest history
- [[braintree-web-sdk]] — browser SDK concept
- [[paypal-braintree-integration]] — Braintree PayPal v6 processing boundary
