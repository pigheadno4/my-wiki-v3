<!-- Source URL: https://docs.metronome.com/api-reference/credit-grants/list-credit-ledger-entries.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List credit ledger entries

> Fetches a list of credit ledger entries. Returns lists of ledgers per customer. Ledger entries are returned in chronological order. Ledger entries associated with voided credit grants are not included. This is a Plans (deprecated) endpoint. New clients should implement using Contracts.




## OpenAPI

````yaml /openapi.plans.json post /credits/listEntries
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
  /credits/listEntries:
    post:
      tags:
        - Credit grants
      summary: List credit ledger entries
      description: >
        Fetches a list of credit ledger entries. Returns lists of ledgers per
        customer. Ledger entries are returned in chronological order. Ledger
        entries associated with voided credit grants are not included. This is a
        Plans (deprecated) endpoint. New clients should implement using
        Contracts.
      operationId: listCreditLedgerEntries
      parameters:
        - $ref: '#/components/parameters/NextPage'
        - in: query
          name: sort
          description: Ledgers sort order by date, asc or desc. Defaults to asc.
          required: false
          schema:
            type: string
            enum:
              - asc
              - desc
      requestBody:
        description: Optional filters on the ledger entries to return
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreditLedgerEntriesQueryPayload'
            example:
              starting_on: '2021-01-01T00:00:00Z'
              ending_before: '2021-02-01T00:00:00Z'
              customer_ids:
                - 6a37bb88-8538-48c5-b37b-a41c836328bd
              credit_type_ids:
                - 2714e483-4ff1-48e4-9e25-ac732e8f24f2
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
                      $ref: '#/components/schemas/CustomerCreditTypeLedger'
                  next_page:
                    type: string
                    nullable: true
              example:
                data:
                  - customer_id: 6a37bb88-8538-48c5-b37b-a41c836328bd
                    ledgers:
                      - credit_type:
                          id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                          name: USD (cents)
                        starting_balance:
                          including_pending: 400
                          excluding_pending: 400
                          effective_at: '2021-01-01T00:00:00Z'
                        ending_balance:
                          including_pending: 110
                          excluding_pending: 400
                          effective_at: '2021-02-01T00:00:00Z'
                        entries: []
                        pending_entries:
                          - amount: 290
                            reason: Automated invoice deduction
                            running_balance: 110
                            effective_at: '2021-02-01T00:00:00Z'
                            created_by: Metronome System
                            credit_grant_id: f06b3d1b-c724-4e0b-99d1-20c0526bf21b
                            invoice_id: 92fb6de8-eb2f-47e5-ae1b-b1e0fb1f388d
                next_page: null
        '404':
          $ref: '#/components/responses/NotFound'
components:
  parameters:
    NextPage:
      name: next_page
      in: query
      description: Cursor that indicates where the next page of results should start.
      required: false
      schema:
        type: string
  schemas:
    CreditLedgerEntriesQueryPayload:
      type: object
      properties:
        customer_ids:
          type: array
          description: >-
            A list of Metronome customer IDs to fetch ledger entries for. If
            absent, ledger entries for all customers will be returned.
          items:
            type: string
            format: uuid
        credit_type_ids:
          type: array
          description: >-
            A list of Metronome credit type IDs to fetch ledger entries for. If
            absent, ledger entries for all credit types will be returned.
          items:
            type: string
            format: uuid
        starting_on:
          type: string
          description: >-
            If supplied, only ledger entries effective at or after this time
            will be returned.
          format: date-time
        ending_before:
          type: string
          description: >-
            If supplied, ledger entries will only be returned with an
            effective_at before this time. This timestamp must not be in the
            future. If no timestamp is supplied, all entries up to the start of
            the customer's next billing period will be returned.
          format: date-time
    CustomerCreditTypeLedger:
      type: object
      required:
        - customer_id
        - ledgers
      properties:
        customer_id:
          type: string
          format: uuid
        ledgers:
          type: array
          items:
            $ref: '#/components/schemas/CreditTypeLedger'
    CreditTypeLedger:
      type: object
      required:
        - credit_type
        - starting_balance
        - ending_balance
        - entries
        - pending_entries
      properties:
        credit_type:
          $ref: '#/components/schemas/CreditType'
        starting_balance:
          type: object
          required:
            - excluding_pending
            - including_pending
            - effective_at
          properties:
            excluding_pending:
              type: number
              description: >-
                the starting balance, including all posted grants, deductions,
                and expirations that happened at or before the effective_at
                timestamp
            including_pending:
              type: number
              description: >-
                the excluding_pending balance plus any pending activity that has
                not been posted at the time of the query
            effective_at:
              type: string
              format: date-time
              description: >-
                the starting_on request parameter (if supplied) or the first
                credit grant's effective_at date
        ending_balance:
          description: the effective balances at the end of the specified time window
          type: object
          required:
            - excluding_pending
            - including_pending
            - effective_at
          properties:
            excluding_pending:
              type: number
              description: >-
                the ending balance, including the balance of all grants that
                have not expired before the effective_at date and deductions
                that happened before the effective_at date
            including_pending:
              type: number
              description: >-
                the excluding_pending balance plus any pending invoice
                deductions and expirations that will happen by the effective_at
                date
            effective_at:
              type: string
              format: date-time
              description: >-
                the ending_before request parameter (if supplied) or the current
                billing period's end date
        entries:
          type: array
          items:
            $ref: '#/components/schemas/CreditLedgerEntry'
        pending_entries:
          type: array
          items:
            $ref: '#/components/schemas/CreditLedgerEntry'
    Error:
      required:
        - message
      type: object
      properties:
        message:
          type: string
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
