# Fixed queries — docs-account-sales-day-payout

## Q1 — Purpose, scope, and what must not be inferred

**Answer:** Adyen Sales day payout groups a merchant account's sales-day funds into a payable batch after a delay, independent of the individual shopper payment methods' settlement timelines. The snapshot calls it the default payout model but says only Pass-through payout is available in Africa, Brazil, and Turkey; use is subject to Sales day payout Terms of Service. The model and its schedule examples do not prove a specific merchant's eligibility, final payable amount, payout instruction execution, or bank receipt. This is merchant settlement, not the legacy outbound Payout API.

**Raw locators:** lines 19–29 (model, Terms, default and regional exception); lines 35–51 (assignment, frequency and adjustments); lines 124–132 (batch close, instruction and holidays).

**Canonical route:** [[adyen-index]] → [[adyen-sales-day-payout]] → [[source-adyen-docs-account-sales-day-payout]] → [[raw/adyen/docs/account/sales-day-payout/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Answer:** Sales from a merchant-local sales day are assigned to a payable batch after a configured delay. Daily is the default payout frequency, while changing frequency can group multiple sales days. The sales day defaults to local midnight-to-midnight, with a configurable later fixed close as late as 6:00 AM. The page says a payable batch closes two hours after the sales-day close; Adyen then creates a bank instruction and conditionally starts an automatically configured Settlement details report. It also says batches close according to payout frequency, so the exact close for non-daily schedules should not be inferred from the daily example. Delay depends on settlement mix, currency, acquiring region and possibly partner setup; bank holidays may extend it. Acceleration is limited by merchant location and Adyen review, with unsupported currency or payment-method mix among refusal reasons. Refunds, chargebacks and capture shortfalls alter the current payable batch. Assignment or instruction creation is not proof of money arriving at a bank.

**Raw locators:** lines 37–43 (assignment and frequency); 45–51 (adjustments); 53–88 (delay, example schedule, currency/acquiring/method and partner conditions); 90–114 (accelerated review); 116–128 (cutoff, batch close and instruction); 130–143 (holidays).

**Canonical route:** [[adyen-index]] → [[adyen-sales-day-payout]] → [[source-adyen-docs-account-sales-day-payout]]; full conditions at [[raw/adyen/docs/account/sales-day-payout/2026-09-15]].
