# C22 Issuing balance webhook use-case retrieval checks

## Q1 — What scopes and conditions do the examples configure?

The pilot page illustrates a Configuration API balance-webhook setting targeting the whole `balancePlatform` for current `balance` `lessThan` USD 5,000; an `accountHolder` target using `lessThanOrEqual` at the same current-balance threshold; and a `balanceAccount` target using `available` `lessThan` for each specified account (raw lines 26–45, 97–116, 169–188). Its request examples use the test Balance Platform host and `status: active` (raw lines 49–70, 120–141, 192–213). These are setup examples for a balance platform, account holder, or balance-account ID, not live eligibility proof. Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-balance-updates-use-cases]] → [[raw/adyen/docs/issuing/balance-updates/use-cases/2026-09-15]].

## Q2 — What pilot and example-data limits should a reader preserve?

The page says balance webhooks are in pilot and its processes/documentation may change (raw lines 19–20). The six-account example says below JPY 1,000 but sends `value: 100000` and shows `available: 95000`, without stating a JPY scaling rule (raw lines 169–188, 203–210, 219–234). Its sample event has `accountHolderId`, `settingIds` and `currency` but no `balanceAccountId`, so the payload shown does not itself identify which individual account changed (raw lines 222–238). Test examples do not establish successful production delivery. Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-balance-updates-use-cases]] → [[raw/adyen/docs/issuing/balance-updates/use-cases/2026-09-15]].
