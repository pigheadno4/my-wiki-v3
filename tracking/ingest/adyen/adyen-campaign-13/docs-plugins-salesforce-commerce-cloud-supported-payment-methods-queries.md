# Fixed retrieval checks — Adyen SFCC supported payment methods

## Q1 — Purpose, scope, and non-inference

**Question:** What does this table establish for SFRA and Composable Storefront, and what does it not establish for a merchant or SiteGenesis?

**Expected answer:** The table lists payment-method compatibility and the starting version for each of two storefront types, SFRA and Composable Storefront. It has no SiteGenesis column, so it should not be treated as a SiteGenesis support matrix. A check mark and version do not prove a merchant account has the method enabled, that a country/currency and feature combination is eligible, or that a live order/payment succeeded. The page routes SFRA to the Web Components-filtered method overview and Composable to the Web Drop-in-filtered overview for country/region and feature detail.

**Raw locators:** Intro lines 17–26; `Add payment methods to your account` lines 28–41; category table headings and rows lines 43–202.

**Canonical wiki route:** [[adyen-index]] → [[adyen-salesforce-commerce-cloud]] → [[source-adyen-docs-plugins-salesforce-commerce-cloud-supported-payment-methods]].

## Q2 — Central capability, prerequisites, and warnings

**Question:** How should a reader use the version columns and merchant-account request step for a specific method?

**Expected answer:** Select the correct storefront column and method row, then compare its listed starting version and support flag. SFRA and Composable thresholds differ: for example iDEAL is SFRA `24.3.0+` and Composable `2.0.0+`; BACS Direct Debit is SFRA `21.1.0+` and marked unsupported for Composable. A merchant can request methods in its test or live Customer Area, but submission is not enablement. Consult the linked storefront-specific method overview for country/region and feature conditions. Apple Pay Express has a separate product-detail-page note giving v25.1.0 or later. That number aligns with SFRA versioning, but the note itself does not explicitly label a storefront; do not apply it to Composable or infer Composable PDP support. The raw's 2025-08-04 last-modified metadata predates SFRA V26.1.0+/V26.2.0+ rows, while the separately retained SFCC overview places V26 in January 2026; preserve the captured table without inferring an exact update date. No capture/order/refund or settlement guarantee follows from this matrix.

**Raw locators:** Frontmatter last-modified line 11; intro lines 19–24; account-request lines 28–41; BACS line 90; iDEAL line 103; SFRA V26 rows lines 105 and 202; Apple Pay/Express lines 160–163 and note line 193. The related [[source-adyen-docs-plugins-salesforce-commerce-cloud]] overview places SFRA V26 in January 2026.

**Canonical wiki route:** [[adyen-index]] → [[adyen-salesforce-commerce-cloud]] → [[source-adyen-docs-plugins-salesforce-commerce-cloud-supported-payment-methods]] → [[raw/adyen/docs/plugins/salesforce-commerce-cloud/supported-payment-methods/2026-09-15|pinned raw snapshot]].
