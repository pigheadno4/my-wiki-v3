# Braintree C11 quality audit

Final result:20/20 fixed queries PASS across ten pages; five groups form one
audit, not five extra audits. Selected raw reads were complete; no extra raw
selected in audits, no source repair or unresolved query. Group B's incorrect
concept-section labels were corrected by its auditor to Related, with root
router verified; this was report-only, not source retry or another full audit.
Coordinator checked all question identities, direct answers, locators and routes.

Mechanical close PASS:10 canonical files equal final approved candidates and
receipts; exact raw hashes/canonical URLs, unique raw and canonical owners,
path-qualified raw links, approved concept snippets and reciprocal routes,
company/index uniqueness and counts all agree.81 sources=65 website+16 GitHub,
excluding changelogs.14 touched typed pages passed validate_wiki checks;
git diff --check passed. No code tests repeated for this documentation-only run.
Earlier pending aggregate notes reflect audit-time state; complete catalogs were
verified once at mechanical close. Generic disputes routes legitimately use the
root generic concept index; provider catalogs also list all promoted sources.


# Braintree C11 query audit — Group A (Search Fields / Search Results)

Scope: `search-fields-node` and `search-results-node`; exactly four fixed questions from `tracking/ingest/braintree/braintree-campaign-11/selection-review.md`. This is Group A of the single 20-question C11 audit.

Timing (UTC): actual_start `2026-09-21T12:10:31Z`; analysis_end `2026-09-21T12:10:58Z`; handoff `2026-09-21T12:11:04Z`.

## `search-fields-node`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-search-fields-node]]`) → `wiki/sources/braintree/source-braintree-search-fields-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/general/searching/search-fields/node-2026-09-16.md`.

1. **Navigation question — Where is Node search-field operators documented?**
   - **Object/action match:** Yes — the route reaches the Node Search Fields reference for operator selection, not object-specific customer/transaction/dispute search criteria or result consumption.
   - **Direct answer:** `[[source-braintree-search-fields-node]]` routes to the pinned reference. The raw organizes Node search operators under `Text fields`, `Multiple value fields`, and `Range fields`, with Node.js examples under each category.
   - **Exact raw locator:** `# Search Fields`, lines 14–23; `## Text fields`, lines 26–59; `## Multiple value fields`, lines 61–82; `## Range fields`, lines 84–123.
   - **Verdict:** **PASS**.

2. **Detail question — Where are supported field types, operators and important qualifications documented?**
   - **Object/action match:** Yes — the answer uses the generic Node search-field page and treats transaction snippets only as operator examples, not as an exhaustive object/field catalog.
   - **Direct answer:** The three field types are text, multiple-value, and range. Text supports `is`, `isNot`, `startsWith`, `endsWith`, and `contains`, with a 255-character limit per text search field. Multiple-value fields support `is` and `in`. Range fields support `is`, `between`, `max`, and `min`; non-time `between` is inclusive and `max`/`min` are respected as written. For time filters, the lower bound is inclusive, the upper bound is exclusive regardless of operator, and one minute is automatically added to the upper bound; the worked example includes through `17:00:59` and excludes `17:01:00`.
   - **Exact raw locator:** field types at lines 16–21; text operators/limit at line 28; multiple-value operators at line 63; range operators and non-time/time qualifications at lines 86–92; Node amount/created-at examples at lines 95–123.
   - **Verdict:** **PASS**.

## `search-results-node`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-search-results-node]]`) → `wiki/sources/braintree/source-braintree-search-results-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/general/searching/search-results/node-2026-09-16.md`.

3. **Navigation question — Where is Node search-result consumption documented?**
   - **Object/action match:** Yes — the route reaches the Node Search Results reference for consuming returned searches, not search-field operator selection or an object-specific search endpoint.
   - **Direct answer:** `[[source-braintree-search-results-node]]` routes to the pinned reference. The raw documents no-callback stream consumption under `Stream responses` and callback-provided iteration under `Iterable responses`.
   - **Exact raw locator:** `# Search Results`, line 14; `## Stream responses`, lines 16–43; `## Iterable responses`, lines 45–57.
   - **Verdict:** **PASS**.

