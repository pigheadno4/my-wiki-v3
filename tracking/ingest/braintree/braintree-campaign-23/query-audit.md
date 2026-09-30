# Braintree C23 fixed query audit

All five predetermined groups below cover the ten approved pages and 20 fixed questions. Each group used the root → provider index → concept → source → full raw route, with a bounded gap sweep.

# Braintree C23 fixed-query audit — Group A

Date: 2026-09-30
Scope: Marketplace Article Overview + Marketplace Developer-Guide Overview
Repository mode: read-only; report only

## Article Overview route

`wiki/index.md` → `wiki/braintree-index.md` (`Marketplace`) → `wiki/concepts/braintree-marketplace.md` (`Article-level product orientation`) → `wiki/sources/braintree/source-braintree-marketplace-article-overview.md` → `raw/braintree/articles/guides/braintree-marketplace/overview-2026-09-16.md`

1. **Where is Braintree's Marketplace article overview? — PASS**
   - **Object/action match:** Requested the article-level Marketplace overview; the route terminates at the `/articles/guides/braintree-marketplace/overview` source and raw, not the developer guide or a Node operation page.
   - **Direct answer:** It is cataloged as `[[source-braintree-marketplace-article-overview]]`; the exact raw is `raw/braintree/articles/guides/braintree-marketplace/overview-2026-09-16.md`.
   - **Raw locator:** source identity and slug at lines 1 and 5-10; article heading at line 14.

2. **What product orientation and scope does this article itself state? — PASS**
   - **Object/action match:** Requested the article's own product orientation and scope, not setup steps or current-support proof.
   - **Direct answer:** The article frames a marketplace as an owner facilitating purchases from multiple providers and often charging them a service fee. It says Braintree Marketplace can split transactions, route a designated service fee to the master merchant, disburse the balance to the sub-merchant, and begin onboarding from basic contact information while Braintree verifies identity. Its stated scope is restricted to a US-domiciled master merchant and US-domiciled sub-merchants; it is incompatible with PayPal, Braintree recurring billing, and most third-party shopping carts, and every merchant account requires special Braintree approval. New merchants are directed to Sales, so the collected page does not establish current Marketplace availability, eligibility, approval, or successful processing. The unresolved recurring-billing conflict remains: this page says Marketplace is incompatible with Braintree recurring billing, while the collected testing/go-live guide tells applicable integrations to recreate recurring-billing plans or settings in production; do not infer recurring-billing support.
   - **Raw locator:** owner/provider and product model at lines 22-24; Sales/current-entry boundary at lines 17-18 and 30-31; US, incompatibility, and special-approval scope at lines 27-35; master merchant, sub-merchant, service fee, escrow, and webhook terminology at lines 38-45. Conflict counterpart: `raw/braintree/docs/guides/braintree-marketplace/testing-go-live/node-2026-09-16.md`, lines 67-72 and 93-97.

## Developer-Guide Overview route

`wiki/index.md` → `wiki/braintree-index.md` (`Marketplace`) → `wiki/concepts/braintree-marketplace.md` (`Developer-guide orientation`) → `wiki/sources/braintree/source-braintree-marketplace-guide-overview.md` → `raw/braintree/docs/guides/braintree-marketplace/overview-2026-09-16.md`

3. **Where is Braintree's Marketplace developer-guide overview? — PASS**
   - **Object/action match:** Requested the developer-guide overview; the route terminates at the `/docs/guides/braintree-marketplace/overview` source and raw, not the article route or a language-specific task page.
   - **Direct answer:** It is cataloged as `[[source-braintree-marketplace-guide-overview]]`; the exact raw is `raw/braintree/docs/guides/braintree-marketplace/overview-2026-09-16.md`.
   - **Raw locator:** source identity and slug at lines 1 and 5-10; guide heading at line 14.

