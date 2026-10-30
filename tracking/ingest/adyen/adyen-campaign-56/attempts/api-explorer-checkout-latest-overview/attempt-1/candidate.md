---
title: "Adyen Checkout API v72 overview"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/overview"
raw_files:
  - "adyen/api-explorer/Checkout/latest/overview/2026-09-14.md"
tags: [adyen, checkout-api, online-payments, api-reference]
---

## Overview

This 2026-09-14 capture of Adyen's Checkout API **v72** overview describes the API for initiating and authorising online card, wallet, and local-method payments. It is an API-level reference and endpoint directory, linked to [[adyen]] and [[adyen-online-payments]]. The URL contains `latest`, but the captured content and example paths say **v72**; this snapshot does not establish a later current version.

## Key takeaways

- Each Checkout API request uses an API key in the `X-API-Key` header (raw lines 11–18). The version suffix is `vXX`; the captured test example and Servers entry use `https://checkout-test.adyen.com/v72` (lines 20–26, 72–73).
- For live access, the page specifies a key from the live Customer Area and a company-specific `{PREFIX}` in the live endpoint URL; it points to Customer Area **Developers > API URLs > Prefix** and a go-live checklist (lines 56–66). These are prerequisites stated by the page, not evidence of an account's live eligibility or executed transaction.
- The General endpoint table routes to payment sessions, payment-method discovery, payments and details, stored payment methods, orders and partial-payment support, payment modifications, payment links, Apple Pay sessions, PayPal order updates, donations, and other operations (lines 75–108). Method and path labels are navigation; this overview gives no endpoint-specific request or response schema, required fields, eligibility, or outcome guarantee.

## Detail locators

- API purpose, authentication, versioning, libraries, Postman, live setup: raw lines 5–70.
- Test server and complete method/path/summary inventory: raw lines 72–108.
- For behavior or schema, read the corresponding endpoint reference and relevant integration guide; an endpoint listed here alone does not establish its contract.

## Related

- [[adyen-online-payments]] — online integration context and provider guide routes.
- [[source-adyen-docs-online-payments-build-your-integration-sessions-flow]] — separate Sessions integration guide.
- [[source-adyen-docs-online-payments-build-your-integration-advanced-flow]] — separate Advanced integration guide.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/overview/2026-09-14|Checkout API v72 overview, captured 2026-09-14]]
