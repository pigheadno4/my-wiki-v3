# Braintree C41 fixed-query audit J — positions 37–40

- Campaign: `braintree-campaign-41`
- Mode: read-only query audit
- Assigned jobs: positions 37–40
- Required questions: 8 total, exactly 2 per page
- Analysis end (UTC): `2026-10-06T15:32:55Z`
- Result: **8 PASS / 0 FAIL** for content answers and retrieval

## Shared checks and bounded extra-evidence sweep

- Read `CLAUDE.md`, `rules/query-and-synthesis.md`, and the C41 fixed-query policy in `tracking/ingest/braintree/braintree-campaign-41/selection-review.md` before auditing.
- Followed the root/provider/concept/source/pinned-raw chain. Fully read all four promoted source pages and all four selected raws. Source `canonical_url` and `raw_files`, raw Source URL metadata, manifest identity, and pinned SHA-256 all match.

| Position | Job | Verified SHA-256 |
| ---: | --- | --- |
| 37 | `in-person-hardware-verifone-v400m` | `df698417d9f721d700ea740f9807961e772cbdbb4edf98250ef320f66e119a7b` |
| 38 | `docs-guides-ach-testing-go-live` | `2d60b06e110ed7e41d8cef2f6301a4338364f22683ac3e9faaa885299b0ec4bc` |
| 39 | `in-person-about-technical-overview` | `d0516dd2c79dd7ca25a7a7dd281cf75259bd7a3047ce478727b7a91c165e2380` |
| 40 | `docs-guides-payment-method-types-overview` | `a77c95119b653a5c844126c4f6b864e378a0e5882ff6111b75aa89d91a27f6bc` |

- The bounded filename and related-route sweep found the separate ACH lifecycle/eligibility raw, the V400m-linked integration checklist and E285 page, and the adjacent P400/M400 reader pages. None is required to answer these eight exact-page questions, so no extra authority was fully read or used as evidence.
- Bounded evidence gaps: the ACH capture has missing verification-state labels at raw lines 60–64 and 70, so those labels must not be reconstructed. The Technical Overview's captured support table lists P400, E285 and M400 at raw lines 44–47 but not V400m; the separately assigned, later-updated V400m page documents that device. This snapshot difference neither proves that V400m was supported at the Technical Overview's capture point nor that it is currently supported or unsupported. Linked GraphQL references, method-specific support pages and SDK changelogs remain navigation, not evidence, unless separately read.

## Position 37 — `in-person-hardware-verifone-v400m`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md` provider catalog → **deferred missing edge** → `wiki/concepts/braintree-in-person.md:22` → `wiki/sources/braintree/source-braintree-in-person-hardware-verifone-v400m.md` → `raw/braintree/in-person/hardware/verifone-v400m-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This is a 2026-09-16 collected, unversioned Braintree **In-Person hardware** page for the Verifone V400m. Its exact scope is the V400m device, terminal kit, optional charging and charging-plus-Ethernet bases, fixed-stand privacy shield, captured hardware specifications, entry modes, WiFi support, and reader/location/gateway-level idle-screen image configuration. It names no SDK, API version or software package. It is not documentation for the E285, P400, M400 or another reader and does not establish current availability, certification, PCI compliance of a whole deployment, merchant/account enablement, reader pairing or online state, payment-method enablement, or successful authorization, capture, settlement or funding. Object/action match is exact: evaluate the captured V400m hardware/interface constraints and request idle-screen configuration through the documented engineering handoff; it is not a transaction-processing procedure.

Locators: source lines 12–30; raw identity and device scope lines 1–21; kit/accessory scope lines 24–34; specifications lines 37–47; base/interface behavior lines 50–66; entry modes and WiFi lines 69–77; idle-screen configuration scope lines 80–82.

### Q2 — purpose, conditions, warnings, and detail route — PASS

The page's central purpose is a V400m hardware and customization reference. A fixed-stand installation marks the privacy shield as required for PCI compliance. Ethernet is described only while docked on the full-feature base, and that base does not automatically switch the reader between Ethernet and WiFi when docked or undocked. Captured WiFi scope is 2.4 GHz with WPA 1/2 PSK using CCMP (AES) or TKIP. A custom image must meet the listed 320-by-464-pixel, 72-dpi, JPG/GIF/PNG, 2 MB and GIF-only-animation constraints; the request supplies the applicable reader serial numbers or location IDs, or uses gateway-account scope, through a PayPal Solutions Engineer or Integration Engineer. The page says configuration refresh occurs within 12 hours or on reboot; that statement is not proof of completed configuration or current reader state. Exact specifications, file tips, submission identifiers and the post-go-live support route remain in the pinned raw.

