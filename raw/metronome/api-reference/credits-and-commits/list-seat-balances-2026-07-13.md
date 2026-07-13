<!-- Source URL: https://docs.metronome.com/api-reference/credits-and-commits/list-seat-balances.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List seat balances

> Retrieve detailed balance for seat-based credits and commits from the contract's subscriptions, broken down by individual seats.

### Use this endpoint to:
- Display per-seat balance information in customer dashboards
- Filter balance data by subscription or specific seats

### Key response fields:
An array of seat balance objects containing:
- Seat id
- Balance: current total balance across all commits and credits

### Usage guidelines:
- Date filtering: use `covering_date` OR `starting_at`/`ending_before` to filter balance data by time range
- Set `include_credits_and_commits=true` for detailed commits and credits breakdown per seat
- Set `include_ledgers=true` for detailed transaction history per commit/credit per seat




## OpenAPI

````yaml /openapi.json post /v1/contracts/seatBalances/list
openapi: 3.0.1
info:
  title: Metronome
  version: 1.0.0
servers:
  - url: https://api.metronome.com
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
  - name: Products
    description: Products are the items that customers purchase.
  - name: Rate cards
    description: Rate cards are used to define default pricing for products.
  - name: Contracts
    description: >-
      A contract defines a customer’s products, pricing, discounts, commitments,
      and more. Use these endpoints to create and update contracts data.
  - name: Credits and commits
    description: Credits and commits are used to manage customer balances.
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
  - name: Named schedules
    description: >-
      Named schedules are used for storing custom data that can change over
      time. Named schedules are often used in custom pricing logic.
