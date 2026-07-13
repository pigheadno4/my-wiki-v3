<!-- Source URL: https://docs.metronome.com/guides/events/high-volume-ingestion.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Usage events at scale

As your business grows, your event volume will grow with it. Your billing architecture needs to support everything from initial product launches to sudden spikes in adoption, without introducing delays or hitting unexpected processing limits.

Metronome’s infrastructure is designed to provide this reliability at scale. We support companies who send billions of events per day and rely on Metronome to accurately calculate their millions of end-customer’s billing in real-time. This guide outlines how Metronome's architecture is built for scale and how you can leverage its capabilities to ensure data integrity as you grow.

## High throughput event ingest

Metronome's infrastructure supports up to 110,000 events per second (6.6 million events per minute) without requiring pre-aggregation or rollups. Default ingest rate limit starts at 5,000 events per second. If you need higher throughput, contact Metronome to increase it.

When scaling to send high event volumes, batching your events helps you take full advantage of this capacity. You can batch 100 events per request sent to Metronome’s ingest endpoint. To do so, submit an array of usage event objects using a POST request and sending events whose schema matches the structure outlined.

Learn more about sending usage to Metronome [here](/guides/events/send-usage-events).

```bash theme={null}
curl https://api.metronome.com/v1/ingest \
  -H "Authorization: Bearer <API_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '[
  {
    "transaction_id": "event-20250910-001",
    "customer_id": "customer_123",
    "timestamp": "2025-09-10T12:00:00Z",
    "event_type": "ai-run",
    "properties": {
      "model_name": "gpt-5",
      "input_tokens": "10000",
      "output_tokens": "1000",
      "type": "input"
    }
  },
  {
    "transaction_id": "event-20250910-002",
    "customer_id": "customer_456",
    "timestamp": "2025-09-10T12:05:00Z",
    "event_type": "ai-run",
    "properties": {
      "model_name": "gpt-4o",
      "input_tokens": "8000",
      "output_tokens": "900",
      "type": "output"
    }
  }
  // additional 98 events objects
]'
```

## Monitor event data in the UI

The Metronome UI offers direct access to inspect your event pipeline through our dedicated event explorer. This feature is useful to validate that Metronome has successfully ingested events, that they've been successfully matched to Metronome objects like [Billable Metrics](/guides/get-started/core-concepts/create-billable-metrics), and to identify duplicate events. With the events UI, you can:

* See summary-level time-based entire event stream or isolated duplicate event graphs
  * Includes custom time-frame viewing options
* Search by customer, duplicates, billable metrics, and transaction IDs
* View complete usage event payloads from individual events
* View usage event attribution to matched customer and [billable metrics](/guides/get-started/core-concepts/create-billable-metrics)
* Export a CSV event log

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/AzoEmRc69c1nBkjv/images/docs/guides/implement-metronome/event-stream.png?fit=max&auto=format&n=AzoEmRc69c1nBkjv&q=85&s=d7235e8d5f6a47329cf2ae6c45700e20" alt="Event stream in Metronome UI" width="2522" height="1054" data-path="images/docs/guides/implement-metronome/event-stream.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/RmXuQ2v0AyTvK_BJ/images/docs/guides/implement-metronome/event-summary.png?fit=max&auto=format&n=RmXuQ2v0AyTvK_BJ&q=85&s=9fd66d6d671396c5bce0769b65c75df2" alt="Event summary in Metronome UI" width="2138" height="806" data-path="images/docs/guides/implement-metronome/event-summary.png" />
</Frame>

## Maintaining data integrity at scale

The Metronome UI is great for spot-checking and quick validation. For sustained reliability at high volumes, you’ll want automated, programmatic checks that run continuously and alert you before issues affect customers or revenue. Use the guidance below to build a more scalable event posture.

High-volume event ingestion  requires effective monitoring and maintenance of your event pipeline. Metronome provides end-to-end visibility and self-serve tooling to help you resolve issues before they impact your business.

* **Queue and Retry:** You should follow industry-standard best practices around queueing, retries, message queue logging, alerting, and use of dead-letter queues. Please see [here](guides/get-started/core-concepts/send-usage-events#queue-and-retry) for Metronome’s recommendations.
* **Usage Pipeline Observability:** Metronome's [**Event Search API**](/api-reference/usage/search-events) allows you to sample raw events and validate that they are matching active billable metrics. This is a critical control for preventing silent revenue loss if an upstream system changes an event schema.
* **Seamless Backfills and Recovery:** If an incident occurs, you need to be able to recover data quickly. Metronome offers a 34-day historical ingest and deduplication window processed through the same [ingest endpoint](/api-reference/usage/ingest-events). This extended window ensures you can replay more than 24 hours of traffic and re-rate draft invoices and credit ledgers in real time.

  Corrections beyond 34 days is handled by our operations team and is usually completed promptly.
