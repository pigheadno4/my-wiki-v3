<!-- Source URL: https://docs.metronome.com/api-reference/credits-and-commits/list-balances.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List balances

> Retrieve a comprehensive view of all available balances (commits and credits) for a customer. This endpoint provides real-time visibility into prepaid funds, postpaid commitments, promotional credits, and other balance types that can offset usage charges, helping you build transparent billing experiences.

### Use this endpoint to:
- Display current available balances in customer dashboards
- Verify available funds before approving high-usage operations
- Generate balance reports for finance teams
- Filter balances by contract or date ranges

### Key response fields:
An array of balance objects (all credits and commits) containing:

- Balance details: Current available amount for each commit or credit
- Metadata: Product associations, priorities, applicable date ranges
- Optional ledger entries: Detailed transaction history (if `include_ledgers=true`)
- Balance calculations: Including pending transactions and future-dated entries
- Custom fields: Any additional metadata attached to balances

### Usage guidelines:
- Use the [getNetBalance](https://docs.metronome.com/api-reference/credits-and-commits/get-the-net-balance-of-a-customer) endpoint to retrieve a single combined current balance
- Date filtering: Use `effective_before` to include only balances with access before a specific date (exclusive)
- Set `include_balance=true` for calculated balance amounts on each commit or credit
- Set `include_ledgers=true` for full transaction history
- Set `include_contract_balances = true` to see contract level balances
- Balance logic: Reflects currently accessible amounts, excluding expired/future segments
- Manual adjustments: Includes all manual ledger entries, even future-dated ones




## OpenAPI

````yaml /openapi.json post /v1/contracts/customerBalances/list
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
  /v1/contracts/customerBalances/list:
    post:
      tags:
        - Credits and commits
      summary: List balances
      description: >
        Retrieve a comprehensive view of all available balances (commits and
        credits) for a customer. This endpoint provides real-time visibility
        into prepaid funds, postpaid commitments, promotional credits, and other
        balance types that can offset usage charges, helping you build
        transparent billing experiences.


        ### Use this endpoint to:

        - Display current available balances in customer dashboards

        - Verify available funds before approving high-usage operations

        - Generate balance reports for finance teams

        - Filter balances by contract or date ranges


        ### Key response fields:

        An array of balance objects (all credits and commits) containing:


        - Balance details: Current available amount for each commit or credit

        - Metadata: Product associations, priorities, applicable date ranges

        - Optional ledger entries: Detailed transaction history (if
        `include_ledgers=true`)

        - Balance calculations: Including pending transactions and future-dated
        entries

        - Custom fields: Any additional metadata attached to balances


        ### Usage guidelines:

        - Use the
        [getNetBalance](https://docs.metronome.com/api-reference/credits-and-commits/get-the-net-balance-of-a-customer)
        endpoint to retrieve a single combined current balance

        - Date filtering: Use `effective_before` to include only balances with
        access before a specific date (exclusive)

        - Set `include_balance=true` for calculated balance amounts on each
        commit or credit

        - Set `include_ledgers=true` for full transaction history

        - Set `include_contract_balances = true` to see contract level balances

        - Balance logic: Reflects currently accessible amounts, excluding
        expired/future segments

        - Manual adjustments: Includes all manual ledger entries, even
        future-dated ones
      operationId: listCustomerBalances-v1
      requestBody:
        description: List all balances (commits and credits) for a customer
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
                id:
                  type: string
                  format: uuid
                access_type:
                  x-mint:
                    groups:
                      - ff:create-quantity-based-commits
                  x-stainless-skip: true
                  type: string
                  enum:
                    - SPEND
                    - spend
                    - QUANTITY
                    - quantity
                  description: >-
                    Filters balances by how they are drawn down. `SPEND` deducts
                    the dollar cost of usage. `QUANTITY` deducts the number of
                    units used.
                covering_date:
                  description: >-
                    Return only balances that have access schedules that "cover"
                    the provided date
                  type: string
                  format: date-time
                starting_at:
                  description: >-
                    Include only balances that have any access on or after the
                    provided date
                  type: string
                  format: date-time
                effective_before:
                  description: >-
                    Include only balances that have any access before the
                    provided date (exclusive)
                  type: string
                  format: date-time
                include_contract_balances:
                  type: boolean
                  description: Include balances on the contract level.
                include_archived:
                  type: boolean
                  description: >-
                    Include archived credits and credits from archived
                    contracts.
                include_ledgers:
                  type: boolean
                  description: >-
                    Include ledgers in the response. Setting this flag may cause
                    the query to be slower.
                include_balance:
                  type: boolean
                  description: >-
                    Include the balance of credits and commits in the response.
                    Setting this flag may cause the query to be slower.
                next_page:
                  type: string
                  description: The next page token from a previous response.
                limit:
                  type: integer
                  minimum: 1
                  maximum: 25
                  default: 25
                  description: The maximum number of commits to return. Defaults to 25.
                exclude_zero_balances:
                  x-mint:
                    groups:
                      - ff:allow-exclude-zero-balances
                  type: boolean
                  description: Exclude balances with zero amounts from the response.
                webhook_notification_id:
                  x-mint:
                    groups:
                      - ff:api-allow-webhook-notification-id
                  x-stainless-skip: true
                  type: string
                  description: >-
                    Indicates that this API request was triggered by a webhook
                    notification with the provided ID.
            example:
              customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
              id: 6162d87b-e5db-4a33-b7f2-76ce6ead4e85
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
                      oneOf:
                        - $ref: '#/components/schemas/Commit'
                        - $ref: '#/components/schemas/Credit'
                  next_page:
                    type: string
                    nullable: true
              example:
                data:
                  - id: 62c0cb84-bf3f-48b9-9bcf-a8ddf8c1cf35
                    type: PREPAID
                    rate_type: LIST_RATE
                    name: My test commit
                    description: My test commit description
                    priority: 100
                    product:
                      id: 2e30f074-d04c-412e-a134-851ebfa5ceb2
                      name: My product A
                    rollover_fraction: 0.1
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
                    invoice_schedule:
                      credit_type:
                        id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                        name: USD (cents)
                      schedule_items:
                        - id: f15e4e23-f74e-4de4-9b3a-8b07434116c4
                          invoice_id: 525b9759-7bbd-4a05-aab1-d7c43c976b57
                          amount: 10000000
                          unit_price: 10000000
                          quantity: 1
                          timestamp: '2020-03-01T00:00:00.000Z'
                      do_not_invoice: false
                    invoice_contract:
                      id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                    ledger:
                      - invoice_id: 525b9759-7bbd-4a05-aab1-d7c43c976b57
                        amount: 10000000
                        timestamp: '2020-03-01T00:00:00.000Z'
                        type: PREPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION
                        segment_id: 2d45952c-5a6e-43a9-8aab-f61ee21be81a
                    uniqueness_key: 946g9bepi1-uniqueness-key
                    created_at: '2020-01-01T00:00:00.000Z'
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
    Commit:
      type: object
      required:
        - id
        - type
        - product
        - created_at
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
            - PREPAID
            - POSTPAID
        rate_type:
          type: string
          enum:
            - COMMIT_RATE
            - LIST_RATE
        name:
          type: string
        priority:
          type: number
          description: >-
            If multiple credits or commits are applicable, the one with the
            lower priority will apply first.
        cost_basis:
          x-mint:
            groups:
              - ff:commit-cost-basis
          type: number
          description: >-
            The ratio of the amount paid for the commit to the amount of credit
            granted.
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
          description: >-
            The schedule that the customer will gain access to the credits
            purposed with this commit.
        invoice_schedule:
          $ref: '#/components/schemas/SchedulePointInTime'
          description: The schedule that the customer will be invoiced for this commit.
        invoice_contract:
          type: object
          required:
            - id
          properties:
            id:
              type: string
              format: uuid
          description: The contract that this commit will be billed on.
        recurring_commit_id:
          type: string
          format: uuid
          description: >-
            The ID of the recurring commit that this commit was generated from,
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
            The subscription configuration for this commit, if it was generated
            from a recurring commit with a subscription attached.
        rolled_over_from:
          type: object
          required:
            - contract_id
            - commit_id
          properties:
            commit_id:
              type: string
              format: uuid
            contract_id:
              type: string
              format: uuid
        description:
          type: string
        rollover_fraction:
          type: number
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
        amount:
          type: number
          description: (DEPRECATED) Use access_schedule + invoice_schedule instead.
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
            $ref: '#/components/schemas/CommitLedger'
          description: >-
            A list of ordered events that impact the balance of a commit. For
            example, an invoice deduction or a rollover.
        balance:
          $ref: '#/components/schemas/BalanceForCommitsAndCredits'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: commit
        uniqueness_key:
          $ref: '#/components/schemas/UniquenessKeyForCommitsAndCredits'
        archived_at:
          type: string
          format: date-time
          description: >-
            RFC 3339 timestamp indicating when the commit was archived. If not
            provided, the commit is not archived.
        hierarchy_configuration:
          $ref: '#/components/schemas/CommitHierarchyConfiguration'
          description: Optional configuration for commit hierarchy access control
        spend_tracker_attributes:
          $ref: '#/components/schemas/SpendTrackerAttributes'
          x-mint:
            groups:
              - ff:tb-spend-trackers
          description: >-
            Optional attributes controlling how this commit interacts with spend
            trackers.
        created_at:
          type: string
          format: date-time
          description: >
            Timestamp of when the commit was created.

            - Recurring commits: latter of commit service period date and parent
            commit start date

            - Rollover commits: when the new contract started
        created_by:
          type: string
          description: >-
            The actor who created this commit. Omitted for system-generated
            commits such as recurring commits, rollover commits, and threshold
            commits.
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
    SchedulePointInTime:
      type: object
      properties:
        credit_type:
          $ref: '#/components/schemas/CreditType'
        schedule_items:
          type: array
          items:
            type: object
            required:
              - id
              - amount
              - unit_price
              - quantity
              - timestamp
            properties:
              id:
                type: string
                format: uuid
              invoice_id:
                type: string
                format: uuid
                nullable: true
              amount:
                type: number
              unit_price:
                type: number
              quantity:
                type: number
              timestamp:
                type: string
                format: date-time
        do_not_invoice:
          type: boolean
          description: >-
            This field is only applicable to commit invoice schedules. If true,
            this schedule will not generate an invoice.
          default: false
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
    CommitLedger:
      oneOf:
        - $ref: '#/components/schemas/PrepaidCommitSegmentStartLedgerEntry'
        - $ref: >-
            #/components/schemas/PrepaidCommitAutomatedInvoiceDeductionLedgerEntry
        - $ref: '#/components/schemas/PrepaidCommitRolloverLedgerEntry'
        - $ref: '#/components/schemas/PrepaidCommitExpirationLedgerEntry'
        - $ref: '#/components/schemas/PrepaidCommitCanceledLedgerEntry'
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
        - $ref: '#/components/schemas/PrepaidCommitCreditedLedgerEntry'
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
        - $ref: '#/components/schemas/PrepaidCommitSeatBasedAdjustmentLedgerEntry'
        - $ref: '#/components/schemas/PostpaidCommitInitialBalanceLedgerEntry'
        - $ref: >-
            #/components/schemas/PostpaidCommitAutomatedInvoiceDeductionLedgerEntry
        - $ref: '#/components/schemas/PostpaidCommitRolloverLedgerEntry'
        - $ref: '#/components/schemas/PostpaidCommitTrueupLedgerEntry'
        - $ref: '#/components/schemas/PrepaidCommitManualLedgerEntry'
        - $ref: '#/components/schemas/PostpaidCommitManualLedgerEntry'
        - $ref: '#/components/schemas/PostpaidCommitExpirationLedgerEntry'
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
    SpendTrackerAttributes:
      type: object
      required:
        - counts_as_discounted
      properties:
        counts_as_discounted:
          type: boolean
          description: >-
            If true, this commit is included in spend trackers with discounted
            set to DISCOUNTED_ONLY
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
    PrepaidCommitSegmentStartLedgerEntry:
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
            - PREPAID_COMMIT_SEGMENT_START
        timestamp:
          type: string
          format: date-time
        amount:
          type: number
        segment_id:
          type: string
          format: uuid
    PrepaidCommitAutomatedInvoiceDeductionLedgerEntry:
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
            - PREPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION
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
    PrepaidCommitRolloverLedgerEntry:
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
            - PREPAID_COMMIT_ROLLOVER
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
    PrepaidCommitExpirationLedgerEntry:
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
            - PREPAID_COMMIT_EXPIRATION
        timestamp:
          type: string
          format: date-time
        amount:
          type: number
        segment_id:
          type: string
          format: uuid
    PrepaidCommitCanceledLedgerEntry:
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
            - PREPAID_COMMIT_CANCELED
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
    PrepaidCommitCreditedLedgerEntry:
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
            - PREPAID_COMMIT_CREDITED
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
    PrepaidCommitSeatBasedAdjustmentLedgerEntry:
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
            - PREPAID_COMMIT_SEAT_BASED_ADJUSTMENT
        timestamp:
          type: string
          format: date-time
        amount:
          type: number
        segment_id:
          type: string
          format: uuid
    PostpaidCommitInitialBalanceLedgerEntry:
      type: object
      required:
        - type
        - timestamp
        - amount
      properties:
        type:
          type: string
          enum:
            - POSTPAID_COMMIT_INITIAL_BALANCE
        timestamp:
          type: string
          format: date-time
        amount:
          type: number
    PostpaidCommitAutomatedInvoiceDeductionLedgerEntry:
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
            - POSTPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION
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
    PostpaidCommitRolloverLedgerEntry:
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
            - POSTPAID_COMMIT_ROLLOVER
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
    PostpaidCommitTrueupLedgerEntry:
      type: object
      required:
        - type
        - timestamp
        - amount
        - invoice_id
      properties:
        type:
          type: string
          enum:
            - POSTPAID_COMMIT_TRUEUP
        timestamp:
          type: string
          format: date-time
        amount:
          type: number
        invoice_id:
          type: string
          format: uuid
        contract_id:
          x-mint:
            groups:
              - client_id:11db091c-975b-4908-9f67-b1ceb126acdf
          type: string
          format: uuid
    PrepaidCommitManualLedgerEntry:
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
            - PREPAID_COMMIT_MANUAL
        timestamp:
          type: string
          format: date-time
        amount:
          type: number
        reason:
          type: string
    PostpaidCommitManualLedgerEntry:
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
            - POSTPAID_COMMIT_MANUAL
        timestamp:
          type: string
          format: date-time
        amount:
          type: number
        reason:
          type: string
    PostpaidCommitExpirationLedgerEntry:
      type: object
      required:
        - type
        - timestamp
        - amount
      properties:
        type:
          type: string
          enum:
            - POSTPAID_COMMIT_EXPIRATION
        timestamp:
          type: string
          format: date-time
        amount:
          type: number
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
