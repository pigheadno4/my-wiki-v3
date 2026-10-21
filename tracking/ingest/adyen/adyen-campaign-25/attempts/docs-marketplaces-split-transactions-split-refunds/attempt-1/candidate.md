---
title: "Adyen Marketplaces: Split refunds"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/split-transactions/split-refunds"
raw_files:
  - "adyen/docs/marketplaces/split-transactions/split-refunds/2026-09-15.md"
tags: [adyen, marketplaces, platforms, refunds, split-transactions]
---

## Overview

This 2026-09-15 Marketplace-path guide explains how a platform requests a refund of a captured payment and allocates deductions across its users' and its own liable balance accounts with refund split instructions. The split determines which credited party bears the refund; the request and test examples are not proof that the refund or balance movements completed. This is an Adyen for Platforms balance-account flow, separate from Classic Platforms. [[adyen]] [[adyen-platforms]] (raw lines 15–19, 35–39)

## Key takeaways

- The platform needs Checkout API credentials, standard-webhook handling and a subscription to transfer or transaction webhooks. Some payment methods do not support partial refunds; the guide limits refund deductions to balance accounts credited by the payment and says to reuse the original split's `pspReference` values. The outcome of the refund request arrives asynchronously in a `REFUND` webhook. (raw lines 21–33, 789)
- Use the original payment PSP reference in `POST /payments/{paymentPspReference}/refunds`. The request includes `amount` and `merchantAccount`; refund value must equal or, for a partial refund, be below the captured amount, and the top-level refund currency must match payment authorization. A refund `reference` is optional. The guide strongly recommends explicit `splits` for every partial refund; it does not specify a no-splits partial-refund allocation rule. (raw lines 35–51)
- For explicit splits, `account` identifies the user's or platform's balance account to debit, `amount.value` gives that split's deduction, and `type` selects the leg. `BalanceAccount` debits the specified balance account; `Commission` reverses the original platform commission against the liable balance account; fee types and an FX `Remainder` have separate meanings. `reference` is conditionally required for `BalanceAccount`; `amount.currency` is conditionally required when the split refund is in a different currency. The page's top-level currency-matching rule and split-level conditional currency instruction should be read at their own scopes rather than treated as interchangeable. (raw lines 55–68)
- For a **full** refund without `splits`, the deduction follows the original payment **authorization** split ratio, not the capture split. That path assumes the authorization contained splits; if it did not, the full refund is debited from the marketplace's liable balance account. This page does not extend that fallback rule to a partial refund. (raw lines 511–521)
- The API request validates split formatting, **not** whether target balance accounts exist or remain usable. Even if the request succeeds, a nonexistent target or one linked to a closed account holder causes the full transaction and its fees to be booked to the marketplace's liable balance account. The guide routes balance correction to a separate internal fund transfer. Request acceptance is therefore not destination-booking proof. (raw lines 791–795)
- Track each refund split separately: `balancePlatform.transfer.created` with outgoing/`received`, then transfer updates such as `authorised` and `refunded`, and a `balancePlatform.transaction.created` booking event. The page says to acknowledge each webhook and describes cumulative prior events and `sequenceNumber` in transfer updates. The illustrated user-sale, transaction-fee and platform-commission legs are TEST samples with different balance-account liabilities; the first transfer status is not final booking or customer receipt. (raw lines 797–815, 819–834, 902–904, 986–989, 1087–1089, 1134–1151, 1451–1468, 1620–1623, 1721–1723)
- **Sample reconciliation caution:** The transaction-fee transfer sample uses transfer ID `8KREG78BWDNEKXHW` and balance account `BA...0002`, but its transaction-created sample uses transfer ID `3JERI65VWKBRFIVB` and account `BA...0001`. The commission transfer sample uses transfer ID `7JHRI65VWKBRFPMG` and the liable account `BA...0003`, while its transaction-created sample again uses `3JERI65VWKBRFIVB` and `BA...0001`. Treat those identifiers as inconsistent illustrative data, not a join rule. (raw lines 1167–1171, 1205, 1419–1443, 1484–1487, 1522, 1736–1760)

## Detail locators

- Raw lines 70–509: explicit-split refund examples in Checkout v72/test and version-labeled Java/PHP/.NET/Node/Go/Python/Ruby SDKs; example USD 80.00 refund allocates 4.00 commission and 76.00 user balance deduction. Raw lines 523–787: full-refund examples without split instructions.
- Raw lines 819–1132: outgoing user sale-amount transfer and booking example; lines 1134–1449: transaction-fee leg; lines 1451–1766: platform commission leg. `pspPaymentReference` identifies the associated payment and `modificationPspReference` the refund in the example transfer metadata (raw lines 823–828, 1140–1145, 1457–1462).
- Raw lines 1768–1781: optional FX `Remainder` booking to a selected balance account; the linked currency-conversion guide owns the fuller conversion procedure.

## Related

- [[adyen-platforms]] — parent Adyen for Platforms context.
- [[source-adyen-docs-platforms-online-payments-split-transactions-split-refunds]] — parallel Platforms-path refund guide; use this page's pinned Marketplace-path evidence for the claims above.
- [[adyen-platform-internal-transfers]] — separate balance-correction transfer route.
- [[adyen-currencies-and-fx]] — FX context for the `Remainder` route.

## Raw Sources

- [[raw/adyen/docs/marketplaces/split-transactions/split-refunds/2026-09-15|Marketplace split refunds, captured 2026-09-15]]
