# Braintree Campaign 40 Fixed Query Audit — Group L (45–48)

Audit time: 2026-10-05T01:44:14Z

Scope: exactly four Campaign 40 manifest jobs, with two fixed questions per source page. Catalog changes remain coordinator-owned; this audit makes no repository edits. Answers are bounded to the 2026-09-16 captures, and linked pages or downloads are not behavioral evidence unless identified below as fully read supporting authority.

## Result

**8/8 PASS.** All eight fixed queries are answerable from the promoted source summaries with exact pinned-raw routes. The answers preserve object/action scope, prerequisites, material conflicts and warnings, and the required non-inference boundaries.

## Shared evidence and routing checks

- **Manifest/object integrity — PASS:** `manifest.json:413-445` identifies these as positions 45–48 with the expected Braintree job IDs, canonical URLs, source targets and pinned raw paths. All four attempt-1 independent reviews are approved.
- **Pinned hashes and reverse hashes — PASS:** recomputed SHA-256 values match the manifest, and each digest occurs on exactly one Markdown file under `raw/braintree/`:
  - Local Payment Contexts: `6553294c354841946601012e93a6841e74307151e514935d77a5421a5b78f354`
  - SPF Records: `cbf3e7820c7237a36e1c5a90619959eeb5b01d675bdaf98754a41d32b4e8add8`
  - Application Uploader Sample File: `62ab4e6f789a7d7436ed60c3fa947ac14dbea73a47f5ce5f0a9b7406d4d40095`
  - Prohibited Transactions: `efad6964618b4f46505e4f9f955a4c70466ec52cce723d2c0e8a045ee97f49a5`
- **Full reads — PASS:** all four promoted sources and all four manifest-pinned raws were read completely. The Non-Instant Local Payments raw, Application Uploader overview raw, PayPal Intake Data Dictionary raw, compliance overview raw, email-receipts raw and recurring-billing email-notifications raw were also read completely where needed to bound lifecycle, CSV-authority, compliance and SPF-feature questions.
- **Root/provider/concept/source/raw routes — PASS:** `wiki/index.md:5-11` routes to Braintree. The current provider index contains the four direct source rows at `wiki/braintree-index.md:381-384` and the three routed concepts at `:648-655`. Reciprocal concept routes are `braintree-payment-methods.md:23`, `braintree-control-panel.md:19`, and `braintree-payment-platform.md:27-28`; each source links back to Braintree and its main concept, and `wiki/companies/braintree.md:386-389` links to all four. Each source frontmatter and Raw Sources section resolves to its manifest raw, whose line 1 canonical URL matches. Any further catalog work is deferred to the coordinator.
- **Bounded gap sweep — PASS:** distinctive-term, path and canonical searches found no competing same-canonical factual raw or older capture. The separate non-instant guide confirms creation and outcome handling are distinct from context lookup; the uploader overview and dictionary identify submission/review and field-definition authorities while no linked CSV body is collected; the compliance overview routes government/sanctions responsibility without replacing the dedicated page; the two email-feature guides add Support/Control Panel activation steps but do not reconcile the SPF page's own requirement conflict. Discovery inventories and links remain navigation, not factual duplicates. No contradiction or missing authority changes an answer.

## 45. `graphql-integration-guides-local-payment-contexts`

### Q1. What object and actions does the page document, and what prerequisite and identifier inputs does it state?

**PASS.** It documents retrieval of an existing `LocalPaymentContext` through the root `node(id: $id)` query using a GraphQL global ID. If the caller instead has a legacy UUID, it documents conversion with `idFromLegacyId(legacyId: $legacyId, type: $type)` and `LegacyIdType = PAYMENT_CONTEXT`. The captured prerequisite is a PayPal account created and linked, with login credentials, to the Braintree Control Panel. The page does not establish that a particular merchant is linked, enabled or authorized, nor does it identify a client SDK, package/schema version or Sandbox-versus-Production environment.

Locators: source `:14,18-21,26-27,31-36`; raw `:20,25,28-54,116-145`.

### Q2. What may be learned from the displayed context and error examples, and why are they not payment-finality evidence?

**PASS.** The selection set exposes identity/type, amount/currency, approval URL, merchant account, timestamps, payment ID and order ID; the response happens to show a `MULTIBANCO` context for `1.00 EUR` with null transaction/approval/expiry timestamps, and the separate example shows `NOT_FOUND` with `node: null`. These are website examples, not an exhaustive schema, verified runtime result, universal nullability rule or lifecycle ordering. Retrieval and ID conversion do not create or approve a context, charge/authorize/capture funds, process a webhook, settle a transaction or prove funding. The fully read non-instant guide places creation and simulated payment/expiry outcomes in separate sections, reinforcing that a context lookup or selected status-like field is not itself finality.

