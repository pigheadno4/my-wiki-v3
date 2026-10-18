# Reports Overview component — retrieval probes

## Q1 — Scope and report grain

**Query:** Which reports can the Platform Experience Reports Overview component show, and does a downloaded file prove every payout or bank receipt?

**Expected answer:** In this captured guide, the component supports only the Balance Platform Payout report and lists downloadable CSV reports for a selected balance account and time period. The underlying report describes automatic payouts completed for that balance account with related debit and credit transactions. Coverage is designed for automatic payouts with default settlement delay, and expressly excludes manual payouts, pass-through payouts and sales-day payout T+0. A visible file is a report artifact, not an independent beneficiary bank credit; a missing file does not rule out out-of-scope payouts.

**Raw locators:** lines 27-35 (purpose/version); 43-55 (requirements/limits); 59-83 (list, CSV and report grain); 96-109 (time filters). **Canonical discovery route:** [[adyen-index]] → [[adyen-platform-components]] → [[source-adyen-docs-platforms-components-overview-after-payment-reports-component]] → [[raw/adyen/docs/platforms/components-overview/after-payment/reports-component/2026-09-15]].

## Q2 — Access, cadence and customization

**Query:** What access and setup are needed to show Reports Overview for a user, and does the midnight UTC statement guarantee a payout report for each day?

**Expected answer:** The guide requires an Adyen for Platforms integration, Balance Platform API key with Reports Overview Component: View role, configured generation of the Balance Platform Payout report, and a server-created Session authentication token scoped to the account holder, role, allowed origin and platform product. The front end initializes the versioned library with a session-refresh callback; live origins require HTTPS. The time-filter section says report data is generated daily at midnight UTC+0; it does not specify the UI list refresh time or guarantee a report for every account/day. Optional balanceAccountId locks the account view; custom fields require onDataRetrieve and platform-provided data. Versioned UI examples and TEST tokens do not establish live access or financial execution.

**Raw locators:** lines 43-55 (setup/limits); 96-109 (UTC filter); 128-180 (session); 182-303 (library/initializer); 359-405 (custom fields). **Canonical discovery route:** [[adyen-index]] → [[adyen-platform-components]] → [[source-adyen-docs-platforms-components-overview-after-payment-reports-component]] → [[raw/adyen/docs/platforms/components-overview/after-payment/reports-component/2026-09-15]].
