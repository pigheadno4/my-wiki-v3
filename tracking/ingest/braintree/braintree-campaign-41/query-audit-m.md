# Braintree C41 fixed-query audit M — positions 49–50

- Campaign: `braintree-campaign-41`
- Mode: read-only fixed-query audit
- Assigned jobs: positions 49–50
- Required questions: 4 total, exactly 2 per page
- Analysis end (UTC): `2026-10-06T15:39:14Z`
- Result: **4 PASS / 0 FAIL** for content answers and retrieval

## Shared checks and bounded gap sweep

- Read `CLAUDE.md`, `rules/query-and-synthesis.md`, and the C41 fixed-query policy in `tracking/ingest/braintree/braintree-campaign-41/selection-review.md` before auditing. Followed the root → provider index → main concept → source → pinned raw route, and fully read both promoted source pages and both pinned raws.
- Manifest job identity, raw path, source target, canonical URL, source `canonical_url` and `raw_files`, and raw `Source URL` metadata agree. Computed SHA-256 values match the manifest:

| Position | Job | Verified SHA-256 |
| ---: | --- | --- |
| 49 | `docs-guides-functions-accept-new-payment-method` | `5ac47cdaf14bf83f71bf3de875e56db6a3435ccca91489948cf52c855f03c23b` |
| 50 | `graphql-guides` | `4ee1a367857aeaa8183cd70b1e6f6d45656265876167e49e415035b524b9d918` |

- The bounded filename/related-route sweep found the separate Functions CLI, overview, advanced and other operation raws, plus separate GraphQL concept, API-call, pagination, testing and exact-SHA schema routes. The assigned pages already answer their page-scoped questions. No extra authority was needed or used as factual evidence; linked routes remain navigation until fully read.

## Position 49 — `docs-guides-functions-accept-new-payment-method`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md:706` → `wiki/concepts/braintree-payment-platform.md:28` → `wiki/sources/braintree/source-braintree-docs-guides-functions-accept-new-payment-method.md` → `raw/braintree/docs/guides/functions/accept-new-payment-method-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This is a 2026-09-16 capture of an unversioned Braintree **Functions documentation preview** for connecting a new payment-method service to Braintree transaction handling. It uses the `paymentMethod` template and an illustrative merchant-authored JavaScript authorization handler: initialize `MyNewPaymentMethod`; receive and parse transaction data; construct an external service request; map the service response into Braintree's response shape; locally test; configure authorization/capture/refund/void/vault triggers; deploy; then select the Function on a sale with `functionName`. The Node-style gateway and CLI examples pin no SDK, CLI, package, API or runtime version. Sandbox is the default deployment account/environment; production requires the prompt option or `btfns deploy --production`.

Do not infer current Functions availability or merchant/account eligibility from the preview/contact invitation; a complete third-party provider contract; package availability; secure production authentication, secret handling, validation, timeout/retry/idempotency or PCI design; successful testing/deployment; token creation or consumption; or a successful authorization, capture, refund, void, vault, settlement or funding outcome. The example `Authorized` mapping is authored sample code, not execution evidence.

Locators: source lines 12–21; raw preview/availability lines 14–18; template and generated operation files lines 21–29; authorization-handler scope lines 30–62; full illustrative handler lines 79–119; environment-qualified deployment lines 139–158; sale and subsequent-operation routing lines 159–193.

### Q2 — central purpose, conditions, warnings, and detail route — PASS

The page's central purpose is to demonstrate the end-to-end shape of a custom payment-method Function: implement the external authorization call and Braintree response mapping, test locally, supply the trigger map, deploy to the intended environment, and pass the deployed Function's name when creating a sale. Before deployment the page says local testing is important and the configuration file must be correct. `btfns generate-test-data` creates an example payload, not provider-realistic or successful-test proof. Deployment defaults to sandbox; production is explicit. Configured triggers are then invoked automatically, and later calls for that transaction route back to the Function without repeating `functionName`; extra data absent from the Transaction API may use Custom Fields.

