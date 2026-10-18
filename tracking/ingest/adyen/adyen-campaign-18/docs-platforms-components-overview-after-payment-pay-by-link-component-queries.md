# Pay by Link components — retrieval probes

## Q1 — Purpose, state and split boundary

**Query:** What do the Pay by Link Platform Experience components do, and does a Completed link prove user balance booking or settlement?

**Expected answer:** The Overview and Details components provide portal UI for creating, viewing, filtering, sharing, copying and expiring links; the page also covers terms and theme settings. Payment pending means started but unconfirmed; Completed is the component's link state after the required payment has processed. The component does not change split logic: the store's split configuration determines allocation, with liable balance account fallback when none is configured. A UI state or link creation callback alone does not prove settlement or a bank payout.

**Raw locators:** lines 27-37 (purpose/version); 56-61 (limits and split); 69-95 and 125-179 (statuses/Details); 182-207 (creation); 409 (creation callback). **Canonical discovery route:** [[adyen-index]] → [[adyen-platform-components]] → [[source-adyen-docs-platforms-components-overview-after-payment-pay-by-link-component]] → [[raw/adyen/docs/platforms/components-overview/after-payment/pay-by-link-component/2026-09-15]].

## Q2 — Access, expiry and integration

**Query:** What setup and limits does this captured Pay by Link component guide require before a platform user creates a link?

**Expected answer:** It calls for Adyen for Platforms, a Balance Platform API key with relevant Pay By Link Component roles, a server-created scoped Session authentication token, a front-end Platform Experience library, and an account holder associated with at least one store linked to a payByLink or eCommerce business line. Store-specific shopper terms URL and compliance confirmation must precede first-link creation. Links are searchable for up to 90 days, user expiry may be up to 70 days, and absent a value links expire after 24 hours. Created link details cannot be edited; the component does not send email automatically. Version-specific features and CDN/SRI details must be checked against the selected library version, and example sessions do not establish current access.

**Raw locators:** lines 37-65 (version, roles, limits/setup); 182-207 and 220-235 (creation and terms); 253-319 (server session); 321-409 (front-end setup and callbacks). **Canonical discovery route:** [[adyen-index]] → [[adyen-platform-components]] → [[source-adyen-docs-platforms-components-overview-after-payment-pay-by-link-component]] → [[raw/adyen/docs/platforms/components-overview/after-payment/pay-by-link-component/2026-09-15]].
