---
title: "Braintree Hosted Fields Start"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/start/hosted-fields"
raw_files:
  - "braintree/docs/start/hosted-fields-2026-09-16.md"
tags: [braintree, javascript-sdk, hosted-fields, credit-cards, pci]
---

## Overview

This unversioned Braintree start page introduces Hosted Fields as a JavaScript SDK integration for merchant-styled card entry on desktop and mobile websites. It describes Hosted Fields iframe inputs, direct client-to-Braintree transmission of collected card data, and a one-time-use payment-method nonce used in place of raw payment information.

## Key takeaways

- Hosted Fields renders custom iframe inputs for certain sensitive payment fields within the merchant checkout page while leaving the merchant in control of the surrounding checkout presentation. The page separately points to card-specific form events for updating the merchant UI.
- The collected card data is sent directly from the client to Braintree, so the page says the customer's raw payment information does not touch the merchant server. Braintree associates the data with a secure, one-time-use payment-method nonce used instead.
- The page says Hosted Fields can be used to remain eligible for SAQ A PCI compliance and helps minimize PCI scope. This is eligibility and scope guidance in a fetched documentation snapshot, not proof of a merchant's compliance status.
- The integration route pairs a Braintree server SDK with a JavaScript web client and then adds Hosted Fields. The page links a JavaScript v3 client reference, but does not identify the version of the JavaScript SDK to which the rest of the start-page prose applies.
- Field-validity events and nonce creation remain distinct from transaction processing: this page does not establish card acceptance, authorization, settlement, merchant enablement, browser rendering, or a successful payment. It identifies Drop-in UI separately as a pre-formatted mobile-and-web form option.

## Detail locators

- Hosted Fields purpose and merchant control of website checkout styling: `# Hosted Fields`, line 16.
- Custom iframe inputs for sensitive payment fields: `### Inputs for credit card data`, line 21.
- SAQ A eligibility, brand styling and card-specific UI events: lines 24-36.
- Direct client-to-Braintree card-data path, raw server-data boundary and one-time-use payment-method nonce: `## Hosted Fields and your server`, lines 39-45.
- Server SDK, JavaScript web-client and Hosted Fields integration sequence: `## Integrate Hosted Fields` > `##### Step-by-step`, lines 48-57.
- JavaScript v3 reference and separate pre-formatted Drop-in UI route: lines 59-61.

## Evidence boundary

This is a fetched documentation snapshot whose embedded metadata reports an update time of 2025-04-01 and whose capture is dated 2026-09-16. It is not live SDK documentation, rendered UI evidence, current browser or SDK support, account eligibility, PCI validation, tokenization proof, or payment-execution evidence. Linked guides and references remain separate evidence.

## Related

- Company: [[braintree]]
- Concept: [[braintree-web-sdk]]
- Related source: [[source-braintree-hosted-fields-faq-javascript-v3]]
- Related source: [[source-braintree-hosted-fields-styling-javascript-v3]]

## Related raw API references

- Hosted Fields examples, setup-and-integration guide and JavaScript v3 client reference linked by the captured page were not read for this entry.

## Raw Sources

- [[raw/braintree/docs/start/hosted-fields-2026-09-16|Braintree Hosted Fields start page]] - complete captured start page for the Hosted Fields role, client/server data boundary, nonce substitution and integration routes
