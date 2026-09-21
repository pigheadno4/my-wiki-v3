# Braintree C12 close audit

Result: PASS. Ten approved sources promoted;20/20 fixed query questions passed.
First-pass content9/10; ten initial full reviews and one targeted correction
review. No full retry review, query repair or coordinator semantic repair.

## Mechanical close

Verified all10 source/candidate/receipt equality, approved reviews and suggestions,
raw SHA-256/canonical URL/located quotes, exact factual raw backlinks and unique
raw ownership; all approved concept snippets present once, source-to-concept
backlinks, new company/index entries once, and root/provider navigation.
Generic typed-page validation passed16 files:10 sources,4 existing concepts,
company and provider log. Count91=75 website+16 GitHub sources, excluding
changelogs. git diff --check passed. Raw and GitHub source files unchanged by C12.
No documentation-only code suite, separate three-page audit or default third
coordinator raw reread. Final audit group correctly rejected the question's
mandatory-action premise and retained the raw's can-now-be-created wording.

## Fixed query evidence

# Braintree C12 query audit — Group A (Dispute Text Evidence / Merchant Account Create)

Scope: exactly the four fixed Group A questions from C12 selection review. Both selected raws were read completely; the cited Finalize authority was also read completely for the retained submission boundary.

Timing (UTC): actual start `2026-09-21T12:52:33Z`; analysis end `2026-09-21T12:52:57Z`; handoff `2026-09-21T12:53:09Z`.

## `dispute-add-text-evidence-node`

Actual route: `wiki/index.md` (`## Concepts (generic)` → `[[disputes]]`) → `wiki/concepts/disputes.md` (`## Sources` → `[[source-braintree-dispute-add-text-evidence-node]]`) → `wiki/sources/braintree/source-braintree-dispute-add-text-evidence-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/dispute/add-text-evidence/node-2026-09-16.md`.

1. **Where is Node dispute text-evidence addition documented?**
   - **Object/action match:** adds one text-evidence item to a dispute through the Node gateway; this is not file evidence or final submission.
   - **Direct answer:** `source-braintree-dispute-add-text-evidence-node.md` documents `gateway.dispute.addTextEvidence()` and routes to the exact collected request reference. The primary example passes a dispute ID and plain text; categorized examples pass the dispute ID plus a `{ category, content }` object.
   - **Exact locator:** selected raw `# Dispute: Add Text Evidence > first ### Promise`, lines 21–40; categorized form under `## Examples > ### Submitting categorized evidence > ### Node`, lines 201–220.
   - **Verdict:** PASS — the live generic concept → source → raw route lands on the requested Node evidence-addition action.

2. **What access/status restrictions and evidence-content routes are documented, and how is adding evidence distinguished from final submission?**
   - **Object/action match:** qualifications for adding text evidence, plus the separate action that submits accumulated evidence.
   - **Direct answer:** API dispute management is available only to merchants who can access disputes in the Braintree Control Panel, and text evidence may be added only while the dispute status is `open`. The raw supports a plain text string or categorized `{ category, content }` input; categorized evidence is conditional, may have reason-code-dependent validation, and is not required for every dispute. A successful add returns a successful result with the evidence object; otherwise validation errors apply. `addTextEvidence()` adds an item but does not establish final submission or a status transition. The fully read Finalize authority states that `gateway.dispute.finalize()` is required to submit evidence to the banks and changes an `Open` dispute to `Disputed`.
   - **Exact locator:** selected Add Text Evidence raw lines 16–20 (access/status), 23–39 (plain input and result), 42–47 (categorized-evidence qualifications), 49–195 (category/content guidance), and 201–220 (categorized examples). Supporting Finalize raw line 19 (bank submission and `Disputed` transition) and lines 20–21 (required finalize call).
   - **Verdict:** PASS — access, status, content routes, and the cross-operation submission boundary are directly supported without treating the category table as a promoted schema inventory.

## `merchant-account-create-node`

