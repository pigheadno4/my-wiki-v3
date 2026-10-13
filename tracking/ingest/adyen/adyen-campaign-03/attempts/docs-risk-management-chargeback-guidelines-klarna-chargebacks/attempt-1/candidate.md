---
title: "Klarna chargebacks | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/klarna-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/klarna-chargebacks/2026-09-15.md"
tags: [adyen, klarna, disputes, chargebacks, risk-management]
---

## Overview

This Adyen guide describes the Klarna dispute route for merchants using Klarna for physical-goods business models: shopper complaint, Dispute Notification in the pre-November 2026 flow, mandatory Request for Information (RFI), defense submission, Klarna review, and possible first chargeback. Klarna's upfront-payment and non-payment-risk protection is conditional on meeting its order-fulfillment rules; failure to follow Klarna scheme rules can lead to a chargeback. This is a 2026-09-15 documentation snapshot, not proof of a merchant's current Klarna eligibility, a live dispute, or current scheme terms.

## Key takeaways

- The captured guide announces a phased Klarna dispute-system change: from **1 November 2026**, Dispute Notification is removed and disputes go directly to RFI; the standard RFI response window rises from **14 to 21 days for most reason codes**, while `unauthorized_purchase` remains **7 days** and `high_risk_order` **96 hours**. It also announces PDF-only evidence files, at most **7 MB per file**. Further changes are described as coming in March 2027. The later sections still describe the earlier Dispute Notification and 14-day standard RFI flow, so these dated instructions must be selected by the applicable phase rather than combined.
- In the earlier flow, a Dispute Notification gives the merchant **21 days** to contact the shopper and resolve the complaint, or **7 days** for returns; unauthorized-purchase and high-risk-order complaints can move to RFI much sooner. At RFI, Klarna requires the requested information. The guide's earlier standard RFI deadline is **14 days**, with the same 7-day and 96-hour exceptions. An unanswered RFI can cause a chargeback deducted from the next payable batch.
- A merchant defending an RFI has **one attempt** to submit all necessary evidence. The guide routes the merchant to reason-specific templates, PDF conversion, and submission through the Disputes API or Customer Area; submitted documents cannot later be changed.
- At Information Supplied, Adyen forwards the documents and sends an `INFORMATION_SUPPLIED` webhook. Klarna decides the case: if it accepts the defense, the guide says no further journals are booked and that is final; if it rejects it, the first Chargeback journal and webhook follow, the merchant account is debited, and that chargeback cannot be defended. The page also says stop-request emails were discontinued from 1 May 2023 and routes `high_risk_order` cases through RFI instead.

## Detail locators

- Introductory paragraphs and `Key changes from November 2026` — conditional guarantee, phased timing, removed notification, revised RFI windows and PDF/7 MB evidence rule.
- `## Dispute Notification` — earlier-phase shopper contact windows, expedited reasons, webhook and Customer Area labels, and reason codes.
- `## Request for Information`, `### Request for Information reason codes`, and `### Respond to an RFI` — mandatory information, earlier-phase deadlines, one-shot defense, templates and PDF submission.
- `## Information Supplied` and `## 1st Chargeback` — Adyen forwarding, Klarna decision, journals, webhooks, account debit and finality.
- `## Managing chargebacks` — API and Customer Area routes and discontinued stop-request email notice.

## Related

- Company: [[adyen]]
- Provider concept: [[adyen-risk-management]]
- Generic background: [[disputes]]

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/klarna-chargebacks/2026-09-15|2026-09-15 snapshot — Klarna chargebacks and phased dispute changes]]