4. **What purpose and navigation scope does this developer guide itself state? — PASS**
   - **Object/action match:** Requested the guide's own purpose and navigation scope, not the implementation details of its linked Node pages.
   - **Direct answer:** The guide orients a master merchant to the same Marketplace owner/provider, transaction-splitting, service-fee, disbursement, and identity-verification model, then defines the core terms and routes the master merchant to four API feature areas: onboarding sub-merchants, confirming onboarding, creating transactions with service fees, and holding transactions in escrow. It is a navigation overview, not an operation specification. Its own scope requires all parties to be US-domiciled, says Marketplace is incompatible with PayPal, Braintree recurring billing, and most third-party carts, and requires special Braintree approval for all merchant accounts. New merchants are directed to Sales; the page does not prove current support or eligibility. Preserve the same unresolved recurring-billing conflict and do not infer support.
   - **Raw locator:** orientation at lines 20-26; Sales/current-entry boundary at lines 17-18 and 30-31; US, incompatibility, and special-approval scope at lines 33-36; terminology at lines 37-44; four-feature navigation at lines 47-54. Conflict counterpart: `raw/braintree/docs/guides/braintree-marketplace/testing-go-live/node-2026-09-16.md`, lines 67-72 and 93-97.

## Shared checks

- **Complete evidence reads:** Read both selected overview raws in full (46 and 55 lines). Their SHA-256 values match the C23 manifest: article `1ba3b335b3b57c351a78d7820d03813d2825a9b5b5678695adaebae7524ed20e`; guide `8e12708d29d9751c9c7fd0ece491886fb61931bb7790db2f2f2414534757bc26`.
- **Bounded gap sweep:** Searched the Braintree Marketplace article/docs raw subtrees for overview paths plus `recurring billing`, `API features`, and `marketplace solution`. No additional overview snapshot was found. Other Marketplace operation pages were outside these overview questions.
- **Extra full read:** Selected and read `raw/braintree/docs/guides/braintree-marketplace/testing-go-live/node-2026-09-16.md` in full (121 lines) solely to verify the already-routed recurring-billing conflict. Lines 70-72 establish sandbox/production separation including recurring-billing settings; lines 93-97 instruct recreation of recurring-billing plans or settings. This conflicts with both overview raws' incompatibility statement and does not resolve support.
- **Reciprocal/navigation check:** `wiki/braintree-index.md` catalogs both sources and the `[[braintree-marketplace]]` concept; the concept separately routes to both overview sources and carries the conflict warning; each source links back to `[[braintree-marketplace]]` and to its exact raw. The article and developer-guide identities remain distinct throughout.
- **Issues/repairs:** None. All four fixed questions pass; no repository repair or coordinator transition is indicated by this group.

---

# Braintree C23 fixed-query audit — Group B

Scope: Marketplace article onboarding plus Marketplace Node.js onboarding. Both pinned raw pages were read completely. Article claims and Node-guide claims are kept separate; this audit does not infer current Marketplace support or merchant eligibility.

## Route 1 — Marketplace onboarding article

`wiki/index.md:11` → `wiki/braintree-index.md:258` → `wiki/concepts/braintree-marketplace.md:28-30` → `wiki/sources/braintree/source-braintree-marketplace-article-onboarding.md:1-8,52-54` → `raw/braintree/articles/guides/braintree-marketplace/onboarding-2026-09-16.md:1-81`

- **Q1 — Where is Braintree's Marketplace onboarding article? — PASS.** Object/action match: article-level Marketplace sub-merchant onboarding, not the Node.js creation procedure. Direct answer: source page `wiki/sources/braintree/source-braintree-marketplace-article-onboarding.md`; exact raw `raw/braintree/articles/guides/braintree-marketplace/onboarding-2026-09-16.md`; canonical URL `https://developer.paypal.com/braintree/articles/guides/braintree-marketplace/onboarding`. Raw locator: source identity/title at lines 1-14; article body at lines 17-78.
- **Q2 — What onboarding roles and conditions does this article itself state? — PASS.** Object/action match: roles and conditions stated by the article only. Direct answer: the marketplace collects applicant/business information and submits it through the Braintree API (the Control Panel cannot create the sub-merchant); Braintree verifies that information and returns status through a webhook; afterward the marketplace supports its sub-merchants and is responsible for ensuring lawful delivery. Collection depends on Marketplace use and funding destination. The article lists first name, last name, address, DOB (applicant at least 13), email, and SSN or Tax ID, with a full Tax ID for a registered business and otherwise a full nine-digit SSN; business name, mobile phone, routing number, and account number become required under the stated Tax-ID, legacy-Venmo, or bank-disbursement conditions, and a bank destination must be a checking account. Venmo funding is described only for existing Marketplace users and is expressly unavailable as a funding destination for new merchants. Before accepting payments, sub-merchants must accept Braintree's merchant agreements through the marketplace's Terms of Service. New merchants seeking a Marketplace solution are directed to Sales. The separate 1099-K passage is dated “As of January 1, 2022” and is not treated here as current tax guidance. Raw locators: roles/API/webhook/support at line 22; funding-dependent collection and Venmo boundary at lines 25-31; required and conditional data at lines 36-60; merchant agreement at lines 65-67; dated tax passage at lines 70-78.

