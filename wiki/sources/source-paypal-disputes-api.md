---
title: "PayPal Disputes API"
type: source
date_ingested: 2026-04-18
original_format: webpage
raw_files:
  - "paypal-disputes-api-2025.md"
  - "paypal-disputes-test-go-live-2025.md"
  - "paypal-disputes-reasons-evidence-2025.md"
  - "paypal-disputes-test-values-2025.md"
  - "paypal-disputes-file-types-2025.md"
tags: [paypal, disputes, chargebacks, disputes-api, webhooks]
---

## Summary

Comprehensive guide to the PayPal Disputes API for programmatic dispute management. Covers the full lifecycle from listing disputes to resolving them, with detailed endpoint references, request/response shapes, and webhook integration.

## Key Takeaways

- **Base path**: `/v1/customer/disputes`
- **9 action endpoints**: list, show, send-message, make-offer, accept-claim, provide-evidence, escalate, provide-supporting-info, appeal, acknowledge-returned-item
- **HATEOAS-driven**: use `links[]` in the show-dispute response to determine available actions at each lifecycle stage
- **`CHARGEBACK` in API ≠ card chargeback**: it's PayPal's internal lifecycle stage label for an escalated claim
- **Opt-out of inquiry stage**: contact account manager; all disputes then start directly at CHARGEBACK stage
- **Accelerated Response**: rolling-out feature — merchant submits docs within 10 days; post-escalation window varies by scenario

## Dispute Lifecycle Stages

| `dispute_life_cycle_stage` | Meaning |
| --- | --- |
| `INQUIRY` | Pre-claim; INR/SNAD only; 20-day window; internal disputes only |
| `CHARGEBACK` | Escalated claim; PayPal adjudicates; merchant can accept/contest/offer |
| `PRE_ARBITRATION` | First appeal; merchant appeals chargeback outcome |
| `ARBITRATION` | Second appeal; card network adjudicates external cases |

## Key Response Fields (Show Dispute Details)

| Field | Purpose |
| --- | --- |
| `dispute_life_cycle_stage` | Current stage → determines available actions |
| `status` | `OPEN` / `WAITING_FOR_SELLER_RESPONSE` / `WAITING_FOR_BUYER_RESPONSE` / `UNDER_REVIEW` / `RESOLVED` |
| `seller_response_due_date` | Deadline — missing it auto-closes in buyer's favor |
| `allowed_response_options` | `make_offer.offer_types` + `accept_claim.accept_claim_types` + `acknowledge_return_item.acknowledgement_types` |
| `evidences[].evidence_type` | Type of evidence requested (e.g. `PROOF_OF_FULFILLMENT`) |
| `evidences[].source` | `REQUESTED_FROM_SELLER` = action required |
| `evidences[].document.url` | Download URL (requires `DOCUMENTS_DISPUTES_DOWNLOAD` scope) |
| `links[]` | HATEOAS links — check these first to know what actions are available |

## CHARGEBACK Disambiguation

> [!warning] `CHARGEBACK` ≠ card chargeback
> In the Disputes API, `dispute_life_cycle_stage: CHARGEBACK` means **PayPal has taken over adjudication of an escalated internal claim**. It is NOT a credit/debit card chargeback filed with a bank. Card chargebacks from banks appear as external disputes and also use this same stage label — context is `dispute_channel: EXTERNAL` vs `INTERNAL`. Always check `dispute_channel` alongside `dispute_life_cycle_stage`.

## Status Transition Logic

Statuses do not change arbitrarily — each transition is triggered by a specific event:

