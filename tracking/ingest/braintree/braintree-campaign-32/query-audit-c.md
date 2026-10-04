# C32 Query Audit C — 8/8 PASS

- Campaign: `braintree-campaign-32`
- Approved group: C
- Analysis end (UTC): 2026-10-04T03:15:08Z
- Scope: four approved pages, two fixed questions per page; read-only query audit

## `extend-oauth-client-side-ios-v7` — 2/2 PASS

**Q1 — Locate the exact Braintree Extend OAuth client-side Connect document for iOS v7 and its pinned raw.**

- **Direct answer:** `wiki/sources/braintree/source-braintree-extend-oauth-client-side-ios-v7.md`, titled **Braintree Extend OAuth Client-side Connect Flow for iOS v7**, owns the canonical `.../extend/oauth/client-side/ios/v7` page. Its sole factual raw is `raw/braintree/docs/guides/extend/oauth/client-side/ios/v7-2026-09-16.md`.
- **Actual route:** `[[index]]` → `[[braintree-index]]` → `[[braintree-auth]]` → `[[source-braintree-extend-oauth-client-side-ios-v7]]` → `[[raw/braintree/docs/guides/extend/oauth/client-side/ios/v7-2026-09-16]]`.
- **Exact locators:** root index line 11; Braintree index line 389; concept line 27; source frontmatter lines 2, 6–8 and Raw Sources lines 48–50; raw identity lines 1, 6–9 and iOS v7 route in the slug at line 7.
- **Verdict:** **PASS** — the exact platform/version source and pinned dated raw resolve through the current relevant concept.

**Q2 — State the iOS v7 client/server transition and its material availability and security qualifications.**

- **Direct answer:** The iOS app starts a merchant-consent flow from a **Connect with Braintree** button, presents a server-provided Connect URL in `SFSafariViewController`, and receives the post-consent return through a custom URL scheme only after the platform server creates the merchant access token. The page's purpose is this client-side handoff; it is not evidence that consent completed, a token is usable, or a payment was accepted. The snapshot labels OAuth closed beta in production and open beta in sandbox. It warns that custom schemes can be intercepted, so sensitive information must not be returned in the URL. Although the prose says the delegate ensures a trusted source, the sample only broadcasts the URL and returns `true`, with no visible validation of `url` or `sourceApplication`. The dated certificate notice names March 30, 2026 and iOS SDK 6.17.0+, but is not current support or eligibility proof.
- **Exact locators:** availability raw 17–18; certificate notice 21–22; responsibility sequence 25–32; server-supplied URL 62–72; server token creation/custom return 112–114; claimed trust check versus displayed handler 139–150; interception warning 153–156.
- **Verdict:** **PASS** — the answer preserves the actual client/server boundary, beta scope, custom-scheme risk, sample trust gap and dated lifecycle warning without inferring authorization or payment success.

## `extend-forward-api-configuration` — 2/2 PASS

**Q1 — Locate the exact unversioned Braintree Extend Forward API Configuration document and its pinned raw.**

- **Direct answer:** `wiki/sources/braintree/source-braintree-extend-forward-api-configuration.md`, titled **Braintree Extend Forward API Configuration**, owns the canonical `.../extend/forward-api/configuration` page. Its sole factual raw is `raw/braintree/docs/guides/extend/forward-api/configuration-2026-09-16.md`.
- **Actual route:** `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-platform]]` → `[[source-braintree-extend-forward-api-configuration]]` → `[[raw/braintree/docs/guides/extend/forward-api/configuration-2026-09-16]]`.
- **Exact locators:** root index line 11; Braintree index line 402; concept line 27; source frontmatter lines 2, 6–8 and Raw Sources lines 57–59; raw identity lines 1, 6–9.
- **Verdict:** **PASS** — the exact unversioned configuration source and dated raw resolve through the source's current main concept.

**Q2 — State what Forward API configuration controls and the sandbox-to-production transition, with security and authority qualifications.**

