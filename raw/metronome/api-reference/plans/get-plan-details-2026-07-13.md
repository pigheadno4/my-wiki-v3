<!-- Source URL: https://docs.metronome.com/api-reference/plans/get-plan-details.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get plan details

> Fetch high level details of a specific plan. This is a Plans (deprecated) endpoint. New clients should implement using Contracts.




## OpenAPI

````yaml /openapi.plans.json get /planDetails/{plan_id}
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
  /planDetails/{plan_id}:
    get:
      tags:
        - Plans
      summary: Get plan details
      description: >
        Fetch high level details of a specific plan. This is a Plans
        (deprecated) endpoint. New clients should implement using Contracts.
      operationId: getPlanDetails
      parameters:
        - $ref: '#/components/parameters/PlanId'
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
                    $ref: '#/components/schemas/PlanDetail'
              example:
                data:
                  id: d46c3bce-40a6-4fbf-9b45-fcb00d45ad5f
                  name: Plan with Minimums
                  description: A plan with minimums
                  credit_grants:
                    - name: Acme Corp Promotional Credit Grant
                      amount_granted: 2400
                      amount_paid: 1500
                      effective_duration: 3
                      priority: '1'
                      send_invoice: true
                      reason: Prepaid grant
                      recurrence_interval: 1
                      amount_granted_credit_type:
                        id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                        name: USD (cents)
                      amount_paid_credit_type:
                        id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                        name: USD (cents)
                  minimums:
                    - name: Invoice minimum
                      value: 10000
                      start_period: 0
                      credit_type:
                        id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                        name: USD (cents)
                  overage_rates:
                    - start_period: 0
                      to_fiat_conversion_factor: 1600
                      fiat_credit_type:
                        id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                        name: USD (cents)
                      credit_type:
                        id: d46c3bce-40a6-4fbf-9b45-fcb00d45ad5f
                        name: MetroBux
                  custom_fields:
                    x_account_id: KyVnHhSBWl7eY2bl
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
  schemas:
    PlanDetail:
      required:
        - id
        - name
        - custom_fields
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        description:
          type: string
        minimums:
          type: array
          items:
            required:
              - name
              - value
              - start_period
              - credit_type
            type: object
            properties:
              name:
                type: string
              value:
                type: number
              start_period:
                type: number
                description: >-
                  Used in price ramps.  Indicates how many billing periods pass
                  before the charge applies.
              credit_type:
                $ref: '#/components/schemas/CreditType'
        overage_rates:
          type: array
          items:
            required:
              - to_fiat_conversion_factor
              - start_period
              - fiat_credit_type
              - credit_type
            type: object
            properties:
              to_fiat_conversion_factor:
                type: number
              start_period:
                type: number
                description: >-
                  Used in price ramps.  Indicates how many billing periods pass
                  before the charge applies.
              fiat_credit_type:
                $ref: '#/components/schemas/CreditType'
              credit_type:
                $ref: '#/components/schemas/CreditType'
        credit_grants:
          type: array
          items:
            required:
              - name
              - amount_granted
              - amount_paid
              - priority
              - effective_duration
              - send_invoice
              - amount_granted_credit_type
              - amount_paid_credit_type
            type: object
            properties:
              name:
                type: string
              amount_granted:
                type: number
              amount_paid:
                type: number
              effective_duration:
                type: number
              priority:
                type: string
              send_invoice:
                type: boolean
              reason:
                type: string
              recurrence_duration:
                type: number
              recurrence_interval:
                type: number
              amount_paid_credit_type:
                $ref: '#/components/schemas/CreditType'
              amount_granted_credit_type:
                $ref: '#/components/schemas/CreditType'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: plan
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
