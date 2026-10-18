# Balance webhook use cases — retrieval checks

## Q1 — purpose, scope, and event identity

**Query:** Which Balance webhook settings does Adyen's Platforms use-cases page illustrate, and can its example event identify the exact balance account or prove a live balance change?

**Expected retrieval:** The limited-availability pilot page gives three TEST examples: a platform-wide `balance` below USD 5,000; an account-holder-scoped `balance` at or below USD 5,000; and individual balance-account `available` thresholds, with a separate setting per account for six foreign-currency accounts. Example `balancePlatform.balanceAccount.balance.updated` payloads show settingIds, platform, currency and balances, with accountHolderId in the latter examples. They omit balanceAccountId even in the individually targeted example. These are illustrative events, not proof of any live account state, notification delivery, transfer, payout, or beneficiary bank receipt.

**Raw locators:** lines 15–24 (pilot and example purpose); 26–95 (platform-wide setting/event); 97–167 (user setting/event); 169–239 (per-account setting/event).

**Canonical route:** [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-balance-updates-use-cases]] → [[raw/adyen/docs/platforms/balance-updates/use-cases/2026-09-15]].

## Q2 — threshold values and limits

**Query:** Can I copy the page's JPY 1,000 available-balance threshold request as-is, and do these examples settle whether multiple conditions use all or any matching?

**Expected retrieval:** The JPY example says a 1,000 threshold but submits `conditions.value: 100000` and shows `available: 95000` in a TEST event. The page does not explain that scaling; the separate Adyen currency guide says JPY amounts have no decimal minor units. Therefore verify the current Balance webhook API's threshold-unit contract before using that value. The three use cases each have one condition, so they do not resolve the related configuration guide's all-versus-any multi-condition conflict. The configuration guide owns subscription, roles and the 20-settings/20-condition-sets limits, while the manage guide covers edits and deletion.

**Raw locators:** lines 169–188 (JPY 1,000 narrative and 100000 setting table); 197–239 (request and example event); related [[source-adyen-docs-development-resources-currency-codes]] raw lines 164–172 (JPY no-decimal minor-unit convention); related [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]] raw lines 88–90 (multi-condition conflict).

**Canonical route:** [[index]] → [[adyen-index]] → [[adyen-platforms]] and [[adyen-webhooks]] → [[source-adyen-docs-platforms-balance-updates-use-cases]] → [[raw/adyen/docs/platforms/balance-updates/use-cases/2026-09-15]].
