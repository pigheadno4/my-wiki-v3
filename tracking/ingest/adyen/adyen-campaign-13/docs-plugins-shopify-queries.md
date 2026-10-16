# Fixed retrieval checks — Adyen Shopify payments apps

## Q1 — Purpose, scope, and non-inference

**Question:** What does the Shopify guide cover, and what should its setup and test examples not be taken to prove?

**Expected answer:** It covers setup, activation, testing, and live-account transition for separate Adyen Payments - Credit Cards and Adyen - Alternative Payments Shopify apps. It supplies no app/package version, universal country/currency method matrix, capture/order lifecycle, or live payment proof. A payment-method request in Customer Area, test-mode card fixture, or app activation does not establish live account approval, method enablement, a successful order, or financial outcome.

**Raw locators:** Introduction lines 15–23; `Requirements` and `Step 1` lines 25–49; `Test your integration` lines 118–193; `Go live` lines 195–219.

**Canonical wiki route:** [[adyen-index]] → [[adyen-shopify]] → [[source-adyen-docs-plugins-shopify]] (Shopify concept/index route proposed for coordinator creation).

## Q2 — Central capability, prerequisites, and warnings

**Question:** What conditions govern app setup, method configuration, region selection, test mode, and go-live migration?

**Expected answer:** Shopify Checkout Extensibility is required. The Credit Cards app is installed/configured first; Alternative Payments setup depends on it and syncs Customer Area-enabled methods. Connection uses Authorize with Adyen and Customer Area Grant access. Only one merchant account per region can be selected; selecting multiple errors and requires re-authentication. Apple Pay and Google Pay are exempted by this guide from Adyen Customer Area enablement, while other methods require setup there. Test mode is for test transactions; the page recommends tests including 3DS2 and failure triggers, and its Incorrect CVC row unusually uses `INVALID_CARD_NUMBER`. Live use requires an approved live account and separate configuration/payment-method requests because test settings do not copy; the prescribed switch disconnects the test account and connects/activates live, then repeats testing. No live payment outcome follows automatically.

**Raw locators:** `Requirements` lines 25–32; setup lines 34–116, especially 68–75, 87–92 and 96–116; test lines 118–153; `Go live` lines 195–219.

**Canonical wiki route:** [[adyen-index]] → [[adyen-shopify]] → [[source-adyen-docs-plugins-shopify]] → [[raw/adyen/docs/plugins/shopify/2026-09-15|pinned raw snapshot]].
