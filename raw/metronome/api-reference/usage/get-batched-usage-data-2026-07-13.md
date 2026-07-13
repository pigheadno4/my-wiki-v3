<!-- Source URL: https://docs.metronome.com/api-reference/usage/get-batched-usage-data.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get batched usage data

> Retrieve aggregated usage data across multiple customers and billable metrics in a single query. This batch endpoint enables you to fetch usage patterns at scale, broken down by time windows, making it ideal for building analytics dashboards, generating reports, and monitoring platform-wide usage trends.

### Use this endpoint to:
- Generate platform-wide usage reports for internal teams
- Monitor aggregate usage trends across your entire customer base
- Create comparative usage analyses between customers or time periods
- Support capacity planning with historical usage patterns

### Key response fields:
An array of `UsageBatchAggregate` objects containing:

- `customer_id`: The customer this usage belongs to
- `billable_metric_id` and `billable_metric_name`: What was measured
- `start_timestamp` and `end_timestamp`: Time window for this data point
- `value`: Aggregated usage amount for the period
- `groups` (optional): Usage broken down by group keys with values
- `next_page`: Pagination cursor for large result sets

### Usage guidelines:
- Time windows: Set `window_size` to `hour`, `day`, or `none` (entire period)
- Required parameters: Must specify `starting_on`, `ending_before`, and `window_size`
- Filtering options:
  - `customer_ids`: Limit to specific customers (omit for all customers)
  - `billable_metrics`: Limit to specific metrics (omit for all metrics)
- Pagination: Use `next_page` cursor to retrieve large datasets
- Null values: Group values may be null when no usage matches that group




## OpenAPI

````yaml /openapi.json post /v1/usage
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
  /v1/usage:
    post:
      tags:
        - Usage
      summary: Get batched usage data
      description: >
        Retrieve aggregated usage data across multiple customers and billable
        metrics in a single query. This batch endpoint enables you to fetch
        usage patterns at scale, broken down by time windows, making it ideal
        for building analytics dashboards, generating reports, and monitoring
        platform-wide usage trends.


        ### Use this endpoint to:

        - Generate platform-wide usage reports for internal teams

        - Monitor aggregate usage trends across your entire customer base

        - Create comparative usage analyses between customers or time periods

        - Support capacity planning with historical usage patterns


        ### Key response fields:

        An array of `UsageBatchAggregate` objects containing:


        - `customer_id`: The customer this usage belongs to

        - `billable_metric_id` and `billable_metric_name`: What was measured

        - `start_timestamp` and `end_timestamp`: Time window for this data point

        - `value`: Aggregated usage amount for the period

        - `groups` (optional): Usage broken down by group keys with values

        - `next_page`: Pagination cursor for large result sets


        ### Usage guidelines:

        - Time windows: Set `window_size` to `hour`, `day`, or `none` (entire
        period)

        - Required parameters: Must specify `starting_on`, `ending_before`, and
        `window_size`

        - Filtering options:
          - `customer_ids`: Limit to specific customers (omit for all customers)
          - `billable_metrics`: Limit to specific metrics (omit for all metrics)
        - Pagination: Use `next_page` cursor to retrieve large datasets

        - Null values: Group values may be null when no usage matches that group
      operationId: getUsageBatch-v1
      parameters:
        - $ref: '#/components/parameters/NextPage'
      requestBody:
        description: The usage query to run
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UsageBatchQueryPayload'
            example:
              window_size: day
              starting_on: '2021-01-01T00:00:00Z'
              ending_before: '2021-01-03T00:00:00Z'
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
                      $ref: '#/components/schemas/UsageBatchAggregate'
                  next_page:
                    type: string
                    nullable: true
              example:
                data:
                  - customer_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                    billable_metric_id: 9570e4f3-d1da-4b95-ba81-bd40ee002727
                    billable_metric_name: CPU hours
                    start_timestamp: '2021-01-01T00:00:00Z'
                    end_timestamp: '2021-01-02T00:00:00Z'
                    value: 1234
                  - customer_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                    billable_metric_id: 9570e4f3-d1da-4b95-ba81-bd40ee002727
                    billable_metric_name: CPU hours
                    start_timestamp: '2021-01-02T00:00:00Z'
                    end_timestamp: '2021-01-03T00:00:00Z'
                    value: 1234
                next_page: null
components:
  parameters:
    NextPage:
      name: next_page
      in: query
      description: Cursor that indicates where the next page of results should start.
      required: false
      schema:
        type: string
  schemas:
    UsageBatchQueryPayload:
      required:
        - window_size
        - starting_on
        - ending_before
      type: object
      properties:
        customer_ids:
          type: array
          description: >-
            A list of Metronome customer IDs to fetch usage for. If absent,
            usage for all customers will be returned.
          items:
            type: string
            format: uuid
        billable_metrics:
          type: array
          description: >-
            A list of billable metrics to fetch usage for. If absent, all
            billable metrics will be returned.
          items:
            type: object
            required:
              - id
            properties:
              id:
                type: string
                format: uuid
              group_by:
                type: object
                required:
                  - key
                properties:
                  key:
                    type: string
                    description: The name of the group_by key to use
                  values:
                    type: array
                    description: >-
                      Values of the group_by key to return in the query. If this
                      field is omitted, all available values will be returned,
                      up to a maximum of 200.
                    minItems: 1
                    maxItems: 200
                    items:
                      type: string
                      minLength: 1
        window_size:
          type: string
          description: >-
            A window_size of "day" or "hour" will return the usage for the
            specified period segmented into daily or hourly aggregates. A
            window_size of "none" will return a single usage aggregate for the
            entirety of the specified period.
          enum:
            - hour
            - day
            - none
            - HOUR
            - DAY
            - NONE
            - Hour
            - Day
            - None
        starting_on:
          type: string
          format: date-time
        ending_before:
          type: string
          format: date-time
    UsageBatchAggregate:
      required:
        - customer_id
        - billable_metric_id
        - billable_metric_name
        - start_timestamp
        - end_timestamp
        - value
      type: object
      properties:
        customer_id:
          type: string
          format: uuid
        billable_metric_id:
          type: string
          format: uuid
        billable_metric_name:
          type: string
        start_timestamp:
          type: string
          format: date-time
        end_timestamp:
          type: string
          format: date-time
        value:
          type: number
          nullable: true
        groups:
          type: object
          additionalProperties:
            type: number
            nullable: true
          description: >-
            Values will be either a number or null. Null indicates that there
            were no matches for the group_by value.
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