Actual route: `wiki/index.md` (`[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-merchant-account-create-node]]`) → `wiki/sources/braintree/source-braintree-merchant-account-create-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/merchant-account/create/node-2026-09-16.md`.

3. **Where is Node merchant-account creation documented?**
   - **Object/action match:** demonstrates general `merchantAccount.create()` request examples; it is not listing, lookup, update, or currency-specific Braintree Auth creation.
   - **Direct answer:** `source-braintree-merchant-account-create-node.md` documents callback and Promise forms of `gateway.merchantAccount.create(merchantAccountParams)` and routes to the exact collected request raw.
   - **Exact locator:** selected raw `# Merchant Account: Create > ### Callback`, lines 18–62; `> ### Promise`, lines 64–108, with invocations at lines 60 and 106.
   - **Verdict:** PASS — the provider-index → server-SDK concept → source → raw route lands on the requested creation examples.

4. **What identity/funding/agreement inputs and result handling do the examples establish without implying universal onboarding eligibility?**
   - **Object/action match:** the displayed creation-request categories and handler signatures, not an onboarding contract or exhaustive field definition.
   - **Direct answer:** both worked examples group individual identity/address, business identity/address, bank-oriented funding, `tosAccepted`, `masterMerchantAccountId`, and a requested `id`, then pass that object to `merchantAccount.create()`. The callback receives `err` and `result`; the Promise resolves to `result`. Both bodies are empty, so the page establishes no result fields, success/failure implementation, approval, activation, funding readiness, transaction eligibility, universal requiredness, or eligibility for every merchant.
   - **Exact locator:** selected raw callback example lines 21–60 and Promise example lines 67–106; empty handlers at lines 60 and 106.
   - **Verdict:** PASS — the answer preserves example status and result limits without converting displayed values into universal onboarding rules.

## Shared gap and completeness check

- Full evidence read: selected Add Text Evidence and Merchant Account Create raws were read from provenance header to final line. The linked Finalize source/raw was read completely because the retained source makes a factual cross-operation final-submission claim. Raw identities: Add Text Evidence `9cdec2627715752cecf0a72e11560bc23b8eae93eeee7abe94275021cbd7bd06`; Merchant Account Create `c128567d3f0ab050d8c0630ea9d515c767def03b33616a902b64e47f4064e0cb`; Finalize `649ec4f5a44e839f45a13090faf190763df165d58a25397af55f0ac598be31dc`.
- Bounded gap sweep: filename and distinctive-text searches surfaced adjacent dispute evidence-requirements/file-evidence and Marketplace onboarding/create material, plus the currency-specific merchant-account operation. The fixed questions are answered by the selected raws and the explicit Finalize authority; adjacent pages were not needed and were not imported as factual evidence.
- Route integrity: the root generic `disputes` concept lists Add Text Evidence and Finalize under `## Sources`; the Braintree provider index routes to `braintree-server-sdk`, whose `## Related` section lists Merchant Account Create. Each selected source links its exact raw and reciprocal main concept.
- Completeness: 4/4 fixed questions answered; each includes object/action match, direct answer, exact locator, and verdict. No route or evidence repair is required.

**Group verdict: PASS (4/4).**

# Braintree C12 query audit — Group B

- Scope: four of 20 fixed questions; Merchant Account Create For Currency + Merchant Account Update.
- `start_utc`: `2026-09-21T12:45:44Z`
- `analysis_end_utc`: `2026-09-21T12:46:22Z`
- `handoff_utc`: `2026-09-21T12:46:29Z`
- Aggregate company/provider-index/log/count work: pending; not part of this audit.

## Merchant Account Create For Currency (Node.js)

Route: [[index]] → [[braintree-index]] → [[braintree-server-sdk]] → [[source-braintree-merchant-account-create-for-currency-node]] → [[raw/braintree/docs/reference/request/merchant-account/create-for-currency/node-2026-09-16]].

