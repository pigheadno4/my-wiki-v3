# docs-plugins-adobe-commerce-supported-payment-methods fixed queries

## Q1 — Purpose, scope, and what not to infer

**Question:** What does this Adyen Adobe Commerce page establish about payment-method support?

**Answer:** The 2026-09-15 capture, with 2024 last-modified metadata, lists methods and countries/regions against **Standard** and **Headless** plugin columns, with check and X marks (raw lines 15–21, 40–187). The page calls this the “latest version” but names no exact plugin release, so its matrix must not be presented as the supported methods of a particular installed version. A check mark indicates this documentation's plugin/integration row, not a merchant's enabled method, current account or country eligibility, currency eligibility or a successful payment. Merchant-account method request is a separate Customer Area step (lines 25–38). The country/region column does not define a currency table or clarify every country applicability dimension. Canonical route: [[source-adyen-docs-plugins-adobe-commerce-supported-payment-methods]] → [[adyen-magento2]]; evidence: [[raw/adyen/docs/plugins/adobe-commerce/supported-payment-methods/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Question:** How should a merchant read a method row and its special conditions before offering it?

**Answer:** Read the exact method, country/region, Standard and Headless cells, including X rows, in the raw matrix; the categories are cards, cash/ATM, direct debit, online banking, BNPL, prepaid/gift cards and wallets (raw lines 40–187). The merchant can inspect and submit method requests under its merchant account in test or live Customer Area, with prompted information where applicable (lines 25–38); a submitted request is not proof of activation. Trustly lists DK, FI, NO, SE and “more,” with a Support route for other European countries/regions (lines 119–122). The Apple Pay, Google Pay and PayPal **Express** rows require the separate express checkout module (lines 159–179, 189). This page provides no method-specific recurring, refund or partial-payment capabilities or currency limits, and its unpinned “latest version” wording must stay separate from the exact-version [[source-github-adyen-magento2]] route. Canonical route: [[source-adyen-docs-plugins-adobe-commerce-supported-payment-methods]] → [[adyen-magento2]]; evidence: [[raw/adyen/docs/plugins/adobe-commerce/supported-payment-methods/2026-09-15]] lines 19–38, 40–189.
