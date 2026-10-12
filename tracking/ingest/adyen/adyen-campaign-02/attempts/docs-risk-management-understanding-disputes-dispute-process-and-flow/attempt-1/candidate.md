---
title: "Dispute flow | Adyen Docs"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/understanding-disputes/dispute-process-and-flow"
raw_files:
  - "adyen/docs/risk-management/understanding-disputes/dispute-process-and-flow/2026-09-15.md"
tags: [adyen, disputes, chargebacks, risk-management, webhooks]
---

## Overview

This Adyen webpage explains the merchant-facing dispute flow: how a cardholder's issuer initiates a chargeback, when Adyen debits the merchant, how the merchant may accept or defend, and how to follow later stages in Customer Area or dispute webhooks. The page says flows vary by card scheme and payment method. This is a 2026-09-15 documentation snapshot whose own `last_modified` metadata is 2024-04-12, not independent current scheme-policy or merchant-account evidence.

## Key takeaways

- A Notification of Fraud and a Request for Information are optional early stages and do not withdraw funds at that stage. A Notification of Chargeback marks the defense period; depending on the payment method, the chargeback debit may occur days after that notification or after a defense. At the Chargeback stage, the disputed amount is withdrawn. Adyen's overview also says it debits a chargeback processing fee.
- The merchant can accept or defend through Customer Area or the Disputes API. A defense requires supporting documents. Once Adyen receives and forwards documents at Information Supplied, they can no longer be changed. Accepting a chargeback or missing the document deadline makes the Chargeback stage final in the described flow.
- Chargeback Reversed means the disputed amount returns to the merchant, but the webhook table warns that `CHARGEBACK_REVERSED` can remain `Pending` during issuer review and may be followed by a second chargeback; a `Won` final status is specifically qualified there to the Visa allocation flow after issuer acceptance in pre-arbitration. Do not treat a returned amount or that event alone as a final win.
- Pre-arbitration applies only to some flows. Merchant self-acceptance or self-decline requires eligibility, a supported dispute flow, and additional Adyen configuration and approval. Acceptance loses the case and brings a second chargeback; declining can lead to scheme arbitration. The page says an issuer-favoring arbitration decision can add a fee of up to USD 600 to the second chargeback. A second chargeback is final and does not permit new defense documents.
- Following dispute events by webhook requires the Standard webhook with dispute events enabled. Customer Area visibility and dispute-webhook management depend on the listed roles. Status and event names are navigation into the raw tables; they are not guarantees that every stage or webhook occurs for every dispute.

## Detail locators

- `## Requirements` — online-payments prerequisite, role-specific Customer Area access, Standard webhook setup, and Customer Area versus Disputes API management routes.
- `## Dispute flow overview` — cardholder, issuer, Adyen, and merchant roles; debit, defense, issuer review, fund return, and monitoring routes.
- `## Dispute stages` — optional NOF/RFI, NoC defense start, Chargeback, Information Supplied, Chargeback Reversed, conditional pre-arbitration and arbitration, and final Second Chargeback.
- `## Follow a dispute through the flow` / `### Customer Area` — notifications, payment lifecycle journal entries, dispute details/history, dashboard, and example statuses.
- `### Dispute webhooks` — event codes and example statuses for fraud, information requests, chargeback, reversal, pre-arbitration, arbitration, deadline expiry, and issuer comments.

## Related

- Company: [[adyen]]
- Provider concept: [[adyen-risk-management]]
- Generic background: [[disputes]]
- Related event concept: [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/risk-management/understanding-disputes/dispute-process-and-flow/2026-09-15|2026-09-15 snapshot — Adyen dispute flow]]
