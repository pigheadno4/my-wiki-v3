# Fixed retrieval checks: Classic Google Pay

## Q1 — Purpose and scope

**Query:** What does the Adyen Classic Google Pay page cover, and is it a new Checkout API integration guide?

**Expected answer:** It is a dated Google Pay guide for an existing Classic `/authorise` online integration on Android or web. The endpoint is inactive and unsupported for new integrations; Adyen directs new builds and migrations to Checkout API routes. It is not evidence of current Google SDK behavior, present merchant eligibility, or an approved payment; metadata says last modified in 2019.

**Raw locators:** `# Google Pay (classic)`, lines 14–23; `## Step 1: Integrate the Google Pay SDK`, lines 25–45. **Canonical retrieval route:** [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-classic-google-pay]] → [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/classic-google-pay/2026-09-15|pinned raw]].

## Q2 — Client/server token, merchant ID and live boundary

**Query:** Where does the Google Pay token go in the Classic flow, and what distinct account or live setup is described?

**Expected answer:** The Google API request sample sets `allowedPaymentMethods` to CARD and TOKENIZED_CARD and uses payment-gateway tokenization with gateway `adyen`; its `gatewayMerchantId` sample is the Adyen MerchantAccount or CompanyAccount name. After the merchant server receives the Google Pay token, it posts Classic `/authorise` with that token in `additionalData.googlepay.token`, alongside illustrative amount, merchant reference and merchant account. Before live use, integration/testing alone is insufficient: the page requires a Google Pay request in live Customer Area and merchant-ID configuration for that payment method. The page shows no authorization response, capture or webhook confirmation; do not infer payment success from token receipt or request submission.

**Raw locators:** `## Step 1`, lines 25–45; `## Step 2`, lines 47–67; `## Step 3`, lines 69–71. **Canonical retrieval route:** [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-classic-google-pay]] → [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/classic-google-pay/2026-09-15|pinned raw]].
