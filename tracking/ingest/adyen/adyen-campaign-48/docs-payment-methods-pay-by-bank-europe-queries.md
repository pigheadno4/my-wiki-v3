# Pay by Bank (Europe) overview worker retrieval queries

## Q1 — Identity, availability and shopper route

**Query:** What is Pay by Bank (Europe), who does the shopper visit, and which countries does this captured overview state?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-pay-by-bank-europe.md` → `raw/adyen/docs/payment-methods/pay-by-bank-europe/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/pay-by-bank-europe`; full pinned raw `raw/adyen/docs/payment-methods/pay-by-bank-europe/2026-09-15.md`, `# Pay by Bank (Europe)` lines 15–27, shopper redirect sequence lines 29–39 and capability table lines 41–43. Onboarding needs Adyen approval; Tink redirects to the bank. Merchant-form issuer selection is UK-only. Prose lists DE/FR/UK, while table adds FI; retain that conflict rather than claiming current Finland or merchant eligibility.

## Q2 — Authorization, funds and chargeback qualifications

**Query:** Does a successful Pay by Bank (Europe) AUTHORISATION webhook prove receipt of funds, and what does the page say happens after delayed/non-arriving funds?

**Expected route:** Same root → Adyen index → online-payments concept → Pay by Bank (Europe) source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path: `## Chargebacks` lines 45–60 and integration routes lines 62–80. Successful AUTHORISATION means verification and transfer initiation, not guaranteed funds. Bank cancellation or delayed processing can prevent funding; Adyen may not learn the failure. Status remains SentForSettle until funds arrive; after 8 weekdays without funds the documented sequence is Settled then Chargeback with CHARGEBACK webhook. It cannot be defended; late funds trigger CHARGEBACK_REVERSED. The capability table's recurring “See note” has no clear note on this captured page, so it does not supply a recurring implementation recipe.
