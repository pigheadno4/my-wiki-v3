---
title: "Adyen Issuing: raise cardholder disputes"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/raise-disputes"
raw_files:
  - "adyen/docs/issuing/raise-disputes/2026-09-15.md"
tags: [adyen, issuing, disputes, chargebacks, cardholders]
---

## Overview

This 2026-09-15 Adyen Issuing guide describes how a **card-issuing platform** raises disputes on behalf of cardholders for captured payments made with Adyen-issued cards. It covers duplicate charges, fraud and non-delivery, plus draft submission, dispute status webhooks and dispute-account fund movements. The platform may provide a cardholder UI backed by the Raise disputes API, or upload a dispute package through a Customer Area **pilot** feature. This issuer-side process is distinct from a merchant's acquiring-side dispute defense. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The guide says cardholders can raise a maximum of **35 disputes over their possession of their card**. Duplicate-charge and fraud disputes have a **120-day window from the authorised transaction date**; non-delivery has a **120-day window from when goods or services should have been delivered**. These are source-stated windows, not proof that any claim is eligible or will win.
- The platform locates the captured payment's `transactionId`, raises a `duplicate`, `fraud` or `notDelivered` dispute, can attach supporting information, and presents it to the cardholder. For suspected loss or theft, the guide directs the platform to close the card. The API path calls for moving the reviewed draft to `submitted` or `closed`; Customer Area bulk upload submits automatically after processing. Requirements include the Bank disputes webservice role, Manage issuing disputes Customer Area role for viewing, and dispute plus transfer webhooks.
- `balancePlatform.dispute.created` provides the dispute ID and initially `draft` status for API-raised disputes. A draft can be edited. Once a dispute is `closed`, it **cannot be edited, reopened or submitted**; closure can also follow a deadline, Adyen ineligibility decision or scheme rejection. Submission sends the case to the card scheme, with later status changes on `balancePlatform.dispute.updated`.
- `chargeback` means funds were returned to the **Disputes balance account**; it is not the final `won` state. `won` means the acquirer can no longer challenge, with this guide listing Mastercard's challenge period as 45 days and Visa's as 30 days after chargeback. `secondPresentment` means funds were returned to the acquirer.
- Correlate the capture `transactionId`, Adyen dispute `id`, and ARN. A chargeback or second presentment mutates the Disputes balance account and emits `balancePlatform.transfer.created`; the guide maps dispute `chargeback` to transfer `category: issuedCard, type/status: chargeback`, while dispute `secondPresentment` maps to transfer `type/status: secondChargeback`. The ARN appears in the transfer webhook's `reference` and the accounting report. The related [[source-adyen-docs-issuing-webhook-types]] catalog (its raw lines 79 and 88) instead lists second-chargeback transfer `type: chargeback`, `status: secondChargeback`, and `secondChargeback` as a dispute-updated status. This Raise disputes guide uses dispute `secondPresentment` and transfer `type/status: secondChargeback` (its raw lines 119 and 136). The captured guides conflict on transfer `type` and dispute-status naming; verify observed payloads before relying on either mapping.

## Detail locators

- Platform duty, dispute paths, captured-payment scope and requirements: raw lines 19–45.
- Workflow and card closure instruction: raw lines 47–67.
- 35 limit, reason-specific 120-day triggers, supporting information: raw lines 69–94.
- Draft, closed, submitted, chargeback, won and second-presentment meaning: raw lines 96–119.
- Correlation IDs, balance-account movements and transfer mapping: raw lines 121–138.

## Related

- [[adyen]] — provider.
- [[adyen-issuing]] — Issuing concept and source route.
- [[source-adyen-docs-issuing-raise-disputes-not-delivered]] — non-delivery dispute detail.
- [[source-adyen-docs-issuing-manage-cards]] — card status and closure details.
- [[source-adyen-docs-issuing-webhook-types-payment-events]] — separate payment webhook events.

## Raw Sources

- [[raw/adyen/docs/issuing/raise-disputes/2026-09-15|Adyen Issuing raise-disputes guide, captured 2026-09-15]]
