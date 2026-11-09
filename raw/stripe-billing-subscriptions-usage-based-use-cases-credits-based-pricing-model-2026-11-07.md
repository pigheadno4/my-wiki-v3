<!-- Source URL: https://docs.stripe.com/billing/subscriptions/usage-based/use-cases/credits-based-pricing-model -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Set up a credit-based pricing model

Charge customers for pre-purchase credits.

## Metronome versus basic usage-based billing

This page describes the lifecycle and concepts for basic usage-based billing, which is built on the Billing Meters API. Unless you’re maintaining an existing Billing Meters integration, use [Metronome](https://docs.stripe.com/billing/usage-based.md) — Stripe’s primary usage-based billing platform — for any new integration, including adding usage-based pricing to existing flat-rate subscriptions.

The core architectural difference is where billing logic lives. In basic usage-based billing, you ingest meter events through the Stripe API and the Billing Meters API aggregates usage at the end of the billing period before generating an invoice. In Metronome, a dedicated billing engine handles event ingestion, real-time metering, rating, and contract management, then passes finalized charges to Stripe for payment collection and invoicing.

This difference matters for several common requirements:

- **Real-time usage visibility**: Basic usage-based billing only reconciles usage at invoice time. Customers and your team can’t see live credit balances or usage totals mid-cycle. Metronome provides real-time usage tracking.
- **Prepaid credits**: Basic usage-based billing supports billing credits that reconcile at invoice time, but customers can exceed their balance during the cycle. Metronome supports real-time credit burndown, where usage reduces the credit balance as it occurs.
- **Enterprise contracts**: Basic usage-based billing doesn’t support commits, minimum spend requirements, or ramp schedules. Metronome supports all of these natively.
- **Dimensional pricing**: Basic usage-based billing supports a limited set of pricing structures. Metronome supports dimensional and composite pricing configurations.

See [Compare basic usage-based billing and Metronome](https://docs.stripe.com/billing/subscriptions/usage-based/compare-metronome.md) for a full feature comparison.

> This page describes basic usage-based billing with Billing Meters. Unless you’re maintaining an existing Billing Meters integration, use [Metronome](https://docs.stripe.com/billing/usage-based.md), which handles metering, pricing models, prepaid credits, enterprise contracts, and automated invoice generation. [Compare your options](https://docs.stripe.com/billing/subscriptions/usage-based/compare-metronome.md) to decide which approach fits your use case.

Credits allow you to offer a fixed, monetary amount of usage across your usage-based products. This model works well when you want to give customers upfront predictability while aligning revenue directly to usage. For example, if you sell an API that processes images and cloud storage, a customer might buy 100 USD of credits at the start of the month. They can spend any combination of API usage and cloud storage up to the monetary amount, and pay an overage charge for either service at the end of the month if they exceed 100 USD of usage.

Credits apply indiscriminately across meters. To set specific limits on your various consumption based products,(for example 100 API requests and 3GB’s of storage) use the [flat fee and overage](https://docs.stripe.com/billing/subscriptions/usage-based-v1/use-cases/flat-fee-and-overages.md) model.

## What you’ll build

In this guide, build the following subscription for a fictional company called Hypernian, which provides LLM. They charge customers at the following rates:

| Credits | Fee |
| --- | --- |
| Per user | 10 USD |

| Usage | Fee |
| --- | --- |
| Input token | 0.03 USD per token |
| Output token | 0.05 USD per token |

## Create a meter

Meters specify how to aggregate meter events over a billing period. Meter events represent all actions that customers take in your system (for example, API requests). Meters attach to prices and form the basis of what’s billed.

For the Hypernian example, meter events are the number of input and output tokens a customer uses in a query. The meter is the sum of tokens over a month. In this example. you create a meter for each token type.

You can use the Stripe Dashboard or API to [configure a meter](https://docs.stripe.com/billing/subscriptions/usage-based/meters/configure.md). To use the API with the Stripe CLI to create a meter, [get started with the Stripe CLI](https://docs.stripe.com/cli.md).

#### Dashboard

1. On the [Meters](https://dashboard.stripe.com/test/meters) page, click **Create meter**.
2. On the **Create meter** page, do the following:
   - For **Meter name**, enter the name of the meter to display and for organization purposes. For the Hypernian example, enter “Hypernian Input tokens.”
   - For **Event name**, enter the name to display in meter events when reporting usage to Stripe. For the Hypernian example, enter “hypernian_input_tokens.”
   - Set the **Aggregation method** in the dropdown:
     - For the Hypernian example, select **Sum**. This will *sum the values* reported (in this example, number of tokens a customer uses) to determine the usage to bill for.
     - Choose **Count** to bill based on the *number* of events reported.
     - Choose **Last** to bill based on the *last value* reported.
     - Use the preview pane to set example usage events and verify the aggregation method.
   - Click **Create meter**.
   - To create a meter for output tokens, repeat the previous steps and set the meter name to “Hypernian Output Tokens” and the Event name to “hypernian_output_tokens.”
   - (Optional) Under **Advanced settings**, specify the **Dimensions** that you want to tag your usage data with. To generate granular segment specific alerts, or to granularly price usage based on a combination of attributes, submit your usage data with dimensions that are populated for analytics and reporting. Some example dimensions are LLM model, token type, region, and event type.

#### API

```curl
curl https://api.stripe.com/v1/billing/meters \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "display_name=Hypernian Input tokens" \
  -d event_name=hypernian_input_tokens \
  -d "default_aggregation[formula]=sum" \
  -d "customer_mapping[event_payload_key]=stripe_customer_id" \
  -d "customer_mapping[type]=by_id" \
  -d "value_settings[event_payload_key]=value"
```

To create a meter for output tokens, repeat the previous step with the following values.

```curl
curl https://api.stripe.com/v1/billing/meters \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "display_name=Hypernian Output tokens" \
  -d event_name=hypernian_output_tokens \
  -d "default_aggregation[formula]=sum" \
  -d "customer_mapping[event_payload_key]=stripe_customer_id" \
  -d "customer_mapping[type]=by_id" \
  -d "value_settings[event_payload_key]=value"
```

## Create a pricing model

Use the Stripe Dashboard or API to create a [pricing model](https://docs.stripe.com/products-prices/pricing-models.md) that includes your [Products](https://docs.stripe.com/api/products.md) and their pricing options. [Prices](https://docs.stripe.com/api/prices.md) define the unit cost, currency, and billing period.

For the Hypernian example, you create two products each with a meter billed at a monthly interval. Use the meter that you created in the previous step.

#### Dashboard

1. On the [Product catalog](https://dashboard.stripe.com/products?active=true) page, click **Create product**.
2. On the **Add a product** page, do the following:
   - For **Name**, enter the name of your product. For the Hypernian example, enter `Hypernian`.
   - (Optional) For **Description**, add a description that appears in [Checkout](https://docs.stripe.com/payments/checkout.md), in the [customer portal](https://docs.stripe.com/customer-management.md) and in [quotes](https://docs.stripe.com/quotes.md).
   - Select **Recurring**.
   - Under **Billing period**, select **More pricing options**.
3. On the **Add price** page, do the following:
   - Under **Choose your pricing model**, select **Usage-based**.
   - Choose your pricing structure:
     - For the Hypernian example, select **Per Unit**. Under **Price**, set the **Amount** to `0.03 USD`.
     - Under **Meter**, select the meter you created and select Hypernian Input tokens from the dropdown.
     - For **Billing period**, select **Monthly**.
   - Under **Meter**, select the meter you created. For the Hypernian example, select **Hypernian Input tokens** from the dropdown.
   - Select the appropriate **Billing period**. For the Hypernian example, select **Monthly**.
   - Click **Next**.
4. Repeat the previous steps and create a product named “Hypernian output usage” with a price of `0.05 USD`. Attach it to the **Aplaca AI output token meter** with the same monthly billing period.

#### API

Create the product and price for the input usage’s tiered pricing.

```curl
curl https://api.stripe.com/v1/products \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "description=Input usage fee for Hypernian" \
  -d "name=Hypernian Input Usage"
```

```curl
curl https://api.stripe.com/v1/prices \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "product={{PRODUCT_ID}}" \
  -d currency=usd \
  -d billing_scheme=per_unit \
  -d "recurring[interval]=month" \
  -d "recurring[interval_count]=1" \
  -d "recurring[usage_type]=metered" \
  -d "recurring[meter]={{METER_ID}}" \
  -d unit_amount_decimal=3
```

Create the product and price for the output usage’s tiered pricing.

```curl
curl https://api.stripe.com/v1/products \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "description=Ouput usage fee for Hypernian" \
  -d "name=Hypernian Output Usage"
```

```curl
curl https://api.stripe.com/v1/prices \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "product={{PRODUCT_ID}}" \
  -d currency=usd \
  -d billing_scheme=per_unit \
  -d "recurring[interval]=month" \
  -d "recurring[interval_count]=1" \
  -d "recurring[usage_type]=metered" \
  -d "recurring[meter]={{METER_ID}}" \
  -d unit_amount_decimal=5
```

## Create a customer

Next, create a customer.

#### Dashboard

1. On the [Customers](https://dashboard.stripe.com/test/customers) page, click **Add customer**.
2. On the **Create customer** page, do the following:
   - For **Name**, enter the name of your customer. For the Hypernian example, enter `Jenny Rosen`.
   - (Optional) Add an email address and description for your customer.
   - Click **Add customer**.

#### API

> #### Use the Accounts v2 API to represent customers
> 
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
> 
> To join the Accounts v2 preview, go to [Account previews and features](https://dashboard.stripe.com/settings/previews) in your Dashboard and enable **Reusable payment methods for Global Payouts**.
> 
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) or [Customer](https://docs.stripe.com/api/customers/create.md) when your customer creates an account with your business, or when saving a payment method. Associate the object’s ID with your own internal representation of a customer.

Create a new customer or retrieve an existing one to associate with this payment.

#### Accounts v2

Set `configuration.customer` to an empty object to enable the customer configuration on this account.

```curl
curl -X POST https://api.stripe.com/v2/core/accounts \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  --json '{
    "contact_email": "jenny.rosen@example.com",
    "display_name": "Jenny Rosen",
    "configuration": {
        "customer": {}
    },
    "include": [
        "configuration.customer"
    ]
  }'
```

#### Customers v1

```curl
curl https://api.stripe.com/v1/customers \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "name=Jenny Rosen" \
  --data-urlencode "email=jenny.rosen@example.com"
```

## Grant billing credits to your customer

Use the Stripe Dashboard or API to create a credit grant for your customer.

> #### Credits are burned down at the end of the billing period
> 
> With this version of usage-based billing, credits are burned down when the invoice is created at the end of the billing period. [Advanced usage-based billing](https://docs.stripe.com/billing/subscriptions/usage-based/advanced/compare.md), currently in private preview, lets you set up credit grants that burn down in real time.

Billing credits only apply to [subscription](https://docs.stripe.com/api/invoices/object.md#invoice_object-subscription) line items that link to a [meter price](https://docs.stripe.com/api/prices/object.md#price_object-recurring-meter). The [Usage Records API](https://docs.stripe.com/api/usage_records.md) isn’t supported.

#### Dashboard

1. On the [Customers](https://dashboard.stripe.com/test/customers) page, select the customer name.
2. On the customer page, under **Credit grants**, click the plus (**+**) symbol.
3. On the **New credit grant** page, do the following:

- For **Name**, enter a name for your credit grant.
- For **Amount**, specify the amount of the credit grant. For the Hypernian example, enter 10.
- (Optional) Under **Effective date**, specify a date for when to grant the credit.
- (Optional) Under **Expiry date**, specify the date, if any, when the credits expire.
- (Optional) Under **Priority**, specify the priority for this credit grant.
- (Optional) Under **Eligibility**, specify a list of usage-based prices that this credit grant applies to.
- Click **Create grant**.

#### API

#### Accounts v2

```curl
curl https://api.stripe.com/v1/billing/credit_grants \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer_account={{CUSTOMERACCOUNT_ID}}" \
  -d "name=Credit grant" \
  -d "applicability_config[scope][price_type]=metered" \
  -d category=paid \
  -d "amount[type]=monetary" \
  -d "amount[monetary][value]=1000" \
  -d "amount[monetary][currency]=usd"
```

#### Customers v1

```curl
curl https://api.stripe.com/v1/billing/credit_grants \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "name=Credit grant" \
  -d "applicability_config[scope][price_type]=metered" \
  -d category=paid \
  -d "amount[type]=monetary" \
  -d "amount[monetary][value]=1000" \
  -d "amount[monetary][currency]=usd"
```

## Create a subscription

[Subscriptions](https://docs.stripe.com/api/subscriptions.md) allow you to charge recurring amounts by associating a customer with a specific price.

Use the Stripe Dashboard or API to create a subscription that includes your customer, product, and usage-based price.

For the Hypernian example, you create a subscription for both the Hypernian Input Token and Hypernian Output Token products, billed monthly to Jenny Rosen.

> You can associate a single metered price with one or more subscriptions.
> 
> When you create a `billing_mode=flexible` subscription, Stripe excludes metered line items from the first invoice since no prior usage exists to bill. Stripe creates an invoice only if the subscription is backdated with previously accrued usage or if pending invoice items exist. When you create a `billing_mode=classic` subscription, Stripe generates a zero monetary value invoice line item for each metered subscription item.

#### Dashboard

1. On the [Subscriptions](https://dashboard.stripe.com/test/subscriptions) page, click **Create test subscription**.
2. On the **Create a test subscription** page, do the following:
   - Under **Customer**, select the name of your customer. For the Hypernian example, select **Jenny Rosen**.
   - Under **Product**, select your prices. For the Hypernian example, select the price under **Hypernian Input Usage** and **Hypernian Output Usage**.
   - (Optional) Modify the subscription details and settings as needed.
   - Click **Create test subscription**.

#### API

Locate your customer ID on the customer details page. To locate your price IDs, go to each product details page and click the overflow menu (⋯) under **Pricing**. Select **Copy price ID**.

#### Accounts v2

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer_account={{CUSTOMERACCOUNT_ID}}" \
  -d "items[0][price]={{INPUT_PRICE_ID}}" \
  -d "items[1][price]={{OUTPUT_PRICE_ID}}"
```

#### Customers v1

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "items[0][price]={{INPUT_PRICE_ID}}" \
  -d "items[1][price]={{OUTPUT_PRICE_ID}}"
```

## Send a test meter event

Use [Meter Events](https://docs.stripe.com/api/billing/meter-event.md) to [record customer usage](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage.md) for your meter. At the end of the billing period, Stripe bills the reported usage.

You can test your usage-based billing by sending a meter event through the Stripe Dashboard or API. When using the API, specify the customer ID and value for the `payload`.

After you send meter events, you can view usage details for your meter on the [Meters](https://dashboard.stripe.com/test/meters) page in the Dashboard.

#### Dashboard

1. On the [Meters](https://dashboard.stripe.com/test/meters) page, select the meter name. For the Hypernian example, select **Hypernian Input tokens**.
2. On the meter page, click **Add usage** > **Manually input usage**.
3. On the **Add usage** page, do the following:
   - Select your customer from the **Customer** dropdown.
   - For **Value**, enter a sample value. For the Hypernian example, enter `3000`.
   - Click **Submit**.

#### API

```curl
curl https://api.stripe.com/v1/billing/meter_events \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d event_name=hypernian_input_tokens \
  -d "payload[stripe_customer_id]={{CUSTOMER_ID}}" \
  -d "payload[value]=3000"
```

## Create a preview invoice

[Create a preview invoice](https://docs.stripe.com/api/invoices/create_preview.md) to see a preview of a customer’s invoice that includes details such as the meter price and usage quantity.

#### Dashboard

1. On the [Subscriptions](https://dashboard.stripe.com/test/subscriptions) page, select a subscription. For the Hypernian example, select the subscription for **Jenny Rosen**.

2. On the subscription details page, scroll down to the **Upcoming invoice** section. The preview invoice shows the subscription amount to bill the customer on the specified date.

3. Click **View full invoice** to see complete details for the upcoming invoice, including:

   - Customer
   - Billing method
   - Creation date
   - Connected subscription
   - Subscription details (usage quantity and meter price)
   - Amount due

   Because Stripe processes meter events asynchronously, upcoming invoices might not immediately reflect recently received meter events.

#### API

```curl
curl https://api.stripe.com/v1/invoices/create_preview \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "subscription={{SUBSCRIPTION_ID}}"
```

## Apply billing credits to invoices

After the invoice finalizes, Stripe automatically applies all applicable billing credits. The available balance on the credit grant updates based on the amount of billing credits applied to the invoice.

You can find the amount of billing credits applied to an invoice in the Stripe Dashboard.

1. On the [Customers](https://dashboard.stripe.com/test/customers) page, select the customer name.
2. On the customer page, under **Invoices**, select an invoice.
3. On the invoice page, under **Subtotal**, find the line for **Credit grant applied**.

## Retrieve the available billing credit balance

Use the Stripe Dashboard or API to see the available billing credit balance for a customer. When using the API, retrieve the [Credit Balance Summary](https://docs.stripe.com/api/billing/credit-balance-summary/retrieve.md) endpoint.

#### Dashboard

1. On the [Customers](https://dashboard.stripe.com/test/customers) page, select the customer name.
2. On the customer page, under **Credit grants**, find the list of credit grants that can apply to invoices. You can see the credit grant’s [available_balance](https://docs.stripe.com/api/billing/credit-balance-summary/object.md#billing_credit_balance_summary_object-balances-available_balance) in the **Available** column.

#### API

#### Accounts v2

```curl
curl -G https://api.stripe.com/v1/billing/credit_balance_summary \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer_account={{CUSTOMERACCOUNT_ID}}" \
  -d "filter[type]=applicability_scope" \
  -d "filter[applicability_scope][price_type]=metered"
```

#### Customers v1

```curl
curl -G https://api.stripe.com/v1/billing/credit_balance_summary \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "filter[type]=applicability_scope" \
  -d "filter[applicability_scope][price_type]=metered"
```

## List transactions for a credit grant

Use the Stripe Dashboard or API to see the transactions for a specific credit grant or customer. When using the API, call the [Credit Balance Transaction](https://docs.stripe.com/api/billing/credit-balance-transaction/list.md) endpoint.

#### Dashboard

1. On the [Customers](https://dashboard.stripe.com/test/customers) page, select the customer name.
2. On the customer page, under **Credit grants**, select a credit grant.
3. View details for the credit balance transactions.

#### API

#### Accounts v2

```curl
curl -G https://api.stripe.com/v1/billing/credit_balance_transactions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer_account={{CUSTOMERACCOUNT_ID}}" \
  -d credit_grant={{CREDIT_GRANT_ID}}
```

#### Customers v1

```curl
curl -G https://api.stripe.com/v1/billing/credit_balance_transactions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d credit_grant={{CREDIT_GRANT_ID}}
```

## Optional: Fund the credit grant

Use the Stripe Dashboard or API to create a one-off [invoice](https://docs.stripe.com/invoicing.md) to collect payment from a customer. When using the API, listen for the `invoice.paid` [webhook](https://docs.stripe.com/webhooks.md) and grant billing credits to your customer.

#### Dashboard

1. On the [Customers](https://dashboard.stripe.com/test/customers) page, select the customer name.
2. On the customer page, click **Create invoice**.
3. Follow the instructions to [create an invoice](https://docs.stripe.com/invoicing/dashboard.md).

#### API

#### Accounts v2

```curl
curl https://api.stripe.com/v1/invoices \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer_account={{CUSTOMERACCOUNT_ID}}" \
  -d "description=credit purchase" \
  -d collection_method=charge_automatically
```

```curl
curl https://api.stripe.com/v1/invoiceitems \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer_account={{CUSTOMERACCOUNT_ID}}" \
  -d "description=billing credits purchase" \
  -d unit_amount_decimal=1000 \
  -d currency=usd \
  -d invoice={{INVOICE_ID}}
```

#### Customers v1

```curl
curl https://api.stripe.com/v1/invoices \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "description=credit purchase" \
  -d collection_method=charge_automatically
```

```curl
curl https://api.stripe.com/v1/invoiceitems \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "description=billing credits purchase" \
  -d unit_amount_decimal=1000 \
  -d currency=usd \
  -d invoice={{INVOICE_ID}}
```

```curl
curl https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/finalize \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d auto_advance=true
```

## Optional: Retrieve usage for a custom time period

Use the [Meter Event Summary](https://docs.stripe.com/api/billing/meter-event-summary.md) to retrieve total usage for a custom time period. The meter event summary returns a customer’s aggregated usage for a period, based on the aggregation formula defined by the meter. If you represent your customers as customer-configured [Accounts](https://docs.stripe.com/api/v2/core/accounts/object.md), pass the `Account` ID to the `customer` parameter.

In the Hypernian example, the meter event summary returns the sum of tokens for a specific customer, meter, and time window.

Because Stripe processes meter events asynchronously, meter event summaries might not immediately reflect recently received meter events.

```curl
curl -G https://api.stripe.com/v1/billing/meters/{{METER_ID}}/event_summaries \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d customer={{CUSTOMER_ID}} \
  -d start_time=1717249380 \
  -d end_time=1717249440
```
