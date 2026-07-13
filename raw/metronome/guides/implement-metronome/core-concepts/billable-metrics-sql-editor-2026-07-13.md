<!-- Source URL: https://docs.metronome.com/guides/implement-metronome/core-concepts/billable-metrics-sql-editor.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create SQL billable metrics

Billable metrics defined using the SQL Editor are formatted as SQL queries that are run against a table called `events`, which includes all of the raw usage events that are sent in to Metronome. Similar to the Basic Filters editor, billable metric SQL queries should include a set of filters that identify the correct usage events to query over, and an aggregation to turn these events into a value that Metronome will use as the quantity for downstream line items.

Metronome handles filtering down the SQL queries for individual customers over the course of their billing period. You do not need to include this logic in your queries - simply focus on filtering and aggregation!

## Supported features and functionality​

Here is how you can access elements of your usage event within the query:

* Query the `events` table
* You can access the event\_type field in the SQL editor by using `event_type`
* You can access the timestamp field in the SQL editor by using `timestamp`
* You can access any fields in the properties dictionary by using `properties.field_name`

If your query returns more than one column, Metronome first looks for a column called `value` to use as the column for the metric quantity. If no column `value` exists, Metronome uses the first column returned in the query. Any other columns returned can be used as group keys in downstream pricing and packaging.

<Info>
  **INFO**

  If extra columns are returned but are not used as presentation or pricing group keys, Metronome sums over all of the results to generate a single quantity for the metric.
</Info>

## Supported functions and operators​

The SQL Editor supports these functions and operators.

* **Aggregations**
  * `COUNT`: Counts the number of rows
  * `SUM`: Sums numbers
  * `MAX`: Takes the maximum of numbers
  * `MIN`: Takes the minimum of numbers
  * `AVG`: Averages numbers
  * `EARLIEST`: Returns the earliest value of a column based on its `timestamp`
  * `LATEST`: Returns the latest value of a column based on its `timestamp`
  * `COUNT DISTINCT`: Counts the distinct values in the expression
* **Math**
  * `+`, `-`, `*`, `/`
  * `=`, `!=`, `>`, `<`, `≥`, `≤`
  * `LEAST`: Returns the least of its arguments
  * `GREATEST`: Returns the maximum of its arguments
  * `ROUND`: Rounds a number to a specified number of decimal places
  * `CEIL`: Returns the smallest integer value that is greater or equal to the input
  * `FLOOR`: Returns the largest integer value that is less than or equal to the input
* **Logic**
  * `AND`
  * `OR`
  * `NOT`
  * `CASE WHEN`
  * `IS NULL`
  * `IS NOT NULL`
  * `IN`
  * `NOT IN`
  * `=`
  * `!=`
* **Dates**
  * `DATE_TRUNC`: Truncates the `timestamp` field to the `hour` or `day`.
* **Casting**
  * `CAST`

## Example creation flow​

As an example of a more complex scenario, use the SQL Editor to create billable metric that tracks the daily average of storage used over a billing period.

