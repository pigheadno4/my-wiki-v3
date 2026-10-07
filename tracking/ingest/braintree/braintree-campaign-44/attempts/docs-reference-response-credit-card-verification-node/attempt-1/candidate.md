---
title: "Braintree Credit Card Verification Response Reference (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/response/credit-card-verification/node"
raw_files:
  - "braintree/docs/reference/response/credit-card-verification/node-2026-09-16.md"
tags: [braintree, node-js, credit-card-verification, response-objects, processor-responses]
---

## Overview

This collected Braintree Node.js website page is a response reference for Credit Card Verification data. It orients readers to gateway-returned product-ID meaning and to network response diagnostics that may appear on some transaction and verification objects; it does not document how to submit a verification request or perform a charge.

## Key takeaways

- The page says the gateway returns product IDs for credit and debit card payment methods. A product ID is generally one to three characters and indicates the specific credit product issued to the customer, but this captured snapshot contains no product-ID inventory after that description, so no code-to-product mapping can be recovered from it.
- Some transaction and verification objects can include a network response code and text in addition to processor response data. When present, these are raw card-network responses that can add detail about why a request was approved or declined, but the page explicitly makes them supplemental and names the processor response code as the source of truth.
- The headings distinguish values returned through an error result object from values returned directly or through a successful result object, yet their response-object and request lists are blank in this capture. The page therefore does not identify the originating request operations or establish success, approval, charge, or lifecycle semantics from those headings alone.
- Results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products policy. That external policy is not included in the pinned raw, so its effect is not interpreted here.

## Detail locators

- Results-limitation notice: `# Credit Card Verification`, lines 17-18.
- Blank response-object and request lists under the error-result and direct-or-successful-result headings: lines 21-40.
- Product-ID purpose and general length qualification, followed by the absent inventory: `## Product ID codes`, lines 41-46.
- Network-response presence, diagnostic purpose, raw-network origin, processor-response authority and card-network navigation: `## Network response codes`, lines 47-59.

## Evidence boundaries

> [!warning] This is a 2026-09-16 snapshot of an unversioned Node.js website route, not evidence for an exact Node SDK package or version. It documents returned verification-oriented metadata rather than charge behavior or request construction, and it establishes neither product or merchant enablement in any environment, current availability, nor the status or outcome of an individual verification or payment.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Broader transaction response route: [[source-braintree-transaction-response-node]]

## Raw Sources

- [[raw/braintree/docs/reference/response/credit-card-verification/node-2026-09-16|Braintree Credit Card Verification response reference - Node.js]] - complete collected page containing the policy notice, blank containing-object/request lists, product-ID description and network-response authority boundary
