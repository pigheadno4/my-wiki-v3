# Braintree C43 fixed-query audit L — positions 45–48

- Campaign: `braintree-campaign-43`
- Mode: read-only independent query audit
- UTC start: `2026-10-07T11:48:12Z`
- UTC completion: `2026-10-07T11:49:14Z`
- Scope: manifest positions 45–48; exactly two fixed questions per page (8 total)
- Result: **8 PASS / 0 FAIL**

## Shared checks, bounded gap sweep, and extra authority

- **Manifest identity, pins, URLs, and primary ownership — PASS.** Source frontmatter, raw provenance, and manifest paths/URLs agree. Recomputed SHA-256 pins are: package-tracking Node `6a867f000b837d013e4abeee22e6a4a2f7e33396d937103ff2c535f054206aab`; Drop-in landing `30446e645e37b55f3d3b6fef5652d8e5832c6116f132bae1b84dfba0f43a0bdc`; Drop-in examples `53c38d38fa49a641823942676a114db4c19a3768919b4ae877eeaab422245aac`; Verifone P400 reference `d46b7e81f00b8ebf527609053651ffff018e326c9a1669d278711819995f337a`. Exact canonical-URL and raw-path lookup finds one primary source owner for each.
- **Full reads and reciprocal routes — PASS.** `CLAUDE.md`, `rules/query-and-synthesis.md`, the C43 selection questions/manifest positions, relevant root/provider routes, all three main concepts, all four selected sources, and all four pinned raws were read. Each source links its main concept and exact raw; each main concept links the source. The actual routes resolve from root index through the Braintree index and concept even before direct C43 catalog rows are added.
- **Package-tracking conflict authority — PASS.** The package-tracking overview source and its complete pinned raw were read because the selected Node page retains a lifecycle conflict. The overview says to add tracking after the transaction settles (`overview` raw lines 86–112); the selected Node page labels its creation step as after submitting for settlement (selected raw lines 63–111). The selected source explicitly preserves the difference and does not claim a currently accepted gateway status.
- **Drop-in lifecycle conflict authority — PASS.** The complete cumulative GitHub source, current `1.48.0` README, exact release manifest, and release note were read. The website raws state October 1, 2026/2027 milestones (both selected raws lines 17–22), while the exact `braintree-web-drop-in@1.48.0` README states September 1, 2026/2027 and the release manifest dates `1.48.0` to September 10, 2026. The selected sources retain this as source-specific conflict, not a resolved/current support commitment.
- **Bounded gap sweep — PASS.** Filename/topic search found package-tracking client-side, Drop-in setup/customization/tutorial, P400 hardware, and other Verifone material. None is required for another retained claim. The P400 page's firmware-release and EMV-receipt references remain explicitly **unread navigation only**; no version, receipt, sibling-device, exact-package, or runtime behavior was imported.
- **Deferred aggregate edges — PASS, not a content failure.** Direct provider/company source rows, company source count, provider log, and other campaign-close aggregates remain coordinator-owned close work. Their current absence does not break the concept-mediated evidence routes.

## Position 45 — `docs-guides-package-tracking-server-side-node` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:821` → `wiki/concepts/braintree-server-sdk.md:49` → `wiki/sources/braintree/source-braintree-docs-guides-package-tracking-server-side-node.md` → `raw/braintree/docs/guides/package-tracking/server-side/node-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is a 2026-09-16 capture of an unversioned Braintree server-side Node.js website example. It covers a transaction sale with line items and settlement submission, package-metadata creation, and later transaction lookup. It does not establish an exact Node package/runtime, current availability, merchant or transaction eligibility, product enablement, a complete runnable program, provider success, or authorization, capture, settlement, funding, shipment, carrier acceptance, delivery, buyer-notification, dispute, or hold-release outcomes. Evidence: source lines 12–23; raw lines 1–18 and 18–130.
2. **Central action, conditions/warnings, and raw detail — PASS.** The example sets `submitForSettlement`, creates package metadata with illustrative carrier/tracking values, `notifyPayer`, and optional line items, passes a transaction ID to `gateway.transaction.packageTracking()`, then uses `gateway.transaction.find()` to read tracker fields including a later `paypalTrackerId`. It correctly warns that the snippets depend on undefined surrounding variables and that the Node heading says “after submitting for settlement” while the overview says “after the transaction settles.” Exact sale, package, callback, and retrieval details remain at raw lines 18–60, 63–111, and 115–130; source locators are lines 31–36.

## Position 46 — `docs-start-drop-in` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:823` → `wiki/concepts/braintree-web-drop-in.md:41` → `wiki/sources/braintree/source-braintree-docs-start-drop-in.md` → `raw/braintree/docs/start/drop-in-2026-09-16.md`.

