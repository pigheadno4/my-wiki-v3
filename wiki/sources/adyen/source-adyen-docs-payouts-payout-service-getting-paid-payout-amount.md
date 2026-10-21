---
title: "Adyen Payout Service available payout amount calculation"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/getting-paid/payout-amount"
raw_files:
  - "adyen/docs/payouts/payout-service/getting-paid/payout-amount/2026-09-15.md"
tags: [adyen, payout-service, payouts, balance-platform, available-balance]
---

## Overview

This 2026-09-15 Payout Service guide explains how Adyen considers a balance account's existing balance and future-dated debits/credits before determining an amount available to pay out. It is a balance-calculation explanation, not a payout request, source-debit, bank-credit or live eligibility record. A material arithmetic wording conflict in its negative-future-change case is unresolved. [[adyen]] [[adyen-payouts]]

## Key takeaways

- Adyen says it verifies the **available balance** before a payout to account for potential obligations from a negative balance. The existing balance is the balance as of the calculation day, including amounts with value dates through that day. “Future balance changes” are future-value-date debits and credits already booked by the calculation day. See raw lines 17-24.
- Only a **negative total** of expected future debits/credits changes the available-balance calculation; zero or positive totals are ignored. The page's negative example uses USD 100 existing balance and future changes of USD −50 plus USD +30, yielding a net USD −20 and stated available USD 80. Zero and positive examples both retain USD 100. See raw lines 26-63.
- **Unresolved arithmetic conflict:** raw line 26 says available balance is existing balance “minus future balance changes” when that future total is negative. Literal subtraction of USD −20 from USD 100 yields USD 120, whereas the page's worked example says USD 80 at raw lines 38-41. The example corresponds to reducing the existing balance by the magnitude of the negative net, but this source does not resolve the prose formula. Do not automate the literal wording or infer a verified payout ceiling without checking the applicable balance/API behavior.
- The guide links separate scheduled- and on-demand-payout procedures. Its examples do not show a request, approval, transfer status, booking, settlement or beneficiary-bank receipt. See raw lines 65-68.

## Detail locators

- `# Calculating the payout amount`, raw lines 15-30: purpose, existing balance, future-change date criteria, negative-only inclusion and ambiguous “minus” wording.
- `### Example 1`, raw lines 34-41: USD 100 plus future USD −20 net produces the stated USD 80 available balance, conflicting with literal subtraction of the negative total.
- `### Example 2` and `### Example 3`, raw lines 45-63: zero/positive future totals ignored; available balance remains USD 100.
- `## See also`, raw lines 65-68: separately routed scheduled and on-demand payouts.

## Related

- [[adyen-payouts]] — Payout Service and distinct legacy Online Payout API context.
- [[adyen-financial-products]] — modern payout product-family context.
- [[source-adyen-docs-payouts-payout-service-getting-paid-on-demand-payouts]] — separate request and lifecycle route.
- [[source-adyen-docs-payouts-payout-service-getting-paid-scheduled-payouts]] — separate scheduled payout route.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/getting-paid/payout-amount/2026-09-15|Adyen Payout Service payout-amount guide, captured 2026-09-15]]
