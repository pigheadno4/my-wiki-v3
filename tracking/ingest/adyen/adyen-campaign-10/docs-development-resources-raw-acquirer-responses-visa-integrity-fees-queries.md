# Fixed retrieval checks: Visa system integrity fee categories

## Q1 — Purpose, setup and dated fee scope

**Query:** What is this Adyen Visa raw-response mapping for, what setup does it require, and does it establish current Visa fee liability?

**Expected answer:** The 2026-09-15 webpage snapshot is a guide for merchant-built online retry logic to map failed Visa transaction raw responses to Visa system integrity fee categories. It describes excessive-retry and data-quality fee types, requires an online-payments integration, and says to enable raw responses in Customer Area. `refusalCodeRaw` is available only for Visa and Mastercard transactions through Adyen's own acquiring platform; `refusalReasonRaw` holds the full raw response. This source does not establish current fee amounts, regional applicability, merchant-specific liability, or a live scheme rule.

**Raw locators:** purpose and fee types, lines 15–21 and 30–37; requirements, lines 23–28; raw response fields, lines 59–66. **Canonical retrieval route:** [[adyen-online-payments]] → [[source-adyen-docs-development-resources-raw-acquirer-responses-visa-integrity-fees]] → [[raw/adyen/docs/development-resources/raw-acquirer-responses/visa-integrity-fees/2026-09-15|pinned raw]].

## Q2 — Retry categories and code 14 conflict

**Query:** What retry guidance does this snapshot give for Visa categories 1–4, and can raw code `14` be assigned one retry instruction from this page?

**Expected answer:** Category 1 says do not retry; categories 2, 3 and 4 state up to 15 retries in 30 days. Category 3 concerns incorrect payment details and the page also discusses a data-quality fee. The table places raw code `14` in category 1 with no retry and in category 3 with maximum 15 in 30 days. That conflict prevents one reliable instruction for code `14` from this snapshot. The dated statements are not a current Visa retry policy; inspect current authoritative rules before operational decisions.

**Raw locators:** category definitions and retry text, lines 39–57; code `14` category 1 row, line 74; code `14` category 3 row, line 100; category 4 catch-all, lines 107–108. **Canonical retrieval route:** [[adyen-online-payments]] → [[source-adyen-docs-development-resources-raw-acquirer-responses-visa-integrity-fees]] → [[raw/adyen/docs/development-resources/raw-acquirer-responses/visa-integrity-fees/2026-09-15|pinned raw]].
