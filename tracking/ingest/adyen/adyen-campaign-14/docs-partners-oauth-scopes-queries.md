# Fixed retrieval checks — docs-partners-oauth-scopes

## Q1 — Purpose, scope, and what not to infer

**Query:** What does the partner OAuth scopes page provide, and what does it not imply?

**Answer:** It maps each OAuth access-token scope to specific customer merchant-account resources and API actions. An existing OAuth client's scope cannot currently be changed; broader requests require a new OAuth client and renewed customer-resource access. Possessing a scope name does not imply customer consent, authorization for every merchant account, live eligibility or payment execution. It was last modified and captured 2026-09-15. Evidence: raw lines 11, 15–45, 47–199. Canonical route: [[adyen-index]] → [[adyen-partner-oauth]] → ## Sources → [[source-adyen-docs-partners-oauth-scopes]] → [[raw/adyen/docs/partners/oauth/scopes/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Query:** Which API actions and qualifications are attached to the main partner OAuth scopes?

**Answer:** Webhook read lists GET configurations and a POST test; webhook write additionally lists create, PATCH and DELETE. Online-payment write covers Checkout Payments/Modifications/Orders/Utility and only GET storedPaymentMethods in Recurring with Checkout v70; it excludes tokenization, raw-card submission and payment links, which need separate scopes. Client-side online setup requires allowed origins and a generated client key through Management API because OAuth does not give Customer Area access; the live URL prefix is merchant-specific and fetched with the merchant ID from the granted accounts. Tokenization scope extends online payments for token use and Checkout Recurring list/delete but not separate Recurring API tokenization. Raw-card scope is disabled by default, requires SAQ D and account-manager enablement. Pay by Link plus subsequent recurring use needs its link, online-payment and tokenization scopes. Account-settings write text names modification but lists only GET; Cloud device scope lists device sync/async and status/connection operations. Actual merchant consent, roles, scope grant and live enablement must be checked separately. Evidence: raw lines 47–72, 74–163, 165–199. Canonical route: [[adyen-index]] → [[adyen-partner-oauth]] → ## Sources → [[source-adyen-docs-partners-oauth-scopes]] → [[raw/adyen/docs/partners/oauth/scopes/2026-09-15]].
