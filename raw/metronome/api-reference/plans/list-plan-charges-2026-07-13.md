<!-- Source URL: https://docs.metronome.com/api-reference/plans/list-plan-charges.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List plan charges

> Fetches a list of charges of a specific plan. This is a Plans (deprecated) endpoint. New clients should implement using Contracts.




## OpenAPI

````yaml /openapi.plans.json get /planDetails/{plan_id}/charges
openapi: 3.0.1
info:
  title: Metronome
  version: 1.0.0
servers:
  - url: https://api.metronome.com/v1
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
  - name: Plans
    description: >-
      [Plans](https://docs.metronome.com/pricing-and-packaging/create-plans/)
      determine the base pricing for a customer. Use these endpoints to add a
      plan to a customer, end a customer plan, retrieve plans, and retrieve plan
      details. Create plans in the [Metronome
      app](https://app.metronome.com/plans).
  - name: Contracts
    description: >-
      A contract defines a customer’s products, pricing, discounts, commitments,
      and more. Use these endpoints to create and update contracts data.
  - name: Credit grants
    description: >-
      [Credit
      grants](https://docs.metronome.com/invoicing/how-billing-works/manage-credits/)
      adjust a customer balance for prepayments, reimbursements, promotions, and
      so on. Use these endpoints to create, retrieve, update, and delete credit
      grants.
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
paths:
  /planDetails/{plan_id}/charges:
    get:
      tags:
        - Plans
      summary: List plan charges
      description: >
        Fetches a list of charges of a specific plan. This is a Plans
        (deprecated) endpoint. New clients should implement using Contracts.
      operationId: getPlanCharges
      parameters:
        - $ref: '#/components/parameters/PlanId'
        - $ref: '#/components/parameters/PageLimit'
        - $ref: '#/components/parameters/NextPage'
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
                      $ref: '#/components/schemas/PlanCharge'
                  next_page:
                    type: string
                    nullable: true
              example:
                data:
                  - id: a23b3cf4-47fb-4c3f-bb3d-9e64f7704015
                    name: Server Hours
                    product_id: d7998a03-db47-4d3f-97e4-d26f3f418718
                    product_name: Dedicated Server
                    start_period: 0
                    tier_reset_frequency: 1
                    credit_type:
                      id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                      name: USD (cents)
                    charge_type: usage
                    prices:
                      - value: 50
                        tier: 0
                    custom_fields:
                      x_account_id: KyVnHhSBWl7eY2bl
                next_page: 31646362333134302d363735362d346661372d396436362d383
components:
  parameters:
    PlanId:
      name: plan_id
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
    PlanCharge:
      required:
        - id
        - name
        - product_id
        - product_name
        - prices
        - charge_type
        - credit_type
        - custom_fields
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        charge_type:
          $ref: '#/components/schemas/ChargeType'
        product_id:
          type: string
        product_name:
          type: string
        quantity:
          type: number
        start_period:
          type: number
          description: >-
            Used in price ramps.  Indicates how many billing periods pass before
            the charge applies.
        tier_reset_frequency:
          type: number
          description: >-
            Used in pricing tiers.  Indicates how often the tier resets. Default
            is 1 - the tier count resets every billing period.
        credit_type:
          $ref: '#/components/schemas/CreditType'
        unit_conversion:
          required:
            - division_factor
          type: object
          description: Specifies how quantities for usage based charges will be converted.
          properties:
            division_factor:
              type: number
              description: The conversion factor
            rounding_behavior:
              type: string
              enum:
                - floor
                - ceiling
              description: >-
                Whether usage should be rounded down or up to the nearest whole
                number. If null, quantity will be rounded to 20 decimal places.
        prices:
          type: array
          items:
            required:
              - value
              - tier
            type: object
            properties:
              value:
                type: number
              tier:
                type: number
                description: >-
                  Used in pricing tiers.  Indicates at what metric value the
                  price applies.
              quantity:
                type: number
              collection_schedule:
                type: string
              collection_interval:
                type: number
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: charge
    ChargeType:
      type: string
      enum:
        - usage
        - fixed
        - composite
        - minimum
        - seat
    CreditType:
      required:
        - name
        - id
      type: object
      properties:
        name:
          type: string
        id:
          type: string
          format: uuid
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