Locators: source lines 18–42; raw fixed-stand condition lines 27–34; base and no-auto-switch warning lines 50–66; WiFi values lines 75–77; scope and file constraints lines 80–97; format tips lines 102–111; upload steps, refresh statement and support route lines 116–133.

## Position 38 — `docs-guides-ach-testing-go-live`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md:649` → `wiki/concepts/braintree-payment-methods.md:25` → `wiki/sources/braintree/source-braintree-docs-guides-ach-testing-go-live.md` → `raw/braintree/docs/guides/ach/testing-go-live-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This is a collected, unversioned Braintree **ACH Direct Debit Testing and Go Live** website guide. It scopes ACH to eligible merchants implementing a custom client-side integration with the JavaScript v3 SDK and explicitly excludes Drop-in UI; it does not pin an exact JavaScript v3 package version. Its objects/actions are sandbox routing/account-number fixtures for network-check, micro-transfer and independent-check verification; a verified bank-account payment method plus amount-selected transaction simulations; transaction-status and qualified webhook behavior; and production account-setting, webhook-endpoint and enablement steps. It is not proof of current merchant eligibility or enablement, a real bank account or its ownership, a live debit, exact present SDK behavior, production credentials, completed production configuration, authorization, settlement or funding. Object/action match is exact: select synthetic sandbox responses and prepare a production transition, not execute or prove a live ACH lifecycle.

Locators: source lines 12–30; raw availability and SDK/UI scope lines 14–18; verification fixtures lines 21–67; sandbox transaction fixtures lines 68–92; production checklist lines 95–100.

### Q2 — purpose, conditions, warnings, and detail route — PASS

The central purpose is to supply sandbox fixtures and a short go-live checklist. Routing-number tests use a real nine-digit routing number; network-check and micro-transfer results depend on the exact account-number tables. Account `1000000001` simulates a three-business-day micro-transfer settlement delay and requires the displayed micro-deposit values. Independent-check sandbox verification accepts any 4–17-digit number. Transaction simulation requires a verified bank-account payment method; listed amounts select failure or settlement-declined paths, while amounts outside the table are described as successful in sandbox. The webhook footnote is limited to final Settlement Declined outcomes for insufficient funds or unauthorized transaction. Before live use, the page instructs the merchant to mirror tested settings, recreate transaction webhooks in production against production endpoints, and contact Braintree for production ACH enablement. All fixtures are synthetic, and the malformed/missing state labels must not be inferred. Exact account numbers, response codes, amounts, statuses, deposit values and production steps remain in the pinned raw.

Locators: source lines 18–40; raw routing and network-check values lines 24–45; micro-transfer values and incomplete state narratives lines 48–64; independent-check condition lines 65–67; verified-method prerequisite and amount/status table lines 68–85; successful-sandbox conditions lines 86–92; go-live steps lines 95–100.

## Position 39 — `in-person-about-technical-overview`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md` provider catalog → **deferred missing edge** → `wiki/concepts/braintree-in-person.md:18` → `wiki/sources/braintree/source-braintree-in-person-about-technical-overview.md` → `raw/braintree/in-person/about/technical-overview-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This is a collected, unversioned, high-level Braintree **In-Person architecture** page. It frames In-Person as additional Braintree GraphQL objects and mutations. The exact object/action chain is an API caller acting for a `Merchant`, creating `InStoreLocation` objects with `createInStoreLocation`, pairing `InStoreReader` objects with `pairInStoreReader`, retaining generated location and reader IDs, creating an `InStoreContext` with `requestChargeFromInStoreReader` using amount and reader ID, retaining the context ID, polling context status, and receiving a `Transaction` object after customer interaction. It is not exact-version GraphQL schema or SDK/GitHub authority, a complete field/error/permission contract, a deployment design, current account/hardware eligibility, reader pairing or online proof, or evidence of authorization, capture, settlement, funding or successful payment. Object/action match is exact: explain the application-mediated object relationship and polling flow, not prove any runtime outcome.

Locators: source lines 12–22; raw page purpose and GraphQL boundary lines 14–23; exact object/mutation flow lines 26–34; high-level capability navigation lines 50–61.

