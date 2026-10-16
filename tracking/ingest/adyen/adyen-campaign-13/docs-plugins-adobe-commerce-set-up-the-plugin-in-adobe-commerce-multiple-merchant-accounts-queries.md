# Fixed retrieval checks — docs-plugins-adobe-commerce-set-up-the-plugin-in-adobe-commerce-multiple-merchant-accounts

## Q1 — Purpose, scope, and what not to infer

**Query:** What is this Adobe Commerce multiple-merchant-account page for, and what does it not establish?

**Answer:** It is a configuration guide to arranging Adobe Commerce websites, stores and store views, and selecting the relevant store view in payment-method settings when an installation uses more than one Adyen merchant account. It does not prove any merchant account is active, define account-specific API credentials or webhook routing, establish token portability, or show which account ultimately receives funds. It has no exact package version; metadata last modified 2023-05-03, snapshot captured 2026-09-15. Evidence: raw lines 11, 15–19, 21–41, 68–87. Canonical route: [[adyen-index]] → [[adyen-magento2]] → ## Related → [[source-adyen-docs-plugins-adobe-commerce-set-up-the-plugin-in-adobe-commerce-multiple-merchant-accounts]] → [[raw/adyen/docs/plugins/adobe-commerce/set-up-the-plugin-in-adobe-commerce/multiple-merchant-accounts/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Query:** How does the page separate multiple merchant accounts in one Adobe Commerce installation, and what scope warning matters?

**Answer:** Adobe Commerce is organized website → store → store view. The page says processing payments from different merchant accounts requires multiple store views. If the accounts use different websites, additional websites can separate them; if they share a website, add separate store views. Create and enable the view under its store, then select that view under **Stores → Configuration → Sales → Payment Methods** / **Scope: Default Config** and save view-specific payment-method settings. Merely naming a view after an account or changing the method display does not prove correct credential/webhook binding, a payment outcome, or a cross-account funds path; those topics are not specified here. Evidence: raw lines 21–41, 51–75. Canonical route: [[adyen-index]] → [[adyen-magento2]] → ## Related → [[source-adyen-docs-plugins-adobe-commerce-set-up-the-plugin-in-adobe-commerce-multiple-merchant-accounts]] → [[raw/adyen/docs/plugins/adobe-commerce/set-up-the-plugin-in-adobe-commerce/multiple-merchant-accounts/2026-09-15]].
