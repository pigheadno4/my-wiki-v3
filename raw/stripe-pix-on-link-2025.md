<!-- Source URL: https://docs.stripe.com/payments/link/pix -->
<!-- Fetched: 2026-05-08 -->

# Pix on Link

Learn about Pix, a popular payment method in Brazil, on Link.
Available in: US
Pix is a popular real-time payment method in Brazil that works by transferring funds between two bank accounts. To pay with Pix, customers scan a QR code on a checkout page and complete the payment in their preferred banking app.

Link allows customers to save personal details, allowing faster checkouts for future transactions across Link merchants. For businesses, Link it enables Pix acceptance without any additional integration changes or business logic.

## Get started

Pix is automatically enabled when you turn on [Link](https://docs.stripe.com/payments/link.md), subject to [eligibility requirements](https://docs.stripe.com/payments/pix.md#prohibited-business-categories).

> Only [Payment Links](https://docs.stripe.com/payment-links.md), [Stripe Checkout (Hosted)](https://docs.stripe.com/checkout/quickstart.md) and the [Payment Element](https://docs.stripe.com/payments/advanced.md) support Pix on Link. Link doesn’t offer Pix in other payment flows.

Pix in Link is currently supported for:

- One-time and on-session payments
- Payments presented in BRL
- Transaction amounts from 5 BRL to 3,000 USD equivalent in BRL
- Eligible US businesses, subject to onboarding and restricted-business exclusions

### Pix checkout for a new Link customer

The following steps illustrate how a new Link customer checks out with Pix for the first time:

1. The Customer selects **Pix** from your checkout page and enters the required buyer information (name, address, and a tax identifier).
1. After the buyer clicks **Pay**, they’re signed up to Link, and receive a QR code and a Pix code to scan from their phone.
1. The buyer opens up their banking app, scans the QR code or copies the Pix code. They then see details of the transaction and authorize the payment.
1. After the payment completes, they’re redirected back to your checkout page.

### Pix experience for a returning Link customer

If a customer has previously paid through Pix on Link, their Pix details are already saved to their Link account:

1. The customer selects **Pix**.
1. They click **Pay** and receive a QR code with their saved customer details automatically filled.
1. The buyer scans the QR code that redirects them to make a payment through bank apps or internet banking.
1. They complete the payment, receive a notification that the payment is complete, and are redirected back to your checkout page.

### Statement descriptor

The statement descriptor in the customer’s bank statement shows Stripe’s service provider “Ebanx” as the payment recipient. Your business name appears in the **Message to payor** field.

### Brazilian consumer tax

IOF (“Imposto sobre Operações Financeiras”) is a Brazilian tax applicable to all transactions that involve a currency exchange (for example, from BRL to USD). The IOF is collected from Brazilian buyers paying international businesses outside of Brazil. The current rate is 3.5% of the transaction value.

For payments using Pix on Link, your customer pays the IOF. Stripe handles the calculation of the tax through our partner. When your customer completes a payment in their banking app they pay a marked up amount, inclusive of the IOF.

Stripe also handles all relevant customer disclosures on your behalf.

### Receipts

In Brazil, businesses commonly send a receipt for each transaction and itemize the Brazilian consumer tax (IOF) amount. Our Pix service provider, Ebanx, sends customer receipts on your behalf.

### Disputes

The risk of fraud or unrecognized payments on Pix is low because customers must authenticate each payment in their banking app. Disputes raised through Pix are handled in the same way as other payment methods on Link.

## See also

- [Link payment methods](https://docs.stripe.com/payments/link/link-payment-methods.md)
- [Link in different payment integrations](https://docs.stripe.com/payments/link/link-payment-integrations.md)
- [Pix payments](https://docs.stripe.com/payments/pix.md)
