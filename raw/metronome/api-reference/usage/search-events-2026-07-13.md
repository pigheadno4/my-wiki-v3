<!-- Source URL: https://docs.metronome.com/api-reference/usage/search-events.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Search events

> This endpoint retrieves events by transaction ID for events that occurred within the last 34 days. It is specifically designed for sampling-based testing workflows to detect revenue leakage. The Event Search API provides a critical observability tool that validates the integrity of your usage pipeline by allowing you to sample raw events and verify their matching against active billable metrics. 

Why event observability matters for revenue leakage:
Silent revenue loss occurs when events are dropped, delayed, or fail to match billable metrics due to:
- Upstream system failures
- Event format changes
- Misconfigured billable metrics

### Use this endpoint to:
- Sample raw events and validate they match the expected billable metrics
- Build custom leakage detection alerts to prevent silent revenue loss
- Verify event processing accuracy during system changes or metric updates
- Debug event matching issues in real-time

### Key response fields:
- Complete event details including transaction ID, customer ID, and properties
- Matched Metronome customer (if any)
- Matched billable metric information (if any)
- Processing status and duplicate detection flags

### Usage guidelines:
⚠️ Important: This endpoint is heavily rate limited and designed for sampling workflows only. Do not use this endpoint to check every event in your system. Instead, implement a sampling strategy to randomly validate a subset of events for observability purposes.




## OpenAPI

````yaml /openapi.json post /v1/events/search
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
  /v1/events/search:
    post:
      tags:
        - Usage
      summary: Search events
      description: >
        This endpoint retrieves events by transaction ID for events that
        occurred within the last 34 days. It is specifically designed for
        sampling-based testing workflows to detect revenue leakage. The Event
        Search API provides a critical observability tool that validates the
        integrity of your usage pipeline by allowing you to sample raw events
        and verify their matching against active billable metrics. 


        Why event observability matters for revenue leakage:

        Silent revenue loss occurs when events are dropped, delayed, or fail to
        match billable metrics due to:

        - Upstream system failures

        - Event format changes

        - Misconfigured billable metrics


        ### Use this endpoint to:

        - Sample raw events and validate they match the expected billable
        metrics

        - Build custom leakage detection alerts to prevent silent revenue loss

        - Verify event processing accuracy during system changes or metric
        updates

        - Debug event matching issues in real-time


        ### Key response fields:

        - Complete event details including transaction ID, customer ID, and
        properties

        - Matched Metronome customer (if any)

        - Matched billable metric information (if any)

        - Processing status and duplicate detection flags


        ### Usage guidelines:

        ⚠️ Important: This endpoint is heavily rate limited and designed for
        sampling workflows only. Do not use this endpoint to check every event
        in your system. Instead, implement a sampling strategy to randomly
        validate a subset of events for observability purposes.
      operationId: searchEvents-v1
      requestBody:
        description: Search events request
        content:
          application/json:
            schema:
              type: object
              required:
                - transactionIds
              properties:
                transactionIds:
                  type: array
                  items:
                    type: string
                  description: The transaction IDs of the events to retrieve
            example:
              transactionIds:
                - 2021-01-01T00:00:00Z_cluster42
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  required:
                    - id
                    - transaction_id
                    - customer_id
                    - event_type
                    - timestamp
                  properties:
                    id:
                      type: string
                    customer_id:
                      type: string
                      description: The ID of the customer in the ingest event body
                    event_type:
                      type: string
                    properties:
                      type: object
                      additionalProperties: true
                    timestamp:
                      type: string
                      format: date-time
                    transaction_id:
                      type: string
                    is_duplicate:
                      type: boolean
                    processed_at:
                      type: string
                      format: date-time
                    matched_customer:
                      type: object
                      description: >-
                        The customer the event was matched to if a match was
                        found
                      properties:
                        id:
                          type: string
                          format: uuid
                        name:
                          type: string
                    matched_billable_metrics:
                      type: array
                      items:
                        $ref: '#/components/schemas/BillableMetricForEventsSearch'
              example:
                - id: 123e4567-e89b-12d3-a456-426614174000
                  transaction_id: 2021-01-01T00:00:00Z_cluster42
                  customer_id: team@example.com
                  event_type: heartbeat
                  timestamp: '2021-01-01T00:00:00Z'
                  properties:
                    cluster_id: '42'
                    cpu_seconds: 60
                    region: Europe
                  processed_at: '2021-01-01T00:00:05Z'
                  is_duplicate: false
                  matched_customer:
                    id: 98765432-10fe-cba9-8765-432109876543
                    name: Acme Corp
                  matched_billable_metrics:
                    - id: 8deed800-1b7a-495d-a207-6c52bac54dc9
                      name: CPU Hours