## Route 2 — Marketplace Node.js onboarding guide

`wiki/index.md:11` → `wiki/braintree-index.md:258` → `wiki/concepts/braintree-marketplace.md:20-26` → `wiki/sources/braintree/source-braintree-marketplace-guide-onboarding-node.md:1-8,55-57` → `raw/braintree/docs/guides/braintree-marketplace/onboarding/node-2026-09-16.md:1-260`

- **Q3 — Where is Braintree's Marketplace Node onboarding guide? — PASS.** Object/action match: Node.js guide for master-merchant creation of a sub-merchant merchant account, not the article-level orientation or confirmation page. Direct answer: source page `wiki/sources/braintree/source-braintree-marketplace-guide-onboarding-node.md`; exact raw `raw/braintree/docs/guides/braintree-marketplace/onboarding/node-2026-09-16.md`; canonical URL `https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/onboarding/node`. Raw locator: source identity/title at lines 1-14; Node onboarding body at lines 17-253.
- **Q4 — What onboarding sequence, conditions and boundaries does this Node guide itself state? — PASS.** Object/action match: sequence, conditions, and boundaries stated by this Node guide only. Direct answer: the master merchant onboards each sub-merchant by (1) gathering the required information, (2) creating a merchant account with `gateway.merchantAccount.create(...)`, and (3) confirming creation through the later status/webhook step. Individual information is always required; `phone` is optional, and a non-registered business requires a full nine-digit SSN. A registered company additionally supplies `business`; `legal_name` and `tax_id` are required, the other displayed business fields are optional, and the account must still be tied to an individual. Bank funding requires `destination = bank`, account and routing numbers for a checking account, and those bank fields must not be sent for another destination; Venmo destinations are unavailable for new merchants. Braintree says it does not verify bank details: a final-disbursement error produces a disbursement-exception webhook and holds funds until correction. `tos_accepted` records acceptance of Braintree's terms through the marketplace website terms. `master_merchant_account_id` nests the account and routes service fees to the master; a sandbox ID must be changed for production. A requested sub-merchant `id` is optional and otherwise generated. Critically, a valid create result can still be `pending`; it is not proof of approval, activation, completed onboarding, funding readiness, or transaction eligibility, and the guide routes the reader to result-status handling plus confirmation webhooks. New merchants seeking Marketplace are directed to Sales. Raw locators: availability and create-then-confirm sequence at lines 17-24; Node create examples at lines 25-115; individual/business conditions at lines 117-149; funding conditions and failure boundary at lines 152-187; terms at lines 190-200; master/environment boundary at lines 201-220; optional ID at lines 223-233; pending result and confirmation route at lines 234-253.

## Shared checks

- **Bounded gap sweep:** searched `raw/braintree/` filenames and content for Marketplace, onboarding, sub-merchant, master merchant, and merchant-account creation. The sweep surfaced adjacent Marketplace overview/create/confirmation/update/testing/funding pages, merchant-account references, the sub-merchant webhook reference, a separate GraphQL account-onboarding page, and Marketplace reconciliation articles. The sources' `Related raw API references` were also inspected. No additional page was selected as evidence: the questions explicitly ask what each named article/guide itself states, both selected raw pages were sufficient, and importing adjacent-page claims would violate the article/Node boundary. Extra full reads: none beyond the two selected raw pages.
- **Reciprocal links:** PASS. `wiki/braintree-index.md:258` links the `braintree-marketplace` concept; the concept links the article at line 30 and the Node guide at line 22; each source links back to `[[braintree-marketplace]]` (`article:43`, `Node:46`). Each source's `raw_files` entry and `## Raw Sources` link resolve to the exact raw used here (`article:7-8,52-54`; `Node:7-8,55-57`). Raw files remain immutable and require no reverse links.
- **Pinned integrity:** PASS. SHA-256 matches C23 manifest: article `782325c7445f521185d07dd523ba049ddc295fa8c5ac3817ab054c0bd38ec6e6`; Node guide `cd09e797c979b95f7a72a873a4a9aa0fa83c8cad93d09a369b678983520e1230`.
- **Issues:** no retrieval failure or wrong-object answer. Material cautions are the dated article tax statement, conditional-required fields presented under an “Optional parameters” heading, and the Node guide's `pending` result/current-availability boundary.

