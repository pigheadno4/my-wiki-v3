# Braintree C04 final retrieval audit

Result: 10/10 PASS, zero query repairs or extra full raw reads.
Two disjoint groups comprise the single planned ten-question audit. Group A
aggregation-pending note is historical; final catalogs were validated at close.

# Braintree C04 final query audit — group A

## Timing (UTC)

- Actual start: `2026-09-20T13:16:45Z`
- Analysis end: `2026-09-20T13:17:32Z`
- Handoff: `2026-09-20T13:18:15Z`

## tokenization-key-javascript-v3

**Actual route:** `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-web-sdk.md` → `wiki/sources/braintree/source-braintree-tokenization-key-javascript-v3.md` → `raw/braintree/docs/guides/authorization/tokenization-key/javascript/v3-2026-09-16.md`.

1. **Navigation — Where is JavaScript v3 SDK initialization with a tokenization key documented?**
   - **Object/action match:** JavaScript client-SDK initialization with a tokenization key — match; this is client authorization for tokenization, not transaction authorization or payment success.
   - **Direct answer:** Follow `[[braintree-web-sdk]]` to `[[source-braintree-tokenization-key-javascript-v3]]`. The exact raw's `## Initializing the SDK` section says to initialize before displaying payment UI, then shows both Drop-in and custom-client callback and Promise forms passing the tokenization key as `authorization`.
   - **Exact raw locator:** `raw/braintree/docs/guides/authorization/tokenization-key/javascript/v3-2026-09-16.md`, `## Initializing the SDK`, lines 78–115.
   - **Verdict:** **PASS**

2. **Detail — Where are reduced privileges, key lifecycle and setup qualifications documented?**
   - **Object/action match:** tokenization-key capability limits, reuse/revocation lifecycle, Control Panel acquisition, environment binding, and SDK-version qualification — match.
   - **Direct answer:** `### Static` says one key may be reused indefinitely across many client apps, multiple labeled active keys are allowed, and revocation deauthorizes clients using that key. `### Reduced privilege` limits clients to payment-information tokenization and states the customer/configuration, Vault, saved-method retrieval, and 3D Secure restrictions. `## Obtaining a tokenization key` gives the Control Panel steps and generation action; the opening qualification says Account Admin permission may be needed after an insufficient-privileges error. `## Adding a tokenization key to your app` says reduced-authority keys are publishable but bound to one environment, with production keys always reaching live regardless of environment variables or debug mode. `## Initializing the SDK` qualifies JavaScript support as v2.17 or higher.
   - **Exact raw locator:** same raw, opening lines 16–20; `### Static`, lines 23–29; `### Reduced privilege`, lines 32–41; `## Obtaining a tokenization key`, lines 44–54; `## Adding a tokenization key to your app`, lines 57–73; `## Initializing the SDK`, lines 78–82.
   - **Verdict:** **PASS**

## webhooks-testing-go-live-node

**Actual route:** `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-webhooks.md` → `wiki/sources/braintree/source-braintree-webhooks-testing-go-live-node.md` → `raw/braintree/docs/guides/webhooks/testing-go-live/node-2026-09-16.md`.

1. **Navigation — Where are Node webhook sample generation and test-notification routes documented?**
   - **Object/action match:** Node webhook testing through locally generated sample signature/payload data and the distinct Braintree-triggered destination test — match; this is not webhook creation, parsing-only documentation, or production delivery proof.
   - **Direct answer:** Follow `[[braintree-webhooks]]` to `[[source-braintree-webhooks-testing-go-live-node]]`. Under `## Sample payload and signature`, the exact raw shows callback and Promise calls to `gateway.webhookTesting.sampleNotification()` and parsing of the resulting signature/payload. Under `## Trigger a test notification from Braintree`, it gives the Control Panel path and **Check URL** action for firing a test to an existing webhook destination.
   - **Exact raw locator:** `raw/braintree/docs/guides/webhooks/testing-go-live/node-2026-09-16.md`, `## Sample payload and signature`, lines 17–50; `## Trigger a test notification from Braintree`, lines 56–71.
   - **Verdict:** **PASS**

2. **Detail — How do local sample payloads differ from Braintree-triggered tests, and what limitations are stated?**
   - **Object/action match:** comparison of the two testing routes and their page-stated payload/handler limitations — match.
   - **Direct answer:** `sampleNotification(kind, id)` locally generates a parsable signature and payload that the merchant POSTs to its own application; the result contains a dummy object of the requested type and may omit data expected from a production webhook. **Check URL** instead causes Braintree to send a test notification to the configured destination URL. In production, the handler must inspect notification kind: assuming another kind can raise an exception when code accesses an absent object. The collected page leaves the fired test's exact kind as an unresolved template expression, and neither route proves successful real-production-event delivery or a complete production payload.
   - **Exact raw locator:** same raw, sample purpose and calls lines 17–47; argument and incomplete-dummy warning lines 48–50; Braintree-triggered route and unresolved-kind text lines 56–58; **Check URL** steps lines 60–67; production handler-kind caution lines 69–71.
   - **Verdict:** **PASS**

## Shared checks

