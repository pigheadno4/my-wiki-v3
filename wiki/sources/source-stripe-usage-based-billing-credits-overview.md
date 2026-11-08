---
title: "Stripe: Billing Credits (Overview)"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits"
raw_files:
  - "stripe-billing-subscriptions-usage-based-billing-credits-2026-11-07.md"
  - "stripe-usage-based-billing-credits-overview-2025.md"
tags: [stripe, billing, usage-based, credits, credit-grants, invoicing]
---

## Summary

Stripe describes Credit Grants for prepaid or promotional billing credits allocated to a customer for usage-based merchant offerings. The 2026-05-05 capture labels the feature **Public preview**; the 2026-11-07 capture omits that banner. Omission does not establish general availability or eligibility for an account. Both captures retain the same core eligibility, finalization, priority, ledger, and 100-unused-grant rules. The November capture also renders the customer → Meter events → meter/price → invoice and Credit Grant → invoice relationship as text, where the old capture had no diagram rendering. See [[stripe-usage-based-billing]] and [[stripe]].

## Approved and prohibited use

The guide permits free or paid credits for memberships, pay-as-you-go plans, subscriptions, or specific products and services offered by the merchant. It prohibits gift cards or gift certificates, stored value **not intended for those approved merchant offerings**, payments to third parties, and digital-wallet linking. The older source phrase “stored value for non-subscription spending” was too narrow: the approved list includes merchant products and services beyond subscriptions.

## Grant states

| State | Captured meaning |
| --- | --- |
| Pending | Available balance is not yet usable |
| Granted | Eligible based on `effective_at`; omitted `effective_at` makes the grant effective immediately |
| Depleted | Balance fully used |
| Expired | Reached `expires_at` or manually expired; credits do not expire without this field unless manually expired |
| Voided | Only grants never applied to an invoice can be voided; voided grants cannot apply to future invoices |

> [!warning] Contradiction
> Both captures' Granted row says `effective_at` “must occur in the future” and also says omitting it makes the grant effective immediately (new line 48; old line 40). This page does not resolve exact timestamp validation, so do not infer a universal future-only requirement.

## Eligibility and application

A grant applies only when the invoice `period_end` is on or after `effective_at`, before `expires_at` if set, the grant has available balance **at invoice finalization**, and currency matches. Eligible charges must be subscription items using metered prices with usage reported through **Meters**. One-off invoices, one-time setup items, licensed-price items, and metered items using legacy Usage Records are excluded. Price-level applicability can further restrict a grant to specified metered prices.

Credits apply **after discounts**, but before taxes and `invoice_credit_balance`. Across invoices, the first invoice to finalize uses credits first; independently finalized subscription invoices have no guaranteed order. Within an invoice, line order controls. Among multiple applicable grants, use priority (lower number first), earlier expiry, promotional category, earlier effective date, then earlier creation date. A credit shown on a preview or draft is provisional; application occurs at finalization and another invoice can consume the grant first. This can change threshold timing. Finalization and credit application do not prove customer payment settlement.

## Ledger, available balance, and unused-grant cap

The Credit Balance Summary has two different amounts. **Ledger balance** reflects the sum after recorded credit and debit transactions; the grant is backed by an immutable, append-only **ledger**, but the **balance changes** as transactions are appended. **Available balance** is the amount currently usable, described as ledger balance less expired credits or unrecorded transactions.

A customer can have up to **100 unused Credit Grants**; a further grant request fails at that limit. A grant counts while it is neither voided nor expired and is either pending before `effective_at` **or** has a positive ledger balance. A zero available balance with a positive ledger balance still counts, including when credits appear on a draft invoice. It stops counting when credits applied to a finalized invoice **deplete its ledger balance to zero**, or when the grant expires or is voided. Merely finalizing an invoice does not stop the count if its ledger balance remains positive.

## Voids and Credit Notes

Voiding an invoice reinstates applied credits to the grant, but reinstated credits expire immediately if the grant is past `expires_at`. A Credit Note does **not** reinstate those credits; the guide says to create a new grant to restore them. Neither capture documents that any particular grant, invoice, credit transaction, refund, or payment occurred.

## Related pages

- [[stripe-usage-based-billing]] — usage-based billing concept
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-billing-subscriptions-usage-based-billing-credits-2026-11-07|Billing credits guide, captured 2026-11-07]] — full current assigned capture (145 lines)
- [[raw/stripe-usage-based-billing-credits-overview-2025|Billing credits guide, captured 2026-05-05]] — historical raw; reformatted from plain-text paste as documented by its prior source entry
