# Retrieval checks — Business Accounts balance-account transfer limits

## Q1 — purpose and prerequisites

**Question:** What does this guide configure, and what prerequisites and scope apply?

**Located answer:** It configures amount-based limits for outgoing external transfers from a user's balance account linked to a `bankAccount` payment instrument (Adyen business account). The requirements table names an Adyen for Platforms Business Accounts integration, Configuration API Balance platform base role, transfer and transaction webhook subscriptions, linked business account, installed Authentication SDK and registered SCA devices (raw lines 15-36). Internal transfers and incoming external transfers are excluded (raw line 33). This dated guide does not establish a specific user's eligibility or a completed transfer.

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-use-transfer-limits-balance-accounts]] → [[raw/adyen/docs/business-accounts/use-transfer-limits/balance-accounts/2026-09-15]].

## Q2 — material boundary, failure or conflict

**Question:** Can an active limit be deleted, and can the sample request for current effective limits be used as written?

**Located answer:** No. The guide permits deletion only for pending or scheduled limits; an active limit requires a new overriding limit (raw lines 723-745). It describes balance-account overrides by matching `scope` and `transferType`, but its next sentence says a platform limit applies when no platform limit was set, an internal contradiction (raw lines 616-624). The current-effective-limits prose names `/balanceAccounts/{id}/transferLimits/current` (raw line 627), while the curl example calls `/balanceAccounts/{id}/transferLimits` (raw lines 640-647); several creation examples also contain malformed JSON (for example raw lines 145-165). The examples therefore need verification against the API reference before use.

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-use-transfer-limits-balance-accounts]] → [[raw/adyen/docs/business-accounts/use-transfer-limits/balance-accounts/2026-09-15]].
