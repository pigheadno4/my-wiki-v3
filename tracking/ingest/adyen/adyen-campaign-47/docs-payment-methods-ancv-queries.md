# ANCV overview worker retrieval queries

## Q1 — Identity, roles and scope

**Query:** What is ANCV in Adyen's payment-method documentation, and who contracts and handles settlement/reporting?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ancv.md` → `raw/adyen/docs/payment-methods/ancv/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/ancv`; full pinned raw `raw/adyen/docs/payment-methods/ancv/2026-09-15.md`, `# ANCV` lines 15–25 and capability table lines 27–29. Preserve French holiday-voucher, FR/EUR, direct ANCV merchant contract, Adyen gateway role, and ANCV settlement/reporting. The snapshot proves neither merchant enablement nor an operational payment.

## Q2 — Partial-payment rule and capability qualifications

**Query:** How does ANCV partial authorization work, which response supplies orderData, and how should the capture/refund matrix be read?

**Expected route:** Same root → Adyen index → online-payments concept → ANCV source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path: capability table lines 27–29, one-partial-capture statement line 31, `## Partial payments` lines 33–39, and `## How do you want to integrate?` lines 41–53. Merchant handling of a lower shopper authorization requires partial payments and `orderData` from `/payments/details`, not `/payments`. The matrix marks multiple partial captures available, but the prose permits only one partial capture per payment; retain both as an unresolved source conflict. Refunds are marked available with “See note,” but no clear note appears in this captured page; follow method-specific details. Web and API-only are routes, not complete recipes.
