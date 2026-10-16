---
title: "Payment processing in NetSuite"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/netsuite/payment-processing-in-netsuite"
raw_files:
  - "adyen/docs/plugins/netsuite/payment-processing-in-netsuite/2026-09-15.md"
tags: [adyen, netsuite, authorisation, capture, refunds]
---

## Overview

Adyen's NetSuite payment-processing guide (page metadata last modified 2023-08-01; captured 2026-09-15) describes the SuitePayment transaction paths for authorisation, capture, direct cash sales, and refunds, plus plug-in logs and a result-label mapping. It is a workflow description, not evidence that an individual NetSuite order, capture, refund, settlement, or bank receipt succeeded. See [[adyen-netsuite]] for the integration scope.

## Key takeaways

- A **Sales Order** represents purchase intent and can request authorisation before shipment, separately from capture. In NetSuite Customer Center, an available active payment processing profile may be selected automatically; **Get Authorisation** triggers the automated request. **Credit Card Approved** instead signals authorisation received outside automated communication, with an Adyen PSP reference entered manually in **P/N Ref.** and optional **Auth. Code**. The guide says a successful authorisation is saved on the order and a pre-capture authorisation can be voided; a checkbox alone is not proof of a provider authorisation (raw lines 16–31).
- For a previously authorised Sales Order, shipment confirmation drives capture using the original reference. If the order was manually authorised, the Adyen **P/N Ref.** must be entered before shipment confirmation. NetSuite requests secondary confirmation on a capture request, after which Cash Sale details become available. Adyen creates references for stages, while the Adyen account transaction line references the original authorisation P/N Ref.; later references are available in NetSuite. The request and NetSuite record are distinct from a confirmed financial settlement (raw lines 33–42).
- A direct **Cash Sale** needs no preceding Sales Order. Unless the card was manually pre-approved, it initiates an authorise-and-capture request. For a partial capture or imported authorisation, the PSP reference may need manual entry if not shown automatically (raw lines 44–54).
- **Customer Refund** and **Cash Refund from a Cash Sale** initiate referenced refunds. Both require a **P/N Reference** against the original Auth/Sale; unreferenced refunds and credits in this SuitePayment bundle are not supported. The procedure asks to match request data and save, which does not prove the refund completed (raw lines 56–71).
- Plug-in execution logs are available in NetSuite Customer Center and requested for Support. The Adyen-to-NetSuite result mapping includes Authorised → ACCEPT, Received/Pending/PENDING → CONFIRMATION_PENDING, Refused → GENERAL_REJECT and Cancelled → PAYMENT_TERMINATED; unlisted values fall to GENERAL_REJECT or FATAL_ERROR. These are mapped labels, not a substitute for checking the underlying payment stage or outcome (raw lines 73–125).

## Detail locators

- Sales Order authorisation, manual approval fields and void: raw lines 16–31.
- Shipment-linked capture, references and Cash Sale: raw lines 33–54.
- Refund transaction types and original-reference rule: raw lines 56–71.
- Plug-in execution-log route: raw lines 73–84.
- Full Adyen/NetSuite result mapping and fallback labels: raw lines 86–125.

## Related

- [[adyen-netsuite]] — NetSuite integration concept and source route.
- [[adyen]] — Adyen provider page.

## Raw Sources

- [[raw/adyen/docs/plugins/netsuite/payment-processing-in-netsuite/2026-09-15|NetSuite payment processing, captured 2026-09-15]]
