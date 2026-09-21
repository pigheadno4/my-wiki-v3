# Braintree C02 final retrieval audit

Result: 10/10 PASS; zero query repairs and zero additional raw reads.
Two disjoint groups comprise the single planned ten-question audit.
Group A catalog-pending observation is historical; final catalog aggregation
completed at 12:15:27Z and is covered by the closing mechanical check.

# Braintree C02 final query audit — group A

## Timing (UTC)

- Start observed: 2026-09-19T12:14:38Z
- Analysis end: 2026-09-19T12:15:38Z
- Handoff: 2026-09-19T12:16:19Z

Catalog status at audit time: `wiki/braintree-index.md` has not yet aggregated these two promoted website-source entries. This is a temporal campaign-close state, not a permanent retrieval failure: both concept routes and their reciprocal source links are live.

## hosted-fields-events-javascript-v3

Actual route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-web-sdk.md` → `wiki/sources/braintree/source-braintree-hosted-fields-events-javascript-v3.md` → `raw/braintree/docs/guides/hosted-fields/events/javascript/v3-2026-09-16.md`.

1. **Navigation question:** Where can I find JavaScript Hosted Fields events for updating my form UI?
   - **Object/action match:** JavaScript v3 Hosted Fields events used to update merchant-controlled form UI — match.
   - **Direct answer:** Follow the Braintree Web SDK concept's Related route to **Braintree Hosted Fields Events (JavaScript v3)**. The raw guide says event listeners expose field state so the merchant page can update its UI, and it shows listener registration with `HostedFields.on` in the create callback.
   - **Exact raw locator:** `raw/braintree/docs/guides/hosted-fields/events/javascript/v3-2026-09-16.md`, `# Events`, lines 14–30.
   - **Verdict:** PASS.

2. **Detail question:** Where are event meanings and field-state access documented, and which reference version do the links name?
   - **Object/action match:** Hosted Fields event meanings, on-demand field-state access, and linked API-reference version — match.
   - **Direct answer:** Event meanings are in the `# Events` table. On-demand form/field state is documented under `getState`, with callback and Promise examples inspecting each provided field's `isValid`. The Hosted Fields API links name `braintree-web` reference version **3.92.1**; this version applies to the linked references, not unspecified SDK versions.
   - **Exact raw locator:** same raw; event table lines 20–28; `getState` explanation and examples lines 86–130; versioned reference links lines 16–17, 30, 86, and 133.
   - **Verdict:** PASS.

## transaction-refund-node

Actual route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-server-sdk.md` → `wiki/sources/braintree/source-braintree-transaction-refund-node.md` → `raw/braintree/docs/reference/request/transaction/refund/node-2026-09-16.md`.

3. **Navigation question:** Where is the Node transaction-refund operation documented?
   - **Object/action match:** Node.js server SDK `gateway.transaction.refund()` operation — match; it is not the separate `transaction.credit()` operation.
   - **Direct answer:** Follow the Braintree Server SDK concept's Related route to **Braintree Transaction Refund (Node.js)**. The exact raw page is the Node Transaction: Refund reference and shows `gateway.transaction.refund(...)`.
   - **Exact raw locator:** `raw/braintree/docs/reference/request/transaction/refund/node-2026-09-16.md`, `# Transaction: Refund > Node`, lines 13–25.
   - **Verdict:** PASS.

4. **Detail question:** What eligibility and omitted-amount behavior are stated, and where are refund-decline and settlement-failure details located?
   - **Object/action match:** Eligibility and amount behavior for Node transaction refunds, plus distinct processor-decline and settlement-failure routes — match.
   - **Direct answer:** A transaction must be `settled` or `settling`; the refund cannot exceed the remaining non-refunded amount; a fully refunded transaction cannot be refunded again; and an escrow-held transaction can be refunded only in full. With no amount, the page says the entire transaction amount is refunded; after a prior partial refund, another refund with no balance specified refunds the remaining non-refunded amount. Refund processor-decline details are under `## Examples > Refund processor declines`: the most current SDK exposes `processor_response_code`, while an older SDK may instead return a validation error. Settlement-failure details are under `## Examples > Settlement failures`, where a processor-declined capture exposes `processor_settlement_response_code`. The malformed introduction says `useinstead` for a transaction not yet in settlement but names no alternative action; this audit does not reconstruct it.
   - **Exact raw locator:** same raw; omitted amount line 15 and line 75; `## Requirements` lines 31–37; `### Refund processor declines` lines 80–89; `### Settlement failures` lines 91–100.
   - **Verdict:** PASS.

## Shared checks

- **Gap sweep:** Filename and canonical-URL metadata found the exact JavaScript v3 events raw plus Android v5 and iOS v7 sibling event pages, and the exact Node refund raw plus separate Refunds/Voids/Credits and Refund Authorizations articles. The questions are language/operation-specific, the selected raws answer them directly, and neither promoted source declares a `Related raw API references` route. No extra raw was needed or fully read; sibling/article metadata was not used as factual evidence.
- **Reciprocal routes:** PASS. `braintree-web-sdk.md` links to the Hosted Fields events source, whose Related section links back to `braintree-web-sdk`; `braintree-server-sdk.md` links to the Node refund source, whose Related section links back to `braintree-server-sdk`.
- **Pinned hashes:** PASS. Hosted Fields raw SHA-256 is `8deddae2653e4fd16281a2ca12543e7b4348ed8f5769819c18550acfc6c07dd6`; Node refund raw SHA-256 is `ffc419baf8cc3a2eb0556da4358d03e5768aeb9470940d3d964df2b1a6ff3da0`. Both match `tracking/ingest/braintree/braintree-campaign-02/manifest.json`.

Group A result: **4/4 PASS; 0 retrieval misses; 0 extra full raw reads; no repairs required.**