1. **Navigation question — Where is Node merchant-account creation for a currency documented?**
   - Object/action match: Node.js currency-specific merchant-account creation, not general merchant onboarding or ordinary merchant-account creation.
   - Direct answer: `[[source-braintree-merchant-account-create-for-currency-node]]`, backed by `[[raw/braintree/docs/reference/request/merchant-account/create-for-currency/node-2026-09-16]]`, documents `gateway.merchantAccount.createForCurrency()`.
   - Exact locator: raw `# Merchant Account: Create For Currency`, lines 13–19; callback and Promise examples at lines 24–56.
   - Verdict: **PASS**.

2. **Detail question — What Braintree Auth availability restriction and currency/input/result guidance is stated?**
   - Object/action match: availability, displayed authentication/currency input, and result handling for currency-specific account creation.
   - Direct answer: the method is supported only for merchants using Braintree Auth. Both displayed variants construct `BraintreeGateway` with `accessToken: merchantAccessToken`, pass `{ currency: 'USD' }` to `createForCurrency()`, test `result.success`, and on success read `result.merchantAccount.currencyIsoCode`. The callback form exposes `err`; the Promise form resolves `result`. An unsupported `currency` returns a validation error, with separate validation-error and currency-support references for exact details. The page does not establish general onboarding eligibility, arbitrary currency support, or a complete request/result schema.
   - Exact locator: Braintree Auth restriction at lines 18–19; callback input/result handling at lines 24–39; Promise input/result handling at lines 41–56; unsupported-currency routes at line 57 and related navigation at lines 58–62.
   - Verdict: **PASS**.

## Merchant Account Update (Node.js)

Route: [[index]] → [[braintree-index]] → [[braintree-server-sdk]] → [[source-braintree-merchant-account-update-node]] → [[raw/braintree/docs/reference/request/merchant-account/update/node-2026-09-16]].

3. **Navigation question — Where is Node merchant-account updates documented?**
   - Object/action match: Node.js update of an identified merchant account, not account creation or onboarding.
   - Direct answer: `[[source-braintree-merchant-account-update-node]]`, backed by `[[raw/braintree/docs/reference/request/merchant-account/update/node-2026-09-16]]`, demonstrates `gateway.merchantAccount.update()`.
   - Exact locator: raw `# Merchant Account: Update`, lines 13–33.
   - Verdict: **PASS**.

4. **Detail question — What account identifier, changes and result handling are shown, and which wider update effects are not established?**
   - Object/action match: only the identifier, update object, callback, and outcome shown by this worked update example.
   - Direct answer: the example calls `gateway.merchantAccount.update("blue_ladder_store", merchantAccountParams, callback)`; the parameter object sets `individual.firstName` to `"Jane"`. The callback exposes `err` and `result`, reads `result.success`, and the comment shows `true`. If the merchant account cannot be found, the page routes to `notFoundError`. It does not establish general identifier format, all updateable fields, unsuccessful-result/error handling, universal eligibility, validation rules, or effects on approval, verification, funding, settlement, existing transactions, agreements, or activation.
   - Exact locator: response-object route at line 15; parameter object at lines 21–25; identifier/invocation/callback/result check at lines 27–30; not-found route at line 33; Marketplace/sub-merchant navigation at lines 36–40.
   - Verdict: **PASS**.

## Shared gap sweep and route check

- Both selected evidence files were read completely. Each promoted source's `## Related raw API references` routes were inspected.
- Filename sweep found general merchant-account create/all/find pages plus Braintree Auth, Marketplace, onboarding, funding, processing, response, and validation guides. No extra full read was selected: the direct endpoint raws answer these four questions. Adjacent pages would be needed only for exact supported currencies, validation payloads, onboarding eligibility, funding behavior, complete response fields, or wider Marketplace effects, none of which is claimed here.
- No older snapshot of either exact canonical endpoint appeared in the sweep.
- Reciprocal links resolve from `[[braintree-server-sdk]]` to both promoted sources; each source resolves to its exact path-qualified raw and provides local navigation-only routes for the authorities it names. `[[braintree-index]]` routes to the concept. Direct provider-index source entries remain pending aggregate work and are not required for these actual routes.

