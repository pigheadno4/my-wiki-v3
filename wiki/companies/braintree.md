---
title: "Braintree"
type: company
tags: [braintree, payments, checkout, javascript-sdk]
source_count: 2
---

## Overview

Braintree is represented in this wiki by two independently versioned browser repositories: the modular Braintree Web SDK and the prebuilt Braintree Web Drop-in UI. Both produce or support Braintree payment-method nonces for server processing, but their package versions and evidence histories must remain separate.

## Web SDK Surface

- Hosted Fields provides merchant-styled, Braintree-hosted card inputs.
- 3D Secure verifies card nonces and reports liability-shift outcomes.
- PayPal Checkout v6, Venmo, Fastlane, Apple Pay, and Google Pay connect external wallet experiences to Braintree processing.
- Local Payment, SEPA, US bank account, and Instant Verification cover additional payment and bank-verification paths.
- Data Collector, Payment Ready, and preferred-method signals support risk and presentation decisions but do not themselves prove eligibility.

## Drop-in Surface

`braintree-web-drop-in@1.47.0` provides an opinionated UI for cards, PayPal, PayPal Credit, Venmo, Apple Pay, and Google Pay, with vaulted-method display, optional Data Collector output, and 3D Secure verification. It pins `braintree-web@3.123.2`, not the separately retained `3.144.0` modular SDK.

The repository schedules Drop-in deprecation for 2026-09-01 and unsupported status for 2027-09-01 and directs merchants to migrate to the modular Braintree SDK. Its notice says processing will be supported for one year after deprecation, while processing on unsupported SDKs may be suspended at any time. Current support status should be rechecked for time-sensitive guidance.

## Versioned Implementation Knowledge

The retained history begins with `braintree-web@3.143.0` and currently reaches `3.144.0` at exact SHA `41460fba05c1ea1222e795b36a10765a6699b8e7`. The newer release adds PayPal View/Edit Funding Instrument, expands PayPal Checkout v6 session options, and prevents failed incognito detection from aborting Venmo creation while preserving the 23-component architecture.

Repository evidence is not current enablement guidance. PayPal and Fastlane modules also have delegated-runtime boundaries, and legacy source modules should not be treated as recommendations for new integrations.

## Knowledge Status

- Ingested cumulative GitHub repository sources: 2
- Ingested package releases: 3
- Latest retained Braintree Web release: `braintree-web@3.144.0` at `41460fba05c1ea1222e795b36a10765a6699b8e7`
- Latest retained Drop-in release: `braintree-web-drop-in@1.47.0` at `ec1c7c533c2e878545f2b25505c56b7e22dc1c17`

## Sources

- [[source-github-braintree-web]] — cumulative Braintree Web implementation baseline
- [[changelog-github-braintree-web]] — package-qualified release ledger
- [[source-github-braintree-web-drop-in]] - cumulative Drop-in implementation baseline
- [[changelog-github-braintree-web-drop-in]] - package-qualified Drop-in release ledger

## Related

- [[braintree-index]] — Braintree catalog and operations links
- [[braintree-log]] — collection and ingest history
- [[braintree-web-sdk]] — browser SDK concept
- [[braintree-web-drop-in]] - prebuilt checkout UI and migration boundary
- [[paypal-braintree-integration]] — Braintree PayPal v6 processing boundary
