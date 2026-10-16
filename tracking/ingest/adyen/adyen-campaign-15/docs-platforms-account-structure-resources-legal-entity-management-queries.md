# Fixed retrieval checks — Platforms LEM resources

Q1. What is this source's purpose and scope, and what must not be inferred?
- Expected: A 2026-09-15 Adyen for Platforms orientation page naming Legal Entity Management resources to provide verification information for platform users. It distinguishes legal entity, business line, transfer instrument and supporting document, and links to separate onboarding/account-holder/balance-account guides. Creating resources or seeing the diagram does not prove verification, capability use, merchant-of-record identity, payment, payout or bank receipt. The linked Issuing-path requirements URL is navigation, not optional-product eligibility.
- Raw locators: `raw/adyen/docs/platforms/account-structure-resources/legal-entity-management/2026-09-15.md:15-39`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-platforms-account-structure-resources-legal-entity-management.md` → `[[adyen-platforms]]`.

Q2. What does each resource describe, and what prerequisites/limits follow?
- Expected: Legal entity stores user legal-name/address/tax information; business line stores industry/source-of-funds information; transfer instrument is described as the user's verified bank account for payouts; supporting documents help verify the legal entity or instrument. Adyen says it must verify platform users before processing payments, paying out user funds or offering financial products, and the LEM API manages these resources. The page does not specify API permissions, country/version conditions, resource cardinality or an individual verification decision; follow linked detailed guides for operations.
- Raw locators: `raw/adyen/docs/platforms/account-structure-resources/legal-entity-management/2026-09-15.md:19-34`, `:36-39`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-platforms-account-structure-resources-legal-entity-management.md` → `[[adyen-platforms]]`.