4. **Detail question — What SDK-version, stream/callback and result-consumption qualifications are documented?**
   - **Object/action match:** Yes — every qualification belongs to the Node result-consumption page; it is not generalized to another SDK or turned into an exact final-count guarantee.
   - **Direct answer:** As of version 1.11.0, omitting the callback returns a Node object-mode stream; the examples pipe it to an object-mode writable or consume `data`/`end` before `resume()`. With a callback, the yielded response defines `each`. Searches first return matching IDs and fetch each record lazily during iteration: deleted records are skipped, and updated records are returned only if they still match, otherwise skipped. Therefore the exact count is unknown while iterating; after `ready`, `searchResponse.length()` gives the maximum number that will be supplied, not a guaranteed final count. Transaction searches cap at 50,000 results; all other searches cap at 10,000.
   - **Exact raw locator:** versioned no-callback stream and pipe example at lines 16–29; event/resume form at lines 31–43; callback `each` form at lines 45–57; lazy retrieval and delete/update races at lines 59–73; maximum-count meaning and `ready` example at lines 76–88; search-type caps at lines 90–93.
   - **Verdict:** **PASS**.

## Shared gap sweep and completeness check

- Both selected raws were read completely. Filename and exact-claim sweeps found the two generic searching references plus object-specific customer, transaction, subscription, dispute and credit-card-verification searches, Control Panel search, GraphQL search and a reporting guide. No extra raw was selected: the two generic references directly answer all four fixed questions, and object-specific criteria do not fill a gap or conflict. The Search Fields page's search-results link reaches the second selected raw, which was fully read for questions 3–4; no result-consumption fact was attributed back to the Search Fields source.
- Reciprocal routes: **PASS** — both root → Braintree index → `[[braintree-server-sdk]]` → source → exact raw routes resolve; the concept contains each audited source exactly once, and each source links back to the concept and its exact path-qualified raw. Aggregate direct provider-source catalog entries remain pending, but both required concept-led routes are live.
- Raw identity: **PASS 2/2** — source `canonical_url`, `raw_files`, Raw Sources link, raw Source URL, manifest identity and computed SHA-256 agree for Search Fields (`f43f5f38ea303b5b96505c50a8c5e44bbfd3bdba4eef29ba0cc576598f5499d2`) and Search Results (`f5285154662ac662b0b1c43d2920c60eff0cf587886fcf1bc03b90e99a9b6e71`).
- Completeness: **PASS** — 2 routes; exactly 4/4 predetermined questions; 4/4 object/action matches, direct answers, exact locators and PASS verdicts; no retrieval repair, extra full read, promotion recommendation, contradiction, or unresolved answer.

**Group verdict: PASS (4/4).**

# Braintree C11 query audit — Group B (Customer Search / Verification Search)

Scope: exactly the four fixed Group B questions from C11 selection review. Both selected raw pages were read completely; the bounded gap sweep did not expand the factual evidence set.

Timing (UTC): actual start `2026-09-21T12:18:47Z`; analysis end `2026-09-21T12:19:41Z`; corrected handoff `2026-09-21T12:23:08Z`.

## `customer-search-node`

Actual route: `wiki/index.md` (`[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-customer-search-node]]`) → `wiki/sources/braintree/source-braintree-customer-search-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/customer/search/node-2026-09-16.md`.

1. **Where is Node customer search documented?**
   - **Object/action match:** searches Braintree Vault customers with the Node gateway; it is not credit-card-verification or transaction search.
   - **Direct answer:** `source-braintree-customer-search-node.md` documents `gateway.customer.search()` and routes to the exact collected request reference. The opening callback example filters by customer ID and consumes Customer objects with `response.each()`.
   - **Exact locator:** selected raw `# Customer: Search`, lines 13–21 (Customer response collection and general routes); `> ### Node`, lines 23–34 (search call, ID filter, and callback iteration).
   - **Verdict:** PASS — the live provider-index → concept → source → raw route lands on the requested Node customer-search action.

