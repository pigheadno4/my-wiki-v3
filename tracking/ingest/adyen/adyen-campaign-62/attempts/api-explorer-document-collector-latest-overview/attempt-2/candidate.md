---
title: "Adyen Document Collector API v1 overview"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Document-Collector/latest/overview"
raw_files:
  - "adyen/api-explorer/Document-Collector/latest/overview/2026-09-15.md"
tags: [adyen, document-collector, cross-border, invoices, api-explorer]
---

## Overview

The captured Document Collector API v1 overview says merchants can upload supporting documents for payment processing. Its stated current scope is PDF cross-border invoices for INR transactions under Reserve Bank of India cross-border payment guidelines. This is a document-upload API overview, not an invoice review, payment, or settlement result. [[adyen]] [[adyen-payments]]

## Key takeaways

- Adyen contact supplies an API credential and API key. The page shows `X-API-Key` authentication and basic authentication with username and password as alternatives. Its curl fragments show `multipart/form-data`; detailed upload body and response fields belong to the operation page, not this overview. See raw lines 9–23.
- Version suffixes use `vXX`; the captured example and server list use `/v1`. Test base URL is `https://document-collector-test.adyen.com/v1`, and live base URL is `https://document-collector-live.adyen.com/v1`. For live, the page says Adyen contact provides the live credential and describes username/password requests to the live URL. See raw lines 25–43.
- The only endpoint listed here is `POST /crossBorderInvoices`, summarized as `Upload a document`. The overview gives no required request properties, file-size limit, response contract, upload acceptance criteria, asynchronous review outcome, timing, or payment-state transition. See raw lines 45–50.

## Related

- [[adyen-payments]] — provider payment-processing context.
- [[adyen-api-access]] — general credential concepts; this source's specific authentication modes are above.

## Related raw API references

- [[raw/adyen/api-explorer/Document-Collector/latest/post/crossBorderInvoices/2026-09-15|POST /crossBorderInvoices]] — separate operation page for request and response details.

## Raw Sources

- [[raw/adyen/api-explorer/Document-Collector/latest/overview/2026-09-15|Document Collector API v1 overview]]
