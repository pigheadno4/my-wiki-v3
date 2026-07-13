<!-- Source URL: https://docs.metronome.com/api-reference/plans/list-customers-on-a-plan.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List customers on a plan

> Fetches a list of customers on a specific plan (by default, only currently active plans are included). This is a Plans (deprecated) endpoint. New clients should implement using Contracts.




## OpenAPI

````yaml /openapi.plans.json get /planDetails/{plan_id}/customers
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
  /planDetails/{plan_id}/customers:
    get:
      tags:
        - Plans
      summary: List customers on a plan
      description: >
        Fetches a list of customers on a specific plan (by default, only
        currently active plans are included). This is a Plans (deprecated)
        endpoint. New clients should implement using Contracts.
      operationId: getPlanCustomers
      parameters:
        - $ref: '#/components/parameters/PlanId'
        - $ref: '#/components/parameters/PageLimit'
        - $ref: '#/components/parameters/NextPage'
        - $ref: '#/components/parameters/CustomerPlanStatus'
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
                      $ref: '#/components/schemas/CustomerAndPlanDetail'
                  next_page:
                    type: string
                    nullable: true
              example:
                data:
                  - customer_details:
                      id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                      created_at: '2024-01-01T00:00:00.000Z'
                      updated_at: '2024-01-01T00:00:00.000Z'
                      external_id: team@example.com
                      ingest_aliases:
                        - team@example.com
                      name: Example, Inc.
                      customer_config:
                        salesforce_account_id: 0015500001WO1ZiABL
                      custom_fields:
                        x_account_id: KyVnHhSBWl7eY2bl
                    plan_details:
                      id: d46c3bce-40a6-4fbf-9b45-fcb00d45ad5f
                      name: Plan with Minimums
                      ending_before: '2024-04-01T00:00:00Z'
                      starting_on: '2022-02-01T00:00:00Z'
                      custom_fields:
                        x_account_id: KyVnHhSBWl7eY2bl
                      customer_plan_id: a23b3cf4-47fb-4c3f-bb3d-9e64f7704015
                next_page: null
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
    CustomerPlanStatus:
      name: status
      in: query
      description: >-
        Status of customers on a given plan. Defaults to `active`.


        * `all` - Return current, past, and upcoming customers of the plan.

        * `active` - Return current customers of the plan.

        * `ended` - Return past customers of the plan.

        * `upcoming` - Return upcoming customers of the plan.


        Multiple statuses can be OR'd together using commas, e.g.
        `active,ended`.

        **Note:** `ended,upcoming` combination is not yet supported.
      required: false
      schema:
        type: string
        enum:
          - all
          - active
          - ended
          - upcoming
      explode: false
  schemas:
    CustomerAndPlanDetail:
      required:
        - customer_details
        - plan_details
      type: object
      properties:
        customer_details:
          $ref: '#/components/schemas/CustomerDetail'
        plan_details:
          $ref: '#/components/schemas/CustomerPlanDetail'
    CustomerDetail:
      required:
        - external_id
        - id
        - name
        - created_at
        - updated_at
        - customer_config
        - ingest_aliases
        - custom_fields
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: the Metronome ID of the customer
        external_id:
          type: string
          description: >-
            (deprecated, use ingest_aliases instead) the first ID (Metronome or
            ingest alias) that can be used in usage events
        ingest_aliases:
          type: array
          description: >-
            aliases for this customer that can be used instead of the Metronome
            customer ID in usage events
          items:
            type: string
        name:
          type: string
        customer_config:
          $ref: '#/components/schemas/CustomerConfig'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: customer
        created_at:
          type: string
          format: date-time
          description: RFC 3339 timestamp indicating when the customer was created.
        archived_at:
          type: string
          format: date-time
          description: >-
            RFC 3339 timestamp indicating when the customer was archived. Null
            if the customer is active.
          nullable: true
        updated_at:
          type: string
          format: date-time
          description: RFC 3339 timestamp indicating when the customer was last updated.
        current_billable_status:
          x-mint:
            groups:
              - client_id:5b9e3072-415b-4842-94f0-0b6700c8b6be
              - client_id:179e395f-5349-4fe2-bf12-64ab4e5bc560
              - client_id:f157d376-0781-4ef3-9db9-775a9052148e
              - client_id:7dd2f652-7629-4925-9069-77f5c5d3db37
              - client_id:c0ce3dc0-6d3e-4f6b-aadf-dfb90f2bf9f5
              - client_id:cf874b25-ca3b-460b-b6fe-5f33b3c2ea33
              - client_id:9c7e2b27-9b4c-4b76-9df7-f9cb05665a6a
              - client_id:8e3a848a-4566-4cfb-be49-64d80118a7fc
          required:
            - value
          type: object
          description: >-
            This field's availability is dependent on your client's
            configuration.
          properties:
            value:
              $ref: '#/components/schemas/BillableStatus'
            effective_at:
              type: string
              format: date-time
              nullable: true
    CustomerPlanDetail:
      required:
        - id
        - name
        - custom_fields
        - starting_on
        - customer_plan_id
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        starting_on:
          type: string
          format: date-time
          description: The start date of the plan
        ending_before:
          type: string
          format: date-time
          description: The end date of the plan
          nullable: true
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: plan
        customer_plan_id:
          type: string
          format: uuid
    CustomerConfig:
      required:
        - salesforce_account_id
      type: object
      properties:
        salesforce_account_id:
          type: string
          description: The Salesforce account ID for the customer
          nullable: true
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
    BillableStatus:
      type: string
      enum:
        - billable
        - unbillable
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