paths:
  /v1/contracts/seatBalances/list:
    post:
      tags:
        - Credits and commits
      summary: List seat balances
      description: >
        Retrieve detailed balance for seat-based credits and commits from the
        contract's subscriptions, broken down by individual seats.


        ### Use this endpoint to:

        - Display per-seat balance information in customer dashboards

        - Filter balance data by subscription or specific seats


        ### Key response fields:

        An array of seat balance objects containing:

        - Seat id

        - Balance: current total balance across all commits and credits


        ### Usage guidelines:

        - Date filtering: use `covering_date` OR `starting_at`/`ending_before`
        to filter balance data by time range

        - Set `include_credits_and_commits=true` for detailed commits and
        credits breakdown per seat

        - Set `include_ledgers=true` for detailed transaction history per
        commit/credit per seat
      operationId: listSeatBalances-v1
      requestBody:
        description: List seat-level balances for commits and credits.
        content:
          application/json:
            schema:
              type: object
              required:
                - customer_id
                - contract_id
              properties:
                customer_id:
                  type: string
                  format: uuid
                  description: The customer ID to retrieve seat balances for
                contract_id:
                  type: string
                  format: uuid
                  description: The contract ID to retrieve seat balances for
                subscription_ids:
                  type: array
                  items:
                    type: string
                    format: uuid
                  description: >-
                    Optional filter to only include seats from specific
                    subscriptions. If subscriptions ids are not mapped to
                    SEAT_BASED subscriptions, error will be returned.
                seat_ids:
                  type: array
                  items:
                    type: string
                  description: Optional filter to only include specific seats.
                skip_missing_seat_ids:
                  type: boolean
                  default: false
                  description: >-
                    When true, any seat_ids not found in contract subscriptions
                    will be silently omitted from the response instead of
                    returning a 400 error.
                include_credits_and_commits:
                  type: boolean
                  default: false
                  description: Include credits and commits in the response
                include_ledgers:
                  type: boolean
                  default: false
                  description: >-
                    Include ledger entries for each commit and commit.
                    `include_credits_and_commits` must be set to `true` for
                    `include_ledgers=true` to apply.
                starting_at:
                  type: string
                  format: date-time
                  description: >-
                    Include only commits or credits with access effective on or
                    after this date (cannot be used with covering_date).
                effective_before:
                  type: string
                  format: date-time
                  description: >-
                    Include only commits or credits with access effective on or
                    before this date (cannot be used with covering_date).
                covering_date:
                  type: string
                  format: date-time
                  description: >-
                    Include only commits or credits with access that cover this
                    specific date (cannot be used with starting_at or
                    ending_before).
                limit:
                  type: integer
                  description: >
                    Maximum number of seats to return. Range: 1-100. Default:
                    25.

                    When `include_credits_and_commits = true`, if the total
                    commits/credits across all seats exceeds 100, a limit of 100
                    applies to the total credits and commits. Seats are included
                    greedily to maximize the number of seats returned.

                    Example: if seat 1 has 98 commits and seat 2 has 10 commits,
                    both seats will be returned (total: 108 commits). Each
                    returned seat includes all of its associated credits and
                    commits.
                cursor:
                  type: string
                  description: >-
                    Page token from a previous response to retrieve the next
                    page
            example:
              customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
              contract_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
              subscription_ids:
                - 8deed800-1b7a-495d-a207-6c52bac54dc9
              include_credits_and_commits: true
              include_ledgers: true
              covering_date: '2024-03-01T00:00:00.000Z'
              limit: 25
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                required:
                  - data
                  - pagination
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/SeatBalance'
                  pagination:
                    type: object
                    required:
                      - seats_included
                      - seats_available_for_next_page
                    properties:
                      seats_included:
                        type: number
                        description: Number of seats included in this response
                      seats_available_for_next_page:
                        type: number
                        description: Number of seats available to fetch in the next page
                      next_page:
                        type: string
                        nullable: true
                        description: >-
                          Token to retrieve the next page of results. Null if no
                          more pages available
              example:
                data:
                  - seat_id: seat_1
                    balances:
                      - credit_type_id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                        balance: 30000
                        starting_balance: 50000
                    commits:
                      - id: 62c0cb84-bf3f-48b9-9bcf-a8ddf8c1cf35
                        balance: 30000
                        start_date: '2024-01-01T00:00:00.000Z'
                        end_date: '2024-02-01T00:00:00.000Z'
                        ledger_entries:
                          - type: PREPAID_COMMIT_SEGMENT_START
                            amount: 50000
                            timestamp: '2024-01-01T00:00:00.000Z'
                          - type: PREPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION
                            amount: -20000
                            timestamp: '2024-01-31T00:00:00.000Z'
                    credits:
                      - id: fa411f5b-fb85-4755-9d4d-530717be083c
                        balance: 20000
                        start_date: '2024-01-01T00:00:00.000Z'
                        end_date: '2024-02-01T00:00:00.000Z'
                        ledger_entries:
                          - type: CREDIT_SEGMENT_START
                            amount: 25000
                            timestamp: '2024-01-01T00:00:00.000Z'
                          - type: CREDIT_AUTOMATED_INVOICE_DEDUCTION
                            amount: -5000
                            timestamp: '2024-01-31T00:00:00.000Z'
                  - seat_id: seat_2
                    balances:
                      - credit_type_id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                        balance: 45000
                        starting_balance: 45000
                    commits:
                      - id: 62c0cb84-bf3f-48b9-9bcf-a8ddf8c1cf35
                        balance: 45000
                        start_date: '2024-01-01T00:00:00.000Z'
                        end_date: '2024-02-01T00:00:00.000Z'
                        ledger_entries:
                          - type: PREPAID_COMMIT_SEGMENT_START
                            amount: 45000
                            timestamp: '2024-01-01T00:00:00.000Z'
                    credits: []
                pagination:
                  next_page: eyJsYXN0X3NlYXRfaWQiai
                  seats_included: 2
                  seats_available_for_next_page: 8
        '404':
          $ref: '#/components/responses/NotFound'
