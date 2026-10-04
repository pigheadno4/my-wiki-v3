# Braintree C33 fixed query audit — Group D — 8/8 PASS

- Analysis end UTC: `2026-10-04T04:17:05Z`
- Artifact handoff UTC: `2026-10-04T04:18:37Z`
- Scope: `reference-forward-api-tokenization-errors`, `reference-forward-api-validation-errors`, `reference-forward-api-functions`, `reference-forward-api-variables`; two fixed questions each.
- Authority rule: concepts were navigation only. Each answer was checked against the complete canonical source page and complete pinned raw. No sibling error, function, variable, destination, Orchestration, retry, or payment-lifecycle behavior is imported.

## reference-forward-api-tokenization-errors

**Object/action matched:** unversioned Braintree Forward API tokenization-error reference / classify failures returned by Forward API tokenization and provide selected sandbox negative-test triggers.

**Actual route:** `wiki/index.md:11` → `wiki/braintree-index.md:32` → `wiki/concepts/braintree-forward-api.md:27` → `wiki/sources/braintree/source-braintree-reference-forward-api-tokenization-errors.md:1-55` → `raw/braintree/docs/reference/forward-api/tokenization-errors-2026-09-16.md`.

1. **Q1 — PASS.** The precise evidence is the collected, unversioned **Tokenization Errors** reference for Forward API tokenization. It names no SDK, language, SDK version, endpoint, or request authentication scheme. The opening JSON is explicitly an illustrative response-body shape with `error`, `message`, and `request-uuid`; the catalog maps errors to HTTP 400, 422, or 500. Production Forward API use is eligibility-gated, while the supplied unsuccessful card/nonce and PayPal `max_amount` triggers are sandbox negative-test fixtures, not production rules. Locators: raw `5-20`, `22-54`, `59-77`.
2. **Q2 — PASS.** Its central purpose is failure classification for tokenization: unsupported instrument type is HTTP 400; the cataloged validation, issuer, risk, network, PayPal, cryptogram, and token-state conditions are HTTP 422; an unhandled tokenization exception is HTTP 500. The `Denied due to risk` explanation must never be shown to the customer because of information-disclosure risk. Some entries give condition-specific customer or alternate-method directions, but the page defines no general retry, remediation, destination acceptance, authorization, capture, settlement, or funding contract. Locators: raw `33-54`; disclosure warning `38`; fixtures `59-77`.

## reference-forward-api-validation-errors

**Object/action matched:** unversioned Braintree Forward API validation-error reference / describe request/configuration/security validation failures returned to the caller application.

**Actual route:** `wiki/index.md:11` → `wiki/braintree-index.md:32` → `wiki/concepts/braintree-forward-api.md:29` → `wiki/sources/braintree/source-braintree-reference-forward-api-validation-errors.md:1-60` → `raw/braintree/docs/reference/forward-api/validation-errors-2026-09-16.md`.

1. **Q1 — PASS.** This is the collected, unversioned **Validation Errors** reference. It names no SDK, language, SDK version, or endpoint. Its illustrative response body has top-level `error`, nested `message`, and `request-uuid`; every validation error is documented to carry `"validation_error?": true` in `message`, with error-specific fields where listed. Production Forward API use is subject to eligibility. Locators: raw `5-20`, `22-34`.
2. **Q2 — PASS.** The page's responsibility is to catalog validation failures in configuration shape, JSON/request inputs, HTTP methods/headers, URLs/network access, mutual-TLS certificate/key inputs, config/payment-method selection, and production-only restrictions. Inline certificates are sandbox-only; inline configs are forbidden in production and production configs require submission and approval; production `debug_transformations` is forbidden because it may return PCI-sensitive data; mutual TLS requires both certificate and key. Only the final two entries instruct retry after a specific change—updating Vault email/phone for AMEX network tokenization, or changing the payment method for an endpoint limited to `PayPalBillingAgreement` and `VenmoAccount`. They are not a general retry or success guarantee, and validation does not prove downstream destination or payment lifecycle behavior. Locators: raw `36-69`; production/config/debug boundaries `38-39`, `62`; mTLS `40-41`, `48`; scoped retries `68-69`.

## reference-forward-api-functions

**Object/action matched:** sparse, unversioned Braintree Forward API functions reference / identify the intentionally minimal transformation DSL and the route for requesting a missing function.

**Actual route:** `wiki/index.md:11` → `wiki/braintree-index.md:32` → `wiki/concepts/braintree-forward-api.md:28` → `wiki/sources/braintree/source-braintree-reference-forward-api-functions.md:1-53` → `raw/braintree/docs/reference/forward-api/functions-2026-09-16.md`.

