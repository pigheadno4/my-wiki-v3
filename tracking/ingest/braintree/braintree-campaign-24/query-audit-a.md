# Braintree C24 fixed-query audit — Group A

Scope: Article Overview + Plans. Result: **4/4 PASS**.

## Routes

- **Article Overview:** `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-recurring-billing.md` → `wiki/sources/braintree/source-braintree-recurring-article-overview.md` → `raw/braintree/articles/guides/recurring-billing/overview-2026-09-16.md`
- **Plans:** `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-recurring-billing.md` → `wiki/sources/braintree/source-braintree-recurring-article-plans.md` → `raw/braintree/articles/guides/recurring-billing/plans-2026-09-16.md`

## Exact questions

### 1. Where is the article-level recurring-billing overview?

- **Object/action match:** Article-level recurring-billing overview; matched the `/articles/` page, not the separate developer-guide overview.
- **Direct answer:** Follow the Article Overview route above to `source-braintree-recurring-article-overview.md`, then its pinned raw article.
- **Exact raw locator:** `overview-2026-09-16.md`, source URL line 1; slug lines 6–9; `# Overview` line 14.
- **Verdict:** **PASS**

### 2. What scope and prerequisites does this article itself state?

- **Object/action match:** Scope and prerequisites stated by the overview article itself; matched the pinned article raw.
- **Direct answer:** Recurring billing automatically charges customers in monthly increments. Setup requires a plan created in the Control Panel or via the API and a customer stored in the Vault; the customer's preferred payment method is then associated with the plan to create a subscription. The article identifies plans, customers, and subscriptions as the three elements: plans define cycle length/date/default cost and expiration cycles; customers include a payment method and may link to multiple subscriptions; subscriptions use a specific payment method and may differ from the original plan.
- **Exact raw locator:** `overview-2026-09-16.md`, `# Overview` line 16; three elements and their roles at lines 18–41.
- **Verdict:** **PASS**

### 3. Where is the recurring-billing plans article?

- **Object/action match:** Article-level plans page; matched the `/articles/` page, not the separate Node guide or Plan API references.
- **Direct answer:** Follow the Plans route above to `source-braintree-recurring-article-plans.md`, then its pinned raw article.
- **Exact raw locator:** `plans-2026-09-16.md`, source URL line 1; slug lines 6–9; `# Plans` line 14.
- **Verdict:** **PASS**

### 4. What plan setup and constraints does this article itself state?

- **Object/action match:** Plan setup and constraints stated by the plans article itself; matched the pinned article raw.
- **Direct answer:** A plan is required before creating subscriptions and acts as a template for amount, currency, and billing cycle. The Control Panel creation flow includes billing date, number of billing cycles, add-ons or discounts, and trial periods, with an explicit instruction to read trial risks and requirements first. On an existing plan, the billing cycle cannot be changed, while the article says other elements can be; updates affect only new subscriptions, not existing ones. EU merchants must give four weeks' notice before a recurring-plan price change and before billing after six or more months since the last payment; the article says those notices are not required outside the EU but remain good practice. Deletion is Control-Panel-only and is blocked when any former or current subscription is associated with the plan.
- **Exact raw locator:** `plans-2026-09-16.md`, plan prerequisite/template line 16; `## Creating a plan` lines 19–42; `## Updating a plan` lines 47–63; `## Deleting a plan` lines 68–77.
- **Verdict:** **PASS**

## Shared checks

- **Pinned evidence:** Both raw files were read completely. SHA-256 matches the manifest: overview `f80f41e4f4752901623fc769a1f9931a3e0c54f2dbcf013f5fff5d8b0de5f79d`; plans `a3eafcc71ca5f7a0db2824c1026dcfbc2b4aabbd7a5ac8c6d09363b6ca332062`.
- **Bounded gap sweep:** A filename/content sweep of the Braintree recurring-billing routes found the separate developer-guide overview and Node plans guide plus adjacent API references. They are different evidence objects and were not needed for these questions, which explicitly ask about the article pages themselves; no extra full read was selected. No older same-canonical article snapshot was found.
- **Reciprocal links:** Root index routes to `braintree-index`; the provider index routes to both the concept and both source pages; the concept routes to both sources; each source links back to `braintree-recurring-billing` and to its exact pinned raw. **PASS**.