---

# Braintree C23 fixed query audit — Group C

Scope: `marketplace-guide-create-node` and `marketplace-guide-confirmation-node`; four fixed questions from C23 `selection-review.md`. Repository evidence only; both selected raw pages were read in full and their SHA-256 hashes match the manifest.

## Page route: Marketplace Node create

`wiki/index.md` → `wiki/braintree-index.md` (Marketplace) → `wiki/concepts/braintree-marketplace.md` (Marketplace transaction processing) → `wiki/sources/braintree/source-braintree-marketplace-guide-create-node.md` → `raw/braintree/docs/guides/braintree-marketplace/create/node-2026-09-16.md`

- **Q1 — Where is the Marketplace Node create guide? PASS.** Object/action match: Marketplace **Node transaction creation with service fees**, not merchant-account creation or onboarding. The source is `[[source-braintree-marketplace-guide-create-node]]`; its canonical guide is `https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/create/node`, preserved at `raw/braintree/docs/guides/braintree-marketplace/create/node-2026-09-16.md`. Exact raw locator: source URL and slug, lines 1 and 6–9; page identity, line 14.
- **Q2 — What create action and prerequisites does this guide itself state? PASS.** After the master merchant has **successfully onboarded a sub-merchant**, it creates a transaction attributed to that sub-merchant with `gateway.transaction.sale()`. The guide requires selecting the correct `merchantAccountId`, collecting client device data and including it as `deviceData`, and supplying a nonempty `serviceFeeAmount` from zero through the total transaction amount; the example also supplies the amount and payment-method nonce. The fee is deducted from the amount disbursed to the sub-merchant and sent to the master merchant. Exact raw locator: onboarding prerequisite and feature scope, lines 20–24; attribution and device-data prerequisites, lines 27–30; Node call, lines 31–42; service-fee requiredness, range and allocation, lines 43–45. Boundary: the page directs new Marketplace merchants to Sales (lines 17–18); this collected guide is not complete onboarding proof or evidence of current support, transaction success, settlement, or disbursement.

## Page route: Marketplace Node confirmation

`wiki/index.md` → `wiki/braintree-index.md` (Marketplace) → `wiki/concepts/braintree-marketplace.md` (Marketplace onboarding) → `wiki/sources/braintree/source-braintree-marketplace-guide-confirmation-node.md` → `raw/braintree/docs/guides/braintree-marketplace/confirmation/node-2026-09-16.md`

- **Q3 — Where is the Marketplace Node confirmation guide? PASS.** Object/action match: Marketplace **Node post-verification sub-merchant onboarding confirmation**, not account creation or transaction creation. The source is `[[source-braintree-marketplace-guide-confirmation-node]]`; its canonical guide is `https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/confirmation/node`, preserved at `raw/braintree/docs/guides/braintree-marketplace/confirmation/node-2026-09-16.md`. Exact raw locator: source URL and slug, lines 1 and 6–9; page identity, line 14.
- **Q4 — What confirmation step and state boundaries does this guide itself state? PASS.** After third-party verification of the sub-merchant information, the merchant confirms merchant-account creation as **approved or declined via a webhook**; this requires a configured webhook endpoint, and the Node examples parse the webhook POST's `bt_signature` and `bt_payload`. The approved path listens for `SubMerchantAccountApproved` and shows an `active` merchant account; only after confirming successful onboarding does the guide say transactions can start on that account. The declined path listens for `SubMerchantAccountDeclined`, exposes a message and validation errors, and routes the merchant to gather more information and contact Customer Success. Exact raw locator: trigger and webhook prerequisite, lines 20–26; approved event, returned state and transaction boundary, lines 29–43; declined event, errors and follow-up, lines 44–64. Boundary: this page covers the post-verification approved/declined notification step, not account creation, the full verification lifecycle, decision timing, or proof that every onboarding, funding, processing, or current-availability condition is satisfied; the Sales availability notice is at lines 17–18.

## Shared checks

