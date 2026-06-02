---
title: "PayPal Customer Disputes"
type: source
date_ingested: 2026-04-16
original_format: webpage
raw_files:
  - "paypal-customer-disputes.md"
  - "paypal-disputes-integration-guide.md"
  - "paypal-disputes-testing.md"
  - "paypal-disputes-acceptance-tests.md"
  - "paypal-disputes-faq.md"
  - "paypal-disputes-webhooks.md"
  - "paypal-disputes-lifecycle-reference.md"
tags: [paypal, disputes, chargebacks, resolution-center, disputes-api]
---

## Summary

Overview of PayPal's dispute system — how disputes arise, the two resolution paths, buyer workflows, and the Disputes API for automation.

## Key Takeaways

- **Dispute triggers**: non-receipt of goods/services, item not as described, or buyer needing transaction details
- **Two resolution paths**:
  1. **PayPal Resolution Center** — buyer files directly with PayPal or seller; seller responds; refund if resolved in buyer's favor
  2. **Bank/card issuer chargeback** — buyer disputes with bank; dispute created in PayPal; seller responds; refund if resolved in buyer's favor
- **Buyer options in Resolution Center**: non-receipt, item not as described, unauthorized activity, billing issue
- **Disputes API actions**: list, show details, message other party, make offer (full/partial refund or replacement), escalate to claim, provide evidence (tracking + file uploads), accept claim, appeal dispute

## Disputes API Capabilities

| Method | Purpose |
| --- | --- |
| List disputes | View open cases |
| Show dispute details | Transaction ID, date opened, other details |
| Send message | Communicate with other party |
| Make offer | Full refund + return, partial refund, or replacement |
| Escalate to claim | Bring PayPal in to adjudicate |
| Provide evidence | Tracking info + file uploads |
| Accept claim | Refund customer, close case |
| Appeal dispute | Submit additional info to contest |

## Dispute Lifecycle Stages

The integration guide covers a 5-step flow:

1. **Setup** — create app with Disputes feature enabled
2. **Gather info** (any stage) — list disputes, show details, acknowledge returned item
3. **Inquiry stage** (`status: INQUIRY`) — message other party, make offer, escalate to claim
4. **Claim stage** — provide evidence, accept claim, appeal dispute
5. **Settlement** (sandbox only) — update dispute status, settle dispute

## Offer Types

| Offer type | Description |
| --- | --- |
| Refund only | Merchant refunds a specific amount |
| Refund + return | Full refund; customer must return item to specified address |
| Refund + replacement | Merchant refunds and ships replacement item |

Offer request body fields: `note` (required), `offer_amount` (required), `return_shipping_address` (optional), `invoice_id` (optional).

## Dispute Reasons & Required Evidence

| Reason | Evidence types |
| --- | --- |
| MERCHANDISE_OR_SERVICE_NOT_RECEIVED | PROOF_OF_FULFILLMENT (tracking + carrier or note/doc), PROOF_OF_REFUND |
| MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED | OTHER (note/doc), PROOF_OF_REFUND |
| UNAUTHORISED | PROOF_OF_FULFILLMENT, PROOF_OF_REFUND, OTHER |
| CREDIT_NOT_PROCESSED | PROOF_OF_REFUND, OTHER |
| DUPLICATE_TRANSACTION | PROOF_OF_REFUND, OTHER |
| INCORRECT_AMOUNT | PROOF_OF_REFUND (for difference), OTHER |
| PAYMENT_BY_OTHER_MEANS | PROOF_OF_REFUND, OTHER |
| CANCELED_RECURRING_BILLING | PROOF_OF_REFUND, OTHER (e.g. subscription agreement) |
| OTHER | PROOF_OF_REFUND, OTHER |

## Document Constraints

- Max 50 MB total per request; max 10 MB per file
- Supported formats: JPG, JPEG, GIF, PNG, PDF

## Sandbox Setup (Buyer-Side Disputes)

