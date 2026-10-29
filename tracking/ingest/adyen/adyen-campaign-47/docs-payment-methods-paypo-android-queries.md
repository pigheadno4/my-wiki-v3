# Fixed queries — PayPo Android chooser

## Q1 — purpose and limits

**Query:** What does the captured PayPo Android page provide, and what does it leave to other guides?

**Expected answer:** The page at `https://docs.adyen.com/payment-methods/paypo/android` is a 2026-09-15-captured Android integration chooser. It links method-specific Drop-in and Components children and the main Android Sessions/Advanced integrations. It does not give method request fields, SDK version requirements, capture procedure, merchant eligibility, or proof of a live payment (full pinned `raw/adyen/docs/payment-methods/paypo/android/2026-09-15.md`, `# PayPo for Android` lines 15–17 and chooser/See also lines 19–36). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paypo-android.md`.

## Q2 — UI and server-side routes

**Query:** Which Android PayPo UI paths and underlying server-side flows does this chooser point to?

**Expected answer:** Drop-in is the all-in-one UI path at `/payment-methods/paypo/android-drop-in`; Components points to `/payment-methods/paypo/android-component` and names `InstantPaymentComponent` for redirecting to PayPo (pinned `raw/adyen/docs/payment-methods/paypo/android/2026-09-15.md`, `### How do you want to integrate?` lines 19–27). The page says to create the main integration first and links Android Drop-in and Android Components for both Sessions and Advanced flows (`## See also` lines 29–36). These links are navigation, not evidence that any merchant is configured or that a redirect/payment completed. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paypo-android.md`.
