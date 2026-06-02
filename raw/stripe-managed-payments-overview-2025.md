<!-- Source URL: https://docs.stripe.com/payments/managed-payments -->
<!-- Fetched: 2026-04-23 -->

# Managed Payments

Sell digital products globally with the Stripe merchant of record solution for tax, fraud, disputes, and support.

Use Managed Payments to sell digital products such as SaaS, software, and digital content or downloads. The Stripe merchant of record solution handles indirect tax compliance in more than 80 countries, along with fraud prevention, dispute management, and transaction-level customer support.

## Learn more

- How Managed Payments works — Learn how Managed Payments works.
- Managed Payments eligibility — Learn which products, countries, and integrations are supported.
- Tax compliance with Managed Payments — Learn how Managed Payments handles indirect tax compliance in more than 80 countries.

## Use cases

- Build a Checkout integration — Build a new Checkout integration with Managed Payments enabled.
- Update your Checkout integration — Update an existing Checkout integration to use Managed Payments.
- Create payment links — Create payment links with Managed Payments enabled to start collecting payments for digital products.
- Accept mobile app payments — Use Managed Payments to accept payments from a mobile app.

## Compare Managed Payments with other Stripe products

| Feature | Managed Payments | Other Stripe products |
| --- | --- | --- |
| Merchant of record | Stripe | Your business |
| Manage indirect tax compliance | ✓ (80+ countries) | Available with Tax |
| Checkout page compatible with | Checkout, Payment Links | Checkout, Elements, Hosted Invoice Page, Payment Links |
| Support for subscriptions | Available with Billing | Available with Billing |
| Protect against fraud | | Available with Radar |
| Respond to disputes | | Available with Payments |
| Transaction-level customer support | ✓ | |
| Support for platforms | | Available with Connect |

> Managed Payments handles indirect tax compliance (sales tax, VAT, and GST) on transactions in more than 80 countries.

## Unsupported integrations

Managed Payments doesn't support:

- Stripe Connect (platform or marketplace integrations)
- Payment flows that use embeddable web components or other advanced integrations
- Attaching invoice items on a Customer object to a Managed Payments subscription
- Generating a one-off invoice on a Customer object or for a subscription outside the billing period
- Creating a subscription outside of Checkout or Payment Links
- Third-party tax integrations
