# Fixed retrieval queries — PaySafeCard Android Component

## Q1 — Purpose and evidence boundary

**Query:** What does the captured PaySafeCard Android Component guide add, and what does it not prove?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paysafecard-android-component.md` → `raw/adyen/docs/payment-methods/paysafecard/android-component/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/paysafecard/android-component`; full pinned raw `raw/adyen/docs/payment-methods/paysafecard/android-component/2026-09-15.md`, `# PaySafeCard Android Component` lines 15–23, Sessions and Advanced requirements lines 25–36 and 364–372. It is a method-specific add-on to existing Android Components, not proof of present merchant enablement, a complete base integration or executed live payment.

## Q2 — Shopper reference, Component and sample limits

**Query:** What must the Sessions and Advanced requests add, how is PaySafeCard shown on Android, and which request/test caveats apply?

**Expected route:** Same root → Adyen index → online-payments concept → PaySafeCard Android Component source → pinned raw.

**Evidence locator:** Same canonical stem and full raw path. Sessions requires Checkout API v68+, redirect handling, Customer Area setup and `shopperReference` in `/sessions` (lines 29–47); Advanced requires redirect handling and `shopperReference` in `/payments`, without a version minimum in its own requirement row (lines 364–372, 460–469). Compose and non-Compose use `InstantPaymentComponent` for `paysafecard`, with session method lookup versus Advanced `/paymentMethods` lookup and a unique Compose key for reset/screen/session changes (lines 270–352, 374–458). The Advanced `/payments` samples omit `paymentMethod` even though the Component looks it up, so these are not complete requests (lines 416–419, 475–489, 512–752); Sessions SDK snippets omit request construction and both curl blocks lack continuation before `-d` (lines 57–58, 87–89, 479–480). The sample response is redirect, not final authorization (lines 755–769); test code and Support live setup are at lines 354–362 and 771–779, with the Support link pointing to a test Customer Area URL.
