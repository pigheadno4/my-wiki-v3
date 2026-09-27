# Braintree C18 fixed query audit — Group D

Scope: exactly the four fixed Group D questions for Vault Overview and Create New Customers. Both promoted source pages and both pinned raws were read completely. The repository remained read-only.

## `control-panel-vault-overview`

Actual concept-led route: `wiki/index.md` (`## PSP Indexes`, line 11 → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts`, line 198 → `[[braintree-control-panel]]`) → `wiki/concepts/braintree-control-panel.md` (`## Sources`, line 19 → `[[source-braintree-control-panel-vault-overview]]`) → `wiki/sources/braintree/source-braintree-control-panel-vault-overview.md` (`raw_files`, lines 7–8; `## Raw Sources`, lines 50–52) → `raw/braintree/articles/control-panel/vault/overview-2026-09-16.md`.

1. **Where is Braintree Control Panel Vault overview documented?**
   - **Object/action match:** Braintree's collected Control Panel Vault overview, not customer creation, customer/payment-method update, card verification, recurring-billing setup, or an API operation.
   - **Direct answer:** The promoted `source-braintree-control-panel-vault-overview.md` retrieval entry routes to the complete collected `# Overview` raw at the path above.
   - **Exact raw locator:** provenance and canonical identity at lines 1 and 6–7; page identity at line 14; Vault purpose at lines 16–18.
   - **Verdict:** PASS.

2. **Which Vault administration routes does this overview identify, and what does it leave to dedicated pages?**
   - **Object/action match:** overview-level Vault administration and export routes; not the procedure, permission, eligibility, or outcome for a specific create, update, delete, search, verification, or payment action.
   - **Direct answer:** The overview says a stored customer Vault record can be updated, deleted, and searched, but gives no procedures. It gives one concrete export route—Control Panel → **Reports** → **Vault** → the desired **Export** option → date range → **Filter And Download**—for three distinct outputs: customers, customers with payment-method tokens, and customers with addresses. Exports are limited to 40,000 rows, and opening the download in Excel or another spreadsheet program may omit rows because of the program's limits. The overview separately states that stored payment-method data is encrypted and associated with a token, and that CVV is never stored; it does not establish create/update/card-verification steps, permissions, supported methods, or outcomes, which the promoted source routes to dedicated pages as navigation-only. A recurring ECI shown on a statement does not itself mean future recurring-payment enrollment.
   - **Exact raw locator:** `## How it works`, lines 23–29; `## Exporting Vault records`, lines 34–55; `## Charge shows as recurring on customer statement`, lines 60–62.
   - **Verdict:** PASS.

## `control-panel-vault-create`

Actual concept-led route: `wiki/index.md` (`## PSP Indexes`, line 11 → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts`, line 198 → `[[braintree-control-panel]]`) → `wiki/concepts/braintree-control-panel.md` (`## Sources`, line 21 → `[[source-braintree-control-panel-vault-create]]`) → `wiki/sources/braintree/source-braintree-control-panel-vault-create.md` (`raw_files`, lines 7–8; `## Raw Sources`, lines 49–51) → `raw/braintree/articles/control-panel/vault/create-2026-09-16.md`.

3. **Where is creating customers in Braintree Control Panel Vault documented?**
   - **Object/action match:** creation of a new Vault customer record through the Control Panel, optionally with a credit card; not adding a payment method later to an existing customer, updating a record, proving card-verification success, or authorizing/settling a transaction.
   - **Direct answer:** The promoted `source-braintree-control-panel-vault-create.md` retrieval entry routes to the complete collected `# Create New Customers` raw at the path above.
   - **Exact raw locator:** provenance and canonical identity at lines 1 and 6–7; page identity and the Control Panel/API entry routes at lines 14–22.
   - **Verdict:** PASS.

4. **Which creation steps and resulting Vault or payment-method boundaries does this page document?**
   - **Object/action match:** the page's new-customer creation choices and resulting customer/payment-method boundaries; not later payment-method attachment, card-verification outcome, purchase authorization, or settlement.
   - **Direct answer:** The page identifies three entry routes: select **Store in Vault** while creating a transaction; choose **Vault** → **New Customer** in the Control Panel; or use the separate API route. In direct Control Panel creation, the user chooses to save the customer with or without a payment method. Including a payment method requires card number and expiration date. At this collected snapshot, the Control Panel stores only credit-card payment methods; other payment methods must use the API. Card verification is recommended when saving a credit or debit card, but this page does not prove verification success or payment authorization; only when verification is enabled and the account has multiple merchant accounts does it say the user can choose the verifying merchant account. CVV may be required depending on account setup, but is never stored. A billing address is optional and is used only for applicable configured AVS rules. Thus customer creation without a payment method is not payment-method creation, and the page does not document adding a payment method later or transaction authorization/settlement.
   - **Exact raw locator:** `# Create New Customers`, lines 14–22; `## New record requirements`, lines 25–33; `## Payment method details`, lines 53–71; `## Billing address`, lines 76–82.
   - **Verdict:** PASS.

## Shared gap sweep and reciprocal-link check

- **Pinned evidence:** complete selected raws match the C18 manifest hashes: Vault Overview `501e30bad2711922aea41216e74b1740bcf9052ac18f0b865252ac340850ed77`; Create New Customers `39914aaf63788285104f2afd14e4b68281c619505a1e45269f3ecde01626ced6`. Canonical URLs agree across manifest, source frontmatter, and raw provenance. No older snapshot of either canonical page was found.
- **Bounded gap sweep:** the Vault raw inventory contains Overview, Create, Update, and Card Verification. Topic search also surfaced the separate Control Panel transaction-creation page and other different-object pages. The four fixed questions are expressly page-scoped and the two pinned raws answer them completely, so Update, Card Verification, transaction creation, customer-create API, AVS/CVV, recurring-billing, and PCI pages remain navigation-only; no extra full read was needed. No customer/payment-method, CVV, export, verification, authorization, or settlement conflict was found.
- **Reciprocal routes:** the root routes to `braintree-index`; the provider index routes to `braintree-control-panel`; that concept lists each promoted source exactly once; each source links back to the concept and to its exact pinned raw through both `raw_files` and `## Raw Sources`. The provider index also contains accurate direct source rows, but the audited concept-led routes do not depend on them.
- **Completeness:** all 4/4 fixed questions include object/action match, a direct answer, exact raw locator, and verdict. **No repair or promotion recommendation is required.**

**Group verdict: PASS (4/4).**