2. **Where are filters and result-consumption examples, and what result-limitation notice is stated?**
   - **Object/action match:** customer-search criteria and consumption of returned customer objects, not a general operator inventory.
   - **Direct answer:** the opening example consumes results with callback `response.each()`. The raw groups filter examples under Customer fields, Address fields, Credit card fields, Credit card number, Expiration date, Created at, and Payment method token with duplicates. It states that results are limited according to the linked PayPal Data Protection Addendum; the collected page does not define a numeric limit there. Its separate All customers section warns that search results are currently capped and that the displayed all-customer call is not implemented in Node.
   - **Exact locator:** selected raw lines 18–21 (policy-based limitation and operator route); lines 23–34 (callback consumption); `## Examples`, lines 37–170 (filter-example sections and their qualifications); `### All customers`, lines 173–182 (cap warning and Node non-implementation).
   - **Verdict:** PASS — the requested examples and limitations are directly locatable without inflating the page into an exhaustive parameter catalog.

## `credit-card-verification-search-node`

Actual route: `wiki/index.md` (`[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-credit-card-verification-search-node]]`) → `wiki/sources/braintree/source-braintree-credit-card-verification-search-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/credit-card-verification/search/node-2026-09-16.md`.

3. **Where is Node credit-card verification search documented?**
   - **Object/action match:** searches credit-card-verification records with the Node verification gateway, distinct from customer or transaction search.
   - **Direct answer:** `source-braintree-credit-card-verification-search-node.md` documents `gateway.creditCardVerification.search()`. The opening example filters by verification ID, iterates verification objects with `response.each()`, and reads each verification's status.
   - **Exact locator:** selected raw `# Credit Card Verification: Search > ### Node`, lines 22–33; gateway call and ID filter at lines 25–26, verification iteration/status at lines 27–30.
   - **Verdict:** PASS — the live route and raw example match the requested verification-search object and action.

4. **Where are verification-specific search criteria and result limits, distinct from transactions or customers?**
   - **Object/action match:** criteria are applied through `gateway.creditCardVerification.search()` and return verification records; no transaction/customer-search behavior is imported.
   - **Direct answer:** the raw demonstrates verification-specific criteria grouped around customer details, credit-card details, associated payment-method token, billing-address postal code, and creation time. For created-at searches, an explicit timezone is respected; otherwise the gateway-account timezone is used, while returned time values are always UTC. The page states only that results are limited according to the linked PayPal Data Protection Addendum; it supplies no numeric limit or further policy interpretation.
   - **Exact locator:** selected raw lines 16–19 (policy-based limitation and operator route); `## Examples`, lines 38–118 (verification-specific criteria groups and created-at timezone qualification), especially lines 117–118 for timezone/default/UTC behavior.
   - **Verdict:** PASS — the evidence remains verification-specific and preserves the stated, non-numeric limitation boundary.

## Shared gap and completeness check

- Full selected evidence read: both raw pages were read from provenance header through their final See also entries. Raw identities match the promoted sources: Customer Search `2cf1e877e8dbdef107f13bed047d95fe54cca5fd56ee110fbc0dfce6b0c17264`; Verification Search `ca8a27537272aa529150dad905e4220171aba8e6bfb07a8d83f05edb3689f5df`.
- Bounded gap sweep: filename and distinctive-text searches surfaced the two selected raws plus adjacent general Search fields/Search results and Customer/Verification response references; broad distinctive-text matches in other request/response pages do not change these object-specific answers. Adjacent pages remain navigation-only and were not imported as factual evidence.
- Route integrity: `wiki/index.md` exposes `[[braintree-index]]`; the provider index exposes `[[braintree-server-sdk]]`; that concept lists each selected source once under `## Related`; each source reciprocally links the concept and its exact raw under `## Raw Sources`.
- Completeness: 4/4 fixed questions answered; each includes object/action match, direct answer, exact raw locator, and verdict. No route or evidence repair is required.

