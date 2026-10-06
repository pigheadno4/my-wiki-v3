# Braintree C41 fixed-query audit I — positions 33–36

- Campaign: `braintree-campaign-41`
- Mode: read-only query audit
- Assigned jobs: positions 33–36
- Required questions: 8 total, exactly 2 per page
- Analysis end (UTC): `2026-10-06T15:23:59Z`
- Result: **8 PASS / 0 FAIL** for content answers and retrieval

## Shared checks and bounded extra-evidence sweep

- Read `CLAUDE.md`, `rules/query-and-synthesis.md`, and the C41 fixed-query policy in `tracking/ingest/braintree/braintree-campaign-41/selection-review.md` before auditing.
- Followed the root/provider/concept/source/pinned-raw chain. Fully read all four promoted source pages and all four selected raws. Source `canonical_url` and `raw_files`, raw Source URL metadata, manifest identity, and pinned SHA-256 all match.

| Position | Job | Verified SHA-256 |
| ---: | --- | --- |
| 33 | `docs-reference-client-reference-javascript-v2-configuration` | `bd3eb7b5e3369a23c76cafe67a64d8f3918b13b0db1f89f71dd2c9c189f97ea7` |
| 34 | `in-person-guides-card-data-collection` | `da97a07c5432395f5419fcef8b8ab467587217d7d094fd746a7f3eeefbfaa5a3` |
| 35 | `docs-guides-fastlane-faq` | `881fda98c78733512be490f1b894fefdc4825acb66e3171e62e7a47d8d67d823` |
| 36 | `docs-guides-functions-cli-reference` | `e551cc90098e1b447554fd685f58fdb633da43ba5eb4abc54487fc65053e2519` |

- The bounded filename and related-route sweep found adjacent JavaScript-v2 references, the separate In-Person sub-processors page and GraphQL guides, other Fastlane guides, and other Functions guides. None is required to answer these eight page-scoped questions, so no extra authority was fully read or used as evidence.
- Bounded evidence gaps: the collected Card Data page links to a live GraphQL reference that is not preserved as an exact mutation-schema raw, so its rendered request/query samples are snapshot examples rather than current schema authority. Fastlane raw line 44 contains an unanchored warning about subdomains, wildcards, and protocols; the missing subject must not be reconstructed. The Fastlane vaulting answers conflict at raw lines 57–67 versus 81–85. The Functions raw contains `btfn ls --triggers` at line 103 while the documented namespace is `btfns`, and the default output text at line 214 is malformed; neither should be silently normalized.

## Position 33 — `docs-reference-client-reference-javascript-v2-configuration`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md:658` → `wiki/concepts/braintree-web-sdk.md:80` → `wiki/sources/braintree/source-braintree-docs-reference-client-reference-javascript-v2-configuration.md` → `raw/braintree/docs/reference/client-reference/javascript/v2/configuration-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This is the collected historical Braintree.js **JavaScript v2** browser-client reference for `braintree.setup(authorization, integrationType, options)`. The exact objects/actions are a client token or tokenization key string, a `dropin` or `custom` integration type, setup options, readiness/error/tokenization callbacks, and the payment-method details returned after client tokenization. It is not JavaScript v3, an exact retained GitHub/package version, a server API or credential-creation guide, current browser/SDK support, merchant enablement, or proof of authorization, capture, settlement, or payment completion. Object/action match is exact: configure and receive results from the v2 client integration, then hand a nonce to merchant server code.

Locators: source lines 12–23; raw identity and signature lines 1–26; common setup-option boundary lines 29–37; callback and integration-type conditions lines 38–59; returned-detail scope lines 62–107.

### Q2 — purpose, conditions, warnings, and detail route — PASS

The page's central purpose is to define setup-level configuration and callback handoff. `onReady` exposes teardown and, only for Custom, PayPal launch/close methods; `initAuthFlow` must run synchronously from a user click or the browser blocks the popup. Supplying `onPaymentMethodReceived` transfers responsibility to the merchant: Braintree.js neither inserts the hidden nonce nor submits the form automatically. `paymentMethodNonceReceived` is deprecated; Drop-in requires `container`, Custom requires `id`; error types vary by integration. PayPal billing-address output requires merchant eligibility/enabling, and phone output depends on the PayPal business-account setting. Precise option names, result fields, and value lists remain in the pinned raw.

