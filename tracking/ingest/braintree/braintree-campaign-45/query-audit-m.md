# Braintree C45 fixed-query audit M — positions 49–50

- Scope: `braintree-campaign-45`, group M only; positions 49–50.
- UTC start: `2026-10-07T14:17:58Z`
- UTC analysis end: `2026-10-07T14:18:52Z`
- Result: **4/4 PASS**.

## Shared checks (once)

- Followed `wiki/index.md` → `wiki/braintree-index.md` → each page's main concept → exact source → complete pinned raw. The root routes to `[[braintree-index]]`; the provider index has direct rows for both sources and both main concepts. Deferred direct catalog rows are coordinator-close work and would not be content failures; none is missing here.
- Manifest pins match retained evidence: GraphQL raw SHA-256 `25c6c66f71cf877e33ad798b8609668c68031d5b8c34e32d4ef8602a142689b4`; sub-processors raw SHA-256 `aee0bad525fa3af71500ef6c4a8850bc423d4994943d8a1f7ce72d5d6f51c1e7`. Each source `canonical_url` matches its manifest URL and the raw line-1 Source URL.
- Single ownership holds: each exact canonical URL and each exact `raw_files` path occurs in only its intended source under `wiki/sources/`. Both raws are tracked and unmodified. Each source has matching frontmatter provenance plus a `## Raw Sources` link; each source links its main concept, and each main concept links back to the source.
- One bounded filename/topic gap sweep under `raw/braintree/` found only the two pinned pages plus `raw/braintree/in-person/guides/custom-prompts-2026-09-16.md`. The latter is not needed to answer either requested object/action: the sub-processor page itself establishes its Custom Prompts processing scope, and no Custom Prompts integration behavior is retained as evidence in that source. No supporting authority beyond the two complete primary raws was used. GraphQL schema, launch article, terminology, FAQ, and neighboring page links remain explicitly navigation-only.

## Position 49 — `in-person-reference-graphql-docs`

Route: `[[braintree-index]]` → `[[braintree-in-person]]` → `[[source-braintree-in-person-reference-graphql-docs]]` → `raw/braintree/in-person/reference/graphql-docs-2026-09-16.md`.

Requested object/action: the Braintree In-Person-hierarchy **GraphQL Docs landing page** and its action of routing an integrator to GraphQL resources/schema navigation—not the neighboring schema or an In-Person payment operation.

### Q1 — scope and non-inference: PASS

Provider/document/product/SDK/version/environment/account/object/action are all bounded correctly. This is a PayPal-hosted Braintree website reference landing document under the In-Person hierarchy, about the Braintree GraphQL API and navigation to its schema/launch resources. It names no SDK, package, SDK version, API version, Sandbox/Production environment, merchant/account type, credential, schema object, field, mutation, or runtime request. The source correctly prevents inference of exact deployed schema, In-Person operations, inputs, device support, authorization/errors/lifecycle, compatibility, availability, account eligibility, successful execution, or payment outcome.

Locators: source lines 14, 18–24; raw identity/purpose lines 14–16, schema-navigation lines 19–23, and positioning/navigation lines 26–30.

### Q2 — purpose, conditions/warnings, and detail retrieval: PASS

The retained answer stays on the same landing-page object: its purpose is to provide GraphQL integration resources; it says the linked schema defines supported API features and positions GraphQL as Braintree's next-generation integration path. The consequential warning is that these are navigation and positioning statements, not field-level schema, In-Person support, account/environment enablement, current-support, or execution proof. Precise page detail is retrievable at raw lines 14–16 (`# GraphQL Docs` purpose), 19–23 (`See what the API can do` and schema link), 26–30 (`Our next-generation API` and launch link), and 32 (neighbor navigation). The source does not substitute claims from the unread neighboring schema, article, terminology, or sub-processor page.

Locators: source lines 18–31 and 39–43; pinned raw lines 14–16, 19–23, 26–30, 32.

## Position 50 — `in-person-reference-paypal-braintree-sub-processors`

Route: `[[braintree-index]]` → `[[braintree-in-person-custom-prompts]]` → `[[source-braintree-in-person-reference-paypal-braintree-sub-processors]]` → `raw/braintree/in-person/reference/paypal-braintree-sub-processors-2026-09-16.md`.

Requested object/action: the **PayPal Braintree In-Person Custom Prompts sub-processor list** and the action of identifying the named processors, their described services, and labeled entity country—not general Braintree/PayPal vendor coverage or Custom Prompts integration behavior.

### Q1 — scope and non-inference: PASS

Provider/document/product/SDK/version/environment/account/object/action are all bounded correctly. This is an unversioned PayPal-hosted Braintree In-Person reference page whose object is the processors of personal data for In-Person Custom Prompts and whose action is disclosure/list lookup. It specifies no SDK, API/package version, Sandbox/Production environment, merchant account, credential, prompt operation, transaction object, or execution procedure. The source correctly blocks inference of current/comprehensive PayPal or Braintree vendor coverage, account-specific data flow, data storage/residency/transfer, legal or contractual role, compliance, service availability, Custom Prompts enablement/behavior, or payment outcome.

Locators: source lines 14, 18–20; raw title/scope lines 14–16 and table lines 18–20.

### Q2 — purpose, conditions/warnings, and detail retrieval: PASS

The retained answer matches the list object: the page states the processors act on behalf of PayPal Braintree's In-Person Custom Prompts features, then lists Amazon Web Services, Inc. for cloud hosting and Splunk for application logging/performance monitoring, with `Entity Country` shown as United States for both. The consequential boundary is that `Entity Country` is only the table's field label and must not be recast as storage, residency, transfer, or all-processing-location evidence; the snapshot also does not prove present completeness. Exact scope is at raw lines 14–16 and every table value is at raw lines 18–20. The adjacent GraphQL Docs and FAQ links at raw line 22 supply no evidence for this answer.

Locators: source lines 18–25; pinned raw lines 14–20 and navigation boundary line 22.

## Completeness pass

- Four predetermined questions answered exactly once: two per selected page.
- Each answer restates and preserves the requested object/action, covers all mandated scope dimensions, uses same-object primary evidence, gives exact raw locators, and has an explicit PASS/FAIL result.
- No repository file was edited; this report is the only output.

- UTC handoff: `2026-10-07T14:19:21Z`
