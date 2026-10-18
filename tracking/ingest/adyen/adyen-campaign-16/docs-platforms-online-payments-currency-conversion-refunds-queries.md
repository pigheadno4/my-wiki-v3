# Fixed retrieval checks: docs-platforms-online-payments-currency-conversion-refunds

## Q1 — Pilot scope and refund currencies

**Query:** What does the Platforms refund currency-conversion overview say about pilot availability, the customer's refund currency, the user's debit currency and conversion cost?

**Expected answer:** The 2023-modified, 2026-09-15-captured page describes a limited-availability pilot whose process and documentation may change; current enrollment is not established. It says a refund can exchange currencies again so the customer receives the refund in the original payment's processing currency. Its PLN/CZK example debits the user in the settlement currency CZK and credits the customer in processing currency PLN. Adyen says the conversion uses the prevailing exchange rate plus a conversion markup. The illustrative amounts are not a guaranteed refund amount or rate, and the overview does not prove a completed refund or bank receipt.

**Evidence locators:** `raw/adyen/docs/platforms/online-payments/currency-conversion/refunds/2026-09-15.md:19-26`. **Canonical route:** `[[adyen]]` → `[[adyen-currencies-and-fx]]` → `[[source-adyen-docs-platforms-online-payments-currency-conversion-refunds]]` → pinned raw.

## Q2 — Remainder, destination and source conflict

**Query:** Why can an FX refund have a remainder, how can it be booked, and what ambiguity should a reader avoid?

**Expected answer:** Moving exchange rates and Adyen's markup can make the reconverted settlement-currency refund unequal to what the customer originally paid in processing currency. The difference is the remainder; the page says a same-day refund remainder is usually, not always, negative. A refund request can include a `Remainder` split item to book it to the user or platform. If no booking instruction is supplied, it books to the platform's liable balance account. Adyen recommends including the split for per-transaction Balance Platform Accounting Report reconciliation, but this is advice rather than a stated mandatory field. The next-step label “Your platform” conflicts with its line-46 description “to the customer”; the body supports user/platform remainder routes and gives no third customer-destination rule. The child guides provide implementation details; do not import them into this overview.

**Evidence locators:** `raw/adyen/docs/platforms/online-payments/currency-conversion/refunds/2026-09-15.md:28-34`, `:36-46`. **Canonical route:** `[[adyen]]` → `[[adyen-currencies-and-fx]]` → `[[source-adyen-docs-platforms-online-payments-currency-conversion-refunds]]` → pinned raw.