- **Gap sweep:** Filename and content sweeps covered authorization/tokenization-key siblings and overview material, webhook create/parse/overview/test references, and the Control Panel webhook page. Neither promoted source has `## Related raw API references`. The two exact, fully read selected raws directly answer all four fixed object/actions; no neighboring raw was needed as factual evidence, and the sweep exposed no relevant conflict. No historical equivalence was inferred.
- **Extra full reads:** None beyond the two assigned exact raws.
- **Reciprocal and retrieval routes:** **PASS** — root index routes to the Braintree index; the provider index routes to `braintree-web-sdk` and `braintree-webhooks`; each concept links to its promoted source; each source links back to its concept and to its exact path-qualified raw. The two source entries and company aggregate are still absent while campaign close aggregation is pending, but both concept-led routes are live, so this temporal state does not break either audited route.
- **Raw identity:** **PASS** — source `raw_files` and `## Raw Sources` resolve to the selected raw paths. Computed SHA-256 values match the C04 manifest: tokenization key `5b90f79342ef1592f47e7452c83b8b46dc3e1a74facfd62e6babec2086a9e246`; webhook testing `0d598c4655ef9602d4ea1044f35633c334e375350a98bdb8db64833dc8191e76`.
- **Coverage:** 2 pages, 4/4 predetermined questions, 4 PASS, 0 FAIL, 0 unresolved, no repair required.

# Braintree C04 final query audit — group B

Timing (UTC): actual_start `2026-09-20T13:21:25Z`; analysis_end `2026-09-20T13:23:42Z`; handoff `2026-09-20T13:23:48Z`.

## payment-method-nonce-find-node

Route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-server-sdk.md` → `wiki/sources/braintree/source-braintree-payment-method-nonce-find-node.md` → `raw/braintree/docs/reference/request/payment-method-nonce/find/node-2026-09-16.md`.

- Navigation question — object/action match: Node.js `gateway.paymentMethodNonce.find()` lookup — MATCH. Direct answer: the Node payment-method-nonce lookup is documented on the routed source page, with the method purpose and nonce-argument form under `# Payment Method Nonce: Find`. Exact raw locator: lines 13–19; invocation examples at `### Callback`, lines 20–33, and `### Promise`, lines 35–48. **PASS**.
- Detail question — object/action match: whether that lookup consumes the nonce and where its returned 3D Secure information is described — MATCH. Direct answer: no; the find call does not consume the nonce. It returns the nonce string with 3D Secure information for server-side risk checking before transaction creation; `threeDSecureInfo` and its absent-information branch are shown in both examples. Exact raw locator: `# Payment Method Nonce: Find`, line 19; `### Callback`, lines 20–32; `### Promise`, lines 35–47. **PASS**.

## payment-method-nonce-create-node

Route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-server-sdk.md` → `wiki/sources/braintree/source-braintree-payment-method-nonce-create-node.md` → `raw/braintree/docs/reference/request/payment-method-nonce/create/node-2026-09-16.md`.

- Navigation question — object/action match: Node.js server-side `gateway.paymentMethodNonce.create()` creation — MATCH. Direct answer: the Node server-side creation operation is documented on the routed source page under `# Payment Method Nonce: Create`, with callback and Promise invocations. Exact raw locator: heading at line 13; callback at lines 21–26; Promise at lines 28–33. **PASS**.
- Detail question — object/action match: permitted use cases and required input for that server-side creation operation — MATCH. Direct answer: Braintree says merchants **should only** create payment-method nonces server-side when using 3D Secure or Checkout with PayPal; this is guidance, not a claim that creation is universally required or available. The page requires only the payment-method token as input. Exact raw locator: `# Payment Method Nonce: Create`, warning at lines 17–18 and input statement at line 20. **PASS**.

## payment-method-delete-node

Route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-server-sdk.md` → `wiki/sources/braintree/source-braintree-payment-method-delete-node.md` → `raw/braintree/docs/reference/request/payment-method/delete/node-2026-09-16.md`.

- Navigation question — object/action match: Node.js `gateway.paymentMethod.delete()` deletion by payment-method token — MATCH. Direct answer: the routed source page documents payment-method deletion by token and the Node invocation. Exact raw locator: `# Payment Method: Delete`, lines 13–16; `### Node`, lines 17–20. **PASS**.
- Detail question — object/action match: consequences of that payment-method deletion for associated subscriptions and already-paid remaining days — MATCH. Direct answer: all subscriptions associated with the deleted payment method are canceled immediately, and the customer forfeits any remaining days already paid for. Exact raw locator: `# Payment Method: Delete`, lines 15–16. **PASS**.

## Shared checks

- Pinned identity/hash: all three canonical URLs occur uniquely in the raw capsule; SHA-256 values match the manifest: find `b94626a054da43209556c3b92a3c3d1cf87c1e373c5164c9fde7da7bb814246c`, create `600f6f22b1ab28fb134d79c38b835bb8d99f880a97588b4de8eb5f65334791c6`, delete `bd0221b398a20d04fd9e700aed2eece10e72650b454edd9dde0dd46127bd30e5`. Promoted source bytes equal the approved candidate for find attempt 1, create attempt 2, and delete attempt 1. **PASS**.
- Reciprocal/navigation links: root → Braintree index, Braintree index → `braintree-server-sdk`, concept → each source, each source → concept, and each source → its exact path-qualified raw file all resolve in the audited content; frontmatter canonical URLs and `raw_files` paths match the manifest. **PASS**.
- Gap sweep (recorded once): searched the Braintree raw capsule by exact canonical URL, operation/family filenames, and the material nonce/deletion phrases; none of the three source pages has a `## Related raw API references` section. No extra full raw read was required because each pinned operation page directly and completely answers its assigned questions. The sweep surfaced `raw/braintree/docs/guides/recurring-billing/manage/node-2026-09-16.md` as navigation-only corroboration of the deletion consequence; no answer relies on it, so it was not selected as factual evidence. No historical same-canonical snapshot was present. **PASS**.
- Completeness: 3 actual routes, 6/6 predetermined questions, 6/6 object/action matches, 6/6 direct answers, 6/6 exact locators, 6/6 verdicts. No repair required.