Creating disputes in sandbox requires 6 steps: get buyer OAuth consent via Log in with PayPal → generate merchant access token → generate JWT assertion (base64url of `{iss: CLIENT_ID, email: BUYER_EMAIL}`) → buyer sends money to merchant → note transaction ID → POST to `/v1/customer/disputes` with JWT in `PayPal-Auth-Assertion` header.

Creating chargebacks: POST to `/v2/customer-support/process-chargeback` with seller transaction ID (transaction must have been made via credit card).

## Appeal Outcomes

- Seller wins appeal → money from PayPal; `CASE.RESOLVED` webhook; settlement report entry `T0805`
- Seller loses appeal → no money movement; case closed; `CASE.RESOLVED` webhook

## Negative Testing

Trigger errors by embedding `ERRDIS0xx` IDs in the dispute ID path or `disputed_transaction_id` query param. Test values are case sensitive.

| Action | Endpoint | Error codes covered |
| --- | --- | --- |
| List disputes | `GET /v1/customer/disputes?disputed_transaction_id=ERRDIS023–034` | FORBIDDEN, INVALID_RESOURCE_ID, NOT_ACCEPTABLE, UNSUPPORTED_MEDIA_TYPE, RATE_LIMIT_REACHED, SERVICE_UNAVAILABLE, INTERNAL_SERVICE_ERROR, AUTHORIZATION_ERROR, VALIDATION_ERROR (×4) |
| Show dispute details | `GET /v1/customer/disputes/ERRDIS015–022` | FORBIDDEN → AUTHORIZATION_ERROR (8 codes) |
| Send message | `POST .../ERRDIS091–099/send-message` | + UNPROCESSABLE_ENTITY |
| Make offer | `POST .../ERRDIS100–108/make-offer` | + UNPROCESSABLE_ENTITY |
| Escalate | `POST .../ERRDIS082–090/escalate` | + UNPROCESSABLE_ENTITY |
| Provide evidence | `POST .../ERRDIS035–050/provide-evidence` | + UNPROCESSABLE_ENTITY, VALIDATION_ERROR (×7) |
| Accept claim | `POST .../ERRDIS051–065/accept-claim` | + UNPROCESSABLE_ENTITY (×2), VALIDATION_ERROR (×5) |
| Acknowledge return | `POST .../ERRDIS109–117/acknowledge-return-item` | + UNPROCESSABLE_ENTITY |
| Appeal | `POST .../ERRDIS066–081/appeal` | + UNPROCESSABLE_ENTITY, VALIDATION_ERROR (×7) |

## Acceptance Test Criteria (34 scenarios)

Grouped by feature:

| Feature | Scenarios | Key behavioral rules |
| --- | --- | --- |
| Dispute created webhook | 1–7 | Seller opt-in → INQUIRY; seller opt-out → CHARGEBACK; no duplicate disputes on closed transaction |
| Dispute updated webhook | 8–10 | NR reason can be updated to SNAD or UNAUTHORIZED mid-dispute |
| Dispute resolved webhook | 11–13 | Settle sandbox with `adjudication_outcome: BUYER_FAVOR / SELLER_FAVOR` |
| Provide evidence | 14–17 | Check HATEOAS links + merchant response due date before calling; PROOF_OF_REFUND and PROOF_OF_SHIPMENT both supported |
| Accept claim | 18–21 | Partial refund < dispute amount → email customer for consent; ≥ dispute amount → case closes |
| Appeal dispute | 22–25 | Check HATEOAS appeal link before calling; PROOF_OF_REFUND and PROOF_OF_SHIPMENT supported |
| Send message | 26–27 | Requires opt-in to dispute phase; message visible in show dispute details |
| Make offer | 28–31 | NR: REFUND only; SNAD: REFUND, REFUND_WITH_RETURN, REFUND_WITH_REPLACEMENT |
| Escalate claim | 32–33 | Stage transitions INQUIRY → CHARGEBACK; triggers dispute updated webhook |
| Other | 34 | Use webhook ID to deduplicate webhooks |

