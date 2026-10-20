---
title: "Adyen Issuing: Webhook types"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/webhook-types"
raw_files:
  - "adyen/docs/issuing/webhook-types/2026-09-15.md"
tags: [adyen, issuing, webhooks, transfers, disputes]
---

## Overview

This Adyen Issuing webhook catalog was last modified in 2020 and captured on 2026-09-15. It maps balance-platform events such as resource changes, issued-card payments/refunds, fund movements and raised disputes to webhook families and event `type` values. Some webhook families also expose `data.status` to distinguish lifecycle states; receiving an event type alone is not proof of a final payment, booked funds or dispute outcome.

## Key takeaways

- Configuration webhooks cover account holders, balance accounts, payment instruments and network tokens. The network-token `created` event starts **inactive**; `updated` can indicate **active**, **suspended** or **closed**. A separate balance webhook reports balance-account balance changes. See raw lines 39–60.
- Transfer `created` reports a request to credit or deduct a balance account, while transfer `updated` reports a status change. The table identifies payment, bank transfer, chargeback and second-chargeback events by `category`, `type` and sometimes `status`. See raw lines 62–79.
- Dispute `created` and `updated` report raised Issuing-card dispute and status changes; report `created` announces a generated report ready for download. The status lists in this catalog are a dated snapshot, not proof of a particular dispute outcome. See raw lines 81–96.
- **Payment webhooks are deprecated; the page directs integrations to transfer webhooks instead.** The listed older incoming/outgoing transfer and payment events remain as historical reference. See raw lines 98–109.

## Source and related-guide differences

- For a second chargeback, this catalog's transfer table gives `category: issuedCard`, `type: chargeback`, `status: secondChargeback` (raw line 79). The related Issuing Raise disputes guide gives `type: secondChargeback`, `status: secondChargeback` for `secondPresentment` ([[raw/adyen/docs/issuing/raise-disputes/2026-09-15|related Raise disputes raw line 136]]). The captured guides disagree on the transfer `type`; verify actual payloads before relying on either mapping.
- This catalog's dispute-updated row lists `secondChargeback` as a possible dispute status (raw line 88), while that related dispute-lifecycle guide calls the status `secondPresentment` ([[raw/adyen/docs/issuing/raise-disputes/2026-09-15|related Raise disputes raw line 119]]). Keep dispute status distinct from transfer `type` and `status`; the snapshots do not reconcile the naming.
- The opening subscription list names Configuration, Payment method, Transfer, Dispute, Negative balance warning and Report (raw lines 28–35), while the detailed sections also include Balance and do not detail Payment method or Negative balance warning (raw lines 39–109). Treat it as a navigation catalog, not an exhaustive subscription setup guide.

## Detail locators

- Event categories and configuration/balance families: [[raw/adyen/docs/issuing/webhook-types/2026-09-15|raw lines 19–60]].
- Transfer event mapping and dispute/report families: [[raw/adyen/docs/issuing/webhook-types/2026-09-15|raw lines 62–96]].
- Deprecated payment webhook table and scenario links: [[raw/adyen/docs/issuing/webhook-types/2026-09-15|raw lines 98–125]].

## Related

- [[adyen-issuing]] — Issuing balance-platform model and source catalog.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/issuing/webhook-types/2026-09-15|Issuing webhook types (captured 2026-09-15)]]
