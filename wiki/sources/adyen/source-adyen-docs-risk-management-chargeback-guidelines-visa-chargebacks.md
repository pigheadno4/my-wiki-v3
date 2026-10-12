---
title: "Adyen Visa Chargebacks Guide"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/visa-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/visa-chargebacks/2026-09-15.md"
tags: [adyen, visa, chargebacks, disputes, rdr]
---

## Overview

This [[adyen]] guide describes Visa dispute handling through two default chargeback workflows and the separate Rapid Dispute Resolution (RDR) refund workflow. **Allocation** covers fraud and authorization cases; **Collaboration** covers consumer disputes and processing errors. RDR resolves eligible customer claims by refund before they become a chargeback, although Adyen's interface refers to RDR-qualified transactions as chargebacks. The workflows and deadlines below are the guide's 2026-09-15 snapshot, not a determination of a specific case's present deadline or outcome. See [[adyen-risk-management]].

## Key takeaways

- In either default flow, Notification of Chargeback can follow a payment becoming Settled or Refunded; the chargeback stage debits the merchant account. After review, the merchant can accept, closing defense, or defend with reason-specific documents through Customer Area or the Disputes API. An order summary alone is insufficient. Once Adyen forwards submitted documents, they cannot be changed or supplemented later.
- The guide's defense window is **9 days** for disputes opened from 21 July 2025 on payments processed locally in the US or Canada; it states **18 days** for earlier US/Canada disputes and all other regions. Without 3DS liability shift, Adyen says defense is difficult and recommends submitting evidence only when requirements are met. These date and locality conditions matter when applying the window.
- **Allocation:** defending does not immediately return the chargeback amount. Adyen automatically forwards a pre-arbitration case to the bank; if accepted, chargeback reversal is final. If declined, the chargeback remains. For the guide's listed valid reasons to dispute a pre-arbitration loss, contact the Adyen Disputes Team within five days of that status.
- **Collaboration:** the disputed amount returns after evidence upload, but the cardholder's bank can send pre-arbitration within the guide's 30–32-day window. A case is accepted when response time expires; direct merchant accept/decline requires Adyen configuration and approval. Declining can lead to scheme arbitration and significant costs. A second chargeback is final and permits no new defense documents; scheme arbitration can impose the guide's USD 600 filing fee on the losing party in addition to the dispute amount.
- **RDR:** the separate, rule-conditioned process refunds an eligible claim before a chargeback. The guide says it cannot be defended, carries no chargeback or interchange fees, and is excluded from the Visa dispute count. Its indicator is visible in Customer Area and reports; the `rapidDisputeResolution` webhook field requires Disputes API use, configured dispute webhooks, and enabling that additional setting.

## Detail locators

- **Opening and Overview**, raw lines 19–46 — Allocation, Collaboration, and separate RDR scope and stage maps.
- **Visa Allocation Flow**, raw lines 48–102 — notification, debit, defense route, dated deadline, document finality, pre-arbitration outcomes, five-day escalation, and reversal.
- **Visa Collaboration flow**, raw lines 104–165 — defense, earlier refund of disputed amount, pre-arbitration timing and approval, second chargeback, and arbitration fee.
- **Visa Rapid Dispute Resolution flow**, raw lines 167–209 — refund-before-chargeback treatment, inability to defend, fee/count treatment, and conditional indicator surfaces.
- **Reason codes and guidelines**, raw lines 210–215 — Visa reason-code and defense-requirement navigation.

## Related

- [[adyen-risk-management]]
- [[source-adyen-docs-risk-management-disputes-api]]

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/visa-chargebacks/2026-09-15|Adyen Visa chargebacks guide (2026-09-15 snapshot)]]
