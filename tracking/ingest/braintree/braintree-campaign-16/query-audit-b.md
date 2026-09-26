# Braintree C16 Query Audit — Group B

- Scope: Control Panel Create + Clone Transactions.
- Audited: `2026-09-23T12:29:52Z`.
- Evidence: both selected raw pages read completely; current source, root/provider-index and concept routes inspected.

## Control Panel Create Transactions

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-control-panel]]` → `[[source-braintree-control-panel-transaction-create]]` → `[[raw/braintree/articles/control-panel/transactions/create-2026-09-16]]`.

1. **Query:** Where is Braintree Control Panel Create Transactions documented?
   - **Object/action match:** Manual creation in the Braintree Control Panel, distinct from the recommended API route.
   - **Direct answer:** `[[source-braintree-control-panel-transaction-create]]` is the retrieval entry; its complete evidence is the raw Create Transactions article linked above.
   - **Exact raw locator:** `# Create Transactions`, lines 14–18; `## On a new credit card`, lines 27–39; `## On an existing Vault record`, lines 42–61.
   - **Verdict:** PASS. The concept route is live; direct provider-index cataloging is pending the aggregate close.

2. **Query:** When can a merchant create a transaction in the Control Panel, and what payment-method and settlement limits apply?
   - **Object/action match:** Control Panel creation eligibility and authorization/settlement submission, not server-SDK sale semantics.
   - **Direct answer:** Braintree recommends the API but documents manual Control Panel creation. Credit/debit cards can be new or vaulted; PayPal, Apple Pay and other payment types must already be vaulted. A Vault customer can use the default method or another stored token. For authorization-only creation, clear `Submit for Settlement`. Settling above the authorized amount needs industry and processor settlement-adjustment support; the article does not establish final settlement or funding from creation or submission.
   - **Exact raw locator:** API/manual route line 16; payment-method prerequisite line 18; qualified amount ceiling lines 21–22; Vault selection lines 42–52; authorization checkbox lines 55–59.
   - **Verdict:** PASS.

## Control Panel Clone Transactions

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-control-panel]]` → `[[source-braintree-control-panel-transaction-clone]]` → `[[raw/braintree/articles/control-panel/transactions/clone-2026-09-16]]`.

3. **Query:** Where is Braintree Control Panel Clone Transactions documented?
   - **Object/action match:** Clone an existing transaction in the Control Panel, not the separate SDK/API clone operation.
   - **Direct answer:** `[[source-braintree-control-panel-transaction-clone]]` is the retrieval entry and links the full raw Clone Transactions article.
   - **Exact raw locator:** `# Clone Transactions`, lines 14–18; `## Compatibility`, lines 21–30; `## Cloning a transaction`, lines 33–52.
   - **Verdict:** PASS. The concept route is live; direct provider-index cataloging is pending the aggregate close.

4. **Query:** Which existing transactions can be cloned in the Control Panel, and what is copied versus entered anew?
   - **Object/action match:** Control Panel clone compatibility and inputs, with no API-method inference.
   - **Direct answer:** A compatible original contributes its transaction information, including the payment method; the new amount is entered, plus CVV if applicable. PayPal/Apple Pay/Google Pay/Venmo transactions, Vault-origin transactions, and `Processor Declined`, `Failed`, `Gateway Rejected` or `Settling` statuses are excluded. Fraud/Risk Threshold gateway rejections have the stated narrow mistaken-fraud exception. Vault-origin charges should instead be created from the Vault record. The user may need both Create Sales and Submit Sales for Settlement permissions. No supplied CVV means no CVV check, even when rules are enabled. Clearing `Submit for Settlement` creates an authorization-only path, not proof of settlement or funding.
   - **Exact raw locator:** copied information and amount lines 16–18; exclusions lines 23–28; narrow exception line 30; amount/CVV and submission choice lines 43–48; permissions lines 51–52; CVV behavior lines 57–59.
   - **Verdict:** PASS.

## Bounded gap sweep

- Searched current Braintree concept/source routes for Control Panel create/clone and the separate Node clone reference. No wrong-object route or material contradiction affects these four fixed questions; API/SDK references remain navigation-only for these two sources.
- Both source pages link their full raw evidence and have reciprocal `[[braintree-control-panel]]` entries. No missing scope warning, broken route or answer gap found. Group B: **4/4 PASS**.
