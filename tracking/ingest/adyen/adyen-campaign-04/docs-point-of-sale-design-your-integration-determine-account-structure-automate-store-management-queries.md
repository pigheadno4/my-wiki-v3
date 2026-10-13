# Fixed retrieval checks — Adyen automate store management

## 1. Purpose and scope

**Query:** What is this page for, and what should a reader avoid inferring from it?

**Answer:** It is Adyen's 2026-09-15 POS guide to automating store retrieval, creation, updates, and store payment-method configuration with the Management API. It covers merchant/store records and settings; its test curl and version-specific SDK examples do not establish current live eligibility, a successful API request, or Terminal API transaction behavior. Locate the purpose at raw line 19; the Management API route and example boundaries are summarized in [[source-adyen-docs-point-of-sale-design-your-integration-determine-account-structure-automate-store-management]].

**Route:** [[index]] → [[adyen-index]] → [[adyen-pos-store-management]] → [[source-adyen-docs-point-of-sale-design-your-integration-determine-account-structure-automate-store-management]] → [[raw/adyen/docs/point-of-sale/design-your-integration/determine-account-structure/automate-store-management/2026-09-15]] (catalog promotion pending).

## 2. Central capability, prerequisites, and warnings

**Query:** How can a POS integrator automate store management, and what prerequisites or consequential status changes matter?

**Answer:** Use the Management API with an API credential/API key carrying Stores read/read-write and Payment methods read/read-write roles for a POS integration (raw lines 28–39). GET lists account-accessible or merchant-scoped stores (lines 66–341); POST creates a store for a merchant account (lines 518–547); PATCH requires its unique Adyen store ID, which older stores may lack (lines 41–47, 1696–1709). A new active store has no payment methods: add them individually, and assign/board terminals before transacting (lines 49–57, 1027–1050). Inactivation blocks new transactions but allows outstanding captures; closing requires inactivation, moves terminals to merchant inventory, and cannot be reversed (lines 55–57). Live store-related requests have rate limits (line 39). Payment-method listings can include web-only methods that terminals do not support (lines 1033–1037). The POST field table marks `businessLineId` required and names `storeIds`, while curl and some SDK examples omit that field and some use `storeId`; verify the current API Explorer schema and business-line requirements before making a call (lines 1042–1069, 1221).

**Route:** [[index]] → [[adyen-index]] → [[adyen-pos-store-management]] → [[source-adyen-docs-point-of-sale-design-your-integration-determine-account-structure-automate-store-management]] → [[raw/adyen/docs/point-of-sale/design-your-integration/determine-account-structure/automate-store-management/2026-09-15]] (catalog promotion pending).
