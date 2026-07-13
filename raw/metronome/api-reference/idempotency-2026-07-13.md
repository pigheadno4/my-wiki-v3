<!-- Source URL: https://docs.metronome.com/api-reference/idempotency.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# API idempotency

This page describes how Metronome supports idempotency so you can safely retry requests without creating duplicate data. Idempotency ensures operations like creating customers or ingesting usage events succeed exactly once, even when requests are retried due to network issues, timeouts, or client logic.

Metronome provides built-in idempotency mechanisms so you can safely retry requests without introducing extraneous data.

## How Metronome supports idempotency

Metronome uses different idempotency mechanisms depending on the type of data:

| Method                       | Where used                           | Scope                        | Conflict behavior                                        | Retention                                  |
| ---------------------------- | ------------------------------------ | ---------------------------- | -------------------------------------------------------- | ------------------------------------------ |
| **Transaction ID**           | Event ingestion (`/ingest`, Segment) | Usage events                 | Ignores subsequent events with the same ID               | 34 days                                    |
| **Ingest alias**             | Customer writes (create or update)   | Customers                    | Returns `409 Conflict` if ingest alias is already in use | Until released                             |
| **`uniqueness_key`**         | Resource creation                    | Select resources (see below) | Returns `409 Conflict`                                   | Until released (only available for Alerts) |
| **`Idempotency-Key` header** | POST API requests                    | Request cache                | Returns `409 Conflict` if parameters differ              | ≥ 24 hours                                 |

## Event ingestion

[Usage events](/guides/get-started/core-concepts/send-usage-events) stream to Metronome at high scale. To prevent duplicates, Metronome uses the `transaction_id` field as an idempotency key.

Once a usage event has been accepted with a given transaction ID, Metronome ignores subsequent events with the same transaction ID within the next 34 days. This allows you to safely retry sending events without risk of duplication.

## Ingest aliases

[Ingest aliases](/guides/get-started/core-concepts/provision-customer#understand-ingest-aliases%E2%80%8B) map your internal customer identifiers to a Metronome customer ID. When you send usage keyed on an ingest alias, Metronome automatically associates it with the correct customer.

Ingest aliases are also naturally idempotent, preventing the creation of duplicate customer entities or conflicting records.

<Warning>
  **MOVING INGEST ALIASES**

  Due to the idempotent nature of ingest aliases, you can move an ingest alias between customers only if you first remove it from the original customer. This rule applies to both archived and active customers.
</Warning>

## API requests

Metronome supports two methods of ensuring idempotency through the REST API:

* Using uniqueness keys (on select endpoints)
* Using the Idempotency-Key header

### Uniqueness keys

Metronome supports idempotency for commonly created resources in Metronome by accepting a `uniqueness_key` field in the request payload. This uniqueness key is stored as part of the resource in Metronome, and Metronome ensures that no resources can share the same uniqueness key. If you attempt to create a resource with a uniqueness key already in use, you receive an HTTP `409 Conflict` error with message *“This uniqueness key has already been used.”*

Examples of resources with uniqueness keys:

* [Contract](/api-reference/contracts/create-a-contract)
* [Alert](/api-reference/alerts/create-an-alert)
* Customer-level commits and credits
* Contract edits \[coming soon]

### Idempotency-Key header

Metronome recommends using an `Idempotency-Key` header for endpoints that don’t include a dedicated uniqueness key. Metronome supports sending an `Idempotency-Key` header for all POST endpoints. If the `Idempotency-Key` header is provided and the request begins executing (it passes validation and doesn't conflict with another concurrent request), the results of the API call are persisted, and the same results returned.

**Behavior:**

* Keys must be unique per request
* Retrying with the same key and identical parameters returns the original result.
* Retrying with the same key but different parameters returns **HTTP `409 Conflict`**.
* Metronome retains idempotency keys for at least 24 hours.
* Idempotency applies even if a request returns an HTTP 500 error, meaning Metronome will cache and return the error

**Understand idempotency with errors**:

When a request with `Idempotency-Key` header returns an error, Metronome caches the error and returns it for subsequent retries with the same idempotency key. **This behavior follows industry best practices**—when an operation fails midway, retries without manual review can make the situation worse. In these situations, Metronome caches and returns the error to ensure you see the failure consistently, investigate the state of the system, and decide whether to retry or resolve manually.

## Best practices

* **Generate deterministic keys for resource-based idempotency**: Derive keys from business logic (for example, hash of external ID and operation type) so retries always reuse the same key.
* **Use random keys when appropriate**: Generate UUIDs if you don’t need deterministic keys (e.g., `Idempotency-Key` header).
* **Match retries to key lifetime**:
  * Usage events: retry within 34 days.
  * REST API writes: retry within 24 hours.
* **Prefer uniqueness keys when available**: Use `uniqueness_key` for resource creation like contracts instead of the `Idempotency-Key` header.
* **Implement safe retries**: Always retry with exponential backoff and reuse the same key.
