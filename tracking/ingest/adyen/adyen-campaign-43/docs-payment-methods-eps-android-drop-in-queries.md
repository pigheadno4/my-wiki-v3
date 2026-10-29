# Fixed-query retrieval: source-adyen-docs-payment-methods-eps-android-drop-in

Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-eps-android-drop-in]]. Canonical: https://docs.adyen.com/payment-methods/eps/android-drop-in. Pinned raw: `raw/adyen/docs/payment-methods/eps/android-drop-in/2026-09-15.md`.

## Q1 — What does this page cover, and what should not be inferred?

It supplies only EPS-specific additions to an existing Android Drop-in integration, split into Sessions and Advanced flows (raw/adyen/docs/payment-methods/eps/android-drop-in/2026-09-15.md:15-25,113-121). Sessions names Checkout API v68+, and both flows require EPS added in Customer Area (raw/adyen/docs/payment-methods/eps/android-drop-in/2026-09-15.md:29-34,115-121). It is not standalone proof of current EPS merchant enablement, a completed bank redirect, or settled payment; live acceptance requires an EPS request in the live Customer Area (raw/adyen/docs/payment-methods/eps/android-drop-in/2026-09-15.md:107-111,192-196).

## Q2 — What base-flow, redirect and recurring qualifications matter?

The base Sessions `/sessions` request needs no extra EPS parameters; the Advanced `/payments` request likewise needs none, but Advanced must already handle `action.type: redirect` (raw/adyen/docs/payment-methods/eps/android-drop-in/2026-09-15.md:36-40,115-149). Both show optional `setSubmitButtonVisible`, default true, whose schematic sample is not copy-ready (raw/adyen/docs/payment-methods/eps/android-drop-in/2026-09-15.md:42-62,123-143). Recurring EPS is via SEPA Direct Debit: permission and transparent schedule/amount are strongly recommended; token creation adds `storePaymentMethod` and `shopperReference` to `/payments`, then a token-created webhook follows settlement before future `ContAuth` payments with a stored ID and recurring model (raw/adyen/docs/payment-methods/eps/android-drop-in/2026-09-15.md:64-103,151-190). The Sessions section's token-creation `/payments` language is a separate recurring use case, not an extra field for the base `/sessions` payment.
