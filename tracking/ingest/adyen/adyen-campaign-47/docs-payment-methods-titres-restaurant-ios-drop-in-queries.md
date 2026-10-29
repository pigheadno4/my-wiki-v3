# Fixed retrieval checks — Titres-restaurant iOS Drop-in

## Q1 — Purpose and scope

**Query:** What does the captured Titres-restaurant iOS Drop-in guide add, and what does it establish about live acceptance?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-titres-restaurant-ios-drop-in.md` → `raw/adyen/docs/payment-methods/titres-restaurant/ios-drop-in/2026-09-15.md`.

**Answer:** The guide adds method-specific setup to an existing iOS Drop-in integration, with a minimum v5.4.0 requirement, CONECS activation card, SIRET and Conecs MID supplied when adding the method in Customer Area. The Sessions path needs no extra method-specific iOS Drop-in configuration and returns the result in `didComplete`. Issuer-supplied test credentials and Adyen Support activation are still needed for testing and live acceptance. The page is not proof that a particular merchant is currently enabled or has completed a payment.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/titres-restaurant/ios-drop-in`; pinned raw `raw/adyen/docs/payment-methods/titres-restaurant/ios-drop-in/2026-09-15.md`, `# Titres-restaurant iOS Drop-in integration` lines 15–27, `## API reference` and `## Drop-in configuration` lines 29–52, `## Test and go live` lines 96–100.

## Q2 — Split tender and outcome

**Query:** On this iOS Drop-in page, when are balance/order callbacks used, and does an order request finish the payment?

**Expected route:** Same root → Adyen index → online-payments concept → iOS Drop-in source → pinned raw.

**Answer:** For the additional-use-case `/payments` path, `checkBalance` calls `/paymentMethods/balance` when the shopper pays with the meal voucher. If voucher balance is below the transaction, `requestOrder` calls `/orders` for the total amount so the voucher and another method can make partial payments; `cancelOrder` calls `/orders/cancel` if the shopper cancels. These callbacks do not themselves authorize a payment. The `/payments` resultCode is shown to the shopper, the outcome also arrives by webhook, and an Authorised payment still needs capture when manual capture is used. The page's broad `/sessions` v5.0.0 wording does not erase its v5.4.0 requirement.

**Evidence locator:** Same canonical stem and full pinned raw path; `### Tab: /payments` lines 50–81 and `## Show the payment result` lines 83–94, with version wording at lines 25 and 33–42.
