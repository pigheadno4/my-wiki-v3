---
title: "Stripe: Custom Canadian PAD Mandate Agreements"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/acss-debit/custom-pad-agreement"
raw_files:
  - "stripe-payments-acss-debit-custom-pad-agreement-2026-11-07.md"
  - "stripe-acss-custom-pad-agreement-2025.md"
tags: [stripe, acss, acss-debit, canada, mandates, pad, compliance, payments-canada]
---

## Summary

Guide for businesses considering a custom Canadian PAD mandate agreement for ACSS. The default Stripe.js mandate is intended to cover almost all businesses. The guide gives two scenarios in which a business can create a custom agreement: seeking authorization not to send debit notification emails, or providing different or additional cancellation or recourse terms that satisfy Payments Canada rules. It does not make a custom agreement mandatory for either scenario or state that these are the only possible reasons.

## Key Details

**Reasons to consider a custom mandate given by this guide**: (1) obtain customer authorization not to send debit notification emails, or (2) provide different or additional cancellation or recourse terms that satisfy Payments Canada rules. These are examples of when a business can create one, not mandatory or exhaustive gates.

**When NOT needed**: customized email content (use same mandate text), custom payment schedule (use `interval_description` via API).

**11 table requirement rows, including two conditional rows** (the schedule/triggers row applies only to `payment_schedule` `interval` or `combined`; sporadic authorization applies only to `sporadic` or `combined`):

1. **Business contact info** — accurate contact information that lets the customer reach the business through a communication method the customer uses; the Rocket Rides name, postal address, and email are examples, not a required three-field list
2. **Agreement acceptance date**
3. **PAD type** — `personal` or `business` (matches `transaction_type`)
4. **Authority to debit** — clear statement customer authorizes variable debits
5. **Payment schedule/triggers** — required if `payment_schedule` is `interval` or `combined`; must show `interval_description` value
6. **Sporadic authorization** — required if `payment_schedule` is `sporadic` or `combined`; must state each sporadic payment requires express customer authorization
7. **PAD confirmation period modification** — customer agrees to immediate debit + confirmation within 5 days
8. **Pre-notification period modification** — pre-debit notices are required unless expressly waived. If the customer opts out, the waiver text must be included and **bolded, highlighted, or underlined**; the period can otherwise be modified in the agreement.
9. **Recourse/reimbursement statement** — the guide requires its specified statement verbatim in its entirety; use the exact raw text at `raw/stripe-payments-acss-debit-custom-pad-agreement-2026-11-07.md:70`, not a paraphrase.
10. **Cancellation terms** — customer can revoke authorization with specified notice period
11. **Notice of Stripe as PSP** — must disclose Stripe as payment service provider

The Rocket Rides address, email, and thirty-day cancellation notice in the table are sample agreement terms; the requirement is accurate business contact information and cancellation terms specifying the notice period, not those sample values. The 2026-11-07 diff normalizes table formatting, selects a `direct-api` link variant, and changes an example link to HTTPS; it does not establish a new PAD mandate rule.

## Related

- [[stripe]] — provider
- [[stripe-acss-debit]] — Canadian PAD / ACSS Debit concept

## Raw Sources

- [[raw/stripe-payments-acss-debit-custom-pad-agreement-2026-11-07|2026-11-07 custom PAD guide]] — 11 requirement rows, conditional schedule rows, notice/waiver and recourse language

- [[raw/stripe-acss-custom-pad-agreement-2025|2026-05-02 custom PAD guide]] — verbatim webpage content; sample mandate section not included in pasted content
