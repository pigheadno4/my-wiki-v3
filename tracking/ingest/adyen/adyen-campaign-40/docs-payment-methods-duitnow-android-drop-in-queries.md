# Q1 — Purpose, scope and limits

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-android-sdk.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-duitnow-android-drop-in.md` → pinned raw.

This 2026-09-15 page adds DuitNow to an **existing Android Drop-in** integration, with separate Sessions and Advanced prerequisites (raw `adyen/docs/payment-methods/duitnow/android-drop-in/2026-09-15.md:15-37`). It documents method-specific request/configuration additions and test/live setup, not a complete base integration or payment result flow (raw lines 39-65). It does not establish a minimum SDK/API version, QR/action behavior, current account enablement or an executed transaction (raw lines 21-71).

# Q2 — Central capability, prerequisites and warnings

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-android-sdk.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-duitnow-android-drop-in.md`. Online-method retrieval also routes through `wiki/concepts/adyen-online-payments.md`.

The merchant needs the corresponding existing Android Drop-in Sessions or Advanced flow and DuitNow added in Customer Area (raw `adyen/docs/payment-methods/duitnow/android-drop-in/2026-09-15.md:21-37`). DuitNow adds no **method-specific** fields to Sessions `/sessions` or Advanced `/payments`, and no extra Drop-in configuration in either branch (raw lines 39-57); that does not remove ordinary base request requirements. The page says to test with real payment details and small amounts, check test status in Customer Area, and contact Support to add DuitNow in the live Customer Area before accepting live payments (raw lines 59-65). It gives no DuitNow-specific response, QR, webhook or settlement instructions (raw lines 39-71).
