# Fixed retrieval checks — docs-payment-methods-titres-restaurant

## Q1 — Identity, time and scope

**Query:** What does Adyen's Titres-restaurant overview describe, and what should not be inferred from it?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-titres-restaurant.md` → `raw/adyen/docs/payment-methods/titres-restaurant/2026-09-15.md`.

**Answer:** It describes French meal-voucher prepaid cards, with a EUR 25 daily limit, another-method remainder option and Sunday/public-holiday restriction as claims in a page last modified 2023-06-21 and fetched 2026-09-15 (raw 5–21). The snapshot does not establish today's rules, merchant eligibility or a completed payment. Canonical stem: `https://docs.adyen.com/payment-methods/titres-restaurant`.

## Q2 — Issuers, features and activation

**Query:** Which issuer/channel combinations, feature marks and activation prerequisites are in the Titres-restaurant page?

**Expected route:** same root → provider → concept → source → pinned raw.

**Answer:** The page lists Bimpli, Sodexo and Up Déjeuner for online payments, Edenred for in-person, and says all meal-voucher cards are co-badged with Conecs (raw 21). Its FR/EUR direct prepaid/gift-card matrix marks separate captures supported while recurring, refunds, partial/multiple partial captures and chargebacks are marked unsupported (23–25). Merchants need commission authorization, a CONECS card/MID and separate issuer contracts (27–34). Web, iOS, API-only and in-person links route to other guides (36–60). Keep the online/in-person issuer split and historical nature of the EUR 25/day and Sunday/holiday claims; do not infer current legal scope or account availability. Canonical stem: `https://docs.adyen.com/payment-methods/titres-restaurant`; pinned raw: `raw/adyen/docs/payment-methods/titres-restaurant/2026-09-15.md`.
