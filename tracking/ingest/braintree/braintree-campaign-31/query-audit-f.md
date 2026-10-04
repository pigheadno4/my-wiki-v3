# C31 Query Audit F — 4/4 PASS

Campaign contract: group F is `lpm-pay-upon-invoice-ios-v7` + `lpm-alipay`, four questions (`selection-review.md:42-54`). Both jobs are reviewer-approved in `jobs.json` (`lpm-alipay`: lines 288-304; Pay Upon Invoice iOS v7: lines 364-380), and this audit uses the promoted wiki pages, not candidate drafts.

## Q1 — Pay Upon Invoice iOS v7 exact route — PASS

**Object/action match:** locate the named Pay Upon Invoice document at the iOS v7 route and descend to its pinned website raw.

**Exact route:** `wiki/index.md:11` → `wiki/braintree-index.md:399` → `wiki/concepts/braintree-payment-methods.md:23` → `wiki/sources/braintree/source-braintree-local-payment-methods-pay-upon-invoice-ios-v7.md:2,6-8,43-45` → `raw/braintree/docs/guides/local-payment-methods/pay-upon-invoice/ios/v7-2026-09-16.md`. The provider index also exposes the exact source directly at `wiki/braintree-index.md:118`. The canonical route is `/braintree/docs/guides/local-payment-methods/pay-upon-invoice/ios/v7` (`raw:6-8`); this is dated website evidence, not exact-SHA package evidence.

## Q2 — Pay Upon Invoice iOS v7 actual behavior/absence — PASS

The complete 19-line raw contains a Pay Upon Invoice heading (`raw:14`) and exactly one substantive availability statement: Pay Upon Invoice is only available for the JavaScript v3 SDK (`raw:17-18`). Therefore this iOS v7 route documents **no iOS integration procedure**—no iOS setup, request fields, lifecycle, eligibility rules, or outcome behavior may be imported from a sibling. The promoted source preserves that boundary and directs implementation research to a separately evaluated JavaScript v3 route (`source:14-25,37-45`). Snapshot scope remains material: it does not prove current availability, account enablement, buyer eligibility, successful execution, or package behavior (`source:16`).

## Q3 — Alipay exact route — PASS

**Object/action match:** locate the unversioned named-method Alipay page and descend to its pinned raw plus the declared supporting currency authority.

**Exact route:** `wiki/index.md:11` → `wiki/braintree-index.md:399` → `wiki/concepts/braintree-payment-methods.md:22` → `wiki/sources/braintree/source-braintree-local-payment-methods-alipay.md:2,6-10,58-61` → `raw/braintree/docs/guides/local-payment-methods/alipay-2026-09-16.md`. The provider index also exposes the exact source directly at `wiki/braintree-index.md:125`. The canonical route is `/braintree/docs/guides/local-payment-methods/alipay` (`raw:6-8`); no platform or SDK version is stated.

## Q4 — Alipay actual restriction/absence — PASS

The complete 26-line primary raw states limited release, buyers only in China, and a Customer Success Manager contact path (`raw:17-21`). Its table states payment type `alipay`; buyers in China; sellers globally except Russia, Brazil, and Mainland China; currency codes `AUD`, `CAD`, `EUR`, `GBP`, `HKD`, `NZD`, `SGD`, `USD`; and `Min: N/A Max: 300,000 CNY` (`raw:23-25`). This is applicability/onboarding information, not an integration flow or merchant approval.

The promoted source correctly preserves the material unresolved currency relationship: the fully read same-snapshot umbrella article says Local Payment Method transactions are automatically presented in Euros (`raw/braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16.md:19-21`), while the Alipay row lists eight currency codes and a CNY-denominated maximum. Neither raw explains presentment versus those codes, conversion, settlement, or per-currency limit behavior, so none is inferred (`source:15,19-22,29-40`). The Alipay page documents no checkout initiation, redirect, client/server flow, SDK/platform/version, environment procedure, settlement, funding, or outcome handling (`source:22`).

## Integrity and bounded gap sweep

- Primary SHA-256 values match the manifest exactly: Pay Upon Invoice iOS v7 `bf18b4e8b4c74e2e1fa0232591a772e67186c540db33653dabe2a2d28dca320b` (`manifest.json:188-194`); Alipay `27198cf3f271f535958503f8a0fb125b8b0872d010bb2536b3266fa7ce2a4d04` (`manifest.json:152-158`).
- Both promoted source files are byte-identical to their approved final candidates (`cmp` exit 0), but all answers above were checked against actual promoted routes and full raw evidence.
- Each primary raw has one `raw_files` reverse owner, its expected promoted source. Each source links `[[braintree-payment-methods]]`, and the concept links back to each source. The Alipay source also declares the umbrella article in both `raw_files` and `Raw Sources`; that supporting raw is intentionally shared by other source pages and is not treated as Alipay's exclusive primary owner.
- Filename/content sweep found the selected Alipay raw, the selected iOS v7 raw, the sibling Android v5 and JavaScript v3 Pay Upon Invoice raws, and the umbrella Euro statement. Only the umbrella article required one additional full read to validate the Alipay conflict. No sibling or older page was fully read or used to fill absent iOS/Alipay behavior.
- No navigation gap, missing reverse link, unresolved locator, or additional material conflict blocks these four answers.

Analysis end: 2026-10-04T02:24:22Z
