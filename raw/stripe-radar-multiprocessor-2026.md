<!-- Source URL: https://docs.stripe.com/radar/multiprocessor -->
<!-- Fetched: 2026-05-10 -->

# Radar risk signals for multiple payment processors

Evaluate your non-Stripe processed payments with Radar.

[Stripe Radar](https://docs.stripe.com/radar.md) allows businesses to evaluate their externally-processed payments in real time and receive risk signals from the Radar AI models. You can request a payment evaluation at any time in the payment lifecycle–not only when you submit to the processor.

### Fraudulent payment

The `fraudulent_payment` signal identifies if a payment will likely result in a dispute with a fraudulent reason code or an early fraud warning. Payment evaluations provide this signal by default.

### Fraudulent dispute (Private preview)

The `fraudulent_dispute` signal identifies if a payment will likely result in a dispute and blocks these payments with a fraudulent reason code.

### Early fraud warning (Private preview)

The `early_fraud_warning` signal identifies if a payment will likely result in an early fraud warning.

## Prerequisites

Before you request a payment evaluation on an externally-processed transaction, you must:

- Create a [tokenized PaymentMethod](https://docs.stripe.com/api/payment_methods/create.md). We currently support only [card type](https://docs.stripe.com/api/payment_methods/create.md#create_payment_method-type) payment methods.
- Create a [Radar Session token](https://docs.stripe.com/radar/radar-session.md), which automatically collects [advanced risk factors](https://docs.stripe.com/disputes/prevention/advanced-fraud-detection.md) for each transaction.
- Collect the customer email by populating the [billing_details.email](https://docs.stripe.com/api/payment_methods/create.md#create_payment_method-billing_details-email) attribute in the payment method or creating a new customer (either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) object or a [Customer](https://docs.stripe.com/api/customers/create.md) object).

The following diagram shows your initial call to create a `PaymentEvaluation` and the real-time response from Stripe with risk signals.
A diagram showing the Payment Evaluation API sequence of interactions for a standard payment. (See full diagram at https://docs.stripe.com/radar/multiprocessor)
