# C37 fixed query audit C

Analysis end (UTC): 2026-10-04T07:42:16Z
Handoff (UTC): 2026-10-04T07:43:32Z

## 9. APAC accepted payment methods

Route: `wiki/index.md:11` -> `wiki/braintree-index.md:553` -> `wiki/concepts/braintree-payment-methods.md:25` -> `wiki/sources/braintree/source-braintree-articles-apac-transactions-accepted-payment-methods.md:44,57-59` -> `raw/braintree/articles/apac/transactions/accepted-payment-methods-2026-09-16.md`; SHA-256 `4cac0a51b28f25c43747c69bd5820b612f578e68df6f0ce7d39b0d68545a1fb1` matches the C37 manifest.

- Q1 — **PASS:** This is a 2026-09-16 Braintree-hosted APAC-path account article, not region-wide policy and with no processor named. Visa and Mastercard are default; direct Amex is limited to merchants domiciled in Hong Kong or Singapore, requires a separate Amex account, and makes Amex responsible for funding, descriptors, chargebacks, and support. Pricing scope is only a Braintree per-transaction fee plus Amex-assessed processing fees, with gateway enablement conditioned on Amex pricing in the original agreement or a signed separate form; no numeric or merchant-specific price is supplied. Raw: card/account scope `17-36`, fees `39-41`, pricing/setup `44-50`.
- Q2 — **PASS:** The page routes acceptance/configuration: direct Amex application plus currency-matched SE numbers; modal PayPal credential linking and eligible-device Apple Pay/Google Pay enablement; SRC limited-release wording; and an additional merchant account plus merchant-account-ID integration update for direct charging in another supported currency. It warns that customer-bank conversion can add fees and complicate refunds/increase chargebacks, and that SRC support remains unresolved rather than proven current. Raw: Amex prerequisites `34-50`, alternative methods `55-75`, currency/conversion/actions `78-84`. SRC conflict locators are recorded once under shared checks.

## 10. AU transaction descriptors

Route: `wiki/index.md:11` -> `wiki/braintree-index.md:559` -> `wiki/concepts/braintree-control-panel.md:21` -> `wiki/sources/braintree/source-braintree-articles-au-transactions-descriptors.md:39,42-44` -> `raw/braintree/articles/au/transactions/descriptors-2026-09-16.md`; SHA-256 `3cf06e70fea598e903acfa90b7b4c9eb558d8b1faccf0b7670b2443b072631e1` matches the C37 manifest.

- Q1 — **PASS:** This is the collected Braintree AU-path article for the addressed account's soft, hard, and per-transaction dynamic statement descriptors. It names no processor, current account assignment, method eligibility, or pricing. The customer's bank controls final rendering; PayPal descriptor changes use the PayPal console rather than the Braintree hard-descriptor contact route. Raw: purpose/example/account scope `14-25`, required fields and configuration route `27-37`.
- Q2 — **PASS:** Soft appears after authorization while pending, hard after settlement/bank finalization, and dynamic is passed per transaction via API. Hard/soft merchant name is limited to 22 alphanumeric characters with periods/spaces; the location subsection says city 13 and state 2 alphanumeric characters with no special characters, while the earlier requirement says city and country—the source correctly leaves that tension unresolved. Refunds default to the original dynamic descriptor; dynamic values are business-name-only, have the listed character rules, require an asterisk for Amex Direct, and must match the registered trading name. Raw: lifecycle/action `20-25`, country/state tension and limits `27-57`, refund/dynamic rules `60-78`.

## 11. AIB AF authorizations

Route: `wiki/index.md:11` -> `wiki/braintree-index.md:552` -> `wiki/concepts/braintree-payment-platform.md:34` -> `wiki/sources/braintree/source-braintree-articles-aib-af-transactions-authorizations.md:41,45-47` -> `raw/braintree/articles/aib-af/transactions/authorizations-2026-09-16.md`; SHA-256 `aa7ffa2b765ea3b25e8024f95968f3dd8bf82d69dcb05c9c6bd96ece0695b350` matches the C37 manifest.

- Q1 — **PASS:** This is the exact 2026-09-16 Braintree-hosted AIB AF authorization article. It does not define AF, state a region or pricing model, establish current account eligibility, or serve as independent current bank policy; no pricing is documented. It must not be used as AIB BF evidence. Raw identity/slug `1-9`; authorization scope `14-20`.
- Q2 — **PASS:** `Authorized` is a bank hold; debit and routing to the merchant account are conditional on later settlement submission, not proof of settlement or funding. Unsubmitted holds expire on card-type-dependent timing. Voids are typically limited to `Authorized` or `Submitted for Settlement`; an Authorized void says release should occur in 24–48 hours, while an automatic-submission or already-submitted void can leave the hold until expiry. A gateway rejection can occur after authorization and triggers a void, but release may still await expiry. Raw: authorization/expiry `14-20`, void prerequisites and limitations `23-32`, gateway rejection `35-39`.

## 12. AIB BF authorizations

Route: `wiki/index.md:11` -> `wiki/braintree-index.md:552` -> `wiki/concepts/braintree-payment-platform.md:35` -> `wiki/sources/braintree/source-braintree-articles-aib-bf-transactions-authorizations.md:46,48-50` -> `raw/braintree/articles/aib-bf/transactions/authorizations-2026-09-16.md`; SHA-256 `4fecb47ae9feb272223da36ce521c2d9ab6d8c9c0ae9f7089a838c093b6dda14` matches the C37 manifest.

- Q1 — **PASS:** This is the exact 2026-09-16 Braintree-hosted AIB BF authorization article. It does not define BF, state a region or pricing model, establish current account eligibility, or serve as independent current bank policy; no pricing is documented. It must not be used as AIB AF evidence. Raw identity/slug `1-9`; authorization scope `14-20`.
- Q2 — **PASS:** `Authorized` is a bank hold and later debit/merchant-account routing depends on settlement submission; authorization alone is not settlement, disbursement, funding, or deposit proof. Unsubmitted authorizations expire by card-type-dependent timing. Voids are typically status-qualified; automatic submission delays void eligibility until `Submitted for Settlement`, whose void does not automatically release the original hold. Gateway rejection may follow authorization and then void it, with bank-side release still qualified. Raw: authorization/expiry `14-20`, void prerequisites and limitations `23-32`, gateway rejection `35-39`.

## Shared checks and extra reads

- **PASS:** All four root -> provider index -> main concept -> source -> raw links resolve; each source names its main concept, each concept links back to the source, each source frontmatter/Raw Sources route matches the manifest raw path, and all four computed hashes match the pinned values. The provider index also lists the four canonical sources at lines `33-36`; exhaustive catalog work was deferred as instructed.
- **PASS:** The only conflict-driven extra full reads were `source-braintree-get-started-payment-methods.md` plus raw `articles/get-started/payment-methods-2026-09-16.md`, and `source-braintree-payment-methods-secure-remote-commerce.md` plus raw `articles/guides/payment-methods/secure-remote-commerce-2026-09-16.md`. Both preserve the same unresolved SRC/Click to Pay tension: end-of-support/error wording at raw `14-15` conflicts with current-tense limited-release wording at getting-started raw `87-89` and dedicated-guide raw `21-48,88-90`. No current-support conclusion was inferred.
- **PASS:** Filename/topic gap sweep found sibling regional/account variants, but none was needed to answer these exact objects/actions beyond the SRC conflict. AU country/state terminology remains unresolved; AF and BF stay separate authorities; authorization was not conflated with settlement, disbursement, funding, or bank arrival.

Result: **8/8 PASS; no material failure.**
