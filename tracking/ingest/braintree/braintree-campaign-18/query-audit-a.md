# Braintree C18 fixed query audit — Group A

## Result

**PASS — 4/4 fixed questions pass; no repair required.** Both promoted sources and both pinned raws were read completely. The raw SHA-256 values exactly match the C18 manifest. This audit reports the 2026-09-16 collected evidence; it does not assert current availability.

## Actual routes and pin checks

| Page | Root → provider index → concept → source → raw | SHA-256 |
| --- | --- | --- |
| Important Gateway Credentials | `wiki/index.md:11` → `wiki/braintree-index.md:198` → `wiki/concepts/braintree-control-panel.md:26` → `wiki/sources/braintree/source-braintree-control-panel-important-gateway-credentials.md:47` → `raw/braintree/articles/control-panel/important-gateway-credentials-2026-09-16.md` | `a3864d08423085a2ccab84f982f2c60dd881955c32394c7bbad9e46c8a31a477` — exact manifest match |
| Custom Fields | `wiki/index.md:11` → `wiki/braintree-index.md:198` → `wiki/concepts/braintree-control-panel.md:23` → `wiki/sources/braintree/source-braintree-control-panel-custom-fields.md:59` → `raw/braintree/articles/control-panel/custom-fields-2026-09-16.md` | `2e37acb3ac5badffd8f33635daa77a9cc3639e11a2fd45fae04e55ca016311b1` — exact manifest match |

## Four fixed questions

### 1. Where are Braintree important gateway credentials documented?

- **Object/action match:** Braintree gateway credential and identifier discovery in the Control Panel, not credential values, a payment API operation, or general account login.
- **Direct answer:** Follow the Important Gateway Credentials route above to the promoted source and pinned raw; the canonical provider URL is `https://developer.paypal.com/braintree/articles/control-panel/important-gateway-credentials`.
- **Exact raw locator:** source URL at raw line 1; `# Important Gateway Credentials` and introduction at lines 14–16; credential sections at lines 19–187.
- **Verdict:** **PASS**.

### 2. Which credential types, access paths and environment or security boundaries does the collected page document?

- **Object/action match:** Identify only credentials/identifiers, their Control Panel retrieval routes, and explicit environment, access, or security limits from this page; do not supply values or infer present support.
- **Direct answer:** The four API credentials are environment, public key, private key and merchant ID. Sandbox and Production route API requests separately and use different API keys, so code must use the matching keys. Public/private keys are user-specific, form that user's API keys, and may be rotated with integration impact; find them in the matching Control Panel under gear → **API** → **API Keys**, generate a key if absent, and use **View** to reveal the private key. The private key must not be shared outside API-call use. The gateway-wide merchant ID differs by environment and is under gear → **Business** or after `/merchants/` in the logged-in URL. A merchant account ID identifies one account within the gateway, is under **Business** → **Merchant Accounts**, requires **Add/Edit Processing Options** visibility, and defaults to the gateway's default merchant account when multiple accounts exist and a request omits it; additional accounts are manually creatable only in Sandbox, while Production additions require Braintree contact. Tokenization keys are under **API** → **Tokenization Keys** and authorize client-SDK tokenization for server use. The gateway-wide CSE key is under **API** → **Client-Side Encryption Keys** and is described only for the older integration method.
- **Exact raw locator:** API credential list lines 19–27; environment/key separation and rotation lines 30–43; public/private access and confidentiality lines 48–76; merchant ID lines 79–98; merchant-account scope, default, path, permission and environment limits lines 106–154; tokenization keys lines 162–174; CSE key lines 177–187.
- **Verdict:** **PASS**.

### 3. Where are Braintree Control Panel custom fields documented?

- **Object/action match:** Control Panel custom-field definition, configuration and visibility, not the operation-specific transaction, Vault, or 3D Secure request behavior linked from the article.
- **Direct answer:** Follow the Custom Fields route above to the promoted source and pinned raw; the canonical provider URL is `https://developer.paypal.com/braintree/articles/control-panel/custom-fields`.
- **Exact raw locator:** source URL at raw line 1; `# Custom Fields` and use-case routes at lines 14–24; configuration and visibility sections at lines 27–122.
- **Verdict:** **PASS**.

### 4. Which configuration and visibility boundaries does this page document?

- **Object/action match:** State the page's custom-field setup, edit/delete eligibility, and where values or Fraud Protection Advanced fields surface; do not turn linked API use cases into setup authority.
- **Direct answer:** Pass Thru fields are configured in the Control Panel but pass values only through the API to merchant servers. Store and Pass Back values are stored in the Control Panel, returned on transaction responses, downloadable through Transaction or Vault Search, and searchable by passed value rather than field name. New definitions can be configured only in the Control Panel—not via API—by a role with **Add/Edit Processing Options**, at gear → **Account Settings** → **Transactions** → **Custom Fields / Options**. The API name used in code is at most 255 characters with no spaces or capitals; the display name appears in transaction history and Vault records. A permitted user may edit the display name or toggle the field type. Deletion is limited to fields never used to collect customer or transaction data. Fraud Protection Advanced fields must be added in its Dashboard; the Control Panel view is described as showing all **ACTIVE** fields added there.
- **Exact raw locator:** type and value visibility lines 27–41; Control-Panel-only setup, permission, path and names lines 44–66; editing lines 69–85; deletion condition/path lines 88–105; Fraud Protection Advanced Dashboard and ACTIVE visibility lines 108–122.
- **Verdict:** **PASS**.

## Group checks

- **Bounded gap sweep:** Searched `raw/braintree/` for the exact page titles/canonical URLs and credential/custom-field terms, then inspected the promoted sources' related-navigation entries. Adjacent pages cover role permissions, search, Fraud Protection Advanced, operation-specific custom-field use, tokenization-key SDK setup, environment switching and deprecated CSE libraries. The two selected raws directly and completely answer the fixed questions; no adjacent file was selected as factual evidence, so no additional full read was required. No older raw with either exact canonical URL exists.
- **Reciprocal links:** root → provider index, provider index → `braintree-control-panel`, concept → both sources, each source → concept, each `raw_files` entry → its exact existing raw, and each path-qualified `## Raw Sources` link are present and resolvable. The provider index also directly catalogs both sources. The Custom Fields navigation-only related raw links all resolve.
- **Concrete repair:** none.