- **Bounded group gap sweep:** inspected the Marketplace guide capsule and filename/content matches for the two requested actions. Adjacent onboarding, overview, testing/go-live, update, merchant-account-create and transaction-sale pages were found, but no extra raw was selected because neither fixed question required cross-page behavior or conflict resolution. **Extra full reads: none.**
- **Reciprocal checks:** `wiki/braintree-index.md` links both sources and `[[braintree-marketplace]]`; each source links the concept; the concept links both sources in the correct onboarding/transaction sections. **PASS.**
- **Separation check:** transaction creation remains conditional on prior successful onboarding; confirmation remains a post-verification webhook step. Neither answer treats either page as complete onboarding proof or as evidence of current Marketplace support. **PASS.**

---

# Braintree C23 fixed query audit — Group D

Repository remained read-only. Both selected raw pages were read in full. No current-support inference is made from the collected snapshots.

## Route 1 — Marketplace processing article

`wiki/index.md` (`[[braintree-index]]`, line 11) → `wiki/braintree-index.md` (Marketplace catalog, line 23) → `wiki/concepts/braintree-marketplace.md` (`## Marketplace transaction processing`, lines 40-42) → `wiki/sources/braintree/source-braintree-marketplace-article-processing.md` → `raw/braintree/articles/guides/braintree-marketplace/processing-2026-09-16.md`.

### Q1. Where is Braintree's Marketplace processing article?

- **Object/action match:** Marketplace article-level transaction processing, not a generic transaction guide or Node operation reference.
- **Answer:** Wiki source `wiki/sources/braintree/source-braintree-marketplace-article-processing.md`; canonical page `https://developer.paypal.com/braintree/articles/guides/braintree-marketplace/processing`; exact raw `raw/braintree/articles/guides/braintree-marketplace/processing-2026-09-16.md`.
- **Raw locator:** source URL and slug at lines 1 and 6-7; `# Processing` at line 14.
- **Verdict:** **PASS**.

### Q2. What processing flow and limits does this article itself state?

- **Object/action match:** Article-level Marketplace fee allocation, escrow, refund and dispute flow; no Node-specific API shape is imported.
- **Answer:** A service fee sends part of a sub-merchant transaction to the master merchant and the remainder to the sub-merchant; if Braintree's transaction fee exceeds the service fee, Braintree first uses settled master-account funds and then debits the master merchant's bank account for the remainder. An escrow hold must be requested through the API at transaction creation or before settlement submission and lasts until an API release. The entire transaction, including the service fee, must be held and released together; partial disbursement requires separate transactions, and Braintree recommends no more than 30 days in escrow. While escrowed, only a full refund is supported and is pulled from escrow; partial refunds become available only after release. Outside escrow, full and partial refunds are available, but refunds are deducted from the master merchant bank account rather than the sub-merchant funding source. Chargebacks/retrievals and their fees are also deducted from the master merchant bank account. The article suggests recoupment through higher/temporary service fees or a vaulted sub-merchant payment method, with ordinary Braintree transaction fees applying to the latter. New merchants are directed to Sales; the snapshot does not establish current Marketplace availability or eligibility.
- **Raw locator:** `## Service fees`, lines 23-31; `## Escrow`, lines 36-46; `## Refunds`, lines 51-55; `## Disputes`, lines 58-60; `## Collecting funds from your sub-merchants`, lines 63-70; availability lines 17-18.
- **Verdict:** **PASS**.

## Route 2 — Marketplace Node update guide

`wiki/index.md` (`[[braintree-index]]`, line 11) → `wiki/braintree-index.md` (Marketplace catalog, line 25) → `wiki/concepts/braintree-marketplace.md` (`## Sub-merchant account maintenance`, lines 32-34) → `wiki/sources/braintree/source-braintree-marketplace-guide-update-node.md` → `raw/braintree/docs/guides/braintree-marketplace/update/node-2026-09-16.md`.

### Q3. Where is the Marketplace Node update guide?

- **Object/action match:** Node.js guide for updating an existing Marketplace sub-merchant, not the generic Merchant Account update reference.
- **Answer:** Wiki source `wiki/sources/braintree/source-braintree-marketplace-guide-update-node.md`; canonical page `https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/update/node`; exact raw `raw/braintree/docs/guides/braintree-marketplace/update/node-2026-09-16.md`.
- **Raw locator:** source URL and slug at lines 1 and 6-7; `# Updating Sub-merchants` at line 14; Node invocation at lines 22-31.
- **Verdict:** **PASS**.

