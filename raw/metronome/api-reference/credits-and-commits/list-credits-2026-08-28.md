<!-- Source URL: https://docs.metronome.com/api-reference/credits-and-commits/list-credits.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List credits

> Retrieve a detailed list of all credits available to a customer, including promotional credits and contract-specific credits. This endpoint provides comprehensive visibility into credit balances, access schedules, and usage rules, enabling you to build credit management interfaces and track available funding.

### Use this endpoint to:
- Display all available credits in customer billing dashboards
- Show credit balances and expiration dates
- Track credit usage history with optional ledger details
- Build credit management and reporting tools
- Monitor promotional credit utilization
• Support customer inquiries about available credits

### Key response fields:
An array of Credit objects containing:
- Credit details: Name, priority, and which applicable products/tags it applies to
- Product ID: The `product_id` of the credit. This is for external mapping into your quote-to-cash stack, not the product it applies to. 
- Access schedule: When credits become available and expire
- Optional ledger entries: Transaction history (if `include_ledgers=true`)
- Balance information: Current available amount (if `include_balance=true`)
- Metadata: Custom fields and usage specifiers

### Usage guidelines:
- Pagination: Results limited to 25 commits per page; use next_page for more
- Date filtering options:
    - `covering_date`: Credits active on a specific date
    - `starting_at`: Credits with access on/after a date
    - `effective_before`: Credits with access before a date (exclusive)
- Scope options:
    - `include_contract_credits`: Include contract-level credits (not just customer-level)
    - `include_archived`: Include archived credits and credits from archived contracts
- Performance considerations:
    - `include_ledgers`: Adds detailed transaction history (slower)
    - `include_balance`: Adds current balance calculation (slower)
- Optional filtering: Use credit_id to retrieve a specific commit




## OpenAPI

````yaml /openapi.json post /v1/contracts/customerCredits/list
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
  /v1/contracts/customerCredits/list:
    post:
      tags:
        - Credits and commits
      summary: List credits
      description: >
        Retrieve a detailed list of all credits available to a customer,
        including promotional credits and contract-specific credits. This
        endpoint provides comprehensive visibility into credit balances, access
        schedules, and usage rules, enabling you to build credit management
        interfaces and track available funding.


        ### Use this endpoint to:

        - Display all available credits in customer billing dashboards

        - Show credit balances and expiration dates

        - Track credit usage history with optional ledger details

        - Build credit management and reporting tools

        - Monitor promotional credit utilization

        • Support customer inquiries about available credits


        ### Key response fields:

        An array of Credit objects containing:

        - Credit details: Name, priority, and which applicable products/tags it
        applies to

        - Product ID: The `product_id` of the credit. This is for external
        mapping into your quote-to-cash stack, not the product it applies to. 

        - Access schedule: When credits become available and expire

        - Optional ledger entries: Transaction history (if
        `include_ledgers=true`)

        - Balance information: Current available amount (if
        `include_balance=true`)

        - Metadata: Custom fields and usage specifiers


        ### Usage guidelines:

        - Pagination: Results limited to 25 commits per page; use next_page for
        more

        - Date filtering options:
            - `covering_date`: Credits active on a specific date
            - `starting_at`: Credits with access on/after a date
            - `effective_before`: Credits with access before a date (exclusive)
        - Scope options:
            - `include_contract_credits`: Include contract-level credits (not just customer-level)
            - `include_archived`: Include archived credits and credits from archived contracts
        - Performance considerations:
            - `include_ledgers`: Adds detailed transaction history (slower)
            - `include_balance`: Adds current balance calculation (slower)
        - Optional filtering: Use credit_id to retrieve a specific commit
      operationId: listCustomerCredits-v1
      requestBody:
        description: List all credits for a customer
        content:
          application/json:
            schema:
              type: object
              required:
                - customer_id
              properties:
                customer_id:
                  type: string
                  format: uuid
                credit_id:
                  type: string
                  format: uuid
                covering_date:
                  description: >-
                    Return only credits that have access schedules that "cover"
                    the provided date
                  type: string
                  format: date-time
                starting_at:
                  description: >-
                    Include only credits that have any access on or after the
                    provided date
                  type: string
                  format: date-time
                effective_before:
                  description: >-
                    Include only credits that have any access before the
                    provided date (exclusive)
                  type: string
                  format: date-time
                include_contract_credits:
                  type: boolean
                  description: Include credits on the contract level.
                include_archived:
                  type: boolean
                  description: >-
                    Include archived credits and credits from archived
                    contracts.
                include_ledgers:
                  type: boolean
                  description: >-
                    Include credit ledgers in the response. Setting this flag
                    may cause the query to be slower.
                include_balance:
                  type: boolean
                  description: >-
                    Include the balance in the response. Setting this flag may
                    cause the query to be slower.
                next_page:
                  type: string
                  description: The next page token from a previous response.
                limit:
                  type: integer
                  minimum: 1
                  maximum: 25
                  default: 25
                  description: The maximum number of commits to return. Defaults to 25.
            example:
              customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
              credit_id: 6162d87b-e5db-4a33-b7f2-76ce6ead4e85
              include_ledgers: true
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
                      $ref: '#/components/schemas/Credit'
                  next_page:
                    type: string
                    nullable: true
              example:
                data:
                  - id: fa411f5b-fb85-4755-9d4d-530717be083c
                    type: CREDIT
                    rate_type: LIST_RATE
                    name: My test credit
                    description: My test credit description
                    priority: 100
                    product:
                      id: 2e30f074-d04c-412e-a134-851ebfa5ceb2
                      name: My product A
                    applicable_product_ids:
                      - 13a2179b-f0cb-460b-85a1-cd42964ca533
                    applicable_contract_ids:
                      - d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                    access_schedule:
                      credit_type:
                        id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                        name: USD (cents)
                      schedule_items:
                        - id: 2d45952c-5a6e-43a9-8aab-f61ee21be81a
                          amount: 10000000
                          starting_at: '2020-02-01T00:00:00.000Z'
                          ending_before: '2021-02-01T00:00:00.000Z'
                    ledger:
                      - invoice_id: 525b9759-7bbd-4a05-aab1-d7c43c976b57
                        amount: 10000000
                        timestamp: '2020-03-01T00:00:00.000Z'
                        type: CREDIT_AUTOMATED_INVOICE_DEDUCTION
                        segment_id: 2d45952c-5a6e-43a9-8aab-f61ee21be81a
                    uniqueness_key: 372p7cvwr3-uniqueness-key
                next_page: null
