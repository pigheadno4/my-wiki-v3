<!-- Source URL: https://docs.metronome.com/api-reference/usage/ingest-events.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ingest events

> The ingest endpoint is the primary method for sending usage events to Metronome, serving as the foundation for all billing calculations in your usage-based pricing model. This high-throughput endpoint is designed for real-time streaming ingestion, supports backdating 34 days, and is built to handle mission-critical usage data with enterprise-grade reliability. Metronome supports 100,000 events per second without requiring pre-aggregation or rollups and can scale up from there. See the [Send usage events](/guides/events/send-usage-events) guide to learn more about usage events.

### Use this endpoint to:
Create a customer usage pipeline into Metronome that drives billable metrics, credit drawdown, and invoicing. Track customer behavior, resource consumption, and feature usage

### What happens when you send events:
- Events are validated and processed in real-time
- Events are matched to customers using customer IDs or customer ingest aliases
- Events are matched to billable metrics and are immediately available for usage and spend calculations

### Usage guidelines:
- Historical events can be backdated up to 34 days and will immediately impact live customer spend
- Duplicate events are automatically detected and ignored (34-day deduplication window)

#### Event structure:
Usage events are simple JSON objects designed for flexibility and ease of integration:
```json
{
  "transaction_id": "2021-01-01T00:00:00Z_cluster42",
  "customer_id": "team@example.com",
  "event_type": "api_request",
  "timestamp": "2021-01-01T00:00:00Z",
  "properties": {
    "endpoint": "/v1/users",
    "method": "POST",
    "response_time_ms": 45,
    "region": "us-west-2"
  }
}
```

Learn more about [usage event structure definitions](/guides/events/design-usage-events).

#### Transaction ID
  The transaction_id serves as your idempotency key, ensuring events are processed exactly once. Metronome maintains a 34-day deduplication window - significantly longer than typical 12-hour windows - enabling robust backfill scenarios without duplicate billing.
  - Best Practices:
    - Use UUIDs for one-time events: uuid4()
    - For heartbeat events, use deterministic IDs
    - Include enough context to avoid collisions across different event sources

#### Customer ID
Identifies which customer should be billed for this usage. Supports two identification methods:
  - Metronome Customer ID: The UUID returned when creating a customer
  - Ingest Alias: Your system's identifier (email, account number, etc.) 

Ingest aliases enable seamless integration without requiring ID mapping, and customers can have multiple aliases for flexibility.

#### Event Type:
Categorizes the event type for billable metric matching. Choose descriptive names that aligns with the product surface area.

#### Properties:
Flexible metadata also used to match billable metrics or to be used to serve as group keys to create multiple pricing dimensions or breakdown costs by novel properties for end customers or internal finance teams measuring underlying COGs.




## OpenAPI

````yaml /openapi.json post /v1/ingest
openapi: 3.0.1
info:
  title: Metronome
  version: 1.0.0
servers:
  - url: https://api.metronome.com
    description: Production server
security:
  - bearerAuth: []
