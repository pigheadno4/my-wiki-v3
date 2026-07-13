<!-- Source URL: https://docs.metronome.com/api-reference/plans/list-customer-plans.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List customer plans

> List the given customer's plans in reverse-chronological order. This is a Plans (deprecated) endpoint. New clients should implement using Contracts.




## OpenAPI

````yaml /openapi.plans.json get /customers/{customer_id}/plans
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
  /customers/{customer_id}/plans:
    get:
      tags:
        - Plans
      summary: List customer plans
      description: >
        List the given customer's plans in reverse-chronological order. This is
        a Plans (deprecated) endpoint. New clients should implement using
        Contracts.
      operationId: listCustomerPlans
      parameters:
        - $ref: '#/components/parameters/CustomerId'
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
                      $ref: '#/components/schemas/CustomerPlan'
                  next_page:
                    type: string
                    nullable: true
              example:
                data:
                  - id: 7aa11640-0703-4600-8eb9-293f535a6b74
                    plan_id: 94293d66-aa05-4a8e-881a-c90872047b67
                    plan_name: Standard
                    plan_description: The standard plan for all customers
                    starting_on: '2021-01-01T00:00:00Z'
                    trial_info:
                      ending_before: '2021-01-15T00:00:00Z'
                      spending_caps: []
                    custom_fields:
                      x_account_id: KyVnHhSBWl7eY2bl
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
    CustomerPlan:
      required:
        - id
        - plan_id
        - plan_name
        - plan_description
        - starting_on
        - custom_fields
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: the ID of the customer plan
        plan_id:
          type: string
          format: uuid
          description: the ID of the plan
        plan_name:
          type: string
        plan_description:
          type: string
        starting_on:
          type: string
          format: date-time
        ending_before:
          type: string
          format: date-time
        net_payment_terms_days:
          type: number
        trial_info:
          type: object
          required:
            - ending_before
            - spending_caps
          properties:
            ending_before:
              type: string
              format: date-time
            spending_caps:
              type: array
              items:
                type: object
                required:
                  - amount
                  - amount_remaining
                  - credit_type
                properties:
                  credit_type:
                    $ref: '#/components/schemas/CreditType'
                  amount:
                    type: number
                    example: 123.45
                  amount_remaining:
                    type: number
                    example: 123
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: customer_plan
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
