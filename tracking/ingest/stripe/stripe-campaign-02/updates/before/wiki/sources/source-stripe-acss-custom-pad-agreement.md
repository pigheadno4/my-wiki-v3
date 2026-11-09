---
title: "Stripe: Custom Canadian PAD Mandate Agreements"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-acss-custom-pad-agreement-2025.md"
tags: [stripe, acss, acss-debit, canada, mandates, pad, compliance, payments-canada]
---

## Summary

Compliance guide for creating custom PAD mandate agreements for ACSS. Most businesses should not need this — the default Stripe.js mandate covers almost all cases. Custom mandates are needed only to waive debit notification emails or add non-standard cancellation/recourse terms.

## Key Details

**When to use a custom mandate**: (1) waive debit notification emails, (2) add custom cancellation or recourse terms beyond Payments Canada defaults.

**When NOT needed**: customized email content (use same mandate text), custom payment schedule (use `interval_description` via API).

**9 required elements**:

1. **Business contact info** — name, address, email reachable by customer
2. **Agreement acceptance date**
3. **PAD type** — `personal` or `business` (matches `transaction_type`)
4. **Authority to debit** — clear statement customer authorizes variable debits
5. **Payment schedule/triggers** — required if `payment_schedule` is `interval` or `combined`; must show `interval_description` value
6. **Sporadic authorization** — required if `payment_schedule` is `sporadic` or `combined`; must state each sporadic payment requires express customer authorization
7. **PAD confirmation period modification** — customer agrees to immediate debit + confirmation within 5 days
8. **Pre-notification period modification** — must be **bold/highlighted/underlined**; customer waives right to pre-notification of PAD timing/amount. Required if waiving Stripe notification emails.
9. **Recourse/reimbursement statement** — exact text required: "You have certain recourse rights if any debit doesn't comply with this PAD agreement. For example, you have the right to receive reimbursement for any debit that isn't authorized or isn't consistent with this PAD Agreement. To obtain more information on your recourse rights, contact your financial institution or visit www.payments.ca."
10. **Cancellation terms** — customer can revoke authorization with specified notice period
11. **Notice of Stripe as PSP** — must disclose Stripe as payment service provider

## Raw Sources

- [[stripe-acss-custom-pad-agreement-2025]] — verbatim webpage content; sample mandate section not included in pasted content
