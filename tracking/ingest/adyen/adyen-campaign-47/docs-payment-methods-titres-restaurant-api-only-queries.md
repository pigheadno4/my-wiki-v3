# Fixed retrieval checks — docs-payment-methods-titres-restaurant-api-only

## Q1 — Purpose and boundary

**Query:** What does the Titres-restaurant API-only page cover, and does its balance Success prove a payment?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-titres-restaurant-api-only.md` → `raw/adyen/docs/payment-methods/titres-restaurant/api-only/2026-09-15.md`.

**Answer:** It is a 2022-modified add-on to an existing Web API-only integration, with merchant-built form, issuer discovery, balance check, order-based split tender, /payments and webhook result handling (raw 15–19, 29–63, 357–503). A balance response's resultCode Success only indicates the example balance-check response (342–355), not an authorized payment. This snapshot does not establish current eligibility or secure handling rules. Canonical stem: `https://docs.adyen.com/payment-methods/titres-restaurant/api-only`.

## Q2 — Activation, brand types, split payments and outcomes

**Query:** What credentials and steps are needed for Titres-restaurant API-only, and what happens when voucher balance is insufficient?

**Expected route:** same root → provider → concept → source → pinned raw.

**Answer:** Existing API-only integration, CONECS activation card, SIRET and Conecs MID are prerequisites (21–27); the overview also describes separate issuer contracts. FR/EUR /paymentMethods discovery lists issuer-branded types for Up, Apetiz/Bimpli and Sodexo (29–59), but its displayed response is malformed JSON (40–55). /paymentMethods/balance uses generic mealVoucher_FR with number/expiry/reference (61–73); if balance is insufficient, create an order and ask for partial payments with voucher plus another method (357–359), not partial capture. Server /payments uses generic mealVoucher_FR and requires number, expiry and CVC (361–371). Present resultCode and receive asynchronous webhook outcome; Authorised still needs capture when manual capture is used (486–503). TEST credentials come from issuer, and live activation needs Support (505–509). The old examples use TEST v72/v68 and expiryYear 2023, so are not current runnable credentials (80–92, 376–393). Canonical stem: `https://docs.adyen.com/payment-methods/titres-restaurant/api-only`; pinned raw: `raw/adyen/docs/payment-methods/titres-restaurant/api-only/2026-09-15.md`.
