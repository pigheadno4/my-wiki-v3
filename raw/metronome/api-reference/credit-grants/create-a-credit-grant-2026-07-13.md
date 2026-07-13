<!-- Source URL: https://docs.metronome.com/api-reference/credit-grants/create-a-credit-grant.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a credit grant

> Create a new credit grant. This is a Plans (deprecated) endpoint. New clients should implement using Contracts.




## OpenAPI

````yaml /openapi.plans.json post /credits/createGrant
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
  /credits/createGrant:
    post:
      tags:
        - Credit grants
      summary: Create a credit grant
      description: >
        Create a new credit grant. This is a Plans (deprecated) endpoint. New
        clients should implement using Contracts.
      operationId: createGrant
      requestBody:
        description: The details of the credit grant to create.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateCreditGrantPayload'
            example:
              customer_id: 9b85c1c1-5238-4f2a-a409-61412905e1e1
              grant_amount:
                amount: 1000
                credit_type_id: 5ae401dc-a648-4b49-9ac3-391bb5bc4d7b
              name: Acme Corp Promotional Credit Grant
              reason: Incentivize new customer
              effective_at: '2022-02-01T00:00:00Z'
              expires_at: '2022-04-01T00:00:00Z'
              paid_amount:
                amount: 5000
                credit_type_id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
              priority: 0.5
              credit_grant_type: trial
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
  schemas:
    CreateCreditGrantPayload:
      required:
        - customer_id
        - grant_amount
        - name
        - expires_at
        - paid_amount
        - priority
      type: object
      properties:
        customer_id:
          type: string
          format: uuid
          description: the Metronome ID of the customer
        uniqueness_key:
          $ref: '#/components/schemas/UniquenessKey'
        grant_amount:
          description: the amount of credits granted
          type: object
          required:
            - amount
            - credit_type_id
          properties:
            amount:
              type: number
            credit_type_id:
              description: >-
                the ID of the pricing unit to be used. Defaults to USD (cents)
                if not passed.
              type: string
              format: uuid
        paid_amount:
          description: the amount paid for this credit grant
          type: object
          required:
            - amount
            - credit_type_id
          properties:
            amount:
              type: number
            credit_type_id:
              description: >-
                the ID of the pricing unit to be used. Defaults to USD (cents)
                if not passed.
              type: string
              format: uuid
        name:
          type: string
          description: the name of the credit grant as it will appear on invoices
        effective_at:
          type: string
          format: date-time
          description: >-
            The credit grant will only apply to usage or charges dated on or
            after this timestamp
        expires_at:
          type: string
          format: date-time
          description: >-
            The credit grant will only apply to usage or charges dated before
            this timestamp
        invoice_date:
          type: string
          format: date-time
          description: The date to issue an invoice for the paid_amount.
        priority:
          type: number
        reason:
          type: string
        credit_grant_type:
          type: string
        product_ids:
          type: array
          items:
            type: string
            format: uuid
          description: >-
            The product(s) which these credits will be applied to. (If
            unspecified, the credits will be applied to charges for all
            products.). The array ordering specified here will be used to
            determine the order in which credits will be applied to invoice line
            items
        rollover_settings:
          $ref: '#/components/schemas/CreditGrantRolloverSettings'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          description: Custom fields to attach to the credit grant.
    Id:
      required:
        - id
      type: object
      properties:
        id:
          type: string
          format: uuid
    UniquenessKey:
      type: string
      minLength: 1
      maxLength: 128
      description: >-
        Prevents the creation of duplicates. If a request to create a record is
        made with a previously used uniqueness key, a new record will not be
        created and the request will fail with a 409 error.
    CreditGrantRolloverSettings:
      type: object
      description: >-
        Configure a rollover for this credit grant so if it expires it rolls
        over a configured amount to a new credit grant. This feature is
        currently opt-in only. Contact Metronome to be added to the beta.
      required:
        - expires_at
        - priority
        - rollover_amount
      properties:
        expires_at:
          type: string
          format: date-time
          description: The date to expire the rollover credits.
        priority:
          type: number
          description: >-
            The priority to give the rollover credit grant that gets created
            when a rollover happens.
        rollover_amount:
          description: Specify how much to rollover to the rollover credit grant
          oneOf:
            - $ref: '#/components/schemas/RolloverAmountMaxPercentage'
            - $ref: '#/components/schemas/RolloverAmountMaxAmount'
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
    RolloverAmountMaxPercentage:
      type: object
      required:
        - type
        - value
      properties:
        type:
          type: string
          enum:
            - MAX_PERCENTAGE
          description: Rollover up to a percentage of the original credit grant amount.
        value:
          type: number
          description: >-
            The maximum percentage (0-1) of the original credit grant to
            rollover.
          minimum: 0
          maximum: 1
    RolloverAmountMaxAmount:
      type: object
      required:
        - type
        - value
      properties:
        type:
          type: string
          enum:
            - MAX_AMOUNT
          description: Rollover up to a fixed amount of the original credit grant amount.
        value:
          type: number
          description: The maximum amount to rollover.
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
