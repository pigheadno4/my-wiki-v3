# Fixed retrieval checks — Salesforce OMS manual setup

Q1. What package/setup scope does this guide cover, and what must not be inferred?
- Expected: Manual setup of the Adyen Salesforce OMS package for an SFCC storefront using the Adyen payments cartridge; guided setup is default from OMS v3.3.0. Prerequisites include connected OMS Org, Standard webhooks, manual capture and dependent Apex package, while later automatic-capture steps form a separate branch. The guide does not prove the package was installed, a merchant has live eligibility, a seller/legal-entity identity, or an actual order/payment/capture/refund/bank result.
- Raw locators: `raw/adyen/docs/plugins/salesforce-order-management-system/install-and-set-up-the-package/manual-setup/2026-09-15.md:15-55`, `:354-361`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-plugins-salesforce-order-management-system-install-and-set-up-the-package-manual-setup.md` → proposed `[[adyen-salesforce-order-management-system]]`.

Q2. Which gateway, webhook, credential and capture conditions are consequential?
- Expected: Gateway External Reference matches B2C Payment Processor ID, with POS gateway only for endless aisle. Salesforce site endpoints expose guest/API permissions and Named Credential URL; Standard webhooks use HMAC, JSON/TLS and required/conditional events. A success webhook can precede later capture/refund failure, so monitor GatewayResultCode; HTTP 200 test is not final processing proof. Configure API-key Principal Credential and permission access for automation user, case-sensitive merchant metadata and optional sales-channel mapping. Automatic capture and immediate-capture method variants need duplicate-request safeguards; live account switch updates HMAC, merchant name if different, Checkout URL and API key.
- Raw locators: `raw/adyen/docs/plugins/salesforce-order-management-system/install-and-set-up-the-package/manual-setup/2026-09-15.md:57-109`, `:111-214`, `:235-338`, `:354-431`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-plugins-salesforce-order-management-system-install-and-set-up-the-package-manual-setup.md` → proposed `[[adyen-salesforce-order-management-system]]`.