Locators: source lines 18–31; raw CORS/CSP and readiness lines 35–45; tokenization/server-handoff and required-field lines 46–59; card details lines 62–75; PayPal field and eligibility conditions lines 77–107.

## Position 34 — `in-person-guides-card-data-collection`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md` provider catalog → **deferred missing edge** → `wiki/concepts/braintree-in-person.md:17` → `wiki/sources/braintree/source-braintree-in-person-guides-card-data-collection.md` → `raw/braintree/in-person/guides/card-data-collection-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This is a collected, unversioned Braintree **In-Person** website guide for using a Braintree reader to collect raw magstripe track data from non-PCI-scoped, ISO 7813 cards under merchant-account-configured BIN ranges. The exact objects/actions are `requestNonPciCardDataFromInStoreReader`, its reader/context ID, node polling of `InStoreContext.status`, retrieval of track 1/track 2 data, and optional caller-owned result display. It is not Braintree transaction processing, issuer authorization, vaulting, capture, settlement, funding, consent/security/retention guidance, current GraphQL-schema authority, or proof that a reader interaction or external-card transaction succeeded. Object/action match is exact: collect eligible card data and expose it to the API caller, which separately contacts any third-party issuer.

Locators: source lines 12–25; raw identity and feature boundary lines 1–24; account setup lines 27–32; request/context/query examples lines 35–48; caller-owned result lines 51–56.

### Q2 — purpose, conditions, warnings, and detail route — PASS

The central flow configures non-PCI BIN ranges, initializes a reader swipe, waits for interaction, polls the returned context at the page-stated two-second interval, retrieves available tracks, then lets the caller display its own external result. Braintree says PCI card data will not be returned; the card must use ISO 7813, must not conflict with known PCI BINs, and must fall within configured merchant ranges. Sandbox setup requires full test-card numbers or at least their first eight digits. The feature is unavailable offline; context data is retrievable for about ten minutes and deleted after the first successful retrieval. The caller should avoid PII in result text. The sub-processors link is navigation only, and the rendered mutation/query remains the page snapshot rather than exact current schema authority.

Locators: source lines 18–35; raw setup lines 27–32; request gate and variables lines 35–42; response qualification lines 45–48; display/PII warning lines 51–56; offline, format, BIN, retention and deletion conditions lines 59–77; sub-processor route lines 82–84.

## Position 35 — `docs-guides-fastlane-faq`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md:658` → `wiki/concepts/braintree-web-sdk.md:112` → `wiki/concepts/paypal-fastlane.md:91` → `wiki/sources/braintree/source-braintree-docs-guides-fastlane-faq.md` → `raw/braintree/docs/guides/fastlane/faq-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This collected, unversioned Braintree website FAQ covers merchants integrating **PayPal Fastlane through Braintree**: provisioning/disablement signals, identity/profile selectors, payment-token handling, delivery controls, CSP, vaulting answers, and Payment versus Flexible Integration responsibilities. The page names no Braintree Web SDK or hosted Fastlane runtime version. Its exact objects/actions include `triggerAuthenticationFlow()`, address/card selectors, `paymentToken`, `addressOptions`, `transaction.sale()`, and integration-form responsibilities. It is not direct PayPal Orders API guidance, a country-availability matrix, current merchant/buyer eligibility, security/privacy compliance proof, or evidence of authentication, token consumption, Vault, transaction, authorization, capture, or settlement success. Object/action match is exact: troubleshoot and select a Braintree Fastlane integration pattern.

Locators: source lines 12–26; raw identity and troubleshooting table lines 1–23; disablement behavior lines 25–40; integration-pattern table lines 103–120.

### Q2 — purpose, conditions, warnings, and detail route — PASS

