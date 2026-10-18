# Balance webhook configuration — retrieval checks

## Q1 — purpose, scope, and non-inference

**Query:** What does Adyen's Platforms “Configure balance webhooks” guide enable, and does creating a setting prove a user's balance or payout?

**Expected retrieval:** This limited-availability pilot guide covers a Customer Area Balance webhook subscription plus Configuration API settings for automatic notifications of balance changes. A setting can target the entire balance platform, all balance accounts of a particular account holder, or one balance account. It is configuration for conditional alerts; a saved setting or illustrative threshold does not prove the account's balance, a delivered notification, a transfer, a payout, or beneficiary-bank receipt. The page warns that pilot processes and documentation may change.

**Raw locators:** lines 15–30 (pilot, purpose, subscription and scopes); 73–96 (setting fields/targets); 98–149 (illustrative liable-account threshold and saved setting ID).

**Canonical route:** [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]] → [[raw/adyen/docs/platforms/balance-updates/configure-balance-webhook/2026-09-15]].

## Q2 — roles, limits, condition logic, and sample warnings

**Query:** What must be configured to receive balance-change webhooks, what are the setting limits, and can the page establish whether multiple conditions use all or any matching?

**Expected retrieval:** Subscribe and enable Balance webhook in the Platforms Customer Area tab, set receiver URL/security, store its ID, then POST a setting under the nested balance-platform/webhook settings route with target type/id, currency and status. The Configuration API credential needs Balance Platform BCL role and Customer Area user needs Merchant technical integrator or Merchant admin. The documented limits are 20 settings per webhook and 20 condition sets per setting. Optional conditions name balance type, comparator and value; no conditions cover all balance changes for the target accounts, while inactive status suppresses matched notifications. The conditions row says all configured conditions must match, but the active-status row says any condition can trigger; preserve the conflict rather than promising Boolean semantics. The USD 5,000 liable-account threshold is a test example. Its cURL path omits the settings suffix named in prose, and troubleshooting “resend POST” text links PATCH-style paths. The guide lists duplicate-condition, missing-account and invalid-currency errors, not proof of live delivery.

**Raw locators:** lines 32–39 (roles and caps); 41–75 (subscription and settings endpoint); 79–96 (required/optional fields and conflicting condition language); 98–149 (example and setting ID); 151–244 (troubleshooting).

**Canonical route:** [[index]] → [[adyen-index]] → [[adyen-platforms]] and [[adyen-webhooks]] → [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]] → [[raw/adyen/docs/platforms/balance-updates/configure-balance-webhook/2026-09-15]].
