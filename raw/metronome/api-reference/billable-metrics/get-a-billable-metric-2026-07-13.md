<!-- Source URL: https://docs.metronome.com/api-reference/billable-metrics/get-a-billable-metric.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a billable metric

> Retrieves the complete configuration for a specific billable metric by its ID. Use this to review billable metric setup before associating it with products. Returns the metric's `name`, `event_type_filter`, `property_filters`, `aggregation_type`, `aggregation_key`, `group_keys`, `custom fields`, and `SQL query` (if it's a SQL billable metric). 

Important: 
- Archived billable metrics will include an `archived_at` timestamp; they no longer process new usage events but remain accessible for historical reference.




## OpenAPI

````yaml /openapi.json get /v1/billable-metrics/{billable_metric_id}
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
  /v1/billable-metrics/{billable_metric_id}:
    get:
      tags:
        - Billable metrics
      summary: Get a billable metric
      description: >
        Retrieves the complete configuration for a specific billable metric by
        its ID. Use this to review billable metric setup before associating it
        with products. Returns the metric's `name`, `event_type_filter`,
        `property_filters`, `aggregation_type`, `aggregation_key`, `group_keys`,
        `custom fields`, and `SQL query` (if it's a SQL billable metric). 


        Important: 

        - Archived billable metrics will include an `archived_at` timestamp;
        they no longer process new usage events but remain accessible for
        historical reference.
      operationId: getBillableMetric-v1
      parameters:
        - $ref: '#/components/parameters/BillableMetricId'
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                required:
                  - data
                properties:
                  data:
                    $ref: '#/components/schemas/BillableMetricV1'
              example:
                data:
                  id: 8deed800-1b7a-495d-a207-6c52bac54dc9
                  name: CPU Hours
                  event_type_filter:
                    in_values:
                      - cpu_usage
                  property_filters:
                    - name: cpu_hours
                      exists: true
                    - name: region
                      exists: true
                      in_values:
                        - EU
                        - NA
                    - name: machine_type
                      exists: true
                      in_values:
                        - slow
                        - fast
                  aggregation_type: SUM
                  aggregation_key: cpu_hours
                  group_keys:
                    - - region
                    - - machine_type
        '404':
          $ref: '#/components/responses/NotFound'
components:
  parameters:
    BillableMetricId:
      name: billable_metric_id
      in: path
      required: true
      schema:
        type: string
        format: uuid
      example: 13117714-3f05-48e5-a6e9-a66093f13b4d
  schemas:
    BillableMetricV1:
      type: object
      required:
        - id
        - name
      properties:
        id:
          type: string
          format: uuid
          description: ID of the billable metric
        name:
          type: string
          description: The display name of the billable metric.
        event_type_filter:
          $ref: '#/components/schemas/EventTypeFilter'
        property_filters:
          $ref: '#/components/schemas/PropertyFiltersArray'
        aggregation_type:
          $ref: '#/components/schemas/AggregationType'
        aggregation_key:
          $ref: '#/components/schemas/AggregationKey'
        group_keys:
          $ref: '#/components/schemas/GroupKeysArray'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
        sql:
          type: string
          description: The SQL query associated with the billable metric
        archived_at:
          type: string
          format: date-time
          description: >-
            RFC 3339 timestamp indicating when the billable metric was archived.
            If not provided, the billable metric is not archived.
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
    AggregationType:
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
      description: Specifies the type of aggregation performed on matching events.
    AggregationKey:
      type: string
      description: >-
        A key that specifies which property of the event is used to aggregate
        data. This key must be one of the property filter names and is not
        applicable when the aggregation type is 'count'.
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
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
    Error:
      required:
        - message
      type: object
      properties:
        message:
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
  responses:
    NotFound:
      description: The specified resource was not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
