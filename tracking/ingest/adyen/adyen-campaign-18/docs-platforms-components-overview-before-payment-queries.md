# Before-payment component hub retrieval checks

Q1. Which component route does the Adyen before-payment hub point a platform to for bank-account collection and status viewing?
Expected forward route: [[adyen-index]] → [[adyen-platform-components]] → ## Sources → [[source-adyen-docs-platforms-components-overview-before-payment]] → [[raw/adyen/docs/platforms/components-overview/before-payment/2026-09-15]]. Inspect raw lines 19–25 for onboarding purpose and the Transfer Instrument child card, then follow the related detailed child source for implementation specifics.

Q2. Does this page establish that a user's bank account has passed verification or that the platform can already accept payments for them?
Expected forward route: [[adyen-index]] → [[adyen-platform-components]] → ## Sources → [[source-adyen-docs-platforms-components-overview-before-payment]] → [[raw/adyen/docs/platforms/components-overview/before-payment/2026-09-15]]. Raw lines 19–25 describe prerequisite onboarding and a component link, while lines 27–30 only route to other guides; no user-specific verification or operation outcome is shown.
