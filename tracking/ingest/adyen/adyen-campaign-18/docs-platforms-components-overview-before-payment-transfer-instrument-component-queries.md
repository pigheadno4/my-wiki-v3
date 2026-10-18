# Transfer Instrument components retrieval checks

Q1. What are the prerequisites and session scope for embedding Adyen's Transfer Instrument components in a platform onboarding portal?
Expected forward route: [[adyen-index]] → [[adyen-platform-components]] → ## Sources → [[source-adyen-docs-platforms-components-overview-before-payment-transfer-instrument-component]] → [[raw/adyen/docs/platforms/components-overview/before-payment/transfer-instrument-component/2026-09-15]]. Inspect raw lines 23–35 for LEM v3/v4, API-only partial scope and library-version caveat; lines 43–53 for credentials/setup; lines 98–113 for LEM key, owning legal entity, roles, origin and product.

Q2. Does a component `complete` event or displayed bank-account status prove verification approval or payout delivery?
Expected forward route: [[adyen-index]] → [[adyen-platform-components]] → ## Sources → [[source-adyen-docs-platforms-components-overview-before-payment-transfer-instrument-component]] → [[raw/adyen/docs/platforms/components-overview/before-payment/transfer-instrument-component/2026-09-15]]. Inspect raw lines 57–75 for configuration versus management and statuses; lines 565–574 for callback semantics, and lines 580–602 for illustrative payload with incomplete verification fields. The page does not establish a booked payout or bank receipt.