The snippets are illustrative and require validation: the first incremental request fragment defines `httpOptions` but calls `fetch(..., options)` (raw lines 53–65), while the later complete example uses `httpOptions` (lines 97–105). Neither example supplies a real provider's full security/error contract. Exact commands, payload fields, example endpoint/mapping, YAML trigger keys, environment selector and transaction calls remain in the pinned raw.

Locators: source lines 18–30; raw initialization lines 21–29; request/mapping examples and mismatch lines 30–119; testing/mock-data conditions lines 121–138; configuration/deployment lines 139–158; `functionName`, automatic routing and Custom Fields lines 159–193.

## Position 50 — `graphql-guides`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md:706` → `wiki/concepts/braintree-payment-platform.md:30` → `wiki/sources/braintree/source-braintree-graphql-guides.md` → `raw/braintree/graphql/guides-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This is a 2026-09-16 capture of the unversioned Braintree **GraphQL Get Started landing/basic-orientation page**. It is documentation navigation plus generic GraphQL teaching material: routes for newcomers, API concepts, concrete API-call examples, the API Explorer and the separate GitHub schema repository; query-versus-mutation definitions; a `ping` example; arbitrary operation-name labels; schema/type and introspection orientation; and Braintree's stated Relay compatibility, primarily for lookup and search. It names no SDK, package/API version, environment, merchant account, credential, endpoint, payment object or payment operation.

Do not treat its teaching snippets or links as exact Braintree schema, SDK behavior, current deployment scope, account access, credentials, merchant eligibility, request execution or payment outcome evidence. The dated page's statement that the schema is always up to date does not establish the current schema or parity with a separately retained exact-SHA repository snapshot. Linked but unread guides are navigation, not transferred behavior.

Locators: source lines 12–22; raw landing purpose and intent routes lines 14–35; query/mutation and `ping` examples lines 38–76; schema/introspection scope lines 79–101; API Explorer line 104–106; Relay statement lines 109–111.

### Q2 — central purpose, conditions, warnings, and detail route — PASS

The page's central purpose is to orient a reader and send them to the appropriate Braintree GraphQL authority. A newcomer can read top-to-bottom or choose the named route; queries fetch data, mutations make changes, both may accept inputs, and an operation name is only a caller-chosen label. The page says the schema defines types, allowed queries/mutations, inputs, payloads and return shapes; introspection can inspect schema information; and the API Explorer can inspect the Braintree schema and try operations. Its Relay statement is expressly concentrated on object lookup and search, not a blanket guarantee for unlisted fields, pagination shapes, SDKs or deployments.

The pinned raw provides only the landing page's examples and route labels. Precise current schema details must be retrieved from an applicable current schema/API Explorer authority; commit-qualified implementation details belong to the separate `[[source-github-graphql-api]]` route. Concrete request procedures belong to `[[source-braintree-graphql-guides-making-api-calls]]`, and Relay pagination shapes to `[[source-braintree-graphql-guides-connections]]`; those routes were not needed as evidence for this landing-page audit.

Locators: source lines 18–31 and related-route lines 38–43; raw choice of paths lines 18–35; query/mutation and naming behavior lines 41–76; schema/introspection guidance lines 79–101; Explorer lines 104–106; Relay boundary lines 109–111.

## Deferred aggregate-edge check — separate from content verdicts

- No missing assigned-page aggregate edge was observed at handoff: both sources are present in the provider catalog (`wiki/braintree-index.md:69–70`), company catalog (`wiki/companies/braintree.md:68–69`), and reciprocal main-concept source list (`wiki/concepts/braintree-payment-platform.md:28,30`); the provider index links the main concept at line 706.
- Shared catalog/company/index/count closure remains coordinator-owned. This read-only audit made no repository changes, and this aggregate observation does not change the **4 PASS / 0 FAIL** content result.

## Handoff

- Corrections requested: none.
- Content blockers: none.
- Full extra-evidence reads: none required.
- Handoff UTC: `2026-10-06T15:39:58Z`