**Group verdict: PASS (4/4).**

# Braintree C11 query audit — Group C (Dispute Accept / Finalize)

Scope: exactly the four fixed Group C questions from C11 selection review. Selected evidence was read in full; the bounded gap sweep did not expand the factual evidence set.

Timing (UTC): actual start `2026-09-21T12:15:46Z`; analysis end `2026-09-21T12:17:00Z`; handoff `2026-09-21T12:17:15Z`.

## `dispute-accept-node`

Actual route: `wiki/index.md` (`## Concepts (generic)` → `[[disputes]]`) → `wiki/concepts/disputes.md` (`## Sources` → `[[source-braintree-dispute-accept-node]]`) → `wiki/sources/braintree/source-braintree-dispute-accept-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/dispute/accept/node-2026-09-16.md`.

1. **Where is Node dispute acceptance documented?**
   - **Object/action match:** one Braintree dispute accepted by ID with the Node gateway; this is not finalization or evidence upload.
   - **Direct answer:** `source-braintree-dispute-accept-node.md` documents the Promise call `gateway.dispute.accept("a_dispute_id")` and routes to the exact collected request reference.
   - **Exact locator:** selected raw `# Dispute: Accept > ### Promise`, lines 22–27; invocation at line 24 and success/validation-error behavior at lines 26–27.
   - **Verdict:** PASS — the live index → concept → source → raw route lands on the requested object and action.

2. **What access and refund warnings are stated, and which eligibility details are missing from the collected rendering?**
   - **Object/action match:** acceptance availability, eligibility caveat, and the already-refunded transaction branch.
   - **Direct answer:** API dispute management is available only to merchants who can access disputes in the Braintree Control Panel. The page says only disputes with a particular status may be accepted, but its collected sentence ends `status of.` and contains no eligibility value; this audit does not infer `Open` from the separate Finalize page. If the disputed transaction was already refunded, the page says **do not accept the dispute** and instead submit file or text evidence of the refund.
   - **Exact locator:** selected raw `# Dispute: Accept`, line 17 (access); lines 19–21 (missing status value and prior-refund warning/evidence alternatives).
   - **Verdict:** PASS — the direct answer preserves the rendering defect and the type-specific alternate-evidence warning without reconstructing unsupported eligibility.

## `dispute-finalize-node`

Actual route: `wiki/index.md` (`## Concepts (generic)` → `[[disputes]]`) → `wiki/concepts/disputes.md` (`## Sources` → `[[source-braintree-dispute-finalize-node]]`) → `wiki/sources/braintree/source-braintree-dispute-finalize-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/dispute/finalize/node-2026-09-16.md`.

3. **Where is Node dispute finalization documented?**
   - **Object/action match:** one Braintree dispute finalized by ID with the Node gateway; this is distinct from accepting a dispute or merely adding evidence.
   - **Direct answer:** `source-braintree-dispute-finalize-node.md` documents `gateway.dispute.finalize("a_dispute_id")` and routes to the exact collected request reference.
   - **Exact locator:** selected raw `# Dispute: Finalize > first ### Node`, lines 24–28; invocation at line 26 and success/validation-error behavior at line 28.
   - **Verdict:** PASS — the live route lands on the requested Node finalization action.

4. **What eligibility, evidence-submission requirement and status transition are stated?**
   - **Object/action match:** finalization eligibility and its effect on dispute evidence/status, with the same API-access boundary.
   - **Direct answer:** API management requires Control Panel dispute access. Only disputes in `Open` status can be finalized. Finalization submits the evidence to the banks and changes the status to `Disputed`; the page explicitly requires calling `finalize` for evidence to be submitted, so adding or preparing evidence alone is not established as submission.
   - **Exact locator:** selected raw `# Dispute: Finalize`, line 17 (access); line 19 (`Open`, submission to banks, and `Disputed` transition); `> IMPORTANT`, lines 20–21 (required finalize call).
   - **Verdict:** PASS — all requested qualifications are directly stated in the selected raw and remain scoped to finalization.

