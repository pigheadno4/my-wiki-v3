# Cashout webhooks — retrieval checks

## Q1 — purpose, scope, and non-inference

**Query:** What does Adyen's Platforms “Webhooks for cashouts” page document? Does a cashout transfer reaching `received`, `authorised`, or `booked` prove that the user's bank received an instant payout?

**Expected retrieval:** The source is a dated Platforms balance-platform webhook guide for a platform user's cashout. It distinguishes incoming cashout funding, conditional fee debit, conditional bank payout to the user's transfer instrument, and later cashout repayment of the advance when the original sales funds settle. `balancePlatform.transfer.created`, `balancePlatform.transfer.updated`, and `balancePlatform.transaction.created` describe balance-account transfers and debits/credits. For the optional bank payout, the example separately shows `tracking.status: credited` after `booked`; booked balance-account debit is not that tracking event. Even example tracking is not independent proof of beneficiary-bank receipt or current account eligibility. Do not route this to legacy Online Payouts Payout API or POS card cashout.

**Raw locators:** lines 19–30 (scope, legs, webhook kinds); 82–115 (test sales/request scenario); 701–1126 (optional bank payout, booked debit, transaction, later credited tracking); 1128–1132 (repayment timing).

**Canonical route:** [[adyen-platforms]] → [[source-adyen-docs-platforms-cash-out-instantly-cashout-webhooks]] → [[raw/adyen/docs/platforms/cash-out-instantly/cashout-webhooks/2026-09-15]].

## Q2 — capability, prerequisites, and warnings

**Query:** How should a platform identify and monitor the cashout legs, and what must it set up before receiving these webhooks? Which example details should not become a general payout-state or bank-receipt guarantee?

**Expected retrieval:** Configure a server that receives and accepts webhooks, and subscribe to Transfer and Transaction webhooks in Customer Area. Identify each transfer by `category`, `direction`, and `type`: funding `internal/incoming/cashoutFunding`; fee `internal/outgoing/cashoutFee`; payout `bank/outgoing/bankTransfer`; repayment `internal/outgoing/cashoutRepayment`. The fee and payout legs are conditional on the cashout request. The example's payout includes `categoryData.priority: instant`, but its EUR amounts, dates, IDs and timing are test data. Received, authorised and booked are distinct stages; the payout sample has a later credited tracking update. This page gives no failed/returned/retry path. For repayment timing, the opening says the transfer is triggered on the originally scheduled settlement date (line 24), while the detailed section says the transfer request is created on cashout day and the amount deducted at settlement (line 1130); do not infer a universal creation or trigger time. Its repayment prose names updated events while two sample envelopes still say `balancePlatform.transfer.created` and `status: received`; the fee narrative names a liable account while the booked example carries a `CashOutFunding` counterparty. Preserve those conflicts and consult actual operation evidence.

**Raw locators:** lines 19–37 (legs, opening repayment timing and subscription); 43–74 (identifier table); 409–700 (fee and counterparty example); 701–1126 (conditional bank payout and tracking); 1128–1381 (repayment timing narrative and conflicting sample fields).

**Canonical route:** [[adyen-webhooks]] and [[adyen-platforms]] → [[source-adyen-docs-platforms-cash-out-instantly-cashout-webhooks]] → [[raw/adyen/docs/platforms/cash-out-instantly/cashout-webhooks/2026-09-15]].
