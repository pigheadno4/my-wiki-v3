<!-- Source URL: https://docs.metronome.com/guides/implement-metronome/core-concepts/create-billable-metrics.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create billable metrics

A billable metric is a customizable query that filters and aggregates events from your event stream. These metrics are tracked continuously as usage enters Metronome through the ingestion pipeline. The ingestion process transforms raw usage data into actionable pricing metrics, enabling you to accurately meter and bill for your products. This is what is ultimately used to calculate the *quantity* for invoice line items, and can be used for alerts.

Billable metrics are a foundational piece of the pricing model within Metronome. Once billable metrics are created, they contribute to an invoice as follows:

* Billable metrics are associated with [products](/guides/get-started/core-concepts/create-products-contracts), which is where you set the presentation layer for how line items should be displayed on an invoice.
* List prices are defined for products as rates on a [rate card](/guides/get-started/core-concepts/create-manage-rate-cards).
* Rates can be associated or overwritten on a [contract](/guides/get-started/core-concepts/provision-customer), which is where invoices are generated for each Metronome customer. Quantities for each of the line items are calculated from events using the billable metric definition.

Implementing billable metrics in Metronome involves these steps:

1. Identify usage components to price on.
2. Identify the desired scale and latency needed for invoice calculations.
3. Define `Group keys` to organize your metric data.
4. Define filters and an aggregation strategy to identify and accumulate relevant events from your usage stream.

## 1. Identify usage components​

Before implementing your billable metrics, determine the factors that contribute to your usage-based billing. You should consider what aspects of your service your customers value most, what they would expect to see on a final invoice, and what data elements you have available to send to Metronome. Some example metrics may include:

* Number of API calls
* Number of input and output tokens consumed
* Storage used (GB hours)
* Number of users

Designing billable metrics goes hand-in-hand with designing usage events. While your usage events may include a number of relevant properties that you may want to price on, your billable metrics should individually align to the component that you may want to meter.

For example, your usage event could be a heartbeat from a server that contains CPU utilization, memory used, and cloud region. If you would like each of these usage components to contribute to a user’s pricing, create separate metrics to aggregate the value from each property.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/TrrblT2KR7zYyGbN/images/docs/get-started/core-concepts/billable-metrics/billable-metrics-1-be008dcf69b0ae2a81d99524274fe228.png?fit=max&auto=format&n=TrrblT2KR7zYyGbN&q=85&s=ecb3da455d873e1aee54c2711b1315bf" alt="Usage components" width="2434" height="1372" data-path="images/docs/get-started/core-concepts/billable-metrics/billable-metrics-1-be008dcf69b0ae2a81d99524274fe228.png" />
</Frame>

For more information on what to consider before designing your usage events, please review our [Design usage events](/guides/events/design-usage-events) guide.

## 2. Identify desired scale and latency​

Before implementing your billable metrics, consider the scale of events that you send to Metronome for a particular metric.

Metronome offers two types of billable metrics:

* **Streaming billable metrics** : metrics designed for ultra low latency and high throughput workflows. Use Streaming billable metrics if:
  * Your metric definitions can be defined through a set of simple filters and aggregations (e.g. `COUNT`, `SUM`, `MAX`, or `LATEST`).
  * You require real-time [alerting](/guides/customers-billing/set-up-notifications/create-and-manage-notifications) across a wide customer base with a high event volume.

### Streaming billable metric aggregation types

Streaming billable metrics support four aggregation types: `COUNT`, `SUM`, `MAX`, and `LATEST`. All four are available everywhere—UI, API, Plans, and Contracts.

`LATEST` returns the most recent value for the property within the billing period—useful for metrics where you want to bill on a point-in-time reading (for example, the latest reported seat count or storage size) rather than a sum or max across the period.

If you need to count distinct values (for example, unique users), use a [SQL billable metric](/guides/implement-metronome/core-concepts/billable-metrics-sql-editor) with `count(distinct …)`.

<Info>
  **INFO**

  When using streaming billable metrics, the billable metric must be defined in Metronome before any usage can be associated with it. If usage is sent before a streaming metric is defined, it isn't attributed to the metric by default. Since Metronome retains all raw events received, we can perform a reflow if you ever need past events to apply to a new streaming billable metric — reach out to your Metronome representative to get this performed.