components:
  schemas:
    SeatBalance:
      type: object
      required:
        - seat_id
        - balances
      properties:
        seat_id:
          type: string
          description: The unique identifier for the seat
        balances:
          type: array
          items:
            $ref: '#/components/schemas/SeatBalanceByCreditType'
        commits:
          type: array
          nullable: true
          description: Array of commits applicable to this seat with their balances
          items:
            $ref: '#/components/schemas/SeatCommitBalance'
        credits:
          type: array
          description: Array of credits applicable to this seat with their balances
          items:
            $ref: '#/components/schemas/SeatCreditBalance'
    SeatBalanceByCreditType:
      type: object
      required:
        - credit_type_id
        - balance
        - starting_balance
      properties:
        credit_type_id:
          type: string
          format: uuid
        balance:
          type: number
          description: >-
            The total balance across all commits and credits for this seat, of
            this credit type.
        starting_balance:
          type: number
          description: >-
            The total initial balances of all commits and credits for this seat,
            of this credit type.
    SeatCommitBalance:
      type: object
      required:
        - id
        - balance
        - start_date
      properties:
        id:
          type: string
          format: uuid
          description: The commit or credit ID
        balance:
          type: number
          description: The current balance for this commit for this specific seat
        start_date:
          type: string
          format: date-time
          description: The datetime when the commit becomes active
        end_date:
          type: string
          format: date-time
          nullable: true
          description: The datetime when the commit expires
        ledger_entries:
          type: array
          items:
            $ref: '#/components/schemas/SeatBalanceCommitLedger'
          description: >-
            Transaction history for this commit for this seat (only included if
            include_ledgers=true)
    SeatCreditBalance:
      type: object
      required:
        - id
        - balance
        - start_date
      properties:
        id:
          type: string
          format: uuid
          description: The credit ID
        balance:
          type: number
          description: The current balance for this credit for this specific seat
        start_date:
          type: string
          format: date-time
          description: The datetime when the credit becomes active
        end_date:
          type: string
          format: date-time
          nullable: true
          description: The datetime when the credit expires
        ledger_entries:
          type: array
          items:
            $ref: '#/components/schemas/SeatBalanceCreditLedger'
          description: >-
            Transaction history for this credit for this seat (only included if
            include_ledgers=true)
    Error:
      required:
        - message
      type: object
      properties:
        message:
          type: string
    SeatBalanceCommitLedger:
      type: object
      required:
        - type
        - amount
        - timestamp
      properties:
        type:
          $ref: '#/components/schemas/SeatBalanceCommitLedgerEntryType'
          description: Commit ledger type
        amount:
          type: number
          description: Amount of the ledger entry
        timestamp:
          type: string
          format: date-time
          description: The datetime when the ledger is created
    SeatBalanceCreditLedger:
      type: object
      required:
        - type
        - amount
        - timestamp
      properties:
        type:
          $ref: '#/components/schemas/SeatBalanceCreditLedgerEntryType'
          description: Credit ledger type
        amount:
          type: number
          description: Amount of the ledger entry
        timestamp:
          type: string
          format: date-time
          description: The datetime when the ledger is created
    SeatBalanceCommitLedgerEntryType:
      type: string
      enum:
        - PREPAID_COMMIT_SEGMENT_START
        - PREPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION
        - PREPAID_COMMIT_ROLLOVER
        - PREPAID_COMMIT_EXPIRATION
        - PREPAID_COMMIT_CANCELED
        - PREPAID_COMMIT_CREDITED
        - PREPAID_COMMIT_MANUAL
        - PREPAID_COMMIT_SEAT_BASED_ADJUSTMENT
    SeatBalanceCreditLedgerEntryType:
      type: string
      enum:
        - CREDIT_SEGMENT_START
        - CREDIT_AUTOMATED_INVOICE_DEDUCTION
        - CREDIT_EXPIRATION
        - CREDIT_CANCELED
        - CREDIT_CREDITED
        - CREDIT_MANUAL
        - CREDIT_SEAT_BASED_ADJUSTMENT
        - CREDIT_ROLLOVER
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