- **Direct answer:** The page establishes two JSON inputs: the incoming forward request identifies the merchant, outgoing payment-method nonce or token and destination URL; the config defines the outbound request's format, structure and transformations. Sandbox may carry an inline config, whereas production configs are reviewed and imported by Braintree and referenced by name. `debug_transformations: true` prevents the outgoing request and returns what would have been sent; the example response exposes a full test card number, so it is not safe payment-outcome evidence and may contain sensitive payment data. Production use remains eligibility-gated, and the page directs the reader to an Account Manager or Business Development. It does not establish present eligibility, config approval, destination authority, acceptance, authorization, capture, settlement or funding. The separate role authority and unresolved Account Admin tension are recorded once under Shared checks.
- **Exact locators:** production eligibility raw 16–17; two JSON sources 19–24; incoming request responsibility 26–30; config purpose and sandbox/production transition 33–35; illustrative credentials and transformation 36–70; named sandbox config 70–87; no-outgoing-request debug behavior and returned card data 90–126.
- **Verdict:** **PASS** — the answer preserves configuration responsibility, the sandbox/production transition, sensitive debug output and the eligibility/authority boundary without converting forwarding into payment execution.

## `extend-forward-api-braintree-api-forwarding` — 2/2 PASS

**Q1 — Locate the exact unversioned Braintree guide for forwarding alternate-Braintree-API payment tokens and its pinned raw.**

- **Direct answer:** `wiki/sources/braintree/source-braintree-extend-forward-api-braintree-api-forwarding.md`, titled **Braintree Extend Forwarding Braintree API Payment Tokens**, owns the canonical `.../extend/forward-api/braintree-api-forwarding` page. Its sole factual raw is `raw/braintree/docs/guides/extend/forward-api/braintree-api-forwarding-2026-09-16.md`.
- **Actual route:** `[[index]]` → `[[braintree-index]]` → `[[braintree-forward-api]]` → `[[source-braintree-extend-forward-api-braintree-api-forwarding]]` → `[[raw/braintree/docs/guides/extend/forward-api/braintree-api-forwarding-2026-09-16]]`.
- **Exact locators:** root index line 11; Braintree index line 387; concept line 21; source frontmatter lines 2, 6–8 and Raw Sources lines 46–48; raw identity lines 1, 6–9.
- **Verdict:** **PASS** — the exact named token-forwarding source and dated raw resolve through the Forward API concept.

**Q2 — State which request object is used for each alternate-Braintree-API token case and the material qualifications.**

- **Direct answer:** A token returned from the alternate Braintree API is supplied as `payment_method_nonce`; a stored payment-method token backed by a payment method in that API is supplied as `payment_method_token`. Both displayed requests are server-authenticated examples against Braintree's sandbox forwarding endpoint and an `httpbin.org` destination, with inline request-shaping configs. They establish input selection and request construction only. Production use is eligibility-gated; the page does not establish current enablement, required destination authority, a returned destination response, request acceptance, or any payment creation, authorization, capture, settlement, reconciliation or funding.
- **Exact locators:** eligibility raw 17–18; returned token/`payment_method_nonce` 20–45; backed stored token/`payment_method_token` 46–72; sandbox endpoint, Basic-auth keys, merchant ID, destination and transformation are inside the two displayed request blocks.
- **Verdict:** **PASS** — the two objects are distinguished exactly and the examples remain sandbox request-construction evidence, not destination or payment-outcome proof.

## `extend-forward-api-examples` — 2/2 PASS

**Q1 — Locate the exact unversioned Braintree Forward API Examples catalog and its pinned raw.**

- **Direct answer:** `wiki/sources/braintree/source-braintree-extend-forward-api-examples.md`, titled **Braintree Forward API Examples**, owns the canonical `.../extend/forward-api/examples` page. Its sole factual raw is `raw/braintree/docs/guides/extend/forward-api/examples-2026-09-16.md`.
- **Actual route:** `[[index]]` → `[[braintree-index]]` → `[[braintree-forward-api]]` → `[[source-braintree-extend-forward-api-examples]]` → `[[raw/braintree/docs/guides/extend/forward-api/examples-2026-09-16]]`.
- **Exact locators:** root index line 11; Braintree index line 387; concept lines 10, 16 and 25; source frontmatter lines 2, 6–8 and Raw Sources lines 49–51; raw identity lines 1, 6–9.
- **Verdict:** **PASS** — the exact named examples catalog and dated raw resolve through the Forward API concept.

