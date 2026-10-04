---
title: "Braintree Forward API Worldpay Destination Guide"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/forward-api/worldpay"
raw_files:
  - "braintree/docs/guides/extend/forward-api/worldpay-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, worldpay, request-override]
---

## Overview

This collected, unversioned Braintree developer guide identifies `worldpay_shared` as the Forward API configuration for interacting with Worldpay APIs and describes how to add optional request fields through an override body. It is a Braintree-hosted destination guide, not Worldpay-owned API authority, evidence of current Worldpay capability or merchant access, or proof that a forwarded request or payment was accepted or executed. See [[braintree]] and [[braintree-forward-api]].

## Key takeaways

- The page says production Forward API use is subject to eligibility and directs readers to an Account Manager or Business Development.
- For additional non-mandatory fields, it tells the caller to populate the override attribute with a `body` whose value is a JSON or XML string containing the optional attributes and values.
- Data sent through this override route appears in Braintree's logs; the page says not to send sensitive data or customer PII this way.

## Detail locators

- Production eligibility and contact route: `**AVAILABILITY**`, raw lines 16-17.
- `worldpay_shared` configuration and optional-field override-body description: raw line 19.
- Logging and sensitive-data/PII caution: `**NOTE**`, raw lines 20-21.
- Examples navigation: raw line 23.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-forward-api]]

## Related raw API references

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Braintree Forward API overview]] - linked navigation-only route for the eligibility notice; not read as factual evidence for this source
- [[raw/braintree/docs/reference/forward-api/forward-2026-09-16|Braintree Forward API forward reference]] - linked navigation-only route for override details; not read as factual evidence for this source
- [[raw/braintree/docs/guides/extend/forward-api/examples-2026-09-16|Braintree Forward API examples]] - linked next-page navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/extend/forward-api/worldpay-2026-09-16|Braintree Forward API Worldpay destination guide]] - complete collected page covering production eligibility, the `worldpay_shared` configuration, optional override-body fields, and the logging/PII caution
