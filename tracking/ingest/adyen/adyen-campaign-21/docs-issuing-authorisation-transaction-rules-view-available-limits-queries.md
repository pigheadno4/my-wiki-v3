# Q1 — purpose and prerequisites

**Query:** What does this Issuing available-limits lookup report, and which integration, role and request IDs does the guide require?

**Answer:** The page describes reading a card payment instrument's limit, used and remaining amount/count, source, interval and `calculatedAt` snapshot (raw lines 32–38, 68–108). Its requirements name **Adyen Issuing**, Configuration API access and **Bank Manage TransactionRules role** (raw lines 48–53). GET `/paymentinstruments/{id}/limits` needs the issued-card ID; `transactionRuleId` is optional and omission invokes the transaction-rule hierarchy (raw lines 70–77). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-authorisation-transaction-rules-view-available-limits]] → [[raw/adyen/docs/issuing/authorisation/transaction-rules/view-available-limits/2026-09-15]].

# Q2 — material limit and conflict

**Query:** Does remaining limit equal uncaptured or settled spending capacity for every rule, and can the example's timezone field be used as the schema?

**Answer:** No. Authorized amount/count reduce available limit even before capture; canceled or expired authorization releases it (raw lines 59–66). Only `totalAmount` or `matchingTransactions` payment-instrument-level limits are supported; combined `matchingValues`/`matchingTransactions`, higher aggregation and `blockList` are excluded (raw lines 54–56). The table names `timezone` with default UTC, but the JSON example uses `timeZone` with CST (raw lines 131, 168, 190); check the applicable schema and observed response. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-authorisation-transaction-rules-view-available-limits]] → [[raw/adyen/docs/issuing/authorisation/transaction-rules/view-available-limits/2026-09-15]].
