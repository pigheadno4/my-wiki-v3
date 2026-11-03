---
title: "Adyen Balance Platform API v2 GET account-holder transaction rules"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/accountHolders/(id)/transactionRules"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/accountHolders/(id)/transactionRules/2026-11-02.md"
tags: [adyen, balance-platform, issuing, transaction-rules, api]
---

## Overview

This 2026-11-02 [[adyen]] Balance Platform Configuration API v2 TEST reference describes `GET /accountHolders/{id}/transactionRules`: a read of transaction rules associated with the account holder identified by the required path `id`. Its listed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`. The `latest` documentation URL does not establish current version, live access or account eligibility. See [[adyen-issuing]] for the rule context.

## Key takeaways

- The only listed input is the required account-holder path `id`; the page shows no query or request-body parameters (raw lines 12–18). A 200 says the request succeeded and may return an optional `transactionRules` array. This read does not create, update, activate or apply a rule to a specific transaction (raw lines 19–27).
- Returned rule objects describe their own resource scope through `entityKey` (`entityType` and `entityReference`), distinct rule `id`, merchant `reference`, `type`, `status`, `requestType`, `ruleRestrictions`, `interval`, `outcomeType`, `score`, start/end dates and optional override ID. The array is optional; within a returned rule, the schema marks `description`, `entityKey`, `interval`, `reference`, `ruleRestrictions` and `type` **Yes**. The children of `entityKey` are individually **No** (raw lines 27–47, 73–76). These are response-field markers, not GET request requirements.
- The rule schema lists `blockList`, `maxUsage`, `velocity` and `bypass` types; `bypass` calls for an `overridesRule` ID and empty restrictions. For velocity/maxUsage, `aggregationLevel` must be no higher than `entityKey` and defaults to `paymentInstrument`. `requestType` defaults to `authorization`; `outcomeType` defaults to `hardBlock`, with `scoreBased` restricted to -100 through 100 and disallowed for `bankTransfer`, while `enforceSCA` is only allowed for `authentication` (raw lines 28, 42–46, 73, 76).
- `interval.type` is marked required within the returned `interval`. Rolling/sliding intervals require `duration`, capped at 90 days or equivalent. The response descriptions give defaults for day of month (1), day of week (Monday), time of day (00:00:00) and time zone (UTC), while fixed daily/weekly/monthly reset wording uses CET. The listed `interval.dayOfWeek` values omit Saturday; consult the table as captured rather than assuming the full week (raw lines 35–41).
- The response schema says supplied `startDate` causes **creation** with active status, and omitted `endDate` leaves evaluation until inactive. These describe rule lifecycle fields; this GET response is a readback, not an activation or outcome acknowledgement (raw lines 30, 74–75). Restrictions and operations occupy raw lines 47–72.
- Errors are documented as 400, 401, 403, 422 and 500 (raw lines 79–176). The generic 422 and 500 JSON examples discuss changing a payment instrument's balance account and creating a payment instrument, respectively, so they do not define failures specific to this GET (raw lines 219–244). No idempotency, deletion, propagation or asynchronous outcome is specified here. A returned rule does not prove that it was evaluated for a transaction or that an authorization, bank transfer, booking, settlement or bank receipt occurred.

## Detail locators

- Endpoint, purpose, TEST server and required path ID: raw lines 5–17.
- Response object identities, interval/outcome defaults and conditional fields: raw lines 19–47, 73–76.
- All available rule restrictions and operations: raw lines 47–72.
- Error response tables and generic examples: raw lines 79–244.

## Related

- [[adyen-issuing]] — rule and Issuing context.
- [[source-adyen-api-explorer-balanceplatform-latest-post-transactionrules]] — separate creation endpoint, with its own request contract.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/accountHolders/(id)/transactionRules/2026-11-02|GET account-holder transaction rules reference, captured 2026-11-02]]