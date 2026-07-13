<!-- Source URL: https://docs.metronome.com/api-reference/plans/get-the-plan-adjustments-for-a-customer.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get the plan adjustments for a customer

> Lists a customer plans adjustments. See the [price adjustments documentation](https://plans-docs.metronome.com/pricing/managing-plans/#price-adjustments) for details. This is a Plans (deprecated) endpoint. New clients should implement using Contracts.




## OpenAPI

````yaml /openapi.plans.json get /customers/{customer_id}/plans/{customer_plan_id}/priceAdjustments
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
  /customers/{customer_id}/plans/{customer_plan_id}/priceAdjustments:
    get:
      tags:
        - Plans
      summary: Get the plan adjustments for a customer
      description: >
        Lists a customer plans adjustments. See the [price adjustments
        documentation](https://plans-docs.metronome.com/pricing/managing-plans/#price-adjustments)
        for details. This is a Plans (deprecated) endpoint. New clients should
        implement using Contracts.
      operationId: getPlanPriceAdjustments
      parameters:
        - $ref: '#/components/parameters/CustomerId'
        - $ref: '#/components/parameters/CustomerPlanId'
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
                      $ref: '#/components/schemas/PriceAdjustment'
                  next_page:
                    type: string
                    nullable: true
              example:
                data:
                  - charge_id: 8b24d3dc-6db5-432d-9416-8439b3fbf242
                    charge_type: usage
                    start_period: 0
                    prices:
                      - adjustment_type: fixed
                        value: -0.05
                      - adjustment_type: quantity
                        value: 2
                      - adjustment_type: override
                        tier: 2
                        value: 4
                  - charge_id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                    charge_type: fixed
                    start_period: 1
                    prices:
                      - adjustment_type: percentage
                        value: -5
                next_page: 31646362333134302d363735362d346661372d396436362d383
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
    CustomerPlanId:
      name: customer_plan_id
      in: path
      description: the ID of a customer-plan relationship
      required: true
      schema:
        type: string
        format: uuid
      example: 7aa11640-0703-4600-8eb9-293f535a6b74
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
    PriceAdjustment:
      type: object
      required:
        - charge_id
        - charge_type
        - start_period
        - prices
      properties:
        charge_id:
          type: string
          format: uuid
        charge_type:
          $ref: '#/components/schemas/ChargeType'
        start_period:
          type: number
        quantity:
          type: number
        prices:
          type: array
          items:
            required:
              - adjustment_type
            type: object
            properties:
              adjustment_type:
                type: string
                enum:
                  - fixed
                  - quantity
                  - percentage
                  - override
                description: Determines how the value will be applied.
              value:
                type: number
              quantity:
                type: number
              tier:
                type: number
                description: >-
                  Used in pricing tiers.  Indicates at what metric value the
                  price applies.
    ChargeType:
      type: string
      enum:
        - usage
        - fixed
        - composite
        - minimum
        - seat
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
