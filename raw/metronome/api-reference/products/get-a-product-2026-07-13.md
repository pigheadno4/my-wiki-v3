<!-- Source URL: https://docs.metronome.com/api-reference/products/get-a-product.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a product

> Retrieve a product by its ID, including all metadata and historical changes.




## OpenAPI

````yaml /openapi.json post /v1/contract-pricing/products/get
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
  /v1/contract-pricing/products/get:
    post:
      tags:
        - Products
      summary: Get a product
      description: >
        Retrieve a product by its ID, including all metadata and historical
        changes.
      operationId: getProduct-v1
      requestBody:
        description: The ID of the product to get
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Id'
            example:
              id: d84e7f4e-7a70-4fe4-be02-7a5027beffcc
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
                    $ref: '#/components/schemas/ProductListItem'
              example:
                data:
                  id: 9c9a4a71-171e-41f9-b8da-d982baf1a388
                  type: COMPOSITE
                  initial:
                    name: My Composite Product
                    starting_at: '2020-01-01T00:00:00.000Z'
                    composite_product_ids:
                      - e5e40bc7-ef69-42ec-a77e-cd696f6bfa3d
                    created_at: '2019-12-30T04:24:55.123Z'
                    created_by: Bob
                  current:
                    name: My Updated Composite Product Name
                    starting_at: '2020-01-01T00:00:00.000Z'
                    composite_product_ids:
                      - e5e40bc7-ef69-42ec-a77e-cd696f6bfa3d
                    created_at: '2019-12-30T04:24:55.123Z'
                    created_by: Bob
                  updates:
                    - name: My Updated Composite Product Name
                      starting_at: '2020-02-01T00:00:00.000Z'
                      created_at: '2019-12-30T09:24:55.123Z'
                      created_by: Alice
                  custom_fields:
                    x_account_id: KyVnHhSBWl7eY2bl
        '404':
          $ref: '#/components/responses/NotFound'
components:
  schemas:
    Id:
      required:
        - id
      type: object
      properties:
        id:
          type: string
          format: uuid
    ProductListItem:
      type: object
      required:
        - id
        - type
        - initial
        - current
        - updates
      properties:
        id:
          type: string
          format: uuid
        type:
          type: string
          enum:
            - USAGE
            - SUBSCRIPTION
            - COMPOSITE
            - FIXED
            - PRO_SERVICE
        archived_at:
          type: string
          format: date-time
          nullable: true
        initial:
          $ref: '#/components/schemas/ProductListItemState'
        current:
          $ref: '#/components/schemas/ProductListItemState'
        updates:
          type: array
          items:
            $ref: '#/components/schemas/ProductListItemUpdate'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: contract_product
    ProductListItemState:
      type: object
      required:
        - name
        - created_at
        - created_by
      properties:
        name:
          type: string
        starting_at:
          type: string
          format: date-time
        netsuite_internal_item_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          description: >-
            This field's availability is dependent on your client's
            configuration.
        created_at:
          type: string
          format: date-time
        created_by:
          type: string
        netsuite_overage_item_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          description: >-
            This field's availability is dependent on your client's
            configuration.
        billable_metric_id:
          type: string
        composite_product_ids:
          type: array
          items:
            type: string
            format: uuid
        quantity_conversion:
          $ref: '#/components/schemas/QuantityConversion'
        quantity_rounding:
          $ref: '#/components/schemas/QuantityRounding'
        composite_tags:
          type: array
          items:
            type: string
        is_refundable:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: boolean
          description: >-
            This field's availability is dependent on your client's
            configuration.
        tags:
          type: array
          items:
            type: string
        composite_scope:
          type: string
          enum:
            - CUSTOMER
            - CONTRACT
          x-mint:
            groups:
              - ff:composite-support-charge-m1-enabled
          x-stainless-skip: true
          description: Determines what spend contributes to calculating this charge.
        exclude_free_usage:
          type: boolean
        include_composite_spend:
          type: boolean
          x-mint:
            groups:
              - ff:m2-composite-on-composite
          x-stainless-skip: true
          description: >-
            Only for composite products. If true, allows a composite to
            incorporate spend from other composite products. Defaults to false
        pricing_group_key:
          $ref: '#/components/schemas/PricingGroupKey'
        presentation_group_key:
          $ref: '#/components/schemas/PresentationGroupKey'
    ProductListItemUpdate:
      type: object
      required:
        - created_at
        - created_by
      properties:
        name:
          type: string
        starting_at:
          type: string
          format: date-time
        is_refundable:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: boolean
        created_at:
          type: string
          format: date-time
        created_by:
          type: string
        billable_metric_id:
          type: string
          format: uuid
        quantity_conversion:
          $ref: '#/components/schemas/QuantityConversion'
        quantity_rounding:
          $ref: '#/components/schemas/QuantityRounding'
        netsuite_internal_item_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          description: >-
            This field's availability is dependent on your client's
            configuration.
        netsuite_overage_item_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          description: >-
            This field's availability is dependent on your client's
            configuration.
        composite_product_ids:
          type: array
          items:
            type: string
            format: uuid
        composite_tags:
          type: array
          items:
            type: string
        tags:
          type: array
          items:
            type: string
        exclude_free_usage:
          type: boolean
        include_composite_spend:
          type: boolean
          x-mint:
            groups:
              - ff:m2-composite-on-composite
          x-stainless-skip: true
          description: >-
            Only for composite products. If true, allows a composite to
            incorporate spend from other composite products. Defaults to false
        pricing_group_key:
          $ref: '#/components/schemas/PricingGroupKey'
        presentation_group_key:
          $ref: '#/components/schemas/PresentationGroupKey'
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
