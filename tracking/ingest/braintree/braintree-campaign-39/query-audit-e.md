# Braintree Campaign 39 query audit — group E

- Provider/job/object/action: `braintree` / `braintree-campaign-39` / manifest positions 17–20 / read-only fixed-query audit.
- Manifest: `/Users/tengtao/Development/wiki-v2/tracking/ingest/braintree/braintree-campaign-39/manifest.json`.
- Analysis end UTC: `2026-10-04T15:02:48Z`.
- Handoff UTC: `2026-10-04T15:02:48Z`.

## Shared checks — PASS

- Read `CLAUDE.md`, `rules/query-and-synthesis.md`, the full selection review, and the exact full manifest. Verified the provider, campaign, four exact job IDs, source targets, canonical URLs, and requested query action.
- The four pinned raw SHA-256 values match the manifest: `94555dd48ce4c55d18aa2e9d958867d656af6a546601c46fb005c7521eb0f484`, `34531aed25c97bba8e909f079367517e9ac6b3b5c108e5ab7806cc72bca5843b`, `5fc07e766caf9960ef30526cbafa804d0316718df9c4fd09aa9db50d367586f3`, and `326c8f15658c1fbda951983d0da7a5ee0bc102a620563d7e8811eb341e6af39d`.
- Read `wiki/index.md` and `wiki/braintree-index.md` fully; each assigned source has one Braintree-index entry, one primary concept route, one unique source owner for its raw file, and a reciprocal Raw Sources link. Aggregate catalog work was not required.
- Read each assigned source and pinned raw file fully. Also read the two used concepts fully. The bounded filename/related-reference sweep found the underwriting overview and processor/account-specific sibling settlement/change pages; none was needed to answer these source-local questions, and no sibling scope or values were imported. The NAB settlement raw was separately assigned and fully read, so its link from the bank-change source was not treated as unread evidence.
- Existing qualifications were preserved without claiming that no conflicts exist. No repository file, campaign state, transition, catalog, commit, or push was changed.

## 17. `articles-risk-and-security-underwriting-periodic-reviews` — PASS

Route/page: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-platform]]` → `[[source-braintree-articles-risk-and-security-underwriting-periodic-reviews]]` → `raw/braintree/articles/risk-and-security/underwriting/periodic-reviews-2026-09-16.md`.

1. Scope: a Braintree article, fetched `2026-09-16` (page metadata updated `2025-04-01`), describing Braintree in its stated role as the merchant-account provider performing periodic underwriting/risk reviews after onboarding. It states no processor, payment method, region, currency, or jurisdiction and is not proof of an account review, approval, funding decision, or current universal/legal rule. Raw: frontmatter lines 1–10; identity/purpose line 16.
2. Purpose/action and limits: refresh business-model, billing, volume, and financial-health information; cadence may be quarterly, semi-annual, or annual according to business risk. Underwriting may request financial statements, business-model confirmation, and growth expectations. Reply with attachments or use the secure Control Panel upload; respond within the requested time, with the important notice asking for documents within two weeks. Silence after significant time may cause a funding hold; inability to supply the exact documents should be disclosed so alternatives can be assessed. Possible held funds, reserve, or termination are risk rationale, not predicted outcomes. Raw locators: purpose `# Periodic Reviews`, line 16; consequences `## Why periodic reviews are necessary`, line 21; timing/cadence/materials lines 27–39; delivery and two-week/hold/alternative-document conditions lines 42–52.

## 18. `articles-nab-transactions-settlement-funding-timeline` — PASS