</Info>

* **SQL billable metrics** : metrics designed with SQL queries to support more complex calculations.
  * Used if the desired billable metrics are not satisfied by the basic filters provided in streaming billable metrics.

<Info>
  **INFO**

  For many alerting workloads, SQL billable metrics will have comparable performance to streaming billable metrics. For complex queries or high numbers of SQL billable metrics, the Metronome team can help provide guidance to achieve desired latency. Please reach out to your Metronome team if you are interested in using SQL billable metrics with alerts.
</Info>

## 3. Define group keys​

`Group keys` are used in Metronome to specify one or more properties that can be used to break out usage in downstream pricing and packaging. This functions similarly to a `group by` clause in a SQL query. Group keys must first be defined in the metrics layer in order to be available to use in downstream pricing and packaging. A given billable metric can have many group keys.

Group keys help support the following use cases in the platform:

* **Presentation group keys** allow you to separate out quantities on an invoice by a particular property value.
  * For example, if you specify `user_id` as a group key, you can display usage on an invoice broken out by each `user_id` . This is useful for attributing spend across a larger organization.
* **Pricing group keys** form the basis for [dimensional pricing](/guides/get-started/core-concepts/create-manage-rate-cards#dimensional-pricing%E2%80%8B) and allow you to price a metric differently based on property values.
  * For example, if you specify properties `[cloud_service_provider, region]` as a group key, you can set up separate rates for events with different values of this property.
    * Events with properties `cloud_service_provider=aws` and `region=us-east-1` are priced at \$0.50
    * Events with property `cloud_service_provider=azure` and `region=southindia` are priced at \$0.40

If you create a product that uses both presentation and pricing group keys, you need to define all of the properties across both keys in one compound group key. For instance, if you want a product to support both of the examples above—presentation group key on `user_id` and pricing group key on `[cloud_service_provider, region]` , create a group key on the billable metric that looks like `[user_id, cloud_service_provider, region]` .

<Note>
  **CONFIGURATION NOTE**

  Using group keys with many possible values for a given customer can increase latency when calling the Metronome API. If you anticipate the cardinality of these possible values reaching one thousand, contact your Metronome representative to discuss your configuration.
</Note>

### Define group keys on streaming billable metrics​

Group keys for streaming billable metrics are defined through the basic filters editor, or through the [create billable metric](/api-reference/billable-metrics/create-a-billable-metric) API endpoint. To include a property in a group key, it must be first defined in the property filters with an `Exists` or `In` filter. Group keys are not editable once a metric is created, so it is important to consider if they are needed for your invoice presentation or pricing when creating your billable metrics.

### Define group keys on SQL billable metrics​

When defining a SQL billable metric, any property returned by your SQL query outside of the `value` column can be used as a group key. For example, to use the property `user_id` as a presentation group key, and `region` as a pricing group key, your SQL query may look like:

```sql theme={null}
SELECT count() as value, properties.user_id, properties.region  
FROM events  
WHERE event_type = 'api_request'  
GROUP BY user_id, region
```

## 4. Define filters and aggregations for relevant events​

Once you have the pricing elements from your usage stream that you would like to see represented in Metronome, you must implement your billable metric definition. Metronome offers two tools for defining Billable Metrics:

* [Basic Filters editor](/guides/get-started/core-concepts/billable-metrics-basic-filters/) A user-friendly interface with predefined filters and aggregations, suitable for most basic use cases.

<Info>
  **INFO**

  All metrics created with the Basic Filters editor are created as streaming billable metrics.
</Info>

* [SQL Editor](/guides/get-started/core-concepts/billable-metrics-sql-editor/) A more flexible option allowing custom SQL queries for complex scenarios. All metrics created with the SQL editor are created as SQL billable metrics.

## 5. Send and trace events to test your billable metric​

Once you've created your billable metric, send some events to make sure they are correctly matching as expected. Use the [ingest](/api-reference/usage/ingest-events) endpoint to send your test events, then call the [searchEvents](/api-reference/usage/search-events) endpoint with the events' `transaction_ids`. The response contains the list of matched billable metrics, as well as the matched customer if it exists. If you've set up a matching customer and matching billable metric, but do not see these values populated, you can dig into the billable metric definition to see if anything is incorrectly defined.