> [!warning] Contradiction — document upload limits
> Acceptance test criteria (scenario 14, updated 2024-09-23): **10 MB total / 5 MB per file**.
> Integration guide (updated 2025-12-17): **50 MB total / 10 MB per file**.
> The integration guide is likely authoritative as it is more recent.

## Use Cases

- Automate handling of large dispute volumes
- Manage PayPal disputes from internal tools without using the Resolution Center
- Surface open disputes to sellers in a shopping cart (read-only)

## Lifecycle Stages Reference

- **Inquiry stage**: 20-day window for buyer/seller to resolve without PayPal; `dispute_lifecycle_stage: INQUIRY`
- **Claim stage**: escalated after 20 days; stages are CHARGEBACK → PRE_ARBITRATION → ARBITRATION
- **Settlement**: PayPal adjudicates and communicates outcome to bank, merchant, and customer

### Dispute status → available actions

| Status | Buyer actions | Seller actions |
| --- | --- | --- |
| OPEN | validate-eligibility, send-message, escalate, cancel, change-reason; after offer: accept-offer, deny-offer | send-message, make-offer, accept-claim, escalate, partial-update |
| WAITING_FOR_BUYER_RESPONSE | provide-evidence, cancel | — |
| WAITING_FOR_SELLER_RESPONSE | — | provide-evidence, accept-claim, acknowledge-return-item |
| UNDER_REVIEW | — | — |
| RESOLVED | — | — |

### Actions by stage

| Stage | Seller | Buyer |
| --- | --- | --- |
| Gathering info (any) | list disputes, show details | list disputes, show details |
| Inquiry | send-message, make-offer, escalate, acknowledge-return-item | send-message, accept-offer, deny-offer, escalate, cancel, change-reason |
| Claim | accept-claim, provide-evidence, provide-supporting-info, appeal | accept-offer, deny-offer, provide-evidence, provide-supporting-info, cancel, change-reason |

![Dispute state machine](../raw/assets/paypal-disputes-state-machine.svg)

## Webhook Payload Schema

Key top-level fields in dispute webhook events:

| Field | Description |
| --- | --- |
| `dispute_id` | Stable ID — never changes through life of transaction |
| `disputed_transactions` | Array with `buyer_transaction_id`, `seller_transaction_id`, `transaction_status`, items |
| `reason` | Dispute reason code (10 values — see below) |
| `status` | OPEN, WAITING_FOR_BUYER_RESPONSE, WAITING_FOR_SELLER_RESPONSE, UNDER_REVIEW, RESOLVED, OTHER |
| `dispute_amount` | Amount disputed (may be less than transaction total) |
| `dispute_outcome` | `outcome_code` + `amount_refunded` |
| `dispute_life_cycle_stage` | INQUIRY, CHARGEBACK, PRE_ARBITRATION, ARBITRATION |
| `dispute_channel` | INTERNAL (buyer contacts PayPal) or EXTERNAL (buyer contacts bank/card issuer) |
| `messages` | Array of buyer/seller messages with `posted_by`, `time_posted`, `content` |
| `evidences` | Array with `evidence_type`, `evidence_info`, `documents`, `notes`, `item_id` |
| `buyer_response_due_date` | Missed → case closes in merchant's favor |
| `seller_response_due_date` | Missed → case closes in customer's favor |
| `offer` | `buyer_requested_amount`, `seller_offered_amount`, `offer_type` |
| `communication_details` | Merchant contact info for evidence sharing |
| `links` | HATEOAS links for allowed next actions |

### Offer types (4)

- `REFUND` — refund only, no item return (chargeback phase)
- `REFUND_WITH_RETURN` — full refund + customer returns item (chargeback phase)
- `REFUND_WITH_REPLACEMENT` — refund + merchant ships replacement (inquiry phase)
- `REPLACEMENT_WITHOUT_REFUND` — replacement only, no refund (inquiry phase)

