# Braintree C09 final query audit

Overall:10/10 PASS; no extra selected raw reads or post-audit repairs.
Mechanical close passed; Group A pending-catalog observation resolved.

# Braintree C09 Query Audit — Group A (Plan Update/Create)

Status: PASS — 4/4 fixed questions. This is Group A of the single ten-question C09 audit.

Timing (UTC): started_at `2026-09-20T15:21:18Z`; analysis_end `2026-09-20T15:22:36Z`; handoff_at `2026-09-20T15:23:18Z`.

## Plan Update (Node.js)

Route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-server-sdk.md` → `wiki/sources/braintree/source-braintree-plan-update-node.md` → `raw/braintree/docs/reference/request/plan/update/node-2026-09-16.md`.

1. **Navigation question — Where is Node plan updating by ID documented?** Object/action match: plan / update by ID / Node.js. Direct answer: `source-braintree-plan-update-node` routes to the Node reference for `gateway.plan.update("aPlanId", attributes, ...)` in callback and Promise forms. Exact raw locator: `# Plan: Update`, lines 13–42; callback invocation at lines 16–28 and Promise invocation at lines 30–41. **PASS**.

2. **Detail question — Where are add-on/discount changes, multiple updates, overrides and trial-period examples; what can this page establish about effects on existing subscriptions?** Object/action match: plan update / associated add-ons and discounts / multiple changes / override behavior / trial-period update / existing-subscription evidence boundary. Direct answer: the add-on/discount section documents modification tokens and displayed `addOns`/`discounts` add-update-remove structures. Material warning: when add-ons or discounts already belong to the plan, omitting modification tokens removes all modifications associated with that plan after the update. Separate sections show multiple changes, inherited details with a bounded override list, and callback/Promise trial-period examples; the page says passing `trial_period` removes the plan's billing day of month. The complete page makes no statement that plan changes propagate to existing subscriptions, so it cannot establish such an effect. Exact raw locators: two approaches and destructive omission warning at `### Add-ons and discounts`, lines 43–80; displayed add-update-remove examples at lines 82–146; multiple-update examples at `### Multiple updates`, lines 148–199; inheritance, override list and examples at `### Override details`, lines 201–288; trial-period effect and examples at the source's `### Update trail period`, lines 290–311. **PASS**.

## Plan Create (Node.js)

Route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-server-sdk.md` → `wiki/sources/braintree/source-braintree-plan-create-node.md` → `raw/braintree/docs/reference/request/plan/create/node-2026-09-16.md`.

3. **Navigation question — Where is Node plan creation documented?** Object/action match: plan / create / Node.js. Direct answer: `source-braintree-plan-create-node` routes to the Node reference for `gateway.plan.create(attributes, ...)` in callback and Promise forms. Exact raw locator: `# Plan: Create`, lines 13–40; callback invocation at lines 20–29 and Promise invocation at lines 31–40. **PASS**.

4. **Detail question — What merchant prerequisite is stated, and where are required-input and add-on/discount creation examples documented?** Object/action match: merchant prerequisite / Node plan creation inputs / plan-creation add-ons and discounts. Direct answer: before creating a plan, the page requires the merchant's recurring-billing feature to be enabled; it does not document how enablement is performed. Required-input prose and callback/Promise examples appear in the opening creation section. Add-ons and discounts can be included using modification tokens or the displayed `addOns`/`discounts` add-update-remove structures, followed by inheritance and bounded-override examples. This creation page does not establish that creating a plan creates a subscription or changes existing subscriptions. Exact raw locators: prerequisite at line 17; required-input prose and callback/Promise examples at lines 19–40; modification-token examples at `### Add add_ons/discounts when creating a plan`, lines 42–71; displayed add-update-remove structures at lines 72–177; inheritance, override list and expanded examples at lines 178–284. **PASS**.

## Shared completeness check

Both selected raws were read completely. Root-index → Braintree-index → server-SDK-concept routing and both reciprocal source links are live; aggregate source cataloging is pending but does not break these concept-led routes. The gap sweep searched Braintree raw filenames for plan create/update and recurring-billing plans, plus exact prerequisite, modification-token, billing-day and existing-subscription terms. It found the two selected operation raws and two recurring-billing guide raws (`raw/braintree/docs/guides/recurring-billing/plans/node-2026-09-16.md` and `raw/braintree/articles/guides/recurring-billing/plans-2026-09-16.md`). No extra raw was selected: the exact operation raws fully answer these four questions, the create source marks its Node guide as navigation-only, and the existing-subscription question expressly asks what the update page itself establishes. No repair, promotion recommendation, contradiction or unresolved answer was required. Shared completeness verdict: **PASS**.

# Braintree C09 Query Audit — Group B

## Timing

- `started_at`: `2026-09-20T15:22:59Z`
- `analysis_end_at`: `2026-09-20T15:23:45Z`
- `final_handoff_at`: `2026-09-20T15:24:47Z`

