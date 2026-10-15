---
title: "Adyen click and collect: assistant pickup"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/retail-use-cases/click-and-collect/c-and-c-assistant-pickup"
raw_files:
  - "adyen/docs/unified-commerce/retail-use-cases/click-and-collect/c-and-c-assistant-pickup/2026-09-15.md"
tags: [adyen, unified-commerce, click-and-collect, assistant-pickup, card-recognition, manual-capture]
---

## Overview

Adyen's assistant-pickup click-and-collect guide describes a shopper who orders online and authorizes the payment, while another person collects the goods in store. The merchant uses a zero-amount Pay by Link transaction to record the assistant's card alias and/or Payment Account Reference (PAR), then checks the same card through terminal card acquisition at pickup. Only after this recognition step does the guide call for manual capture of the **shopper's online authorization**. See [[adyen]], [[adyen-unified-commerce]] and [[adyen-card-recognition]].

## Key takeaways

- This described flow needs both Adyen ecommerce and POS integrations and a consolidated order/inventory or ERP system, or an orchestration layer connecting systems and consuming webhooks. The merchant must decide whether the online order captured in store counts as an ecommerce or in-store sale; the guide does not make that attribution decision.
- The shopper's online Checkout API payment is authorized with **manual capture**. Its `AUTHORISATION` webhook provides the payment `pspReference` and amount to retain for later capture. An authorized result leads the merchant to collect the assistant's contact details and send a zero-amount payment link. The assistant's link takes no payment; it collects card alias and/or PAR, which the merchant saves under the assistant on the shopper's order/profile after the link's own `AUTHORISATION` webhook. The link webhook and online-purchase webhook refer to different transactions.
- The zero-amount link needs Pay by Link settings, including terms and conditions, and is created with Checkout `POST /paymentLinks`. This use-case guide says to restrict `allowedPaymentMethods` to `scheme` because subsequent terminal card acquisition works with cards and NFC wallets. It asks the merchant to explain that the assistant's card will not be charged and must be available at pickup; this is guidance, while the example text is illustrative.
- At pickup, a Terminal API `CardAcquisitionRequest` obtains PAR (if present) and/or alias. The merchant matches those identifiers against its saved assistant/order record, then ends acquisition with `EnableServiceRequest`. Card acquisition is a non-financial recognition step, not a second charge or proof of the assistant's civil identity. The guide requires enabling shopper-identifying data in API responses and webhooks. It suggests explaining how the assistant's information will be used; it does not specify a consent implementation.
- The capture request is Checkout API `POST /payments/{paymentPspReference}/captures` for the amount due, using the **online purchase** PSP reference from its `AUTHORISATION` webhook. The guide explicitly says not to use the link's `AUTHORISATION` webhook. Capture belongs to the shopper's authorization; receiving the goods is a separate merchant fulfillment event. The examples do not prove a successful live capture or settlement.

## Detail locators

- Lines 19–35: two participants, secure card-identifier intent, pickup-time capture, integration and merchant-system prerequisites.
- `## Shopper journey` and `## Considerations` (lines 38–101): contact/link/card sequence, sale attribution, required manual capture, identifier comparison and enabled response/webhook data.
- `#### Online purchase` (lines 143–218): Sessions/Advanced example requests, authorized-result branch, assistant details, and online payment webhook reference/amount; example API version and values are illustrative.
- `#### Payment link to assistant` (lines 220–275): Pay by Link setup, zero-amount request, card-method restriction, communication guidance, and the link webhook's separate assistant identifier record.
- `#### In-store pickup` (lines 277–420): terminal card acquisition, PAR/alias response (including optional Base64 encoding), end-acquisition request, and Checkout manual capture using the online purchase reference.

## Related

- [[adyen-unified-commerce]] — provider cross-channel concept and reciprocal source route.
- [[adyen-card-recognition]] — card acquisition and recognition boundary.
- [[source-adyen-docs-unified-commerce-pay-by-link]] — hosted link overview and first-live-link terms prerequisite.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/retail-use-cases/click-and-collect/c-and-c-assistant-pickup/2026-09-15|Assistant pickup guide, captured 2026-09-15]]
