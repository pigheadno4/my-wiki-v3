<!-- Source URL: https://docs.metronome.com/api-reference/products/update-a-product.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a product

> Updates a product's configuration while maintaining billing continuity for active customers. Use this endpoint to modify product names, metrics, pricing rules, and composite settings without disrupting ongoing billing cycles. Changes are scheduled using the starting_at timestamp, which must be on an hour boundary—set future dates to schedule updates ahead of time, or past dates for retroactive changes. Returns the updated product ID upon success. 

### Usage guidance: 
- Product type cannot be changed after creation. For incorrect product types, create a new product and archive the original instead.




## OpenAPI

````yaml /openapi.json post /v1/contract-pricing/products/update
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
  /v1/contract-pricing/products/update:
    post:
      tags:
        - Products
      summary: Update a product
      description: >
        Updates a product's configuration while maintaining billing continuity
        for active customers. Use this endpoint to modify product names,
        metrics, pricing rules, and composite settings without disrupting
        ongoing billing cycles. Changes are scheduled using the starting_at
        timestamp, which must be on an hour boundary—set future dates to
        schedule updates ahead of time, or past dates for retroactive changes.
        Returns the updated product ID upon success. 


        ### Usage guidance: 

        - Product type cannot be changed after creation. For incorrect product
        types, create a new product and archive the original instead.
      operationId: updateProduct-v1
      requestBody:
        description: >
          Updates a product's configuration while maintaining billing continuity
          for active customers. Use this endpoint to modify product names,
          metrics, pricing rules, and composite settings without disrupting
          ongoing billing cycles. Changes are scheduled using the starting_at
          timestamp, which must be on an hour boundary–set future dates to
          schedule updates ahead of time, or past dates for retroactive changes.
          Returns the updated product ID upon success. 


          Usage guidance: 

          Product type cannot be changed after creation. For incorrect product
          types, create a new product and archive the original instead.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateProductListItemPayload'
            example:
              product_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
              name: My Updated Product
              starting_at: '2020-01-01T00:00:00.000Z'
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
                    $ref: '#/components/schemas/Id'
              example:
                data:
                  id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '404':
          $ref: '#/components/responses/NotFound'
components:
  schemas:
    UpdateProductListItemPayload:
      type: object
      required:
        - product_id
        - starting_at
      properties:
        product_id:
          type: string
          format: uuid
          description: ID of the product to update
        name:
          type: string
          description: >-
            displayed on invoices. If not provided, defaults to product's
            current name.
        starting_at:
          type: string
          format: date-time
          description: >-
            Timestamp representing when the update should go into effect. It
            must be on an hour boundary (e.g. 1:00, not 1:30).
        is_refundable:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: boolean
          description: >-
            Defaults to product's current refundability status. This field's
            availability is dependent on your client's configuration.
        exclude_free_usage:
          type: boolean
          description: >-
            Beta feature only available for composite products. If true,
            products with $0 will not be included when computing composite
            usage. Defaults to false
        include_composite_spend:
          type: boolean
          x-mint:
            groups:
              - ff:m2-composite-on-composite
          x-stainless-skip: true
          description: >-
            Only for composite products. If true, allows a composite to
            incorporate spend from other composite products. Defaults to false
        billable_metric_id:
          type: string
          format: uuid
          description: >-
            Available for USAGE products only. If not provided, defaults to
            product's current billable metric.
        sql_breakdown_granularity:
          type: string
          enum:
            - HOUR
            - hour
            - SERVICE_PERIOD
            - service_period
          description: >-
            Defines the breakdown behavior when calculating usage from SQL
            Billable Metrics. If set to 'service_period' (default), the usage
            will be evaluated once for all events the invoice service period and
            the usage will be applied at the last instant of the invoice. If set
            to 'hour', it will be broken down and evaluated for each hour. For
            most use cases, 'hour' is recommended. The setting has no effect for
            Streaming Billable Metrics.
        netsuite_internal_item_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          description: >-
            If not provided, defaults to product's current
            netsuite_internal_item_id. This field's availability is dependent on
            your client's configuration.
        netsuite_overage_item_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          description: >-
            Available for USAGE and COMPOSITE products only. If not provided,
            defaults to product's current netsuite_overage_item_id. This field's
            availability is dependent on your client's configuration.
        composite_product_ids:
          type: array
          items:
            type: string
            format: uuid
          description: >-
            Available for COMPOSITE products only. If not provided, defaults to
            product's current composite_product_ids.
        quantity_conversion:
          $ref: '#/components/schemas/QuantityConversion'
        quantity_rounding:
          $ref: '#/components/schemas/QuantityRounding'
        tags:
          type: array
          items:
            type: string
          description: If not provided, defaults to product's current tags
        composite_tags:
          type: array
          items:
            type: string
          description: >-
            Available for COMPOSITE products only. If not provided, defaults to
            product's current composite_tags.
        pricing_group_key:
          $ref: '#/components/schemas/PricingGroupKey'
        presentation_group_key:
          $ref: '#/components/schemas/PresentationGroupKey'
    Id:
      required:
        - id
      type: object
      properties:
        id:
          type: string
          format: uuid
    Error:
      required:
        - message
      type: object
      properties:
        message:
          type: string
    QuantityConversion:
      type: object
      nullable: true
      description: >-
        Optional. Only valid for USAGE products. If provided, the quantity will
        be converted using the provided conversion factor and operation. For
        example, if the operation is "multiply" and the conversion factor is
        100, then the quantity will be multiplied by 100. This can be used in
        cases where data is sent in one unit and priced in another.  For
        example, data could be sent in MB and priced in GB. In this case, the
        conversion factor would be 1024 and the operation would be "divide".
      required:
        - conversion_factor
        - operation
      properties:
        name:
          type: string
          description: Optional name for this conversion.
        conversion_factor:
          type: number
          description: The factor to multiply or divide the quantity by.
        operation:
          type: string
          enum:
            - multiply
            - divide
            - MULTIPLY
            - DIVIDE
          description: The operation to perform on the quantity
    QuantityRounding:
      type: object
      nullable: true
      description: >-
        Optional. Only valid for USAGE products. If provided, the quantity will
        be rounded using the provided rounding method and decimal places. For
        example, if the method is "round up" and the decimal places is 0, then
        the quantity will be rounded up to the nearest integer.
      required:
        - rounding_method
        - decimal_places
      properties:
        rounding_method:
          type: string
          enum:
            - round_up
            - round_down
            - round_half_up
            - ROUND_UP
            - ROUND_DOWN
            - ROUND_HALF_UP
        decimal_places:
          type: number
          minimum: 0
    PricingGroupKey:
      type: array
      items:
        type: string
      description: >-
        For USAGE products only. If set, pricing for this product will be
        determined for each pricing_group_key value, as opposed to the product
        as a whole. The superset of values in the pricing group key and
        presentation group key must be set as one compound group key on the
        billable metric.
    PresentationGroupKey:
      type: array
      items:
        type: string
      description: >-
        For USAGE products only. Groups usage line items on invoices. The
        superset of values in the pricing group key and presentation group key
        must be set as one compound group key on the billable metric.
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