### Q4. What update action, prerequisites and limitations does this guide itself state?

- **Object/action match:** Updating an existing Marketplace sub-merchant with the Node SDK; no account-creation or disbursement-success claim is imported.
- **Answer:** Call `gateway.merchantAccount.update()` with the existing merchant account ID and only the attributes being changed; omitted attributes remain unchanged, and a missing account routes to `notFoundError`. The guide groups changes under `individual`, `business`, and `funding`. Every sub-merchant must have individual details. Business details are optional additional details for a registered business and do not replace the always-required individual details. Funding details control where Braintree will disburse settled funds. After successful updates, only the last four digits of SSNs and bank account numbers are returned. New merchants are directed to Sales. The guide does not establish current availability or eligibility, and its success examples do not themselves prove later validation, processing, or disbursement.
- **Raw locator:** required ID, changed attributes and unchanged omissions at lines 20-21; Node call at lines 22-31; missing-account and three attribute groups at lines 33-38; individual requirement and masking at lines 41-69; registered-business qualification and optional/in-addition condition at lines 70-93; funding purpose and masking at lines 94-115; availability lines 17-18.
- **Verdict:** **PASS**.

## Group D bounded gap sweep

- Searched `raw/braintree/` once for Marketplace processing/update identity and the decisive phrases around `merchantAccount.update`, omitted attributes, service fees, escrow and partial refunds. Results preserved the article-versus-Node authority split; unrelated regional pricing, generic refund and validation-error pages were not selected as evidence.
- **Single extra full read:** `raw/braintree/docs/reference/request/merchant-account/update/node-2026-09-16.md` (lines 1-40). It confirms the generic Node example `gateway.merchantAccount.update("blue_ladder_store", merchantAccountParams, ...)`, `result.success`, the missing-account `notFoundError` route, and a link to the sub-merchant guide (lines 13-40). It does not state the Marketplace guide's omitted-field rule, registered-business condition, always-required individual details, funding meaning, or sensitive-output limits, so it did not replace or broaden the selected guide's answer.
- **Reciprocal checks:** `wiki/braintree-index.md` links both selected sources (lines 23 and 25); `wiki/concepts/braintree-marketplace.md` links them in purpose-matched sections (lines 34 and 42); each source links back to `[[braintree-marketplace]]` (processing source line 38; update source line 40). **PASS**.

## Issues

None. All four fixed questions pass retrieval, object/action identity, raw-detail, and reciprocal-route checks.

---

# Braintree C23 fixed query audit — Group E

## Page route: Marketplace funding article

`wiki/index.md:11` → `wiki/braintree-index.md:258` → `wiki/concepts/braintree-marketplace.md:48-50` → `wiki/sources/braintree/source-braintree-marketplace-article-funding.md` → `raw/braintree/articles/guides/braintree-marketplace/funding-2026-09-16.md`

- **Q1 — Where is Braintree's Marketplace funding article?** Object/action match: **Marketplace article-level funding route**, not generic settlement funding or proof of a bank deposit. **Answer:** the collected article is the source page `[[source-braintree-marketplace-article-funding]]`; its canonical URL is `https://developer.paypal.com/braintree/articles/guides/braintree-marketplace/funding`, and its exact pinned raw is `raw/braintree/articles/guides/braintree-marketplace/funding-2026-09-16.md`. Raw locator: URL/title at lines 1 and 5-14. **PASS**.
- **Q2 — What funding flow and qualifications does this article itself state?** Object/action match: **post-settlement Marketplace disbursement flow and its stated qualifications**, not a generic funding timeline. **Answer:** new merchants seeking a marketplace solution are sent to Sales. After a gateway transaction settles, funds should reach the master merchant's bank account and the sub-merchant's funding source within 1–3 business days unless held in escrow, with at most one deposit per party per day. Escrow holds and releases the whole transaction, service fee included; partial disbursement requires separate transactions. The bank route uses onboarding details and accepts checking accounts only. Venmo funding destinations are unavailable to new merchants; in the described legacy flow, an unmatched recipient has 30 days to create an account, and failure to act produces no disbursement-exception webhook, so manual follow-up is required. Disbursement-exception webhooks notify only failures, because banks and Venmo do not confirm success; expected timing, descriptors, or absence of an exception therefore do **not** prove an individual deposit arrived. Raw locator: availability at lines 17-18; timing/daily maximum at 23-31; escrow/partial-disbursement rule at 34-38; checking-account route at 43-57; Venmo qualification and manual-follow-up exception at 60-74; failure-only webhook boundary at 88-99. **PASS**.

