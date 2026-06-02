<!-- Source URL: https://docs.stripe.com/payments/orchestration/feature-support -->
<!-- Fetched: 2026-05-11 -->

# Supported Orchestration features

Learn about the features that Orchestration supports.

> #### Want access to Orchestration?
>
> Orchestration is in private preview.

When using Orchestration with different payment processors, you might encounter payment features that don’t work that you would normally expect to work with Stripe. In these cases, the request fails with a `400` error code `orchestration_unsupported`. The first unsupported feature found is also included in the error message.

## Error protection

During the onboarding process, you can opt into error protection, which automatically handles these cases. If we see a payment requesting an unsupported feature, we route the payment to Stripe instead of the originally determined payment processor. This avoids returning these validation errors. We also consider error protection during [cross-processor retries](https://docs.stripe.com/payments/orchestration/retries.md). However, if there was a failover and the original processor was Stripe, we ignore the error protection configuration. We do so to avoid a duplicate attempt on Stripe. Contact your Stripe representative to enable this configuration.

## Supported features

Orchestration currently supports the following features for each payment service provider.

| Processor:                                                                                             | Adyen       | Braintree   | Worldpay WPG  |
| ------------------------------------------------------------------------------------------------------ | ----------- | ----------- | ------------- |
| Automatic confirmation                                                                                 | ✓ Supported | ✓ Supported | ✓ Supported   |
| Automatic capture                                                                                      | ✓ Supported | ✓ Supported | ✓ Supported   |
| [Manual capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md) 1               | ✓ Supported | ✓ Supported | ✓ Supported   |
| Full refunds 4                                                                                         | ✓ Supported | ✓ Supported | ✓ Supported   |
| Partial refunds 4                                                                                      | ✓ Supported | ✓ Supported | ✓ Supported   |
| 3DS                                                                                                    | ✓ Supported | ✓ Supported | ✓ Supported   |
| [Statement descriptors](https://docs.stripe.com/get-started/account/statement-descriptors.md) 2        | ✓ Supported | ✓ Supported | ✓ Supported   |
| [Wallets](https://docs.stripe.com/payments/orchestration/wallet-payments.md) (Apple Pay, Google Pay) 3 | ✓ Supported | ✓ Supported | ✓ Supported   |
| Network tokens                                                                                         | ✓ Supported | ✓ Supported | - Unsupported |
| Recurring transactions                                                                                 | ✓ Supported | ✓ Supported | ✓ Supported   |

1 Multicapture is currently unsupported.

2 `statement_descriptor_suffix_kanji` is unsupported. `statement_descriptor_suffix_kana` is only supported on **Adyen**.

3 3DS isn’t supported with Apple Pay and Google Pay (DPAN). Google Pay (FPAN) isn’t supported on **Adyen**.

4 You can initiate a preemptive refund for a PaymentIntent with a status of `processing`. Stripe submits the refund request to the corresponding processor after the payment succeeds, or fails the refund request if the payment fails.

If you’re interested in a feature that Orchestration doesn’t support, contact your Stripe representative.