tags:
  - name: Customers
    description: >-
      [Customers](https://docs.metronome.com/provisioning/create-customers/) in
      Metronome represent your users for all billing and reporting. Use these
      endpoints to create, retrieve, update, and archive customers and their
      billing configuration.
  - name: Billable metrics
    description: >-
      [Billable
      metrics](https://docs.metronome.com/understanding-metronome/how-metronome-works#billable-metrics)
      in Metronome represent the various consumption components that Metronome
      meters and aggregates.
  - name: Usage
    description: >-
      [Usage
      events](https://docs.metronome.com/connecting-metronome/send-usage-data/)
      are the basis for billable metrics. Use these endpoints to send usage
      events to Metronome and retrieve aggregated event data.
  - name: Products
    description: Products are the items that customers purchase.
  - name: Rate cards
    description: Rate cards are used to define default pricing for products.
  - name: Contracts
    description: >-
      A contract defines a customer’s products, pricing, discounts, commitments,
      and more. Use these endpoints to create and update contracts data.
  - name: Credits and commits
    description: Credits and commits are used to manage customer balances.
  - name: Invoices
    description: >-
      [Invoices](https://docs.metronome.com/invoicing/) reflect how much a
      customer spent during a period, which is the basis for billing. Metronome
      automatically generates invoices based upon your pricing, packaging, and
      usage events. Use these endpoints to retrieve invoices.
  - name: Alerts
    description: >-
      [Alerts](https://docs.metronome.com/connecting-metronome/alerts/) monitor
      customer spending, balances, and other billing factors. Use these
      endpoints to create, retrieve, and archive customer alerts. To view sample
      alert payloads by alert type, navigate
      [here.](https://docs.metronome.com/manage-product-access/create-manage-alerts/#webhook-notifications)
  - name: Custom fields
    description: >-
      [Custom fields](https://docs.metronome.com/integrations/custom-fields/)
      enable adding additional data to Metronome entities. Use these endpoints
      to create, retrieve, update, and delete custom fields.
  - name: Security
    description: >-
      [Security](https://docs.metronome.com/developer-resources/security/)
      endpoints allow you to retrieve security-related data.
  - name: Settings
    description: >-
      Use these endpoints to configure a billing API key, a webhook secret, or
      invoice finalization behavior.
  - name: Named schedules
    description: >-
      Named schedules are used for storing custom data that can change over
      time. Named schedules are often used in custom pricing logic.
paths:
  /v1/ingest:
    post:
      tags:
        - Usage
      summary: Ingest events
      description: >
        The ingest endpoint is the primary method for sending usage events to
        Metronome, serving as the foundation for all billing calculations in
        your usage-based pricing model. This high-throughput endpoint is
        designed for real-time streaming ingestion, supports backdating 34 days,
        and is built to handle mission-critical usage data with enterprise-grade
        reliability. Metronome supports 100,000 events per second without
        requiring pre-aggregation or rollups and can scale up from there. See
        the [Send usage events](/guides/events/send-usage-events) guide to learn
        more about usage events.


        ### Use this endpoint to:

        Create a customer usage pipeline into Metronome that drives billable
        metrics, credit drawdown, and invoicing. Track customer behavior,
        resource consumption, and feature usage


        ### What happens when you send events:

        - Events are validated and processed in real-time

        - Events are matched to customers using customer IDs or customer ingest
        aliases

        - Events are matched to billable metrics and are immediately available
        for usage and spend calculations


        ### Usage guidelines:

        - Historical events can be backdated up to 34 days and will immediately
        impact live customer spend

        - Duplicate events are automatically detected and ignored (34-day
        deduplication window)


        #### Event structure:

        Usage events are simple JSON objects designed for flexibility and ease
        of integration:

        ```json

        {
          "transaction_id": "2021-01-01T00:00:00Z_cluster42",
          "customer_id": "team@example.com",
          "event_type": "api_request",
          "timestamp": "2021-01-01T00:00:00Z",
          "properties": {
            "endpoint": "/v1/users",
            "method": "POST",
            "response_time_ms": 45,
            "region": "us-west-2"
          }
        }

        ```


        Learn more about [usage event structure
        definitions](/guides/events/design-usage-events).


        #### Transaction ID
          The transaction_id serves as your idempotency key, ensuring events are processed exactly once. Metronome maintains a 34-day deduplication window - significantly longer than typical 12-hour windows - enabling robust backfill scenarios without duplicate billing.
          - Best Practices:
            - Use UUIDs for one-time events: uuid4()
            - For heartbeat events, use deterministic IDs
            - Include enough context to avoid collisions across different event sources

        #### Customer ID

        Identifies which customer should be billed for this usage. Supports two
        identification methods:
          - Metronome Customer ID: The UUID returned when creating a customer
          - Ingest Alias: Your system's identifier (email, account number, etc.) 

        Ingest aliases enable seamless integration without requiring ID mapping,
        and customers can have multiple aliases for flexibility.


        #### Event Type:

        Categorizes the event type for billable metric matching. Choose
        descriptive names that aligns with the product surface area.


        #### Properties:

        Flexible metadata also used to match billable metrics or to be used to
        serve as group keys to create multiple pricing dimensions or breakdown
        costs by novel properties for end customers or internal finance teams
        measuring underlying COGs.
      operationId: ingest-v1
      requestBody:
        content:
          application/json:
            schema:
              type: array
              minItems: 1
              maxItems: 100
              items:
                $ref: '#/components/schemas/Event'
            example:
              - transaction_id: 2021-01-01T00:00:00Z_cluster42
                customer_id: team@example.com
                event_type: heartbeat
                timestamp: '2021-01-01T00:00:00Z'
                properties:
                  cluster_id: '42'
                  cpu_seconds: 60
                  region: Europe
      responses:
        '200':
          description: Success
components:
  schemas:
    Event:
      required:
        - customer_id
        - event_type
        - timestamp
        - transaction_id
      type: object
      properties:
        transaction_id:
          type: string
          minLength: 1
          maxLength: 128
        customer_id:
          type: string
          minLength: 1
        event_type:
          type: string
          minLength: 1
        timestamp:
          type: string
          description: RFC 3339 formatted
        properties:
          type: object
          additionalProperties: true
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
