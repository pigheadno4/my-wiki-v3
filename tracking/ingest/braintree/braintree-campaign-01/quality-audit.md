# Braintree C01 final query audit

Result: 10/10 PASS. Reports preserved below; group A catalog observations precede final aggregation.

# Braintree C01 final query audit — group A

## Timing (UTC)

- Start: 2026-09-19T10:27:00Z
- Analysis end: 2026-09-19T10:28:24Z
- Handoff: 2026-09-19T10:28:58Z

## transaction-sale-node

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-server-sdk]]` → `[[source-braintree-transaction-sale-node]]` → `[[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16]]`.

1. **Navigation — Where do I find the Node operation for creating a transaction?**
   - Object/action check: matches the Node.js Transaction: Sale operation for creating a transaction; it is not a response-object or settlement-only page.
   - Direct answer: follow the route above to the Braintree Transaction: Sale source and its pinned raw page; the Node operation is `gateway.transaction.sale()`.
   - Exact raw locator: `raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16.md`, `# Transaction: Sale`, lines 13–24.
   - Verdict: **PASS**

2. **Detail — What payment-source alternatives are documented, and how does the example request immediate submission for settlement?**
   - Object/action check: matches inputs to the Node transaction-creation request and the request option for immediate settlement submission.
   - Direct answer: the transaction takes an `amount` and either a `payment_method_nonce`, `payment_method_token`, or `customer_id`; `customer_id` uses the customer's default payment method. The Node example requests immediate submission with `options: { submitForSettlement: true }`.
   - Exact raw locator: `raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16.md`, introduction lines 17 and 21–30.
   - Verdict: **PASS**

## get-started

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-server-sdk]]` → `[[source-braintree-get-started]]` → `[[raw/braintree/docs/start/overview-2026-09-16|Braintree Get Started overview]]`.

1. **Navigation — Where can I find the initial Braintree integration flow and prerequisites?**
   - Object/action check: matches the Braintree Direct Get Started overview for an initial sandbox integration, including prerequisites and the integration flow; it is not the similarly named support-articles collection.
   - Direct answer: follow the route above to the Get Started source and pinned raw overview; prerequisites are under `What you will need`, and the integration flow is under `How it works`.
   - Exact raw locator: `raw/braintree/docs/start/overview-2026-09-16.md`, `# Overview` lines 24–40, `## What you will need` lines 55–82, and `## How it works` lines 85–110.
   - Verdict: **PASS**

2. **Detail — Where are client/server responsibilities and the checkout sequence documented, and what does each side do?**
   - Object/action check: matches the client/server SDK responsibility split and the checkout handoff sequence, not transaction settlement or fulfillment behavior.
   - Direct answer: `What you will need > Client and server SDKs` says the client SDK securely collects customer payment information and the server SDK acts on it. `How it works` documents the sequence: the front end requests a client token and initializes the client SDK; the server generates and returns the token with the server SDK; the customer submits payment information and the client SDK sends it to Braintree and receives a payment-method nonce; the front end sends the nonce to the merchant server; the server uses the server SDK to create a transaction.
   - Exact raw locator: `raw/braintree/docs/start/overview-2026-09-16.md`, `### Client and server SDKs` lines 65–75 and `## How it works` lines 85–110.
   - Verdict: **PASS**

## Shared checks

- Gap sweep: inspected related/unlinked metadata for Transaction Sale and Get Started, including the linked transaction response, transaction guide, client-token/authorization material, Drop-in tutorial, checkout UI, and adjacent support-article paths. No extra full evidence read was needed because the two pinned raw pages directly answer all assigned object/actions. The existing Drop-in lifecycle-date conflict remains source-qualified and does not affect these four questions.
- Extra full reads: none beyond the two assigned pinned raw files, both read completely.
- Reciprocal route check: **PASS** — root index → Braintree index → `braintree-server-sdk`; that concept links to both promoted sources; each source links back to `braintree-server-sdk` and to its exact raw. The two new source entries are temporarily absent from the Braintree index's `## Sources` list while catalog aggregation is pending; this is not a permanent retrieval failure because both live concept routes resolve.
- Raw identity: both complete-read file SHA-256 values match the approved manifest (`e8b790af…e5988` and `2d1f7b0…b7b4`).
- Coverage: 2 pages, 4/4 predetermined questions, 4 PASS, 0 FAIL, 0 unresolved.

# Braintree C01 final query audit — group B

- Scope: `webhooks-overview`, `control-panel-overview`, `credit-cards-client-javascript-v3` only
- Started (UTC): `2026-09-19T10:30:27Z`
- Analysis ended (UTC): `2026-09-19T10:32:26Z`
- Handoff (UTC): `2026-09-19T10:33:02Z`
- Result: **PASS — 6/6 predetermined questions passed; no retrieval repair required.**

## webhooks-overview

