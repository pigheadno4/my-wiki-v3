---
title: "Stripe — Dispute Sample Evidence Packets"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: https://docs.stripe.com/disputes/visual-evidence
raw_files:
  - "stripe-disputes-visual-evidence-2026-11-07.md"
  - "stripe-disputes-visual-evidence-2026.md"
tags: [stripe, disputes, chargebacks, evidence, visual-examples, dispute-response]
---

## Summary

Stripe gives **illustrative, non-exhaustive** evidence-packet examples for seven dispute categories. **Credit not processed** and **Duplicate** explicitly show paired **Approved** and **Denied** packet sections; the other categories give counter-evidence examples without that paired structure. The images are examples, not records of a real customer, transaction, issuer decision, or guaranteed outcome.

Both raw Markdown captures contain **66 image embeds pointing to 64 distinct paths**. The May capture points to 64 locally saved `raw/assets/stripe-disputes-evidence-*.png` files; the November capture points to Stripe CDN URLs. The raw text and URL changes do not establish that the local and remote image bytes or pixels are identical. No remote-image download or visual comparison is evidenced here.

## Categories and Packet Examples

| Category | Illustrative packet content |
| --- | --- |
| **Credit not processed** | **Approved** subsection: original transaction, refund details, processor log, merchant account statement. **Denied** subsection: reason for denying a refund, customer communication showing the policy before chargeback, and terms shown at checkout. |
| **Duplicate** | **Approved** subsection: investigation summary, valid and refunded transactions, refund details, processor log, and bank statement. **Denied** subsection: investigation and differences between two intentional purchases, time gap, and separate purchase confirmations. |
| **Fraudulent** | Investigation summary; IP and location compared with billing address and past orders; a fraud risk score **if available** and verification details; available AVS, CVV, and 3DS evidence; conclusion. The example's low-risk score is illustrative, not proof of authorization. |
| **General** | Order confirmation and receipt with amount, method, and transaction ID; pricing and tax presentation before payment; POS or system logs; relevant customer communication, including billing concerns and pre-purchase price disclosure. |
| **Product not received** | Physical goods: delivery terms, notifications, signature/photo where available, marked delivery timing, relevant carrier and tracking information. Digital goods: delivery/activation terms, messages, download or access logs, activation and login records. Services: service terms, scheduling and completion messages, receipt, and session/fulfillment logs. |
| **Product unacceptable** | Quality/functionality evidence against advertised features and specifications; product listing and marketing at time of purchase; accepted terms and refund policy; support and resolution records. |
| **Subscription canceled** | Terms agreed at signup, including renewal/cancellation/refund policy; actual cancellation records and methods; renewal notices, receipts, billing history, and usage or communication logs relevant to the disputed period. |

These are examples to adapt to the actual dispute reason and available records. A category row is not a required universal checklist or evidence of an issuer's eventual decision.

## Packet Patterns

For a **fraudulent** case, the page illustrates a sequence from investigation summary through location, any available risk score, customer verification, and conclusion. A risk score, AVS/CVV result, or completed 3DS flow should be described accurately for the actual payment; the sample does not prove those signals exist or establish liability shift.

For **product not received**, the useful proof differs by product type: a physical shipment needs relevant delivery and tracking records; a digital item needs access or activation records; a service needs scheduling, completion, and fulfillment records. For **subscription canceled**, use the terms and actual cancellation or usage history for the disputed period, rather than assuming a cancellation never occurred.

The page links Dashboard and API dispute-management routes but does **not** state file-format, size, page-limit, one-file-per-type, or final-submission rules. Use [[source-stripe-disputes-responding]] and [[source-stripe-disputes-best-practices]] for those channel and dispute-specific limits.

## Related Pages

- [[disputes]] — dispute concept
- [[stripe]] — provider overview
- [[source-stripe-disputes-categories]] — evidence fields by category
- [[source-stripe-disputes-reason-codes]] — reason-code guidance
- [[source-stripe-disputes-responding]] — response and submission workflow
- [[source-stripe-disputes-best-practices]] — formatting and limits

## Raw Sources

- [[raw/stripe-disputes-visual-evidence-2026-11-07|Stripe sample evidence packets, 2026-11-07 capture]] — remote Stripe CDN image references, not locally downloaded here
- [[raw/stripe-disputes-visual-evidence-2026|Stripe sample evidence packets, 2026-05-09 capture]] — locally saved image references in `raw/assets/stripe-disputes-evidence-*.png`
