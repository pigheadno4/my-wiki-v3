# C24 Marketplace capabilities retrieval checks

## Q1 — How are Marketplace user capabilities requested and made usable?

Adyen generally configures defaults during design, automatically requested on account-holder creation; extra capabilities require a separate request and can prompt KYC checks (raw lines 19–27). Inspect verification status via account-holder webhooks or GET `/accountHolders/{id}`, then inspect `requested`, `allowed` and `enabled`; a capability can be used only if both allowed and enabled are true (raw lines 94–121). Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-verification-overview-capabilities]] → [[raw/adyen/docs/marketplaces/verification-overview/capabilities/2026-09-15]].

## Q2 — Does `pending` or `invalid` always disable use, and can `rejected` be fixed by resubmission?

No. A first-time pending request is normally not allowed, but a previously allowed capability can remain allowed during re-verification after data changes (raw line 105). Ordinary invalid verification sets allowed false, yet changed/missing data after previous success may leave `invalid` with allowed true during a specific remediation deadline; the user must provide information within that deadline (raw lines 107, 120). `rejected` is final and cannot be resolved by updating data or uploading documents (raw line 108). Usability still requires enabled true as well as allowed true (raw line 121). Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-verification-overview-capabilities]] → [[raw/adyen/docs/marketplaces/verification-overview/capabilities/2026-09-15]].
