<!-- Source URL: https://docs.stripe.com/payments/link/upi -->
<!-- Fetched: 2026-05-08 -->

# UPI on Link

Learn about UPI, a popular payment method in India, on Link.
Available in: US
UPI is a real-time payment system developed by the National Payments Corporation of India. UPI works by instantly transferring funds between two bank accounts.

Customers use their preferred banking or wallet app to authenticate and approve payments. On desktop, customers scan a QR code using their preferred UPI app. On mobile, customers are redirected to their UPI app to complete the payment.

Link allows customers to save personal details, allowing faster checkouts for future transactions. For your business, Link enables UPI acceptance without any additional integration changes or business logic.

## Get started

UPI is automatically enabled when you turn on [Link](https://docs.stripe.com/payments/link.md), subject to [eligibility requirements](https://docs.stripe.com/payments/upi.md).

> Only [Payment Links](https://docs.stripe.com/payment-links.md), [Stripe Checkout (Hosted)](https://docs.stripe.com/checkout/quickstart.md) and [Elements](https://docs.stripe.com/payments/advanced.md) support UPI on Link. Link doesn’t offer UPI in other payment flows.

UPI in Link supports:

- One-time and on-session payments
- Payments presented in INR
- Transaction amounts from 1 INR to 100,000 INR
- Eligible US businesses, subject to onboarding and restricted-business exclusions

### UPI checkout for a new Link customer

The following steps describe how a new Link customer checks out with UPI for the first time.

1. The customer selects **UPI** and enters buyer information.
1. They click **Pay**, and depending on their device type:
   - On desktop, they see a QR code that they scan with their preferred UPI app to complete the transaction.
   - On mobile, customers see a list of UPI apps. After selecting their preferred one, they’re redirected to that app to complete the payment.
1. After completing the payment, buyers are redirected to your checkout page and are notified of payment status.

Customers automatically sign up for Link when they complete the transaction, and store their details for future checkouts.

### UPI experience for a returning Link customer

If a customer has previously paid with UPI on Link, their payment details (for example, name, address, and virtual payment address) have already been saved to their Link account:

1. The customer selects **UPI**.
1. They click **Pay**, and depending on their device type:
   - On desktop, they receive a QR code to scan that redirects them to choose a banking app on their smartphone to complete the transaction.
   - On mobile, they’re redirected to a list of UPI-supported banking apps that they can pay with.
1. They authorize and complete the payment and receive a notification that their payment is complete.

### Refunds

You can refund UPI payments up to 60 days after the original payment. Refunds are asynchronous and can take up to 7 business days to complete. Stripe notifies you of the final refund status using the `refund.updated` or `refund.failed` _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund](https://docs.stripe.com/api/refunds/object.md) object’s status transitions to `succeeded`. In the rare instance that a refund fails, the `Refund` object’s status transitions to `failed` and Stripe returns the amount to your balance. You’ll need to arrange an alternative way to refund your customer.

### Disputes

The risk of fraud or unrecognized payments is low because the customer must authenticate the payment with their bank. However, the customer might dispute a UPI transaction with their bank or PSP. For example, they might dispute the payment when their bank account is debited for a failed transaction, or after a failure to receive goods and services. If their bank or PSP accepts the request to return funds, you can’t contest the dispute and Stripe immediately removes funds from your Stripe account.

## See also

- [Link payment methods](https://docs.stripe.com/payments/link/link-payment-methods.md)
- [Link in different payment integrations](https://docs.stripe.com/payments/link/link-payment-integrations.md)
- [UPI payments](https://docs.stripe.com/payments/upi.md)