**Q2 — State the catalog's actual purpose and its material security, availability and example-only qualifications.**

- **Direct answer:** The catalog demonstrates how Forward API functions and transformations construct outbound request values from Vault data and caller-supplied values: nested functions, Basic-auth header construction, hashing, overrides and pass-through, conditional transformations, XML paths/attributes, multiple payment methods, aliases and transformation-local `/var` bindings. It also documents the Vault/CVV boundary: Braintree does not store CVV for vaulted payment methods; when a destination requires CVV, the example combines a long-lived payment-method token with a separately collected CVV-only nonce and reads the suffixed CVV variable. Production use is eligibility-gated. Credentials placed in `sensitive_data` or `data`, sandbox calls, `httpbin.org`, debug results and named destination shapes are examples, not a complete secrets policy, destination authority, current destination compatibility, acceptance or payment execution evidence.
- **Exact locators:** eligibility raw 16–17; functions 38–85; Basic-auth construction and per-request variables 88–175; hash/template/override 183–247; override precedence 250–301; conditional transformations 304–343; XML examples 346–427; Vault/CVV prerequisite and suffixing 430–472; multiple methods/aliases 477–573; `/var` lifetime and non-emission 576–598.
- **Verdict:** **PASS** — the answer captures the catalog's construction purpose, CVV prerequisite and eligibility/security limits without treating sandbox examples as destination compatibility, authority, acceptance or settlement proof.

## Shared evidence, gap sweep and link checks

- **Primary integrity:** all four complete primary raws were read. Their SHA-256 values exactly match the C32 manifest: iOS `56c3e273…03568`; configuration `6cada0c9…94b6`; Braintree-token forwarding `333522e4…0b97`; examples `7879e083…7b2a`.
- **Forward/reverse routes:** every wikilink target in the four stated routes exists. Each source links back to its concept (the examples page does so in Overview), each concept links to the source, each source declares the pinned raw in both `raw_files` and Raw Sources, and each exact raw path is owned by exactly one source through `raw_files`. Raw reverse ownership is derived from source metadata; no raw edit is required.
- **Shared authority read:** fully read `source-braintree-control-panel-users-roles-role-permissions.md` and both of its factual raws. The role table says **Forward Payment Methods with the Forward API** is available to all sandbox merchants and approved production merchants and is not included in Account Admin (role-permissions raw line 66). The supporting managing-users raw calls Account Admin the maximum-permission role (line 41). This remains a documented scope tension; do not infer that Account Admin automatically grants Forward API access.
- **iOS related/conflict sweep:** fully read the same-date Braintree Auth iOS v7 source and raw. It is a separate canonical path with largely overlapping client code but different availability and server-transition wording: the Auth page says Braintree Auth is closed beta, while the Extend OAuth page says production closed beta and sandbox open beta. The current audited Extend source deliberately routes through `braintree-auth` and explicitly declines to infer Extend product ownership from the URL alone. No availability or credential claim was transferred between the two sources, and no automatic merge into `braintree-extend-oauth` was assumed.
- **Forward API gap sweep:** inspected filename/content matches and every Related raw API reference named by the four source pages. The Forward API overview, request/config/function/variable references, transformations, cryptography and general test-nonce pages remain navigation-only for these central-responsibility questions; none was needed to support an answer above. No unlinked raw supplied a contradictory payment, acceptance, settlement, eligibility or destination-authority claim.
- **Catalog timing:** company/source-catalog aggregation is outside this group's pass condition as instructed. The tested root → Braintree index → concept routes are live; coordinator close checks remain responsible for final exhaustive catalog aggregation.

**Final verdict: 8/8 PASS.**
