# Fixed retrieval queries — PayPo Android Drop-in

## Q1 — Purpose and scope

**Query:** What is the PayPo Android Drop-in guide, and what does its captured evidence not establish?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paypo-android-drop-in.md` → `raw/adyen/docs/payment-methods/paypo/android-drop-in/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/paypo/android-drop-in`; full pinned raw `raw/adyen/docs/payment-methods/paypo/android-drop-in/2026-09-15.md`, title and add-on scope lines 15–23, Sessions/Advanced headings and requirements lines 25–34 and 444–452. This is PayPo-specific guidance for existing Android Drop-in, with PL/PLN and test examples; it does not prove present merchant enablement or a real successful payment.

## Q2 — Required fields, redirect and capture

**Query:** What differs between Sessions and Advanced, what happens at redirect and authorization, and what capture/test qualifications apply?

**Expected route:** Same root → Adyen index → online-payments concept → PayPo Android Drop-in source → pinned raw.

**Evidence locator:** Same canonical stem and full raw path. Sessions needs Checkout API v68+, `shopperName` and `shopperEmail` on `/sessions` (lines 29–47); Advanced needs redirect action handling and `paymentMethod.type: paypo`, name and email on `/payments`, with no version minimum stated in its row (lines 444–472). Advanced example returns `RedirectShopper`/redirect action (lines 844–858). The offer link lasts up to 72 hours before authorization; 30-day shopper term starts at authorization, followed by mandatory full-amount capture; automatic capture is configurable and merchant funding is described after capture (lines 390–420, 860–890). Test values and live Customer Area request appear at lines 430–442 and 892–904. Both flows require no added PayPo Drop-in configuration (lines 424–426, 456–458). Sessions app-scheme and Advanced HTTPS returnUrl examples differ (lines 65, 493); both payment curl blocks lack continuation before `-d` (lines 58–59, 483–484).
