# Manage balance webhook settings — retrieval checks

## Q1 — purpose, scope, and read routes

**Query:** What does Adyen's Platforms “Manage your balance webhook settings” page cover, and how do I view all settings versus one setting? Does a listed active setting prove a balance movement?

**Expected retrieval:** This limited-availability pilot page covers Configuration API management of existing Balance webhook settings. GET `/balancePlatforms/{id}/webhooks/{id}/settings` lists settings; GET the same path with `/{settingId}` inspects one, using platform and webhook IDs plus the setting ID for one-setting operations. Response examples show target, currency, status and conditions. This is configuration state, not proof that a webhook was delivered, a balance changed, a transfer booked, or a beneficiary bank received funds. Creation and subscription live in the separate configuration guide.

**Raw locators:** lines 15–28 (pilot, scope and list route); 40–79 (list response); 81–119 (single-setting route/response); 265–273 (configuration next step).

**Canonical route:** [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-balance-updates-manage-balance-webhook]] → [[raw/adyen/docs/platforms/balance-updates/manage-balance-webhook/2026-09-15]].

## Q2 — update consequences and stopping alerts

**Query:** How should a platform add or remove conditions from a Balance webhook setting, and what happens if it removes the only condition, sets the status inactive, or deletes the setting?

**Expected retrieval:** PATCH the specific setting path with the IDs. To add a condition, send the old and new sets together; to remove one, omit it but include every condition to keep. Clearing the last condition causes updates for all balance changes in the specified target account(s), a broadening of alerts. Setting `status: inactive` temporarily stops notifications for the setting, whereas DELETE permanently stops them for the setting/conditions. The page is pilot documentation. Its active-status row says any condition can trigger, while the related configure guide says all configured conditions must match; preserve this unresolved conflict when discussing multiple conditions. The sample IDs, balances and thresholds are TEST examples, and the page does not establish a restored-setting path after deletion.

**Raw locators:** lines 121–147 (PATCH and fields); 155–195 (add and remove instructions); 224–263 (inactive, empty-condition and DELETE outcomes); related [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]] raw lines 88–90 for the conflicting all-conditions statement.

**Canonical route:** [[index]] → [[adyen-index]] → [[adyen-platforms]] and [[adyen-webhooks]] → [[source-adyen-docs-platforms-balance-updates-manage-balance-webhook]] → [[raw/adyen/docs/platforms/balance-updates/manage-balance-webhook/2026-09-15]].
