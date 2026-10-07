# Braintree Campaign 44 fixed-query audit — group G

## Shared checks

- Assignment **PASS**: group G covers manifest positions 25–28 only. This was a repository-read-only audit; the only write is this external report.
- Pins, canonical ownership and provenance **PASS**:

  | Pos. | Canonical URL | Pinned raw | SHA-256 |
  | ---: | --- | --- | --- |
  | 25 | `https://developer.paypal.com/braintree/docs/guides/google-pay/server-side/node` | `raw/braintree/docs/guides/google-pay/server-side/node-2026-09-16.md` | `ff79e6cd43c643052f17dc520dbc080c07de7ed9c8cd31c4ea5c8ec923d1ff07` |
  | 26 | `https://developer.paypal.com/braintree/docs/reference/general/level-2-and-3-processing/overview` | `raw/braintree/docs/reference/general/level-2-and-3-processing/overview-2026-09-16.md` | `c5f9ee46b18db1157ea686e5ee5d86f2d7098b575ae5cbbbf49f0233dec8c186` |
  | 27 | `https://developer.paypal.com/braintree/docs/guides/amex-express-checkout/overview` | `raw/braintree/docs/guides/amex-express-checkout/overview-2026-09-16.md` | `46b2fb76342d967a28cea5528867b9f33e0dbcec148115d45d7d3882db57baaf` |
  | 28 | `https://developer.paypal.com/braintree/docs/guides/functions/overview` | `raw/braintree/docs/guides/functions/overview-2026-09-16.md` | `73ed3d6367a273d4fb7524ec07ac0c19e6088af246f326fc355288dc403f7a4f` |

  Each canonical URL and pinned raw has exactly one source owner under `wiki/sources/`; source frontmatter matches the manifest, each candidate is byte-identical to its promoted source, and each Raw Sources link resolves to the exact pinned raw.
- Retrieval and reciprocity **PASS**: all actual routes resolve from `[[index]]` through `[[braintree-index]]`, the named main concept, the source and exact raw. Every source links its main concept and every concept links back to the source. Deferred direct provider-catalog rows, company counts and close-time log aggregation are not failures while these concept routes work.
- Full-read and bounded-gap sweep **PASS**: all four source pages and all four primary pinned raws were read in full. A single filename/topic sweep found Google Pay integration/support siblings, Level 2/3 required-fields and Wells IC siblings, Amex setup/client/server/test siblings, and Functions task/CLI siblings. None is needed for a retained claim or conflict; they remain navigation, not duplicate primary authority.

## Position 25 — `docs-guides-google-pay-server-side-node`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-methods]]` → `[[source-braintree-docs-guides-google-pay-server-side-node]]` → `[[raw/braintree/docs/guides/google-pay/server-side/node-2026-09-16]]`.

1. **Scope — PASS.** This is a Braintree-hosted, unversioned Node.js-routed server-side Google Pay webpage snapshot fetched 2026-09-16. Its objects/actions are a client-produced Google Pay card nonce and device data passed into a server `transaction.sale()` request, plus qualified Vault storage. “Latest Android and JavaScript SDKs” is only the page's captured family-level availability wording; no exact Node package/runtime, environment or account enablement is identified. Do not infer current support, direct Google/PayPal Orders integration, successful sale/submission/settlement/funding, or successful Vault storage. Raw: lines 1–22, 25–70 and 73–84.
2. **Purpose/action and material conditions — PASS.** The source accurately routes nonce/device-data handoff, callback/Promise sale examples, legacy `AndroidPayCard` response identity, and the distinction between conditionally supported Google Pay card storage and unsupported PayPal-account vaulting with the named store options. It flags the damaged opening instruction and treats syntax as illustrative, not runnable proof. Precise examples and conditions remain at raw lines 30–67, 69–70 and 73–84.