## One shared completeness check

All four fixed questions include object/action match, direct answer, exact raw locator, and verdict. Each page has one actual route. Full selected evidence reads, filename/related-reference gap sweep, reciprocal-link checks, Braintree Auth restriction, displayed currency/input/result handling, update identifier/change/result handling, not-found route, and wider-effect boundaries are present without optional schema inventory. Result: **4/4 PASS; no repair or promotion recommendation from this group.**

# Braintree C12 query audit — Group C (Merchant Account All / Find)

Scope: exactly the four fixed Group C questions from C12 selection review. Both selected raw pages were read completely; navigation-only response and exception references were not used as factual evidence.

Timing (UTC): actual start `2026-09-21T12:54:27Z`; analysis end `2026-09-21T12:54:36Z`; handoff `2026-09-21T12:54:44Z`.

## `merchant-account-all-node`

Actual route: `wiki/index.md` (`[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-merchant-account-all-node]]`) → `wiki/sources/braintree/source-braintree-merchant-account-all-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/merchant-account/all/node-2026-09-16.md`.

1. **Where is Node merchant-account listing documented?**
   - **Object/action match:** retrieves the merchant-account collection through the Node gateway; it is not single-account find or account creation/update.
   - **Direct answer:** `source-braintree-merchant-account-all-node.md` documents `gateway.merchantAccount.all()` and routes to the exact collected request raw. The page identifies the result as a collection of Merchant Account objects.
   - **Exact locator:** selected raw `# Merchant Account: All`, line 15 (collection identity); `> ### Node`, lines 16–30, with the invocation at lines 25–29.
   - **Verdict:** PASS — the live provider-index → server-SDK concept → source → raw route lands on the requested listing action.

2. **How are the returned account collection and callback consumed without importing account-creation behavior?**
   - **Object/action match:** callback consumption of the returned collection only.
   - **Direct answer:** the callback receives `err` and `merchantAccounts`, calls `merchantAccounts.forEach()`, and logs each `merchantAccount.currencyIsoCode`. The example does not inspect `err` or establish filtering, ordering, pagination, empty/failure semantics, request inputs, eligibility, side effects, creation, update, or account lifecycle behavior.
   - **Exact locator:** selected raw `# Merchant Account: All > ### Node`, lines 25–29; collection identity at line 15. The separate Merchant Account response reference is routed by line 15 but was not imported as response-schema evidence.
   - **Verdict:** PASS — the answer stays within displayed collection consumption and explicitly avoids account-creation behavior.

## `merchant-account-find-node`

Actual route: `wiki/index.md` (`[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-merchant-account-find-node]]`) → `wiki/sources/braintree/source-braintree-merchant-account-find-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/merchant-account/find/node-2026-09-16.md`.

3. **Where is Node single merchant-account lookup documented?**
   - **Object/action match:** looks up one merchant account by identifier through the Node gateway; it is distinct from collection listing.
   - **Direct answer:** `source-braintree-merchant-account-find-node.md` documents `gateway.merchantAccount.find("theMerchantAccountId", callback)` and routes to the exact collected request raw.
   - **Exact locator:** selected raw `# Merchant Account: Find > ### Node`, lines 19–24; invocation and callback at lines 21–23.
   - **Verdict:** PASS — the live route lands on the requested single-account lookup action.

4. **What identifier, callback and not-found guidance is stated, and where are response details routed?**
   - **Object/action match:** the displayed find identifier, callback signature, and missing-account navigation.
   - **Direct answer:** the example passes the illustrative string `theMerchantAccountId`; it does not define identifier format, origin, or validation. The callback receives `err` and `merchantAccount`, but its body contains only `handle result`, so no response fields, success check, or implemented error handling are shown. When the account cannot be found, the page routes to the Node `notFoundError`. Merchant-account response details are routed separately to the Merchant Account response reference.
   - **Exact locator:** selected raw line 16 (Merchant Account response route), lines 21–23 (identifier/callback), and line 25 (Node `notFoundError` route).
   - **Verdict:** PASS — the direct answer preserves lookup scope and gives verified response/not-found destinations without importing their unread detail.

