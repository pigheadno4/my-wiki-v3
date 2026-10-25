# Alipay+ Android Drop-in retrieval checks

## Q1 — Purpose, scope and inference limit

The canonical source [[source-adyen-docs-payment-methods-alipay-plus-android-drop-in]] is a 2026-09-15-captured add-on for an existing Android Drop-in integration, with Sessions and Advanced server-side-flow sections (raw lines 15–25, 78–80). It does not establish current merchant or specific wallet eligibility, a working redirect, or an authorized/settled payment; it gives setup text and an unexecuted live-test recommendation (raw lines 64–76, 116–126).

Full retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-alipay-plus-android-drop-in]] → [[raw/adyen/docs/payment-methods/alipay-plus/android-drop-in/2026-09-15]].

## Q2 — Capability, prerequisites and warnings

Sessions requires existing Android Drop-in, Checkout API v68+, and Customer Area addition; it says no extra `/sessions` parameters (raw lines 29–40). Advanced separately requires existing Android Drop-in, redirect handling for `action.type: redirect`, and Customer Area addition, with no extra `/payments` parameters; this section gives no API version floor (raw lines 80–114). Both configuration tables show optional `setSubmitButtonVisible`, default `true`, where `false` hides the button (raw lines 44–50, 90–96). Both test sections state no Alipay+ TEST environment and recommend live penny tests, which are not performed here; both say live requests are for “Alipay” while describing Alipay+ acceptance, an unresolved label mismatch (raw lines 64–76, 116–126). No wallet-level eligibility or outcome follows from that wording.

Full retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-alipay-plus-android-drop-in]] → [[raw/adyen/docs/payment-methods/alipay-plus/android-drop-in/2026-09-15]].