components:
  schemas:
    Credit:
      type: object
      required:
        - id
        - type
        - product
      properties:
        id:
          type: string
          format: uuid
        contract:
          required:
            - id
          type: object
          properties:
            id:
              type: string
              format: uuid
        type:
          type: string
          enum:
            - CREDIT
        name:
          type: string
        priority:
          type: number
          description: >-
            If multiple credits or commits are applicable, the one with the
            lower priority will apply first.
        product:
          type: object
          required:
            - id
            - name
          properties:
            id:
              type: string
              format: uuid
            name:
              type: string
        access_schedule:
          $ref: '#/components/schemas/ScheduleDuration'
          description: The schedule that the customer will gain access to the credits.
        description:
          type: string
        recurring_credit_id:
          type: string
          format: uuid
          description: >-
            The ID of the recurring credit that this credit was generated from,
            if applicable.
        subscription_config:
          type: object
          properties:
            subscription_id:
              type: string
              format: uuid
            allocation:
              $ref: '#/components/schemas/SubscriptionConfigAllocation'
            apply_seat_increase_config:
              $ref: '#/components/schemas/ApplySeatIncreaseConfigForRecurringCommit'
          description: >-
            The subscription configuration for this credit, if it was generated
            from a recurring credit with a subscription attached.
        applicable_product_ids:
          type: array
          items:
            type: string
            format: uuid
        applicable_product_tags:
          type: array
          items:
            type: string
        specifiers:
          type: array
          description: >-
            List of filters that determine what kind of customer usage draws
            down a commit or credit. A customer's usage needs to meet the
            condition of at least one of the specifiers to contribute to a
            commit's or credit's drawdown.
          items:
            $ref: '#/components/schemas/CommitSpecifier'
        applicable_contract_ids:
          type: array
          items:
            type: string
            format: uuid
        netsuite_sales_order_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          description: >-
            This field's availability is dependent on your client's
            configuration.
        salesforce_opportunity_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          description: >-
            This field's availability is dependent on your client's
            configuration.
        ledger:
          type: array
          items:
            $ref: '#/components/schemas/CreditLedger'
          description: >-
            A list of ordered events that impact the balance of a credit. For
            example, an invoice deduction or an expiration.
        balance:
          $ref: '#/components/schemas/BalanceForCommitsAndCredits'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: contract_credit
        rate_type:
          type: string
          enum:
            - COMMIT_RATE
            - LIST_RATE
        uniqueness_key:
          $ref: '#/components/schemas/UniquenessKeyForCommitsAndCredits'
        hierarchy_configuration:
          $ref: '#/components/schemas/CommitHierarchyConfiguration'
          description: Optional configuration for credit hierarchy access control
        rolled_over_from:
          type: object
          required:
            - contract_id
            - credit_id
          properties:
            credit_id:
              type: string
              format: uuid
            contract_id:
              type: string
              format: uuid
        created_by:
          type: string
          description: >-
            The actor who created this credit. Omitted for system-generated
            credits such as recurring credits.
    ScheduleDuration:
      type: object
      required:
        - schedule_items
      properties:
        access_type:
          x-mint:
            groups:
              - ff:create-quantity-based-commits
          x-stainless-skip: true
          type: string
          enum:
            - SPEND
            - QUANTITY
          description: >-
            Indicates how the balance is drawn down. `SPEND` deducts the dollar
            cost of usage. `QUANTITY` deducts the number of units used.
        credit_type:
          $ref: '#/components/schemas/CreditType'
        schedule_items:
          type: array
          items:
            type: object
            required:
              - id
              - amount
              - starting_at
              - ending_before
            properties:
              id:
                type: string
                format: uuid
              amount:
                type: number
              starting_at:
                type: string
                format: date-time
              ending_before:
                type: string
                format: date-time
    SubscriptionConfigAllocation:
      type: string
      enum:
        - INDIVIDUAL
        - POOLED
    ApplySeatIncreaseConfigForRecurringCommit:
      type: object
      required:
        - is_prorated
      properties:
        is_prorated:
          type: boolean
          description: Indicates whether a mid-period seat increase should be prorated.
    CommitSpecifier:
      type: object
      properties:
        product_id:
          type: string
          format: uuid
          description: >-
            If provided, the specifier will only apply to the product with the
            specified ID.
        product_tags:
          type: array
          items:
            type: string
          description: >-
            If provided, the specifier will only apply to products with all the
            specified tags.
        pricing_group_values:
          type: object
          additionalProperties:
            type: string
        presentation_group_values:
          type: object
          additionalProperties:
            type: string
        exclude:
          x-stainless-skip: true
          x-mint:
            groups:
              - ff:exclude-specifiers-ga
          type: array
          description: >-
            If provided, the specifier will not apply to product usage that
            matches the inclusion criteria and any of the excluding values.
          items:
            $ref: '#/components/schemas/ExcludeSpecifier'
    CreditLedger:
      oneOf:
        - $ref: '#/components/schemas/CreditSegmentStartLedgerEntry'
        - $ref: '#/components/schemas/CreditAutomatedInvoiceDeductionLedgerEntry'
        - $ref: '#/components/schemas/CreditExpirationLedgerEntry'
        - $ref: '#/components/schemas/CreditCanceledLedgerEntry'
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
        - $ref: '#/components/schemas/CreditCreditedLedgerEntry'
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
        - $ref: '#/components/schemas/CreditManualLedgerEntry'
        - $ref: '#/components/schemas/CreditSeatBasedAdjustmentLedgerEntry'
        - $ref: '#/components/schemas/CreditRolloverLedgerEntry'
    BalanceForCommitsAndCredits:
      type: number
      description: >-
        The current balance of the credit or commit. This balance reflects the
        amount of credit or commit that the customer has access to use at this
        moment - thus, expired and upcoming credit or commit segments contribute
        0 to the balance. The balance will match the sum of all ledger entries
        with the exception of the case where the sum of negative manual ledger
        entries exceeds the positive amount remaining on the credit or commit -
        in that case, the balance will be 0. All manual ledger entries
        associated with active credit or commit segments are included in the
        balance, including future-dated manual ledger entries.
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
    UniquenessKeyForCommitsAndCredits:
      type: string
      minLength: 1
      maxLength: 128
      description: >-
        Prevents the creation of duplicates. If a request to create a commit or
        credit is made with a uniqueness key that was previously used to create
        a commit or credit, a new record will not be created and the request
        will fail with a 409 error.
    CommitHierarchyConfiguration:
      type: object
      required:
        - child_access
      properties:
        child_access:
          oneOf:
            - $ref: '#/components/schemas/CommitHierarchyChildAccessAll'
            - $ref: '#/components/schemas/CommitHierarchyChildAccessNone'
            - $ref: '#/components/schemas/CommitHierarchyChildAccessContractIds'
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
    ExcludeSpecifier:
      type: object
      properties:
        product_tags:
          type: array
          items:
            type: string
          description: >-
            If provided, the specifier will not apply to products with all the
            specified tags.
    CreditSegmentStartLedgerEntry:
      type: object
      required:
        - type
        - timestamp
        - amount
        - segment_id
      properties:
        type:
          type: string
          enum:
            - CREDIT_SEGMENT_START
        timestamp:
          type: string
          format: date-time
        amount:
          type: number
        segment_id:
          type: string
          format: uuid
    CreditAutomatedInvoiceDeductionLedgerEntry:
      type: object
      required:
        - type
        - timestamp
        - amount
        - invoice_id
        - segment_id
      properties:
        type:
          type: string
          enum:
            - CREDIT_AUTOMATED_INVOICE_DEDUCTION
        timestamp:
          type: string
          format: date-time
        amount:
          type: number
        segment_id:
          type: string
          format: uuid
        invoice_id:
          type: string
          format: uuid
        contract_id:
          x-mint:
            groups:
              - client_id:11db091c-975b-4908-9f67-b1ceb126acdf
          type: string
          format: uuid
    CreditExpirationLedgerEntry:
      type: object
      required:
        - type
        - timestamp
        - amount
        - segment_id
      properties:
        type:
          type: string
          enum:
            - CREDIT_EXPIRATION
        timestamp:
          type: string
          format: date-time
        amount:
          type: number
        segment_id:
          type: string
          format: uuid
    CreditCanceledLedgerEntry:
      type: object
      required:
        - type
        - timestamp
        - amount
        - invoice_id
        - segment_id
      properties:
        type:
          type: string
          enum:
            - CREDIT_CANCELED
        timestamp:
          type: string
          format: date-time
        amount:
          type: number
        segment_id:
          type: string
          format: uuid
        invoice_id:
          type: string
          format: uuid
        contract_id:
          x-mint:
            groups:
              - client_id:11db091c-975b-4908-9f67-b1ceb126acdf
          type: string
          format: uuid
    CreditCreditedLedgerEntry:
      type: object
      required:
        - type
        - timestamp
        - amount
        - invoice_id
        - segment_id
      properties:
        type:
          type: string
          enum:
            - CREDIT_CREDITED
        timestamp:
          type: string
          format: date-time
        amount:
          type: number
        segment_id:
          type: string
          format: uuid
        invoice_id:
          type: string
          format: uuid
        contract_id:
          x-mint:
            groups:
              - client_id:11db091c-975b-4908-9f67-b1ceb126acdf
          type: string
          format: uuid
    CreditManualLedgerEntry:
      type: object
      required:
        - type
        - timestamp
        - amount
        - reason
      properties:
        type:
          type: string
          enum:
            - CREDIT_MANUAL
        timestamp:
          type: string
          format: date-time
        amount:
          type: number
        reason:
          type: string
    CreditSeatBasedAdjustmentLedgerEntry:
      type: object
      required:
        - type
        - timestamp
        - amount
        - segment_id
      properties:
        type:
          type: string
          enum:
            - CREDIT_SEAT_BASED_ADJUSTMENT
        timestamp:
          type: string
          format: date-time
        amount:
          type: number
        segment_id:
          type: string
          format: uuid
    CreditRolloverLedgerEntry:
      type: object
      required:
        - type
        - timestamp
        - amount
        - new_contract_id
        - segment_id
      properties:
        type:
          type: string
          enum:
            - CREDIT_ROLLOVER
        timestamp:
          type: string
          format: date-time
        amount:
          type: number
        segment_id:
          type: string
          format: uuid
        new_contract_id:
          type: string
          format: uuid
    CommitHierarchyChildAccessAll:
      type: object
      required:
        - type
      properties:
        type:
          type: string
          enum:
            - ALL
            - all
    CommitHierarchyChildAccessNone:
      type: object
      required:
        - type
      properties:
        type:
          type: string
          enum:
            - NONE
            - none
    CommitHierarchyChildAccessContractIds:
      type: object
      required:
        - type
        - contract_ids
      properties:
        type:
          type: string
          enum:
            - CONTRACT_IDS
            - contract_ids
        contract_ids:
          type: array
          minItems: 1
          items:
            type: string
            format: uuid
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
