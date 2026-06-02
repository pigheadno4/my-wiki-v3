<!-- Source URL: https://docs.stripe.com/radar/supported-payment-methods -->
<!-- Fetched: 2026-05-10 -->

# Supported payment methods with Radar

Configure how Radar evaluates transactions against default risk controls.

Radar fraud protection is active by default for all Stripe users. Radar screens all payment methods against [default risk controls](https://docs.stripe.com/radar/supported-payment-methods.md#default-risk-controls), and blocks all high-risk transactions.

## Default risk controls for all payments

All Radar users are protected by a set of default risk controls that block high-risk payments. Radar is on by default, and applies to [all payment methods](https://docs.stripe.com/payments/payment-methods/overview.md). Radar supports most preview payment methods, but not deprecated payment methods.

You can view blocked payments on the [Radar risk controls](https://dashboard.stripe.com/settings/radar/risk-controls) page in the Dashboard.

## Custom risk settings

If you use Radar for Fraud Teams or Radar for Platforms, you can customize your risk settings for these payment methods:

| Category                                                                                                                                                                                                                                                                                                         | Payment methods                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Status                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| [Cards](https://docs.stripe.com/payments/payment-methods/overview.md#cards)                                                                                                                                                                                                                                      | Credit and debit cards, card-backed digital wallets1                                                                                                                                                                                                                                                                                                                                                                                                                                            | ✓ Supported Supported |
| [Bank Debits](https://docs.stripe.com/payments/payment-methods/overview.md#bank-debits)                                                                                                                                                                                                                          | _ACH_ (Automated Clearing House (ACH) is a US financial network used for electronic payments and money transfers that doesn’t rely on paper checks, credit card networks, wire transfers, or cash), _SEPA_ (Single Euro Payments Area (SEPA) is a payment-integration initiative to simplify bank transfers involving euros. Several dozen countries comprise SEPA. Most of the participating countries are in the European Union and have euro-based economies, but this is not a requirement) | ✓ Supported Supported |
| [ACSS](https://docs.stripe.com/payments/acss-debit.md), [AU Becs](https://docs.stripe.com/payments/au-becs-debit.md), [Bacs](https://docs.stripe.com/payments/payment-methods/bacs-debit.md), [NZ Becs](https://docs.stripe.com/payments/nz-bank-account.md), [PayTo](https://docs.stripe.com/payments/payto.md) | (Private preview)                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Buy Now Pay Later](https://docs.stripe.com/payments/payment-methods/overview.md#buy-now-pay-later)                                                                                                                                                                                                              | [Affirm](https://docs.stripe.com/payments/affirm.md), [Afterpay](https://docs.stripe.com/payments/afterpay-clearpay.md), [Klarna](https://docs.stripe.com/payments/klarna.md)                                                                                                                                                                                                                                                                                                                   | (Private preview)     |
| [Digital wallets](https://docs.stripe.com/payments/payment-methods/overview.md#wallets)                                                                                                                                                                                                                          | [Cash App](https://docs.stripe.com/payments/cash-app-pay.md), [PayPal](https://docs.stripe.com/payments/paypal.md)                                                                                                                                                                                                                                                                                                                                                                              | (Private preview)     |
| [Stablecoin and crypto wallets](https://docs.stripe.com/payments/stablecoin-payments.md)                                                                                                                                                                                                                         | Any compatible crypto wallet                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | (Private preview)     |

1 For example, [Apple Pay](https://docs.stripe.com/apple-pay.md) or [Google Pay](https://docs.stripe.com/google-pay.md).

### Risk controls

> To customize risk controls for any payment methods in private preview, you’ll need to [opt in](https://docs.stripe.com/radar/supported-payment-methods.md#early-access).

You can customize your risk controls with these features:

- **Block and allow lists**: Automatically block or allow transactions based on email address, IP address, email domain, and more.
- **Custom rules**: Create tailored fraud prevention logic using [attributes](https://docs.stripe.com/radar/rules/supported-attributes.md).
- **Rule backtesting**: Test changes against historical data before implementing them.
- **Radar analytics**: View consolidated fraud and performance metrics across all of your payment volume.

### Payment method rules

By default, all supported payment methods inherit your active Radar rules and settings. You can adjust individual payment method rules with the `:payment_method_type:` attribute.

For example, this rule applies only to transactions using Bacs Direct Debit, where the customer IP address has a high number of disputes:

`if :payment_method_type: = 'bacs_debit' and :dispute_count_on_ip_weekly: >  3`

## Request early access

## See also

- Customize Radar [block and allow lists](https://docs.stripe.com/radar/lists.md)
- Customize Radar [rules](https://docs.stripe.com/radar/rules.md)
- Monitor transactions with Radar [analytics](https://docs.stripe.com/radar/analytics.md)
