# C59 fixed-query answers: balancePlatformPayoutSchedule.updated

Pinned raw: `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balancePlatformPayoutSchedule.updated/2026-09-15.md` (SHA-256 `24c5f71b50639b58224c46cd059a85326ce276e76b7252f5cdc818a53acf078d`). Canonical route: [Adyen API Explorer](https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balancePlatformPayoutSchedule.updated). Proposed source: [[source-adyen-api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-balanceplatformpayoutschedule-updated]].

## Q1

The incoming `balancePlatform.balancePlatformPayoutSchedule.updated` webhook is sent when a managed payout schedule is successfully updated on the balance platform (raw lines 5–7). The table requires top-level `data`, `environment` and `type`, permits `test` or `live` environment, and marks `timestamp` optional (lines 11–29). All listed `data` fields are optional: platform/schedule IDs, country/currency, default descriptions, frequency/date values and references, min/max payout amounts and retained amount (lines 14–26). The schedule-ID field mentions a schedule applied to a balance account (line 16), but the event trigger is platform-level and no balance-account ID is listed. `defaultFrequencyValue` is allowed only for monthly or weekly `defaultFrequency`; its monthly 1–31 range sentence uses `frequency`, while its weekly 1–5 range sentence uses `defaultFrequency` (line 21).

## Q2

This event establishes a successful schedule update on the balance platform, not account-level application, payout execution, transfer settlement or bank receipt. The retained-amount field describes a condition for later execution, without showing that any execution occurred (line 26). Any HTTP `2xx` accepts the webhook (lines 31–39). The capture contains no example payload or event-specific delivery order, retry, deduplication, signature, reversal or financial-finality rule. The `latest` URL and 2026-09-15 fetched date are snapshot locators, not fixed current-version proof (lines 1–2).
