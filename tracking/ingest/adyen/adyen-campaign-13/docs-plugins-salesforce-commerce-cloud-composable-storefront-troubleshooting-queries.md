# Fixed retrieval checks — Composable Storefront troubleshooting

Q1. What is this guide's troubleshooting scope, and what must not be inferred?
- Expected: Composable Storefront package diagnostics: check setup, integration logs, package version/release notes, open GitHub issues, then Support or issue filing if the problem persists. It does not establish a root cause, verified fix, live order/payment status, settlement, or an SFRA cache/custom-cartridge procedure. No request-ID collection steps are specified.
- Raw locators: `raw/adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/troubleshooting/2026-09-15.md:15-22`, `:39-60`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-troubleshooting.md` → `[[adyen-salesforce-commerce-cloud]]`.

Q2. Which diagnostic signals and escalation evidence does the page actually provide?
- Expected: Info/Warn/Error/Debug have different meanings; Debug can show sent parameters. Read console or Salesforce Log Center, and browser console if no integration errors appear. Payment Details → Application Info → Payment Device Version locates the package version to compare with release notes. Open GitHub issues are another lead. If the problem persists, file a bug or contact Support with version and relevant screenshots/logs. Treat remedies as conditional and diagnostic material as potentially sensitive; no actual fix, retry or payment outcome follows from these steps.
- Raw locators: `raw/adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/troubleshooting/2026-09-15.md:24-60`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-troubleshooting.md` → `[[adyen-salesforce-commerce-cloud]]`.