Route/page: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-platform]]` → `[[source-braintree-articles-nab-transactions-settlement-funding-timeline]]` → `raw/braintree/articles/nab/transactions/settlement-funding-timeline-2026-09-16.md`.

1. Scope: a Braintree-hosted NAB account/processor-route snapshot fetched `2026-09-16` (page metadata updated `2025-04-01`). It covers credit cards, Amex-funded Apple Pay/Google Pay, and separately managed PayPal disbursement. The NAB overview only establishes that a portal recipient has at least one NAB-**funded** merchant account; it does not establish NAB provisioning, a region, currency, every-account equivalence, or independent current NAB/Amex/PayPal policy. Raw: timeline frontmatter lines 1–10 and method sections lines 19–46; NAB recipient condition is confined to NAB overview raw lines 17–18.
2. Purpose/action and limits: card transactions enter batches with a fixed `9:55pm AET` account cutoff; after processor confirmation of successful settlement, funds are ready for disbursement. If the business bank account is also with NAB, the page says funds should be deposited `1–3` business days after submission for settlement for Visa/Mastercard and `2–8` for Amex; another bank may add delay, and Amex controls its own cutoff/disbursement. Thus submission, settlement confirmation, readiness for disbursement, disbursement handling, and bank arrival are not interchangeable or guaranteed. Amex-funded Apple Pay/Google Pay follows regular Amex handling; PayPal disbursement is separate. Card verification uses `$1`; `$0` triggers `91741`. Raw locators: lifecycle/cutoff lines 16 and 21–23; schedules/qualifications lines 26–31; verification lines 34–36; wallets lines 39–41; PayPal lines 44–46.

## 19. `articles-nab-change-your-bank-account` — PASS

Route/page: `[[index]]` → `[[braintree-index]]` → `[[braintree-control-panel]]` → `[[source-braintree-articles-nab-change-your-bank-account]]` → `raw/braintree/articles/nab/change-your-bank-account-2026-09-16.md`.

1. Scope: a Braintree-hosted NAB-path snapshot fetched `2026-09-16` (page metadata updated `2025-04-02`) for requesting replacement of the business checking account supplied in the original Braintree application. The submitted account must be an Australia-based business checking account. This does not infer NAB provisioning, settlement currency, sibling-account policy, request acceptance, approval, completed change, or payout/bank-arrival proof. Raw: frontmatter lines 1–10; original-account context line 16; account condition lines 49–50.
2. Purpose/action and limits: upload either a bank statement or signed bank letter for the new account through the Control Panel Business Uploads Tool. Online-banking screenshots are rejected. A statement needs the DBA/legal name, BSB and account number, business address, and a clearly stated issue date within three months. A letter needs bank letterhead, the same account/business details, a bank-representative signature, and a clearly stated issue date within six months. Savings, deposit-only, and prepaid-debit accounts are rejected. This is a document-upload request route, not completion evidence. Raw locators: payout context/action lines 16–18; screenshot warning lines 21–22; statement values lines 29–35; letter values lines 38–46; eligible/excluded account types lines 49–50.

## 20. `articles-nab-overview` — PASS

Route/page: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-platform]]` → `[[source-braintree-articles-nab-overview]]` → `raw/braintree/articles/nab/overview-2026-09-16.md`.

1. Scope: a Braintree-hosted, direct-link-only portal snapshot fetched `2026-09-16` (page metadata updated `2025-04-01`) for a recipient with at least one merchant account **funded by NAB**. It does not say NAB provisioned the account, apply to every merchant account, identify a region or currency, establish current independent NAB policy, or prove linked-page behavior or an individual processing/funding outcome. Raw: frontmatter lines 1–10; exact recipient condition lines 17–18.
2. Purpose/action and limits: the portal routes merchants to account-tailored articles because banking partner can affect accepted payment types and other processing details that generic public articles may omit. Business-bank relationship may change timelines; no timeline values appear here, so the exact destination page must be read. Bookmarking is recommended because the articles are unavailable through support-site search. Partner bank depends mostly on signup timing and business domicile, and multiple merchant accounts may have different partner banks. Raw locators: bank/timeline qualification line 22; portal/search limit line 24; bookmark line 26; processing and partner-bank variability line 28.

## Blockers / approval

- Blockers: none; no material retrieval defect for positions 17–20.
- Approval result: **PASS** for all eight fixed answers in group E. This is audit evidence only; it does not authorize a campaign transition, repository write, commit, or push.
