# Braintree C43 fixed-query audit A — positions 1–4

- Campaign: `braintree-campaign-43`
- Mode: read-only independent query audit
- UTC start: `2026-10-07T11:08:21Z`
- UTC completion: `2026-10-07T11:10:24Z`
- Scope: manifest positions 1–4; exactly two fixed questions per page (8 total)
- Result: **8 PASS / 0 FAIL**

## Shared checks and bounded sweep

- **Manifest identity and pins — PASS.** Source `canonical_url`, source `raw_files`, raw Source URL metadata, manifest identity, and recomputed SHA-256 agree for all four assignments: ACH `52b171d41ec7fcb3cf2b4e29876a0d3c7f586007379097958e876d595ceacc37`; PayPal iOS `3075cdb1a4f807343ddaf0f92bbc568977175e9a783897be02d81ecf41ab624e`; deprecated JavaScript encryption `c7caf1d40e95c28e5ca6114c8c62993fbf600da279a01a35e3e53136081b663b`; dispute testing `471f05d17d858a9fc80becae6082bcb7c0ed0b9262ddc7b0e18ad15314c2251c`. Exact raw-path and canonical-URL lookup finds one source owner each.
- **Full reads and retrieval truth — PASS.** `CLAUDE.md`, `rules/query-and-synthesis.md`, the C43 selection questions/manifest, root and Braintree indexes, all four relevant main concepts, all four canonical sources, and all four pinned raws were read. Central actions, consequential prerequisites/warnings, and non-inference boundaries are retained; routine values, procedures, fields, and examples remain at exact raw locators.
- **One bounded additional-authority read — PASS.** The dispute-testing source retains the separate production `replyByDate()` boundary, so the canonical managing-disputes source and its full raw were read once for that claim: `wiki/sources/braintree/source-braintree-docs-guides-disputes-managing.md` and `raw/braintree/docs/guides/disputes/managing-2026-09-16.md` (SHA-256 `07fadb19b6fdf99eacd3a6b27d477d20b822175b88733787ec787208503509f2`). It establishes deadline-bound evidence finalization and bank-review handoff; it is supporting authority only, not ownership of the sandbox-testing page.
- **Navigation and reciprocity — PASS.** Every actual route resolves root → provider index → main concept → canonical source → exact raw. Each source links its main concept and each concept links back. Direct provider/company catalog rows are absent as expected before coordinator close; that deferred aggregate work is not a content failure.
- **Bounded gap sweep — PASS.** The filename/owner sweep found related ACH detail pages, the Android PayPal client-side sibling, the deprecated iOS encryption sibling, and the disputes-managing page. No sibling/current/GitHub/direct-PayPal behavior was transferred. The iOS sample contains `payPalbuttonView` while constructing `payPalButtonView`; the dispute samples use captured illustrative syntax and a past-dated example expiry. These are nonblocking because no retained claim says the snippets compile, are copy-paste runnable, or prove current SDK/runtime behavior.

## Position 1 — `docs-guides-ach-overview` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:760` → `wiki/concepts/braintree-payment-methods.md:23` → `wiki/sources/braintree/source-braintree-docs-guides-ach-overview.md` → `raw/braintree/docs/guides/ach/overview-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is a 2026-09-16 snapshot of an unversioned Braintree overview for US ACH Direct Debit. Its captured availability is limited to eligible merchants using a custom JavaScript v3 client integration plus a server-side SDK, and it explicitly excludes Drop-in UI. It does not establish current eligibility or enablement, another client surface, exact SDK/package behavior, bank-account ownership, or a successful debit, transaction, settlement, or funding outcome. Locators: source lines 12–28; raw lines 14–21.
2. **Central action, material conditions/warnings, and detail locator — PASS.** The route organizes ACH acceptance as tokenizing, vaulting, verifying, and transacting. Tokenization of bank account/routing details yields a one-time nonce that is neither verification nor transactable; it must be vaulted and successfully verified. Vaulting may initiate verification or defer it, but successful verification remains the transaction prerequisite. The captured verification choices are network check, micro-transfers, independent check, and Instant Verification; methods may be combined, with network check then micro-transfers only a recommended example. Exact lifecycle and method descriptions remain at raw lines 23–33, 36–53, and 56–72; source locators are lines 30–38.

