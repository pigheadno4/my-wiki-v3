# Adyen C33 coordinator full-read exemplars

**PASS** — 2026-10-24. The coordinator independently read the three predetermined full pinned raw samples, including the longest, then compared each final promoted source and both locator-backed query answers.

| Pinned raw | Full lines | Result |
| --- | ---: | --- |
| `raw/adyen/docs/payment-methods/alipay/2026-09-15.md` | 83 | PASS |
| `raw/adyen/docs/payment-methods/naverpay/api-only/2026-09-15.md` | 646 | PASS |
| `raw/adyen/docs/payment-methods/paypay/android-component/2026-09-15.md` | 254 | PASS |

Alipay retains the explicit outside-China processing boundary despite broad International/Multiple labels, 12-hour open offer versus final payment state, matrix flow None versus unread child handoff behavior, supported refund variants and unavailable recurring/capture/chargeback marks. Navigation remains distinct from child implementation and historical marketing numbers are not current measurements.

NaverPay API-only raw was fully read in untruncated ranges 1–340 and 341–646. Its final source and Q1/Q2 retain existing Advanced API-only and redirect prerequisites, Customer Area setup, KR/KRW method discovery and kcp_naverpay type, no additional shopper fields, item-information prose versus no-extra-parameters conflict, absent paymentMethod/item fields in illustrative requests, intermediate RedirectShopper response and no final webhook/payment proof. Adyen TEST examples coexist with the explicit absence of a NaverPay test environment; the source recommendation to test live was read only, never executed.

PayPay Android Component retains Sessions-only Checkout v68+, distinct Advanced requirements, redirect handling and Customer Area setup, instant/Compose imports and unique Component keys, session versus paymentMethods method lookup, no extra method-specific fields without waiving base-flow requirements, DGFT AUTHFlow/SALEFlow TEST simulator without PayPay app, and activated LIVE app accessed via Japan-local IP. No currency, completed return, authorization, capture or settlement is inferred from this page.

All three final source/Q1/Q2 comparisons pass. No material final sample failure triggered expanded sampling. Provider catalog completeness is verified at close. Raw is immutable; no provider, wallet, account or payment operation was performed.
