# docs-issuing-balance-updates retrieval checks

Q1. What is the purpose and setup route for Issuing Balance webhooks?

Answer: This pilot feature notifies the platform about balance changes at balance-platform, account-holder or balance-account scope (raw lines 19-32). Subscribe in Customer Area to get a webhook ID, then configure settings through POST `/balancePlatforms/{id}/webhooks/{id}/settings` with the scope and criteria (raw lines 34-47). More granular settings override inherited higher-level settings (raw lines 49-57). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-balance-updates]] → [[raw/adyen/docs/issuing/balance-updates/2026-09-15]].

Q2. What limits the meaning of a configured trigger or an expected notification?

Answer: The overview says all conditions must be met (raw line 47), while the linked configure guide says any in its status row and all in its conditions row (companion raw lines 88-90), leaving multi-condition behavior unresolved. Adyen labels the feature limited availability / pilot and subject to change (raw lines 19-20). A subscription and setting do not prove pilot eligibility, webhook delivery or a completed funds movement. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-balance-updates]] → [[raw/adyen/docs/issuing/balance-updates/2026-09-15]].
