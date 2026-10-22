---
title: "Adyen Payout Service transaction rules"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/transaction-rules"
raw_files:
  - "adyen/docs/payouts/payout-service/transaction-rules/2026-09-15.md"
tags: [adyen, payouts, payout-service, transaction-rules, risk, pilot]
---

## Overview

This 2022-modified, 2026-09-15-captured [[adyen]] Payout Service-path guide describes rules that evaluate **third-party bank-account or card payout requests** and can decline requests meeting defined conditions. It labels **transaction rules for business accounts** a **limited-availability pilot** whose processes and documentation may change; the page does not prove this feature is enabled for a particular balance platform. A rule decision belongs to payout-request evaluation, not to fund booking, settlement or beneficiary receipt. [[adyen-payouts]]

## Key takeaways

- A rule defines **criteria**, **conditions** and an **outcome**. The criteria include request type, rule type, time interval and one balance-platform resource. The page says to set request `type` to **bankTransfer** for third-party payouts even while its overview includes cards; do not infer a distinct card request type or guaranteed card-rule coverage from this page alone. See raw lines 24–53.
- **Blocklist** tests the current request against conditions; **velocity** uses accumulated previous payouts within an interval; **bypass** skips a specified rule for an entity and requires that rule's ID. Bypass is not a general “allow” outcome and does not disable other applicable hard-block rules. Per-transaction, fixed, rolling and sliding windows have different reset/decision behavior. See raw lines 55–80 and 145–157.
- A rule applies to one **balance account**, **account holder** or **balance platform**; each scope expands differently. Velocity totals nevertheless aggregate at the **balance-account level**, and amount aggregation converts payout amounts to the holder/platform default currency. See raw lines 82–96.
- Rule restrictions include counterparty, account/country, description, priority, available-balance percentage, matching-transaction count and total amount. A rule with multiple conditions applies only when **all** match; among multiple applicable rules, **any one** matching `hardBlock` declines the request. The only selectable outcome described is `hardBlock`, not an approval action. See raw lines 98–128 and 141–157.
- For amount/count limits, this page says **authorised** amounts and transactions consume limit even before capture; expiry or cancellation releases the limit. That is a rule-limit accounting claim, not proof of captured, booked or settled payout funds. A rule-declined payout can be inspected in Transfer webhooks via `transactionRulesResult` and `reason: declinedByTransactionRule`, or in Customer Area. See raw lines 130–164.

## Detail locators

- **Pilot scope and request-rule setup:** raw lines 19–53.
- **Blocklist, velocity, bypass, time windows and resource scope:** raw lines 55–96.
- **Restriction fields and authorised-limit accounting:** raw lines 98–139.
- **Hard-block hierarchy and decline evidence:** raw lines 141–164.

## Related

- [[adyen-payouts]]
- [Create transaction rules](https://docs.adyen.com/payouts/payout-service/transaction-rules/create-and-manage)

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/transaction-rules/2026-09-15|Adyen Payout Service transaction rules — collected 2026-09-15]]
