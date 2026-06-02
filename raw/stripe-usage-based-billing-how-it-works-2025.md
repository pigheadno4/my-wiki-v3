<!-- Source URL: https://docs.stripe.com/billing/subscriptions/usage-based/how-it-works -->
<!-- Fetched: 2026-05-05 -->

# How usage-based billing works

Learn how you can launch common usage-based pricing models on Stripe.

Usage-based billing enables you to charge customers based on their usage of your product or service.

The Stripe usage-based billing lifecycle is made up of four major components:

- [Ingestion](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage.md): Send your customer’s usage data to Stripe.
- [Product catalog](https://dashboard.stripe.com/products) set up: Create your usage based and recurring prices.
- [Billing](https://docs.stripe.com/billing/subscriptions/usage-based-v1/use-cases.md): Subscribe your customer to a set of prices that reflect your pricing model. Stripe invoices your customers for the usage they consume.
- [Monitoring](https://docs.stripe.com/billing/subscriptions/usage-based/monitor.md): Set up alerts to receive notifications of customers crossing usage thresholds. Track usage analytics to understand key trends.

## Lifecycle

This is the lifecycle for a typical [usage-based billing](https://docs.stripe.com/billing/subscriptions/usage-based.md) integration that uses products and prices:
Usage-based billing with pricing models (See full diagram at https://docs.stripe.com/billing/subscriptions/usage-based/how-it-works)

## Usage-based billing concepts

Learn about these concepts to understand how usage-based billing works.

| Term                                                                                                                                                                                     | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Customer-configured Accounts](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer) or [Customers](https://docs.stripe.com/api/customers.md) | Use customer-configured `Account` objects or `Customer` objects to represent an entity (typically a person or business) that can make payments to your business. You can use these objects to store billing details, set up subscriptions, track payments, and manage customer information. You can also link customers to your own user system using the `metadata` field, which allows you to associate your internal user IDs with Stripe customer records. |

- For more information about customer-configured `Account` objects, see [Represent customers using Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md).
- For more information about `Customer` objects, see [Customers](https://docs.stripe.com/billing/customer.md). |
  | [Subscriptions](https://docs.stripe.com/api/subscriptions.md) | A Stripe subscription represents a recurring billing relationship with a specific customer and one or more prices. Subscriptions charge customers on a recurring schedule (weekly, monthly, yearly, and so on) and generate invoices at the end of each billing cycle. For more information, see [How subscriptions work](https://docs.stripe.com/billing/subscriptions/overview.md). |
  | [Prices](https://docs.stripe.com/api/prices.md) | Prices are attached to products and represent specific pricing configurations that define how much and how often to charge for a product. To learn about key attributes and the differences between one-time, recurring, and usage-based charges, see [Prices](https://docs.stripe.com/products-prices/how-products-and-prices-work.md#prices). |
  | [Meter](https://docs.stripe.com/api/billing/meter.md) | A Stripe meter tracks usage data (such as API requests, processing time, and data storage) and specifies how to aggregate the data (meter events) over a billing period for usage-based billing. Meters use an aggregation [formula](https://docs.stripe.com/api/billing/meter/object.md#billing_meter_object-default_aggregation-formula) to define how usage events are counted and aggregated. To create a meter, see [Create and configure a meter](https://docs.stripe.com/billing/subscriptions/usage-based/meters/configure.md). |
  | [Meter events](https://docs.stripe.com/api/billing/meter-event.md) | A meter event represents a unit of usage that you report to Stripe for usage-based billing. They capture specific instances of customer usage and include:
- An event name (matching the configured meter)
- A customer identifier
- A numerical usage value
- An optional timestamp (defaults to current time if not specified)
- An optional unique identifier for idempotency
- Any additional dimensions for segmentation |
  | [Meter event summary](https://docs.stripe.com/api/billing/meter-event-summary.md) | You can use the Meter Event Summary to retrieve total usage for a custom time period. The meter event summary returns a customer’s aggregated usage for a period, based on the aggregation formula defined by the meter. Meter event summaries update asynchronously when meter events process. |
