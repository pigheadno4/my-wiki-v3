---
title: "Stripe: Respond to Klarna Disputes"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-15
canonical_url: https://docs.stripe.com/payments/klarna/disputes
original_format: webpage
raw_files:
  - "stripe-payments-klarna-disputes-2026-11-07.md"
  - "stripe-klarna-disputes-2025.md"
tags: [stripe, bnpl, klarna, disputes, chargebacks, inquiries, evidence]
---

## Summary

[[stripe]] guide to Klarna payment disputes: a customer files a complaint or return request in the Klarna app; most cases pass through an inquiry before a chargeback, while some reach chargeback directly. It covers the merchant's refund or evidence choices, fee and funds handling, Dispute API states, and sandbox test triggers. See [[stripe-bnpl]] and [[disputes]].

## Key Details

**Filing window**: Customers generally have 180 calendar days from capture. Klarna may raise a dispute beyond the limitation in exceptional cases including reported fraud, external-authority legal claims, local consumer-protection rules, and debt collection. This is a guide-specific window, not a ranking against other BNPL methods.

**Inquiry**: Stripe notifies the business when Klarna opens an inquiry, and Klarna pauses outstanding customer repayments until resolution. Almost all Klarna disputes start here, with a 21-calendar-day window. The business can seek a mutual resolution and the customer can withdraw the inquiry in the Klarna app, or the business can refund the full disputed amount. A refund during inquiry resolves it without escalation or a dispute fee; Klarna accepts no evidence at this stage. Only an **unresolved** inquiry escalates after the window. Refunds cannot be performed after chargeback escalation.

**Direct chargeback exceptions**: Fraudulent transactions are one example of direct escalation, and Stripe says there are other scenarios. The comparison table says all disputes except fraudulent ones start as inquiries, while the inquiry prose explicitly allows other direct-chargeback exceptions; do not treat that table as an exhaustive rule.

**Partial disputes**: A partial refund resolves an inquiry when it matches the amount of a partial dispute. If the dispute is for the full order, a partial refund does not resolve it; the business can contest the later chargeback with evidence. For a return inquiry, Stripe shows it in Dashboard, API, or events only after the customer provides return proof. In Dashboard, inspect **Issuer evidence** for tracking and verify return or transit before refunding within the inquiry period.

**Chargeback and fee**: On escalation of an unresolved inquiry, Stripe withholds disputed funds and the associated fee pending resolution. The guide's comparison table says the Klarna dispute fee is assessed when a dispute is created, while its inquiry instructions say refunding during inquiry avoids the fee and its chargeback section locates the withholding at escalation. Read the table with those stage-specific instructions; do not infer a fee charged at inquiry opening. If the business wins after countering, Stripe releases the withheld funds and fee; if it loses, Stripe debits them and Klarna returns the disputed amount to the customer. The guide contrasts this single Klarna fee with the card-fee model in its captured comparison.

**Evidence**: Counter a chargeback in the Stripe Dashboard or Disputes API by the displayed deadline or `evidence_due_by`: 12 calendar days from escalation, or 5 days for fraud. Klarna accepts one evidence round. If the business misses submission, Klarna rules for the customer. Dashboard's **Needs Response** flow ends with **Submit Evidence**; the API examples upload files with `purpose=dispute_evidence` and update the Dispute with evidence and `submit=true`. An uploaded file is for one dispute only. The November capture uses cURL examples where the older capture used Node examples; that presentation change alone does not establish a new API contract.

**States and reason fields**: `warning_needs_response` and `warning_closed` are inquiry states; `needs_response`, `under_review`, `lost`, and `won` are chargeback states. `charge.dispute.funds_withdrawn` marks escalation. Stripe's `reason` holds its mapped category and `payment_method_details.klarna.reason_code` holds Klarna's code, shown as **Network Reason Code** in Dashboard. For a lost chargeback, `payment_method_details.klarna.chargeback_loss_reason_code` may appear in the webhook when Klarna closes it; if the business neither countered the dispute nor accepted the loss, the field is unavailable in the webhook but eventually available through the API by fetching the Dispute object. Do not infer an outcome from evidence submission or the status alone before adjudication.

**Sandbox tests**: The capture lists email and phone triggers across 23 customer-country tables, with seven scenario rows per country but six distinct Stripe dispute-reason labels (`General` appears twice). A sandbox transaction can open a dispute and accept evidence; it cannot simulate the final dispute outcome. The listed test regions are capture-dated examples, not proof of current account eligibility or live availability.

## Raw Sources

- [[raw/stripe-payments-klarna-disputes-2026-11-07|November 7, 2026 Klarna disputes guide]] — full Stripe guide capture, fetched 2026-11-07 (575 lines).
- [[raw/stripe-klarna-disputes-2025|May 6, 2026 Klarna disputes guide]] — prior full guide capture, fetched 2026-05-06 (601 lines); historical capture retained, including the earlier italic-markup normalization noted in the original summary.
