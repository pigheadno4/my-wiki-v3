# Braintree C41 fixed-query audit K — positions 41–44 — 8/8 PASS

Analysis end (UTC): `2026-10-06T15:38:43Z`
Handoff (UTC): `2026-10-06T15:39:11Z`

Scope: the four exact Group K promoted source pages and manifest-pinned primary raws. Repository remained read-only; this external handoff is the only write.

## Shared checks

- All four jobs are reviewer-approved in `jobs.json`. Source target, canonical URL, raw `Source URL`, and source `raw_files` identity match the manifest.
- Recomputed SHA-256 values match exactly: disputes `07fadb19b6fdf99eacd3a6b27d477d20b822175b88733787ec787208503509f2`; reporting/reconciliation `9a590604f745bf97f944d39c01e1f0ae68f3a2a8ef4ca8b774a262ec89e10caf`; display information `06e7e66b8c1264693ee919bf008f9375aa914845bf5dbdbc19e7976e6cbda7b6`; partners overview `bdd1ce677494ca60129aeac4b3200ee78dd1850e3a7d98a544402b5766529b6b`.
- All four promoted sources and pinned raws were read completely. The bounded filename and related-reference sweep found no conflict or answer gap requiring another full raw read.
- The live root/provider/concept/source/raw routes resolve. Aggregate company/index/catalog completeness remains coordinator-close scope; no missing aggregate edge was present in the current route state.

## 41. `docs-guides-disputes-managing`

Route: `[[index]]` → `[[braintree-index]]` → `[[disputes]]` → `[[source-braintree-docs-guides-disputes-managing]]` → `[[raw/braintree/docs/guides/disputes/managing-2026-09-16]]`.

1. **PASS — exact scope/non-inference.** This is an unversioned Braintree website guide, captured 2026-09-16, for API dispute management by merchants who can access disputes in the Braintree Control Panel (`AVAILABILITY`, raw lines 17–18). It documents merchant-account dispute objects and response actions, not current eligibility, independent bank/card-network policy, SDK/GitHub implementation, execution, adjudication, settlement, or returned-funds proof.
2. **PASS — purpose/actions/conditions/locators.** New bank-reported disputes create `open` objects; discovery routes are email, webhook, Search, or Find (raw 25–55). A merchant may Accept or challenge with text/file evidence, but evidence must be associated and the dispute finalized before `replyByDate()`; missing the deadline forfeits contest rights and changes status to `expired`, and Braintree will not forward an unfinalized response (raw 58–95). Exact reason-code/evidence requirements and operation schemas remain in the linked API references.

## 42. `in-person-guides-reporting-and-reconciliation`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-in-person]]` → `[[source-braintree-in-person-guides-reporting-and-reconciliation]]` → `[[raw/braintree/in-person/guides/reporting-and-reconciliation-2026-09-16]]`.

1. **PASS — exact scope/non-inference.** This is an unversioned 2026-09-16 Braintree In-Person website snapshot covering lifecycle/status navigation, an illustrative pass-through settlement/funding route, POS-supplied `orderId`, custom fields, and sample reports. It is not exact GraphQL schema, current account/report eligibility, or proof of authorization, capture, settlement, funding, bank deposit, report completeness, or successful reconciliation.
2. **PASS — purpose/actions/conditions/locators.** The page calls T+2 typical but card-scheme- and weekday-dependent and labels the Monday–Wednesday sequence a happy path; own-AMEX-SE merchants receive AMEX disbursements directly (raw 24–43). `orderId` correlates POS sales with Braintree settlement reporting, with exact limits delegated to the GraphQL reference (51–58). Searchable custom fields must be configured on the merchant account before the transaction or it fails (61–68); the three sample reports are generic and account-structure-dependent (71–75).

## 43. `in-person-guides-display-information`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-in-person]]` → `[[source-braintree-in-person-guides-display-information]]` → `[[raw/braintree/in-person/guides/display-information-2026-09-16]]`.

1. **PASS — exact scope/non-inference.** This unversioned 2026-09-16 Braintree In-Person guide documents GraphQL reader-screen text/line-item display requests and cancellation by returned context ID. The four text fields are only said to be supported “as of version 5.2.0,” without identifying the versioned component. Samples do not prove physical display, reader/device compatibility or current support, customer-data collection, checkout, payment, settlement, or funding; offline behavior, supported models/firmware, environments, and account enablement are not established.
2. **PASS — purpose/actions/conditions/locators.** Displays are nonblocking, may be repeated, and can be replaced by a separate charge request; a context ID supports cancellation, and a display lasts 120 seconds unless cancelled or overwritten (raw 19–28). Text is capped at 255 characters and the version-qualified fields are at 31–41. Line-item updates require resending the full cart/totals, allow up to 249 items, require POS-side calculations, and are neither processor input nor transaction storage (42–56). Cancellation and its `inStoreContextId` example are at 57–61.

## 44. `in-person-partners-overview`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-in-person]]` → `[[source-braintree-in-person-partners-overview]]` → `[[raw/braintree/in-person/partners/overview-2026-09-16]]`.

1. **PASS — exact scope/non-inference.** This unversioned 2026-09-16 Braintree In-Person overview says the GraphQL API behaves the same for partners and merchants while discussing partner-specific considerations for software providers bundling Braintree for multiple merchants (raw 16–21). It does not prove official-partner status, acceptance criteria, country or merchant eligibility, account/reader provisioning, feature availability, reader state, or payment outcome.
2. **PASS — purpose/actions/conditions/locators.** In the documented basic-auth example, each merchant has unique gateway-account API keys that a multi-merchant integration must make configurable (24–26). Account structures can affect deposits, reports, users, and other behavior, so the page recommends flexible hierarchy plus Solutions Engineer review (29–31). Official partners must transmit a BN code for tracking (34–36). Reader health, firmware update, location, pairing, display, and prompt calls are recommendations in addition to MVP charge/refund calls, not proof of setup or execution (39–52).

## Result

`8 PASS / 0 FAIL`. No content correction, expanded evidence read, or repository change is requested.