### Evidence types (21)

PROOF_OF_FULFILLMENT, PROOF_OF_REFUND, PROOF_OF_DELIVERY_SIGNATURE, PROOF_OF_RECEIPT_COPY, RETURN_POLICY, BILLING_AGREEMENT, PROOF_OF_RESHIPMENT, ITEM_DESCRIPTION, POLICE_REPORT, AFFIDAVIT, PAID_WITH_OTHER_METHOD, COPY_OF_CONTRACT, TERMINAL_ATM_RECEIPT, PRICE_DIFFERENCE_REASON, SOURCE_CONVERSION_RATE, BANK_STATEMENT, CREDIT_DUE_REASON, REQUEST_CREDIT_RECEIPT, PROOF_OF_RETURN, CHANGE_REASON, OTHER

> [!info] New dispute reason: PROBLEM_WITH_REMITTANCE
> The webhook schema lists `PROBLEM_WITH_REMITTANCE` as a valid dispute reason. This does not appear in the integration guide's dispute reasons section. May be a less common reason code not covered in the integration guide's evidence table.

## FAQ Highlights

- **No extra fees** to integrate the Disputes API
- **Merchant cannot see customer evidence** — legal/privacy restriction; evidence only visible to submitter
- **One dispute or chargeback per transaction** maximum; dispute amount ≤ transaction amount
- **Dispute ID never changes** through the life of a transaction
- **Closed disputes can be reopened** (e.g. buyer files external chargeback)
- **UNAUTHORISED disputes** are filed directly as claims — no escalation available
- **`return_shipping_address`** works only for internal PayPal SNAD cases, not external chargebacks
- **Due dates**: always read from `buyer_response_due_date` / `seller_response_due_date` in show dispute details
- **Final resolution amount**: `dispute_outcome.amount_refunded`

### `dispute_outcome` values

| Value | Merchant result |
| --- | --- |
| RESOLVED_BUYER_FAVOR | Loss |
| RESOLVED_SELLER_FAVOR | Win |
| RESOLVED_WITH_PAYOUT | Win |
| CANCELED_BY_BUYER | Win |
| ACCEPTED | Loss |
| DENIED | Win |
| NONE | Neither (previous dispute closed without decision) |
| Empty | Neither (dispute not yet resolved) |

### Full lifecycle stage order

INQUIRY → CHARGEBACK → PRE_ARBITRATION → ARBITRATION (can move backwards when buyer files external case or changes reason code)

### Webhook events

- `CUSTOMER.DISPUTE.CREATE`
- `CUSTOMER.DISPUTE.UPDATED`
- `CUSTOMER.DISPUTE.RESOLVED`

## Related Pages

- [[paypal]] — company page
- [[disputes]] — dispute/chargeback concept
- [[paypal-fraud-risk]] — fraud and chargeback protection products

## Raw Sources

- [[paypal-customer-disputes]] — verbatim PayPal developer docs on disputes overview
- [[paypal-disputes-integration-guide]] — full API integration guide: lifecycle stages, offer types, 9 dispute reasons + evidence requirements, sandbox setup
- [[paypal-disputes-testing]] — negative testing reference: ERRDIS0xx trigger values for all 9 API actions
- [[paypal-disputes-acceptance-tests]] — 34 acceptance test scenarios: webhooks, evidence, accept claim, appeal, make offer, escalate
- [[paypal-disputes-faq]] — 28 FAQ entries: dispute_outcome values, lifecycle stages, escalation eligibility, evidence visibility, limits
- [[paypal-disputes-webhooks]] — webhook payload schema: all top-level fields, 4 offer types, 21 evidence types, dispute_channel, response due dates
- [[paypal-disputes-lifecycle-reference]] — lifecycle stages reference: 20-day inquiry window, status→actions map, buyer-side actions, state machine diagram