## Shared gap and completeness check

- Full selected evidence read: both raw pages were read from provenance header through the final code block. Raw identity matches the promoted source files: Accept `7e014b4ebf7c639b619b4015b2f66e2d3f51b76ed0453407767dcf3e0849ab69`; Finalize `649ec4f5a44e839f45a13090faf190763df165d58a25397af55f0ac598be31dc`.
- Bounded gap sweep: repository filename and distinctive-text searches surfaced the selected Accept/Finalize raws plus adjacent Dispute response, add-text-evidence, dispute-guide, and chargeback material. Those adjacent pages are not needed to answer the four fixed questions and were not imported as factual evidence. In particular, Finalize’s `Open` value cannot repair Accept’s damaged eligibility sentence.
- Route integrity: the root index exposes the generic `disputes` concept; that concept lists each selected source once; each source reciprocally links `[[disputes]]` and its exact raw under `## Raw Sources`.
- Completeness: 4/4 fixed questions answered; each has object/action match, direct answer, exact raw locator, and verdict. No route or evidence repair is required.

**Group verdict: PASS (4/4).**

# Braintree C11 query audit — Group D (Dispute Find / Search)

Scope: exactly the four fixed Group D questions from C11 selection review. Both selected raw pages were read completely; the bounded gap sweep did not expand the factual evidence set.

Timing (UTC): actual start `2026-09-21T12:21:32Z`; analysis end `2026-09-21T12:21:49Z`; handoff `2026-09-21T12:23:08Z`.

## `dispute-find-node`

Actual route: `wiki/index.md` (`## Concepts (generic)` → `[[disputes]]`) → `wiki/concepts/disputes.md` (`## Sources` → `[[source-braintree-dispute-find-node]]`) → `wiki/sources/braintree/source-braintree-dispute-find-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/dispute/find/node-2026-09-16.md`.

1. **Where is Node single-dispute lookup documented?**
   - **Object/action match:** looks up one dispute by ID with the Node gateway; this is not collection search.
   - **Direct answer:** `source-braintree-dispute-find-node.md` documents `gateway.dispute.find("a_dispute_id")` and routes to the exact collected request reference; the Promise resolves to a dispute value.
   - **Exact locator:** selected raw `# Dispute: Find`, line 23 (single-dispute ID instruction); `> ### Node`, lines 24–29 (find call and resolved dispute).
   - **Verdict:** PASS — the live index → concept → source → raw route lands on the requested single-dispute action.

2. **What identifier, access restriction and result-limitation guidance does the page provide?**
   - **Object/action match:** qualifications for the same single-dispute lookup.
   - **Direct answer:** pass the dispute ID to `gateway.dispute.find()`. API dispute management is available only to merchants who can access disputes in the Braintree Control Panel. Results are limited according to the linked PayPal Data Protection Addendum; the collected page supplies no numeric limit or further policy interpretation. The linked Dispute response page, not this lookup page, owns response-field details.
   - **Exact locator:** selected raw `# Dispute: Find > NOTE`, lines 16–17 (policy limitation); lines 19–21 (response route and access); lines 23–28 (ID lookup and resolved result).
   - **Verdict:** PASS — identifier, access, and limitation boundaries are directly stated without inventing a result schema.

## `dispute-search-node`

Actual route: `wiki/index.md` (`## Concepts (generic)` → `[[disputes]]`) → `wiki/concepts/disputes.md` (`## Sources` → `[[source-braintree-dispute-search-node]]`) → `wiki/sources/braintree/source-braintree-dispute-search-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/dispute/search/node-2026-09-16.md`.

