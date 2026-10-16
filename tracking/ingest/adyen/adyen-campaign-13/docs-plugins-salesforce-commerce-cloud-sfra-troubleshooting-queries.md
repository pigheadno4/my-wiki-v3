# Fixed retrieval checks — Adyen SFRA troubleshooting

## Q1 — Purpose, scope, and non-inference

**Question:** What does this page troubleshoot, and what does following one of its steps not prove?

**Expected answer:** It is a dated SFRA payment-cartridge diagnostic sequence covering setup, third-party/custom cartridge isolation, logs, missing methods, configuration symptoms, and two named order errors. It does not cover Composable Storefront generally or prove that clearing cache, rotating an API key, changing a capture setting, or reimporting metadata fixed a particular merchant deployment. It provides no payment/order outcome or blanket retry instruction.

**Raw locators:** Introduction lines 15–23; steps 1–4 lines 25–63; common errors lines 65–108; escalation lines 110–131.

**Canonical wiki route:** [[adyen-index]] → [[adyen-salesforce-commerce-cloud]] → [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-troubleshooting]] (provider-index link to SFCC concept awaits coordinator placement).

## Q2 — Central capability, prerequisites, and warnings

**Question:** How does the guide distinguish missing methods, configuration errors, and the two exact order-placement errors?

**Expected answer:** For a missing method, check additional setup, then inspect `service-adyen` logs for the `/paymentMethods` country/region/currency and response. For origin-key retrieval or payment-call configuration errors, metadata import is a likely issue; only cartridge **v20.1.2 or earlier** gets the extra live-endpoint setup check. For **“No user found for OriginKey on validation”**, check the merchant-account name and API-key merchant-account access; the guide suggests generating and copying a new key, which changes credentials and requires verification. For **“Expected intent from order api call to be authorize, got capture”**, the page specifically identifies PayPal and recommends `SALE` in code for that mismatch; it is not a universal capture rule. Cache clearing is suggested despite the Adyen cartridge itself not using SFCC cache, and third-party/custom cartridge disabling is temporary diagnosis. Check Business Manager WebDAV logs, then browser console, release notes, cartridge version and Support as appropriate; there is no documented actual fix or financial outcome for any merchant here.

**Raw locators:** Cache/cartridge isolation lines 25–53; logs lines 55–63; missing methods lines 73–79; configuration lines 81–93; order errors lines 95–108; version/escalation lines 110–131.

**Canonical wiki route:** [[adyen-index]] → [[adyen-salesforce-commerce-cloud]] → [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-troubleshooting]] → [[raw/adyen/docs/plugins/salesforce-commerce-cloud/sfra/troubleshooting/2026-09-15|pinned raw snapshot]].
