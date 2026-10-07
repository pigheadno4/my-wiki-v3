# Braintree Campaign 43 fixed-query audit — group M

- Campaign: `braintree-campaign-43`
- Mode: read-only independent query audit
- UTC start: `2026-10-07T11:49:05Z`
- UTC completion: `2026-10-07T11:49:56Z`
- Scope: manifest positions 49–50; exactly two fixed questions per page (4 total)
- Result: **4 PASS / 0 FAIL**

## Shared checks

- **Manifest pins and ownership — PASS.** Position 49 is `https://developer.paypal.com/braintree/docs/guides/amex-express-checkout/amex-brand-requirements`, raw `raw/braintree/docs/guides/amex-express-checkout/amex-brand-requirements-2026-09-16.md`, SHA-256 `d7160cc5f09538c9f9199f4c48bed1359db86b05932db2f9e280315a20e18b71`. Position 50 is `https://developer.paypal.com/braintree/docs/guides/google-pay/overview`, raw `raw/braintree/docs/guides/google-pay/overview-2026-09-16.md`, SHA-256 `44a036952c061144b03220e14ab2e75e0f07ce42c209bf30093c171be93ea4bc`. Recomputed hashes, raw URL metadata, source frontmatter and manifest values agree; each canonical URL and raw path has one source owner.
- **Routes and reciprocity — PASS.** Both actual routes resolve `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-methods]]` → exact source → pinned raw. Each source links the concept and the concept links each source. The promoted source files exactly match their approved attempt-1 candidates. Provider/company direct rows, counts and log updates are coordinator close-time aggregates, not content failures.
- **Full reads and bounded sweep — PASS.** Both sources and both pinned raws were read completely. Because position 49 retains the SRC support-status conflict, `source-braintree-payment-methods-secure-remote-commerce` and `source-braintree-get-started-payment-methods` plus their pinned raws were also read completely: they confirm the unresolved January 20, 2026 end-of-support notice versus current-tense limited-release wording. Other Amex/Google Pay sibling pages and the Google Pay support article remain unread navigation; no claims were imported from them.

## Position 49 — `docs-guides-amex-express-checkout-amex-brand-requirements`

Route: `wiki/index.md:11` → `wiki/braintree-index.md:69` → `wiki/concepts/braintree-payment-methods.md:25` → `wiki/sources/braintree/source-braintree-docs-guides-amex-express-checkout-amex-brand-requirements.md` → `raw/braintree/docs/guides/amex-express-checkout/amex-brand-requirements-2026-09-16.md`.

1. **Scope and non-inference — PASS.** This is an unversioned Braintree website snapshot fetched 2026-09-16 for legacy Amex Express Checkout button and acceptance-mark presentation. Its replacement notice names SRC and labels Android v2, iOS v4 and JavaScript v3 as introduction points, but does not identify an exact package/runtime or environment. It does not prove current Amex Express Checkout or SRC support, a safe migration, merchant/buyer eligibility, account enablement, tokenization, transaction execution, settlement or funding. Source lines 12–26; raw lines 14–26.
2. **Central purpose, conditions/warnings and detail retrieval — PASS.** The source preserves the required use of supplied unmodified graphics, radio-button presentation order, exact product-name spelling/capitalization/style, prohibition on substitute Amex marks, blue-box acceptance-mark distinction, and clickable-button requirement; it correctly treats placement before most manual-entry fields as a suggestion. It also retains replacement-by-SRC, eligible-merchant limited release, API-change and contact-for-access warnings without choosing a current-support answer. Exact brand inventory and presentation detail remain at raw lines 20–26; replacement and SDK-family wording is at raw line 18; the retained conflict is independently visible in the supporting SRC raw at lines 14–15 and 21–48.

## Position 50 — `docs-guides-google-pay-overview`

Route: `wiki/index.md:11` → `wiki/braintree-index.md:70` → `wiki/concepts/braintree-payment-methods.md:23` → `wiki/sources/braintree/source-braintree-docs-guides-google-pay-overview.md` → `raw/braintree/docs/guides/google-pay/overview-2026-09-16.md`.

1. **Scope and non-inference — PASS.** This is an unversioned Braintree developer-overview snapshot fetched 2026-09-16 for Google Pay in-app and web purchasing by customers with supported Android devices. It labels Braintree's “latest” Android and JavaScript SDK families but supplies no exact package version. It does not establish current availability, merchant/buyer eligibility, Google approval, account enablement, device/browser compatibility, runtime behavior, tokenization, authorization, payment, settlement or funding. Source lines 12–26; raw lines 14–22.
2. **Central purpose, conditions/warnings and detail retrieval — PASS.** The source preserves the four-stage route—configure, client, server, test/go-live—the basic client/server card-integration recommendation for new Braintree integrations, and the production Google merchant-ID prerequisite. It distinguishes the JavaScript standalone-button path from the Payment Request component and treats the Android Pay-to-Google Pay Android v4 page as navigation, not a retained migration procedure. Exact route links and alternatives remain at raw lines 25–33, 38–44 and 47–55; inventories, compatibility and implementation detail are not duplicated or treated as execution proof.

## Close

- Verdict: **PASS — 2/2 pages and 4/4 fixed questions**.
- Corrections: none.
- Content blockers: none.
- Repository files modified: none; audit artifact only at `/tmp/braintree-c43-query-audit-m.md`.