3. **Exact scope and non-inference — PASS.** This is an unversioned 2026-09-16 Braintree website landing snapshot for ready-made Drop-in UI across an app or website and for the complementary client/server SDK responsibility split. It is not exact-package implementation evidence or proof of current availability/support, merchant or buyer eligibility, payment-method enablement, platform/region/environment support, runtime compatibility, migration suitability, or payment success. Evidence: source lines 12–24; raw lines 1–26 and 57–76.
4. **Central purpose, conditions/warnings, and raw detail — PASS.** The page presents customizable Drop-in as a quick checkout route, assigns payment-detail collection to client SDKs and gateway requests to server SDKs, and routes server/client setup, optional PayPal/Venmo/Apple Pay, and Hosted Fields/custom alternatives. Its warning accurately retains the website's October 1, 2026 deprecation/no-updates date and October 1, 2027 unsupported/support-ending/possible-suspension date plus the page's iOS-specific migration direction, while preserving the September exact-version conflict and requiring current verification. Exact lifecycle, product, role, and navigation details remain at raw lines 17–22, 26–41, and 44–76; source locators are lines 23–32.

## Position 47 — `docs-start-example-integrations-drop-in-using-the-examples` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:823` → `wiki/concepts/braintree-web-drop-in.md:39` → `wiki/sources/braintree/source-braintree-docs-start-example-integrations-drop-in-using-the-examples.md` → `raw/braintree/docs/start/example-integrations-drop-in/using-the-examples-2026-09-16.md`.

5. **Exact scope and non-inference — PASS.** This 2026-09-16 Braintree website snapshot is navigation/example evidence for GitHub repositories in the listed server languages, with Braintree Web Drop-in as their client integration and local/Heroku as stated run targets. It proves no exact SDK/package version, current support, complete runnable environment, successful test/payment, authorization, settlement, or funding. Evidence: source lines 12–23; raw lines 1–29 and 41–67.
6. **Central purpose, conditions/warnings, and raw detail — PASS.** The page lists Java/Spring, .NET/ASP.NET, Node/Express, PHP, PHP/Slim, Python/Flask, and Ruby/Rails examples. Running one requires a Braintree Sandbox account and Merchant ID/public/private keys, while local setup is delegated to each repository README. Card testing routes to the testing reference; PayPal testing additionally requires a linked PayPal Sandbox account. The source also preserves the October lifecycle schedule, Android/iOS/JavaScript migration routes, and the September exact-version conflict without treating examples as current/runtime/payment proof. Exact lists and conditions remain at raw lines 17–22, 29–38, 41–52, and 55–67; source locators are lines 25–31.

## Position 48 — `in-person-reference-verifone-p400-reference` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:791` → `wiki/concepts/braintree-in-person.md:14` → `wiki/sources/braintree/source-braintree-in-person-reference-verifone-p400-reference.md` → `raw/braintree/in-person/reference/verifone-p400-reference-2026-09-16.md`.

7. **Exact scope and non-inference — PASS.** This is a collected, unversioned Braintree In-Person website device-reference page at a P400-specific URL, with a broader raw title and one shortcut row that separately mentions e285 deep sleep. It covers captured Verifone Reader app keypad/navigation behavior only. It does not prove current device availability, merchant/account eligibility, feature enablement, device health/connectivity, application/firmware compatibility, runtime behavior, production readiness, or any test/live payment. Evidence: source lines 12–29; raw lines 1–17 and 39–63.
8. **Central purpose, conditions/warnings, and raw detail — PASS.** The page documents numeric-key character cycling, off-screen close/back/accept-return controls, `2 + 8` for reader settings, and a captured `Hold X`/eight-second Power Panel row that distinguishes P400 reboot/shutdown from e285 deep sleep. It says the default PayPal screensaver indicates connected-and-ready-for-test-transactions, but the source correctly does not convert that statement into an observed health, connectivity, production, or payment result. Exact key-map, navigation, shortcut, and screensaver details remain at raw lines 17–33, 39–46, 49–61, and 63; source locators are lines 31–36. The linked firmware and EMV pages remain unread navigation.

## Handoff

- Corrections requested: none.
- Content blockers: none.
- Closure follow-up: coordinator adds/checks the four direct provider/company catalog rows, provider log, and shared source-count aggregates.
- Repository files modified: none. Audit artifact only: `/tmp/braintree-c43-query-audit-l.md`.

**Verdict: PASS — 4/4 pages and 8/8 fixed questions.**