## Plan Find (Node.js)

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-server-sdk]]` → `[[source-braintree-plan-find-node]]` → `[[raw/braintree/docs/reference/request/plan/find/node-2026-09-16]]`.

1. **Where is single-plan lookup by ID documented?**
   - Object/action match: Plan / find one plan by ID, not list, create, or update plans.
   - Direct answer: Node single-plan lookup by ID is documented in `[[source-braintree-plan-find-node]]`, backed by the Plan Find raw page. The prose says to look up one plan by ID but renders only “use themethod”; the displayed code supplies `gateway.plan.find()`.
   - Exact raw locator: `# Plan: Find`, lines 15–16; callback invocation at lines 17–20; Promise invocation at lines 22–25.
   - Verdict: **PASS**.

2. **What invocation and callback/Promise result forms does the displayed code support despite the missing method name in prose?**
   - Object/action match: Plan / find one plan by ID / identify only the displayed Node invocation and result-variable forms.
   - Direct answer: callback form is `gateway.plan.find("aPlanId", (err, result) => { });`; Promise form is `gateway.plan.find("aPlanId").then(result => { });`. Both expose a `result` variable, but neither example shows fields within it.
   - Exact raw locator: malformed prose at lines 15–16; callback code at lines 17–20; Promise code at lines 22–25.
   - Verdict: **PASS**.

## Add-On All (Node.js)

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-server-sdk]]` → `[[source-braintree-add-on-all-node]]` → `[[raw/braintree/docs/reference/request/add-on/all/node-2026-09-16]]`.

3. **Where is Node retrieval of all add-ons documented?**
   - Object/action match: Add-On / retrieve the complete Add-On collection, not create or apply add-ons.
   - Direct answer: Node retrieval of all add-ons is documented in `[[source-braintree-add-on-all-node]]`, backed by the Add On: All raw page and its `gateway.addOn.all()` examples.
   - Exact raw locator: collection purpose at `# Add On: All`, line 16; callback example at lines 17–22; Promise example at lines 24–29.
   - Verdict: **PASS**.

4. **How do the examples access the returned collection, and does the linked response reference point to the same SDK language?**
   - Object/action match: Add-On / inspect collection access in the displayed Node callback and Promise examples / verify the response-link language.
   - Direct answer: both examples assign `result.addOns` to `addOns`; callback uses `gateway.addOn.all((err, result) => { ... })`, while Promise uses `gateway.addOn.all().then(result => { ... })`. The linked Add-On response path ends in `/ruby`, and the See Also recurring-billing path also targets `/ruby`; neither is Node response or behavior evidence without a separate full read.
   - Exact raw locator: Ruby response link at line 16; callback access at lines 17–22; Promise access at lines 24–29; Ruby See Also link at lines 31–34.
   - Verdict: **PASS**.

## Discount All (Node.js)

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-server-sdk]]` → `[[source-braintree-discount-all-node]]` → `[[raw/braintree/docs/reference/request/discount/all/node-2026-09-16]]`.

5. **Where is Node retrieval of all discounts documented?**
   - Object/action match: Discount / retrieve the Discount collection, not create or apply discounts.
   - Direct answer: Node retrieval of all discounts is documented in `[[source-braintree-discount-all-node]]`, backed by the Discount: All raw page and its `gateway.discount.all()` callback example.
   - Exact raw locator: collection purpose at `# Discount: All`, line 15; Node callback example at lines 18–23.
   - Verdict: **PASS**.

6. **How does the example access results, and does this page establish discount creation or application behavior?**
   - Object/action match: Discount / inspect the displayed listing result access / test whether the same page establishes creation or application.
   - Direct answer: the sole displayed form is callback-only: `gateway.discount.all((err, result) => { const discounts = result.discounts; });`, so the collection is accessed through `result.discounts`. No Promise form is shown. The completely read page establishes collection listing, its stated not-found route, and navigation links only; it does **not** establish discount creation or application to plans or subscriptions. Its recurring-billing See Also link targets Ruby documentation and is not Node evidence.
   - Exact raw locator: collection purpose at line 15; callback/result access at lines 18–23; not-found route at line 24; Ruby See Also route at lines 27–30; creation/application absence checked across the complete page, lines 1–31.
   - Verdict: **PASS**.

## Shared gap sweep and completeness

- Fully read selected evidence: Plan Find raw logical lines 1–26, Add-On All lines 1–35, and Discount All lines 1–31. No related raw page was used as factual evidence.
- Filename/topic sweep found only the three pinned Node raw pages for these exact operations. The three source pages contain no `## Related raw API references`; no extra full raw read was needed.
- Reciprocal-link check passed: each source is linked from `[[braintree-server-sdk]]`, each source links back to that concept and `[[braintree]]`, and each source routes to its exact path-qualified raw. The provider index also contains all three source entries.
- Identity check passed for all six questions; Plan Find remains single-plan lookup rather than listing, creation, or update.
- One shared completeness check: **PASS** — 3 routes, 6/6 questions, 6/6 object/action checks, 6/6 direct answers, 6/6 exact locators, 6/6 PASS verdicts; callback/Promise scope, `result.addOns` versus `result.discounts`, missing prose method, and Ruby-link boundaries are all preserved.
