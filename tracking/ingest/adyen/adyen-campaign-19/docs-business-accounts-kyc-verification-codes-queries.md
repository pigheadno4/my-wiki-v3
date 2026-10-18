# Fixed queries — docs-business-accounts-kyc-verification-codes

## Q1 — purpose and scope

**Query:** Where does Adyen define Business Accounts verification codes, what are their three layers, and does an action always accompany an error?

**Answer boundary:** The captured overview explains verification-error information for account-holder capabilities and names Platforms or Issuing integration scope. General codes describe broad causes; linked suberrors give finer causes; remediating actions are possible solutions and sent whenever possible, not guaranteed. Do not infer account approval or automatic retries.

**Forward route:** [[index]] → [[adyen-index]] (provider catalog; coordinator must expose [[adyen-business-accounts]] as a concept route) → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-kyc-verification-codes]] → [[raw/adyen/docs/business-accounts/kyc-verification-codes/2026-09-15]]. Exact raw locators: lines 17–25 and 27–35.

## Q2 — capability location and prerequisites

**Query:** Where can an eligible integrator find the verification codes and how are problem, general error, suberror and remediation fields related?

**Answer boundary:** Customer Area account-holder Capabilities tab, Configuration API `GET /accountHolders/{id}`, or account-holder created/updated webhooks. API viewing needs API web service user credentials; Customer Area needs the Manage account holder capabilities role. Capability `problems` identifies the affected legal entity; `verificationErrors` holds general error detail and may carry common actions, while `subErrors` has granular details and its own action array. The example is illustrative; use child catalogs for actual codes. Do not equate a code, status example, or remediation suggestion with verified capability.

**Forward route:** [[index]] → [[adyen-index]] (provider catalog; coordinator must expose [[adyen-business-accounts]] as a concept route) → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-kyc-verification-codes]] → [[raw/adyen/docs/business-accounts/kyc-verification-codes/2026-09-15]]. Exact raw locators: lines 27–61, 69–81, 83–144 and 146–160.
