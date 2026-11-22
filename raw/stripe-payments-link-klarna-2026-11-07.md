<!-- Source URL: https://docs.stripe.com/payments/link/klarna -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Klarna on Link

Offer buy now, pay later payments through Klarna on Link.
Available in: US
Link customers in the United States can use [Klarna payments](https://docs.stripe.com/payments/klarna.md) on Link.

## Get started

Klarna is automatically enabled when you turn on [Link](https://docs.stripe.com/payments/link.md), subject to [eligibility requirements](https://docs.stripe.com/payments/klarna.md#get-started).

> Only [Payment Links](https://docs.stripe.com/payment-links.md), [Stripe Checkout (Hosted)](https://docs.stripe.com/checkout/quickstart.md) and the [Payment Element](https://docs.stripe.com/payments/advanced.md) support Klarna on Link. Link doesn’t offer Klarna in other payment flows.

To disable Klarna on Link, go to your [Link settings](https://dashboard.stripe.com/settings/link) and unselect **Pay later with Klarna**.

### Testing

You can test Klarna on Link in a [sandbox](https://docs.stripe.com/sandboxes.md). Use any of the following cards to complete a test (Klarna on Link) payment:

| Brand | Number | CVC | Date | Usage |
| --- | --- | --- | --- | --- |
| Visa (credit) | 4242424242424242 | Any 3 digits | Any future date | Use for installments plans |
| Unbranded (debit) | 4687388888888881 | Any 3 digits | Any future date | Use for financing plans |

### New Klarna on Link customer

The following images illustrate how an existing Link customer checks out with Klarna on Link for the first time:
![Payment page](https://b.stripecdn.com/docs-statics-srv/assets/klarna-pay-later.26e2c12e42b466e968b65d7aba3b3abd.png)

Customer selects **Pay later** > **Continue to payment plans**.
![Klarna confirmation page](https://b.stripecdn.com/docs-statics-srv/assets/klarna-confirm-info.4e2d6796239ef1ac27592078b7816f25.png)

Customer confirms their identity and clicks **Continue** to create a Klarna account.
![Payment plan selection page](https://b.stripecdn.com/docs-statics-srv/assets/klarna-select-plan.0872a0fe8e12e73d847f0ed19fd27d91.png)

Customer selects one of the available payment plans, and clicks **Continue**.
![Confirm payment page](https://b.stripecdn.com/docs-statics-srv/assets/klarna-pay.c39a0b399713143890ea8d2ab4f88810.png)

Customer reviews their payment details and plan, and clicks **Pay**.

### Returning Klarna on Link customer

The next time a customer sees Klarna on Link at checkout, their Klarna details are already saved to their Link account:
![Payment page](https://b.stripecdn.com/docs-statics-srv/assets/klarna-returning-pay-later.214b5231828ada61eb6032bd0b07e464.png)

Customer clicks **Pay later**.
![Klarna confirmation page](https://b.stripecdn.com/docs-statics-srv/assets/klarna-returning-confirm-info.e0a2ae7e35dbadadb30b29e435a1cf85.png)

Customer reviews their pre-populated payment details, and clicks **Pay**.
![Success page](https://b.stripecdn.com/docs-statics-srv/assets/klarna-returning-success.6d499c3a065a13530c83f7b22661ef1a.png)

Customer returns to your success page.

### Future payments

After a customer’s payment method issuer authorizes a Klarna payment, Stripe immediately deposits the full purchase amount (minus Stripe fees) to your Stripe account. You don’t have to wait for Klarna to collect future installment payments.

## See also

- [Link payment methods](https://docs.stripe.com/payments/link/link-payment-methods.md)
- [Link in different payment integrations](https://docs.stripe.com/payments/link/link-payment-integrations.md)
- [Pricing for Link](https://stripe.com/pricing/local-payment-methods#link)
