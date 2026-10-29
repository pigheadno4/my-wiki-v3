# PayPo Web Drop-in worker retrieval queries

## Q1 — Purpose and flow scope

**Query:** What does the PayPo Web Drop-in guide add to Sessions and Advanced integrations?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paypo-web-drop-in.md` → `raw/adyen/docs/payment-methods/paypo/web-drop-in/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/paypo/web-drop-in`; full pinned raw `raw/adyen/docs/payment-methods/paypo/web-drop-in/2026-09-15.md`, `# PayPo Web Drop-in` lines 15–23, Sessions requirements/fields lines 25–48 and Advanced requirements/fields lines 451–487. Sessions requires Checkout API v68+, Advanced handles redirect, and both add shopper name/email; address rows are unmarked. Example PL/PLN and captured setup do not prove current merchant eligibility or a real payment.

## Q2 — Offer, capture and example qualifications

**Query:** When do PayPo's offer and 30-day shopper payment term run, what capture amount is possible, and how should the redirect and examples be used?

**Expected route:** Same root → Adyen index → online-payments concept → PayPo Web Drop-in source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path: `## Capture the payment` lines 391–405 and 875–889, optional import lines 423–433 and 463–473, redirect response lines 859–873, and `## Test and go live` lines 907–921. The offer lasts up to 72 hours before authorization; shopper repayment term starts at authorization; capture is full amount only, with optional immediate automatic capture. Merchant funding is stated after capture independent of shopper repayment; no actual settlement is proven. `RedirectShopper` is an intermediate action. Sessions uses an app-scheme return URL in this Web guide (lines 54–74), both curl examples omit the continuation between `-X POST` and `-d` (lines 59–60, 498–499), and the Advanced requirement link has unresolved platform-template markup (line 459).
