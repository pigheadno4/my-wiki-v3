---
title: "Adyen Review-page Checkout"
type: concept
category: technology
tags: [adyen, checkout, web-sdk, sessions, payment-actions]
---

## Definition and version boundary

In `@adyen/adyen-web@6.45.0`, the opt-in `onReview` callback separates valid payment-data collection from final submission. A merchant can present an order-review screen before paying. This is SDK orchestration, not a guarantee of payment-method availability or authorization. Earlier version knowledge remains in [[source-github-adyen-web]] and [[changelog-github-adyen-web]].

## Lifecycle

> [!warning] Version warning
> Adyen marks `@adyen/adyen-web@6.45.1` **do not use** because of a payment-action handling bug and directs users to 6.45.2. This warning applies beyond review-page checkout; do not interpret the established 6.45.0 lifecycle as proof that 6.45.1 action mounting works. See [[source-github-adyen-web]] and [[changelog-github-adyen-web]].

The retained 6.45.2 release reports a payment-action mounting fix by reverting the BaseElement/UIElement refactor. Its complete supplemental UIElement implementation is byte-identical to the retained 6.45.0 implementation, restoring status-prop forwarding while preserving the review lifecycle below. Core implementation is also unchanged versus the 6.45.0 snapshot. This is code/release-note evidence, not a reproduced browser or payment result; merchant action ownership and recovery responsibilities remain.

1. A supported Component validates on submit. With `onReview`, it supplies payment data, the Component, and optional order status, then returns without executing its normal payment call.
2. The merchant retains the data and displays a review screen. Card end digits in the retained story are captured separately through `onFieldValid`, not automatically included in review details.
3. For Sessions, `checkout.processPayment(data)` submits through the Session without needing the original payment Component. It returns `void`; completion is callback-driven. Advanced integrations continue their own backend payment flow instead.
4. `onAction` receives a created action Component for merchant mounting. The merchant owns its container and cleanup. Remaining partial-payment balances invoke `onOrderUpdated`; terminal results invoke completion/failure callbacks.

`processPayment` does not repeat Component validity checks or `beforeSubmit` transformations, and has no local in-flight submission guard. Preserve those responsibilities deliberately, handle stale data, disable duplicate confirmation, and implement error/partial-payment recovery. This is not evidence that server-side idempotency is absent.

## Payment-method boundaries

- Card, Bacs Direct Debit, stored PayByBankUS, stored PayTo, and Twint wire the internal review button presentation. The primary label becomes Continue; this is not a universal public `showReview` option.
- Google Pay and Klarna widget execution bypass the normal review submit path. Klarna without its widget uses the inherited path.
- Gift cards can execute partial-balance payment before final review; a sufficient-balance confirmation can enter review. Initial Redeem is not a review button.
- Retained documentation additionally excludes Apple Pay, Amazon Pay, PayPal, and ANCV. Their complete implementations were not retained in this supplement, so those exclusions are documented rather than independently code-verified here.
- PayByBankPix needs branch-level qualification: the hosted stored-payment path bypasses review, while the merchant-page redirect branch still uses inherited submit.

## Documentation discrepancies

> [!warning] Contradiction
> At the exact 6.45.0 SHA, ADR-0004 says `askDonation` needs a type cast, but both retained response types include it. ADR-0003 describes `core.update` with the remaining-order callback, but `processPayment` only calls `onOrderUpdated`. The broad PayByBankPix exclusion also differs from its branch-specific implementation. For these details use the retained code, not the ADR shorthand; immutable documents remain unchanged.

## Integration and evidence limits

The Card and Drop-in stories demonstrate a two-screen Sessions flow and action modal. They are not production templates: the review screen prints the complete payment payload, lacks complete error/order recovery and cleanup, and does not close its modal on every failure. Do not copy its payload display into production.

Configuring `onAction` also changes ordinary mounted UIElement response handling even without `onReview`; it is not merely an observer. Donation presentation after `processPayment` is merchant-owned, using returned donation eligibility rather than assuming automatic setup.

No browser, payment, upstream test, or delegated wallet runtime verification was performed. Current merchant eligibility remains outside repository evidence.

## Sources and related

- [[source-github-adyen-web]] - exact-SHA implementation links and grounding excerpts
- [[changelog-github-adyen-web]] - 6.44.0 to 6.45.0 changes and preserved history
- [[adyen]] - company and independent SDK boundaries
