<!-- Source URL: https://docs.metronome.com/api-reference/credit-grants/list-credit-grants.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List credit grants

> List credit grants. This list does not included voided grants. This is a Plans (deprecated) endpoint. New clients should implement using Contracts.




## OpenAPI

````yaml /openapi.plans.json post /credits/listGrants
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
  /credits/listGrants:
    post:
      tags:
        - Credit grants
      summary: List credit grants
      description: >
        List credit grants. This list does not included voided grants. This is a
        Plans (deprecated) endpoint. New clients should implement using
        Contracts.
      operationId: listGrants
      parameters:
        - $ref: '#/components/parameters/PageLimit'
        - $ref: '#/components/parameters/NextPage'
      requestBody:
        description: Filters specifying which credit grants should be included
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ListCreditGrantPayload'
            example:
              credit_type_ids:
                - 2714e483-4ff1-48e4-9e25-ac732e8f24f2
              customer_ids:
                - d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                - 0e5b8609-d901-4992-b394-c3c2e3f37b1c
              not_expiring_before: '2022-02-01T00:00:00Z'
              effective_before: '2022-02-01T00:00:00Z'
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
                      $ref: '#/components/schemas/CreditGrant'
                  next_page:
                    type: string
                    nullable: true
              example:
                data:
                  - id: 9acbc1d0-2044-44c4-8577-f6078a1d8cd2
                    name: Initial credit purchase
                    customer_id: b310b282-d5cf-4e4f-915f-d8c3c4971e45
                    uniqueness_key: 823j7fqzo1
                    reason: Prepayment
                    effective_at: '2022-01-01T00:00:00.000Z'
                    expires_at: '2022-04-01T00:00:00.000Z'
                    priority: 0.5
                    grant_amount:
                      amount: 100
                      credit_type:
                        id: fa2f1b3d-9d52-4951-a099-25991fd394d6
                        name: cloud consumption units
                    paid_amount:
                      amount: 10
                      credit_type:
                        id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                        name: USD (cents)
                    balance:
                      including_pending: 80
                      excluding_pending: 80
                      effective_at: '2022-02-01T00:00:00.000Z'
                    deductions:
                      - amount: 20
                        reason: Automated invoice deduction
                        running_balance: 80
                        effective_at: '2022-02-01T00:00:00.000Z'
                        created_by: Metronome System
                        credit_grant_id: 9acbc1d0-2044-44c4-8577-f6078a1d8cd2
                        invoice_id: b6a60e95-15f4-403c-be40-f1c1d58cee20
                    pending_deductions: []
                    custom_fields:
                      x_account_id: KyVnHhSBWl7eY2bl
                    credit_grant_type: enterprise
                next_page: null
components:
  parameters:
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
    ListCreditGrantPayload:
      type: object
      properties:
        credit_type_ids:
          description: >-
            An array of credit type IDs. This must not be specified if
            credit_grant_ids is specified.
          type: array
          items:
            type: string
            format: uuid
          example: >-
            d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc,
            0e5b8609-d901-4992-b394-c3c2e3f37b1c
        customer_ids:
          description: >-
            An array of Metronome customer IDs. This must not be specified if
            credit_grant_ids is specified.
          type: array
          items:
            type: string
            format: uuid
          example: >-
            d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc,
            0e5b8609-d901-4992-b394-c3c2e3f37b1c
        credit_grant_ids:
          description: >-
            An array of credit grant IDs. If this is specified, neither
            credit_type_ids nor customer_ids may be specified.
          type: array
          items:
            type: string
            format: uuid
          example: >-
            d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc,
            0e5b8609-d901-4992-b394-c3c2e3f37b1c
        not_expiring_before:
          description: Only return credit grants that expire at or after this timestamp.
          type: string
          format: date-time
          example: '2022-02-01T00:00:00Z'
        effective_before:
          description: >-
            Only return credit grants that are effective before this timestamp
            (exclusive).
          type: string
          format: date-time
          example: '2022-02-01T00:00:00Z'
    CreditGrant:
      required:
        - id
        - name
        - customer_id
        - effective_at
        - expires_at
        - priority
        - grant_amount
        - paid_amount
        - balance
        - deductions
        - pending_deductions
        - custom_fields
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: the Metronome ID of the credit grant
        name:
          type: string
        customer_id:
          type: string
          format: uuid
          description: the Metronome ID of the customer
        invoice_id:
          type: string
          nullable: true
          format: uuid
          description: >-
            the Metronome ID of the invoice with the purchase charge for this
            credit grant, if applicable
        uniqueness_key:
          $ref: '#/components/schemas/UniquenessKey'
          nullable: true
        reason:
          type: string
          nullable: true
        credit_grant_type:
          type: string
          nullable: true
        effective_at:
          type: string
          format: date-time
        expires_at:
          type: string
          format: date-time
        priority:
          type: number
        grant_amount:
          description: the amount of credits initially granted
          type: object
          required:
            - amount
            - credit_type
          properties:
            amount:
              type: number
            credit_type:
              $ref: '#/components/schemas/CreditType'
              description: the credit type for the amount granted
        paid_amount:
          description: the amount paid for this credit grant
          type: object
          required:
            - amount
            - credit_type
          properties:
            amount:
              type: number
            credit_type:
              $ref: '#/components/schemas/CreditType'
              description: the credit type for the amount paid
        balance:
          description: >-
            The effective balance of the grant as of the end of the customer's
            current billing period. Expiration deductions will be included only
            if the grant expires before the end of the current billing period.
          type: object
          required:
            - excluding_pending
            - including_pending
            - effective_at
          properties:
            excluding_pending:
              type: number
              description: >-
                The grant's current balance including all posted deductions. If
                the grant has expired, this amount will be 0.
            including_pending:
              type: number
              description: >-
                The grant's current balance including all posted and pending
                deductions. If the grant expires before the end of the
                customer's current billing period, this amount will be 0.
            effective_at:
              type: string
              format: date-time
              description: The end_date of the customer's current billing period.
        deductions:
          type: array
          items:
            $ref: '#/components/schemas/CreditLedgerEntry'
        pending_deductions:
          type: array
          items:
            $ref: '#/components/schemas/CreditLedgerEntry'
        products:
          description: >-
            The products which these credits will be applied to. (If
            unspecified, the credits will be applied to charges for all
            products.)
          type: array
          items:
            type: object
            required:
              - id
              - name
            properties:
              id:
                type: string
              name:
                type: string
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: credit_grant
    UniquenessKey:
      type: string
      minLength: 1
      maxLength: 128
      description: >-
        Prevents the creation of duplicates. If a request to create a record is
        made with a previously used uniqueness key, a new record will not be
        created and the request will fail with a 409 error.
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
    CreditLedgerEntry:
      type: object
      required:
        - amount
        - reason
        - running_balance
        - effective_at
        - created_by
        - credit_grant_id
      properties:
        amount:
          type: number
          description: an amount representing the change to the customer's credit balance
        reason:
          type: string
          example: Automated invoice deduction
        running_balance:
          type: number
          description: >-
            the running balance for this credit type at the time of the ledger
            entry, including all preceding charges
        effective_at:
          type: string
          format: date-time
        created_by:
          type: string
        credit_grant_id:
          type: string
          format: uuid
          description: the credit grant this entry is related to
        invoice_id:
          type: string
          format: uuid
          nullable: true
          description: >-
            if this entry is a deduction, the Metronome ID of the invoice where
            the credit deduction was consumed; if this entry is a grant, the
            Metronome ID of the invoice where the grant's paid_amount was
            charged
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