# Braintree C02 final query audit — group B

Scope: `webhooks-parse-node`, `payment-method-nonces`, `webhooks-create-node` (six predetermined questions). Repository read-only; no source edits.

## Routes and questions

### webhooks-parse-node

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-webhooks]]` → `[[source-braintree-webhooks-parse-node]]` → `raw/braintree/docs/guides/webhooks/parse/node-2026-09-16.md`.

1. **Navigation — Where do I parse a Braintree webhook notification in Node?**
   - Object/action match: **Yes** — the route reaches the Node webhook parsing guide and its callback/Promise uses of `gateway.webhookNotification.parse()`, not webhook creation or an event-kind reference.
   - Direct answer: Use the Node parsing guide; pass `req.body.bt_signature` and `req.body.bt_payload` to `gateway.webhookNotification.parse()` in either the callback or Promise form.
   - Exact raw locator: `# Parse` → `### Callback`, lines 38–53; `### Promise`, lines 55–70.
   - Verdict: **PASS**

2. **Detail — What signed inputs and parsing exceptions are described, and where are retry conditions documented?**
   - Object/action match: **Yes** — the evidence is the Node parse page for webhook inputs, parse failure, and handler-response retries.
   - Direct answer: The form body contains `bt_signature` and `bt_payload`; the page describes the payload as signed. It describes one parsing exception: an invalid-signature exception when the notification has an invalid signature. `### Retries` states that a response taking longer than 30 seconds is a timeout; Braintree retries hourly for up to 3 hours in sandbox or 24 hours in production, stopping after a successful HTTPS `2xx` response within 30 seconds.
   - Exact raw locator: `# Parse`, lines 16–24; `### Exceptions`, lines 72–74; `### Retries`, lines 77–79.
   - Verdict: **PASS**

### payment-method-nonces

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-server-sdk]]` → `[[source-braintree-payment-method-nonces]]` → `raw/braintree/docs/guides/payment-method-nonces-2026-09-16.md`.

3. **Navigation — Where is the relationship between a payment-method nonce and a GraphQL single-use payment method explained?**
   - Object/action match: **Yes** — the route reaches the terminology/lifecycle guide, not a nonce-create or payment-method operation reference.
   - Direct answer: The payment-method nonces guide explains that an SDK payment-method nonce is a secure one-time-use reference; GraphQL calls the equivalent, same-functionality reference a single-use payment method. The page uses “single-use token” for both.
   - Exact raw locator: `# Payment Method Nonces and Single-Use Payment Methods`, lines 14–16.
   - Verdict: **PASS**

4. **Detail — What use and lifespan restrictions does this page state, and where are they documented?**
   - Object/action match: **Yes** — the reached guide directly owns the stated uses and token lifespan.
   - Direct answer: The two stated purposes are creating transactions through an SDK or GraphQL and creating or updating Vault payment methods for repeat use. A single-use token may be used only once; if unused, it expires three hours after creation. These are input/use statements, not guarantees that either downstream operation succeeds.
   - Exact raw locator: `## Functionality`, lines 29–35; `## Lifespan`, lines 38–40.
   - Verdict: **PASS**

### webhooks-create-node

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-webhooks]]` → `[[source-braintree-webhooks-create-node]]` → `raw/braintree/docs/guides/webhooks/create/node-2026-09-16.md`.

5. **Navigation — Where do I configure a Braintree webhook destination and notification selection?**
   - Object/action match: **Yes** — the route reaches Control Panel destination configuration, not Node handler implementation or notification parsing.
   - Direct answer: Configure it in the Control Panel under gear icon → **API** → **Webhooks** → **Create New Webhook**, then provide the destination URL and notification selections and create the webhook.
   - Exact raw locator: `# Create`, lines 17–29.
   - Verdict: **PASS**

6. **Detail — Which Control Panel permission and destination requirements are documented?**
   - Object/action match: **Yes** — the evidence directly describes the configuring user's permission and webhook destination requirements.
   - Direct answer: The user's role needs **Manage Webhooks**. The destination must be a valid HTTPS path and a publicly accessible URL on the merchant's site; it receives notifications as POST requests. Multiple destinations may route selected notifications to specific endpoints, and creating a webhook requires at least one notification kind.
   - Exact raw locator: `# Create` note, lines 17–18; `## Destination URL`, lines 32–36; `## Notification kinds`, lines 39–41.
   - Verdict: **PASS**

## Group checks

- Gap sweep: filename/topic sweep found neighboring webhook and payment-method/nonce raw pages, but the three routed exact raws fully answered the six assigned questions. No related-raw section was present on these source pages and no extra raw was needed or selected for a full read.
- Reciprocal routes: **PASS** — `braintree-webhooks` links both webhook sources and each links back to `braintree-webhooks`; `braintree-server-sdk` links the nonce source and that source links back to `braintree-server-sdk`.
- Raw ownership and links: **PASS** — each source's `raw_files` value resolves to its exact routed raw, and each `## Raw Sources` link is path-qualified to that same file.
- Pinned hashes: **PASS** — computed hashes equal `manifest.json`: parse `87ed66fd084f4e5bbe7fab87bb086eed17e024cb51141caaea6db8d6c35a865a`; nonces `bc9e8d94f366525a58037adf4ec4e73f438f42d9a3c71957dfc69c96d5cd3429`; create `1871c3f74351d2a3ccd7da289fe6706a2e203fc3f6726e967bc795074a0caffe`.
- Group result: **6/6 PASS; no retrieval miss, unresolved answer, or repair required.**

## Timing (UTC)

- Started: `2026-09-19T12:16:07Z`
- Analysis ended: `2026-09-19T12:17:50Z`
- Handoff: `2026-09-19T12:18:34Z`
