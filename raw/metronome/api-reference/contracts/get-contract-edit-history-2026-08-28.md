<!-- Source URL: https://docs.metronome.com/api-reference/contracts/get-contract-edit-history.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get contract edit history

> List all the edits made to a contract over time. In Metronome, you can edit a contract at any point after it's created to fix mistakes or reflect changes in terms. Metronome stores a full history of all edits that were ever made to a contract, whether through the UI, `editContract` endpoint, or other endpoints like `updateContractEndDate`. 

### Use this endpoint to: 
- Understand what changes were made to a contract, when, and by who

### Key response fields: 
- An array of every edit ever made to the contract
- Details on each individual edit - for example showing that in one edit, a user added two discounts and incremented a subscription quantity.




## OpenAPI

````yaml /openapi.json post /v2/contracts/getEditHistory
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
  /v2/contracts/getEditHistory:
    post:
      tags:
        - Contracts
      summary: Get contract edit history
      description: >
        List all the edits made to a contract over time. In Metronome, you can
        edit a contract at any point after it's created to fix mistakes or
        reflect changes in terms. Metronome stores a full history of all edits
        that were ever made to a contract, whether through the UI,
        `editContract` endpoint, or other endpoints like
        `updateContractEndDate`. 


        ### Use this endpoint to: 

        - Understand what changes were made to a contract, when, and by who


        ### Key response fields: 

        - An array of every edit ever made to the contract

        - Details on each individual edit - for example showing that in one
        edit, a user added two discounts and incremented a subscription
        quantity.
      operationId: getContractEditHistory-v2
      requestBody:
        description: Contract ID
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
                    type: array
                    items:
                      $ref: '#/components/schemas/ContractEdit'
              example:
                data:
                  - id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                    add_commits:
                      - id: addda517-6d7a-42ea-834c-f5e6cf8c670e
                        type: PREPAID
                        product:
                          id: 2e30f074-d04c-412e-a134-851ebfa5ceb2
                          name: My product A
                        description: A new commit
                        applicable_product_tags:
                          - tag1
                          - tag2
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
                  - id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                    add_overrides:
                      - id: 6cf3292a-e85c-4be6-822c-e25ba9d19757
                        created_at: '2020-01-01T00:00:00.000Z'
                        starting_at: '2020-01-01T00:00:00.000Z'
                        type: MULTIPLIER
                        multiplier: 1.5
                        priority: 1
                        override_specifiers:
                          - product_tags:
                              - tag1
                            pricing_group_values:
                              region: us-west-1
                              hardware_type: gpu
                        entitled: true
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
                      - ContractNotFound
                      - CustomerNotFound
                  message:
                    type: string
