<!-- Source URL: https://docs.stripe.com/radar/supported-payment-methods -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Supported payment methods with Radar

Configure how Radar evaluates transactions against default risk controls.

Radar fraud protection is active by default for all Stripe users and for all [supported payment methods](https://docs.stripe.com/payments/payment-methods/overview.md). Radar doesn’t support deprecated payment methods. Users on Radar Standard or above are protected by a set of default risk controls that block high-risk payments. You can view blocked payments on the [Radar risk controls](https://dashboard.stripe.com/settings/radar/risk-controls) page in the Dashboard.

> #### Radar Lite users
> 
> Stripe might still block payments for a variety of reasons, including but not limited to fraud risk, sanctions, and other compliance and regulatory considerations.

## Custom risk settings 

If [your plan](https://docs.stripe.com/radar/how-radar-works.md#compare-plans) supports this feature, you can customize your risk settings for the following types of payment methods:

- [Cards](https://docs.stripe.com/payments/payment-methods/overview.md#cards)
- [Digital wallets](https://docs.stripe.com/payments/payment-methods/overview.md#wallets)
- [Bank debits](https://docs.stripe.com/payments/payment-methods/overview.md#bank-debits)
- [Bank redirects](https://docs.stripe.com/payments/payment-methods/overview.md#bank-redirects)
- [Bank transfers](https://docs.stripe.com/payments/payment-methods/overview.md#bank-transfers)
- [Buy now, pay later](https://docs.stripe.com/payments/payment-methods/overview.md#buy-now-pay-later)
- [Real-time payments](https://docs.stripe.com/payments/payment-methods/overview.md#real-time-payments)
- [Stablecoin payments](https://docs.stripe.com/payments/stablecoin-payments.md)
- [Vouchers](https://docs.stripe.com/payments/payment-methods/overview.md#vouchers)
- [Wallets](https://docs.stripe.com/payments/payment-methods/overview.md#wallets)

### Risk controls

You can customize your risk controls with these features:

- **Block and allow lists**: Automatically block or allow transactions based on email address, IP address, email domain, and more.
- **Custom rules**: Create tailored fraud prevention logic using [attributes](https://docs.stripe.com/radar/rules/supported-attributes.md).
- **Rule backtesting**: Test changes against historical data before implementing them.
- **Radar analytics**: View consolidated fraud and performance metrics across all of your payment volume.

### Payment method rules

By default, all [supported payment methods](https://docs.stripe.com/payments/payment-methods/overview.md) inherit your active Radar rules and settings. You can adjust individual payment method rules with the `:payment_method_type:` attribute.

For example, this rule applies only to transactions using Bacs Direct Debit, where the customer IP address has a high number of disputes:

`if :payment_method_type: = 'bacs_debit' and :dispute_count_on_ip_weekly: >  3`

## See also

- Customize Radar [block and allow lists](https://docs.stripe.com/radar/lists.md)
- Customize Radar [rules](https://docs.stripe.com/radar/rules.md)
- Monitor transactions with Radar [analytics](https://docs.stripe.com/radar/analytics.md)
