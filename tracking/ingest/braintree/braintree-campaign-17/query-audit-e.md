# Braintree C17 fixed query audit — Group E

Scope: exactly the four fixed Group E questions for Control Panel Webhooks and Audit Webhooks. Both promoted source pages and both selected pinned raws were read completely. The repository remained read-only; this report was written only to `/tmp`.

## Result

**PASS (4/4).** Both raw SHA-256 values match the C17 manifest. The actual root → provider index → concept → promoted source → pinned raw chains resolve, and the provider index now also contains direct source catalog rows. The promoted pages preserve the select-partner Audit qualification, distinguish authentication/administration audit events from transaction notifications, and retain the documented Login list/table mismatch. No repair or additional promotion is required.

This audit reports only the 2026-09-16 collected evidence and does not claim current availability or behavior.

## Canonical retrieval routes and pin check

Common entry: `wiki/index.md:11` → `wiki/braintree-index.md:186` (`[[braintree-webhooks]]`) or `wiki/braintree-index.md:187` (`[[braintree-control-panel]]`) → promoted source → exact pinned raw. Direct provider catalog entries are also present at `wiki/braintree-index.md:23-24`.

| Page | Concept → source | Source → pinned raw | Manifest/hash |
| --- | --- | --- | --- |
| Control Panel Webhooks | `wiki/concepts/braintree-webhooks.md:21` and `wiki/concepts/braintree-control-panel.md:20` | `wiki/sources/braintree/source-braintree-control-panel-webhooks.md:45-47` → `raw/braintree/articles/control-panel/webhooks-2026-09-16.md` | `e97c79baf2c2fcad3571a0b074f467e1416daeeb62a2cccb97d8876889b3afb8`, exact match |
| Audit Webhooks | `wiki/concepts/braintree-webhooks.md:22` and `wiki/concepts/braintree-control-panel.md:26` | `wiki/sources/braintree/source-braintree-control-panel-audit-webhooks.md:48-50` → `raw/braintree/articles/control-panel/audit-webhooks-2026-09-16.md` | `efe18ecfd315954fbfb031e72ed53336ed083c1b5d3779823f1f8f8b3a285899`, exact match |

## Four fixed questions

### 1. Where is Braintree Control Panel Webhooks documented?

- **Object/action match:** the Control Panel article for creating and testing gateway webhook configurations, not the Node parsing API, an individual webhook event reference, or the select-partner Audit Webhooks catalog.
- **Direct answer:** follow the canonical route above to `source-braintree-control-panel-webhooks`; its canonical provider URL is `https://developer.paypal.com/braintree/articles/control-panel/webhooks`, and its factual evidence is the exact pinned raw above.
- **Exact raw locator:** canonical provenance at raw line 1 and slug at lines 6-7; page identity at `# Webhooks`, raw line 14; purpose at lines 16-18.
- **Verdict:** **PASS**.

### 2. Which Control Panel webhook configuration, permission and notification boundaries does the page document?

- **Object/action match:** configuration and test actions for the general Control Panel webhook surface; do not import audit-event kinds, SDK parsing behavior, or undocumented delivery guarantees.
- **Direct answer:** the article describes push notifications to a designated destination and lists five notification families: subscription-status changes, disbursements, transaction disputes, Braintree Marketplace sub-merchant-account status changes, and Grant API payment-method status changes. Configuration requires the exact **Manage Webhooks** role permission. The user navigates gear → **API** → **Webhooks** → **Create New Webhook**, supplies a destination URL, selects notifications, and creates the webhook. Creation is not the whole integration: the server must separately parse received notifications. An existing configuration can be tested with **Check URL**; the article warns that production testing can cause unexpected behavior if handling code does not inspect the received webhook kind. The selected page does not state HTTPS/signature requirements, timing, ordering, retry, duplicate, acknowledgement, replay, or failure-recovery semantics. It also does not establish that this general workflow or permission automatically governs select-partner Audit Webhooks.
- **Exact raw locator:** purpose/workflow `# Webhooks`, lines 16-18; families `## Types of webhooks`, lines 21-30; permission and creation flow `## Creating webhooks`, lines 33-48; testing and production warning `## Testing webhooks`, lines 51-66.
- **Verdict:** **PASS**.

### 3. Where is Braintree Control Panel Audit Webhooks documented?