3. **Where is Node dispute search documented?**
   - **Object/action match:** searches for a collection of disputes with the Node gateway; it is distinct from single-ID find.
   - **Direct answer:** `source-braintree-dispute-search-node.md` documents `gateway.dispute.search()`. The opening example filters by dispute ID and iterates returned dispute objects with callback `response.forEach()`.
   - **Exact locator:** selected raw `# Dispute: Search`, lines 19–23 (Dispute collection and operator route); `> ### Node`, lines 24–33 (gateway search, ID criterion, and result iteration).
   - **Verdict:** PASS — the live route lands on the requested dispute-collection search action.

4. **Where are search criteria and result access documented, and what availability or result limits apply?**
   - **Object/action match:** dispute-search criteria and returned dispute access, not a general operator inventory.
   - **Direct answer:** the opening example uses an ID criterion and accesses results through `response.forEach()`. Additional examples show multiple dispute kinds and a disputed-amount range. Operator definitions are delegated to the Search fields page. API dispute management requires Control Panel dispute access, and results are limited according to the linked PayPal Data Protection Addendum; this raw supplies no numeric limit or further policy interpretation.
   - **Exact locator:** selected raw lines 16–17 (policy limitation); lines 19–23 (collection, access, and operator route); lines 24–33 (ID and result access); `## Examples > ### Multiple kinds`, lines 38–50; `### Amount disputed range`, lines 52–61.
   - **Verdict:** PASS — criteria, result access, availability, and the non-numeric limitation are all directly locatable without expanding optional fields.

## Shared gap and completeness check

- Full selected evidence read: both raw pages were read from provenance header through their final example. Raw identities match the promoted sources: Find `0a1bc52997c06495eb47cff7649eeea0cfce349f824576f874d80c862de55044`; Search `c988130c669cd0cf12cfc1a198e2e55291c74244228aef55bb15113837736ee0`.
- Bounded gap sweep: filename and distinctive-text searches surfaced the selected raws plus adjacent Search fields, Dispute response, and dispute-guide material; broad policy/access text also occurs in other request pages. Those pages do not change these action-specific answers and remain navigation-only rather than imported factual evidence.
- Route integrity: the root index exposes `[[disputes]]`; that concept lists each selected source once under `## Sources`; each source reciprocally links the concept and its exact raw under `## Raw Sources`.
- Completeness: 4/4 fixed questions answered; each includes object/action match, direct answer, exact raw locator, and verdict. No route or evidence repair is required.

**Group verdict: PASS (4/4).**

# Braintree C11 query audit — Group E

- Scope: four of 20 fixed questions; Document Upload Create + Dispute Remove Evidence.
- `start_utc`: `2026-09-21T12:23:21Z`
- `analysis_end_utc`: `2026-09-21T12:24:16Z`
- `handoff_utc`: `2026-09-21T12:24:55Z`
- Aggregate company/provider-index/log/count work is outside this audit.

## Document Upload Create (Node.js)

Route: [[index]] → [[braintree-index]] → [[braintree-server-sdk]] → [[source-braintree-document-upload-create-node]] → [[raw/braintree/docs/reference/request/document-upload/create/node-2026-09-16]].

1. **Navigation question — Where is Node document upload creation documented?**
   - Object/action match: Node.js creation of a document upload, not adding evidence to a dispute, submitting evidence, removing evidence, or finalizing a dispute.
   - Direct answer: `[[source-braintree-document-upload-create-node]]`, backed by `[[raw/braintree/docs/reference/request/document-upload/create/node-2026-09-16]]`, documents `gateway.documentUpload.create()`.
   - Exact locator: raw `# Document Upload: Create`, line 13; `## Examples > ### Node`, lines 16–33.
   - Verdict: **PASS**.

