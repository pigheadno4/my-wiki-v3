---
title: "Adyen Dispute Webhooks"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/disputes-api/dispute-notifications"
raw_files:
  - "adyen/docs/risk-management/disputes-api/dispute-notifications/2026-09-15.md"
tags: [adyen, disputes, chargebacks, webhooks, risk-management]
---

## Overview

This [[adyen]] documentation snapshot catalogs dispute events delivered through a configured Standard webhook. It describes event codes and possible dispute statuses, reference fields, setup for optional reference data, and example payloads. Merchants can use the events to alert staff and manage disputes through the Disputes API or Customer Area; the page does not itself establish account-specific eligibility, a successful defense, or final funds movement. See [[adyen-risk-management]] for the provider route and [[disputes]] for cross-provider context.

## Key takeaways

- `eventCode` identifies the dispute event. `pspReference` identifies the dispute across its events, while `originalReference` identifies the disputed payment. Most messages can include `additionalData.disputeStatus`; Adyen says that status is absent for disputed payments processed in Brazil. Do not require it for every event or geography.
- The merchant must configure a Standard webhook and select dispute events; some event types need additional setup. For `CHARGEBACK_REVERSED`, `SECOND_CHARGEBACK`, `PREARBITRATION_WON`, and `PREARBITRATION_LOST`, the guide gives a Customer Area additional setting to include the payment's `originalReference` alongside the dispute `pspReference`. Do not assume the optional reference is present for those events before that setting is enabled.
- `NOTIFICATION_OF_CHARGEBACK` marks the start of the defense period: the merchant can evaluate and begin a defense then, without waiting for `CHARGEBACK`. `INFORMATION_SUPPLIED` means defense documents were uploaded or Adyen auto-defended; it is not a win signal.
- `CHARGEBACK_REVERSED` means the disputed amount was transferred back after defense, but the status can remain `Pending` while the issuer reviews, and a second chargeback can still cause a loss. The page limits a final `Won` status at that stage to the Visa allocation flow when the issuer accepts the defense in pre-arbitration.
- Self-handled pre-arbitration events depend on eligibility and a supported dispute flow. `PREARBITRATION_OPEN` says accepting or declining such a case requires additional configuration and Adyen approval. The event/status table distinguishes later issuer withdrawal, scheme arbitration, defense-period end, and issuer-response expiry; their possible status values are in the raw.

## Detail locators

- **Message identity, status field, Brazil limitation, and requirements:** raw lines 19–44.
- **Event-code meanings and possible statuses:** raw lines 46–81, including notification, reversal, pre-arbitration, arbitration, deadlines, and issuer comments.
- **Standard webhook subscription and original-reference setting:** raw lines 83–99.
- **Per-event example payloads and conditional notes:** raw lines 101–665. These are examples, not universal payload guarantees.

## Related

- [[adyen]]
- [[adyen-risk-management]]
- [[adyen-webhooks]]
- [[disputes]]
- [[source-adyen-docs-risk-management-disputes-api-disputes-api-reference]]

## Raw Sources

- [[raw/adyen/docs/risk-management/disputes-api/dispute-notifications/2026-09-15|Adyen Dispute webhooks — collected 2026-09-15]]
