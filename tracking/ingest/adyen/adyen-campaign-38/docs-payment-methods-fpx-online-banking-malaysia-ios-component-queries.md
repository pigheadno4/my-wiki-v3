# FPX Online Banking Malaysia iOS Component retrieval checks

## Q1 — Purpose, scope and inference limit

The canonical source [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-ios-component]] is a 2026-09-15-captured method-specific add-on to an existing iOS Components integration, with separate Sessions and Advanced server-side-flow sections (raw lines 15–25, 80–84). The page does not itself establish merchant enablement, current availability, a successful redirect, authorization or settlement; it points to base integration guides and gives a distinct live Customer Area request gate (raw lines 19–23, 72–78, 125–131).

Full retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-ios-component]] → [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/ios-component/2026-09-15]].

## Q2 — Capability, prerequisites and warnings

Sessions requires an existing iOS Components integration, Checkout API v68+, redirect handling, and Customer Area setup; it states no additional `/sessions` parameters or method configuration (raw lines 29–48). The Sessions Swift example checks for `molpay_ebanking_fpx_MY`, initializes `InstantPaymentComponent`, sets the session delegate and initiates payment (raw lines 52–70). Advanced separately requires existing Components, redirect handling and setup, states no extra configuration or `/payments` parameters, and uses `self` as delegate (raw lines 84–123); the page does not assign Advanced the Sessions v68 floor. Its Advanced integration label says Components while its target URL uses Drop-in, unlike nearby Components targets (raw lines 88–90, 123). Both test sections use available issuer IDs and test Customer Area status and require a separate live request (raw lines 72–78, 125–131). These are guide conditions, not demonstrated outcomes.

Full retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-ios-component]] → [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/ios-component/2026-09-15]].