## Shared gap and completeness check

- Full selected evidence read: both request raws were read from provenance header through final line. Raw identities match the promoted sources: All `9833645573bf5554df302a1def3c97d9ff770133d477162b99192f82065bb5d9`; Find `92de84650c126047627f0e7eda38810fa9dc134121c1bb4f1e4e2168f3ce079e`.
- Bounded gap sweep: filename and distinctive-text searches surfaced the selected All/Find raws plus adjacent Create, Update, Merchant Account response, and Node exceptions references. The fixed questions ask only where response/not-found details are routed, not for those pages' schemas or exception semantics, so no additional factual raw was selected.
- Route integrity: the root index exposes `[[braintree-index]]`; the provider index exposes `[[braintree-server-sdk]]`; that concept lists both selected sources under `## Related`; each source links its exact raw and reciprocal main concept.
- Completeness: 4/4 fixed questions answered; each includes object/action match, direct answer, exact locator, and verdict. No route or evidence repair is required.

**Group verdict: PASS (4/4).**

# Braintree C12 query audit — Group D (Grant API / OAuth Webhooks)

Scope: exactly the four fixed Group D questions from C12 selection review. Both selected raw pages were read completely; the bounded gap sweep did not expand the factual evidence set.

Timing (UTC): actual start `2026-09-21T12:56:31Z`; analysis end `2026-09-21T12:56:50Z`; handoff `2026-09-21T12:57:03Z`.

## `webhooks-grant-api-node`

Actual route: `wiki/index.md` (`[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-webhooks]]`) → `wiki/concepts/braintree-webhooks.md` (`## Sources` → `[[source-braintree-webhooks-grant-api-node]]`) → `wiki/sources/braintree/source-braintree-webhooks-grant-api-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/general/webhooks/grant-api/node-2026-09-16.md`.

1. **Where is Node Grant API webhooks documented?**
   - **Object/action match:** documents notifications about previously granted payment instruments; it does not perform grant or revoke operations.
   - **Direct answer:** `source-braintree-webhooks-grant-api-node.md` routes to the exact Node Grant API webhook reference, whose Notification kinds section identifies the event conditions and whose Attributes section describes payload categories.
   - **Exact locator:** selected raw `# Grant API > ### Notification kinds`, lines 17–39; `> ### Attributes`, lines 42–46.
   - **Verdict:** PASS — the live provider-index → webhooks concept → source → raw route lands on the requested Grant API notification evidence.

2. **Which granted-instrument event conditions and payload categories are documented, distinct from granting or revoking access?**
   - **Object/action match:** webhook event conditions and payload categories after a grant relationship exists, not instructions or authority to grant/revoke.
   - **Direct answer:** `granted_payment_instrument_update` fires when a payment instrument previously granted to another Braintree merchant is updated; its `kind` is `GrantorUpdatedGrantedPaymentMethod` or `RecipientUpdatedGrantedPaymentMethod` according to which side receives the webhook. `granted_payment_instrument_revoked` is triggered when the grantor revokes a previously granted instrument. The concatenated Attributes rendering describes broad categories: notification kind/time, Vault/payment-method references, revoked PaymentMethod, owning/recipient merchant identifiers, updated-instrument nonce and nonce-use state, and updated-field names. It does not safely map every category to a webhook kind; the separate Grant API webhook guide owns kind-specific attributes. These notifications report events and do not document how to grant or revoke access.
   - **Exact locator:** selected raw lines 23–39 (update/revocation conditions and side-qualified kinds); lines 42–46 (concatenated payload categories and kind-specific guide route).
   - **Verdict:** PASS — event conditions and broad payload categories remain accurate without reconstructing damaged field structure or importing grant/revoke operations.