### Q2 — purpose, conditions, warnings, and detail route — PASS

The central purpose is an architectural orientation plus navigation to detailed flows. The caller must retain generated location, reader and context IDs for the stated later actions, and the application polls context status while the customer interacts. Verifone manufactures the terminal hardware while the page assigns most device functionality/software to Braintree. The captured table calls P400, E285 and M400 available, but that is snapshot documentation, not current availability, provisioning, firmware, connectivity or merchant compatibility. Sandbox and Production readers are stated to behave the same but are not interchangeable: special test cards work on Sandbox readers, and test cards do not work on Production readers. The functionality table's sale, authorization, refund, vaulting, display, prompt, card-data, QR and offline labels are navigation only; verify their separate guides and applicable conditions before using them. Precise current GraphQL schema details must be retrieved from a complete applicable GraphQL authority, not inferred from this overview's links.

Locators: source lines 18–30; raw retained-ID and polling flow lines 26–34; hardware responsibility and snapshot table lines 37–47; environment/test-card warning lines 41–42; capability routes lines 50–61; final architecture/coverage navigation line 63.

## Position 40 — `docs-guides-payment-method-types-overview`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md:649` → `wiki/concepts/braintree-payment-methods.md:23` → `wiki/sources/braintree/source-braintree-docs-guides-payment-method-types-overview.md` → `raw/braintree/docs/guides/payment-method-types-overview-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This is a collected, unversioned, provider-wide Braintree **Payment Method Types** orientation for adding a method to an existing Braintree integration. It assumes client-side and server-side SDK integrations but pins no SDK, API or package version; granular version support is delegated to SDK changelogs. Its scope is production-account banking-partner compatibility, merchant and customer region, account/provider configuration, customer-facing collection UI and client options, method-dependent server handling of payment-method nonces and extra data, end-to-end sandbox/production testing, go-live work, and a separate third-party-provider ownership boundary. It is not a payment-method support matrix, current availability or enablement for a named merchant/buyer/method, exact SDK behavior, proof of testing or go-live, or authorization, capture, settlement or funding evidence. Object/action match is exact: orient selection and integration stages for a payment method type, not provide a method's exact implementation contract.

Locators: source lines 12–28; raw guide-family purpose lines 14–29; account/region qualifications lines 34–48; SDK/version and third-party boundaries lines 51–60; staged integration actions lines 63–75.

### Q2 — purpose, conditions, warnings, and detail route — PASS

The central action is to choose a compatible method, enable/configure it and complete any provider registration, add client UI/options, update server handling when required, then test in Sandbox and Production and complete method-specific go-live steps. Banking-partner support for the production account and both merchant and customer location materially qualify selection. The same nonce-handling server code may work only for simple cases; some methods require extra server-call data, prohibit actions such as vaulting, or need a distinct server implementation. Third-party carts/providers own their client/server integration handling. The merchant must inform payers that Braintree processes the payment using one of the page's two supplied disclosure routes; implementation should use the exact raw language rather than an audit paraphrase. The page's recommendation to use latest SDK versions is snapshot guidance, not a pinned compatibility guarantee. Exact availability, version, fields, regional/account compatibility, fees and disclosure text remain routed to the applicable support/reference/changelog authority and the pinned raw.

Locators: source lines 18–40; raw banking-partner and region conditions lines 37–48; SDK and third-party boundary lines 51–60; four integration stages and method-specific server limits lines 63–75; payer-disclosure requirement and exact text lines 78–81; help/detail routes lines 86–92.

## Deferred catalog/index closure — separate from content failures

- All four promoted source pages have reciprocal main-concept entries, but direct source-catalog entries are not yet present in `wiki/braintree-index.md`; coordinator-owned aggregate close should add/check them.
- `wiki/braintree-index.md` does not yet link the new `[[braintree-in-person]]` retrieval concept. The position-37 and position-39 provider-index routes are therefore incomplete until close. Positions 38 and 40 resolve through the already indexed `[[braintree-payment-methods]]` concept at provider-index line 649.
- No additional concept is required for these four pages. These deferred catalog edges do not change the **8 PASS / 0 FAIL** content result.

## Handoff

- Corrections requested: none.
- Content blockers: none.
- Closure follow-up: add/check the four provider source-catalog entries and the `braintree-in-person` provider-index edge above.
- Handoff UTC: `2026-10-06T15:34:12Z`
