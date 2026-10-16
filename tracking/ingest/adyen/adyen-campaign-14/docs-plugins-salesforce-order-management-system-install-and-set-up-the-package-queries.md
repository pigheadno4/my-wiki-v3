# Fixed retrieval checks — docs-plugins-salesforce-order-management-system-install-and-set-up-the-package

## Q1 — Purpose, scope, and what not to infer

**Query:** What is this Salesforce OMS setup page for, and what does it not prove?

**Answer:** It instructs installation/configuration of Adyen's Salesforce OMS package for an SFCC storefront using the Adyen payments cartridge, including requirements, v3.3.0+ guided setup, capture-mode handling and test-to-live credentials. It is not a Composable Storefront setup guide, a proof of installed version or user roles, an actual gateway/webhook configuration record, or payment/capture/settlement evidence. Its metadata is last modified 2023-12-12 and captured 2026-09-15. Evidence: raw lines 11, 19–64, 68–145. Canonical route: [[adyen-index]] → [[adyen-salesforce-order-management-system]] → ## Sources → [[source-adyen-docs-plugins-salesforce-order-management-system-install-and-set-up-the-package]] → [[raw/adyen/docs/plugins/salesforce-order-management-system/install-and-set-up-the-package/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Query:** What must be set up, how do capture modes differ, and what security/environment transition is described?

**Answer:** The prerequisite table names an Adyen-cartridge SFCC storefront, Standard webhooks, a connected OMS Org, manual capture in Customer Area and the dependent API Library Apex Adyen package; install also calls for multiple currencies and the OMS app. From v3.3.0 the app offers guided configuration, with manual setup as a separate linked route. Later text documents both manual OMS capture after authorization and automatic capture; **Auto Capture Enabled** and method-variant lists prevent duplicate requests, including methods captured immediately regardless of mode. Because the table says manual capture while later instructions handle automatic capture, keep that tension visible and check the merchant's mode. Live transition changes HMAC, merchant account if different, Adyen Checkout named-credential URL/live prefix, and linked external-credential API key; a live account is a separate prerequisite. No detailed role matrix or successful configuration is proven here. Evidence: raw lines 31–38, 50–64, 68–119, 121–145. Canonical route: [[adyen-index]] → [[adyen-salesforce-order-management-system]] → ## Sources → [[source-adyen-docs-plugins-salesforce-order-management-system-install-and-set-up-the-package]] → [[raw/adyen/docs/plugins/salesforce-order-management-system/install-and-set-up-the-package/2026-09-15]].
