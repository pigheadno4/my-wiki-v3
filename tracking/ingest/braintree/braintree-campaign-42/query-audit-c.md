# Braintree C42 fixed-query audit — Group C — 8/8 PASS

- Campaign: `braintree-campaign-42`
- Manifest positions: 9–12
- Started (UTC): `2026-10-07T01:00:40Z`
- Completed (UTC): `2026-10-07T01:01:34Z`
- Verdict: **PASS — 8/8 questions**
- Extra authority reads: none

## Shared checks

- **Manifest identity and pins — PASS.** Each canonical URL, source target and `raw_files` path matches the exact manifest job. Computed SHA-256 values match the manifest: Samsung Pay Card `b0f4ccb33d59c2d68ee3009f832b6ec95c3702adc98e712b204cd0f50f97dbc0`; Visa Checkout Card `76ee0fb2450a57fbffccf375d4f4f311f80ca279bc294f640d350b5598f71f4a`; Masterpass Card `4bab91df7d2ad45b913152084861491f31074177d567ba5e7c570a465168ab5d`; Payment Method Nonce `8b69db899116b1ae45b648168c5c23ab9d199c20d27a18b3b25549451ee6fff1`.
- **Evidence and routes — PASS.** The root index, provider index, both main concepts, all four canonical source pages and all four pinned raws were read in full. Every route below resolves. Main-concept reciprocity is present: Samsung Pay Card links to/from `braintree-payment-methods`; the other three link to/from `braintree-server-sdk`.
- **Bounded gap/conflict sweep — PASS.** The three wallet-labeled raws have the same substantive product-ID table while their titles differ; that does not establish wallet availability, applicability of every row, or cross-product behavior. Samsung Pay Card, Visa Checkout Card and Masterpass Card each have blank containing-response bullets; Payment Method Nonce has no containing-response section. Repeated `I` and `MHD` rows prevent a one-code-to-one-name inference. Separate nonce guide/create/find raws found by the filename sweep were not used because they concern different actions and the exact response raw is sufficient for these questions. No sibling SDK, GitHub, current-provider or unrelated-product behavior was imported.
- **Catalog boundary.** New company/provider source-catalog aggregation is deferred to coordinator close and is separate from these content verdicts; the required live root→provider→concept→source routes already work.

## Position 9 — `docs-reference-response-samsung-pay-card-node`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:707` → `wiki/concepts/braintree-payment-methods.md:27` → `wiki/sources/braintree/source-braintree-docs-reference-response-samsung-pay-card-node.md:1-39` → `raw/braintree/docs/reference/response/samsung-pay-card/node-2026-09-16.md:1-280`.

1. **PASS — Exact scope and non-inference.** This is the collected Braintree **Node.js-routed website response reference** titled `Samsung Pay Card`; it states no numeric Node package release, environment or account scope. Its captured action is a gateway-returned product-ID lookup for credit/debit card payment methods. The blank containing-response list means response membership is not established, and the title/table are not evidence of client-wallet behavior, current Samsung Pay availability, eligibility, SDK/GitHub implementation, or payment execution. Evidence: source `:2-9,14-16,20-23`; raw `:1-28`.
2. **PASS — Central purpose, limitations, and detail route.** The page says product IDs generally have one to three characters and indicate the issued credit product. Its material gaps are the two blank containing-response bullets and the lack of a populated property table; repeated `I` and `MHD` rows also prevent a unique code-to-name inference. The complete lookup is retrievable at raw `:28-279`, including `I` at `:66-67` and `MHD` at `:129,132-134`; summary routing is source `:25-30`.

## Position 10 — `docs-reference-response-visa-checkout-card-node`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:715` → `wiki/concepts/braintree-server-sdk.md:57` → `wiki/sources/braintree/source-braintree-docs-reference-response-visa-checkout-card-node.md:1-39` → `raw/braintree/docs/reference/response/visa-checkout-card/node-2026-09-16.md:1-280`.

3. **PASS — Exact scope and non-inference.** This is the collected Braintree **Node.js-routed website response reference** titled `Visa Checkout Card`, with no numeric Node package release, environment or account scope stated. Its body is not a request or client-integration guide. It does not establish a containing object, current Visa Checkout/SRC support, eligibility, client behavior, package implementation, or successful authorization, settlement, funding or other execution. Evidence: source `:2-9,14,18-21`; raw `:1-28`.
4. **PASS — Central purpose, limitations, and detail route.** Its substantive purpose is the gateway credit/debit product-ID code/name lookup, qualified as generally one to three characters. The two containing-response bullets are blank, no property table is populated, and duplicate `I`/`MHD` mappings preclude a unique-name assumption. Exact values remain at raw `:28-279`, with duplicates at `:66-67,129,132-134`; source locators are `:23-30`.

## Position 11 — `docs-reference-response-masterpass-card-node`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:715` → `wiki/concepts/braintree-server-sdk.md:53` → `wiki/sources/braintree/source-braintree-docs-reference-response-masterpass-card-node.md:1-42` → `raw/braintree/docs/reference/response/masterpass-card/node-2026-09-16.md:1-280`.

5. **PASS — Exact scope and non-inference.** This is the collected Braintree **Node.js-routed website response reference** titled `Masterpass Card`; no numeric Node package release, environment or account scope is stated. It is a narrow response-data lookup, not integration, card creation or transaction-operation authority. Its title does not establish current Masterpass availability, eligibility or that every listed product occurs in a Masterpass response; returned data is not payment-outcome proof. Evidence: source `:2-9,14,18-21,30-33`; raw `:1-28`.
6. **PASS — Central purpose, limitations, and detail route.** The page provides the generic gateway-returned credit/debit product-ID inventory and the generally one-to-three-character qualification. The captured containing-object bullets are blank, no complete object schema is established, and repeated `I`/`MHD` rows are explicitly preserved. The full table is retrievable at raw `:28-279`, with the duplicate rows at `:66-67,129,132-134`; source routing is `:23-28`.

## Position 12 — `docs-reference-response-payment-method-nonce-node`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:715` → `wiki/concepts/braintree-server-sdk.md:49` → `wiki/sources/braintree/source-braintree-docs-reference-response-payment-method-nonce-node.md:1-37` → `raw/braintree/docs/reference/response/payment-method-nonce/node-2026-09-16.md:1-273`.

7. **PASS — Exact scope and non-inference.** This is the collected Braintree **Node.js-routed website response reference** titled `Payment Method Nonce`, with no numeric Node package release, environment or account scope stated. Its captured body is only a returned product-ID lookup; the title does not prove fields on a particular nonce. It does not document nonce creation, lookup, lifespan, consumption, SDK implementation, or authorization/capture/settlement/funding. Evidence: source `:2-9,14,18-21`; raw `:1-21`.
8. **PASS — Central purpose, limitations, and detail route.** The gateway lookup covers credit/debit product IDs, qualified as generally one to three characters. This raw provides no containing-response section or property schema, and repeated `I` and `MHD` rows prevent a unique code-to-product interpretation. Exact values are retrievable at raw `:21-272`, including duplicates at `:59-60,122,125-127`; source locators are `:23-28`.

## Close result

No affected-question correction is required. All four pages preserve exact website/Node route and named-object scope, central lookup purpose, material gaps, precise raw detail routes, and the required non-inference boundaries. Group C passes **8/8**.