1. **Q1 — PASS.** This is a collected, unversioned **Functions** page for the Forward API transformation DSL. It names no SDK, language, SDK version, endpoint, environment-specific invocation form, or function version. Production Forward API remains eligibility-gated. The captured `Parameters` section is empty: there is no function-name, signature, parameter, input/output, error, or lifecycle inventory to recover. Locators: raw `5-25`; empty inventory `25-29`.
2. **Q2 — PASS.** The only documented operational purpose is that Forward API's DSL has been kept intentionally minimal and Braintree provides a contact form when a needed function is unavailable. The page does not document any callable function or transformation behavior, so none is inferred from siblings. Its remaining content is a published **example RSA keypair**, including private-key-shaped material; it must not be copied, reused, or treated as a credential, and its presence proves no validity, environment support, key-management practice, runtime behavior, or payment outcome. Locators: raw `17-22`, `25-66`; example key section `30-66`.

## reference-forward-api-variables

**Object/action matched:** unversioned Braintree Forward API variables reference / resolve literal, global, template, local, and payment-method-qualified values while constructing a destination request.

**Actual route:** `wiki/index.md:11` → `wiki/braintree-index.md:32` → `wiki/concepts/braintree-forward-api.md:26` → `wiki/sources/braintree/source-braintree-reference-forward-api-variables.md:1-65` → `raw/braintree/docs/reference/forward-api/variables-2026-09-16.md`.

1. **Q1 — PASS.** This is the collected, unversioned **Variables** reference for Forward API transformation strings. It names no SDK, language, SDK version, endpoint, or request-authentication mechanism; production use is eligibility-gated. The captured page documents lookup mechanics but ends at an empty `Available Global Variables` heading, so it supplies no name-by-name global-variable inventory. Locators: raw `5-22`, `62-65`.
2. **Q2 — PASS.** Most strings remain literal; `$variable_name` performs a global lookup with increasing precedence **Forward API → request `data` → request `sensitive_data`**, so `sensitive_data` wins collisions. `$/section/...` reads from the partially constructed request and serializes under `request_format`; `$/var/name` is transformation-local, non-serialized, and cannot be supplied by config or forwarding request. Apple Pay exposes the DPAN and DPAN expiration rather than underlying card data. Multiple-token variables are 1-indexed, with unsuffixed and `_1` resolving to the first method. The captured payment-method-plus-nonce sentence is malformed but says nonce variables are `_2`-suffixed; no fuller request shape is reconstructed from siblings. These are construction/substitution rules, not destination authority, acceptance, execution, or lifecycle guarantees. Locators: raw `22-50`, `53-59`, `62-65`.

## Shared provenance, gaps, sweep, and link checks

- **Manifest/hash PASS:** tokenization errors `95b18012c99d3f912a78415a5069db0aee1c9954b66353f024b300d136bfcf26`; validation errors `e1250b9b037de0d8ad2fbedc80553dfb97210eeda1a575a914e2804adb070087`; functions `69504d3a72c856d9d69e3cfab9812e3183fca5175d6ee24d9fce07e33981b566`; variables `6601c5d5b73f520fc154a8ab0ff6990fbeeef23a217f51f812b4bc67c261859e`. Recomputed bytes match `manifest.json`.
- **Canonical/source/raw PASS:** every source frontmatter canonical URL and `raw_files` value matches its manifest job, every `## Raw Sources` entry links the exact dated primary raw, and each raw source comment matches the canonical URL. Reverse lookup maps each primary raw to exactly one canonical source. Exact canonical-URL searches found no older same-canonical content snapshot; sitemap occurrences are discovery metadata, so no historical conflict read was needed.
- **Reciprocal navigation PASS:** root index links Braintree index; Braintree index links `braintree-forward-api`; that concept links all four sources; every source links the concept and its exact raw. Direct source/company catalog aggregation is deferred to campaign close; complete indexed concept routes make that non-fatal here.
- **Sweep / extra reads:** filename and focused-content sweeps found the selected raws, their declared navigation-only related Forward API pages, discovery sitemaps, and one Hyperwallet destination example containing the common `validation_error?` field. None was needed to answer a selected page or resolve a conflict, so no sibling or destination authority was promoted and no extra raw was fully read or used as factual authority. No raw promotion is recommended.
- **No shared evidence gap:** all eight fixed questions are answered from complete, successfully retrieved, hash-matched selected source/raw pairs. Sparse and malformed captured content is disclosed rather than repaired; no Orchestration, downstream execution, automatic retry, authorization, capture, settlement, funding, or runtime guarantee is invented.
