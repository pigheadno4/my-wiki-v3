---
title: "Adyen Payment API v68 overview"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payment/latest/overview"
raw_files:
  - "adyen/api-explorer/Payment/latest/overview/2026-09-15.md"
tags: [adyen, payment-api, classic, api]
---

## Overview

Captured API Explorer overview for **Adyen Payment API v68**, the inactive Classic Payment API. It lists operations to initiate, settle and modify payments, including authorization, 3DS completion, capture, cancellation and refund. This is a versioned endpoint directory, not the Checkout API or a contract for any listed endpoint. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Adyen marks this API **inactive**. The page directs new integrations to the Checkout API and existing Payment API integrations to contact Adyen and migrate to Checkout. Do not transfer Payment API v68 endpoint schemas or behavior to similarly named Checkout API v72 routes.
- Authentication requires an API credential. The overview illustrates either an `X-API-Key` header or basic authentication with username and password. Version suffixes use `vXX`; the captured test server is `https://pal-test.adyen.com/pal/servlet/Payment/v68`.
- Live access calls for a credential from the live Customer Area and a company-specific `{PREFIX}-pal-live.adyenpayments.com` host; the prefix is obtained under Developers → API URLs → Prefix. This overview is setup guidance, not proof of live credentials or payment execution.
- The endpoint table lists `POST /authorise`, `/authorise3d`, `/authorise3ds2`, `/getAuthenticationResult`, `/retrieve3ds2Result`, `/capture`, `/cancel`, `/technicalCancel`, `/cancelOrRefund`, `/refund`, `/adjustAuthorisation`, `/donate` and `/voidPendingRefund`. Their request/response fields, lifecycle conditions, errors and asynchronous outcome semantics are not specified here; follow each endpoint's own raw reference.
- The canonical URL says `latest`, but this captured content identifies v68. It does not establish today's latest version.

## Detail locators

- Raw lines 5–16: v68 identity, inactive status and migration direction.
- Raw lines 18–34: API credential and two authentication examples.
- Raw lines 36–55: version suffix, test and live URL examples, company prefix and server.
- Raw lines 57–74: full endpoint navigation table.

## Related

- [[adyen-online-payments]] — provider online-payments concept; Classic and Checkout sources remain separate.

## Raw Sources

- [[raw/adyen/api-explorer/Payment/latest/overview/2026-09-15|Captured Payment API v68 overview]]