The page's central purpose is troubleshooting plus implementation retrieval. An initialization authorization error may indicate missing merchant/client provisioning and routes to the account team. Merchant disablement falls back to guest checkout, while Control Panel disablement makes the three listed authentication/profile methods return `undefined`. Store pickup must use `pickupInStore` or `shipToStore`; the token lifetime is three hours; checkout reload should call `triggerAuthenticationFlow()` again to reauthenticate or restore the session and return a new token; and `addressOptions` limits merchant-allowed destinations rather than declaring country support. The CSP guidance gives `frame-src *.paypal.com` for Sandbox and Production, with a Hosted Card Fields exception. Most consequentially, vault-then-transact is both allowed at raw lines 65–67 and denied at lines 81–85; the page cannot resolve that contract, so neither route should be treated as authoritative without applicable current evidence.

Locators: source lines 20–37; raw provisioning/disablement lines 16–40; pickup lines 47–53; conflicting vault guidance lines 57–67 and 81–85; CSP lines 69–79; token/address/reload conditions lines 87–97; integration responsibilities lines 103–120. Raw line 44's unanchored domain-format warning remains an explicit evidence gap.

## Position 36 — `docs-guides-functions-cli-reference`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md:648` → `wiki/concepts/braintree-payment-platform.md:28` → `wiki/sources/braintree/source-braintree-docs-guides-functions-cli-reference.md` → `raw/braintree/docs/guides/functions/cli-reference-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This 2026-09-16 Braintree website snapshot is a **documentation-preview CLI reference** for `@braintree/functions-cli` and the `btfns` command namespace. Its objects/actions are CLI installation/uninstallation; creating, listing, testing, packaging, publishing and deploying functions; generating test JSON; and Braintree account login/logout with environment selection. It does not identify an exact CLI/package release and is not current Functions availability, account eligibility, runtime compatibility, exact GitHub implementation, or proof that authentication, testing, publishing, or deployment succeeded. Object/action match is exact: describe CLI commands and their documented local/account/environment effects.

Locators: source lines 12–22; raw identity/preview lines 1–18; installation and captured Node.js requirement lines 21–37; command inventory lines 47–67; account/environment command surfaces lines 107–149.

### Q2 — purpose, conditions, warnings, and detail route — PASS

The central purpose is a command-and-option lookup. The captured preview requires Node.js 8.x or 10.x and offers global npm installation or `npx`; treat those versions as snapshot-scoped, not current guidance. `deploy --production` targets production, `login` selects environment/merchant/user, and `ls` can select environment and account-deployed functions. `init` writes configuration/JavaScript files for one of three named templates, `generate-test-data` writes JSON beneath the generated project's `__tests__` directory, global uninstall removes the package, and logout ends the documented account session. Confirm account, environment and filesystem target before treating commands as an operational runbook; examples are not execution proof. Exact flags and effects remain in raw, including the unresolved `btfn`/`btfns` inconsistency and malformed default-output text.

Locators: source lines 18–35; raw installation/uninstall lines 21–45; deploy lines 70–84; init templates/options lines 89–105; login/logout/list lines 107–149; package/publish lines 152–180; simulation lines 183–197; generated-file effect lines 200–214.

## Deferred catalog/index closure — separate from content failures

- The four promoted source pages are linked reciprocally from their main concepts, but direct source-catalog entries are not yet present in `wiki/braintree-index.md`; coordinator-owned aggregate close should add/check them.
- `wiki/braintree-index.md` does not yet link the new `[[braintree-in-person]]` retrieval concept, leaving the position-34 provider-index route incomplete until close. The other three routes resolve through indexed concepts; Fastlane traverses indexed `[[braintree-web-sdk]]` to existing `[[paypal-fastlane]]`.
- No additional concept is required for these four pages. These deferred catalog edges do not change the **8 PASS / 0 FAIL** content result.

## Handoff

- Corrections requested: none.
- Content blockers: none.
- Closure follow-up: provider source-catalog entries and the `braintree-in-person` provider-index edge above.
- Handoff UTC: `2026-10-06T15:25:23Z`
