# Braintree C08 final query audit

Overall:10/10 PASS; no extra selected raw reads or post-audit repairs.
Coordinator mechanical close passed; Group A pending-catalog observation resolved.

# Braintree C08 Query Audit — Group A (Update/Create)

Status: PASS — 4/4 fixed questions. This is Group A of the single ten-question C08 audit.

Timing (UTC): started_at `2026-09-20T15:03:29Z`; analysis_end `2026-09-20T15:04:31Z`; handoff_at `2026-09-20T15:04:35Z`.

## Credit Card Update (Node.js)

Route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-server-sdk.md` → `wiki/sources/braintree/source-braintree-credit-card-update-node.md` → `raw/braintree/docs/reference/request/credit-card/update/node-2026-09-16.md`.

1. **Navigation question — Where is updating a stored credit card using Node documented?** Object/action match: stored credit card / update / Node.js. Direct answer: `source-braintree-credit-card-update-node` routes to the Node reference for `gateway.creditCard.update(creditCardToken, attributes, callback)`. Exact raw locator: `# Credit Card: Update > ### Node`, lines 24–40 (invocation at lines 26–39). **PASS**.

2. **Detail question — Where are the example inputs and nonce-versus-raw-card guidance, and how is the PCI warning qualified?** Object/action match: update inputs / nonce versus raw card / update-page PCI advisory. Direct answer: the example identifies the stored card with `creditCardToken`, then shows `cardholderName`, card details, a billing-address region, and `options.verifyCard: true`, with `err`/`result` callback arguments; these are displayed example values, not an exhaustive or required-field schema. The page says direct use **typically requires** PCI SAQ D compliance and recommends `payment_method` functions to avoid PCI concerns from raw card data on the server; it does not make either statement a universal compliance rule or guarantee. It recommends passing only a payment-method nonce; if nonce and raw fields are both supplied, individually supplied fields take precedence and remaining attributes come from the nonce. Exact raw locators: PCI advisory at lines 16–17; example inputs/callback at lines 24–40; nonce/raw-card guidance at lines 42–49. **PASS**.

## Credit Card Create (Node.js)

Route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-server-sdk.md` → `wiki/sources/braintree/source-braintree-credit-card-create-node.md` → `raw/braintree/docs/reference/request/credit-card/create/node-2026-09-16.md`.

3. **Navigation question — Where is Node credit-card creation documented?** Object/action match: credit card / create / Node.js. Direct answer: `source-braintree-credit-card-create-node` routes to the Node reference for `gateway.creditCard.create(creditCardParams, callback)`. Exact raw locator: `# Credit Card: Create > ### Node`, lines 20–31 (invocation at lines 29–30). **PASS**.

4. **Detail question — What does the page say about using payment-method functions and nonces versus raw card data?** Object/action match: create-page payment-method recommendation / nonce versus raw card. Direct answer: the page says direct credit-card creation **typically requires** PCI SAQ D compliance and recommends `payment_method` functions to avoid PCI concerns from raw card data being present on the server; this is qualified provider guidance, not a compliance guarantee or a claim that every credit-card-method use requires SAQ D. It recommends supplying only a payment-method nonce. If both a nonce and raw card data are supplied, individually supplied fields take precedence and remaining attributes come from the nonce. Exact raw locators: qualified advisory and recommendation at lines 16–17; nonce/raw-card guidance and precedence at lines 33–40. **PASS**.

## Shared completeness check

Both selected raws were read completely. Root-index → Braintree-index → server-SDK-concept routing and both reciprocal source links are live; aggregate source cataloging is still pending but does not break these concept-led routes. The gap sweep searched Braintree raw filenames and exact `gateway.creditCard.update`, `gateway.creditCard.create`, and `Payment method nonces vs. raw card data` text. The two selected credit-card raws are the exact operation evidence. The create source's payment-method guide is explicitly navigation-only; neighboring payment-method create/update references were not selected because these four questions are answered completely by the exact credit-card pages. No extra raw read, repair, promotion recommendation, contradiction, or unresolved answer was required.

# Braintree C08 Query Audit - Group B

## Timing

- Start: `2026-09-20T15:05:41Z`
- Analysis end: `2026-09-20T15:06:22Z`
- Handoff: `2026-09-20T15:07:06Z`

## Actual routes

- Expiring Between: `[[index]]` -> `[[braintree-index]]` -> `[[braintree-server-sdk]]` -> `[[source-braintree-credit-card-expiring-between-node]]` -> `[[raw/braintree/docs/reference/request/credit-card/expiring-between/node-2026-09-16]]`
- Find: `[[index]]` -> `[[braintree-index]]` -> `[[braintree-server-sdk]]` -> `[[source-braintree-credit-card-find-node]]` -> `[[raw/braintree/docs/reference/request/credit-card/find/node-2026-09-16]]`
- Delete: `[[index]]` -> `[[braintree-index]]` -> `[[braintree-server-sdk]]` -> `[[source-braintree-credit-card-delete-node]]` -> `[[raw/braintree/docs/reference/request/credit-card/delete/node-2026-09-16]]`

## Six fixed questions

### 1. Where is finding cards expiring between dates documented?