1. Navigate to the Billable Metrics section in the [Metronome app](https://app.metronome.com/).
2. Click `+ Add new Billable Metric`.
3. Choose `SQL query`.
4. Name your metric (for example, `Storage latest daily max`).
5. Enter your SQL query:
   ```sql theme={null}
   SELECT SUM(max_daily_storage) / SUM(num_days) as value, user_id, region
   FROM (
       SELECT
           date_trunc('day', timestamp) as date,
           properties.user_id as user_id,
           properties.region as region,
           MAX(properties.storage_used) as max_daily_storage,
           1 as num_days
       FROM events
       WHERE event_type = 'storage_heartbeat'
       GROUP BY date, user_id, region
   )
   GROUP BY user_id, region
   ```

<Info>
  **INFO**

  In this example, `user_id` is returned so that it can be defined as a `presentation_group_key` when creating a product from this metric. This allows you to display invoices broken out by `user_id`. `region` is returned so that it can be defined as a `pricing_group_key`. This would allow you to add different rates for this billable metric for values of `us-east-1`, `us-west-1`, or `ap-south-1`.
</Info>

6. Preview your metric against any existing usage data to ensure the results are correct. When complete, save your metric.

## SQL breakdown granularity

When you create a Product backed by a SQL billable metric, you can select a SQL breakdown granularity. The default value is `hour`, which is appropriate for most use cases. With `hour` granularity, costs are incurred continuously throughout the billing period as usage is ingested. If you want to use the latest value of a metric, or otherwise have a metric that does not make sense when broken down hourly, you can use `service period`.

## Example

Let's walk through a simple example to compare the two granularities. Imagine you have a simple SUM metric built using a SQL billable metric. On day 1 of the customer's billing period, you send in a value of 5. On day 2, you send in a value of 10. On day 3, you send in a value of 15. The customer's billing period spans from 1/1/2026 to 2/1/2026.

With the default `hour` breakdown granularity, costs are incurred as usage is ingested:

* Assuming you schedule that the rate is \$10 from 1/1/2026 to 1/15/2026, and the rate is \$20 from 1/15/2026 onward, all three events will be priced at \$10.
* If you created a credit or commit that applied only to day 2 of the billing period, only the usage value of 10 and corresponding spend of \$100 would apply against the credit or commit.
* When using the `invoice-breakdowns` endpoint, you would see a value of 5 with a total of \$50 incurred on day 1, a value of 10 with a total of \$100 incurred on day 2, and a value of 15 with a total of \$150 incurred on day 3.

If you instead set the SQL breakdown granularity to `service period`, the full quantity of 30 uses will be incurred at the last time window of the billing period:

* The final price for the billing period will be used for the full quantity. For example, if you schedule that the rate is \$10 from 1/1/2026 to 1/15/2026, and the rate is \$20 from 1/15/2026 onward, the full quantity of 30 will be priced at \$20.
* Credits and commits must cover the last instant of the billing period to apply against the spend.
* When using the `invoice-breakdowns` endpoint, the costs will be incurred in the last time window of the billing period.

## Scheduling a change to or from a SQL billable metric on the Contract Product

If you want to change the metric you're using to bill your customers, you can schedule a change to the billable metric associated with a usage product. SQL billable metrics are swappable on products, and the swap can be scheduled to take effect at any point in a billing period — not only at a billing period boundary.

Let's walk through an example where we switch from Billable Metric A to Billable Metric B, both SQL billable metrics, as of 3/15/2026. Assume that the client is using 1st-of-the-month billing.

* Billable metric A takes the `avg` over the field `value` for events that match `average_metric_v1`.
* Billable metric B takes the `avg` over the field `value_new` for events that match `average_metric_v2`.

We have some usage events that match these billable metrics:

* On 3/1/2026, an event with a `value` of 4 is ingested, with an event type `average_metric_v1`
* On 3/2/2026, an event with a `value` of 6 is ingested, with an event type `average_metric_v1`
* On 3/15/2026, an event with a `value_new` of 10 is ingested, with an event type `average_metric_v2`
* On 3/16/2026, an event with a `value_new` of 12 is ingested, with an event type `average_metric_v2`

In the billing period of the update, during the period before the billable metric update is scheduled, we use only Billable Metric A:

* On 3/1/2026, a quantity of 4 is incurred with its corresponding cost.
* On 3/2/2026, the average of 4 and 6 is 5. A quantity of 4 was already incurred on Day 1, so an additonal quantity of 1 is incurred with its corresponding cost.

In the billing period of the update, after the billable metric update, we use a formula to determine what the value of the combined metric is on each day:

* Billable Metric B's value, using all of the event data for the period up to the current day
* plus Billable Metric A's value, using all of the event data until the day of the swap
* minus Billable Metric B's value, using all of the event data until the day of the swap

This means with the above example:

* On 3/15/2026, a quantity of 10 is incurred with its corresponding cost.
* On 3/16/2026, the average of 10 and 12 is 11. A quantity of 1 is incurred with its corresponding cost.

Note that the third part of the formula, Billable Metric B's value using all of the event data until the day of the swap, is 0 in this case because the two earlier events do not match Billable Metric B.