- **Object/action match:** the select-partner catalog of gateway authentication and administration audit notifications, not transaction-lifecycle notifications, Braintree Auth connected-merchant webhooks, or the general Control Panel creation article.
- **Direct answer:** follow the canonical route above to `source-braintree-control-panel-audit-webhooks`; its canonical provider URL is `https://developer.paypal.com/braintree/articles/control-panel/audit-webhooks`, and its factual evidence is the exact pinned raw above.
- **Exact raw locator:** canonical provenance at raw line 1 and slug at lines 6-7; select-partner availability at `**AVAILABILITY**`, lines 14-15; audit purpose at lines 19-23.
- **Verdict:** **PASS**.

### 4. Which audit-webhook events, permissions and setup/delivery boundaries does this collected article document?

- **Object/action match:** retain the Audit article's own administration/authentication catalog and omissions; do not recast its events as payment, settlement, dispute, subscription, or other transaction notifications.
- **Direct answer:** Audit Webhooks are stated to be available **only to select partners**. The article catalogs:
  - **API:** `ip_restrictions_changed`, tokenization-key created/destroyed, API-key created/destroyed, and `two_factor_changed`.
  - **Login:** password reset, successful Control Panel login, successful SSO login, and a documented mismatch: the rendered constant list contains `UserLoginFailed`, while the table contains `user_locked_out` and no `user_login_failed` row. The two must not be treated as equivalent without further evidence.
  - **AuthZ:** role created/changed/assigned/unassigned and user-suspension status changed.
  - **OAuth:** connected-merchant API access granted and OAuth application created/changed.
  - **Fraud Protection:** AVS rules changed, CVV rules changed, risk threshold created/deleted/changed, and premium fraud protection changed.

  The only shared attributes documented are notification `kind` and the UTC `timestamp` at which it was triggered. The article says information is pushed to a designated destination and links to the separate general Create webhooks article. It states no Audit-specific required permission or setup procedure and no endpoint/transport, timing, ordering, retry, duplicate, signature, acknowledgement, replay, failure-recovery, event-specific payload, or delivery-ID semantics. The generic subscription-expiry workflow example at raw line 21 does not override the Audit event catalog or make these transaction notifications.
- **Exact raw locator:** availability lines 14-15; purpose and general-webhook route lines 19-23; `## API > ### Notifications`, lines 26-42; `## Login > ### Notifications`, lines 45-59; `## AuthZ > ### Notifications`, lines 62-77; `## OAuth > ### Notifications`, lines 80-93; `## Fraud Protection > ### Notifications`, lines 96-112; `## Shared Attributes`, lines 115-120.
- **Verdict:** **PASS**.

## Bounded gap sweep

The sweep was limited to `raw/braintree` matches for the exact names and distinguishing strings `Audit Webhooks`, `UserLoginFailed`, `user_locked_out`, `Manage Webhooks`, `Create New Webhook`, and `Check URL`. Besides the two selected raws, it surfaced discovery inventories and the linked role-permission, Node create, Node testing/go-live, and transaction-issues pages. Those are separate permission/detail, SDK implementation, or transaction-issue objects. They were not needed to answer what the two selected articles themselves document and were not imported as factual evidence. The general Webhooks raw was already one of the two fully read selected raws; although Audit links to it for general information, the Audit article does not say its permission or setup steps apply to Audit Webhooks.

No contradictory promoted or unlinked raw was found in this bounded sweep. The one internal evidence discrepancy is the Audit Login constant-list/table mismatch, which the Audit source already preserves explicitly at source lines 24-25 and the concepts/provider catalog do not flatten.

## Reciprocal-link check

- Root → provider index: present at `wiki/index.md:11`.
- Provider index → both concepts: present at `wiki/braintree-index.md:186-187`.
- Both concepts → both promoted sources: present at `wiki/concepts/braintree-webhooks.md:21-22` and `wiki/concepts/braintree-control-panel.md:20,26`.
- Each promoted source → both concepts: Control Panel Webhooks source lines 34-36; Audit Webhooks source lines 40-42.
- Each promoted source → exact raw: present and resolvable at source lines 45-47 and 48-50 respectively; `raw_files` frontmatter points to the same paths.
- Direct provider index → promoted sources: present at `wiki/braintree-index.md:23-24`.

**Group verdict: PASS (4/4); no gap or repair required.**