## Position 26 — `docs-reference-general-level-2-and-3-processing-overview`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-platform]]` → `[[source-braintree-docs-reference-general-level-2-and-3-processing-overview]]` → `[[raw/braintree/docs/reference/general/level-2-and-3-processing/overview-2026-09-16]]`.

1. **Scope — PASS.** This is a Braintree general-reference, unversioned webpage snapshot for Level 2/3 credit-card processing, not an SDK or environment guide. Its objects/actions are specific Level 2 transaction data and Level 3 line-item/additional data supplied when creating sales for certain Visa/Mastercard corporate or purchasing cards. Account scope is US merchants with a linked Tax ID and EU/UK merchants with a linked VAT ID, further conditioned on MCC qualification. Do not infer current card-network policy, a complete eligible-card/field table, exact API/SDK version, actual merchant/card/MCC eligibility, lower interchange, authorization, settlement or funding. Raw: lines 1–20 and 21–25.
2. **Purpose/action and material conditions — PASS.** The page says the data can help qualify for lower interchange, distinguishes Level 2 from Level 3 inputs, records snapshot-qualified US Visa CEDP wording, and explains network reporting to business cardholders. It directs exact field details to Required Fields and account/use-case questions to bank-specific articles or support; the source preserves that CEDP has no effective date and makes no rate guarantee. Raw: lines 16–20 and 23–25.

## Position 27 — `docs-guides-amex-express-checkout-overview`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-methods]]` → `[[source-braintree-docs-guides-amex-express-checkout-overview]]` → `[[raw/braintree/docs/guides/amex-express-checkout/overview-2026-09-16]]`.

1. **Scope — PASS.** This is a 2026-09-16 Braintree snapshot of the legacy Amex Express Checkout website overview and its stated SRC replacement, not an exact implementation or environment guide. It records SRC introduction labels for Android v2, iOS v4 and JavaScript v3 client-SDK generations, not current package support. Merchant/account scope is most US-domiciled merchants or merchants processing through a direct Amex account; cardmember scope is US. The principal objects/actions are an Amex merchant-specific card number stored by Braintree and a nonce used to create transactions. Do not infer current Amex/SRC support, access, enablement, migration success or payment outcome. Raw: lines 1–23 and 24–35.
2. **Purpose/action and material conditions — PASS.** The source preserves the checkout credential flow, Vault-and-nonce handoff and the Control Panel → client script → server adjustment → test/go-live setup route. Crucially, it leaves unresolved the same-page conflict between “replaced by SRC” and Amex Express Checkout being “currently available,” while retaining SRC's limited-release eligibility, changeable API and access-request warnings. Exact statements and route links remain at raw lines 17–18, 20–28 and 29–35.

## Position 28 — `docs-guides-functions-overview`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-platform]]` → `[[source-braintree-docs-guides-functions-overview]]` → `[[raw/braintree/docs/guides/functions/overview-2026-09-16]]`.

1. **Scope — PASS.** This is a Braintree Functions documentation-preview snapshot fetched 2026-09-16. It describes Braintree-platform triggers executing uploaded merchant-provided code that interacts with partners/vendors and may map responses back to Braintree. It identifies no exact SDK, runtime, version, client/server placement, environment or account eligibility, and the raw does not call Functions beta. Do not infer current availability, production readiness, enablement, deployment, third-party response, code success, payment authorization or transaction outcome. Raw: lines 1–22 and 23–28.
2. **Purpose/action and material conditions — PASS.** The source accurately presents Functions as opening the Braintree API to provided code, with payment-method authorization, accounting, fraud-score and custom-workflow examples rather than guaranteed capabilities. It preserves Braintree-owned triggers, merchant-code responsibility for partner/vendor interaction, conditional response mapping, existing-integration orientation, and the inquiry/next-step routes. Precise examples and navigation remain at raw lines 17–28, 29–44 and 45–54.

## Close

- Result: **8/8 answers PASS**.
- Corrections: none.
- Blockers: none.
- Audit completed (UTC): `2026-10-07T12:48:06Z`.
