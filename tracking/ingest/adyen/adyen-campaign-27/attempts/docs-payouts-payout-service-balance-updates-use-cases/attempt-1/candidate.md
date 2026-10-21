---
title: "Adyen Payout Service balance-webhook setting use cases"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/balance-updates/use-cases"
raw_files:
  - "adyen/docs/payouts/payout-service/balance-updates/use-cases/2026-09-15.md"
tags: [adyen, payout-service, balance-webhooks, balance-platform, pilot]
---

## Overview

This Payout Service page (modified and captured 2026-09-15) gives **example** Configuration API settings and test `balancePlatform.balanceAccount.balance.updated` events for thresholds at balance-platform, account-holder and individual balance-account scope. It marks balance webhooks as a **limited-availability pilot** whose processes and documentation may change. These examples show notification configuration, not a payout request, booked transfer, bank receipt or live feature access. See [[adyen]] and [[adyen-payouts]].

## Key takeaways

- **Scope and conditions differ:** The first example targets a `balancePlatform` and uses USD `balance` `lessThan` 500000 for any account's current balance dropping below the stated USD 5000. The second targets an `accountHolder` and uses USD `balance` `lessThanOrEqual` 500000, including equality at the stated USD 5000. The third targets each specific `balanceAccount` separately, uses `available` rather than current `balance`, and uses `lessThan`. Preserve the target, balance type, comparator and currency together; the examples are not interchangeable.
- **Event interpretation:** The sample events have `environment: test` and distinguish `balances.available`, `pending`, `reserved` and `balance`. Their values illustrate threshold matching for the configured metric, not movement of funds or delivery of a notification in a live account.
- **JPY example conflict:** The third use case describes an available-balance threshold below **1000** in each foreign currency and labels the event “below JPY 1000,” yet its JPY setting uses `conditions.value: 100000` and the sample event uses `balances.available: 95000`. The page does not reconcile those figures. The separate Adyen currency-code reference lists JPY with zero decimals and says JPY 10 is submitted as 10 minor units for its stated API scope; this raises a concrete unit concern but does not, by itself, establish the correct balance-webhook setting. Verify JPY units and intended threshold with Adyen before using this example.

## Detail locators

- Pilot notice and example-only scope: pinned raw lines 15-24.
- Platform-wide current-balance example and TEST webhook: pinned raw lines 26-95.
- Account-holder current-balance example with inclusive threshold: pinned raw lines 97-167.
- Per-balance-account available-balance example and JPY numerical conflict: pinned raw lines 169-239.
- Separate Adyen currency reference for JPY zero-decimal/minor-unit context: [[source-adyen-docs-development-resources-currency-codes]], pinned raw lines 83 and 166-172.

## Related

- [[adyen-payouts]] — Payout Service parent concept and reciprocal route.
- [[adyen-currencies-and-fx]] — currency-unit reference; balance-webhook JPY example requires clarification.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/balance-updates/use-cases/2026-09-15|Payout Service balance-webhook use cases, captured 2026-09-15]]
