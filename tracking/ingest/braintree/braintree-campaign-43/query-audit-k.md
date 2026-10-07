# Braintree C43 fixed-query audit K — positions 41–44

- Campaign: `braintree-campaign-43`
- Mode: read-only independent query audit
- UTC start: `2026-10-07T11:45:47Z`
- UTC completion: `2026-10-07T11:47:27Z`
- Scope: manifest positions 41–44; exactly two fixed questions per page (8 total)
- Result: **8 PASS / 0 FAIL**

## Shared checks, bounded gap sweep, and route ownership

- **Manifest identity, pins, URLs, and unique ownership — PASS.** The four selected job IDs, source targets, raw paths, canonical URLs, and SHA-256 values are pairwise unique. Recomputed hashes match the manifest: Amex Direct `2d894ec17d0470caa55ce7ca2c2ac41ddfe83c529e39550fe1739bf89ce2ac8d`; PayPal Commerce iOS theming `cbdc9de9d54fa85706aae79961bf4733f6e1953eacef19e294b14f7f4b0e3ded`; Google Pay Android v5 testing/go-live `ec2f974e2f7804a937743f55c4f4bac93830f57e5b75b181545e16e3ebd72b19`; In-Person firmware updates `5079724759627f786658789ea44dd4fde6081b5425b4c696e44305293b019a7a`. Each exact raw path and canonical URL has one source owner under `wiki/sources/`.
- **Full reads and reciprocal routes — PASS.** `CLAUDE.md`, `rules/query-and-synthesis.md`, C43 selection questions and manifest positions, root/provider route entries, all four main-concept route entries, all four source pages, and all four pinned raws were read. Each actual route resolves root index → Braintree index → one primary concept → source → exact raw, and each source/main-concept pair links reciprocally.
- **Bounded gap sweep — PASS.** Filename/topic searches found the broader PayPal Commerce iOS family, Google Pay iOS/JavaScript testing variants, and In-Person release-note/troubleshooting routes, but no sibling authority was needed to support a retained material claim or resolve a conflict. Those pages, the linked test-amount/test-nonce authorities, PayPal Commerce setup page, firmware release notes, RMS beta page, and troubleshooting page remain **unread navigation only** and are not used as evidence here. No platform, package, current-site, or runtime behavior was transferred.
- **Deferred aggregate edges — PASS, not a content failure.** Direct source rows in `wiki/braintree-index.md` and `wiki/companies/braintree.md`, plus the campaign-wide company count/log close, remain coordinator-owned closure work. Their current absence does not break the four actual concept-mediated routes.

## Position 41 — `docs-guides-amex-direct-industry-specific-node` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:768` → `wiki/concepts/braintree-server-sdk.md:52` → `wiki/sources/braintree/source-braintree-docs-guides-amex-direct-industry-specific-node.md` → `raw/braintree/docs/guides/amex-direct-industry-specific/node-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is a captured, unversioned Braintree Node.js website guide for optional transaction industry data when the gateway uses an American Express Direct processor connection. Its object/action scope is one Lodging or Travel/Cruise industry-data type per transaction, illustrated through `gateway.transaction.sale()`. It does not establish a Node package/runtime version, current merchant or transaction eligibility, processor enablement, interchange treatment, request acceptance, authorization, settlement, or funding. Evidence: source lines 12–23; raw lines 1–19.
2. **Central purpose, conditions/warnings, and raw detail — PASS.** The entry preserves the Amex Direct condition and one-industry-type limit, distinguishes the required Travel/Cruise `travelPackage` and required Lodging folio/check-in/check-out fields, and treats callback/Promise blocks as examples rather than runnable or successful-payment proof. Exact field values, formats, limits, and routine example syntax remain at raw lines 22, 27–68, 72, and 77–116; source locators are lines 25–31.

## Position 42 — `docs-guides-paypal-commerce-ios-initial-theming-and-configuration` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:772` → `wiki/concepts/braintree-ios-sdk.md:83` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-commerce-ios-initial-theming-and-configuration.md` → `raw/braintree/docs/guides/paypal-commerce-ios/initial-theming-and-configuration-2026-09-16.md`.

