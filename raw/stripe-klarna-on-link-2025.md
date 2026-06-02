<!-- Source URL: https://docs.stripe.com/payments/link/klarna -->
<!-- Fetched: 2026-05-08 -->

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

| Brand             | Number           | CVC          | Date            | Usage                      |
| ----------------- | ---------------- | ------------ | --------------- | -------------------------- |
| Visa (credit)     | 4242424242424242 | Any 3 digits | Any future date | Use for installments plans |
| Unbranded (debit) | 4687388888888881 | Any 3 digits | Any future date | Use for financing plans    |

### New Klarna on Link customer

The following images illustrate how an existing Link customer checks out with Klarna on Link for the first time:
![Payment page](assets/stripe-klarna-link-pay-later.png)

Customer selects **Pay later** > **Continue to payment plans**.
![Klarna confirmation page](assets/stripe-klarna-link-confirm-info.png)

Customer confirms their identity and clicks **Continue** to create a Klarna account.
![Payment plan selection page](assets/stripe-klarna-link-select-plan.png)

Customer selects one of the available payment plans, and clicks **Continue**.
![Confirm payment page](assets/stripe-klarna-link-pay.png)

Customer reviews their payment details and plan, and clicks **Pay**.

### Returning Klarna on Link customer

The next time a customer sees Klarna on Link at checkout, their Klarna details are already saved to their Link account:
![Payment page](assets/stripe-klarna-link-returning-pay-later.png)

Customer clicks **Pay later**.
![Klarna confirmation page](assets/stripe-klarna-link-returning-confirm-info.png)

Customer reviews their pre-populated payment details, and clicks **Pay**.
![Success page](assets/stripe-klarna-link-returning-success.png)

Customer returns to your success page.

### Future payments

After a customer’s payment method issuer authorizes a Klarna payment, Stripe immediately deposits the full purchase amount (minus Stripe fees) to your Stripe account. You don’t have to wait for Klarna to collect future installment payments.

## See also

- [Link payment methods](https://docs.stripe.com/payments/link/link-payment-methods.md)
- [Link in different payment integrations](https://docs.stripe.com/payments/link/link-payment-integrations.md)
- [Pricing for Link](https://stripe.com/pricing/local-payment-methods#link)
