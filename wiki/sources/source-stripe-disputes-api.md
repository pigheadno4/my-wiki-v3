---
title: "Stripe — Use the API to Respond to Disputes"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/disputes/api"
raw_files:
  - "stripe-disputes-api-2026-11-07.md"
  - "stripe-disputes-api-2026.md"
tags: [stripe, disputes, chargebacks, api, evidence, file-upload, webhooks]
---

## Overview

Stripe's May 9 and November 7, 2026 guides describe API-based dispute retrieval, evidence updates, listing by a PaymentIntent or Charge, and webhook events. The November capture adds `charge.dispute.created` and says a Dispute exposes a Charge reference and a **nullable** PaymentIntent reference, but no direct invoice or subscription reference. For an associated subscription, the guide routes to a separate [subscription webhook procedure](https://docs.stripe.com/billing/subscriptions/webhooks.md#refund-events); it does not define that full procedure or prove that every dispute concerns a subscription. See [[disputes]].

## Core API operations

- **Retrieve a Dispute:** `GET /v1/disputes/{id}`; the May Node example uses `stripe.disputes.retrieve(id)`. The illustrative response includes evidence and `evidence_details.due_by` and `submission_count`. Its ellipsis means the displayed object is not a complete parseable response or a guarantee of a particular dispute state.
- **Update with evidence:** The guide updates a Dispute by ID with structured `evidence` fields. The May Node example uses `stripe.disputes.update(id, { evidence: {...} })`; the November curl example sends text and a file ID to `POST /v1/disputes/{id}`. Supplying fields through this operation does not itself prove evidence acceptance, final submission state, a won dispute, or returned funds.
- **List and select:** `GET /v1/disputes` can filter by `payment_intent` or `charge`; May shows corresponding Node `stripe.disputes.list(...)` examples and November shows curl. One payment can have multiple disputes, each with a unique Dispute ID. Use the returned Dispute ID to retrieve or update the intended case. A payment filter is not a subscription lookup.

The move from Node to curl illustrations changes the displayed example language, not an established SDK availability or REST-contract boundary. This guide does not document dispute acceptance, cancellation, issuer adjudication, or the final payment/subscription outcome.

## Evidence types and limits

- Text evidence fields take strings; the **combined character count** across text-based evidence submissions is limited to **150,000**. File-based fields take a `file_upload` object ID. The May update example includes `customer_email_address`, `shipping_date`, and `shipping_documentation`; the November curl sample uses the same fields.
- For documents or images, upload with purpose `dispute_evidence` through the File Upload API, then use the resulting File_upload ID in a dispute evidence field. The guide points to separate file recommendations; it does not guarantee an upload will be accepted as sufficient evidence.
- For a single file or large plaintext evidence, both API captures name `uncategorized_file` and `uncategorized_text` as catch-all fields, while advising use of as many relevant specific fields as possible. This `uncategorized_file` fact comes from this API guide's May and November captures, as recorded in the scoped context resolution; it must not be attributed to a separate setup guide that lacks it.

## Dispute-created event and subscription boundary

The November guide says Stripe sends `charge.dispute.created` when a dispute is created. The Dispute object has a `charge` reference and may have a `payment_intent` reference; `payment_intent` is nullable. It has no direct invoice or subscription reference. Follow the linked subscription webhook guide for any associated-subscription resolution, checking that guide's own version and null-ID conditions before implementing. Neither a Charge nor a PaymentIntent filter proves subscription association.

## Detail locators

- [[raw/stripe-disputes-api-2026-11-07|November 7, 2026 capture]]: retrieve/update and illustrative response lines 13–54; evidence types, 150,000-character limit and catch-all fields lines 56–65; multiple disputes and list filters lines 67–89; dispute-created event and nullable reference boundary lines 91–93.
- [[raw/stripe-disputes-api-2026|May 9, 2026 capture]]: Node retrieve/update examples lines 12–62; evidence fields and limits, including `uncategorized_file`, lines 64–73; multiple-dispute filtering and unique-ID guidance lines 75–105.

## Related

- [[stripe]]; [[disputes]]; [[source-stripe-disputes-responding]]; [[source-stripe-disputes-best-practices]]

## Raw Sources

- [[raw/stripe-disputes-api-2026-11-07|November 7, 2026 dispute API guide]]
- [[raw/stripe-disputes-api-2026|May 9, 2026 dispute API guide]]
