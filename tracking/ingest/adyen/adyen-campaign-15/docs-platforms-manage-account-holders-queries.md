# Fixed retrieval checks — manage account holders

Q1. What is the page's purpose and scope, and what must not be inferred?
- Expected: A 2023-modified Adyen for Platforms guide captured 2026-09-15 for Configuration API and Customer Area management of account holders. The account holder represents a platform user and links legal entities, balance accounts and capabilities; it is not itself a legal entity, balance account or merchant-account hierarchy. Do not infer live eligibility, legal seller/merchant-of-record, completed KYC, payout, bank receipt or payment.
- Raw locators: `raw/adyen/docs/platforms/manage-account-holders/2026-09-15.md:15-29`, `:292-336`, `:1225-1253`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-platforms-manage-account-holders.md` → proposed `[[adyen-platforms]]` foundation concept.

Q2. What are the core operations, prerequisites and consequences?
- Expected: Create the legal entity before POSTing an account holder; save the holder ID for webhooks and later balance-account creation. A capability request is sent to Adyen for approval and is distinct from allowed/enabled/verification status; Customer Area actions and KYC documents have separate roles. Suspension disables payout capabilities but leaves related balance accounts/payment instruments active; platform API reactivation applies only to currently suspended holders and cannot undo Adyen suspension. Permanent close requires emptying each balance account, closing non-primary then primary accounts, then closing the holder. Test URLs/SDK examples are not live proof.
- Raw locators: `raw/adyen/docs/platforms/manage-account-holders/2026-09-15.md:23-29`, `:238-290`, `:750-756`, `:979-987`, `:1213-1223`, `:1248-1289`, `:1560-1594`, `:1861-1925`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-platforms-manage-account-holders.md` → proposed `[[adyen-platforms]]` foundation concept.
