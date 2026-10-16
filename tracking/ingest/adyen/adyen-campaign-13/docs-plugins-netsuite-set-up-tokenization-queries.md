# Fixed retrieval checks — docs-plugins-netsuite-set-up-tokenization

## Q1 — Purpose, scope, and what not to infer

**Query:** What does this NetSuite tokenization page cover, and what does it not establish?

**Answer:** It is Adyen's NetSuite configuration guide for Payment Instruments, Adyen payment-processing-profile token choices, Customer Area additional data, imported tokens, transaction overrides and recurring-contract notifications. It does not establish merchant enablement or consent, successful token creation in a particular account, token validity, authorization or any later recurring-payment success. The manual-token subsection is an unfinished sentence, not a usable procedure. The page is 2023-modified and captured 2026-09-15, with no package version. Evidence: raw lines 11, 15–35, 107–109, 126–156. Canonical route: [[adyen-index]] → [[adyen-netsuite]] → ## Sources → [[source-adyen-docs-plugins-netsuite-set-up-tokenization]] → [[raw/adyen/docs/plugins/netsuite/set-up-tokenization/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Query:** How is tokenization configured or an existing token imported in this NetSuite guide, and what risks and conditions matter?

**Answer:** Enable NetSuite Payment Instruments first, noting the UI/field change; Pay by Link tokenization also needs PBL custom preferences. Edit the Adyen payment processing profile to choose card tokenization, one of CardOnFile/UnscheduledCardOnFile/Subscription (sent with the request), optional PBL tokenization/default behavior, and matching card or general token method instances. Select the listed Card data plus Payment recurring details in the merchant Customer Area. Import a token in the Customer Record with matching type, method, value and Adyen family. A token created outside NetSuite needs its Adyen Shopper Reference; otherwise NetSuite uses its internal customer ID and Adyen invalidates an existing token whose reference does not match. Transaction card tokenization and recurring-model overrides can inherit profile settings when blank. Notifications need webhooks and RECURRING_CONTRACT; general tokens arise for non-card details on the webhook, distinct from card-token notifications. None of this guarantees future payment success, and the manual-token section cannot fill in missing steps. Evidence: raw lines 21–27, 36–78, 80–105, 107–156. Canonical route: [[adyen-index]] → [[adyen-netsuite]] → ## Sources → [[source-adyen-docs-plugins-netsuite-set-up-tokenization]] → [[raw/adyen/docs/plugins/netsuite/set-up-tokenization/2026-09-15]].
