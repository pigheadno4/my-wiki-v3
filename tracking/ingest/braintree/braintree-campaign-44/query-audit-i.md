# Braintree C44 fixed-query audit — group I

- Scope: approved C44 positions 33–36; eight predetermined queries.
- Result: **PASS — 8/8 queries**.
- Completed UTC: `2026-10-07T12:51:22Z`

## Shared checks

- **Pins, URLs, provenance and primary ownership — PASS.** Recomputed SHA-256 values match the manifest: In-Person Request Dev Kit `18be844da99d09f68b3065d8a2c8be75e95c8951532727a9bdc5968d8ed6b4c7`; IP Addresses `45d4ccc0cc7e22180f603aeddb200d8c8f2e16d9134b2bedea4839d74063eeaf`; Countries Node `b32f558895495c5d19f5c095af0628b59e49db4e077f4448adbc31b043103dfb`; Google Pay Decrypted Server Side Node `7a80dd4586d180f4235c80880a0468fc16bfc8d12663ebdbbbde8f818bc0c6c1`. Manifest URL, source `canonical_url`, raw `Source URL`, `raw_files`, and path-qualified `Raw Sources` agree. The four raw paths, URLs and source targets are unique, and each pinned raw has exactly one primary source owner. All raws record `Fetched: 2026-09-16` and `Discovery: llms.txt,sitemap.xml`.
- **Reciprocity and retrieval — PASS.** Routes resolve from `wiki/index.md:11` through provider-owned concepts linked at `wiki/braintree-index.md:791,812-813,821`, then reciprocal source/concept links, source frontmatter, and exact primary raw. Direct C44 source rows are not yet in the provider catalog; this is deferred coordinator close work, not a failure while the concept-mediated routes work.
- **Full reads and bounded gap sweep — PASS.** Read all four sources and pinned raws completely. One bounded filename/topic sweep covered adjacent In-Person onboarding, IP allowlisting, country, and Google Pay routes. Only the retained Google Pay comparison needed supporting evidence: the normal server-side source and raw were read in full and confirm the client-produced nonce/device-data route (`source-braintree-docs-guides-google-pay-server-side-node.md:14-19`; raw `:25-67`). That supporting raw remains owned by its own source and does not duplicate a primary here. Other adjacent raws remain navigation-only because the primary evidence answers the queries.
- **Scope and examples — PASS.** Answers preserve provider, document, product, SDK-family, version, environment, account/actor, object and action scope. Illustrative JavaScript is nonblocking: no source makes a runnable, current-package, present-availability or successful-execution guarantee, and the material risks, empty captured country list and amount qualification are retained.

## Position 33 — `in-person-get-started-1-get-started` — PASS / PASS

**Route:** `wiki/index.md:11` → `wiki/braintree-index.md:791` → `wiki/concepts/braintree-in-person.md:14` → `wiki/sources/braintree/source-braintree-in-person-get-started-1-get-started.md:12-50` → `raw/braintree/in-person/get-started-1/get-started-2026-09-16.md:1-48`.

1. **Exact scope and non-inference — PASS.** This is Braintree's fetched 2026-09-16, unversioned In-Person Dev Kit onboarding page. It covers an approval-gated request for a Sandbox reader and card-present test cards; actors/conditions are a PayPal/Braintree Account Executive or Solutions Engineer and either a signed NDA or existing Braintree merchant status. It is not an SDK/client-server credential guide and does not prove current eligibility, approval, kit receipt, reader readiness, production enablement, or a payment outcome. Source `:14,18-21`; raw `:14-24,44-46`.
2. **Purpose, action, conditions, warning and detail route — PASS.** After Account Executive approval, request through the Account Executive/Solutions Engineer, or contact Sales if neither is engaged; while waiting, follow the separately linked Sandbox, technical-overview and developer-doc routes. The material warning is that Dev Kit Sandbox readers are incompatible with production environments and cannot read production cards. Exact request/receipt conditions and wait-state routes remain at raw `:19-36,40-46`. Source `:18-35`.

## Position 34 — `docs-reference-general-braintree-ip-addresses` — PASS / PASS

**Route:** `wiki/index.md:11` → `wiki/braintree-index.md:812` → `wiki/concepts/braintree-payment-platform.md:28` → `wiki/sources/braintree/source-braintree-docs-reference-general-braintree-ip-addresses.md:12-41` → `raw/braintree/docs/reference/general/braintree-ip-addresses-2026-09-16.md:1-52`.

