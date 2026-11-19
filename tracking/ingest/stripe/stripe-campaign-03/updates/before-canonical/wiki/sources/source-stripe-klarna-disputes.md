---
title: "Stripe: Respond to Klarna Disputes"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-klarna-disputes-2025.md"
tags: [stripe, bnpl, klarna, disputes, chargebacks, inquiries, evidence]
---

## Summary

Full Klarna dispute lifecycle guide: two-stage process (inquiry → chargeback), dispute fee model, evidence requirements, and per-country test data for all 7 dispute reasons across 23 countries.

## Key Details

**180-day dispute window** (longest of any BNPL). Fraud/legal exceptions can exceed this.

**Two-stage process**:
- **Inquiry** (21 days): customer files via Klarna app. No evidence accepted. Options: contact customer, refund (avoids fee), or let escalate.
- **Chargeback**: inquiry auto-escalates after 21 days. Evidence accepted. Fee withheld until resolved; reversed if merchant wins.

**Klarna dispute fee model**: fee charged on creation but **reversed if you win** (unlike card disputes which charge regardless).

**Evidence deadlines**: 12 days standard; **5 days for fraud** disputes. Only **one round** of evidence — submit everything at once.

**Fraud disputes**: skip inquiry, go directly to chargeback.

**Return inquiries**: visible only after customer provides return proof (tracking). Check "Issuer evidence" tab for tracking details before processing refund.

**Partial disputes**: issue partial refund matching disputed amount to resolve without escalation.

**Webhook**: `charge.dispute.funds_withdrawn` marks inquiry → chargeback escalation. Each uploaded file must be used for a single dispute only.

**Test disputes**: per-country email+phone triggers for 7 dispute reasons × 23 countries.

## Raw Sources

- [[stripe-klarna-disputes-2025]] — verbatim webpage content (601 lines); fixed `_Unlike cards..._` → `*italic*`
