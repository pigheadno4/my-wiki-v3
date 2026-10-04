---
title: "Braintree Orchestration Flutterwave Integration Guide"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/orchestration/flutterwave"
raw_files:
  - "braintree/docs/guides/orchestration/flutterwave-2026-09-16.md"
tags: [braintree, orchestration, flutterwave, card-payments, reconciliation]
---

## Overview

This collected Braintree-hosted guide describes a Flutterwave connector that lets merchants use an existing Braintree integration for card-not-present transactions through the PayPal Orchestration platform. It characterizes the destination interface as a non-public card-direct API, distinct from Flutterwave's public-facing products. The page is Braintree integration evidence, not independent Flutterwave authority, proof of current merchant enablement, or evidence that any example transaction executed, settled, or funded.

## Key takeaways

- Setup spans both sides: the page requires a Braintree merchant account configured for the connector and Flutterwave-provisioned access to the card-direct API. It says Flutterwave supplies separate sandbox and production usernames and passwords and directs the merchant to share them securely with a Braintree AM or TAM. No credential value belongs in this wiki.
- The guide directs merchants to perform all transaction operations through Braintree because direct Flutterwave operations can create discrepancies or synchronization errors. This Orchestration transaction route is distinct from [[braintree-forward-api]], which is the Braintree Extend request-construction and payment-data-forwarding route; forwarding-only rules are not imported here.
- The feature tables document dual-step charge, standalone authorization, full capture, void, and full or partial refund routes, while marking single-step charge, partial capture, capture above the authorized amount, and incremental authorization unsupported. Authorization and capture carry a seven-day limit in this snapshot. Exact operation support, field mappings, status mappings, and currencies remain in the raw locators below.
- A charge is described as authorization followed immediately by capture. For retryable capture or refund gateway errors, the guide maps the transaction to `SETTLING` and says Braintree polls for the outcome. It warns not to fulfill before `SETTLED`, not to create a duplicate capture or refund retry loop for `SETTLING`, and to Find or Search after timeout or uncertainty before a second create. These status statements do not establish bank funding.
- The page says recurring or vaulted-card transactions may omit CVV and send an empty string, which some issuers might decline. It also says the connector does not support 3DS data pass-through, network tokens, or AVS response fields. Its sandbox test-card remapping and expiry-controlled outcomes are test instructions, not proof of live availability or execution.
- The connector description says raw card numbers can be submitted without a preceding tokenization step, while the transaction-field table labels several payment-method fields as provided "During tokenization." The snapshot does not explain that wording relationship, so no additional tokenization requirement or exemption is inferred.

## Detail locators

- Connector identity, merchant audience, card-not-present purpose, and non-public card-direct API distinction: `# Flutterwave Integration Guide`, lines 14-20.
- Supported and unsupported transaction lifecycle, refund, instrument, verification, fraud-signal, and 3DS/AVS capabilities: `## Features`, lines 21-108.
- Braintree merchant-account configuration, Flutterwave provisioning, environment-specific credentials, secure-sharing route, and support contact: `## Before you begin`, lines 111-119.
- Braintree-only operation warning and transaction-creation fields, including the tokenization-label tension: `## Transactions` and `### Transaction creation`, lines 120-145.
- Operation-specific Braintree-to-Flutterwave field mappings for authorization, charge, verification, capture, refund, and void: `### Fields that Braintree passes to Flutterwave`, lines 148-199.
- Optional customer creation, vaulting, recurring/vaulted-card CVV qualification, and empty-string behavior: `### Customer creation` through `### CVV handling`, lines 202-214.
- Supported transaction-operation matrix: `### Supported transaction operations`, lines 217-233.
- Result-to-status mapping, retryable-error reconciliation, fulfillment warning, and dual-step charge sequence: `## Transaction status mapping`, lines 236-286.
- Duplicate-retry avoidance, timeout uncertainty lookup, and MAID-qualified failed-authorization retry configuration: `## Retries`, lines 289-295.
- Acquirer and CVV response-code mappings: `## Response codes`, lines 298-387.
- Sandbox remapping and expiration-date-controlled test outcomes: `## Testing`, lines 390-433.
- Duplicate-reference handling, recurring/vaulted CVV behavior, and lack of 3DS, network-token, and AVS support: `## Known limitations`, lines 436-443.
- Snapshot currency list: `## Supported currencies`, lines 446-448.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Existing server-operation context: [[braintree-server-sdk]]
- Existing currency context: [[braintree-currencies]]
- Distinct request-forwarding product: [[braintree-forward-api]]

## Related raw API references

- [[raw/braintree/docs/guides/transactions/node-2026-09-16|Braintree Node.js transactions guide]] - unread navigation-only destination for general transaction operations; not used as factual evidence here
- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Braintree Node.js transaction sale reference]] - unread navigation-only destination for authorization and charge; not used as factual evidence here
- [[raw/braintree/docs/reference/request/transaction/submit-for-settlement/node-2026-09-16|Braintree Node.js submit-for-settlement reference]] - unread navigation-only destination for capture; not used as factual evidence here
- [[raw/braintree/docs/reference/request/transaction/refund/node-2026-09-16|Braintree Node.js refund reference]] - unread navigation-only destination for refunds; not used as factual evidence here
- [[raw/braintree/docs/reference/request/transaction/void/node-2026-09-16|Braintree Node.js void reference]] - unread navigation-only destination for voids; not used as factual evidence here
- [[raw/braintree/docs/reference/response/transaction/node-2026-09-16|Braintree Node.js transaction response reference]] - unread navigation-only destination for response fields and statuses; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/guides/orchestration/flutterwave-2026-09-16|Braintree Flutterwave Integration Guide]] - fully read collected guide covering connector identity, setup, transaction operations, field and status mappings, reconciliation, testing, limitations, and currencies