## `webhooks-oauth-node`

Actual route: `wiki/index.md` (`[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-webhooks]]`) → `wiki/concepts/braintree-webhooks.md` (`## Sources` → `[[source-braintree-webhooks-oauth-node]]`) → `wiki/sources/braintree/source-braintree-webhooks-oauth-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/general/webhooks/oauth/node-2026-09-16.md`.

3. **Where is Node OAuth webhooks documented?**
   - **Object/action match:** documents parsing the OAuth access-revocation notification for a connected merchant; it does not perform OAuth revocation or trigger delivery.
   - **Direct answer:** `source-braintree-webhooks-oauth-node.md` routes to the exact Node OAuth webhook reference. The raw contains availability, notification-kind, attribute, callback-parse, and Promise-parse sections.
   - **Exact locator:** selected raw `# OAuth`, lines 14–18; `> ### Notification kinds`, lines 23–33; `> ### Attributes`, lines 36–38; parsing examples at lines 39–82.
   - **Verdict:** PASS — the live route lands on the requested OAuth webhook evidence and preserves parsing versus event generation.

4. **What production/sandbox availability and event/payload qualifications are stated?**
   - **Object/action match:** OAuth webhook beta availability, sole documented event condition, payload categories, and displayed parsing behavior.
   - **Direct answer:** OAuth is closed beta in production and open beta in sandbox. The sole documented event is `oauth_access_revocation`, triggered when a connected merchant revokes API access; no other OAuth event kind is established. Payload categories are notification kind, UTC trigger time, connected merchant ID, and OAuth application client ID. Callback and Promise examples configure Sandbox, parse `btSignature`/`btPayload`, show `OAuthAccessRevoked`, and read `notification.oauthAccessRevocation.merchantId`; the Sandbox example does not override the separate production/sandbox availability statement or prove the code triggers delivery.
   - **Exact locator:** selected raw `# OAuth > AVAILABILITY`, lines 17–18; `> ### Notification kinds`, lines 23–33; `> ### Attributes`, lines 36–38; callback example lines 44–62 and Promise example lines 64–82.
   - **Verdict:** PASS — beta environments, event scope, payload categories, and parse-only behavior are directly supported and correctly qualified.

## Shared gap and completeness check

- Full selected evidence read: both webhook raws were read from provenance header through final line. Raw identities match the promoted sources: Grant API `2e827fb7e15bc040c40285099e8cccd2035e962e8c8c2911228799fc99a4203b`; OAuth `429fbef83ca7a057dfba2e85c9850e869da515db157e40c1cd120964e7e7f6e2`.
- Bounded gap sweep: filename and distinctive-text searches surfaced the selected webhook raws plus adjacent webhook parsing, payment-method grant/revoke, and OAuth overview/access-token materials. The fixed questions concern notification evidence and are fully answered by the selected raws; adjacent operation/setup pages were not imported as factual evidence.
- Route integrity: the root index exposes `[[braintree-index]]`; the provider index exposes `[[braintree-webhooks]]`; that concept lists both sources under `## Sources`; each source links its exact raw and reciprocal main concept.
- Completeness: 4/4 fixed questions answered; each includes object/action match, direct answer, exact locator, and verdict. No route or evidence repair is required.

**Group verdict: PASS (4/4).**

# C12 query audit — Group E

- Scope: the four fixed Group E questions from `selection-review.md` (4 of 20 campaign questions).
- Start UTC: `2026-09-21T12:59:56Z`
- Analysis end UTC: `2026-09-21T13:01:24Z`
- Handoff UTC: `2026-09-21T13:02:04Z`
- Aggregate note: campaign aggregate files were pending during this audit; the promoted concept routes were used.

## Route: Local Payment Methods webhooks

`wiki/index.md:11` → `wiki/braintree-index.md:131` → `wiki/concepts/braintree-webhooks.md:22` → `wiki/sources/braintree/source-braintree-webhooks-local-payment-methods-node.md:43-45` → `raw/braintree/docs/reference/general/webhooks/local-payment-methods/node-2026-09-16.md`

