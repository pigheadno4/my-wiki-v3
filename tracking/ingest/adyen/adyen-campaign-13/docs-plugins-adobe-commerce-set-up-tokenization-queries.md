# Fixed retrieval checks — Adyen Adobe Commerce tokenization

## Q1 — Purpose, scope, and non-inference

**Question:** What does this page set up, and what does a saved Vault token not establish?

**Expected answer:** It describes Adobe Commerce plugin tokenization for listed payment methods, with a shopper-facing `Save for my next payment` checkbox and Adobe Commerce Vault storage of token information. The page has no exact plugin-version statement. A configured method or stored token does not itself prove the shopper authorized a later charge, that the credential may be reused under another recurring model/identity, or that a later payment or subscription succeeded. Adobe Commerce has no native automatic shopper-not-present transaction functionality; subscription billing needs additional integration.

**Raw locators:** Intro and `How it works` lines 17–27; `Subscription payments` lines 79–88.

**Canonical wiki route:** [[adyen-index]] → [[adyen-magento2]] → [[source-adyen-docs-plugins-adobe-commerce-set-up-tokenization]].

## Q2 — Central capability, prerequisites, and warnings

**Question:** What setup and identity fields are required or optional, and which security settings need careful qualification?

**Expected answer:** Enable `RECURRING_CONTRACT` webhooks. Configure Vault tokenization per payment method with Enabled and an applicable `CardOnFile`, `UnscheduledCardOnFile`, or `Subscription` model. Stored-card CVC is required by default; disabling that requirement for recurring card payments needs additional Adyen configuration. Multistore token use is configurable across Magento storefronts, not stated as cross-shopper or cross-merchant permission. The guide enables merchant-account additional-data card fields and Recurring details. Its risk section is optional and advises excluding recurring transactions from risk evaluation and disabling IP/velocity checks; this alters fraud controls and is not prerequisite. Vault maps `shopperReference` to Adobe Commerce `customer_id` and `storedPaymentMethodId` to `gateway_token`. In-person setup has a separate route.

**Raw locators:** Requirements line 31; Vault fields lines 33–49; Customer Area additional data lines 51–68; optional risk lines 70–77; subscription/identity lines 79–88; in-person lines 90–92.

**Canonical wiki route:** [[adyen-index]] → [[adyen-magento2]] → [[source-adyen-docs-plugins-adobe-commerce-set-up-tokenization]] → [[raw/adyen/docs/plugins/adobe-commerce/set-up-tokenization/2026-09-15|pinned raw snapshot]].
