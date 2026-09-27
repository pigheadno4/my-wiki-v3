# Braintree C18 fixed-query audit — Group B

**Scope:** Control Panel Search + Role Permissions only. **Verdict: PASS (4/4).** Both pinned raw hashes match `manifest.json`: Search `cc8a3558c9b2a797672f071936ea65e912871bb47e57a046bc1901814521941d`; Role Permissions `b154edec8cf46587540518d9bb762b162a63a6e66534d00f3288a0409e624ec2`.

## Control Panel Search

**Actual route:** `wiki/index.md` § PSP Indexes → `[[braintree-index]]` § Concepts → `[[braintree-control-panel]]` § Sources → `[[source-braintree-control-panel-search]]` → `[[raw/braintree/articles/control-panel/search-2026-09-16]]`.

1. **Navigation question — Where is Braintree Control Panel search documented?**
   - **Object/action match:** Yes — Control Panel UI search, not SDK, API, GraphQL, or fraud-analysis search.
   - **Answer:** `[[source-braintree-control-panel-search]]`, backed by the collected Control Panel Search article.
   - **Raw locator:** `# Search`, lines 14–20; basic and advanced sections, lines 23–167.
   - **Verdict:** PASS.

2. **Detail question — Which search purposes, result boundaries and permission or date qualifications does this page document?**
   - **Object/action match:** Yes — basic and advanced Control Panel searches and their result/download behavior.
   - **Answer:** Basic search quickly locates specific transactions and Vault records by a limited parameter set; advanced search covers Transactions, Verifications, Vault, and Subscriptions and supports filtered processing/Vault reporting. Basic results are limited to transactions or Vault records from the prior 60 days and newly created transactions/customers may be absent for up to 30 minutes. Gateway-user transaction searches exclude subscriptions; verification search is capped at 40,000 records; Vault search shows only the last 10 transactions for a customer record; CSV downloads cap transaction results at 500,000 and subscription/Vault/verification results at 40,000, with download history available for at least 24 hours. Some downloaded transaction columns depend on account setup. The page instructs users to log in but names no required role or permission.
   - **Raw locator:** basic scope/categories lines 23–52; 60-day/indexing qualification lines 55–56; advanced purposes lines 61–69; gateway-user exclusion and CSV purpose lines 72–87; verification cap lines 98–119; Vault last-10 boundary lines 122–140; subscription scope lines 143–154; download caps/history/account qualification lines 157–167. Full-page absence check: no `permission` or `role` term in lines 14–167.
   - **Verdict:** PASS.

## Role Permissions

**Actual route:** `wiki/index.md` § PSP Indexes → `[[braintree-index]]` § Concepts → `[[braintree-control-panel]]` § Sources → `[[source-braintree-control-panel-users-roles-role-permissions]]` → `[[raw/braintree/articles/control-panel/users-roles/role-permissions-2026-09-16]]`; the source additionally routes to the fully read `[[raw/braintree/articles/control-panel/users-roles/managing-users-roles-2026-09-16]]` for the Account Admin scope tension.

3. **Navigation question — Where are Braintree Control Panel role permissions documented?**
   - **Object/action match:** Yes — assignable Control Panel role rights and their action scopes, not user-creation procedure or general API authorization.
   - **Answer:** `[[source-braintree-control-panel-users-roles-role-permissions]]`, backed by the collected Role Permissions reference.
   - **Raw locator:** `# Role Permissions`, lines 14–22; `## Rights Granted`, lines 27–79.
   - **Verdict:** PASS.

4. **Detail question — Which role-permission categories and action scopes does this page define?**
   - **Object/action match:** Yes — permission categories and the actions each named right grants.
   - **Answer:** The table defines Transactions (create, refund, settle, escrow, void, API-search/report download), Customer Management (Vault customer/payment-method management, verification, API customer search/client token, Vault export), Reporting (reports versus separate statement access, Dashboard graphs), Processing and Security Options (processing/payment-method settings, merchant IDs, API IP restrictions), Fraud Tools and Fraud Protection Advanced Dashboard actions, User Management, Recurring Billing management/view/search/download, Dispute Management, Webhooks, My Account agreements, Statements, Merchant Accounts, Business Management, Forward API, OAuth Applications, Connected OAuth Applications, Read-Only Access, and Search. Assigning Manage Roles or Manage Users requires Account Admin. Material scopes remain distinct: reports do not grant statements; production merchant-account management is Marketplace-qualified while sandbox permits test accounts; Forward API is for all sandbox and approved production merchants and is explicitly not included in Account Admin; OAuth permissions are beta-limited; Manage Connected OAuth Applications may consent to requested scopes even when the user lacks the corresponding rights. The fully read managing-users page says Account Admin has “maximum permissions possible,” so the Forward API statement remains an unresolved documented scope tension, not an inferred override.
   - **Raw locator:** assignment model and Account Admin gate lines 16–22; Transactions lines 29–36; Customer/Reporting/Processing/Security lines 37–42; Fraud/User/Recurring/Dispute lines 43–60; Webhooks through OAuth scopes lines 61–69; Read-Only/Search lines 70–79. Tension evidence: Role Permissions line 66 and Managing Users and Roles line 41.
   - **Verdict:** PASS.

## Bounded gap sweep and reciprocal check

- Filename sweep found the pinned Control Panel pages, users/roles siblings, SCIM pages, and separate Node/GraphQL/API search references. Those separate search and SCIM/login pages are wrong-object evidence for these fixed questions and were not selected for factual use. A content sweep for the defining phrases found only the pinned pages plus tangential fraud-tool and optimized-debit search mentions; neither changes these answers.
- Extra full read: `raw/braintree/articles/control-panel/users-roles/managing-users-roles-2026-09-16.md` (SHA-256 `345b30dc089017638603bc44e5c000eb2d8423387e1f3866c712aaf1a34b4d64`) solely because the promoted role-permissions source cites it for the Account Admin/Forward API tension. No other extra raw was needed.
- Reciprocal/navigation checks pass: root → provider index → Control Panel concept → both sources → exact raw; both sources link back to `[[braintree-control-panel]]`; the concept links both sources; `raw_files` and `## Raw Sources` agree; provider index directly catalogs both sources. No duplicate or missing Group B route found.

**Concrete repair:** none.
