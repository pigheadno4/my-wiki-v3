<!-- Source URL: https://docs.stripe.com/radar/custom-fraud-models -->
<!-- Fetched: 2026-05-10 -->

# Custom fraud models

Combine your business signals with Stripe global network intelligence for more accurate fraud detection.

We train the Radar global model on data from businesses across the Stripe network to create a baseline. A custom fraud model extends this by allowing you to provide signals unique to your business, such as product catalog data, loyalty status, behavioral metrics, or any structured metadata relevant to your risk profile.

Radar combines your metadata with our global network data to learn patterns and build a custom model for your business. A custom fraud model can help you:

- **Catch more fraud**: Identify fraud that looks normal to a global model but is anomalous for your traffic.
- **Approve more legitimate transactions**: Approve transactions that might look risky globally but are typical for your business.
- **Improve false positive tradeoffs**: Improve precision and recall, allowing you to catch more fraud without blocking customers.

## Before you begin

Custom models require:

- **Structured metadata on payments**: You must send relevant business signals as metadata on your payment objects.
- **Sufficient payment volume**: Custom models require enough transaction history to train an effective model. We evaluate this during onboarding.

## How it works

1. **You send metadata with your payments**: Use standard API fields, such as [PaymentIntent.metadata](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-metadata), to attach structured business signals to your Stripe payments. You don’t need to take any additional action.
1. **We train a model on your traffic**: Radar ingests your metadata alongside its global fraud signals and trains a custom model for your business.
1. **Radar uses your custom model to provide a score**: After deployment, a new Radar risk score that incorporates Stripe global intelligence and your custom signals is available. You don’t need to change your integration.
1. **The model evolves with your business**: We retrain the model as your product catalog, customer base, and fraud patterns change.

## Metadata to send

The custom models with the highest impact use signals that go beyond standard financial data and are specific to your business. Examples of high-impact metadata include:

| Signal             | Examples                                                                      |
| ------------------ | ----------------------------------------------------------------------------- |
| User signals       | Account age, verification status, internal identifiers (such as VIP customer) |
| Behavioral signals | Session duration, time from login to checkout, interaction frequency          |
| Product context    | Product category, item value tier, shipping method                            |
| Risk indicators    | Internal risk evaluations, usage-to-payment ratios                            |