| From status | Trigger | To status |
| --- | --- | --- |
| — | Buyer files dispute | `OPEN` |
| `OPEN` | PayPal notifies merchant and requests response | `WAITING_FOR_SELLER_RESPONSE` |
| `WAITING_FOR_SELLER_RESPONSE` | Merchant submits evidence or offer | `WAITING_FOR_BUYER_RESPONSE` |
| `WAITING_FOR_SELLER_RESPONSE` | Merchant escalates or does not respond within deadline | `UNDER_REVIEW` |
| `WAITING_FOR_BUYER_RESPONSE` | Buyer responds (accepts, rejects, or escalates) | `WAITING_FOR_SELLER_RESPONSE` or `UNDER_REVIEW` |
| `UNDER_REVIEW` | PayPal requests more evidence | `WAITING_FOR_SELLER_RESPONSE` or `WAITING_FOR_BUYER_RESPONSE` |
| `UNDER_REVIEW` | PayPal adjudicates | `RESOLVED` |
| `RESOLVED` | Merchant or buyer appeals | `WAITING_FOR_SELLER_RESPONSE` (new PRE_ARBITRATION stage) |

**Key rule**: `seller_response_due_date` is your deadline while in `WAITING_FOR_SELLER_RESPONSE`. Missing it causes auto-resolution in the buyer's favor. Always poll or use webhooks to catch this transition.

## Stage × Status → Actions

| Stage | Status | Actions available |
| --- | --- | --- |
| `INQUIRY` | `OPEN` | None (wait for PayPal to set WAITING_FOR_SELLER_RESPONSE) |
| `INQUIRY` | `WAITING_FOR_SELLER_RESPONSE` | send-message, make-offer, accept-claim, escalate, provide-evidence, acknowledge-returned-item |
| `INQUIRY` | `WAITING_FOR_BUYER_RESPONSE` | None (wait for buyer) |
| `CHARGEBACK/PRE_ARBITRATION/ARBITRATION` | `WAITING_FOR_SELLER_RESPONSE` | provide-evidence, accept-claim, make-offer, appeal (if resolved against merchant) |
| `CHARGEBACK/PRE_ARBITRATION/ARBITRATION` | `UNDER_REVIEW` | provide-supporting-info only |
| Any | `WAITING_FOR_BUYER_RESPONSE` or `RESOLVED` | None |

## `allowed_response_options` Decision Tree

Always read `allowed_response_options` from the show-dispute response **before** deciding what action to take — PayPal controls which options are valid at any given moment.

```text
show-dispute response
└── allowed_response_options
    ├── make_offer.offer_types → present? → POST /make-offer
    │   ├── REFUND              — full refund, buyer keeps item
    │   ├── REFUND_WITH_RETURN  — refund conditional on item return
    │   ├── REFUND_WITH_REPLACEMENT — send replacement instead
    │   └── REPLACEMENT_WITHOUT_REFUND — replacement only
    │
    ├── accept_claim.accept_claim_types → present? → POST /accept-claim
    │   ├── REFUND              — full refund, close in buyer's favor
    │   ├── PARTIAL_REFUND      — partial amount
    │   ├── REFUND_WITH_RETURN  — refund after return
    │   └── REFUND_WITH_RETURN_SHIPMENT_LABEL — PayPal generates return label
    │
    └── acknowledge_return_item.acknowledgement_types → present? → POST /acknowledge-returned-item
        ├── ITEM_RECEIVED
        ├── ITEM_NOT_RECEIVED
        ├── DAMAGED
        ├── EMPTY_PACKAGE_OR_DIFFERENT
        └── MISSING_ITEMS
```

**If none of the above are present**: check `links[]` for `provide_evidence` or `send_message` — those are always available when the status is `WAITING_FOR_SELLER_RESPONSE` during INQUIRY.

## Endpoints

| Action | Method | Path |
| --- | --- | --- |
| List disputes | GET | `/v1/customer/disputes` |
| Show details | GET | `/v1/customer/disputes/{id}` |
| Send message | POST | `/v1/customer/disputes/{id}/send-message` |
| Make offer | POST | `/v1/customer/disputes/{id}/make-offer` |
| Accept claim | POST | `/v1/customer/disputes/{id}/accept-claim` |
| Provide evidence | POST | `/v1/customer/disputes/{id}/provide-evidence` |
| Escalate to claim | POST | `/v1/customer/disputes/{id}/escalate` |
| Provide supporting info | POST | `/v1/customer/disputes/{id}/provide-supporting-info` |
| Appeal | POST | `/v1/customer/disputes/{id}/appeal` |
| Acknowledge returned item | POST | `/v1/customer/disputes/{id}/acknowledge-returned-item` |