Locators: source `:19-27,33-36,45-47`; raw `:28-114`; supporting raw `graphql/integration_guides/non_instant_local_payments-2026-09-16.md:26-50`.

## 46. `articles-guides-configuring-spf-records`

### Q3. What requirement conflict must an answer preserve, and which email features are actually in scope?

**PASS.** The same captured page says SPF configuration is no longer required “for integration,” yet says Braintree email receipts and recurring-billing notifications require the listed SPF steps before Braintree can enable them and that receipts/notifications cannot be sent until verification is complete. The source correctly preserves this as unresolved rather than broadening either statement into current account policy. The adjacent email-feature pages add authorized-signer Support activation and Control Panel configuration, but do not state that SPF is unnecessary and therefore do not resolve the conflict.

Locators: source `:14,21,23-24,28-32`; raw `:17-18,22,30-32`; supporting email-receipts raw `:24-28,38-50`; supporting recurring-notifications raw `:33-43`.

### Q4. What DNS and verification actions are stated, and what do the examples not guarantee?

**PASS.** The merchant or DNS administrator adds `include:spf.braintreegateway.com` to the domain's SPF TXT record, keeps multiple mechanisms on one space-separated SPF record line, then contacts Braintree for verification; host/registrar-specific troubleshooting routes to the domain provider. The displayed `v=spf1 ... -all` strings are examples, not universal DNS configurations. The page says SPF helps reduce spam-folder placement; it does not guarantee delivery, inbox placement, sender authenticity, anti-spoofing, fraud prevention, domain security, account enablement or successful email transmission.

Locators: source `:18-24,29-32`; raw `:20,25-32`.

## 47. `articles-guides-application-uploader-sample-file`

### Q5. What audience, purpose and sample families does this landing page identify?

**PASS.** It is a Braintree-hosted download landing page for preparing PayPal Intake application data. The Application Uploader is explicitly limited to select merchants. For uploader use, the example is a model application file whose test data can be erased to create a header template; the first row must contain headers. The page states two acceptable PayPal Intake input schemas and links separate full v1, full v2 and branded-solution sample CSVs, plus the PayPal Intake Data Dictionary route used by the Intake API or Application Uploader.

Locators: source `:14,18-20,25-29`; raw `:17-28,32-45`.

### Q6. Which constraints are actually evidenced, and what cannot be inferred from the unread CSV downloads or sample preparation?

**PASS.** This page establishes only the header-template use, first-row-header rule, v1/v2 schema labels and distinct branded-solution sample route. The linked CSV bodies were not collected, so the landing page cannot establish exact columns, field keys, values, formats, conditional requirements, schema differences or validation behavior. The separately read dictionary landing page says its downloadable dictionaries carry definitions, acceptable values and formatting, confirming that field detail belongs there rather than in link labels. Downloading or preparing a sample is not submitting an application and does not prove eligibility, acceptance, underwriting/Global Credit approval, biller configuration, payment/payout-method enablement or processing readiness; the fully read uploader overview treats submission and later review as separate steps.

Locators: source `:20-21,28-29,36-41`; raw `:27-40`; supporting dictionary raw `paypal-intake-data-dictionary-2026-09-16.md:22-48`; supporting uploader-overview raw `:32-38,41-98`.

## 48. `articles-risk-and-security-compliance-prohibited-transactions`

### Q7. What prohibition scope and applicability qualifications can the captured page support?

**PASS.** It attributes prohibitions to regulations and financial sanctions and names restricted or high-risk countries, individuals, corporate entities and organizations; restrictions may also apply to banks linked to prohibited sources or countries, and a BIN indicating a high-risk region or bank may lead to unsuccessful processing. The list is not exhaustive, and the BIN wording is not a universal decision rule. Applicability varies with the business's country of domicile and its counterparties, and restrictions can change with laws and political conditions. This is historical Braintree guidance, not current law, legal advice, merchant approval or a prohibited-party/country determination.

Locators: source `:14,18-19,21,23-24,28-31`; raw `:16-18,22`; supporting compliance-overview raw `:19-25`.

### Q8. What bank sequence does the page describe, and why must its outcomes remain modal rather than guaranteed?

**PASS.** The page says the processing bank declines prohibited transactions **in most cases**. In the **rare instance** it authorizes one, the funding bank will **typically** prevent settlement, and Braintree says it will notify the merchant. Those modal terms cannot be converted into guaranteed decline, settlement prevention or notification behavior, and authorization does not establish settlement or funding. The page directs merchants to applicable government sources, naming OFAC only as a US example; it does not prove any individual authorization, decline, settlement block, funding result or notification.

Locators: source `:14,19-24,29-31`; raw `:18,20-22`.

## Analysis end / handoff

Completed at 2026-10-05T01:44:14Z. Query content is ready for coordinator review: **8 PASS, 0 FAIL**. No correction or close blocker was found. Catalog ownership remains deferred to the coordinator, and this audit modified no repository file.
