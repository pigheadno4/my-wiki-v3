<!-- Source URL: https://docs.metronome.com/api-reference/contracts/get-a-contract-v2.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a contract (v2)

> Gets the details for a specific contract, including contract term, rate card information, credits and commits, and more. 

### Use this endpoint to: 
- Check the duration of a customer's current contract
- Get details on contract terms, including access schedule amounts for commitments and credits
- Understand the state of a contract at a past time. As you can evolve the terms of a contract over time through editing, use the `as_of_date` parameter to view the full contract configuration as of that point in time. 

### Usage guidelines: 
- Optionally, use the `include_balance` and `include_ledger` fields to include balances and ledgers in the credit and commit responses. Using these fields will cause the query to be slower.




## OpenAPI

````yaml /openapi.json post /v2/contracts/get
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
  /v2/contracts/get:
    post:
      tags:
        - Contracts
      summary: Get a contract (v2)
      description: >
        Gets the details for a specific contract, including contract term, rate
        card information, credits and commits, and more. 


        ### Use this endpoint to: 

        - Check the duration of a customer's current contract

        - Get details on contract terms, including access schedule amounts for
        commitments and credits

        - Understand the state of a contract at a past time. As you can evolve
        the terms of a contract over time through editing, use the `as_of_date`
        parameter to view the full contract configuration as of that point in
        time. 


        ### Usage guidelines: 

        - Optionally, use the `include_balance` and `include_ledger` fields to
        include balances and ledgers in the credit and commit responses. Using
        these fields will cause the query to be slower.
      operationId: getContract-v2
      requestBody:
        description: Contract and customer IDs
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
                contract_id:
                  type: string
                  format: uuid
                include_ledgers:
                  type: boolean
                  description: >-
                    Include commit/credit ledgers in the response. Setting this
                    flag may cause the query to be slower. Cannot be used with
                    as_of_date parameter.
                as_of_date:
                  type: string
                  format: date-time
                  description: >-
                    Optional RFC 3339 timestamp. Return the contract as of this
                    date. Cannot be used with include_ledgers parameter.
                include_balance:
                  type: boolean
                  description: >-
                    Include the balance of credits and commits in the response.
                    Setting this flag may cause the query to be slower.
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
              contract_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
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
                    $ref: '#/components/schemas/ContractV2'
              example:
                data:
                  id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                  customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
                  rate_card_id: 92f3080d-27ca-4306-a23f-2430de61851e
                  starting_at: '2020-01-01T00:00:00.000Z'
                  net_payment_terms_days: 7
                  ending_before: '2022-01-01T00:00:00.000Z'
                  commits:
                    - id: 62c0cb84-bf3f-48b9-9bcf-a8ddf8c1cf35
                      type: PREPAID
                      name: My test commit
                      description: My test commit description
                      product:
                        id: 2e30f074-d04c-412e-a134-851ebfa5ceb2
                        name: My product A
                      rollover_fraction: 0.1
                      applicable_product_ids:
                        - 13a2179b-f0cb-460b-85a1-cd42964ca533
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
                      created_at: '2020-01-01T00:00:00.000Z'
                  overrides:
                    - id: 6cf3292a-e85c-4be6-822c-e25ba9d19757
                      created_at: '2020-01-01T00:00:00.000Z'
                      product:
                        id: eae8903b-693b-41a7-8c0b-f23748c9a9c8
                        name: My product B
                      starting_at: '2020-01-01T00:00:00.000Z'
                      type: MULTIPLIER
                      multiplier: 0.1
                  scheduled_charges:
                    - id: 8e511ff1-3fd5-4d86-bc89-1e80239874bf
                      name: My test scheduled charge
                      product:
                        id: 2e30f074-d04c-412e-a134-851ebfa5ceb2
                        name: My product A
                      schedule:
                        schedule_items:
                          - id: 6ca40ebc-9c01-484e-a64e-4e47fbbd0ebe
                            invoice_id: 5cced82b-5464-41b4-9ea7-3e080e0a4dba
                            amount: 1000000
                            unit_price: 1000000
                            quantity: 1
                            timestamp: '2020-02-15T00:00:00.000Z'
                  scheduled_charges_on_usage_invoices: ALL
                  transitions:
                    - type: RENEWAL
                      from_contract_id: 9bf48856-b430-42f4-844f-4d2ea85bcff8
                      to_contract_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                  usage_statement_schedule:
                    frequency: MONTHLY
                    billing_anchor_date: '2020-01-01T00:00:00.000Z'
                  created_at: '2019-12-31T14:23:55.234Z'
                  created_by: Alice
                  custom_fields:
                    x_account_id: KyVnHhSBWl7eY2bl
                  usage_filter: []
        '400':
          description: Error
          content:
            application/json:
              schema:
                type: object
                required:
                  - code
                  - message
                properties:
                  code:
                    type: string
                    enum:
                      - CustomerNotFound
                      - ContractNotFound
                  message:
                    type: string