## Provide Evidence

Multipart request required. Key fields:

- `evidence_type`: match value from `evidences[].evidence_type` in show-dispute response
- `evidence_info.tracking_info`: array of `{carrier_name, tracking_number}` for `PROOF_OF_FULFILLMENT`
- `evidence_info.refund_ids`: for `PROOF_OF_REFUND`
- `documents`: attach files (see supported file types reference)
- `notes`: free-text notes

## Accelerated Response (Rolling Out)

Merchant submits docs within 10 days of inquiry start. Post-escalation time depends on who escalates and when:

| Scenario | Post-escalation window | If no docs submitted |
| --- | --- | --- |
| Escalated before day 8 (either party) | Remaining time in 10-day window | Adjudicated on available info |
| Buyer escalates day 8-10, sent message/offer | 3 days | Adjudicated on available info |
| Buyer escalates after day 10, sent message/offer | 3 days | Closed in buyer's favor |
| Buyer escalates after day 10, no message/offer | No additional time | Closed in buyer's favor |
| Merchant escalates after day 8 | 3 days | Adjudicated on available info |

## Webhooks

Subscribe to dispute events via PayPal developer dashboard or Webhooks management API. Handler must: listen → process → verify signature → act. See `/reference/webhook-events/disputes-v1` for event list.

## Common Errors

| Code | Cause | Fix |
| --- | --- | --- |
| 400 | Invalid fields or formats | Validate request body against API reference |
| 401 | Missing/expired/invalid access token | Regenerate token and retry |
| 403 | App or account lacks permission | Confirm Disputes API access, scopes, permissions |

## Related Pages

- [[paypal]] — company page
- [[disputes]] — disputes & chargebacks concept page
- [[source-paypal-disputes-overview]] — disputes overview, setup, Resolution Center guide
- [[source-paypal-customer-disputes]] — older disputes API coverage from developer.paypal.com

## Raw Sources

- [[paypal-disputes-api-2025]] — full 748-line Disputes API guide from docs.paypal.ai with curl examples for all 9 endpoints
- [[paypal-disputes-file-types-2025]] — Evidence file constraints: .jpg/.jpeg/.gif/.png/.pdf; max 10 MB per file; max 50 MB total per API call
- [[paypal-disputes-test-values-2025]] — Disputes API test values: 9 operations, ERRDIS path/query params for negative simulation; list disputes uses query param; accept-claim has 6 extra VALIDATION_ERROR subtypes (INSUFFICIENT_FUNDS, INTANGIBLE_ITEM_CANNOT_BE_RETURNED, MISSING_RETURN_SHIPPING_ADDRESS, etc.); provide-evidence + appeal share 6 VALIDATION_ERROR subtypes (INVALID_EVIDENCE_FILE, MISSING_TRACKING_INFO, MISSING_REFUND_ID, etc.); case-sensitive
- [[paypal-disputes-reasons-evidence-2025]] — Dispute reasons & evidence reference: 9 reasons (MERCHANDISE_OR_SERVICE_NOT_RECEIVED/NOT_AS_DESCRIBED, UNAUTHORISED, CREDIT_NOT_PROCESSED, DUPLICATE_TRANSACTION, INCORRECT_AMOUNT, PAYMENT_BY_OTHER_MEANS, CANCELED_RECURRING_BILLING, OTHER); evidence types per reason: PROOF_OF_FULFILLMENT (tracking_info or doc), PROOF_OF_REFUND (refund_ids), OTHER (notes/docs)
- [[paypal-disputes-test-go-live-2025]] — 1031-line test & go-live guide: 3 sandbox-only buyer endpoints (create dispute/chargeback/change-reason); 2 buyer action endpoints (accept-offer/deny-offer); 2 PayPal-action endpoints (adjudicate/require-evidence); 3 internal dispute + 5 chargeback test scenarios; Accelerated Response sandbox testing; webhook testing for CREATED/UPDATED/RESOLVED events (inquiry + claim stages); test values table; go-live checklist
