---
title: "Adyen Balance Platform API v2 PATCH recurring top-up"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/balanceAccounts/(balanceAccountId)/recurringTopUps/(topUpId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/patch/balanceAccounts/(balanceAccountId)/recurringTopUps/(topUpId)/2026-11-02.md"
tags: [adyen, balance-platform, issuing, recurring-top-ups, configuration-api]
---

## Overview

This 2026-11-02 [[adyen]] Balance Platform API v2 TEST reference describes `PATCH /balanceAccounts/{balanceAccountId}/recurringTopUps/{topUpId}`, updating an existing recurring top-up configuration. Required path IDs select the balance account and its separate recurring top-up. Its listed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`; `latest` does not prove current version, live access or account eligibility. The page links to the separate Issuing management guide; see [[adyen-issuing]].

## Key takeaways

- The request-body table marks `description`, `referenceForBeneficiary`, `status`, `topUpAmount` and `trigger` **No**; it does not separately state whole-body requiredness. `topUpAmount` may specify fixed or target amount, and `trigger` may specify schedule or balance threshold. The request table lists threshold currency/value as **No**; the 200 response marks those children **Yes** within an included threshold. Amounts are in minor units. A description longer than 140 characters is cut off (raw lines 16–36, 54–72).
- `status` permits `active` (enabled for pulling funds) and `inactive` (disabled and cannot be triggered); its table description says an omitted value defaults to active. `referenceForBeneficiary` is sent to the recipient and related transfer webhooks and permits letters and digits. These are configuration descriptions, not proof of a triggered pull or booked balance (raw lines 26–34, 58–59).

> [!warning] Contradiction
> The request table says omitted `status` defaults to `active`, but the request example supplies only `description` and its paired 200 example returns `status: inactive` (raw lines 28, 38–45, 152–179). The capture does not resolve whether omission during PATCH preserves an existing inactive status or applies the stated default. Do not infer a status transition from the example.

- A 200 says the update request succeeded. The response marks `counterparty` (including funding `transferInstrumentId`), `description`, top-up `id`, `topUpAmount` and `trigger` required; `status` and beneficiary reference are optional. Within optional fixed or target amount objects, currency/value are marked required; within optional schedule, `type` is marked required, and within `trigger`, threshold/currency/value are marked required. Schedule descriptions give weekdays, weekly or monthly pulls at 07:00 in the balance account's local time zone, and a `null` default for continuous monitoring (raw lines 46–72). The response example's amount and schedule do not establish an actual transfer (raw lines 150–179).
- Errors listed are 400 request-reading, 401 authentication, 403 permission and 422 validation (raw lines 75–148). The 422 examples show currency mismatch, disabled DirectDebitTopUp property, inactive account holder, invalid funding transfer instrument, missing `receiveFromTransferInstrument` capability and missing sweep routes (raw lines 222–293). They illustrate possible validation failures, not a universal eligibility checklist. The page gives no idempotency, deletion, propagation timing, asynchronous transfer outcome, reversal or bank-credit contract. A configuration update is distinct from a direct-debit pull and later booked credit.

## Detail locators

- Endpoint, TEST v2 host, path IDs and request fields: raw lines 5–36.
- Request and response examples plus success schema: raw lines 38–72, 150–179.
- Error schemas and examples: raw lines 75–148, 181–293.
- Omitted-status wording versus paired example: raw lines 28, 38–45 and 152–179.

## Related

- [[adyen-issuing]] — recurring top-up and funding context.
- [[source-adyen-docs-issuing-add-manage-funds-top-ups-manage-recurring-top-ups]] — separate management guide.
- [[source-adyen-api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-balanceaccount-recurringtopup-updated]] — separate configuration-update event, distinct from transfer and transaction outcomes.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/patch/balanceAccounts/(balanceAccountId)/recurringTopUps/(topUpId)/2026-11-02|PATCH recurring top-up reference, captured 2026-11-02]]