components:
  schemas:
    BillableMetricForEventsSearch:
      allOf:
        - $ref: '#/components/schemas/BillableMetricBase'
        - type: object
          properties:
            aggregation_type:
              $ref: '#/components/schemas/AggregationTypeForEventsSearch'
    BillableMetricBase:
      required:
        - name
        - id
      type: object
      properties:
        group_by:
          type: array
          description: (DEPRECATED) use group_keys instead
          items:
            type: string
            description: >-
              A list of keys that can be used to additionally segment the values
              of the billable metric when making usage queries
        group_keys:
          $ref: '#/components/schemas/GroupKeysArray'
        name:
          type: string
        id:
          type: string
          format: uuid
        aggregate:
          type: string
          description: (DEPRECATED) use aggregation_type instead
        aggregate_keys:
          type: array
          description: (DEPRECATED) use aggregation_key instead
          items:
            type: string
        filter:
          type: object
          description: (DEPRECATED) use property_filters & event_type_filter instead
          additionalProperties: true
        aggregation_key:
          $ref: '#/components/schemas/AggregationKey'
        event_type_filter:
          $ref: '#/components/schemas/EventTypeFilter'
        property_filters:
          $ref: '#/components/schemas/PropertyFiltersArray'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: billable_metric
        sql:
          type: string
          description: The SQL query associated with the billable metric
        archived_at:
          type: string
          format: date-time
          description: >-
            RFC 3339 timestamp indicating when the billable metric was archived.
            If not provided, the billable metric is not archived.
    AggregationTypeForEventsSearch:
      type: string
      enum:
        - count
        - Count
        - COUNT
        - latest
        - Latest
        - LATEST
        - max
        - Max
        - MAX
        - sum
        - Sum
        - SUM
        - unique
        - Unique
        - UNIQUE
        - custom_sql
      description: >-
        Specifies the type of aggregation performed on matching events. Includes
        "custom_sql" for events search endpoint responses.
    GroupKeysArray:
      type: array
      items:
        type: array
        items:
          type: string
      description: >-
        Property names that are used to group usage costs on an invoice. Each
        entry represents a set of properties used to slice events into distinct
        buckets.
    AggregationKey:
      type: string
      description: >-
        A key that specifies which property of the event is used to aggregate
        data. This key must be one of the property filter names and is not
        applicable when the aggregation type is 'count'.
    EventTypeFilter:
      type: object
      properties:
        in_values:
          type: array
          items:
            type: string
          description: >-
            A list of event types that are explicitly included in the billable
            metric. If specified, only events of these types will match the
            billable metric. Must be non-empty if present.
        not_in_values:
          type: array
          items:
            type: string
          description: >-
            A list of event types that are explicitly excluded from the billable
            metric. If specified, events of these types will not match the
            billable metric. Must be non-empty if present.
      description: >-
        An optional filtering rule to match the 'event_type' property of an
        event.
    PropertyFiltersArray:
      type: array
      items:
        $ref: '#/components/schemas/PropertyFilter'
      description: >-
        A list of filters to match events to this billable metric. Each filter
        defines a rule on an event property. All rules must pass for the event
        to match the billable metric.
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
    PropertyFilter:
      type: object
      required:
        - name
      properties:
        name:
          type: string
          description: The name of the event property.
        exists:
          type: boolean
          description: >-
            Determines whether the property must exist in the event. If true,
            only events with this property will pass the filter. If false, only
            events without this property will pass the filter. If null or
            omitted, the existence of the property is optional.
        in_values:
          type: array
          items:
            type: string
          description: >-
            Specifies the allowed values for the property to match an event. An
            event will pass the filter only if its property value is included in
            this list. If undefined, all property values will pass the filter.
            Must be non-empty if present.
        not_in_values:
          type: array
          items:
            type: string
          description: >-
            Specifies the values that prevent an event from matching the filter.
            An event will not pass the filter if its property value is included
            in this list. If null or empty, all property values will pass the
            filter. Must be non-empty if present.
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