components:
  schemas:
    ContractV2:
      type: object
      required:
        - id
        - customer_id
        - starting_at
        - commits
        - overrides
        - scheduled_charges
        - transitions
        - created_at
        - created_by
        - usage_statement_schedule
        - usage_filter
      properties:
        id:
          type: string
          format: uuid
        customer_id:
          type: string
          format: uuid
        package_id:
          x-stainless-skip: true
          type: string
          format: uuid
          description: >-
            (BETA) ID of the package this contract was created from, if
            applicable.
        uniqueness_key:
          $ref: '#/components/schemas/UniquenessKey'
          description: Optional uniqueness key to prevent duplicate contract creations.
        name:
          type: string
        salesforce_opportunity_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          description: >-
            This field's availability is dependent on your client's
            configuration.
        rate_card_id:
          type: string
          format: uuid
        starting_at:
          type: string
          format: date-time
        commits:
          type: array
          items:
            $ref: '#/components/schemas/CommitV2'
        credits:
          type: array
          items:
            $ref: '#/components/schemas/CreditV2'
        has_more:
          $ref: '#/components/schemas/HasMore'
        overrides:
          type: array
          items:
            $ref: '#/components/schemas/OverrideV2'
        discounts:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: array
          description: >-
            This field's availability is dependent on your client's
            configuration.
          items:
            $ref: '#/components/schemas/Discount'
        professional_services:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: array
          description: >-
            This field's availability is dependent on your client's
            configuration.
          items:
            $ref: '#/components/schemas/ProService'
        scheduled_charges:
          type: array
          items:
            $ref: '#/components/schemas/ScheduledCharge'
        scheduled_charges_on_usage_invoices:
          $ref: '#/components/schemas/ScheduledChargesOnUsageInvoices'
        transitions:
          type: array
          items:
            $ref: '#/components/schemas/ContractTransition'
        reseller_royalties:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: array
          description: >-
            This field's availability is dependent on your client's
            configuration.
          items:
            type: object
            required:
              - reseller_type
              - segments
            properties:
              reseller_type:
                $ref: '#/components/schemas/ResellerType'
              segments:
                type: array
                items:
                  $ref: '#/components/schemas/ResellerRoyalty'
        created_at:
          type: string
          format: date-time
        created_by:
          type: string
        netsuite_sales_order_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          description: >-
            This field's availability is dependent on your client's
            configuration.
        net_payment_terms_days:
          type: number
        ending_before:
          type: string
          format: date-time
        archived_at:
          type: string
          format: date-time
        total_contract_value:
          type: number
        usage_filter:
          type: array
          items:
            $ref: '#/components/schemas/UsageFilterV2'
        usage_statement_schedule:
          $ref: '#/components/schemas/UsageStatementSchedule'
        multiplier_override_prioritization:
          type: string
          enum:
            - LOWEST_MULTIPLIER
            - lowest_multiplier
            - EXPLICIT
            - explicit
          description: >-
            Defaults to LOWEST_MULTIPLIER, which applies the greatest discount
            to list prices automatically. EXPLICIT prioritization requires
            specifying priorities for each multiplier; the one with the lowest
            priority value will be prioritized first.
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: contract
        customer_billing_provider_configuration:
          $ref: '#/components/schemas/CustomerBillingProviderConfiguration'
        billing_provider_configuration_schedule:
          x-mint:
            groups:
              - ff:billing-provider-schedule-api
          type: array
          description: >-
            The schedule of billing provider configuration changes on the
            contract, ordered by effective_at ascending.
          items:
            type: object
            required:
              - billing_provider_configuration
              - effective_at
            properties:
              billing_provider_configuration:
                $ref: '#/components/schemas/CustomerBillingProviderConfiguration'
              effective_at:
                type: string
                format: date-time
                description: >-
                  The date this billing provider configuration became or becomes
                  active.
              effective_until:
                type: string
                format: date-time
                description: >-
                  The date this billing provider configuration is superseded by
                  the next entry. Null for the last entry in the schedule.
        revenue_system_configuration_schedule:
          x-mint:
            groups:
              - ff:billing-provider-schedule-api
          type: array
          description: >-
            The schedule of revenue system configuration changes on the
            contract, ordered by effective_at ascending.
          items:
            type: object
            required:
              - revenue_system_configuration
              - effective_at
            properties:
              revenue_system_configuration:
                $ref: '#/components/schemas/CustomerRevenueSystemConfigurationV2'
              effective_at:
                type: string
                format: date-time
                description: >-
                  The date this revenue system configuration became or becomes
                  active.
              effective_until:
                type: string
                format: date-time
                description: >-
                  The date this revenue system configuration is superseded by
                  the next entry. Null for the last entry in the schedule.
        recurring_commits:
          type: array
          items:
            $ref: '#/components/schemas/RecurringCommitV2'
        recurring_credits:
          type: array
          items:
            $ref: '#/components/schemas/RecurringCreditV2'
        spend_threshold_configuration:
          $ref: '#/components/schemas/SpendThresholdConfigurationV2'
        prepaid_balance_threshold_configuration:
          $ref: '#/components/schemas/PrepaidBalanceThresholdConfigurationV2'
        spend_trackers:
          x-mint:
            groups:
              - ff:tb-spend-trackers
          type: array
          items:
            $ref: '#/components/schemas/SpendTracker'
          description: Spend trackers attached to this contract.
        subscriptions:
          $ref: '#/components/schemas/SubscriptionsV2'
        hierarchy_configuration:
          $ref: '#/components/schemas/HierarchyConfigurationV2'
        priority:
          x-mint:
            groups:
              - ff:account-hierarchy-priority-enabled
          type: number
          description: Priority of the contract.
    UniquenessKey:
      type: string
      minLength: 1
      maxLength: 128
      description: >-
        Prevents the creation of duplicates. If a request to create a record is
        made with a previously used uniqueness key, a new record will not be
        created and the request will fail with a 409 error.
    CommitV2:
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
        applicable_contract_ids:
          type: array
          items:
            type: string
            format: uuid
        specifiers:
          type: array
          description: >-
            List of filters that determine what kind of customer usage draws
            down a commit or credit. A customer's usage needs to meet the
            condition of at least one of the specifiers to contribute to a
            commit's or credit's drawdown.
          items:
            $ref: '#/components/schemas/CommitSpecifier'
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
            $ref: '#/components/schemas/CommitLedgerV2'
          description: >-
            A list of ordered events that impact the balance of a commit. For
            example, an invoice deduction or a rollover.
        balance:
          $ref: '#/components/schemas/BalanceForCommitsAndCredits'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: commit
        archived_at:
          type: string
          format: date-time
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
        recurring_commit_id:
          type: string
          format: uuid
          description: The ID of the recurring commit that created this commit
        subscription_config:
          $ref: '#/components/schemas/RecurringCommitSubscriptionConfig'
          description: Attach a subscription to the recurring commit/credit.
    CreditV2:
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
            $ref: '#/components/schemas/CreditLedgerV2'
          description: >-
            A list of ordered events that impact the balance of a credit. For
            example, an invoice deduction or an expiration.
        balance:
          $ref: '#/components/schemas/BalanceForCommitsAndCredits'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: contract_credit
        archived_at:
          type: string
          format: date-time
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
        created_at:
          type: string
          format: date-time
          description: >
            Timestamp of when the credit was created.

            - Recurring credits: latter of credit service period date and parent
            credit start date
        created_by:
          type: string
          description: >-
            The actor who created this credit. Omitted for system-generated
            credits such as recurring credits.
        recurring_credit_id:
          type: string
          format: uuid
          description: The ID of the recurring credit that created this credit
        subscription_config:
          $ref: '#/components/schemas/RecurringCommitSubscriptionConfig'
          description: Attach a subscription to the recurring commit/credit.
    HasMore:
      type: object
      description: >-
        Indicates whether there are more items than the limit for this endpoint.
        Use the respective list endpoints to get the full lists.
      required:
        - commits
        - credits
      properties:
        commits:
          type: boolean
          description: >-
            Whether there are more commits on this contract than the limit for
            this endpoint. Use the /contracts/customerCommits/list endpoint to
            get the full list of commits.
        credits:
          type: boolean
          description: >-
            Whether there are more credits on this contract than the limit for
            this endpoint. Use the /contracts/customerCredits/list endpoint to
            get the full list of credits.
    OverrideV2:
      type: object
      required:
        - id
        - created_at
        - starting_at
      properties:
        id:
          type: string
          format: uuid
        created_at:
          type: string
          format: date-time
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
        applicable_product_tags:
          type: array
          items:
            type: string
        override_specifiers:
          type: array
          items:
            $ref: '#/components/schemas/OverrideSpecifierV2'
        starting_at:
          type: string
          format: date-time
        ending_before:
          type: string
          format: date-time
        entitled:
          type: boolean
        type:
          type: string
          enum:
            - OVERWRITE
            - MULTIPLIER
            - TIERED
        priority:
          type: number
        multiplier:
          type: number
        overwrite_rate:
          $ref: '#/components/schemas/OverwriteRateV2'
        override_tiers:
          type: array
          items:
            $ref: '#/components/schemas/OverrideTier'
        is_commit_specific:
          type: boolean
        target:
          type: string
          enum:
            - COMMIT_RATE
            - LIST_RATE
    Discount:
      type: object
      required:
        - id
        - product
        - schedule
      properties:
        id:
          type: string
          format: uuid
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
        schedule:
          $ref: '#/components/schemas/SchedulePointInTime'
        name:
          type: string
          minLength: 1
        netsuite_sales_order_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          description: >-
            This field's availability is dependent on your client's
            configuration.
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: discount
    ProService:
      type: object
      required:
        - id
        - product_id
        - unit_price
        - quantity
        - max_amount
      properties:
        id:
          type: string
          format: uuid
        description:
          type: string
        product_id:
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
        unit_price:
          type: number
          description: >-
            Unit price for the charge. Will be multiplied by quantity to
            determine the amount and must be specified.
        quantity:
          type: number
          description: >-
            Quantity for the charge. Will be multiplied by unit_price to
            determine the amount.
        max_amount:
          type: number
          description: Maximum amount for the term.
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: professional_service
    ScheduledCharge:
      type: object
      required:
        - id
        - product
        - schedule
      properties:
        id:
          type: string
          format: uuid
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
        schedule:
          $ref: '#/components/schemas/SchedulePointInTime'
        name:
          type: string
          minLength: 1
          description: displayed on invoices
        netsuite_sales_order_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          description: >-
            This field's availability is dependent on your client's
            configuration.
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: scheduled_charge
        archived_at:
          type: string
          format: date-time
    ScheduledChargesOnUsageInvoices:
      type: string
      description: >-
        Determines which scheduled and commit charges to consolidate onto the
        Contract's usage invoice. The charge's `timestamp` must match the usage
        invoice's `ending_before` date for consolidation to occur. This field
        cannot be modified after a Contract has been created. If this field is
        omitted, charges will appear on a separate invoice from usage charges.
      enum:
        - ALL
    ContractTransition:
      type: object
      required:
        - type
        - from_contract_id
        - to_contract_id
      properties:
        type:
          type: string
          enum:
            - RENEWAL
        from_contract_id:
          type: string
          format: uuid
        to_contract_id:
          type: string
          format: uuid
    ResellerType:
      type: string
      enum:
        - AWS
        - AWS_PRO_SERVICE
        - GCP
        - GCP_PRO_SERVICE
    ResellerRoyalty:
      type: object
      required:
        - reseller_type
        - starting_at
        - fraction
        - netsuite_reseller_id
      properties:
        reseller_type:
          $ref: '#/components/schemas/ResellerType'
        fraction:
          type: number
        applicable_product_tags:
          type: array
          items:
            type: string
        applicable_product_ids:
          type: array
          items:
            type: string
        netsuite_reseller_id:
          type: string
        starting_at:
          type: string
          format: date-time
        ending_before:
          type: string
          format: date-time
        reseller_contract_value:
          type: number
        aws_account_number:
          type: string
        aws_payer_reference_id:
          type: string
        aws_offer_id:
          type: string
        gcp_account_id:
          type: string
        gcp_offer_id:
          type: string
    UsageFilterV2:
      type: object
      required:
        - group_key
        - group_values
        - starting_at
      properties:
        group_key:
          type: string
        group_values:
          type: array
          items:
            type: string
        starting_at:
          description: >-
            This will match contract starting_at value if usage filter is active
            from the beginning of the contract.
          type: string
          format: date-time
        ending_before:
          description: >-
            This will match contract ending_before value if usage filter is
            active until the end of the contract. It will be undefined if the
            contract is open-ended.
          type: string
          format: date-time
    UsageStatementSchedule:
      type: object
      required:
        - frequency
        - billing_anchor_date
      properties:
        frequency:
          type: string
          enum:
            - MONTHLY
            - monthly
            - QUARTERLY
            - quarterly
            - ANNUAL
            - annual
            - WEEKLY
            - weekly
        billing_anchor_date:
          type: string
          format: date-time
          description: >-
            Contract usage statements follow a selected cadence based on this
            date.
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
    CustomerBillingProviderConfiguration:
      type: object
      required:
        - id
        - billing_provider
        - customer_id
        - configuration
        - delivery_method_id
        - delivery_method
        - delivery_method_configuration
        - archived_at
      properties:
        id:
          type: string
          format: uuid
          description: >-
            ID of this configuration; can be provided as the
            billing_provider_configuration_id when creating a contract.
        billing_provider:
          $ref: '#/components/schemas/BillingProviderType'
          description: The billing provider set for this configuration.
        customer_id:
          type: string
          format: uuid
        configuration:
          type: object
          additionalProperties: true
          description: >-
            Configuration for the billing provider. The structure of this object
            is specific to the billing provider.
        delivery_method_id:
          type: string
          format: uuid
          description: ID of the delivery method to use for this customer.
        delivery_method:
          $ref: '#/components/schemas/BillingProviderDeliveryMethodType'
          description: The method to use for delivering invoices to this customer.
        delivery_method_configuration:
          type: object
          additionalProperties: true
          description: >-
            Configuration for the delivery method. The structure of this object
            is specific to the delivery method.
        archived_at:
          type: string
          format: date-time
          nullable: true
    CustomerRevenueSystemConfigurationV2:
      type: object
      required:
        - id
        - customer_id
        - delivery_method_id
        - provider
        - configuration
      properties:
        id:
          type: string
          format: uuid
          description: ID of the revenue system configuration.
        customer_id:
          type: string
          format: uuid
        delivery_method_id:
          type: string
          format: uuid
          description: ID of the delivery method used for this customer configuration.
        provider:
          $ref: '#/components/schemas/RevenueSystemProviderTypeV2'
          description: The revenue system provider (e.g. netsuite).
        configuration:
          type: object
          additionalProperties: true
          description: >-
            Configuration for the revenue system. The structure of this object
            is specific to the provider.
        delivery_method:
          $ref: '#/components/schemas/BillingProviderDeliveryMethodType'
          description: The method to use for delivering data to the revenue system.
        delivery_method_configuration:
          type: object
          additionalProperties: true
          description: >-
            Configuration for the delivery method. The structure of this object
            is specific to the delivery method.
        archived_at:
          type: string
          format: date-time
          nullable: true
    RecurringCommitV2:
      allOf:
        - $ref: '#/components/schemas/RecurringCommitOrCreditBaseV2'
        - type: object
          properties:
            invoice_amount:
              type: object
              required:
                - unit_price
                - quantity
                - credit_type_id
              properties:
                unit_price:
                  type: number
                quantity:
                  type: number
                credit_type_id:
                  type: string
                  format: uuid
              description: >-
                The amount the customer should be billed for the commit. Not
                required.
            proration_rounding:
              type: object
              nullable: true
              description: Rounding configuration for prorated recurring commit amounts.
              properties:
                access:
                  $ref: '#/components/schemas/ProrationRoundingConfigV2'
                invoice:
                  $ref: '#/components/schemas/ProrationRoundingConfigV2'
    RecurringCreditV2:
      allOf:
        - $ref: '#/components/schemas/RecurringCommitOrCreditBaseV2'
        - type: object
          properties:
            proration_rounding:
              type: object
              nullable: true
              description: Rounding configuration for prorated recurring credit amounts.
              properties:
                access:
                  $ref: '#/components/schemas/ProrationRoundingConfigV2'
    SpendThresholdConfigurationV2:
      type: object
      required:
        - is_enabled
        - threshold_amount
        - commit
        - payment_gate_config
      properties:
        is_enabled:
          type: boolean
          description: >-
            When set to false, the contract will not be evaluated against the
            threshold_amount. Toggling to true will result an immediate
            evaluation, regardless of prior state.
        threshold_amount:
          description: >-
            Specify the threshold amount for the contract. Each time the
            contract's usage hits this amount, a threshold charge will be
            initiated.
          type: number
        commit:
          $ref: '#/components/schemas/SpendThresholdCommit'
        payment_gate_config:
          $ref: '#/components/schemas/PaymentGateConfigV2'
        discount_configuration:
          $ref: '#/components/schemas/DiscountConfiguration'
          x-mint:
            groups:
              - ff:threshold-billing-discounts
    PrepaidBalanceThresholdConfigurationV2:
      type: object
      required:
        - is_enabled
        - threshold_amount
        - recharge_to_amount
        - commit
        - payment_gate_config
      properties:
        is_enabled:
          type: boolean
          description: >-
            When set to false, the contract will not be evaluated against the
            threshold_amount. Toggling to true will result an immediate
            evaluation, regardless of prior state.
        threshold_amount:
          description: >-
            Specify the threshold amount for the contract. Each time the
            contract's balance lowers to this amount, a threshold charge will be
            initiated.
          type: number
        recharge_to_amount:
          description: Specify the amount the balance should be recharged to.
          type: number
        custom_credit_type_id:
          description: >-
            If provided, the threshold, recharge-to amount, and the resulting
            threshold commit amount will be in terms of this credit type instead
            of the fiat currency.
          type: string
          format: uuid
        commit:
          $ref: '#/components/schemas/PrepaidBalanceThresholdCommitV2'
        payment_gate_config:
          $ref: '#/components/schemas/PaymentGateConfigV2'
        discount_configuration:
          $ref: '#/components/schemas/DiscountConfiguration'
          x-mint:
            groups:
              - ff:threshold-billing-discounts
        threshold_balance_specifiers:
          type: array
          description: >-
            Determines which balances are excluded from remaining balance
            calculation for threshold billing.
          items:
            $ref: '#/components/schemas/ThresholdBalanceSpecifierV2'
    SpendTracker:
      type: object
      required:
        - alias
        - credit_type_id
        - reset_frequency
        - applicable_spend_specifiers
      properties:
        alias:
          type: string
          description: Human-readable identifier, unique per contract.
        credit_type_id:
          type: string
          format: uuid
        reset_frequency:
          type: string
          enum:
            - BILLING_PERIOD
        applicable_spend_specifiers:
          type: array
          items:
            $ref: '#/components/schemas/SpendTrackerApplicableSpendSpecifier'
        accumulated_spend:
          $ref: '#/components/schemas/SpendTrackerAccumulatedSpend'
    SubscriptionsV2:
      type: array
      description: List of subscriptions on the contract.
      items:
        $ref: '#/components/schemas/SubscriptionV2'
    HierarchyConfigurationV2:
      oneOf:
        - $ref: '#/components/schemas/ParentHierarchyConfiguration'
        - $ref: '#/components/schemas/ChildHierarchyConfigurationV2'
      description: >
        Either a **parent** configuration with a list of children or a **child**
        configuration with a single parent.
    ScheduleDuration:
      type: object
      required:
        - schedule_items
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
    CommitLedgerV2:
      oneOf:
        - $ref: '#/components/schemas/PrepaidCommitSegmentStartLedgerEntry'
        - $ref: >-
            #/components/schemas/PrepaidCommitAutomatedInvoiceDeductionLedgerEntry
        - $ref: '#/components/schemas/PrepaidCommitRolloverLedgerEntry'
        - $ref: '#/components/schemas/PrepaidCommitExpirationLedgerEntry'
        - $ref: '#/components/schemas/PrepaidCommitCanceledLedgerEntry'
        - $ref: '#/components/schemas/PrepaidCommitCreditedLedgerEntry'
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
    RecurringCommitSubscriptionConfig:
      type: object
      required:
        - allocation
        - apply_seat_increase_config
        - subscription_id
      properties:
        allocation:
          $ref: '#/components/schemas/SubscriptionConfigAllocation'
        apply_seat_increase_config:
          $ref: '#/components/schemas/ApplySeatIncreaseConfigForRecurringCommit'
        subscription_id:
          type: string
          format: uuid
    CreditLedgerV2:
      oneOf:
        - $ref: '#/components/schemas/CreditSegmentStartLedgerEntry'
        - $ref: '#/components/schemas/CreditAutomatedInvoiceDeductionLedgerEntry'
        - $ref: '#/components/schemas/CreditExpirationLedgerEntry'
        - $ref: '#/components/schemas/CreditCanceledLedgerEntry'
        - $ref: '#/components/schemas/CreditCreditedLedgerEntry'
        - $ref: '#/components/schemas/CreditManualLedgerEntry'
        - $ref: '#/components/schemas/CreditSeatBasedAdjustmentLedgerEntry'
        - $ref: '#/components/schemas/CreditRolloverLedgerEntry'
    OverrideSpecifierV2:
      type: object
      properties:
        commit_ids:
          type: array
          items:
            type: string
        recurring_commit_ids:
          type: array
          items:
            type: string
        any_commit_or_credit_ids:
          type: array
          items:
            type: string
        product_id:
          type: string
          format: uuid
        product_tags:
          type: array
          items:
            type: string
        pricing_group_values:
          type: object
          additionalProperties:
            type: string
        presentation_group_values:
          type: object
          additionalProperties:
            type: string
            nullable: true
        billing_frequency:
          type: string
          enum:
            - MONTHLY
            - QUARTERLY
            - ANNUAL
            - WEEKLY
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
    OverwriteRateV2:
      type: object
      required:
        - rate_type
      properties:
        rate_type:
          type: string
          enum:
            - FLAT
            - flat
            - PERCENTAGE
            - percentage
            - SUBSCRIPTION
            - subscription
            - TIERED
            - tiered
            - TIERED_PERCENTAGE
            - tiered_percentage
            - CUSTOM
            - custom
          x-mint-enum:
            CUSTOM:
              - client_id:5b9e3072-415b-4842-94f0-0b6700c8b6be
              - client_id:179e395f-5349-4fe2-bf12-64ab4e5bc560
              - client_id:f157d376-0781-4ef3-9db9-775a9052148e
              - client_id:7dd2f652-7629-4925-9069-77f5c5d3db37
              - client_id:c0ce3dc0-6d3e-4f6b-aadf-dfb90f2bf9f5
              - client_id:cf874b25-ca3b-460b-b6fe-5f33b3c2ea33
              - client_id:97c07a0c-70db-448a-a1d4-adcd2b8bd1c7
            custom:
              - client_id:5b9e3072-415b-4842-94f0-0b6700c8b6be
              - client_id:179e395f-5349-4fe2-bf12-64ab4e5bc560
              - client_id:f157d376-0781-4ef3-9db9-775a9052148e
              - client_id:7dd2f652-7629-4925-9069-77f5c5d3db37
              - client_id:c0ce3dc0-6d3e-4f6b-aadf-dfb90f2bf9f5
              - client_id:cf874b25-ca3b-460b-b6fe-5f33b3c2ea33
              - client_id:97c07a0c-70db-448a-a1d4-adcd2b8bd1c7
            TIERED_PERCENTAGE:
              - ff:support-charge-ga
            tiered_percentage:
              - ff:support-charge-ga
        price:
          type: number
          description: >-
            Default price. For FLAT rate_type, this must be >=0. For PERCENTAGE
            rate_type, this is a decimal fraction, e.g. use 0.1 for 10%; this
            must be >=0 and <=1.
        quantity:
          type: number
          description: Default quantity. For SUBSCRIPTION rate_type, this must be >=0.
        is_prorated:
          type: boolean
          description: >-
            Default proration configuration. Only valid for SUBSCRIPTION
            rate_type. Must be set to true.
        tiers:
          type: array
          items:
            $ref: '#/components/schemas/Tier'
          description: Only set for TIERED rate_type.
        minimum_config:
          $ref: '#/components/schemas/MinimumConfig'
          x-stainless-skip: true
          x-mint:
            groups:
              - ff:support-charge-ga
        custom_rate:
          x-mint:
            groups:
              - client_id:5b9e3072-415b-4842-94f0-0b6700c8b6be
              - client_id:179e395f-5349-4fe2-bf12-64ab4e5bc560
              - client_id:f157d376-0781-4ef3-9db9-775a9052148e
              - client_id:7dd2f652-7629-4925-9069-77f5c5d3db37
              - client_id:c0ce3dc0-6d3e-4f6b-aadf-dfb90f2bf9f5
              - client_id:cf874b25-ca3b-460b-b6fe-5f33b3c2ea33
              - client_id:97c07a0c-70db-448a-a1d4-adcd2b8bd1c7
          type: object
          additionalProperties: true
          description: >-
            Only set for CUSTOM rate_type. This field is interpreted by custom
            rate processors.
        credit_type:
          $ref: '#/components/schemas/CreditType'
    OverrideTier:
      type: object
      required:
        - multiplier
      properties:
        size:
          type: number
        multiplier:
          type: number
    BillingProviderType:
      type: string
      enum:
        - aws_marketplace
        - stripe
        - netsuite
        - custom
        - azure_marketplace
        - quickbooks_online
        - workday
        - gcp_marketplace
        - metronome
      x-mint-enum:
        netsuite:
          - client_id:11db091c-975b-4908-9f67-b1ceb126acdf
        custom:
          - client_id:11db091c-975b-4908-9f67-b1ceb126acdf
        workday:
          - client_id:11db091c-975b-4908-9f67-b1ceb126acdf
        gcp_marketplace:
          - client_id:11db091c-975b-4908-9f67-b1ceb126acdf
    BillingProviderDeliveryMethodType:
      type: string
      enum:
        - direct_to_billing_provider
        - aws_sqs
        - tackle
        - aws_sns
    RevenueSystemProviderTypeV2:
      type: string
      enum:
        - netsuite
      description: The revenue system provider type.
    RecurringCommitOrCreditBaseV2:
      type: object
      required:
        - id
        - product
        - access_amount
        - priority
        - commit_duration
        - starting_at
        - rate_type
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
        name:
          type: string
          description: >-
            Displayed on invoices. Will be passed through to the individual
            commits
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
        access_amount:
          type: object
          required:
            - unit_price
            - credit_type_id
          properties:
            unit_price:
              type: number
            quantity:
              type: number
            credit_type_id:
              type: string
              format: uuid
          description: The amount of commit to grant.
        description:
          type: string
          description: Will be passed down to the individual commits
        rollover_fraction:
          type: number
          description: >-
            Will be passed down to the individual commits. This controls how
            much of an individual unexpired commit will roll over upon contract
            transition. Must be between 0 and 1.
        priority:
          type: number
          description: Will be passed down to the individual commits
        applicable_product_ids:
          type: array
          items:
            type: string
            format: uuid
          description: Will be passed down to the individual commits
        applicable_product_tags:
          type: array
          items:
            type: string
          description: Will be passed down to the individual commits
        specifiers:
          type: array
          description: >-
            List of filters that determine what kind of customer usage draws
            down a commit or credit. A customer's usage needs to meet the
            condition of at least one of the specifiers to contribute to a
            commit's or credit's drawdown.
          items:
            $ref: '#/components/schemas/CommitSpecifier'
        netsuite_sales_order_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          description: Will be passed down to the individual commits
        rate_type:
          type: string
          enum:
            - COMMIT_RATE
            - commit_rate
            - LIST_RATE
            - list_rate
          description: Whether the created commits will use the commit rate or list rate
        starting_at:
          type: string
          format: date-time
          description: Determines the start time for the first commit
        ending_before:
          type: string
          format: date-time
          description: >-
            Determines when the contract will stop creating recurring commits.
            Optional
        commit_duration:
          type: object
          required:
            - value
          properties:
            value:
              type: number
            unit:
              type: string
              enum:
                - periods
                - PERIODS
          description: The amount of time the created commits will be valid for
        recurrence_frequency:
          type: string
          enum:
            - MONTHLY
            - monthly
            - QUARTERLY
            - quarterly
            - ANNUAL
            - annual
            - WEEKLY
            - weekly
            - DAILY
            - daily
          description: >-
            The frequency at which the recurring commits will be created. If not
            provided: - The commits will be created on the usage invoice
            frequency. If provided: - The period defined in the duration will
            correspond to this frequency. - Commits will be created aligned with
            the recurring commit's starting_at rather than the usage invoice
            dates. - Daily recurring commits have a limit of one per contract,
            and are unable to be created with seat-based subscriptions
        proration:
          type: string
          enum:
            - NONE
            - none
            - FIRST
            - first
            - LAST
            - last
            - FIRST_AND_LAST
            - first_and_last
          description: >-
            Determines whether the first and last commit will be prorated. If
            not provided, the default is FIRST_AND_LAST (i.e. prorate both the
            first and last commits).
        hierarchy_configuration:
          $ref: '#/components/schemas/CommitHierarchyConfiguration'
          description: Optional configuration for recurring credit hierarchy access control
        subscription_config:
          $ref: '#/components/schemas/RecurringCommitSubscriptionConfig'
          description: Attach a subscription to the recurring commit/credit.
    ProrationRoundingConfigV2:
      type: object
      required:
        - rounding_method
        - decimal_places
      properties:
        rounding_method:
          type: string
          enum:
            - HALF_UP
            - FLOOR
            - CEILING
            - half_up
            - floor
            - ceiling
        decimal_places:
          type: number
          minimum: -5
          maximum: 5
          description: >-
            Number of decimal places to round to. Applied directly to the stored
            monetary representation. Negative values round to powers of 10
            (e.g., -2 rounds to nearest 100 in the stored unit).
    SpendThresholdCommit:
      type: object
      allOf:
        - $ref: '#/components/schemas/BaseThresholdCommit'
    PaymentGateConfigV2:
      type: object
      required:
        - payment_gate_type
      properties:
        payment_gate_type:
          type: string
          enum:
            - NONE
            - STRIPE
            - EXTERNAL
          description: >-
            Gate access to the commit balance based on successful collection of
            payment. Select STRIPE for Metronome to facilitate payment via
            Stripe. Select EXTERNAL to facilitate payment using your own payment
            integration. Select NONE if you do not wish to payment gate the
            commit balance.
        tax_type:
          type: string
          enum:
            - NONE
            - STRIPE
            - ANROK
            - PRECALCULATED
          description: >-
            Stripe tax is only supported for Stripe payment gateway. Select NONE
            if you do not wish  Metronome to calculate tax on your behalf.
            Leaving this field blank will default to NONE.
        stripe_config:
          description: Only applicable if using STRIPE as your payment gateway type.
          type: object
          required:
            - payment_type
          properties:
            payment_type:
              type: string
              enum:
                - INVOICE
                - PAYMENT_INTENT
              description: If left blank, will default to INVOICE
            invoice_metadata:
              type: object
              additionalProperties:
                type: string
              description: >-
                Metadata to be added to the Stripe invoice. Only applicable if
                using INVOICE as your payment type.
        precalculated_tax_config:
          description: Only applicable if using PRECALCULATED as your tax type.
          type: object
          required:
            - tax_amount
          properties:
            tax_amount:
              type: number
              description: >-
                Amount of tax to be applied. This should be in the same currency
                and denomination  as the commit's invoice schedule
            tax_name:
              type: string
              description: >-
                Name of the tax to be applied. This may be used in an invoice
                line item description.
    DiscountConfiguration:
      type: object
      required:
        - payment_fraction
      properties:
        payment_fraction:
          type: number
          description: >-
            The fraction of the original amount that the customer pays after
            applying the discount. For example, 0.85 means the customer pays 85%
            of the original amount (a 15% discount).
        cap:
          x-mint:
            groups:
              - ff:threshold-billing-discounts
          allOf:
            - $ref: '#/components/schemas/PrepaidBalanceDiscountCap'
          description: >-
            If provided, the discount stops applying once the spend tracker has
            accumulated this much spend in the billing period.
    PrepaidBalanceThresholdCommitV2:
      type: object
      allOf:
        - $ref: '#/components/schemas/BaseThresholdCommit'
        - $ref: '#/components/schemas/OptionalThresholdCommitFields'
    ThresholdBalanceSpecifierV2:
      type: object
      required:
        - exclude
      properties:
        exclude:
          type: array
          items:
            $ref: '#/components/schemas/ExcludeThresholdBalanceSpecifierV2'
    SpendTrackerApplicableSpendSpecifier:
      type: object
      required:
        - spend_type
        - sources
      properties:
        spend_type:
          type: string
          enum:
            - COMMIT_PURCHASE
        sources:
          type: array
          items:
            type: string
            enum:
              - THRESHOLD_RECHARGE
              - MANUAL
        discounted:
          type: string
          enum:
            - ANY
            - DISCOUNTED_ONLY
            - UNDISCOUNTED_ONLY
    SpendTrackerAccumulatedSpend:
      type: object
      required:
        - amount
        - period_starting_at
        - period_ending_before
      properties:
        amount:
          type: number
        period_starting_at:
          type: string
          format: date-time
        period_ending_before:
          type: string
          format: date-time
    SubscriptionV2:
      required:
        - subscription_rate
        - collection_schedule
        - proration
        - quantity_schedule
        - starting_at
        - quantity_management_mode
        - billing_periods
      type: object
      properties:
        id:
          type: string
          format: uuid
        subscription_rate:
          $ref: '#/components/schemas/SubscriptionRate'
        name:
          type: string
        description:
          type: string
        collection_schedule:
          type: string
          enum:
            - ADVANCE
            - ARREARS
            - advance
            - arrears
        proration:
          $ref: '#/components/schemas/SubscriptionProrationV2'
        quantity_schedule:
          type: array
          description: >-
            List of quantity schedule items for the subscription. Only includes
            the current quantity and future quantity changes.
          items:
            $ref: '#/components/schemas/SubscriptionQuantitySchedule'
        billing_periods:
          $ref: '#/components/schemas/SubscriptionBillingPeriods'
        quantity_management_mode:
          type: string
          enum:
            - SEAT_BASED
            - seat_based
            - QUANTITY_ONLY
            - quantity_only
          description: >-
            Determines how the subscription's quantity is controlled. Defaults
            to QUANTITY_ONLY. **QUANTITY_ONLY**: The subscription quantity is
            specified directly on the subscription. `initial_quantity` must be
            provided with this option. Compatible with recurring commits/credits
            that use POOLED allocation. **SEAT_BASED**: Use when you want to
            pass specific seat identifiers (e.g. add user_123) to increment and
            decrement a subscription quantity, rather than directly providing
            the quantity. You must use a **SEAT_BASED** subscription to use a
            linked recurring credit with an allocation per seat. `seat_config`
            must be provided with this option.
        seat_config:
          $ref: '#/components/schemas/SubscriptionSeatConfig'
        starting_at:
          type: string
          format: date-time
        ending_before:
          type: string
          format: date-time
        fiat_credit_type_id:
          type: string
          format: uuid
        billing_cycle_config:
          $ref: '#/components/schemas/SubscriptionBillingCycleConfig'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: subscription
    ParentHierarchyConfiguration:
      type: object
      required:
        - children
      properties:
        children:
          type: array
          items:
            $ref: '#/components/schemas/HierarchyLink'
          description: List of contracts that belong to this parent.
        parent_behavior:
          type: object
          properties:
            invoice_consolidation_type:
              type: string
              enum:
                - CONCATENATE
                - NONE
              description: >-
                Indicates the desired behavior of consolidated invoices
                generated by the parent in a customer hierarchy


                **CONCATENATE**: Statements on the invoices of child customers
                will be appended to the consolidated invoice


                **NONE**: Do not generate consolidated invoices
    ChildHierarchyConfigurationV2:
      type: object
      required:
        - parent
      properties:
        parent:
          $ref: '#/components/schemas/HierarchyLink'
          description: The single parent contract/customer for this child.
        payer:
          type: string
          enum:
            - SELF
            - PARENT
          description: >-
            Indicates which customer should pay for the child's invoice charges
            **SELF**: The child pays for its own invoice charges **PARENT**: The
            parent pays for the child's invoice charges
        usage_statement_behavior:
          type: string
          enum:
            - CONSOLIDATE
            - SEPARATE
          description: >-
            Indicates the behavior of the child's invoice statements on the
            parent's invoices.


            **CONSOLIDATE**: Child's invoice statements will be added to
            parent's consolidated invoices


            **SEPARATE**: Child's invoice statements will appear not appear on
            parent's consolidated invoices
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
    Tier:
      type: object
      required:
        - price
      properties:
        size:
          type: number
        price:
          type: number
    MinimumConfig:
      type: object
      description: >-
        Only set for TIERED_PERCENTAGE or PERCENTAGE rate_type. Any
        commit-specific overrides will not apply if there is a minimum set on
        the rate/applied override.
      required:
        - minimum
      properties:
        minimum:
          type: number
    BaseThresholdCommit:
      type: object
      required:
        - product_id
      properties:
        product_id:
          type: string
          description: >-
            The commit product that will be used to generate the line item for
            commit payment.
        name:
          type: string
          description: >-
            Specify the name of the line item for the threshold charge. If left
            blank, it will default to the commit product name.
        description:
          type: string
        priority:
          type: number
          description: >-
            The priority of the commit, used to determine drawdown order. Lower
            priority commits are consumed first. Defaults to 100 if not
            specified.
    PrepaidBalanceDiscountCap:
      type: object
      required:
        - spend_tracker_alias
        - amount
      properties:
        spend_tracker_alias:
          type: string
          description: Alias of the spend tracker this cap is measured against.
        amount:
          type: number
          description: Accumulated spend ceiling above which the discount stops applying.
    OptionalThresholdCommitFields:
      type: object
      properties:
        applicable_product_ids:
          type: array
          items:
            type: string
            format: uuid
          description: >-
            Which products the threshold commit applies to. If
            applicable_product_ids, applicable_product_tags or specifiers are
            not provided, the commit applies to all products.
        applicable_product_tags:
          type: array
          items:
            type: string
          description: >-
            Which tags the threshold commit applies to. If
            applicable_product_ids, applicable_product_tags or specifiers are
            not provided, the commit applies to all products.
        specifiers:
          x-mint:
            groups:
              - ff:commit-specifiers
          type: array
          description: >-
            List of filters that determine what kind of customer usage draws
            down a commit or credit. A customer's usage needs to meet the
            condition of at least one of the specifiers to contribute to a
            commit's or credit's drawdown. This field cannot be used together
            with `applicable_product_ids` or `applicable_product_tags`. Instead,
            to target usage by product or product tag, pass those values in the
            body of `specifiers`.
          items:
            $ref: '#/components/schemas/CommitSpecifierInput'
    ExcludeThresholdBalanceSpecifierV2:
      type: object
      required:
        - custom_field_filters
      properties:
        custom_field_filters:
          type: array
          items:
            $ref: '#/components/schemas/BalanceCustomFieldFilterType'
    SubscriptionRate:
      type: object
      required:
        - billing_frequency
        - product
      properties:
        billing_frequency:
          type: string
          enum:
            - MONTHLY
            - QUARTERLY
            - ANNUAL
            - WEEKLY
            - monthly
            - quarterly
            - annual
            - weekly
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
    SubscriptionProrationV2:
      type: object
      required:
        - is_prorated
        - invoice_behavior
      properties:
        is_prorated:
          type: boolean
        invoice_behavior:
          type: string
          enum:
            - BILL_IMMEDIATELY
            - BILL_ON_NEXT_COLLECTION_DATE
            - bill_immediately
            - bill_on_next_collection_date
        rounding:
          $ref: '#/components/schemas/ProrationRoundingConfigV2'
    SubscriptionQuantitySchedule:
      type: object
      required:
        - quantity
        - starting_at
      properties:
        quantity:
          type: number
        starting_at:
          type: string
          format: date-time
        ending_before:
          type: string
          format: date-time
    SubscriptionBillingPeriods:
      type: object
      description: Previous, current, and next billing periods for the subscription.
      properties:
        previous:
          $ref: '#/components/schemas/SubscriptionBillingPeriod'
        current:
          $ref: '#/components/schemas/SubscriptionBillingPeriod'
        next:
          $ref: '#/components/schemas/SubscriptionBillingPeriod'
    SubscriptionSeatConfig:
      type: object
      required:
        - seat_group_key
      properties:
        seat_group_key:
          type: string
          description: >-
            The property name, sent on usage events, that identifies the seat ID
            associated with the usage event.  For example, the property name
            might be seat_id or user_id. The property must be set as a group key
            on billable metrics and a presentation/pricing group key on contract
            products.  This allows linked recurring credits with an allocation
            per seat to be consumed by only one seat's usage.
    SubscriptionBillingCycleConfig:
      type: object
      required:
        - anchor_date
        - invoice_placement
      properties:
        anchor_date:
          type: string
          format: date-time
          description: The date this subscription's billing cycle is anchored to.
        invoice_placement:
          type: string
          enum:
            - ON_SCHEDULED_INVOICE
            - ON_USAGE_INVOICE
          description: >-
            Controls whether this subscription consolidates onto usage invoices
            or gets its own scheduled invoice.
    HierarchyLink:
      type: object
      required:
        - contract_id
        - customer_id
      properties:
        contract_id:
          type: string
          format: uuid
        customer_id:
          type: string
          format: uuid
    CommitSpecifierInput:
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
          description: >-
            If provided, the specifier will apply to product usage with these
            set of pricing group values.
        presentation_group_values:
          type: object
          additionalProperties:
            type: string
          description: >-
            If provided, the specifier will apply to product usage with these
            set of presentation group values.
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
    BalanceCustomFieldFilterType:
      type: object
      required:
        - entity
        - key
        - value
      properties:
        entity:
          type: string
          enum:
            - Commit
            - ContractCredit
            - ContractCreditOrCommit
          x-mint-enum:
            ContractCreditOrCommit:
              - ff:alert-specifiers-enabled
        key:
          type: string
        value:
          type: string
    SubscriptionBillingPeriod:
      type: object
      required:
        - starting_at
        - ending_before
      properties:
        starting_at:
          type: string
          format: date-time
        ending_before:
          type: string
          format: date-time
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
