# Adyen plugin release notes — locator queries

Source stem: `source-adyen-docs-plugins-release-notes`
Canonical URL: https://docs.adyen.com/plugins/release-notes
Pinned raw: `raw/adyen/docs/plugins/release-notes/2026-09-15.md`

## Q1. What must an Adobe Commerce headless integration review when moving to plugin v11.0.0?

In the 2026-08-24 Adobe Commerce v11.0.0 entry, the plugin stops setting `additional_information.cc_type`; the entry points to `ccType` on the payment object through `getCcType()`/`setCcType()`. `sortAndFilterPaymentMethods()` stops returning `adyenPaymentMethodsResponse`, and the `/payments/details` REST endpoint/`adyenPaymentDetails` GraphQL mutation return structured refusal, cancellation and error responses instead of the generic refusal exception. Capture-mode customizations and Multishipping Billing code reading `window.customerData` also need review if present. The entry links a migration guide. Locators: raw lines 48–70 and 92–94. These are v11-specific documented changes, not proof that a particular headless storefront has migrated.

## Q2. Which Cegid version documents an Adyen payment missing from Cegid, and where is its fix recorded?

The 2024-12-19 Cegid Retail Y2 v2.1.12 Known Issues entry says a `receiptData` log line over 40 characters can prevent a Cegid receipt and transaction record even when Adyen processed the payment, creating reconciliation risk (raw lines 813–833). The 2025-01-15 v2.1.13 Fixed entry says that issue was fixed (raw lines 798–804). This is a historical version-specific issue and fix, not evidence that any merchant's transaction reconciled.
