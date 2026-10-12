---
title: "Adyen Build Your Integration"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/build-your-integration"
raw_files:
  - "adyen/docs/online-payments/build-your-integration/2026-09-15.md"
tags: [adyen, online-payments, checkout-api, integration]
---

# Adyen Build Your Integration

## Overview

This Adyen online-payments guide is a server-side flow selection map for integrations that pair Adyen client-side libraries with Checkout API requests. It recommends Sessions as the default for most online-payment integrations and contrasts it with Sessions plus additional methods and the Advanced flow. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Choose the server-side implementation before integrating a client-side library, based on the technical requirements and use cases the integration must support.
- In the Sessions flow, the merchant server makes one `/sessions` request and Adyen sends payment data to the client-side application. The guide describes this as the recommended default for most integrations.
- In the Advanced flow, the merchant server makes `/paymentMethods`, `/payments`, and `/payments/details` requests, and Adyen sends payment data to the merchant server. The guide says this flow supports more use cases.
- Sessions with additional methods adds server requests to `/payments` and `/payments/details`, allowing responses on the merchant server. The comparison table counts two or three server endpoint requests for this variant.
- The captured comparison assigns redirect and additional-action handling only to the client for basic Sessions, but to both client and server for Sessions with additional methods and Advanced. In the supported-use-case table, changing payment-method order for one transaction and inserting a separate terms-agreement page are marked only for Advanced.
- This is a dated architecture-selection guide, not full implementation documentation or proof of current merchant eligibility, payment-method availability, successful payment execution, authorization, capture, or settlement. Its API Explorer links use `latest`, so the snapshot does not establish a fixed Checkout API version.
- This source is Adyen Docs website evidence. Its client-side-library link to GitHub is navigation only, not reviewed GitHub evidence.

## Detail locators

- Default recommendation and client/server framing: `Build your integration`, line 19.
- Flow-selection condition: `Choose your server-side implementation`, line 23.
- One-request Sessions data path: `Sessions flow: a single API request`, line 27.
- Three-request Advanced data path: `Advanced flow: three API requests`, line 32.
- Hybrid server-response path: `Sessions flow with additional methods`, line 39.
- Use-case and responsibility matrices: `Supported use cases`, lines 42–54, and `Integration comparison`, lines 56–63.
- Web, mobile, and cross-platform implementation routes: `Get started`, lines 65–75.

## Related

- [[adyen]] — provider page.
- [[adyen-online-payments]] — provider-level online-payments architecture and lifecycle route.

## Raw Sources

- [[raw/adyen/docs/online-payments/build-your-integration/2026-09-15|Adyen Build your integration (2026-09-15)]]
