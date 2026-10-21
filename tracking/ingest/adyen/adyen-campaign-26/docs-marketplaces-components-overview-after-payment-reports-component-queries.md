# docs-marketplaces-components-overview-after-payment-reports-component retrieval probes

## Q1 — What can the Reports Overview component show, and what access and setup are required?

Answer: In this pinned version, it lists downloadable CSV **Payout reports** for a balance account and selected time period; no other report type is supported (raw lines 43–55, 57–82). The platform needs Adyen for Platforms, a Balance Platform API key with **Reports Overview Component: View**, generated Balance Platform Payout reports, and relevant language/region/browser support (lines 43–55). The backend creates a scoped Session authentication API session with `allowOrigin`, `product: platform`, an `accountHolderId` resource and the view role; the frontend obtains/refreshes that complete session when initializing the component (lines 126–181, 228–295). Live origin must use HTTPS (line 138).

Route: [[index]] → [[adyen-index]] → [[adyen-platform-components]] → [[source-adyen-docs-marketplaces-components-overview-after-payment-reports-component]] → [[raw/adyen/docs/marketplaces/components-overview/after-payment/reports-component/2026-09-15]].

## Q2 — Which payout routes and outcome claims fall outside this component?

Answer: The guide says the Payout report targets automatic payouts with default settlement delay and excludes manual, pass-through and sales-day **T+0** payouts (raw lines 51–52). The UI's report list and CSV are account/time-scoped, with daily midnight **UTC+0** generation and default Last 30 days filter (lines 59–109); this does not establish a live payout or independent beneficiary-bank receipt. Feature details can vary by library version (lines 35–37), and custom fields or styling do not change underlying report coverage (lines 319–380).

Route: [[index]] → [[adyen-index]] → [[adyen-platform-components]] → [[source-adyen-docs-marketplaces-components-overview-after-payment-reports-component]] → [[raw/adyen/docs/marketplaces/components-overview/after-payment/reports-component/2026-09-15]].