components:
  schemas:
    ContractEdit:
      type: object
      required:
        - id
      properties:
        id:
          type: string
          format: uuid
        timestamp:
          type: string
          format: date-time
        uniqueness_key:
          $ref: '#/components/schemas/UniquenessKey'
        add_overrides:
          type: array
          items:
            $ref: '#/components/schemas/OverrideV2'
        add_pro_services:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: array
          items:
            $ref: '#/components/schemas/ProService'
        add_reseller_royalties:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: array
          items:
            $ref: '#/components/schemas/ResellerRoyaltyOrUpdateV2'
        add_discounts:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: array
          items:
            $ref: '#/components/schemas/Discount'
        add_scheduled_charges:
          type: array
          items:
            $ref: '#/components/schemas/ScheduledChargeAdd'
        add_commits:
          type: array
          items:
            $ref: '#/components/schemas/CommitAdd'
        add_credits:
          type: array
          items:
            $ref: '#/components/schemas/CreditAdd'
        add_recurring_commits:
          type: array
          items:
            $ref: '#/components/schemas/RecurringCommitV2'
        add_recurring_credits:
          type: array
          items:
            $ref: '#/components/schemas/RecurringCreditV2'
        add_usage_filters:
          type: array
          items:
            $ref: '#/components/schemas/UsageFilterV2'
        add_subscriptions:
          $ref: '#/components/schemas/SubscriptionsV2'
        add_prepaid_balance_threshold_configuration:
          $ref: '#/components/schemas/PrepaidBalanceThresholdConfigurationV2'
        add_spend_threshold_configuration:
          $ref: '#/components/schemas/SpendThresholdConfigurationV2'
        update_contract_name:
          type: string
          nullable: true
          description: >-
            Value to update the contract name to. If not provided, the contract
            name will remain unchanged.
        update_discounts:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: array
          items:
            $ref: '#/components/schemas/DiscountUpdate'
        update_scheduled_charges:
          type: array
          items:
            $ref: '#/components/schemas/ScheduledChargeUpdate'
        update_commits:
          type: array
          items:
            $ref: '#/components/schemas/CommitUpdate'
        update_credits:
          type: array
          items:
            $ref: '#/components/schemas/CreditUpdate'
        update_recurring_commits:
          type: array
          items:
            $ref: '#/components/schemas/RecurringCommitUpdate'
        update_recurring_credits:
          type: array
          items:
            $ref: '#/components/schemas/RecurringCreditUpdate'
        update_contract_end_date:
          type: string
          format: date-time
        update_refund_invoices:
          type: array
          items:
            $ref: '#/components/schemas/RefundInvoiceUpdate'
        update_subscriptions:
          type: array
          description: Optional list of subscriptions to update.
          items:
            $ref: '#/components/schemas/SubscriptionsUpdate'
        update_prepaid_balance_threshold_configuration:
          $ref: '#/components/schemas/UpdatePrepaidBalanceThresholdConfiguration'
        update_spend_threshold_configuration:
          $ref: '#/components/schemas/UpdateSpendThresholdConfiguration'
        archive_commits:
          type: array
          items:
            required:
              - id
            type: object
            properties:
              id:
                type: string
                format: uuid
        archive_credits:
          type: array
          items:
            required:
              - id
            type: object
            properties:
              id:
                type: string
                format: uuid
        archive_scheduled_charges:
          type: array
          items:
            required:
              - id
            type: object
            properties:
              id:
                type: string
                format: uuid
        remove_overrides:
          type: array
          items:
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
    ResellerRoyaltyOrUpdateV2:
      type: object
      required:
        - reseller_type
      properties:
        reseller_type:
          $ref: '#/components/schemas/ResellerType'
        fraction:
          type: number
        netsuite_reseller_id:
          type: string
        starting_at:
          type: string
          format: date-time
        ending_before:
          type: string
          format: date-time
          nullable: true
        applicable_product_tags:
          type: array
          items:
            type: string
        applicable_product_ids:
          type: array
          items:
            type: string
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
    ScheduledChargeAdd:
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
    CommitAdd:
      type: object
      required:
        - id
        - type
        - product
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
          $ref: '#/components/schemas/CommitAddInvoiceSchedule'
          description: The schedule that the customer will be invoiced for this commit.
        description:
          type: string
        rollover_fraction:
          type: number
        applicable_product_ids:
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
            commit's or credit's drawdown. This field cannot be used together
            with `applicable_product_ids` or `applicable_product_tags`. Instead,
            to target usage by product or product tag, pass those values in the
            body of `specifiers`.
          items:
            $ref: '#/components/schemas/CommitSpecifierInput'
        applicable_product_tags:
          type: array
          items:
            type: string
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
        hierarchy_configuration:
          $ref: '#/components/schemas/CommitHierarchyConfiguration'
          description: Optional configuration for commit hierarchy access control
    CreditAdd:
      type: object
      required:
        - id
        - type
        - product
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
        rollover_fraction:
          type: number
        rate_type:
          type: string
          enum:
            - COMMIT_RATE
            - LIST_RATE
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
            commit's or credit's drawdown. This field cannot be used together
            with `applicable_product_ids` or `applicable_product_tags`. Instead,
            to target usage by product or product tag, pass those values in the
            body of `specifiers`.
          items:
            $ref: '#/components/schemas/CommitSpecifierInput'
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
        hierarchy_configuration:
          $ref: '#/components/schemas/CommitHierarchyConfiguration'
          description: Optional configuration for recurring credit hierarchy access control
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
    SubscriptionsV2:
      type: array
      description: List of subscriptions on the contract.
      items:
        $ref: '#/components/schemas/SubscriptionV2'
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
    DiscountUpdate:
      type: object
      required:
        - id
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        netsuite_sales_order_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
        schedule:
          $ref: '#/components/schemas/SchedulePointInTimeInputV2'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: discount
    ScheduledChargeUpdate:
      type: object
      required:
        - id
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        netsuite_sales_order_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          nullable: true
        invoice_schedule:
          $ref: '#/components/schemas/InvoiceScheduleUpdate'
    CommitUpdate:
      type: object
      required:
        - id
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        description:
          type: string
        access_schedule:
          $ref: '#/components/schemas/AccessScheduleUpdate'
        netsuite_sales_order_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          nullable: true
        rollover_fraction:
          type: number
          nullable: true
        invoice_schedule:
          $ref: '#/components/schemas/InvoiceScheduleUpdate'
        applicable_product_ids:
          type: array
          nullable: true
          items:
            type: string
            format: uuid
          description: >-
            Which products the commit applies to. If applicable_product_ids,
            applicable_product_tags or specifiers are not provided, the commit
            applies to all products.
        specifiers:
          nullable: true
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
        applicable_product_tags:
          type: array
          nullable: true
          items:
            type: string
          description: >-
            Which tags the commit applies to. If applicable_product_ids,
            applicable_product_tags or specifiers are not provided, the commit
            applies to all products.
        product_id:
          type: string
          format: uuid
        hierarchy_configuration:
          $ref: '#/components/schemas/CommitHierarchyConfiguration'
          description: Optional configuration for commit hierarchy access control
        priority:
          type: number
          nullable: true
          description: >-
            If multiple commits are applicable, the one with the lower priority
            will apply first.
        rate_type:
          type: string
          enum:
            - COMMIT_RATE
            - LIST_RATE
          description: If set, the commit's rate type was updated to the specified value.
    CreditUpdate:
      type: object
      required:
        - id
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        description:
          type: string
        access_schedule:
          $ref: '#/components/schemas/AccessScheduleUpdate'
        netsuite_sales_order_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          nullable: true
        rollover_fraction:
          type: number
          nullable: true
        applicable_product_ids:
          type: array
          nullable: true
          items:
            type: string
            format: uuid
          description: >-
            Which products the credit applies to. If applicable_product_ids,
            applicable_product_tags or specifiers are not provided, the credit
            applies to all products.
        specifiers:
          nullable: true
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
        applicable_product_tags:
          type: array
          nullable: true
          items:
            type: string
          description: >-
            Which tags the credit applies to. If applicable_product_ids,
            applicable_product_tags or specifiers are not provided, the credit
            applies to all products.
        product_id:
          type: string
          format: uuid
        hierarchy_configuration:
          $ref: '#/components/schemas/CommitHierarchyConfiguration'
          description: Optional configuration for credit hierarchy access control
        priority:
          type: number
          nullable: true
          description: >-
            If multiple credits are applicable, the one with the lower priority
            will apply first.
        rate_type:
          type: string
          enum:
            - LIST_RATE
            - COMMIT_RATE
          description: If set, the credit's rate type was updated to the specified value.
    RecurringCommitUpdate:
      allOf:
        - $ref: '#/components/schemas/RecurringCommitOrCreditUpdateBase'
        - type: object
          properties:
            invoice_amount:
              type: object
              properties:
                unit_price:
                  type: number
                quantity:
                  type: number
            proration_rounding:
              type: object
              nullable: true
              description: Rounding configuration for prorated recurring commit amounts.
              properties:
                access:
                  $ref: '#/components/schemas/ProrationRoundingConfigV2'
                invoice:
                  $ref: '#/components/schemas/ProrationRoundingConfigV2'
    RecurringCreditUpdate:
      allOf:
        - $ref: '#/components/schemas/RecurringCommitOrCreditUpdateBase'
        - type: object
          properties:
            proration_rounding:
              type: object
              nullable: true
              description: Rounding configuration for prorated recurring credit amounts.
              properties:
                access:
                  $ref: '#/components/schemas/ProrationRoundingConfigV2'
    RefundInvoiceUpdate:
      type: object
      required:
        - invoice_id
        - date
      properties:
        invoice_id:
          type: string
          format: uuid
        date:
          type: string
          format: date-time
    SubscriptionsUpdate:
      type: object
      required:
        - id
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        ending_before:
          type: string
          format: date-time
        quantity_updates:
          type: array
          items:
            type: object
            required:
              - starting_at
            properties:
              quantity:
                type: number
              quantity_delta:
                type: number
              starting_at:
                type: string
                format: date-time
        seat_updates:
          $ref: '#/components/schemas/SubscriptionSeatUpdateInput'
          description: Manage subscription seats for subscriptions in SEAT_BASED mode.
    UpdatePrepaidBalanceThresholdConfiguration:
      type: object
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
          nullable: true
          description: >-
            If provided, the threshold, recharge-to amount, and the resulting
            threshold commit amount will be in terms of this credit type instead
            of the fiat currency.
          type: string
          format: uuid
        commit:
          $ref: '#/components/schemas/UpdatePrepaidBalanceThresholdCommit'
        payment_gate_config:
          $ref: '#/components/schemas/PaymentGateConfigV2'
        discount_configuration:
          x-mint:
            groups:
              - ff:threshold-billing-discounts
          nullable: true
          allOf:
            - $ref: '#/components/schemas/UpdateDiscountConfiguration'
        threshold_balance_specifiers:
          nullable: true
          type: array
          description: >-
            Determines which balances are excluded from remaining balance
            calculation for threshold billing.
          items:
            $ref: '#/components/schemas/ThresholdBalanceSpecifierV2'
    UpdateSpendThresholdConfiguration:
      type: object
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
          $ref: '#/components/schemas/UpdateSpendThresholdCommit'
        payment_gate_config:
          $ref: '#/components/schemas/PaymentGateConfigV2'
        discount_configuration:
          x-mint:
            groups:
              - ff:threshold-billing-discounts
          nullable: true
          allOf:
            - $ref: '#/components/schemas/UpdateDiscountConfiguration'
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
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
    ResellerType:
      type: string
      enum:
        - AWS
        - AWS_PRO_SERVICE
        - GCP
        - GCP_PRO_SERVICE
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
    CommitAddInvoiceSchedule:
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
          description: If true, this schedule will not generate an invoice.
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
        - anchor_date
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
        anchor_date:
          type: string
          format: date-time
          description: The date this recurring commit's billing periods are anchored to.
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
        product_custom_fields:
          $ref: '#/components/schemas/CustomField'
          description: >-
            Custom fields from the subscription product referenced by
            `subscription_rate.product`. These are distinct from the
            subscription instance's `custom_fields`.
    PrepaidBalanceThresholdCommitV2:
      type: object
      allOf:
        - $ref: '#/components/schemas/BaseThresholdCommit'
        - $ref: '#/components/schemas/OptionalThresholdCommitFields'
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
    ThresholdBalanceSpecifierV2:
      type: object
      required:
        - exclude
      properties:
        exclude:
          type: array
          items:
            $ref: '#/components/schemas/ExcludeThresholdBalanceSpecifierV2'
    SpendThresholdCommit:
      type: object
      allOf:
        - $ref: '#/components/schemas/BaseThresholdCommit'
    SchedulePointInTimeInputV2:
      type: object
      description: Must provide either schedule_items or recurring_schedule.
      properties:
        credit_type_id:
          type: string
          format: uuid
          description: Defaults to USD (cents) if not passed.
        schedule_items:
          type: array
          description: Either provide amount or provide both unit_price and quantity.
          items:
            type: object
            required:
              - timestamp
            properties:
              unit_price:
                type: number
                description: >-
                  Unit price for the charge. Will be multiplied by quantity to
                  determine the amount and must be specified with quantity. If
                  specified amount cannot be provided.
              quantity:
                type: number
                description: >-
                  Quantity for the charge. Will be multiplied by unit_price to
                  determine the amount and must be specified with unit_price. If
                  specified amount cannot be provided.
              amount:
                type: number
                description: >-
                  Amount for the charge. Can be provided instead of unit_price
                  and quantity. If amount is sent, the unit_price is assumed to
                  be the amount and quantity is inferred to be 1.
              timestamp:
                type: string
                format: date-time
                description: timestamp of the scheduled event
        recurring_schedule:
          type: object
          description: >-
            Enter the unit price and quantity for the charge or instead only
            send the amount. If amount is sent, the unit price is assumed to be
            the amount and quantity is inferred to be 1.
          required:
            - starting_at
            - ending_before
            - frequency
            - amount_distribution
          properties:
            starting_at:
              type: string
              format: date-time
              description: RFC 3339 timestamp (inclusive).
            ending_before:
              type: string
              format: date-time
              description: RFC 3339 timestamp (exclusive).
            frequency:
              $ref: '#/components/schemas/RecurringScheduleFrequencyV2'
            unit_price:
              type: number
              description: >-
                Unit price for the charge. Will be multiplied by quantity to
                determine the amount and must be specified with quantity. If
                specified amount cannot be provided.
            quantity:
              type: number
              description: >-
                Quantity for the charge. Will be multiplied by unit_price to
                determine the amount and must be specified with unit_price. If
                specified amount cannot be provided.
            amount:
              type: number
              description: >-
                Amount for the charge. Can be provided instead of unit_price and
                quantity. If amount is sent, the unit_price is assumed to be the
                amount and quantity is inferred to be 1.
            amount_distribution:
              type: string
              enum:
                - DIVIDED
                - divided
                - DIVIDED_ROUNDED
                - divided_rounded
                - EACH
                - each
        do_not_invoice:
          type: boolean
          description: >-
            This field is only applicable to commit invoice schedules. If true,
            this schedule will not generate an invoice.
          default: false
    InvoiceScheduleUpdate:
      type: object
      properties:
        add_schedule_items:
          type: array
          items:
            type: object
            required:
              - timestamp
            properties:
              timestamp:
                type: string
                format: date-time
              amount:
                type: number
              quantity:
                type: number
              unit_price:
                type: number
        update_schedule_items:
          type: array
          items:
            type: object
            required:
              - id
            properties:
              id:
                type: string
                format: uuid
              timestamp:
                type: string
                format: date-time
              amount:
                type: number
              quantity:
                type: number
              unit_price:
                type: number
        remove_schedule_items:
          type: array
          items:
            required:
              - id
            type: object
            properties:
              id:
                type: string
                format: uuid
    AccessScheduleUpdate:
      type: object
      properties:
        add_schedule_items:
          type: array
          items:
            type: object
            required:
              - amount
              - starting_at
              - ending_before
            properties:
              amount:
                type: number
              starting_at:
                type: string
                format: date-time
                description: RFC 3339 timestamp (inclusive)
              ending_before:
                type: string
                format: date-time
                description: RFC 3339 timestamp (exclusive)
        update_schedule_items:
          type: array
          items:
            type: object
            required:
              - id
            properties:
              id:
                type: string
                format: uuid
              amount:
                type: number
              starting_at:
                type: string
                format: date-time
                description: RFC 3339 timestamp (inclusive)
              ending_before:
                type: string
                format: date-time
                description: RFC 3339 timestamp (exclusive)
        remove_schedule_items:
          type: array
          items:
            required:
              - id
            type: object
            properties:
              id:
                type: string
                format: uuid
    RecurringCommitOrCreditUpdateBase:
      type: object
      required:
        - id
      properties:
        id:
          type: string
          format: uuid
        ending_before:
          type: string
          format: date-time
        access_amount:
          type: object
          properties:
            unit_price:
              type: number
            quantity:
              type: number
        rate_type:
          type: string
          enum:
            - LIST_RATE
            - list_rate
            - COMMIT_RATE
            - commit_rate
    SubscriptionSeatUpdateInput:
      type: object
      properties:
        add_seat_ids:
          type: array
          description: >-
            Adds seat IDs to the subscription.  If there are unassigned seats,
            the new seat IDs will fill these unassigned seats and not increase
            the total subscription quantity. Otherwise, if there are more new
            seat IDs than unassigned seats, the total subscription quantity will
            increase.
          items:
            $ref: '#/components/schemas/SubscriptionSeatUpdateAssignedSeat'
        remove_seat_ids:
          type: array
          description: >-
            Removes seat IDs from the subscription, if possible.  If a seat ID
            is removed, the total subscription quantity will decrease.
            Otherwise, if the seat ID is not found on the subscription, this is
            a no-op.
          items:
            $ref: '#/components/schemas/SubscriptionSeatUpdateAssignedSeat'
        add_unassigned_seats:
          type: array
          description: >-
            Adds unassigned seats to the subscription. This will increase the
            total subscription quantity.
          items:
            $ref: '#/components/schemas/SubscriptionSeatUpdateUnassignedSeat'
        remove_unassigned_seats:
          type: array
          description: >-
            Removes unassigned seats from the subscription. This will decrease
            the total subscription quantity if there are are unassigned seats.
          items:
            $ref: '#/components/schemas/SubscriptionSeatUpdateUnassignedSeat'
    UpdatePrepaidBalanceThresholdCommit:
      type: object
      allOf:
        - $ref: '#/components/schemas/UpdateBaseThresholdCommit'
        - $ref: '#/components/schemas/OptionalThresholdCommitFieldsUpdate'
    UpdateDiscountConfiguration:
      type: object
      properties:
        payment_fraction:
          type: number
          nullable: true
          description: >
            The fraction of the original amount that the customer pays after
            applying the discount. Set to null to remove the discount fraction.
            For example, 0.85 means the customer pays 85% of the original amount
            (a 15% discount).
        cap:
          x-mint:
            groups:
              - ff:threshold-billing-discounts
          nullable: true
          allOf:
            - $ref: '#/components/schemas/PrepaidBalanceDiscountCapInput'
          description: Update the discount cap. Set to null to remove an existing cap.
    UpdateSpendThresholdCommit:
      type: object
      allOf:
        - $ref: '#/components/schemas/UpdateBaseThresholdCommit'
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
        duration:
          $ref: '#/components/schemas/RelativeDate'
          description: >-
            The length of time the created commit will be valid, starting from
            the end of the invoice's service period. If not provided, defaults
            to one year.
        rollover_fraction:
          type: number
          description: >-
            Fraction of the created commit's unused balance that will roll over.
            Must be between 0 and 1.
        rate_type:
          type: string
          enum:
            - COMMIT_RATE
            - commit_rate
            - LIST_RATE
            - list_rate
          description: >-
            Whether the created commits will be charged at commit rate or list
            rate.
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
    ExcludeThresholdBalanceSpecifierV2:
      type: object
      required:
        - custom_field_filters
      properties:
        custom_field_filters:
          type: array
          items:
            $ref: '#/components/schemas/BalanceCustomFieldFilterType'
    RecurringScheduleFrequencyV2:
      type: string
      enum:
        - MONTHLY
        - monthly
        - QUARTERLY
        - quarterly
        - SEMI_ANNUAL
        - semi_annual
        - ANNUAL
        - annual
        - WEEKLY
        - weekly
    SubscriptionSeatUpdateAssignedSeat:
      type: object
      required:
        - seat_ids
        - starting_at
      properties:
        seat_ids:
          type: array
          items:
            type: string
        starting_at:
          type: string
          format: date-time
          description: Assigned seats will be added/removed starting at this date.
    SubscriptionSeatUpdateUnassignedSeat:
      type: object
      required:
        - quantity
        - starting_at
      properties:
        quantity:
          type: number
          minimum: 1
          description: >-
            The number of unassigned seats on the subscription will
            increase/decrease by this delta. Must be greater than 0.
        starting_at:
          type: string
          format: date-time
          description: Unassigned seats will be updated starting at this date.
    UpdateBaseThresholdCommit:
      type: object
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
          nullable: true
          description: >-
            The priority of the commit, used to determine drawdown order. Lower
            priority commits are consumed first. Defaults to 100 if not
            specified. On updates, set to null to clear a previously configured
            priority.
    OptionalThresholdCommitFieldsUpdate:
      type: object
      properties:
        applicable_product_ids:
          nullable: true
          type: array
          items:
            type: string
            format: uuid
          description: >-
            Which products the threshold commit applies to. If both
            applicable_product_ids and applicable_product_tags are not provided,
            the commit applies to all products.
        applicable_product_tags:
          nullable: true
          type: array
          items:
            type: string
          description: >-
            Which tags the threshold commit applies to. If both
            applicable_product_ids and applicable_product_tags are not provided,
            the commit applies to all products.
        specifiers:
          x-mint:
            groups:
              - ff:commit-specifiers
          nullable: true
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
        duration:
          nullable: true
          allOf:
            - $ref: '#/components/schemas/RelativeDate'
          description: >-
            The length of time the created commit will be valid, starting from
            the end of the invoice's service period. Set to null to clear a
            previously configured duration.
        rollover_fraction:
          type: number
          nullable: true
          description: >-
            Fraction of the created commit's unused balance that will roll over.
            Must be between 0 and 1. Set to null to clear a previously
            configured rollover fraction.
        rate_type:
          type: string
          nullable: true
          enum:
            - COMMIT_RATE
            - commit_rate
            - LIST_RATE
            - list_rate
          description: >-
            Whether the created commits will be charged at commit rate or list
            rate. Set to null to clear a previously configured rate type.
    PrepaidBalanceDiscountCapInput:
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
    RelativeDate:
      type: object
      required:
        - value
        - unit
      properties:
        value:
          type: integer
        unit:
          type: string
          enum:
            - DAYS
            - WEEKS
            - MONTHS
            - YEARS
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
