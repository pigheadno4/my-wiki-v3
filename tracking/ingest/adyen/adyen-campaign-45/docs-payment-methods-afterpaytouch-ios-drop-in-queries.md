# C45 Afterpay iOS Drop-in retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-afterpaytouch-ios-drop-in`

Full pinned raw path: `raw/adyen/docs/payment-methods/afterpaytouch/ios-drop-in/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-afterpaytouch-ios-drop-in]]` → `[[raw/adyen/docs/payment-methods/afterpaytouch/ios-drop-in/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** What does this Afterpay iOS Drop-in page add, and does its US sandbox account choice prove live Afterpay eligibility?

**Answer path:** Opening lines 15–23 scope the page to Afterpay-specific additions to an existing iOS Drop-in, split into Sessions and Advanced. Test sections lines 766–785 and 1575–1594 list AU/NZ/US/CA sandbox shopper accounts. The linked overview `raw/adyen/docs/payment-methods/afterpaytouch/2026-09-15.md` lines 23–31 lists AU/CA/NZ in its payment-method matrix and separate US Cash App Afterpay/$Afterpay branding. A US sandbox choice, TEST request or payment-list result does not prove US live eligibility, merchant enablement or settlement.

## Q2 — central capability, prerequisites and warnings

**Query:** Which iOS Drop-in requests and flow prerequisites does this guide add, and what capture constraints follow?

**Answer path:** Sessions requirements lines 29–34 specify the existing iOS Drop-in, Checkout API v68+ and Customer Area addition; `/sessions` table lines 38–51 marks shopper/country/address/item data required and phone optional. Advanced requirements lines 791–797 explicitly add redirect handling; `/payments` table lines 807–821 includes `afterpaytouch`. No additional method configuration is stated at lines 739–741 and 801–803. Advanced sample lines 1536–1550 returns a redirect action, not final authorisation. Capture sections lines 745–764 and 1552–1571 distinguish automatic/manual capture, 13-day expiry, one-day test expiry, and partial-capture remainder cancellation unless multiple partial capture is enabled. For copying snippets, Sessions NodeJS examples at lines 374–383 and 659–668 use unimported `Config`/`EnvironmentEnum.TEST`; the Advanced Go example labels v10.4.0 but imports `/v9/src` at lines 1230–1235. Verify the intended setup rather than inferring a general SDK defect.