3. **Exact scope and non-inference — PASS.** This is Braintree's fetched 2026-09-16, unversioned website reference for a merchant-managed server/firewall allowing outbound access to Braintree Production or Sandbox destination domains and linked IP ranges. It names no SDK/version, merchant-specific network, ports/protocols or inbound Braintree-origin rule. The collected domain list is not a current-IP guarantee, request-authenticity/security proof, connectivity proof, or payment-success evidence. Source `:14,18-24`; raw `:14-22,25-52`.
4. **Purpose, action, conditions, warning and detail route — PASS.** The purpose is additive allowlisting when merchant security policy would otherwise block server-to-Braintree access. Use the intended environment's FQDNs and linked `ips.json`; Braintree says addresses can change and recommends watching that file. Incorrect/incomplete rules may prevent payment processing, so no static snapshot is promoted as a current firewall inventory. Production details are at raw `:25-38`; Sandbox at `:39-52`; change/failure warnings at `:18-22`. Source `:18-32`.

## Position 35 — `docs-reference-general-countries-node` — PASS / PASS

**Route:** `wiki/index.md:11` → `wiki/braintree-index.md:821` → `wiki/concepts/braintree-server-sdk.md:64` → `wiki/sources/braintree/source-braintree-docs-reference-general-countries-node.md:12-43` → `raw/braintree/docs/reference/general/countries/node-2026-09-16.md:1-143`.

5. **Exact scope and non-inference — PASS.** This is a fetched 2026-09-16, unversioned Braintree Node.js-routed website reference illustrating billing-country inputs to `gateway.transaction.sale()` in callback and Promise forms. It names no exact npm package, Node runtime, environment, merchant/account eligibility or other operation/object contract. The examples do not establish current gateway acceptance, country/payment-method/card coverage, authorization, settlement, or successful execution. Source `:14,18-20,33-34`; raw `:14-16,19-133`.
6. **Purpose, action, conditions, warning and detail route — PASS.** The page presents four alternatives: `billing.countryCodeAlpha2`=`US`, `countryCodeAlpha3`=`USA`, `countryCodeNumeric`=`840`, or `countryName`=`United States of America`; it does not say to send them together. The captured `List of countries` section is empty, so no supported-country inventory may be inferred. Its separate `Unknown` note concerns a returned BIN-derived card issuance country, not the merchant-supplied billing inputs. Exact examples are at raw `:19-133`; empty list/`Unknown` at `:135-140`. Source `:18-29`.

## Position 36 — `docs-guides-google-pay-decrypted-server-side-node` — PASS / PASS

**Route:** `wiki/index.md:11` → `wiki/braintree-index.md:813` → `wiki/concepts/braintree-payment-methods.md:29` → `wiki/sources/braintree/source-braintree-docs-guides-google-pay-decrypted-server-side-node.md:12-42` → `raw/braintree/docs/guides/google-pay/decrypted-server-side/node-2026-09-16.md:1-86`.

7. **Exact scope and non-inference — PASS.** This is a fetched 2026-09-16, unversioned Braintree Google Pay server-side webpage selected through the Node.js route for a merchant server that has already decrypted Google Pay payment data. It creates a sale from decrypted `androidPayCard` values, unlike the separately verified normal client-nonce/device-data handoff. It names no exact package/runtime, environment or eligible merchant/account and does not prove current availability, decryption correctness, authorization, settlement or payment success. Source `:14,30-38`; primary raw `:14-26`; supporting normal-route raw `:25-67`.
8. **Purpose, action, conditions, warning and detail route — PASS.** The central action is `gateway.transaction.sale()` using the decrypted PAN, cryptogram, expiration, card metadata and Google transaction ID, with `submitForSettlement: true`; include `eciIndicator` when the decrypted data contains an ECI. Braintree explicitly discourages server-side decryption because it increases risk and compliance burden. The client-side request amount should reflect what is authorized and submitted for settlement, while the page says transactions can still process when fulfillment changes the amount; that statement is not generalized into a success guarantee. Callback fields are at raw `:29-55`, Promise at `:57-83`, and amount guidance at `:84-86`. Source `:18-28`.

## Query tally

| Page | Q1 exact scope | Q2 purpose/actions/conditions/detail route |
| --- | --- | --- |
| In-Person Request Dev Kit | PASS | PASS |
| IP Addresses and Firewall Allowlisting | PASS | PASS |
| Countries Reference (Node.js) | PASS | PASS |
| Google Pay Decrypted Server-Side (Node.js) | PASS | PASS |

No correction is required. **Verdict: PASS — 4/4 pages, 8/8 fixed queries.**
