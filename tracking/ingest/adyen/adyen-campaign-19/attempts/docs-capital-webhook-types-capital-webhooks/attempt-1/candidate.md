---
title: "Grant lifecycle-related events | Adyen Capital"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/webhook-types/capital-webhooks"
raw_files:
  - "adyen/docs/capital/webhook-types/capital-webhooks/2026-09-15.md"
tags: [adyen, capital, webhooks, grants, lifecycle]
---

## Overview

This 2026-09-15 Adyen Capital reference maps offer and grant-lifecycle events to Capital webhooks and sample payloads. It identifies account holder, dynamic/static offer, grant, grant account and balance account at different grains, and points to separate fund-transfer webhooks for money movement. It is a schema/event guide, not evidence that an event was delivered for a real user, grant funds were booked, a bank received money or a debt was finally settled. See [[adyen]], [[adyen-capital]], and [[adyen-webhooks]].

## Key takeaways

- The event list spans dynamic/static offers, requested, assessed, reviewing, approved, rejected, canceled, pending, failed, active, renewal-eligible, repaid, revoked and written-off stages; detailed samples are given only for some of them. Do not infer an undocumented payload or event type for the unsampled stages (raw lines 19–47).
- Dynamic offer creation uses `balancePlatform.capital.dynamicOffer.created` and includes account-holder/offer IDs, minor-unit minimum/maximum, terms and validity dates. Static offer creation uses `balancePlatform.balanceAccountHolder.capitalOffer.created` and adds fixed amount, fee, basis-point repayment and 30-day threshold fields. An offer-created event is not a grant request or approval (raw lines 49–157).
- Offer selection through component or API creates a `balancePlatform.grants.created` grant with `Requested`; `grantOfferId` identifies the selected offer, `counterparty.accountHolderId` identifies the user, and `grantAccountId` is distinct from grant `id` and, later, `counterparty.balanceAccountId`. Reviewing/Approved/Pending/Active/Repaid use `balancePlatform.grants.updated` with stage-specific `status.code` (raw lines 159–383, 437–480). The sample zero balances at Requested/Reviewing/Approved/Pending are test examples, not an account ledger.
- Reviewing can require additional business data at a typical EUR 25,000 exposure threshold and shows an unresolved `AnaCreditCapabilityRule` action. Approved follows secondary review but is before payout. Pending still awaits required actions, grant transaction booking and any security cooldown; the page then points to separate fund-transfer webhooks at disbursement. Active is described after disbursement with principal plus fee total, but a grant-status event alone should be reconciled to the corresponding transfer/booking evidence rather than treated as a beneficiary-bank receipt (raw lines 199–383).
- Renewal eligibility is an `Active` grant update with `renewal.eligible` and minimum amount, not a new grant automatically funded (raw lines 386–435). Repaid is described after the last repayment and corresponding transfer booking, with zero fee/principal/total in the grant event; test sample values do not prove final debt state for a named grant (raw lines 437–480). The sample renewal minimum (9,440,625 minor units) exceeds the example active principal (629,375), so treat sample numbers as illustrative rather than a reusable threshold (raw lines 368–377, 412–427).

## Detail locators

- Event inventory and offer identifiers/amounts: raw lines 19–157.
- Requested/Reviewing/Approved grant status and identifiers: raw lines 159–287.
- Pending/Active and separate disbursement transfer route: raw lines 289–384.
- Renewal and Repaid semantics/samples: raw lines 386–480.

## Related

- [[adyen-capital]]
- [[source-adyen-docs-capital-grant-lifecycle-and-status]]
- [[source-adyen-docs-capital-webhook-types-fund-transfers-webhooks]]

## Raw Sources

- [[raw/adyen/docs/capital/webhook-types/capital-webhooks/2026-09-15|Pinned Adyen Capital grant lifecycle webhooks]]
