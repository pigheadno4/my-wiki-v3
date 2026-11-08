---
title: "Stripe — Coupons and Promotion Codes for Subscriptions"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/coupons"
raw_files:
  - "stripe-billing-subscriptions-coupons-2026-11-07.md"
  - "stripe-subscriptions-coupons-2026.md"
tags: [stripe, subscriptions, coupons, promotion-codes, discounts, stackable]
---

## Summary

Stripe's subscription-discount guide distinguishes coupons, which define a discount and can be applied by a backend, from customer-facing promotion codes that reference a coupon and inherit its product restrictions. Redeeming creates a Stripe `Discount` object. The guide covers duration, redemption and eligibility, Checkout and customer-portal paths, stacking, and subscription updates (old lines 8–25, 474–587; new lines 9–39, 430–503).

The 2026-11-07 capture explicitly states up to **20 discounts on a subscription, subscription item, or invoice**, shared between coupon and promotion-code applications (new line 24). The May stacking section said up to 20 entries in a `discounts` parameter (old lines 563–571). Neither passage establishes one combined 20-discount budget across all three objects.

## Coupon creation, scope, and duration

Only a coupon's **name** can be edited after creation. `applies_to` can restrict eligible products; associated promotion codes inherit those product restrictions. If no subscription product matches, adding the coupon yields no discount. Existing discounts are reflected in subscription-change prorations, but proration line items cannot be further discounted on the generated invoice (old lines 39–95; new lines 53–109).

- `duration=once` applies to the first invoice and is the stated **default** in the November capture. After that invoice finalizes, the subscription's `discounts` array no longer includes the consumed discount, while the invoice retains it (new lines 193–205).
- `duration=repeating` uses `duration_in_months`; `duration=forever` continues indefinitely. A backdated subscription counts coupon duration from the backdated start, so an elapsed backdated period can consume repeating duration (old lines 215–229; new lines 193–207).

The May capture already described `once` consumption at finalization and also used “finalized or paid” in a later explanatory bullet (old lines 221–227). The November finalization wording does not itself prove a changed runtime transition. The slightly different yearly repeating examples (old line 217; new line 197) do not establish a semantic change.

Deleting a coupon prevents new application to subscriptions or invoices, but does not remove discounts already present (old line 195; new line 176). November's coupon-versus-code table adds that deletion archives associated promotion codes (new line 33). A code whose underlying coupon becomes invalid is permanently inactive, as are codes that expire or reach their own max redemption count (old lines 398–402; new lines 378–382).

## Redemption limits

`max_redemptions` caps coupon redemptions across all customers. The November guide explicitly says both direct coupon application and customer redemption of a promotion code consume the **same underlying coupon** counter (new lines 209–215). The May guide described the aggregate coupon limit without that explicit code-counting sentence (old lines 231–235). A coupon's expiration blocks new applications, but does not end an already-applied `forever` discount (old line 235; new line 215).

## Promotion-code controls

A promotion code is a customer-facing wrapper around a coupon; multiple codes may reference one coupon. Code strings are case-insensitive. **Distinct customer-restricted active codes may reuse the same string**, but an active code redeemable by any customer cannot share that string with another active code. An inactivated code string can be reused (old lines 265–281; new lines 245–261).

Promotion-code-only controls include restriction to a particular customer, first-time transaction, minimum amount, expiration, and max redemption count (new lines 26–33, 287–364). The first-time restriction excludes customers who initiated a PaymentIntent even if it failed, or subscribed to a trial even if canceled (old lines 329–342; new lines 309–322). Minimum amount is checked **at redemption**, so for a subscription it applies to the initial payment, not every renewal (old lines 344–356; new lines 324–336). Do not generalize these code restrictions to directly applied coupons.

A promotion code with amount restrictions cannot be applied to subscription items, invoice items, subscription updates, or future subscription-schedule phases (old lines 249–257; new lines 229–237). A code's expiration cannot be later than its parent coupon's expiration, and its max redemption limit cannot exceed the parent's (old lines 358–384; new lines 338–364).

## Applying discounts and account variants

Coupons can be applied to a subscription on creation or update; Checkout subscription mode accepts a coupon in `discounts`. Promotion codes can be applied on subscription creation or update by first resolving the entered code to a PromotionCode ID; Checkout can show a code-entry box with `allow_promotion_codes` (old lines 97–189, 404–469; new lines 111–170, 384–425).

Accounts v2 examples use `customer_account`; Customers v1 examples use `customer`. The guide says Accounts v2 is generally available for Connect users and in public preview for other users, with a preview version needed by preview participants. November adds a Dashboard preview-enablement instruction. These are documented paths, not proof that a particular account has access (old lines 112–162, 285–303; new lines 126–152, 265–283).

The May capture renders coupon, subscription, and Checkout examples in Node SDK form (old lines 56–66, 112–189, 423–465). November renders corresponding examples in curl (new lines 70–76, 126–170, 403–421). The rendering change is not evidence of Node SDK deprecation.

## Customer portal and stacking

With promotion codes enabled in the customer portal, customers can apply codes while changing subscriptions. **A promotion-code update can succeed even if an associated price upgrade fails due to a payment failure**, because the updates are applied separately (old lines 241–245; new lines 221–225).

Discounts can be stacked on subscriptions and subscription items. Order matters when `percent_off` and `amount_off` are mixed (old lines 474–483; new lines 430–439). Stacking restrictions include unique entries, no coupon paired with its derived promotion code or derived Discount, and redeemed Discount objects already attached to the updated customer or subscription (old lines 563–571; new lines 479–487).

When updating `discounts`, include all existing coupon, code, and Discount entries to keep; omit an existing entry to remove it. `discounts=""` clears all subscription discounts, after which a customer-level discount can apply to invoices. After multiple discounts are set, the deprecated scalar `coupon` or `promotion_code` update parameters cannot be used as described for subscriptions or schedule phases (old lines 573–581; new lines 489–497).

**Discount-only updates do not create prorations or an invoice.** A separate billable current-cycle change can trigger prorations; when combined in one call, Stripe calculates that proration using the updated pricing and discount state (old lines 583–587; new lines 499–503). The discount update is not itself the proration trigger.

## Other discount routes and scripts

The guide also lists negative customer balance, negative invoice items, and a cheaper second Price as alternative discount methods (old lines 589–597; new lines 505–513).

The November page links to [Stripe-authored discount calculation scripts](https://docs.stripe.com/billing/scripts/stripe-authored/discount-calculation.md) and [self-authored discount calculation scripts](https://docs.stripe.com/billing/scripts/discount-calculation.md) (new lines 91–93). Those links are navigation to separate authority; this capture does not specify script rules, account eligibility, or execution outcomes.

## Related pages

- [[stripe-subscriptions-coupons]] — concept route
- [[stripe-subscriptions]] — subscription context
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-billing-subscriptions-coupons-2026-11-07|2026-11-07 coupons guide capture]]
- [[raw/stripe-subscriptions-coupons-2026|2026-05-13 coupons guide capture]]
