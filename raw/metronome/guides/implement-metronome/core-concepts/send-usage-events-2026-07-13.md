<!-- Source URL: https://docs.metronome.com/guides/implement-metronome/core-concepts/send-usage-events.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Send usage events

After [designing your usage events](/guides/events/design-usage-events), send them to Metronome. This guide describes what data to send and best practices to ensure event accuracy.

<Info>
  **INFO**

  Send usage events to Metronome through the [/ingest](/api-reference/usage/ingest-events) endpoint or by [connecting Metronome to Segment](/integrations/platform-integrations/segment).
</Info>

## Usage event structure

A usage event is a JSON object with the following fields:

```json theme={null}
{  
  "transaction_id": "string", // (required) unique identifier for this event  
  "customer_id":    "string", // (required) which customer the event applies to  
  "timestamp":      "string", // (required) when the event happened  
  "event_type":     "string", // (required) the kind of event, such as page_view or sent_email  
  "properties":     {}, // (optional) key/value pairs with event details  
}
```

* **transaction\_id**

  Metronome uses the `transaction_id` to ignore duplicate events. Once a usage event is accepted with a given transaction ID, subsequent events within the next 34 days with the same ID are treated as duplicates and ignored.

* **customer\_id**

  The `customer_id` specifies which of your customers is responsible for any billing associated with the event. There are two ways to identify a Metronome customer in usage events: a customer ID or an  *ingest alias*. Ingest aliases are useful when sending events using an identifier from your system, such as an email address or account number.

  Each customer in Metronome may have multiple ingest aliases, and usage events with a `customer_id` matching any of those aliases can be attributed towards that customer's usage.

* **timestamp**

  The `timestamp` must be an [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) string with a 4-digit year, such as `2025-01-23T01:23:45Z`. When querying usage data or producing an invoice, this field is used to select only events that happened in a certain time range. Timestamps more than 24 hours in the future are rejected by the API.

* **event\_type**

  The `event_type` works along with the `properties` map to describe the details of the event. For example, a content delivery network (CDN) might generate events of the type `http_request` with properties like `domain` and `bytes_sent` to support billing based on data transfer. They might also generate a different type of event, `cache_invalidation`, with a property `number_of_files`. You can name title the `event_type` as needed, but for more insights check out how to [design billable metrics](/guides/get-started/core-concepts/create-billable-metrics/).

* **properties**

  All keys and values in the `properties` map should be represented as strings, even though the values are often numeric. This prevents the loss of precision that often occurs in systems that use floating point numbers. Internally, Metronome uses arbitrary precision decimals to provide exact results of computation. Again, we advise sharing more data here than you might need initially so you can flexibly utilize this later on if need be.

## Queue and retry​

If usage events are lost on their way to Metronome, you’ll lose revenue. If you're sending events through the API, you need to be resilient to failures such as network issues or process crashes. A good way to gain this resilience is to put your usage events on a reliable queue such as [Amazon SQS](https://aws.amazon.com/sqs/) or [RabbitMQ](https://www.rabbitmq.com/), and have a process pull from that queue and push events to Metronome.

If your call to the Metronome `/ingest` endpoint fails with a network error or a `5xx` HTTP status code, some of your events may have been ingested, but others may not. Always retry a failed call to `/ingest` until you receive a `200` status code. The unique `transaction_id` in each event prevents duplicate processing, so retries are always safe.

If your call to the Metronome `/ingest` endpoint fails with a `429` HTTP status code, you have exceeded one of our rate limits. In this case, you should back off and retry the call after a delay. If the request continues to be rate-limited, wait for an exponentially increasing amount of time between retries.

<Warning>
  **AVOID AUTO-RETRIES ON 4XX**

  If a call to `/ingest` fails with a `4xx` HTTP status code (besides `429`), this indicates an issue with the payload. **Do not** automatically retry such a call. Instead, put the event aside in a [dead letter queue](https://en.wikipedia.org/wiki/Dead_letter_queue) and trigger an alarm so you can investigate the failure and resolve the issue.
</Warning>

## Message queue logging​

When first integrating with Metronome, it's helpful to enable logging in your message queue. This lets you audit exactly what usage events are being sent to Metronome. Also enabling logging any time you make a change to your usage events.

## Trial ingestion resilience​

To test your system’s response to elevated error rates from Metronome’s API, Metronome can set up an automatic failure rate of your choice (we recommend 20%). Contact your Metronome representative to specify the % failure rate, when to enable and disable the test, and if you'd like to apply it to your sandbox or production instance.

### Aggregation​

A billable metric aggregates over a single property by default. For example, if you're an email sending service, you might have a usage event that looks like:

```json theme={null}
{  
  "event_type": "email_sent",  
  "properties": {  
    "num_recipients": "8",  
    "size": "1000"  
  },  
  // ...  
}
```

Already, this event supports charging customers based on how many emails they sent or the maximum size of an email. For further aggregation, like total data sent (`num_recipients` \* `size`), use [SQL-based billable metrics](/guides/get-started/core-concepts/billable-metrics-sql-editor/).

## Heartbeat event idempotence​

Usage events typically fall into one of two categories: an event that occurs when a user takes some action, or a periodic "heartbeat" that measures the current state—a common approach in infrastructure services. For example, a service selling computation might send a per-node heartbeat to Metronome each minute describing the CPU and disk utilization on that node. These events could be aggregated into the metrics "CPU minutes" and "gigabyte minutes."

It's important for heartbeat events to ensure that usage is only counted once. This is accomplished by choosing a deterministic `transaction_id` for duplicate events to have the same ID. Metronome guarantees that only one event with a given `transaction_id` is processed.

In the example of a per-node per-minute heartbeat, you might structure a transaction ID as follows:

```bash theme={null}
<node id>_<floor(unix_now()/60)>
```

where `unix_now()` is a function that returns the number of seconds since the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time). By including both the node ID and a minute-granularity timestamp in the transaction ID, it's guaranteed that duplicate events from the same node in the same minute is ignored.

Using this type of `transaction_id` means you also don't have to worry about sending events too often. We recommend sending  *two or more heartbeats* per measurement period. Duplicates are safely ignored, and by using this approach, you decrease the risk of missing a measurement period due to timer imprecision or a temporary delay.

<Warning>
  **CHANGES TO USAGE EVENTS MAY CAUSE BREAKAGES**

  Usage events are designed to target very specific billable metrics, so if the data structure changes, it could prevent downstream metrics from being properly recorded. It's best to work with your Metronome representative any time you are adjusting the structure of your usage events. We can help validate and test the change with you to avoid any disruption.
</Warning>

## Ensure Metronome does not block critical paths

Metronome has been expressly designed to use safely in the most critical parts of your application. In accordance with availability best practices, we suggest verifying that Metronome is not a blocker in your customer creation path. Since Metronome can match events sent at any time before or after customer creation using ingest aliases, we recommend creating the customer in your system first—then creating the matching customer record in Metronome asynchronously.
