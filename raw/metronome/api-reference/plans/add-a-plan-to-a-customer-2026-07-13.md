<!-- Source URL: https://docs.metronome.com/api-reference/plans/add-a-plan-to-a-customer.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a plan to a customer

> Associate an existing customer with a plan for a specified date range.  See the [price adjustments documentation](https://plans-docs.metronome.com/pricing/managing-plans/#price-adjustments) for details on the price adjustments. This is a Plans (deprecated) endpoint. New clients should implement using Contracts.




## OpenAPI

````yaml /openapi.plans.json post /customers/{customer_id}/plans/add
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
  /customers/{customer_id}/plans/add:
    post:
      tags:
        - Plans
      summary: Add a plan to a customer
      description: >
        Associate an existing customer with a plan for a specified date range. 
        See the [price adjustments
        documentation](https://plans-docs.metronome.com/pricing/managing-plans/#price-adjustments)
        for details on the price adjustments. This is a Plans (deprecated)
        endpoint. New clients should implement using Contracts.
      operationId: addPlanToCustomer
      parameters:
        - $ref: '#/components/parameters/CustomerId'
      requestBody:
        description: The customer ID, plan ID, and date range for the plan to be applied
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AddPlanToCustomerPayload'
            example:
              plan_id: d2c06dae-9549-4d7d-bc04-b78dd3d241b8
              starting_on: '2021-02-01T00:00:00Z'
              ending_before: '2022-02-01T00:00:00Z'
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
                  id: 8b24d3dc-6db5-432d-9416-8439b3fbf242
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
  schemas:
    AddPlanToCustomerPayload:
      required:
        - plan_id
        - starting_on
      type: object
      properties:
        plan_id:
          type: string
          format: uuid
        starting_on:
          description: >-
            RFC 3339 timestamp for when the plan becomes active for this
            customer. Must be at 0:00 UTC (midnight).
          type: string
          format: date-time
        ending_before:
          description: >-
            RFC 3339 timestamp for when the plan ends (exclusive) for this
            customer. Must be at 0:00 UTC (midnight).
          type: string
          format: date-time
        net_payment_terms_days:
          description: >-
            Number of days after issuance of invoice after which the invoice is
            due (e.g. Net 30).
          type: number
        price_adjustments:
          type: array
          description: >-
            A list of price adjustments can be applied on top of the pricing in
            the plans. See the [price adjustments
            documentation](https://plans-docs.metronome.com/pricing/managing-plans/#price-adjustments)
            for details.
          items:
            type: object
            required:
              - charge_id
              - adjustment_type
              - start_period
            properties:
              charge_id:
                type: string
                format: uuid
              adjustment_type:
                type: string
                enum:
                  - percentage
                  - fixed
                  - override
                  - quantity
              value:
                type: number
                description: >-
                  The amount of change to a price. Percentage and fixed
                  adjustments can be positive or negative. Percentage-based
                  adjustments should be decimals, e.g. -0.05 for a 5% discount.
              quantity:
                type: number
                description: the overridden quantity for a fixed charge
              tier:
                type: number
                description: >-
                  Used in pricing tiers.  Indicates at what metric value the
                  price applies.
              start_period:
                type: number
                description: >-
                  Used in price ramps.  Indicates how many billing periods pass
                  before the charge applies.
        trial_spec:
          required:
            - length_in_days
          type: object
          description: >-
            A custom trial can be set for the customer's plan. See the [trial
            configuration
            documentation](https://docs.metronome.com/provisioning/configure-trials/)
            for details.
          properties:
            length_in_days:
              type: number
              description: Length of the trial period in days.
            spending_cap:
              type: object
              required:
                - credit_type_id
                - amount
              properties:
                credit_type_id:
                  type: string
                  description: The credit type ID for the spending cap.
                amount:
                  type: number
                  description: >-
                    The credit amount in the given denomination based on the
                    credit type, e.g. US cents.
        overage_rate_adjustments:
          type: array
          description: >-
            An optional list of overage rates that override the rates of the
            original plan configuration. These new rates will apply to all
            pricing ramps.
          items:
            type: object
            required:
              - custom_credit_type_id
              - fiat_currency_credit_type_id
              - to_fiat_conversion_factor
            properties:
              custom_credit_type_id:
                type: string
                format: uuid
              fiat_currency_credit_type_id:
                type: string
                format: uuid
              to_fiat_conversion_factor:
                type: number
                description: >-
                  The overage cost in fiat currency for each credit of the
                  custom credit type.
    Id:
      required:
        - id
      type: object
      properties:
        id:
          type: string
          format: uuid
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
