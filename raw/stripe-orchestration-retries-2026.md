<!-- Source URL: https://docs.stripe.com/payments/orchestration/retries -->
<!-- Fetched: 2026-05-11 -->

# Cross-processor retries with Orchestration

Retry failed payments using a different processor than the one that submitted the original attempt.

Payments can fail for various reasons such as network issues, processor outages, or temporary declines (for example, insufficient funds). Many of these failures are recoverable. With Orchestration, you can automatically retry failed payments using a different processor than the one that submitted the original attempt, helping you to recover more revenue.

## Set up payment retries in the Dashboard

To configure payment retries:

1. Navigate to Payments > Orchestration > [Rules](https://dashboard.stripe.com/orchestration/rules).

1. Create new rules or open existing rules. If you’re making changes to existing rules, you must [duplicate](https://docs.stripe.com/payments/orchestration/rules.md#duplicate-rules) it and then edit the draft of your duplicated rules.

1. In the rule builder, add an `Action` to configure retry behavior:
   - **Main processor**: The processor to use for the initial payment attempt.
   - **Retry processor**: The processor to use if the initial attempt fails.

This setup enables retries of failed payments, and improves the likelihood of successful processing.

## Cross-processor retry behavior

When a payment fails on the main processor, the retry logic depends on several factors:

- **3D Secure**: If 3D Secure (3DS) authentication is attempted on the first attempt on your main processor and your customer doesn’t authenticate successfully, or authenticates successfully but the payment attempt still fails, Orchestration doesn’t retry the transaction on the retry processor. We send a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) webhook event instead.

- [Ineligible features](https://docs.stripe.com/payments/orchestration/feature-support.md): If a payment uses a feature that isn’t supported by the retry processor, such as the `on_behalf_of` parameter with Stripe Connect, Orchestration won’t retry with that processor after the first failure.

- **Blocked transactions**: If Stripe is your main processor and we block a transaction (for example, a high-risk payment identified by Radar), Orchestration treats this as a decline and retries the payment on your chosen retry processor.

- **Adaptive Acceptance**: If you have Adaptive Acceptance enabled and Stripe is your main processor, Stripe might initiate an additional retry on a declined transaction, before triggering a cross-processor retry. If Stripe is your retry processor, Stripe might ultimately initiate two retries, one as a cross-processor retry and the other under Adaptive Acceptance.

## Join the private preview

> #### Want access to Orchestration?
>
> Orchestration is in private preview.
