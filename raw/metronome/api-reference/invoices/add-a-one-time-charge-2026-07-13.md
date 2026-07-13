<!-- Source URL: https://docs.metronome.com/api-reference/invoices/add-a-one-time-charge.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a one time charge

> Add a one time charge to the specified invoice. This is a Plans (deprecated) endpoint. New clients should implement using Contracts.




## OpenAPI

````yaml /openapi.plans.json post /customers/{customer_id}/addCharge
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
  /customers/{customer_id}/addCharge:
    post:
      tags:
        - Invoices
      summary: Add a one time charge
      description: >
        Add a one time charge to the specified invoice. This is a Plans
        (deprecated) endpoint. New clients should implement using Contracts.
      operationId: addOneTimeCharge
      parameters:
        - $ref: '#/components/parameters/CustomerId'
      requestBody:
        description: One time charge creation request
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AddOneTimeChargePayload'
            example:
              charge_id: 5ae4b726-1ebe-439c-9190-9831760ba195
              price: 250
              quantity: 1
              description: One time charge
              invoice_start_timestamp: '2024-01-01T00:00:00Z'
              customer_plan_id: a23b3cf4-47fb-4c3f-bb3d-9e64f7704015
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                x-stainless-empty-object: true
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
    AddOneTimeChargePayload:
      required:
        - charge_id
        - price
        - quantity
        - invoice_start_timestamp
        - customer_plan_id
        - description
      type: object
      properties:
        charge_id:
          description: >-
            The Metronome ID of the charge to add to the invoice. Note that the
            charge must be on a product that is not on the current plan, and the
            product must have only fixed charges.
          type: string
          format: uuid
        price:
          description: >-
            The price of the charge. This price will match the currency on the
            invoice, e.g. USD cents.
          type: number
        quantity:
          type: number
        description:
          type: string
        customer_plan_id:
          description: The Metronome ID of the customer plan to add the charge to.
          type: string
          format: uuid
        invoice_start_timestamp:
          description: The start_timestamp of the invoice to add the charge to.
          type: string
          format: date-time
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
