# Fixed retrieval checks: docs-platforms-managed-payouts

## Q1 — Purpose, scope and financial boundary

**Query:** What are Adyen for Platforms managed payouts, who configures them, and what should not be inferred from a schedule?

**Expected answer:** The 2022-modified, 2026-09-15-captured Platforms overview describes automatic payouts to users on a balance platform through managed schedules. With an Adyen contact's help, a platform creates a schedule for balance accounts sharing a location and currency, taking desired receipt time, user sales-day closing time and time zone into account. This is a Platforms balance-account payout route, separate from the legacy Payout API. A configured schedule, advertised timing or example bank statement description does not prove that payments have settled, a payout executed, a recipient bank credited funds, or who legally owns a particular payment.

**Evidence locators:** `raw/adyen/docs/platforms/managed-payouts/2026-09-15.md:15-25`, `:39-49`, `:51-75`. **Canonical route:** `[[adyen]]` → `[[adyen-platforms]]` → `[[source-adyen-docs-platforms-managed-payouts]]` → pinned raw.

## Q2 — Schedule limits, settlement and timing warnings

**Query:** What location, currency, balance-account, settlement and timing constraints govern managed payout schedules?

**Expected answer:** Only one managed schedule per currency can apply to a balance account; each schedule supports one location and currency. Managed schedules handle local payouts within the same country and currency. A different payout currency or bank account in another country is routed to custom payouts. Managed schedules do not change pass-through settlement or sales-day settlement delays of T+7 or more; those funds can pay out once settled. The page describes Standard as two days and Accelerated as one day after settlement, plus weekday, weekly or monthly frequencies. Weekly/monthly payouts include funds only up to one or two days before the chosen payout date. Payout arrival time is an estimate constrained by local/currency cutoffs and Adyen contract terms, while minimum/maximum amounts and retained balance may constrain payout amount. The US example's USD 200 minimum, USD 100 retention and 9 AM local ETA are illustrative. This overview points to use/execution pages but does not document failure, return or beneficiary-bank confirmation.

**Evidence locators:** `raw/adyen/docs/platforms/managed-payouts/2026-09-15.md:27-49`, `:51-75`, `:77-102`. **Canonical route:** `[[adyen]]` → `[[adyen-platforms]]` → `[[source-adyen-docs-platforms-managed-payouts]]` → pinned raw.
