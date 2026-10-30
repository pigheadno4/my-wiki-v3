# C55 online payments release notes retrieval probes

Source entry: `source-adyen-docs-online-payments-release-notes` (`wiki/sources/adyen/source-adyen-docs-online-payments-release-notes.md`)
Canonical URL: https://docs.adyen.com/online-payments/release-notes
Pinned raw: `raw/adyen/docs/online-payments/release-notes/2026-09-15.md`

## Q1

**Question:** In the captured 2026-09-10 Web v6.45.0 release, what Checkout API compatibility and Sessions review capability are documented?

**Answer:** That specific Web release requires Checkout API v69 or later. For Sessions, it adds a review-page step after the shopper selects Pay, using `onReview` to return payment data, `processPayment` to submit and `onAction` to return an action for display. These are release capabilities, not proof of merchant deployment or a completed payment. The page also recommends the latest Checkout API, which is distinct from the v69 minimum. Locators: pinned raw lines 30–42 (heading, requirement and new callbacks); source entry `source-adyen-docs-online-payments-release-notes`, “Key takeaways” and “Detail locators”; https://docs.adyen.com/online-payments/release-notes.

## Q2

**Question:** Which migration conditions in this release history would matter when moving tokenization to Checkout API v70 and a Web integration to v6.0.0?

**Answer:** In API v70, `/payments` or `/sessions` requests used to store or use stored payment details must include `recurringProcessingModel`; Customer Area `enableRecurring` no longer supplies the request parameters. In Web v6.0.0, Checkout API v69+ is required, imports and instance creation change, `onSubmit`/`onAdditionalDetails` must resolve or reject an `actions` object, failed payments move to `onPaymentFailed`, `countryCode` is mandatory in the checkout configuration or `/sessions`, and IE11 support ends. These conditions are tied to the respective versions; method-specific migrations require their own entry/guide. Locators: pinned raw lines 9022–9045 and 9070–9075 (API v70), 5590–5614 and 5620–5648 (Web v6.0.0); source entry `source-adyen-docs-online-payments-release-notes`, “Key takeaways” and “Detail locators”; https://docs.adyen.com/online-payments/release-notes.