### 1. Where is Node local-payment-method webhooks documented?

- Object/action match: Node.js Local Payment Method webhook notification kinds and payload guidance.
- Direct answer: The documentation is the Braintree Node.js **Local Payment Methods** webhook reference, retained through the Braintree Webhooks concept and its source page.
- Exact locator: raw `# Local Payment Methods > ### Notification kinds`, lines 17-28; source raw backlink at lines 43-45.
- Verdict: **PASS**

### 2. How do instant and non-instant events differ, and which event requires a separate transaction-creation action?

- Object/action match: event meanings for instant versus non-instant local payments, plus the follow-on sale action.
- Direct answer: Instant events are `local_payment_completed` (customer approved, funds withdrawn) and `local_payment_reversed` (payment reversed and purchase amount refunded). Non-instant events are `local_payment_funded` (buyer completed payment) and `local_payment_expired` (payment expired). No event is stated to **require** transaction creation: for `local_payment_completed`, the page says a transaction **can now be created** through `Transaction: Sale` with the `payment_method_nonce`. That action is available and separate, not automatic or stated as mandatory; the nonce is completion-only, and the non-instant event descriptions do not inherit this action.
- Exact locator: raw notification table lines 23-28, especially line 25; nonce qualification in the damaged concatenated attributes rendering at lines 31-35, without reconstructing unnamed fields.
- Verdict: **PASS**

## Route: Settlement Batch Summary generation

`wiki/index.md:11` → `wiki/braintree-index.md:134` → `wiki/concepts/braintree-server-sdk.md:41` → `wiki/sources/braintree/source-braintree-settlement-batch-summary-generate-node.md:44-46` → `raw/braintree/docs/reference/request/settlement-batch-summary/generate/node-2026-09-16.md`

### 3. Where is Node settlement batch summary generation documented?

- Object/action match: Node.js generation of a Settlement Batch Summary report.
- Direct answer: The documentation is the Braintree Node.js **Settlement Batch Summary: Generate** request reference, retained through the Braintree Server SDK concept and its source page.
- Exact locator: raw `# Settlement Batch Summary: Generate`, lines 13-17; source raw backlink at lines 44-46.
- Verdict: **PASS**

### 4. What date/grouping/report scope and result access are documented, distinct from submitting a transaction for settlement?

- Object/action match: date-scoped batch reporting, optional example grouping, and callback/Promise result access—not transaction settlement submission.
- Direct answer: `gateway.settlementBatchSummary.generate()` is shown with `settlementDate: "2012-01-01"` and `groupByCustomField: "custom_field_1"`. The report displays total sales and credits for each batch for a particular date, and transactions can be grouped by one custom field's values. Callback and Promise examples access `result.settlementBatchSummary.records`; incorrect arguments may yield validation errors. This reporting page does not document `transaction.submitForSettlement()` or establish transaction-level settlement eligibility, state changes, or submission effects.
- Exact locator: raw report scope at line 17; callback example and records access at lines 18-26; Promise example and records access at lines 28-36; validation route at lines 38-40.
- Verdict: **PASS**

## Shared route and gap checks

- Both routes resolve through the actual root index, Braintree provider index, owning concept, promoted source, and source-owned raw backlink.
- Filename/content gap sweep found the selected exact Node pages plus related local-payment guides and Settlement Batch Summary response, custom-field, and submit-for-settlement pages. Those adjacent pages are navigation-only and are not needed to answer the four fixed questions; no adjacent factual authority was imported.
- The Local Payment Methods raw attributes section has damaged concatenated rendering and unnamed trailing `Authorized`/`Settled` values, so no payload schema was reconstructed.
- Settlement Batch Summary reporting remains distinct from transaction submission for settlement.

## Completeness

All four fixed questions contain one route/page context, object/action match, direct answer, exact locator, and verdict. Result: **4/4 PASS**. No repair or additional promotion is required from this audit.
