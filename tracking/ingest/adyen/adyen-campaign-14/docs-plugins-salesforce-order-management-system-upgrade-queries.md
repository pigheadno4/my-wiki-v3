# Fixed retrieval checks — Adyen Salesforce OMS upgrade

## Q1 — Purpose, scope, and non-inference

**Question:** Which OMS upgrade branches does this page describe, and what does completing its configuration steps not prove?

**Expected answer:** It describes v2→v3 and v1→v3.2.0 migration paths for the Adyen Salesforce OMS package, separate from an SFCC storefront cartridge/PWA upgrade. It is configuration and migration guidance, not a record that a package was deployed, a webhook verified, a migration script copied records, or a capture, refund, reversal, order or payout succeeded. The final go-live step is separately linked.

**Raw locators:** Intro lines 15–23; v2 steps lines 25–151; v1 steps lines 153–213; go-live link lines 215–217.

**Canonical wiki route:** [[adyen-index]] → [[adyen-salesforce-order-management-system]] → [[source-adyen-docs-plugins-salesforce-order-management-system-upgrade]].

## Q2 — Central capability, prerequisites, and warnings

**Question:** What changes are required on each version path, and which security, account-routing, data and uninstall boundaries matter?

**Expected answer:** For v2→v3, update the gateway provider to `Adyen OMS Provider` and Merchant Credential to `AdyenCheckout`, retain the provider ID for the webhook endpoint, require HMAC verification, enable `CAPTURE_FAILED` and `REFUND_FAILED` events, put the HMAC key in Salesforce metadata, and test. V3 can use the Adyen Default merchant account when the sales-channel field is empty or a channel-specific account when configured; its Named Credential uses API keys rather than basic authentication and needs Principal Credential setup. For v1, Adyen recommends v3.2.0, whose separate namespace permits side-by-side installation; update the existing gateway and site, including Guest Access to the Payments API and enabled Adyen Adapter metadata type, within that site path. Run `BatchAdyenOMSMigration.cls` to copy payment-method custom attribute values to new fields; the page does not claim token migration. Test after the upgrade steps and before uninstalling the old package. The uninstall is consequential and no successful deployment or payment follows from these instructions.

**Raw locators:** Gateway lines 25–45; webhook/HMAC lines 47–115; sales-channel and credential lines 117–151; v1 namespace/site lines 153–188; migration script lines 190–207; uninstall and go-live lines 209–217.

**Canonical wiki route:** [[adyen-index]] → [[adyen-salesforce-order-management-system]] → [[source-adyen-docs-plugins-salesforce-order-management-system-upgrade]] → [[raw/adyen/docs/plugins/salesforce-order-management-system/upgrade/2026-09-15|pinned raw snapshot]].