## Page route: Marketplace Node testing and go-live guide

`wiki/index.md:11` → `wiki/braintree-index.md:258` → `wiki/concepts/braintree-marketplace.md:36-38` → `wiki/sources/braintree/source-braintree-marketplace-guide-testing-go-live-node.md` → `raw/braintree/docs/guides/braintree-marketplace/testing-go-live/node-2026-09-16.md`

- **Q3 — Where is the Marketplace Node testing and go-live guide?** Object/action match: **Marketplace Node testing/go-live guide**, not another payment method's testing guide. **Answer:** the collected guide is the source page `[[source-braintree-marketplace-guide-testing-go-live-node]]`; its canonical URL is `https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/testing-go-live/node`, and its exact pinned raw is `raw/braintree/docs/guides/braintree-marketplace/testing-go-live/node-2026-09-16.md`. Raw locator: URL/title at lines 1 and 5-17. **PASS**.
- **Q4 — What testing and launch boundaries does this guide itself state?** Object/action match: **sandbox simulation and production transition/testing boundaries**, not proof of production approval or current Marketplace eligibility. **Answer:** in sandbox, the sub-merchant first-name input can simulate approval or decline confirmation webhooks, with the decline webhook returning the supplied error; the guide also supplies sandbox routing numbers that pass its checksum requirement. Sandbox and production are entirely separate: objects, processing options, recurring-billing settings, login, merchant ID, and API keys do not transfer. For launch, it recommends a dedicated non-employee API user with Account Admin permission, requires production merchant ID/public/private keys in server-side code, recreation of applicable production settings, and a Node switch to `braintree.Environment.Production`; the client needs no separate change because it gets its client token from the server. It then calls for only a couple of low-value production sales per intended payment-method type, submitted for settlement and followed through to bank deposit. Those checks require real payment methods; settled transactions debit them and incur fees, so amounts and test count must be limited. This procedure is not production-acceptance proof. Its direction to recreate recurring-billing plans/settings remains in unresolved conflict with the recurring-billing overview's explicit statement that recurring billing is incompatible with Marketplace; do not infer Marketplace recurring-billing support. Raw locator: sandbox webhook simulations at lines 17-58; sandbox routing-number values at 59-64; environment isolation at 67-71; production API user and credentials at 74-92; settings recreation at 93-97; Node server switch/client-token boundary at 98-113; real-payment production checks, debits, and fees at 114-120. Conflict evidence: `raw/braintree/docs/guides/recurring-billing/overview-2026-09-16.md:14-19`. **PASS with unresolved cross-page conflict preserved**.

## Shared checks

- Both selected raw pages were read in full. Their SHA-256 values match the C23 manifest: funding `b424113be6033b396d3a8e62eb4c58eee088c9601a177a9e7dbd5134e606ab4a`; testing/go-live `1b65270d7c173202ded1ca183e197638634b3585b43869655cd576e6ba7535d4`.
- One bounded group gap sweep covered Marketplace/funding/testing-go-live filenames and the material phrases for disbursement exceptions, manual follow-up, production testing, sandbox isolation, and recurring-billing/Marketplace compatibility. Generic processor funding timelines and other products' testing guides were adjacent but not needed. No older snapshot of either selected canonical page was found.
- Extra full read: `raw/braintree/docs/guides/recurring-billing/overview-2026-09-16.md`, selected solely to verify the material recurring-billing conflict; line 17 says Braintree recurring billing is not compatible with Braintree Marketplace. No other extra raw was selected.
- Reciprocal checks: `wiki/braintree-index.md:24,26,258` catalogs both sources and the Marketplace concept; the concept links the funding source at line 50 and the testing/go-live source at line 38; each source links back to `[[braintree-marketplace]]` and to its exact raw. The recurring-billing conflict is reciprocal between the testing/go-live and recurring-billing source pages. **PASS**.
- Repairs: none. Material issue retained: the recurring-billing conflict is unresolved; the selected docs must not be used to infer support. Repository files were not changed.