2. **Detail question — What file input, purpose and result guidance is actually shown, without inferring dispute submission?**
   - Object/action match: only the displayed document-upload creation example and its result branch; no dispute submission or lifecycle effect is imported.
   - Direct answer: the example passes `fs.createReadStream('local_file.pdf')` as `file` with `kind: DocumentUpload.Kind.EvidenceDocument` to `gateway.documentUpload.create()`. Those are example inputs, not an exhaustive request schema, supported-file policy, or proof that the upload is attached to a dispute. The Promise callback binds its parameter as `result` but then reads `response.success`, `response.documentUpload`, and `response.errors`; this mismatch must remain visible, so the page supports only the intended success/document-result versus error branches and not a claim that the snippet runs verbatim. It provides no dispute ID and does not state that upload creation attaches or submits evidence, removes evidence, finalizes a dispute, or changes dispute status.
   - Exact locator: file stream, `EvidenceDocument` kind, and create call at lines 19–26; `result`/`response` mismatch and intended result/error access at lines 26–33.
   - Verdict: **PASS**.

## Dispute Remove Evidence (Node.js)

Route: [[index]] → [[disputes]] → [[source-braintree-dispute-remove-evidence-node]] → [[raw/braintree/docs/reference/request/dispute/remove-evidence/node-2026-09-16]]. The Braintree index also catalogs the source directly.

3. **Navigation question — Where is Node removal of dispute evidence documented?**
   - Object/action match: Node.js removal of one dispute evidence item, not document upload creation, evidence addition/submission, dispute acceptance, or finalization.
   - Direct answer: `[[source-braintree-dispute-remove-evidence-node]]`, backed by `[[raw/braintree/docs/reference/request/dispute/remove-evidence/node-2026-09-16]]`, documents `gateway.dispute.removeEvidence()`.
   - Exact locator: raw `# Dispute: Remove Evidence`, lines 13–19; first `### Node`, lines 20–27.
   - Verdict: **PASS**.

4. **Detail question — What dispute status, identifiers and removal/result behavior are established, distinct from finalization?**
   - Object/action match: eligibility, identifiers, and result handling for removal only; finalization and evidence submission remain separate operations.
   - Direct answer: API dispute management is available only to merchants who can access disputes in the Braintree Control Panel. Evidence can be removed only while the dispute status is `Open`. The Node call passes a dispute ID and an evidence ID. If removal succeeds, the result is successful; otherwise the page directs the reader to validation errors, and its Promise example checks `response.success` and logs `response.errors`. The page does not state that removal submits remaining evidence, finalizes the dispute, or changes its status.
   - Exact locator: access restriction at lines 16–17; `Open` eligibility at line 19; dispute and evidence IDs at lines 20–25; success/validation-error guidance at line 27; Promise result/error branch at lines 28–37.
   - Verdict: **PASS**.

## Shared gap sweep and route check

- Both selected raws were read completely. The removal source's related Dispute response raw remains navigation-only because these questions do not require its status inventory or response schema; the upload source has no related-raw section.
- Filename and content sweeps found sibling add-text-evidence and finalize raws. No extra full read was selected: the dedicated upload raw completely exposes its input/result mismatch and absence of a dispute identifier, while the removal raw completely establishes its own eligibility, identifiers, and outcome and contains no submission, finalization, or status-transition claim. No historical copy or actual contradiction requiring adjacent evidence was found; no sibling detail is used as factual evidence here.
- Reciprocal routes are live: `[[braintree-index]]` routes to `[[braintree-server-sdk]]`, which contains the document-upload source exactly once; root `[[index]]` routes to `[[disputes]]`, which contains the removal source exactly once. Each source links back to its concept and to its exact path-qualified raw. `[[braintree-index]]` also directly catalogs both promoted sources.

## One shared completeness check

All four fixed questions include object/action match, direct answer, exact raw locator, and verdict. Each page has one actual concept-led route. Full selected-evidence reads, one group gap sweep, reciprocal-link checks, the upload example mismatch, and the upload/removal/submission/finalization boundaries are present. Result: **4/4 PASS; no retrieval repair, extra full read, promotion recommendation, contradiction, or unresolved answer.**
