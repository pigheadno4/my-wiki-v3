# C45 Afterpay Web Drop-in retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-afterpaytouch-web-drop-in`

Full pinned raw path: `raw/adyen/docs/payment-methods/afterpaytouch/web-drop-in/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-afterpaytouch-web-drop-in]]` → `[[raw/adyen/docs/payment-methods/afterpaytouch/web-drop-in/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** What is the Afterpay Web Drop-in page for, and does its US sandbox option prove live availability?

**Answer path:** Opening lines 15–23 say this page adds method-specific instructions to an existing Web Drop-in integration, with Sessions and Advanced routes. Its test sections at lines 774–793 and 1589–1608 offer AU/NZ/US/CA sandbox account choices. The linked overview `raw/adyen/docs/payment-methods/afterpaytouch/2026-09-15.md` lines 23–31 lists AU/CA/NZ in its method matrix and separate US Cash App Afterpay/$Afterpay branding. Preserve that scope: no US live eligibility, merchant enablement, or payment success follows from a sandbox selector or TEST fixture.

## Q2 — central capability, prerequisites and warnings

**Query:** What does Web Drop-in add for Afterpay in Sessions and Advanced, and what are the redirect/capture boundaries?

**Answer path:** Sessions requirements lines 29–36 specify base Web Drop-in, Checkout API v68+, redirect handling and Customer Area addition; `/sessions` table lines 40–53 specifies required shopper/country/address/items data with optional phone. Advanced requirements lines 799–805 and `/payments` table lines 821–835 add `afterpaytouch` method. Optional tree-shaken `Redirect` import is at lines 739–749 and 807–817; line 803's Advanced base link contains an unresolved encoded platform placeholder. Initial Advanced response lines 1550–1564 is `RedirectShopper`, not final authorisation. Capture sections lines 753–772 and 1566–1585 distinguish automatic/manual setup, 13-day authorisation capture, one-day test expiry and partial-capture remainder cancellation unless multiple partial capture is enabled. Test/live sections require sandbox setup and a live Customer Area request.
