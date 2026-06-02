---
title: "PayPal Invoicing (Overview)"
type: source
date_ingested: 2026-04-15
original_format: webpage
raw_files:
  - "paypal-invoicing-overview.md"
  - "paypal-invoicing-integrate.md"
  - "paypal-invoicing-customize.md"
  - "paypal-invoicing-test-golive.md"
  - "paypal-invoicing-reference.md"
  - "paypal-invoicing-webhooks.md"
  - "paypal-invoicing-overview-2025.md"
  - "paypal-invoicing-lifecycle.md"
  - "paypal-invoicing-choose-solution.md"
  - "paypal-invoicing-quickstart-dashboard.md"
  - "paypal-invoicing-quickstart-api.md"
  - "paypal-invoicing-use-cases.md"
  - "paypal-invoicing-test-values.md"
  - "paypal-invoicing-webhooks-2025.md"
  - "paypal-invoicing-troubleshoot.md"
tags: [paypal, invoicing, api, qr-payment, refunds, reminders, payment-links, ach, lifecycle, erp]
---

## Overview

Overview page for PayPal's Invoicing product — create, send, and manage invoices via the Invoicing REST API or the no-code PayPal business account dashboard.

Source URL: <https://developer.paypal.com/docs/invoicing/>

Last updated: 2025-06-01

## Key Takeaways

### Two integration paths

| Path | Best for |
| --- | --- |
| **Invoicing REST API** | Merchants with their own product UI who want to customize invoice creation |
| **No-code dashboard** | Merchants who don't need API integration — manage invoices from PayPal business account |

### How it works (4 steps)

1. Merchant creates a **draft invoice**
2. Merchant sends draft → PayPal emails customer an **invoice link** (merchant can also share link directly)
3. Customer clicks link to **view invoice**
4. Customer pays with credit card, debit card, PayPal, or PayPal Credit

### Additional features

- Refund requests
- QR payment options
- Customer reminders

### Eligibility

Available in multiple countries (see PayPal country codes reference).

## Customization Options

| Feature | Key parameter | Notes |
| --- | --- | --- |
| QR code | `POST .../generate-qr-code` | Returns Base64 image; set `send_to_recipient: false` to skip email; requires BN code + Auth-Assertion headers |
| Tips | `allow_tip: true` | Flat amount or percent; shows on invoice and payment email |
| Partial payments | `allow_partial_payment: true` | Optionally set `minimum_amount_due` |
| Search, refunds, templates, reminders | See Invoicing API reference | Not detailed in this page |

## Integration (Quick Start)

**Invoice lifecycle**: Draft → Sent → Viewed → Paid (or Cancelled / Overdue)

**2-step core API flow:**

1. `POST /v2/invoicing/invoices` — creates draft; returns `INV2-XXXX` ID (201 Created); invoice not yet visible to customer
2. `POST /v2/invoicing/invoices/{id}/send` — sends to customer via email; status → UNPAID (200 OK)

**Key constraints:**

- After sending, invoice **cannot be deleted** — only cancelled
- To update a sent invoice: use `PUT` + `send_to_recipient: true` to re-notify customer
- Minimal required fields: `detail.currency_code`, `primary_recipients[].billing_info.email_address`, `items[].name/quantity/unit_amount`

## Webhooks (6 events)

| Event | Trigger |
| --- | --- |
| `INVOICING.INVOICE.CANCELLED` | Merchant or customer cancels |
| `INVOICING.INVOICE.CREATED` | Invoice created |
| `INVOICING.INVOICE.PAID` | Paid, partially paid, or payment pending |
| `INVOICING.INVOICE.REFUNDED` | Refunded or partially refunded |
| `INVOICING.INVOICE.SCHEDULED` | Invoice scheduled |
| `INVOICING.INVOICE.UPDATED` | Invoice updated |

> [!info] API version note
> Webhook related-method links point to `/v1/` — while the integration guide uses `/v2/invoicing/`. The CANCELLED event's related method incorrectly links to `invoices_get` (GET) rather than a cancel endpoint — likely a doc error.

## Raw Sources

- [[paypal-invoicing-overview]] — verbatim webpage content with 4-step flow, two integration paths, eligibility note
- [[paypal-invoicing-integrate]] — quick start: auth, create draft (POST /v2/invoicing/invoices), send (POST .../send); lifecycle states; cannot delete after send
- [[paypal-invoicing-customize]] — QR code (POST .../generate-qr-code, Base64 response, send_to_recipient: false for QR-only); tips (allow_tip); partial payments (allow_partial_payment + minimum_amount_due)
- [[paypal-invoicing-test-golive]] — 13 operations with ERRINV codes; business-logic errors (CANT_CANCEL_IN_DRAFT, CANT_SEND_WITHOUT_EMAIL, CANT_PAY_MORE_THAN_AMOUNT, etc.); JSON pointer + path param simulation
- [[paypal-invoicing-reference]] — pointers to: Invoicing API reference (/v2/), PayPal API Executor, Invoicing webhook events
- [[paypal-invoicing-webhooks]] — 6 events (CANCELLED/CREATED/PAID/REFUNDED/SCHEDULED/UPDATED); PAID fires for full, partial, and pending; API links use v1 (integration uses v2); CANCELLED link points to GET (doc error)
- [[paypal-invoicing-overview-2025]] — docs.paypal.ai overview: Invoicing vs Payment Links comparison table (partial payments, ACH/Pay by Bank, reminders — Invoicing only), 4 sub-pages: lifecycle, choose-solution, quickstart, integrate
- [[paypal-invoicing-lifecycle]] — Invoice status lifecycle: 10 statuses, UI↔API name mapping, SENT vs UNPAID distinction, terminal statuses, MARKED_AS_PAID/REFUNDED for external reconciliation
- [[paypal-invoicing-choose-solution]] — Dashboard vs REST API decision guide: no-code/low-volume vs automated/high-volume, OAuth 2.0, identical payer experience
- [[paypal-invoicing-quickstart-dashboard]] — 10-step dashboard quickstart: Create > Invoice, email required, "Amount only" item mode, auto-calculated total, Preview then Send
- [[paypal-invoicing-quickstart-api]] — API quickstart: 3-step create+send flow, INV2-* ID format, cannot delete after send (cancel only), PUT + send_to_recipient:true to update sent invoice
- [[paypal-invoicing-use-cases]] — 6 use case patterns: minimum fields, ERP external invoice, hourly services, shippable goods, digital goods, mixed billing; detail.reference (customer-visible) vs detail.memo (private); don't use qty>1 on AMOUNT lines
- [[paypal-invoicing-test-values]] — Test simulation values (case-sensitive): JSON pointer via detail.reference, path parameter via INV2-ABCD-1234-EINV-XXXX IDs; 10 operations covered; key error codes for business rules
- [[paypal-invoicing-troubleshoot]] — Error codes, HTTP statuses, field limits (invoice number 25 chars, item name 200, note 4000, reference 120); INVOICE_CANNOT_BE_DELETED (draft/scheduled/canceled only)

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[recurring-payments]] — invoicing is distinct from recurring/subscription billing