Route: `wiki/index.md:11` → `wiki/braintree-index.md:58` → `wiki/concepts/braintree-webhooks.md:20` → `wiki/sources/braintree/source-braintree-webhooks-overview.md:40-42` → `raw/braintree/docs/guides/webhooks/overview-2026-09-16.md`.

- Navigation question — object/action match: **Braintree webhook-notification integration starting point**, matched by the webhooks concept/source and selected overview raw. Direct answer: start at `[[braintree-webhooks]]`, which routes to `[[source-braintree-webhooks-overview]]`; the raw overview describes notification purpose, HTTPS delivery, and the configuration sequence. Raw locator: `# Overview`, lines 14-42. **PASS**.
- Detail question — object/action match: **overview-level webhook user permissions and delivery volume**, not parsing/retry semantics. Direct answer: the user's Control Panel role must include webhook permission; after assignment the user can access the Webhooks tab and create a destination. Braintree says it strives to send notifications as quickly as events occur, but simultaneous subscription billing can cause a flood in a short period; the page gives no delivery-time guarantee. Raw locator: `## User permissions`, lines 45-57; `## Volume`, lines 60-62. **PASS**.

## control-panel-overview

Route: `wiki/index.md:11` → `wiki/braintree-index.md:59` → `wiki/concepts/braintree-control-panel.md:20` → `wiki/sources/braintree/source-braintree-control-panel-overview.md:34-36` → `raw/braintree/articles/control-panel/overview-2026-09-16.md`.

- Navigation question — object/action match: **role of the Braintree Control Panel**, matched by the Control Panel concept/source and selected overview raw. Direct answer: use `[[braintree-control-panel]]`, which routes to `[[source-braintree-control-panel-overview]]`; the Control Panel is the gateway administration UI, with specified setup and administration tasks that must be performed there. Raw locator: `# Overview`, lines 14-26. **PASS**.
- Detail question — object/action match: **Control Panel environment distinctions and Dashboard information**. Direct answer: Sandbox is the testing environment and Production is the live environment; their Control Panels are mutually exclusive, do not interact, and may use different credentials. Dashboard information is under `## Dashboard`: it shows sales/transaction volume, totals, averages, and links to statements and reports, but is not for reconciliation; Marketplace transactions are excluded from daily-sales graphs. Raw locator: `## Dashboard`, lines 29-37; `## Environments`, lines 40-48. **PASS**.

## credit-cards-client-javascript-v3

Route: `wiki/index.md:11` → `wiki/braintree-index.md:62` → `wiki/concepts/braintree-web-sdk.md:25-27` → `wiki/sources/braintree/source-braintree-credit-cards-client-javascript-v3.md:32-34` → `raw/braintree/docs/guides/credit-cards/client-side/javascript/v3-2026-09-16.md`.

- Navigation question — object/action match: **client-side credit-card guidance for JavaScript v3**, not native SDK or server processing guidance. Direct answer: use `[[braintree-web-sdk]]`, whose card/authentication section routes to `[[source-braintree-credit-cards-client-javascript-v3]]`, the JavaScript v3 standard client-side guide. Raw locator: `# Standard Client-Side Implementation`, lines 14-20. **PASS**.
- Detail question — object/action match: **JavaScript v3 Card Fields support and the page's directed alternative**. Direct answer: JavaScript v3 does **not** support Card Fields; the page directs JavaScript v3 developers to **Hosted Fields**. It separately says Card Fields are available for Android v5 and iOS v7 only; that is not JavaScript support. Raw locator: `# Standard Client-Side Implementation` → `IMPORTANT`, lines 17-20. **PASS**.

## Shared checks

- Reciprocal routes: **PASS**. The root index routes to the Braintree index; the Braintree index routes to each selected concept and source; each concept routes to its selected source; each selected source routes back to its concept; the Braintree company page also catalogs all three selected sources and concepts.
- `raw_files` / raw links / hashes: **PASS**. Each source has exactly the selected nested raw path in `raw_files`, and its `## Raw Sources` wikilink resolves to the same path after normalizing the omitted `.md` extension. All three raw files exist. SHA-256 values match the manifest: webhooks `222d304fa6eac14e1e694bc291bf697d6949d7e016a4ab63ab4c26be1a0b5d0e`; Control Panel `b26ec12da111dec5938485102438e09188d341a8d419099352b904ea2e8124d3`; JavaScript v3 cards `022edb93cce666fd9b5067342a13f10700af18d3f6fe4f24676bb5d4318b2fa4`.
- Gap sweep: matching related/unlinked raw filenames include webhook create/parse/test/reference pages, Control Panel reporting/task pages, and native Card Fields/Hosted Fields pages. The selected sources have no `## Related raw API references` section. None of those candidates was needed to answer these six overview/support-boundary questions because the selected fully read raws answer them directly; **extra full reads: none**.
- Repository changes: none; audit output only in `/tmp/bt01-audit-b.md`.
