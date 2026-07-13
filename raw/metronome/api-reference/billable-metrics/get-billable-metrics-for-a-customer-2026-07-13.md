<!-- Source URL: https://docs.metronome.com/api-reference/billable-metrics/get-billable-metrics-for-a-customer.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get billable metrics for a customer

> Get all billable metrics available for a specific customer. Supports pagination and filtering by current plan status or archived metrics. Use this endpoint to see which metrics are being tracked for billing calculations for a given customer.




## OpenAPI

````yaml /openapi.json get /v1/customers/{customer_id}/billable-metrics
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
  /v1/customers/{customer_id}/billable-metrics:
    get:
      tags:
        - Billable metrics
      summary: Get billable metrics for a customer
      description: >
        Get all billable metrics available for a specific customer. Supports
        pagination and filtering by current plan status or archived metrics. Use
        this endpoint to see which metrics are being tracked for billing
        calculations for a given customer.
      operationId: listBillableMetrics-v1
      parameters:
        - $ref: '#/components/parameters/CustomerId'
        - $ref: '#/components/parameters/PageLimit'
        - $ref: '#/components/parameters/NextPage'
        - name: on_current_plan
          in: query
          description: >-
            If true, the list of metrics will be filtered to just ones that are
            on the customer's current plan
          required: false
          schema:
            type: boolean
        - name: include_archived
          in: query
          description: If true, the list of returned metrics will include archived metrics
          required: false
          schema:
            type: boolean
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                required:
                  - data
                  - next_page
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/BillableMetricWithDeprecatedFields'
                  next_page:
                    type: string
                    nullable: true
              example:
                data:
                  - name: data transfer (GB)
                    id: 9570e4f3-d1da-4b95-ba81-bd40ee002727
                    group_by:
                      - cluster
                      - region
                    aggregate: sum
                    aggregate_keys:
                      - bytes
                    aggregation_type: SUM
                    aggregation_key: bytes
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
                    group_keys:
                      - - region
                      - - machine_type
                  - name: CPU hours
                    id: 13117714-3f05-48e5-a6e9-a66093f13b4d
                    aggregation_type: SUM
                    aggregation_key: bytes
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
                    group_keys:
                      - - region
                      - - machine_type
                    archived_at: '2024-10-01T11:23:44Z'
                next_page: null
components:
  parameters:
    CustomerId:
      name: customer_id
      in: path
      required: true
      schema:
        type: string
        format: uuid
      example: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
    PageLimit:
      name: limit
      in: query
      description: Max number of results that should be returned
      required: false
      schema:
        type: integer
        minimum: 1
        maximum: 100
    NextPage:
      name: next_page
      in: query
      description: Cursor that indicates where the next page of results should start.
      required: false
      schema:
        type: string
  schemas:
    BillableMetricWithDeprecatedFields:
      allOf:
        - $ref: '#/components/schemas/BillableMetricBase'
        - type: object
          properties:
            aggregation_type:
              $ref: '#/components/schemas/AggregationType'
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
