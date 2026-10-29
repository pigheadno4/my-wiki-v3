# Riverty overview worker retrieval queries

## Q1 — Purpose and scope

**Query:** What is Riverty in this Adyen overview, and what merchant funding/risk boundaries does it state?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-riverty.md` → `raw/adyen/docs/payment-methods/riverty/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/riverty`; full pinned raw `raw/adyen/docs/payment-methods/riverty/2026-09-15.md`, `# Riverty` lines 15–23. Riverty is described as invoice BNPL, with shopper liability/credit risk and reminders/debt collection assigned to Riverty, disputes handled with merchants, T+2 settlement and no sales day payout. The prose's “immediately settled in full” does not establish instant fund arrival, actual payout, current merchant enablement or payment execution.

## Q2 — Central method scope and conditions

**Query:** Which Riverty shopper options, countries/currencies and feature marks are in the captured overview, and what option has a narrower country limit?

**Expected route:** Same root → Adyen index → online-payments concept → Riverty overview source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path, `# Riverty` lines 25–34 and `## How do you want to integrate?` lines 36–48. The page lists 14-day payment, monthly invoice, secure direct debit and split installments; split installments are only stated for Germany, Austria and Netherlands. The Direct-flow matrix lists DE/AT/CH/NL/BE and EUR/CHF, with recurring marked unsupported and refund/capture/chargeback marks supported. These matrix marks are snapshot labels, not per-country currency-option mappings, current eligibility or modification outcomes.

Final cross-page qualifier (approved counterpart warning): the overview matrix labels flow Direct (raw 32–34), while the Web Component child requires redirect handling and subtype (child raw 33–35, 371–372, 494–495). The final source links [[source-adyen-docs-payment-methods-riverty-web-component]] and warns against inferring no redirect from the overview label.
