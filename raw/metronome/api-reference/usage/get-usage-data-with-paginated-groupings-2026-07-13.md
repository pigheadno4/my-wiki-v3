<!-- Source URL: https://docs.metronome.com/api-reference/usage/get-usage-data-with-paginated-groupings.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get usage data with paginated groupings

> Retrieve granular usage data for a specific customer and billable metric, with the ability to break down usage by custom grouping dimensions. This endpoint enables deep usage analytics by segmenting data across attributes like region, user, model type, or any custom dimension defined in your billable metrics.

### Use this endpoint to:
- Analyze usage patterns broken down by specific attributes (region, user, department, etc.)
- Build detailed usage dashboards with dimensional filtering
- Identify high-usage segments for optimization opportunities

### Request parameters
Use [`group_key`](#body-group-key) and [`group_filters`](#body-group-filters) to group by one or more dimensions. This is required for compound group keys and recommended for all new integrations:
```json
{
  "group_key": ["region", "team"],
  "group_filters": {
    "region": ["US-East", "US-West"]
  }
}
```
Important: For compound group keys, you must pass the complete set of keys that make up the compound key. Partial key combinations are not supported. For example, if your billable metric has a compound group key [region, team, environment], you must pass all three keys in group_key—you cannot pass just `[region]` or `[region, team]`.

### Key response fields:
An array of `PagedUsageAggregate` objects containing:
- `starting_on` and `ending_before`: Time window boundaries
- `group`: Object mapping group keys to their values
  - For simple groups, this will be a map with a single key-value pair (e.g., `{"region": "US-East"}`)
  - For compound groups, this will be a map with multiple key-value pairs (e.g., `{"region": "US-East", "team": "engineering"}`)
- `value`: Aggregated usage for this group and time window
- `next_page`: Pagination cursor for large datasets

### Usage guidelines:
- Required parameters: Must specify `customer_id`, `billable_metric_id`, and `window_size`
- Time windows: Set `window_size` to hour, day, or none for different granularities
- Group filtering: Use `group_key` and `group_filters` to specify groups and group filters
- Limits: When using compound group keys (2+ keys in `group_key`), the default and max limit is 100
- Pagination: Use limit and `next_page` for large result sets
- Null handling: Group values may be null for events missing the group key property




## OpenAPI

````yaml /openapi.json post /v1/usage/groups
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
  /v1/usage/groups:
    post:
      tags:
        - Usage
      summary: Get usage data with paginated groupings
      description: >
        Retrieve granular usage data for a specific customer and billable
        metric, with the ability to break down usage by custom grouping
        dimensions. This endpoint enables deep usage analytics by segmenting
        data across attributes like region, user, model type, or any custom
        dimension defined in your billable metrics.


        ### Use this endpoint to:

        - Analyze usage patterns broken down by specific attributes (region,
        user, department, etc.)

        - Build detailed usage dashboards with dimensional filtering

        - Identify high-usage segments for optimization opportunities


        ### Request parameters

        Use [`group_key`](#body-group-key) and
        [`group_filters`](#body-group-filters) to group by one or more
        dimensions. This is required for compound group keys and recommended for
        all new integrations:

        ```json

        {
          "group_key": ["region", "team"],
          "group_filters": {
            "region": ["US-East", "US-West"]
          }
        }

        ```

        Important: For compound group keys, you must pass the complete set of
        keys that make up the compound key. Partial key combinations are not
        supported. For example, if your billable metric has a compound group key
        [region, team, environment], you must pass all three keys in
        group_key—you cannot pass just `[region]` or `[region, team]`.


        ### Key response fields:

        An array of `PagedUsageAggregate` objects containing:

        - `starting_on` and `ending_before`: Time window boundaries

        - `group`: Object mapping group keys to their values
          - For simple groups, this will be a map with a single key-value pair (e.g., `{"region": "US-East"}`)
          - For compound groups, this will be a map with multiple key-value pairs (e.g., `{"region": "US-East", "team": "engineering"}`)
        - `value`: Aggregated usage for this group and time window

        - `next_page`: Pagination cursor for large datasets


        ### Usage guidelines:

        - Required parameters: Must specify `customer_id`, `billable_metric_id`,
        and `window_size`

        - Time windows: Set `window_size` to hour, day, or none for different
        granularities

        - Group filtering: Use `group_key` and `group_filters` to specify groups
        and group filters

        - Limits: When using compound group keys (2+ keys in `group_key`), the
        default and max limit is 100

        - Pagination: Use limit and `next_page` for large result sets

        - Null handling: Group values may be null for events missing the group
        key property
      operationId: getPagedUsage-v1
      parameters:
        - $ref: '#/components/parameters/PageLimit'
        - $ref: '#/components/parameters/NextPage'
      requestBody:
        description: The usage query to run
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PagedUsageQueryPayload'
            examples:
              using_simple_group_key:
                summary: Simple (single key) group_key
                value:
                  customer_id: 04ca7e72-4229-4a6e-ab11-9f7376fccbcb
                  billable_metric_id: 222796fd-d29c-429e-89b2-549fabda4ed6
                  starting_on: '2021-01-01T00:00:00Z'
                  ending_before: '2021-01-03T00:00:00Z'
                  window_size: day
                  group_key:
                    - region
                  group_filters:
                    region:
                      - us-east1
                      - us-west1
              using_compound_group_key:
                summary: Compound (multi-key) group_key with group_filters
                value:
                  customer_id: 04ca7e72-4229-4a6e-ab11-9f7376fccbcb
                  billable_metric_id: 222796fd-d29c-429e-89b2-549fabda4ed6
                  starting_on: '2021-01-01T00:00:00Z'
                  ending_before: '2021-01-03T00:00:00Z'
                  window_size: day
                  group_key:
                    - region
                    - team
                  group_filters:
                    region:
                      - us-east1
                      - us-west1
                    team:
                      - ui
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
                      $ref: '#/components/schemas/PagedUsageAggregate'
                  next_page:
                    type: string
                    nullable: true
              examples:
                using_simple_group_key:
                  summary: Response using single-key group_key
                  value:
                    data:
                      - starting_on: '2021-01-01T00:00:00Z'
                        ending_before: '2021-01-02T00:00:00Z'
                        group_key: region
                        group_value: us-east1
                        group:
                          region: us-east1
                        value: 1234
                      - starting_on: '2021-01-01T00:00:00Z'
                        ending_before: '2021-01-02T00:00:00Z'
                        group_key: region
                        group_value: us-west1
                        group:
                          region: us-west1
                        value: 567
                    next_page: null
                using_compound_group_key:
                  summary: Response using compound group_key and group_filters
                  value:
                    data:
                      - starting_on: '2021-01-01T00:00:00Z'
                        ending_before: '2021-01-02T00:00:00Z'
                        group_key: null
                        group_value: null
                        group:
                          region: us-east1
                          team: ui
                        value: 1234
                      - starting_on: '2021-01-01T00:00:00Z'
                        ending_before: '2021-01-02T00:00:00Z'
                        group_key: null
                        group_value: null
                        group:
                          region: us-west1
                          team: ui
                        value: 890
                    next_page: null
components:
  parameters:
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
    PagedUsageQueryPayload:
      required:
        - billable_metric_id
        - customer_id
        - window_size
      type: object
      properties:
        customer_id:
          type: string
          format: uuid
        billable_metric_id:
          type: string
          format: uuid
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
        group_by:
          type: object
          description: >-
            Use group_key and group_filters instead. Use a single group key to
            group by. Compound group keys are not supported.
          deprecated: true
          required:
            - key
          properties:
            key:
              type: string
              description: The name of the group_by key to use
            values:
              type: array
              description: >-
                Values of the group_by key to return in the query. Omit this if
                you'd like all values for the key returned.
              minItems: 1
              items:
                type: string
                minLength: 1
        group_key:
          $ref: '#/components/schemas/GroupKey'
        group_filters:
          $ref: '#/components/schemas/GroupFilter'
        current_period:
          type: boolean
          description: >-
            If true, will return the usage for the current billing period. Will
            return an error if the customer is currently uncontracted or
            starting_on and ending_before are specified when this is true.
    PagedUsageAggregate:
      required:
        - starting_on
        - ending_before
        - group_key
        - group_value
        - value
      type: object
      properties:
        starting_on:
          type: string
          format: date-time
        ending_before:
          type: string
          format: date-time
        group_key:
          type: string
          nullable: true
          description: Use `group` instead. The group key for single-key grouping.
          deprecated: true
        group_value:
          type: string
          nullable: true
          description: Use `group` instead. The group value for single-key grouping.
          deprecated: true
        group:
          type: object
          additionalProperties:
            type: string
          description: >
            Map of group key to their value for this usage aggregate.

            For simple group keys, this should be a single key e.g. `{"region":
            "US-East"}`

            For compound group keys, this should contain the values of each
            group key that forms the compound e.g. `{"region": "US-East",
            "team": "engineering"}`
        value:
          type: number
          nullable: true
    GroupKey:
      type: array
      description: >
        Group key to group usage by. Supports both simple (single key) and
        compound (multiple keys) group keys.


        For simple group keys, provide a single key e.g. `["region"]`.

        For compound group keys, provide multiple keys e.g. `["region",
        "team"]`.


        For streaming metrics, the keys must be defined as a simple or compound
        group key on the billable metric.

        For compound group keys, all keys must match an exact compound group key
        definition — partial matches are not allowed.


        Cannot be used together with `group_by`.
      items:
        type: string
        minLength: 1
      minItems: 1
      example:
        - region
        - team
    GroupFilter:
      type: object
      description: >
        Object mapping group keys to arrays of values to filter on. Only usage
        matching these filter values will be returned.

        Keys must be present in group_key. Omit a key or use an empty array to
        include all values for that dimension.
      additionalProperties:
        type: array
        items:
          type: string
          minLength: 1
      example:
        region:
          - us-east1
          - us-west1
        team:
          - UI
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
