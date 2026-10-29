# C45 Afterpay Android Component retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-afterpaytouch-android-component`

Full pinned raw path: `raw/adyen/docs/payment-methods/afterpaytouch/android-component/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-afterpaytouch-android-component]]` → `[[raw/adyen/docs/payment-methods/afterpaytouch/android-component/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** What does this Afterpay Android Component page cover, and does its US sandbox choice establish live availability?

**Answer path:** Opening lines 15–23 describe method-specific additions to an existing Android Components integration, split by Sessions and Advanced flow. `## Test and go live` lines 846–865 and 1731–1750 list AU/NZ/US/CA sandbox shopper-account choices. The linked overview `raw/adyen/docs/payment-methods/afterpaytouch/2026-09-15.md` lines 23–31 instead lists AU/CA/NZ in its method matrix and calls the US service Cash App Afterpay/$Afterpay. Preserve the scope difference: neither sandbox selector nor example proves US live eligibility, account enablement or payment success.

## Q2 — central capability, prerequisites and warnings

**Query:** What must an Android Components merchant add for Afterpay, and what happens at redirect and capture?

**Answer path:** Sessions `## Requirements` lines 29–36 requires the base flow, Checkout API v68+, redirect handling and Customer Area addition; `/sessions` table lines 40–53 has required shopper/country/address/items fields and optional phone. Advanced requirements lines 867–875 and `/payments` table lines 963–979 add method `afterpaytouch` and the same data. Component/import sections lines 739–821 and 877–961 show `instant`, optional Compose module, no extra method configuration and `InstantPaymentComponent`; the Advanced response lines 1694–1708 is a redirect action, not final payment proof. Capture sections lines 825–844 and 1710–1729 distinguish automatic/manual capture, 13-day live and one-day test authorisation expiry, and automatic cancellation of the unclaimed amount after partial capture unless multiple partial captures are enabled. For code adaptation, Sessions NodeJS samples at lines 376–385 and 661–670 use `Config` and `EnvironmentEnum.TEST` without importing them in those snippets; they are not verified standalone setup, and this does not establish a general SDK defect. The Advanced Go example labels v10.4.0 but imports `/v9/src` packages at lines 1388–1393, so verify the intended module/version before copying. Test/live sections require sandbox setup and a live Customer Area request.
