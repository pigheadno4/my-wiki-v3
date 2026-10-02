# C26 fixed query audit — Group E

- Analysis end (UTC): `2026-10-02T11:13:01Z`
- Final handoff (UTC): `2026-10-02T11:14:02Z`
- Verdict: **PASS (4/4 questions; 2/2 manifest hashes)**

## sdk-deprecation-javascript-v3

- Route: `wiki/index.md:11` → `wiki/braintree-index.md:320` → `wiki/concepts/braintree-web-sdk.md:57` → `wiki/sources/braintree/source-braintree-client-sdk-deprecation-policy-javascript-v3.md` → `raw/braintree/docs/guides/client-sdk/deprecation-policy/javascript/v3-2026-09-16.md`. The source is also directly listed in `wiki/braintree-index.md:37`.
- Hash: `636fc4478fab8e74bd94268d398408f458cbb7ccfd8b76cd7201e3eff4696f9a` = C26 manifest — **PASS**.
- Q1 — “Where is the JavaScript v3 client-SDK deprecation policy?”
  - Object/action match: JavaScript v3 client-SDK deprecation policy / locate the policy — **MATCH**.
  - Direct answer: `https://developer.paypal.com/braintree/docs/guides/client-sdk/deprecation-policy/javascript/v3`; pinned raw path above.
  - Exact locator: raw lines 1, 6-9, 14 — **PASS**.
- Q2 — “Which lifecycle distinctions and consequences does this historical snapshot state?”
  - Object/action match: historical JavaScript client-SDK lifecycle and browser policy / distinguish states and consequences without inferring current support — **MATCH**.
  - Direct answer: the snapshot recommends regular integration updates and at least annual client-SDK updates; this is guidance, not a hard requirement. Breaking integration changes increase the major version, with browser/OS support and security changes named as examples. Exactly one **Active** major is current and fully supported and receives features; **Inactive** begins when a deprecation date is assigned and receives security updates only; **Deprecated** receives no updates, while processing is stated to remain supported for one year after the deprecation date and immediate upgrade is urged; **Unsupported** receives neither developer nor Braintree Support support, and processing may be suspended at any time. The README for each client SDK is the stated authority for major-version status and dates, and Braintree reserves exceptions. Historically, this snapshot says the active JavaScript major covered the current and previous major Chrome, Firefox, Safari and Edge versions plus IE11. That browser list and these categories do **not** establish current browser support, a current JavaScript-major status/date, or the status of any separately retained GitHub package version.
  - Exact locator: update recommendation lines 17-18; semantic-versioning and breaking-change scope lines 21-33; historical browser scope lines 36-48; lifecycle states and consequences lines 51-60; README authority and exceptions lines 62-66 — **PASS**.

## sdk-migration-javascript-v3

- Route: `wiki/index.md:11` → `wiki/braintree-index.md:320` → `wiki/concepts/braintree-web-sdk.md:79` → `wiki/sources/braintree/source-braintree-client-sdk-migration-javascript-v3.md` → `raw/braintree/docs/guides/client-sdk/migration/javascript/v3-2026-09-16.md`. The source is also directly listed in `wiki/braintree-index.md:36`.
- Hash: `ede8ae722164297994cf0c60a7e4abb6c419e3701e4e3cb7a0745ec12c123bce` = C26 manifest — **PASS**.
- Q3 — “Where is the JavaScript v3 client-SDK migration guide?”
  - Object/action match: JavaScript SDK v2-to-v3 migration guide / locate the guide — **MATCH**.
  - Direct answer: `https://developer.paypal.com/braintree/docs/guides/client-sdk/migration/javascript/v3`; pinned raw path above.
  - Exact locator: raw lines 1, 6-9, 14, 17 — **PASS**.
- Q4 — “Which central migration boundaries and consequential warnings does this snapshot state?”
  - Object/action match: historical JavaScript v2-to-v3 migration / state breaking integration boundaries and material warnings — **MATCH**.
  - Direct answer: v3 is a new major API and upgrading from v2.x requires integration-code changes; it moves toward a lower-level, modular model in which merchants select components rather than load the all-in-one v2 file. A custom UI first creates a gateway client with a tokenization key or client token, then instantiates components; multiple components may share one client. Hosted Fields keeps sensitive inputs in Braintree-hosted iframes but changes tokenization from an SDK-driven form-submit flow to an explicit merchant-timed `tokenize` call whose returned nonce must be sent to the server. Drop-in has its own major migration, moves from an iframe into a styleable page `div`, and remains a separate prebuilt-UI route. The PayPal section is explicitly scoped to v3.63.0+, and its callback sample contains malformed `fuAction` text, so it is not implementation-ready code; the multi-component Promise example also warns older browsers may need a Promise polyfill. Premium Fraud Management Tools derive environment and applicable Kount ID from gateway configuration rather than client-side Kount configuration. Critically, a **Kount Custom** integration with its own Kount merchant ID must contact Braintree **before migrating** so that ID is hard-coded into the Braintree gateway. All of this is snapshot-qualified historical migration guidance, not current SDK/Kount support or exact GitHub-version behavior.
  - Exact locator: major-API/code-change boundary lines 17-21; form/tokenization, formatting, modular and error-message changes lines 24-44; separate Drop-in migration and UI boundary lines 47-71; modular loading lines 74-84; client authorization/component boundary lines 88-123; Hosted Fields iframe and explicit tokenization lines 127-133; PayPal `3.63.0+` scope lines 206-208 and malformed callback token lines 219-247; shared client and Promise-polyfill warning lines 333-384; gateway-derived fraud configuration and Kount Custom pre-migration condition lines 388-393 — **PASS**.

## Shared bounded checks

- Raw gap sweep: one content/path-bounded sweep across Braintree client-SDK, upgrade and reference raws found the two assigned JavaScript raws, separate iOS v7 and Android v5 policy siblings, and the server-SDK deprecation policy. No second JavaScript snapshot or conflicting same-topic raw was found.
- Extra reads: none. The iOS, Android and server policy matches are different platform/server authorities and cannot add JavaScript facts; both assigned raws directly and completely answer the fixed questions.
- Full-raw/hash checks: both assigned raws were read completely; each computed SHA-256 matched its C26 manifest value. In each source page, `raw_files:` and `## Raw Sources` point to the same exact assigned raw.
- Reciprocal checks: `wiki/index.md` routes to `wiki/braintree-index.md`; that index directly lists both source pages and routes to `[[braintree-web-sdk]]`; the concept links both sources; each source links back to `[[braintree-web-sdk]]`, names `[[braintree]]`, and links its exact raw. Website policy/migration evidence remains separate from versioned GitHub implementation evidence.
- Final verdict: **PASS**.