## Position 2 — `docs-guides-paypal-client-side-ios-v7` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:772` → `wiki/concepts/braintree-ios-sdk.md:83` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-client-side-ios-v7.md` → `raw/braintree/docs/guides/paypal/client-side/ios/v7-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is a collected Braintree website page on the iOS v7 PayPal client-side route. It covers Braintree iOS SDK setup and SDK-managed PayPal buttons that present `ASWebAuthenticationSession`, run authentication, and return a nonce/error callback after tokenization. The v7 route is not an exact package release or current support statement; it does not prove account linking, merchant/buyer eligibility, app-switch/fallback behavior, successful tokenization, server transaction creation, authorization, capture, settlement, or funding. Locators: source lines 12–24; raw lines 27–60.
2. **Central action, material conditions/warnings, and detail locator — PASS.** Before adding PayPal, the merchant must integrate the Braintree iOS SDK and create, verify, and link a PayPal account in the Braintree Control Panel. The captured CocoaPods/SPM/Carthage names and SwiftUI/UIKit-wrapped button examples stay in the raw. The page's consequential historical warning says mobile SDK certificates would expire March 30, 2026, directs iOS integrations to 6.17.0+, and warns older published app traffic would fail unless decommissioned or force-upgraded; the source correctly does not turn this into current v7/package status. Exact setup names, button responsibility, examples, and One-Time/Vaulted/Recurring routes are at raw lines 17–22, 27–60, 63–105, 116–131; source locators are lines 28–38.

## Position 3 — `docs-deprecated-client-side-encryption-javascript-library` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:769` → `wiki/concepts/braintree-web-sdk.md:80` → `wiki/sources/braintree/source-braintree-docs-deprecated-client-side-encryption-javascript-library.md` → `raw/braintree/docs/deprecated/client-side-encryption/javascript-library-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is a historical Braintree JavaScript Client-Side Encryption page whose entire integration method is explicitly deprecated. It describes client encryption for a browser or mobile application, merchant-server forwarding through a Braintree client library, and gateway-side decryption. It names no exact current SDK/package or environment and does not establish present support, browser compatibility, PCI/compliance status, tokenization, authorization, processing, settlement, or any payment outcome. Locators: source lines 12–27; raw lines 17–29 and 39–57.
2. **Central action, material conditions/warnings, and detail locator — PASS.** The client encrypts sensitive fields such as card number, CVV, and expiration date with the Braintree public key, forwards ciphertext to the merchant server over HTTPS, and the server forwards it to the gateway whose private key decrypts it. `onSubmitEncryptForm` encrypts fields marked `data-encrypted-name` before form submission; its optional callback follows encryption, and the page warns that multiple submit handlers have no guaranteed cross-browser order. `encryptForm` supports custom pre-encryption callback logic, while `encrypt` is the single-string compatibility/customization path. Exact helper signatures and behavior remain at raw lines 30–36 and 58–93; source locators are lines 29–37.

## Position 4 — `docs-guides-disputes-testing-go-live-node` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:778` → `wiki/concepts/disputes.md:335` → `wiki/sources/braintree/source-braintree-docs-guides-disputes-testing-go-live-node.md` → `raw/braintree/docs/guides/disputes/testing-go-live/node-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is an unversioned Braintree Node-routed website page for sandbox dispute testing by merchants who can access disputes in the Braintree Control Panel. It covers creating a sandbox sale that is instantly disputed and simulating `won`/`lost` outcomes through evidence finalization. It is not an exact Node SDK/package contract, direct PayPal Disputes API authority, current card-network policy, a production test, or proof of a real dispute, adjudication, returned funds, settlement, or payment result. Locators: source lines 12–22; raw lines 17–36 and 60–62.
2. **Central action, material conditions/warnings, and detail locator — PASS.** The central action is a sandbox `Transaction: Sale` with the listed test card; the page says this creates a settled sale with an `open` dispute and can exercise email, a configured webhook, lookup, and response paths. Certain amounts select stated reason-code fixtures. Adding exactly `compelling_evidence` then finalizing simulates `won`; `losing_evidence` then finalizing simulates `lost`. These are deterministic sandbox fixtures, not production rules or outcome guarantees. The supporting managing-disputes authority separately requires production evidence to be finalized before `replyByDate()` for bank review; the testing page itself does not state that deadline. Exact card/amount fixtures and callback/Promise examples remain at raw lines 22–49, 60–97, 101–125, and 130–154; source locators are lines 24–33; supporting deadline raw lines 58–62 and 72–95.

## Handoff

- Corrections requested: none.
- Content blockers: none.
- Closure follow-up: add/check the four direct provider source-catalog rows and company/count aggregates during coordinator close.
- Repository files modified: none. Audit artifact only: `/tmp/braintree-c43-query-audit-a.md`.

**Verdict: PASS — 4/4 pages and 8/8 fixed questions.**