3. **Exact scope and non-inference — PASS.** This is a Braintree-hosted, unversioned PayPal Commerce iOS snapshot for optional initial store configuration and theming via `PayPalCommerce-Config.plist` and `PayPalCommerce-Assets.xcassets`. It is kept distinct from the modern modular Braintree iOS SDK and names no SDK release or environment. The 2025-04-01 page metadata and 2026-09-16 fetch do not prove current account eligibility, package behavior, runtime theme application, asset availability, or payment execution. Evidence: source lines 12–22; raw lines 1–19.
4. **Central purpose, conditions/warnings, and raw detail — PASS.** Including the two files supplies optional initial setup, while most values are overridden by PayPal Commerce Panel theme settings. The source preserves the consequential deferred-onboarding behavior: skipping initial onboarding shows products first but requires completion when an incompletely onboarded user attempts a purchase. Routine font/scanning/color keys, modal styling, asset roles, and exact sizes remain retrievable at raw lines 22–43; source locators are lines 24–28. No exhaustive optional-style or runnable-code treatment is required.

## Position 43 — `docs-guides-google-pay-testing-go-live-android-v5` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:771` → `wiki/concepts/braintree-android-sdk.md:74` → `wiki/sources/braintree/source-braintree-docs-guides-google-pay-testing-go-live-android-v5.md` → `raw/braintree/docs/guides/google-pay/testing-go-live/android/v5-2026-09-16.md`.

5. **Exact scope and non-inference — PASS.** This is a 2026-09-16 snapshot of a Braintree Google Pay testing/go-live guide routed as Android v5. It covers sandbox user-flow/testing behavior and separate production-account/Google access steps, not an exact Android package release or runtime. It does not establish current SDK or certificate status, merchant/device eligibility, account enablement, Google review approval, runtime behavior, or successful payment execution. The March 30, 2026 certificate notice and Android `4.45.0+`/`5.0.0+` thresholds are correctly retained as historical page wording. Evidence: source lines 12–23; raw lines 1–24.
6. **Central purpose, conditions/warnings, and raw detail — PASS.** Full-flow testing needs a stored card or PayPal account, while checkout can add one when absent. Sandbox returns testing nonces and routes simulated server outcomes to separate references; completed Google Pay versus PayPal-through-Google-Pay classification and the environment-qualified `payer_email` difference are preserved. Go-live requires the Braintree production Control Panel toggle plus Google's separate production-access/app-review process; merchant-account-specific enablement routes to Braintree. Exact steps and navigation remain at raw lines 22–40; source locators are lines 25–31. None proves enablement, review completion, or payment success.

## Position 44 — `in-person-post-launch-activities-managing-firmware-updates` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:738` → `wiki/concepts/braintree-in-person.md:18` → `wiki/sources/braintree/source-braintree-in-person-post-launch-activities-managing-firmware-updates.md` → `raw/braintree/in-person/post-launch-activities/managing-firmware-updates-2026-09-16.md`.

7. **Exact scope and non-inference — PASS.** This is a collected, unversioned Braintree In-Person website guide for facilitating card-reader firmware updates through either the reader admin menu or a GraphQL mutation sample. It identifies no exact reader model, SDK/API version, current firmware release, or account/device enablement. It is not evidence of update availability or completion, an installed version, reader health/readiness, support status, transaction processing, authorization, capture, settlement, funding, or payment execution. Evidence: source lines 12–29; raw lines 1–21 and 24–36.
8. **Central purpose, conditions/warnings, and raw detail — PASS.** Readers must be powered on and online, and the page recommends Sandbox testing before production. The reader-menu route uses an environment-specific passcode, conditionally shows **Install Update**, downloads/installs, and restarts; the displayed credential is Sandbox-only and production routes to support. The GraphQL sample uses `requestFirmwareUpdateFromInStoreReader` with `readerId` and returns sample context/reader/status/version fields, none of which guarantees real device state or success. Exact menu commands and sample schema remain at raw lines 24–36; source locators are lines 31–38. Release notes, RMS beta, and troubleshooting are correctly segregated as unread navigation.

## Handoff

- Corrections requested: none.
- Content blockers: none.
- Closure follow-up: coordinator adds/checks the four direct provider/company catalog rows and campaign-wide aggregate/log updates.
- Repository files modified: none. Audit artifact only: `/tmp/braintree-c43-query-audit-k.md`.

**Verdict: PASS — 4/4 pages and 8/8 fixed questions.**
