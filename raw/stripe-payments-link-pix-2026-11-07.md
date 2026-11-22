<!-- Source URL: https://docs.stripe.com/payments/link/pix -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Pix on Link

Use Link to accept Pix, a popular payment method in Brazil.
Available in: US
Pix is a real-time payment method in Brazil that transfers funds directly between bank accounts. Customers pay with Pix by scanning a QR code on the checkout page and completing the payment in their preferred banking app.

Link lets customers save their personal details for faster checkouts across businesses that support Link. With Link, businesses can accept Pix without additional integration changes or business logic.

## Eligibility 

Pix on Link supports:

- On-session payments
- Payments presented in BRL
- Transaction amounts equivalent to 0.50 to 3,000 USD, presented in BRL
- Eligible US businesses that meet onboarding requirements and aren’t classified as restricted businesses

[Payment Links](https://docs.stripe.com/payment-links.md), hosted [Stripe Checkout](https://docs.stripe.com/checkout/quickstart.md) pages, and the [Payment Element](https://docs.stripe.com/payments/advanced.md) support Pix on Link.

### Prohibited business categories 

In addition to the industry and business categories listed in [Prohibited and Restricted Businesses](https://stripe.com/legal/restricted-businesses), the following categories can’t use Pix:

- Crypto businesses
- Insurance companies
- Telehealth or medicine vendors
- Non-profits and charities

For more information about Pix eligibility, go to your account’s [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods).

## How Pix on Link works 

You can offer Pix through both Link and a direct Pix integration. Eligible customers can choose to pay with Pix using Link or without Link at checkout.

Payments made through Link use the Link payment method and the customer’s saved Link details. Payments made through your direct Pix integration use the standard Pix payment flow.

### New customers 

The following steps show how a new Link customer checks out with Pix for the first time:

1. The customer selects **Pix** on your checkout page and enters their name, address, and a tax identifier.
2. They click **Pay**, sign up for Link, and a QR code is displayed.
3. They open their banking app, scan the QR code, review the transaction details, and authorize the payment.
4. After the payment succeeds, the customer sees a confirmation on your checkout page.

### Returning customers 

If a customer has previously paid with Pix on Link, they can use their saved details to pay:

1. The customer selects **Pix**.
2. They click **Pay**. Link automatically fills in their saved details and displays a QR code.
3. They open their banking app, scan the QR code, review the transaction details, and authorize the payment.
4. After the payment succeeds, the customer sees a confirmation on your checkout page.

## Statement descriptor 

The customer’s bank statement lists the Stripe service provider, Ebanx, as the payment recipient. Your business name appears in the `Message to payor` field.

## Brazilian consumer tax 

Imposto sobre Operações Financeiras (IOF) is a Brazilian tax that applies to transactions involving currency conversion, such as converting BRL to USD. Brazilian customers pay IOF when purchasing from international businesses outside Brazil. The IOF rate is 3.5% of the transaction amount (subject to change).

For Pix on Link payments, your customer pays the IOF. Stripe calculates the tax through its payment partner. When your customer completes the payment in their banking app, the total amount includes the IOF.

Stripe also provides the required customer disclosures on your behalf.

## Receipts 

In Brazil, businesses commonly send a receipt for each transaction that itemizes the IOF amount. The Stripe Pix service provider, Ebanx, sends receipts to your customers on your behalf.

## Disputes 

Pix allows disputes in limited circumstances, such as fraud or account takeover. Customers must file disputes with their bank and provide evidence to support their claim. You can’t challenge these disputes.

If Stripe receives notice that its payment partner accepted a request to return the customer’s funds, Stripe removes the funds from your account.

## Refunds 

You can refund a Pix payment within 90 days of the original payment date. The refund typically appears in your account within a few minutes.

## Request access 

Businesses in Australia, Canada, the [European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area) (EEA), Singapore, and the United Kingdom can request access to the private preview.

### Interested in learning more about Pix on Link?

Enter your email to request access.

```bash
curl https://docs.stripe.com/preview/register \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Referer: https://docs.stripe.com/payments/link/pix" \
  -d '{"email": "EMAIL", "preview": "link_lpm_interest_preview"}'
```

## See also

- [Link payment methods](https://docs.stripe.com/payments/link/link-payment-methods.md)
- [Link in different payment integrations](https://docs.stripe.com/payments/link/link-payment-integrations.md)
- [Pix payments](https://docs.stripe.com/payments/pix.md)
