# Fixed retrieval checks — manage stores

Q1. What is the source's purpose and scope, and what must not be inferred?
- Expected: A 2025-modified Adyen for Platforms store-management guide captured 2026-09-15. The store links to a platform user's legal entity through business lines and is associated with a merchant account; store ID, merchant-scoped reference, balance account, account holder and legal entity remain distinct. It covers Customer Area/Management API create/view/update. An active store or example response does not prove account-holder KYC/verification, payment-method enablement, legal seller, current country/product eligibility, actual split or successful payment.
- Raw locators: `raw/adyen/docs/platforms/manage-stores/2026-09-15.md:15-41`, `:43-50`, `:127-150`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-platforms-manage-stores.md` → `[[adyen-platforms]]`.

Q2. What prerequisites and destructive/status consequences govern store actions?
- Expected: Customer Area creation defaults on for onboarding-on-invite platforms; others need Adyen activation, and the admin role is required. Store country/region must be on the holder; another country/region requires another holder. Sales channel controls eCommerce/POS contact/address details and default methods need review. Management API requires Stores read/write credentials plus merchant/business-line details; businessLineIds is required only with multiple merchant-account business lines. Inactive blocks new transactions but permits outstanding capture; closed must follow inactive and cannot reopen. PATCH cannot change country; roles differ for view/update, and test examples are not live proof.
- Raw locators: `raw/adyen/docs/platforms/manage-stores/2026-09-15.md:33-41`, `:52-130`, `:136-157`, `:181-254`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-platforms-manage-stores.md` → `[[adyen-platforms]]`.
