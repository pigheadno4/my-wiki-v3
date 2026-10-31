# Fixed-query answers — negative balance compensation warning overview

## Q1

The 2026-09-15-captured API Explorer overview names the family **Negative balance compensation warning v1** (raw line 5). Adyen says it sends webhooks about balance accounts negative for 20 or more days (line 7). Its sole listed POST event is `balancePlatform.negativeBalanceCompensationWarning.scheduled` (lines 9–14). If funds are not transferred to cover that balance before the scheduled compensation date, the overview says a transfer is made from the liable balance account on that date (line 7). This overview provides no event body, per-notification account ID, amount, currency, or date field; see the separate event-specific reference. Route: [[source-adyen-api-explorer-negative-balance-compensation-warning-webhooks-latest-overview]] via [[adyen-webhooks]]. Canonical URL: https://docs.adyen.com/api-explorer/negative-balance-compensation-warning-webhooks/latest/overview

## Q2

The catalog establishes a warning condition and a conditional future compensation path, not that a liable-account transfer already occurred or that an account balance has been restored (line 7). It gives no event-specific delivery order, retries, deduplication, signature/authentication rules, failure or reversal outcome, or financial-finality guarantee. The captured title says v1, while `latest` is a route label and the September 2026 capture does not prove the current live version (lines 1–5). Route: [[source-adyen-api-explorer-negative-balance-compensation-warning-webhooks-latest-overview]] via [[adyen-webhooks]] and [[adyen-platforms]]. Canonical URL: https://docs.adyen.com/api-explorer/negative-balance-compensation-warning-webhooks/latest/overview
