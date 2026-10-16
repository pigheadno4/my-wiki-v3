# Fixed queries — docs-plugins-salesforce-commerce-cloud-sfra-customization-guide

## Q1 — Purpose, scope, and what must not be inferred

**Answer:** This Adyen webpage guides customization of the Salesforce Commerce Cloud SFRA cartridge checkout: separate-cartridge flow overrides, payment-method configuration and version-gated pre-authorization checks. It does not define Composable Storefront/PWA Kit behavior. A method in the configuration list or sample card callback does not prove merchant enablement, deployed runtime behavior, payment authorization, capture, settlement, or support for modified default code.

**Raw locators:** lines 15–39 (identity, customization types and support/version warning); lines 113–171 (method list, options and edit route); lines 201–214 (pre-authorization hook).

**Canonical route:** [[adyen-index]] → [[adyen-salesforce-commerce-cloud]] → [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-customization-guide]] → [[raw/adyen/docs/plugins/salesforce-commerce-cloud/sfra/customization-guide/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Answer:** From v23.2.1, the guide's preferred pattern adds a custom cartridge before the Adyen cartridge; support continuation is conditional on using a supported version. It warns that editing default Adyen cartridge code can impair support and upgrades. Its later method-configuration steps nevertheless point inside the default `app_adyen_SFRA` path, an unresolved tension that should be retained. The listed method-specific options include pay-button visibility, test/live environment and callbacks, but the method list is not an enablement guarantee. From v25.4.0, the `app.payment.pre.auth` hook can stop or allow an Adyen `/payments` request based on custom checks; the third-party risk call is only an example. The page asks for tests and deployment checks, while `npm install` and `npm run build` alone are not test proof.

**Raw locators:** lines 23–39 (support and v23.2.1 route); 41–67 and 73–111 (cartridge creation/extraction); 113–199 (method-specific options and direct-edit path); 201–214 (v25.4.0 hook); 216–225 (troubleshooting).

**Canonical route:** [[adyen-index]] → [[adyen-salesforce-commerce-cloud]] → [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-customization-guide]]; complete instructions and conflict at [[raw/adyen/docs/plugins/salesforce-commerce-cloud/sfra/customization-guide/2026-09-15]].
