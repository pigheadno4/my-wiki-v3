<!-- Source URL: https://docs.metronome.com/api-reference/invoices/get-customer-costs.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get customer costs

> Fetch daily pending costs for the specified customer, broken down by credit type and line items. Note: this is not supported for customers whose plan includes a UNIQUE-type billable metric. This is a Plans (deprecated) endpoint. New clients should implement using Contracts.




## OpenAPI

````yaml /openapi.plans.json get /customers/{customer_id}/costs
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
  /customers/{customer_id}/costs:
    get:
      tags:
        - Invoices
      summary: Get customer costs
      description: >
        Fetch daily pending costs for the specified customer, broken down by
        credit type and line items. Note: this is not supported for customers
        whose plan includes a UNIQUE-type billable metric. This is a Plans
        (deprecated) endpoint. New clients should implement using Contracts.
      operationId: getCosts
      parameters:
        - $ref: '#/components/parameters/CustomerId'
        - $ref: '#/components/parameters/RequiredStartDate'
        - $ref: '#/components/parameters/RequiredEndDate'
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
                      $ref: '#/components/schemas/Costs'
                  next_page:
                    type: string
                    nullable: true
              example:
                data:
                  - start_timestamp: '2024-01-01T00:00:00Z'
                    end_timestamp: '2024-01-02T00:00:00Z'
                    credit_types:
                      2714e483-4ff1-48e4-9e25-ac732e8f24f2:
                        name: USD (cents)
                        cost: 123.45
                        line_item_breakdown:
                          - name: CPU hours
                            cost: 123.45
                next_page: null
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '404':
          $ref: '#/components/responses/NotFound'
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
    RequiredStartDate:
      name: starting_on
      in: query
      description: RFC 3339 timestamp (inclusive)
      required: true
      schema:
        type: string
        format: date-time
      example: '2024-01-01T00:00:00Z'
    RequiredEndDate:
      name: ending_before
      in: query
      description: RFC 3339 timestamp (exclusive)
      required: true
      schema:
        type: string
        format: date-time
      example: '2024-02-01T00:00:00Z'
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
    Costs:
      required:
        - start_timestamp
        - end_timestamp
        - credit_types
      type: object
      properties:
        start_timestamp:
          type: string
          format: date-time
        end_timestamp:
          type: string
          format: date-time
        credit_types:
          $ref: '#/components/schemas/CostsPerCreditType'
          type: object
    Error:
      required:
        - message
      type: object
      properties:
        message:
          type: string
    CostsPerCreditType:
      type: object
      additionalProperties:
        type: object
        properties:
          name:
            type: string
          cost:
            type: number
          line_item_breakdown:
            type: array
            items:
              $ref: '#/components/schemas/LineItemBreakdown'
    LineItemBreakdown:
      type: object
      required:
        - name
        - cost
      properties:
        name:
          type: string
        cost:
          type: number
        group_key:
          type: string
        group_value:
          type: string
          nullable: true
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