- Object/action match: PASS - the route terminates at the Node.js credit-card `expiringBetween` reference, not a general search, lookup, or expiration-policy page.
- Direct answer: It is documented in `[[source-braintree-credit-card-expiring-between-node]]`, backed by the pinned Node raw at `raw/braintree/docs/reference/request/credit-card/expiring-between/node-2026-09-16.md`. The operation shown is `gateway.creditCard.expiringBetween(before, after)`.
- Exact raw locator: source URL and page identity at lines 1 and 13-16; Node callback invocation at lines 17-22.
- Verdict: PASS.

### 2. How do the shown callback and stream examples supply dates and consume results; does this page specify boundary inclusivity?

- Object/action match: PASS - the answer concerns the two examples for the Node.js credit-card date-range operation.
- Direct answer: Both examples create `before = new Date('2018-01-01')` and `after = new Date('2018-12-31')`. The callback form passes both values to `gateway.creditCard.expiringBetween(before, after, (err, expiredCards) => {})`; it names `expiredCards` but its body does not consume the collection. The stream section creates an object-mode `writableStream` and defines `_write`, but calls `expiringBetween(before, after)` without assigning or piping its return and attaches a `data` listener to the differently spelled `writeableStream`. The collected stream sample is therefore incomplete/broken and must not be presented as executable result-consumption guidance. The page does not specify whether either date is inclusive, nor does it specify timezone interpretation.
- Exact raw locator: callback dates and callback argument at lines 19-22; stream writable setup at lines 27-32; stream dates, unassigned call, and misspelled listener at lines 34-38; only the unqualified phrase `between the specified dates` at lines 15-16.
- Verdict: PASS - evidence limitations are preserved.

### 3. Where is Node stored-credit-card lookup documented?

- Object/action match: PASS - the route terminates at the Node.js credit-card `find` operation, not creation, update, deletion, authorization, or a generic payment-method lookup.
- Direct answer: It is documented in `[[source-braintree-credit-card-find-node]]`, backed by `raw/braintree/docs/reference/request/credit-card/find/node-2026-09-16.md`. The page shows `gateway.creditCard.find(creditCardToken, ...)`.
- Exact raw locator: source URL and page identity at lines 1 and 13; Node lookup at lines 20-23.
- Verdict: PASS.

### 4. What identifier and result form are shown, and what warning or recommended alternative accompanies the operation?

- Object/action match: PASS - the identifier, callback, and advisory all belong to the Node.js credit-card `find` page.
- Direct answer: The example uses the variable `creditCardToken` and a callback with `(err, creditCard)`; it shows no result fields, result consumption, or success condition. The page says the operation **typically requires** PCI SAQ D compliance and recommends using `payment_method` functions to avoid PCI concerns from raw credit-card data being present on the merchant server. This is the page's qualified collected advisory and recommendation, not a claim that every lookup requires SAQ D, a compliance guarantee, or an independently current PCI assessment.
- Exact raw locator: qualified PCI statement and `payment_method` recommendation at lines 16-17; token and callback form at lines 20-23.
- Verdict: PASS.

### 5. Where is Node stored-credit-card deletion documented?

- Object/action match: PASS - the route terminates at the Node.js credit-card `delete` operation, not the separate payment-method deletion operation.
- Direct answer: It is documented in `[[source-braintree-credit-card-delete-node]]`, backed by `raw/braintree/docs/reference/request/credit-card/delete/node-2026-09-16.md`. The page shows `gateway.creditCard.delete(creditCardToken, ...)`.
- Exact raw locator: source URL and page identity at lines 1 and 13; Node deletion invocation at lines 20-22.
- Verdict: PASS.

### 6. What invocation/result form and qualified warning are shown; does this page itself state subscription-cancellation consequences?

- Object/action match: PASS - the answer is limited to the credit-card `delete` page and does not import the neighboring payment-method deletion operation.
- Direct answer: The displayed invocation is `gateway.creditCard.delete(creditCardToken, (err) => { });`; the callback has only `err`, with no returned result object, response fields, or documented success condition. The page says deletion **typically requires** PCI SAQ D compliance and recommends `payment_method` functions to avoid PCI concerns from raw credit-card data on the merchant server. The wording remains a qualified advisory and recommendation, not a universal SAQ D claim or compliance guarantee. This page does not state that deletion cancels subscriptions, forfeits paid service, removes billing relationships, or causes any other downstream association effect.
- Exact raw locator: qualified PCI statement and recommendation at lines 16-17; token-based invocation and error-only callback at lines 20-22. The complete raw ends at line 23 without a subscription-consequence statement.
- Verdict: PASS.

## Shared gap sweep and completeness check

- Fully read the three selected raws end to end. Their source frontmatter and path-qualified Raw Sources links match the terminal evidence files above.
- A filename and exact-operation sweep under `raw/braintree/` found only these three pinned Node raws for the three requested operations. The live source pages contain no `## Related raw API references`; no additional raw was selected or needed for these six questions.
- `[[braintree-server-sdk]]` contains distinct reciprocal links for Expiring Between, Find, and Delete, so all three actual routes resolve without conflating their actions.
- The Expiring Between route preserves the missing rendered object name, unconnected/misspelled stream sample, and unknown date-boundary/timezone semantics. The Find and Delete routes preserve `Typically requires` and recommendation scope. Delete does not import subscription consequences from payment-method deletion.
- Shared completeness verdict: PASS. Six of six fixed questions are directly answerable through the live routes with exact pinned evidence. Repairs: none. Extra full reads: none.
