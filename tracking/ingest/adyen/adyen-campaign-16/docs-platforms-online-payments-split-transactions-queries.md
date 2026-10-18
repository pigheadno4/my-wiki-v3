# Fixed retrieval checks: docs-platforms-online-payments-split-transactions

## Q1 — Purpose, precedence and default

**Query:** What does the Platforms online split-transactions overview establish about store profiles, per-request splits and no-instruction booking?

**Expected answer:** The 2024-modified, 2026-09-15-captured overview describes booking online transaction amounts and fees among user balance accounts and the platform liable balance account. Store-linked automatic split configuration profiles can supply instructions; split instructions in an API request override the profile. If neither a profile nor a request supplies instructions, the entire transaction amount and fees book to the liable balance account. These rules do not establish the seller, merchant of record, legal fund ownership, a successful payment, or payout/bank receipt. Invalid account targets and account capabilities require the specific flow guides; the overview does not define those outcomes.

**Evidence locators:** `raw/adyen/docs/platforms/online-payments/split-transactions/2026-09-15.md:19-30`. **Canonical route:** `[[adyen]]` → `[[adyen-platforms]]` → `[[source-adyen-docs-platforms-online-payments-split-transactions]]` → pinned raw.

## Q2 — Timing, split fields and lifecycle boundaries

**Query:** When can online Platforms split instructions be supplied, what do `splits` and `platformChargebackLogic` do, and what limits or source caveats matter?

**Expected answer:** The page routes payment splits to Checkout `/payments` or `/sessions` at authorization, amount updates to `/payments/{paymentPspReference}/amountUpdates`, capture splits to `/payments/{paymentPspReference}/captures`, and refund splits to `/payments/{paymentPspReference}/refunds`. Capture-time splitting requires a payment method supporting separate captures. Payment/refund `splits` contain an object for each booked portion of the full amount, with purpose in `type` and type-dependent account, amount and reference requirements or recommendations. The table lists all three as required for `BalanceAccount`; the general statement that an omitted `account` books to liable must not turn a required user-account field into an optional one. Potential chargeback booking uses `platformChargebackLogic` in authorization or capture requests. The payment/refund/chargeback subject lists are orientation, not proof of product or account eligibility, executed movement or universal fee behavior. The refund tab's “marketplace's commission” wording does not establish MOR, and its raw line 102 capture link points to an in-person guide while the online capture route appears at lines 148–150.

**Evidence locators:** `raw/adyen/docs/platforms/online-payments/split-transactions/2026-09-15.md:39-53`, `:55-81`, `:83-116`, `:118-140`, `:142-154`. **Canonical route:** `[[adyen]]` → `[[adyen-platforms]]` → `[[source-adyen-docs-platforms-online-payments-split-transactions]]` → pinned raw.
