# C16 Customer Area split-profile management retrieval checks

## Q1 — Purpose, scope, and inference boundary

Query: What does the Adyen for Platforms Customer Area split-profile management page cover, and can it prove a specific store's split, merchant of record, or completed payment outcome?

Expected route: `wiki/sources/adyen/source-adyen-docs-platforms-automatic-split-configuration-manage-split-configurations-customer-area.md` through the Adyen automatic-split concept after promotion. Answer: dated guide for a platform-model operator with the specified Customer Area role to view merchant-account profiles, add/remove rules, edit conditions/logic, and delete profiles. It does not prove a profile's current state, request priority, legal seller/MOR, booked split, capture, settlement or payout. Raw locators: lines 15–34, 36–60, 62–64, 203–222.

## Q2 — Capability, prerequisites, and warnings

Query: How can a Customer Area rule change affect transactions already authorized, and what limits apply to edits or deletion?

Expected route: same source and raw. Answer: adding a rule or editing its conditions/logic takes effect for subsequent transactions and is re-evaluated at capture, so a payment authorized before the edit but captured after it can use the changed profile. Requires platform-model integration, relevant merchant account and **Manage new split configuration settings** role. Description and card-region condition updates are Management API-only. A profile must retain one rule, so its sole rule cannot be removed. The raw gives profile-deletion steps but no store-unlinking or post-deletion booking result. Raw locators: lines 26–34, 62–120, 122–161, 163–205, 214–222.
