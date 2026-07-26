---
title: "Adyen"
type: company
tags: [adyen, payments, checkout, web-sdk]
source_count: 1
---

## Overview

Adyen is represented in this wiki by the independently versioned Adyen Web checkout SDK. The first retained source covers browser Drop-in and Components, Sessions and advanced checkout flows, card entry, 3D Secure 2 actions, stored payment methods, accessibility, analytics, and client risk collection.

## Web checkout surface

- Drop-in provides an all-in-one payment-method list and action flow.
- Components provide individually mounted payment-method experiences.
- Sessions delegate setup and payment orchestration to Adyen's Session endpoints.
- The advanced flow delegates `/payments` and `/payments/details` calls to merchant callbacks.
- Backend payment-method responses and merchant configuration determine what the SDK can present.

## Versioned implementation knowledge

The retained `@adyen/adyen-web@6.41.0` baseline records funding-source-aware cards, Click to Pay and installment conditions, 3DS2 URL and message-origin checks, stored-method filtering, screen-reader behavior, and a PayPal Fastlane adapter.

Repository evidence is not current product eligibility guidance. In particular, the PayPal dependency establishes an adapter boundary; delegated PayPal runtime behavior belongs to the separate PayPal repository history.

## Knowledge status

- Ingested cumulative GitHub repository sources: 1
- Ingested package releases: 1
- Latest retained package release: `@adyen/adyen-web@6.41.0`
- Latest retained exact SHA: `b19eec7054340a1526c87d450fd7dfff75794ed9`

## Sources

- [[source-github-adyen-web]] — cumulative Adyen Web implementation baseline
- [[changelog-github-adyen-web]] — package-qualified release ledger

## Related

- [[adyen-index]] — Adyen catalog and operations links
- [[adyen-log]] — collection and ingest history
- [[co-badged-cards]] — cross-provider network-choice concept
