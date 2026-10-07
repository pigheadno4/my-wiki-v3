# Braintree C42 fixed-query audit — Group B

- Campaign: `braintree-campaign-42`
- Assigned manifest positions: 5–8
- Started (UTC): `2026-10-07T00:54:59Z`
- Completed (UTC): `2026-10-07T00:56:58Z`
- Verdict: **PASS — 8/8 fixed questions passed**

## Shared checks

- The four manifest pins match the files read in full: Venmo Android `24277e9684a617d0652ac6467b21ca5fdde85534b7533a9909506b075a9188fb`; Android Pay Card Node `7452dc248c5322beaeb90da301a5c87cd4b445411d9aace8f89f003bb817a093`; Credit Card Node `a7ac531ed2d0ea76a550bbcec75c9292d1cba4022903c354ec614661cb352099`; Apple Pay Card Node `6033f06ec6fadc3de9e38398b2b513c3ff7f13c44584521bd4502530b56e6ffd`.
- For all four pages, the manifest canonical URL equals the source frontmatter `canonical_url` and the raw line-1 Source URL; each source owns the pinned raw in `raw_files` and links it under `## Raw Sources`.
- The common route begins at `wiki/index.md:11` (`[[braintree-index]]`). Provider-to-concept links are present at `wiki/braintree-index.md:708,715,718`, and every selected source/main-concept pair is reciprocal. Exact-path filename sweeping found only the four pinned dated raws. No sibling, current-provider, GitHub, direct-PayPal/Apple, or navigation-only related raw was used as factual authority.
- Provider-index direct source rows and company/catalog aggregate rows are deferred coordinator-close work, separate from content retrieval failure. They do not break the required actual routes below.

## Position 5 — `docs-guides-venmo-client-side-android-v5`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:718` → `wiki/concepts/braintree-android-sdk.md:76` → `wiki/sources/braintree/source-braintree-docs-guides-venmo-client-side-android-v5.md:1-59` → `raw/braintree/docs/guides/venmo/client-side/android/v5-2026-09-16.md:1-564`.

1. **PASS — Exact scope and non-inference.** This is a collected Braintree Venmo **client-side Android v5 website-family** guide, covering SDK-managed Payment Buttons and a custom request/launcher/return/tokenization flow. The captured examples name `ui-components:5.25.0` and `venmo:5.8.0`, but those example coordinates are not current compatibility claims. The resulting nonce is a separate merchant-server input; the page does not prove current SDK support, merchant/buyer eligibility, production approval, authorization, capture, settlement, or funding. Evidence: source `:12-20,26-30`; raw `:23-49,138-178,208-233`.
2. **PASS — Central action, material conditions, warnings, and detail route.** The integration either lets the SDK launch Venmo and tokenize the return or has the merchant create the authorization request, persist the pending request, handle the app return, and tokenize success. Material conditions retained include eligibility plus Sandbox enablement, pre/post-purchase summaries, `MULTI_USE` versus `SINGLE_USE` consent and vaulting effects, `profile_id` for multiple profiles, per-transaction device data, ECD for addresses, and purchase-context `totalAmount`. The source also preserves the unresolved historical certificate/version tension rather than reconciling it. Exact code, field rules, and validations remain retrievable at source `:32-45` and raw `:37-40,174-203,231-335,343-365,387-422,427-560`.

## Position 6 — `docs-reference-response-android-pay-card-node`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:715` → `wiki/concepts/braintree-server-sdk.md:55` → `wiki/sources/braintree/source-braintree-docs-reference-response-android-pay-card-node.md:1-40` → `raw/braintree/docs/reference/response/android-pay-card/node-2026-09-16.md:1-284`.

3. **PASS — Exact scope and non-inference.** This is the collected Braintree **Node.js website response reference** titled `Android Pay Card`; it states that Google Pay cards are represented as Android Pay cards in Braintree's API to avoid breaking changes. No numeric Node package release is stated. The naming note is not evidence of current Google Pay availability, supported platforms/accounts/cards/regions, direct-Google behavior, package implementation, or payment success. Evidence: source `:12-20,28-31`; raw `:14-32`.
4. **PASS — Central purpose, limitations, and detail route.** The page's substantive action is lookup: the gateway returns product IDs for credit/debit payment methods, generally one to three characters, indicating the issued credit product. The captured containing-response-object list is blank, so no containing types or guaranteed field presence may be inferred. The complete code/name table, including repeated and region/network-qualified entries, remains at raw `:33-283`; summary locators are source `:22-31`.

## Position 7 — `docs-reference-response-credit-card-node`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:715` → `wiki/concepts/braintree-server-sdk.md:57` → `wiki/sources/braintree/source-braintree-docs-reference-response-credit-card-node.md:1-41` → `raw/braintree/docs/reference/response/credit-card/node-2026-09-16.md:1-282`.

5. **PASS — Exact scope and non-inference.** This is a collected Braintree **Node.js website Credit Card response reference** with no numeric Node package release stated. Its captured substance is returned product-ID metadata; it is not a card-creation, request, transaction-operation, SDK-implementation, eligibility, authorization, capture, settlement, or funding guide. Evidence: source `:12-21,29-32`; raw `:14-30`.
6. **PASS — Central purpose, material limitation, and detail route.** The page routes readers to a gateway product-ID code/name lookup; IDs are generally one to three characters and identify the issued credit product. Results are limited under the linked PayPal Data Protection Addendum, but this raw does not contain that external policy and the summary does not interpret it. The containing-response list has two blank entries, leaving a material schema gap. Exact lookup values are retrievable at raw `:28-281`; the limitation and gap are located at raw `:17-25` and source `:23-32`.

## Position 8 — `docs-reference-response-apple-pay-card-node`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:708` → `wiki/concepts/braintree-apple-pay.md:22` → `wiki/sources/braintree/source-braintree-docs-reference-response-apple-pay-card-node.md:1-44` → `raw/braintree/docs/reference/response/apple-pay-card/node-2026-09-16.md:1-280`.

7. **PASS — Exact scope and non-inference.** This is the collected Braintree **Node.js website Apple Pay Card response reference**, with no numeric Node package release stated. It identifies the response-reference object and its returned product-ID lookup; it is not native-client or direct-Apple authority, current availability/configuration evidence, sibling-SDK authority, or proof of authentication, acceptance, execution, authorization, settlement, or funding. Evidence: source `:12-22,31-34`; raw `:14-28`.
8. **PASS — Central purpose, limitations, and detail route.** The gateway lookup returns credit/debit product IDs, generally one to three characters, indicating the issued credit product. The containing-response-object bullets are empty, so containing types are not established; duplicate mappings such as `I` and `MHD` also prevent treating the code alone as a unique name key. The full table remains retrievable at raw `:29-279`, with the blank-list gap at raw `:17-21` and summary locators at source `:24-34`.

## Close result

No affected-question correction is required. All four selected pages preserve exact website/SDK-family scope, central retrieval purpose, consequential conditions or gaps, raw detail routes, and the required non-inference boundaries.
