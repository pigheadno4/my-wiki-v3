<!-- Source URL: https://docs.metronome.com/api-reference/contracts/edit-a-contract.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Edit a contract

> The ability to edit a contract helps you react quickly to the needs of your customers and your business.

### Use this endpoint to:
- Encode mid-term commitment and discount changes
- Fix configuration mistakes and easily roll back packaging changes

### Key response fields:
- The `id` of the edit
- Complete edit details. For example, if you edited the contract to add new overrides and credits, you will receive the IDs of those overrides and credits in the response.

### Usage guidelines:
- When you edit a contract, any draft invoices update immediately to reflect that edit. Finalized invoices remain unchanged - you must void and regenerate them in the UI or API to reflect the edit.
- Contract editing must be enabled to use this endpoint. Contact us via the [Metronome support portal](https://support.metronome.com/) to learn more.




## OpenAPI

````yaml /openapi.json post /v2/contracts/edit
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
  /v2/contracts/edit:
    post:
      tags:
        - Contracts
      summary: Edit a contract
      description: >
        The ability to edit a contract helps you react quickly to the needs of
        your customers and your business.


        ### Use this endpoint to:

        - Encode mid-term commitment and discount changes

        - Fix configuration mistakes and easily roll back packaging changes


        ### Key response fields:

        - The `id` of the edit

        - Complete edit details. For example, if you edited the contract to add
        new overrides and credits, you will receive the IDs of those overrides
        and credits in the response.


        ### Usage guidelines:

        - When you edit a contract, any draft invoices update immediately to
        reflect that edit. Finalized invoices remain unchanged - you must void
        and regenerate them in the UI or API to reflect the edit.

        - Contract editing must be enabled to use this endpoint. Contact us via
        the [Metronome support portal](https://support.metronome.com/) to learn
        more.
      operationId: editContract-v2
      requestBody:
        description: Contract and customer IDs and fields to update
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EditContractPayload'
            example:
              customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
              contract_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
              add_overrides:
                - type: MULTIPLIER
                  starting_at: '2024-11-02T00:00:00Z'
                  product_id: d4fc086c-d8e5-4091-a235-fbba5da4ec14
                  multiplier: 2
                  priority: 100
              add_scheduled_charges:
                - product_id: 2e30f074-d04c-412e-a134-851ebfa5ceb2
                  schedule:
                    schedule_items:
                      - timestamp: '2020-02-15T00:00:00.000Z'
                        unit_price: 1000000
                        quantity: 1
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
                    type: object
                    required:
                      - id
                    properties:
                      id:
                        type: string
                        format: uuid
                      edit:
                        $ref: '#/components/schemas/ContractEdit'
              example:
                data:
                  id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
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
    EditContractPayload:
      type: object
      required:
        - customer_id
        - contract_id
      properties:
        customer_id:
          type: string
          format: uuid
          description: ID of the customer whose contract is being edited
        contract_id:
          type: string
          format: uuid
          description: ID of the contract being edited
        uniqueness_key:
          $ref: '#/components/schemas/UniquenessKey'
          description: Optional uniqueness key to prevent duplicate contract edits.
        add_commits:
          type: array
          items:
            $ref: '#/components/schemas/CommitInputV2'
        add_credits:
          type: array
          items:
            $ref: '#/components/schemas/CreditInputV2'
        add_recurring_commits:
          type: array
          items:
            $ref: '#/components/schemas/RecurringCommitInputV2'
        add_recurring_credits:
          type: array
          items:
            $ref: '#/components/schemas/RecurringCreditInputV2'
        add_discounts:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: array
          items:
            $ref: '#/components/schemas/DiscountInputV2'
        add_overrides:
          type: array
          items:
            $ref: '#/components/schemas/OverrideInputV2'
        add_scheduled_charges:
          type: array
          items:
            $ref: '#/components/schemas/ScheduledChargeInputV2'
        add_professional_services:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: array
          description: >-
            This field's availability is dependent on your client's
            configuration.
          items:
            $ref: '#/components/schemas/ProServiceInput'
        add_reseller_royalties:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: array
          items:
            $ref: '#/components/schemas/ResellerRoyaltyOrUpdateInput'
        add_subscriptions:
          $ref: '#/components/schemas/SubscriptionsInputV2'
        add_spend_threshold_configuration:
          $ref: '#/components/schemas/SpendThresholdConfigurationV2'
        add_prepaid_balance_threshold_configuration:
          $ref: '#/components/schemas/PrepaidBalanceThresholdConfigurationV2'
          type: object
        add_billing_provider_configuration_update:
          $ref: '#/components/schemas/BillingProviderConfigurationUpdate'
          type: object
          description: >-
            Update the billing provider configuration on the contract. Currently
            only supports adding a billing provider configuration to a contract
            that does not already have one.
        add_revenue_system_configuration_update:
          $ref: '#/components/schemas/RevenueSystemConfigurationUpdate'
          x-mint:
            groups:
              - ff:revenue-rec-configurations-enabled
          description: >-
            Update the revenue system configuration on the contract. Currently
            only supports adding a revenue system configuration to a contract
            that does not already have one.
        add_spend_trackers:
          x-mint:
            groups:
              - ff:tb-spend-trackers
          type: array
          items:
            $ref: '#/components/schemas/SpendTrackerInput'
          description: >-
            Spend trackers to add to this contract. Aliases must be unique
            within a contract.
        update_contract_name:
          type: string
          nullable: true
          description: >-
            Value to update the contract name to. If not provided, the contract
            name will remain unchanged.
        update_scheduled_charges:
          type: array
          items:
            $ref: '#/components/schemas/UpdateScheduledChargeInput'
        update_commits:
          type: array
          items:
            $ref: '#/components/schemas/UpdateCommitInput'
        update_credits:
          type: array
          items:
            $ref: '#/components/schemas/UpdateCreditInput'
        update_recurring_commits:
          type: array
          description: >-
            Edits to these recurring commits will only affect commits whose
            access schedules has not started. Expired commits, and commits with
            an active access schedule will remain unchanged.
          items:
            $ref: '#/components/schemas/UpdateRecurringCommitInput'
        update_recurring_credits:
          type: array
          description: >-
            Edits to these recurring credits will only affect credits whose
            access schedules has not started. Expired credits, and credits with
            an active access schedule will remain unchanged.
          items:
            $ref: '#/components/schemas/UpdateRecurringCreditInput'
        update_subscriptions:
          type: array
          description: Optional list of subscriptions to update.
          items:
            $ref: '#/components/schemas/UpdateSubscriptionInput'
        update_spend_threshold_configuration:
          $ref: '#/components/schemas/UpdateSpendThresholdConfiguration'
        update_prepaid_balance_threshold_configuration:
          $ref: '#/components/schemas/UpdatePrepaidBalanceThresholdConfiguration'
        update_contract_end_date:
          type: string
          format: date-time
          description: >-
            RFC 3339 timestamp indicating when the contract will end
            (exclusive).
          nullable: true
        update_net_payment_terms_days:
          type: number
          description: >-
            Number of days after issuance of invoice after which the invoice is
            due (e.g. Net 30).
          nullable: true
        allow_contract_ending_before_finalized_invoice:
          type: boolean
          description: >-
            If true, allows setting the contract end date earlier than the
            end_timestamp of existing finalized invoices. Finalized invoices
            will be unchanged; if you want to incorporate the new end date, you
            can void and regenerate finalized usage invoices. Defaults to true.
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
          description: IDs of commits to archive
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
          description: IDs of credits to archive
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
          description: IDs of scheduled charges to archive
        archive_spend_trackers:
          x-mint:
            groups:
              - ff:tb-spend-trackers
          type: array
          description: Aliases of spend trackers to archive.
          items:
            type: string
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
          description: IDs of overrides to remove
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
    CommitInputV2:
      type: object
      required:
        - type
        - product_id
      properties:
        type:
          type: string
          enum:
            - PREPAID
            - prepaid
            - POSTPAID
            - postpaid
        rate_type:
          type: string
          enum:
            - COMMIT_RATE
            - commit_rate
            - LIST_RATE
            - list_rate
        name:
          type: string
          minLength: 1
          description: displayed on invoices
        product_id:
          type: string
          format: uuid
        access_schedule:
          $ref: '#/components/schemas/ScheduleDurationInputV2'
          description: >-
            Required: Schedule for distributing the commit to the customer. For
            "POSTPAID" commits only one schedule item is allowed and amount must
            match invoice_schedule total.
        invoice_schedule:
          $ref: '#/components/schemas/SchedulePointInTimeInputV2'
          description: >-
            Required for "POSTPAID" commits: the true up invoice will be
            generated at this time and only one schedule item is allowed; the
            total must match access_schedule amount. Optional for "PREPAID"
            commits: if not provided, this will be a "complimentary" commit with
            no invoice.
        amount:
          type: number
          description: (DEPRECATED) Use access_schedule and invoice_schedule instead.
        description:
          type: string
          description: Used only in UI/API. It is not exposed to end customers.
        rollover_fraction:
          type: number
          description: >-
            Fraction of unused segments that will be rolled over. Must be
            between 0 and 1.
        priority:
          type: number
          description: >-
            If multiple commits are applicable, the one with the lower priority
            will apply first.
        applicable_product_ids:
          type: array
          items:
            type: string
            format: uuid
          description: >-
            Which products the commit applies to. If applicable_product_ids,
            applicable_product_tags or specifiers are not provided, the commit
            applies to all products.
        applicable_product_tags:
          type: array
          items:
            type: string
          description: >-
            Which tags the commit applies to. If applicable_product_ids,
            applicable_product_tags or specifiers are not provided, the commit
            applies to all products.
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
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: commit
        temporary_id:
          type: string
          description: >-
            A temporary ID for the commit that can be used to reference the
            commit for commit specific overrides.
        payment_gate_config:
          $ref: '#/components/schemas/CommitPaymentGateConfig'
          description: optionally payment gate this commit
        hierarchy_configuration:
          $ref: '#/components/schemas/CommitHierarchyConfiguration'
          description: Optional configuration for commit hierarchy access control
        spend_tracker_attributes:
          x-mint:
            groups:
              - ff:tb-spend-trackers
          allOf:
            - $ref: '#/components/schemas/SpendTrackerAttributesInput'
          description: >-
            Optional attributes for spend tracker integration. Immutable after
            creation.
    CreditInputV2:
      type: object
      required:
        - product_id
        - access_schedule
      properties:
        name:
          type: string
          minLength: 1
          description: displayed on invoices
        product_id:
          type: string
          format: uuid
        access_schedule:
          $ref: '#/components/schemas/ScheduleDurationInputV2'
          description: Schedule for distributing the credit to the customer.
        description:
          type: string
          description: Used only in UI/API. It is not exposed to end customers.
        applicable_product_ids:
          type: array
          items:
            type: string
            format: uuid
          description: >-
            Which products the credit applies to. If both applicable_product_ids
            and applicable_product_tags are not provided, the credit applies to
            all products.
        applicable_product_tags:
          type: array
          items:
            type: string
          description: >-
            Which tags the credit applies to. If both applicable_product_ids and
            applicable_product_tags are not provided, the credit applies to all
            products.
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
        priority:
          type: number
          description: >-
            If multiple credits are applicable, the one with the lower priority
            will apply first.
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: contract_credit
        rollover_fraction:
          type: number
          description: >-
            Fraction of unused segments that will be rolled over. Must be
            between 0 and 1.
        rate_type:
          type: string
          enum:
            - COMMIT_RATE
            - commit_rate
            - LIST_RATE
            - list_rate
        hierarchy_configuration:
          $ref: '#/components/schemas/CommitHierarchyConfiguration'
          description: Optional configuration for credit hierarchy access control
    RecurringCommitInputV2:
      allOf:
        - $ref: '#/components/schemas/RecurringCommitOrCreditInputBaseV2'
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
              description: >-
                Optional rounding configuration for prorated recurring commit
                amounts.
              properties:
                access:
                  $ref: '#/components/schemas/ProrationRoundingConfigV2'
                invoice:
                  $ref: '#/components/schemas/ProrationRoundingConfigV2'
    RecurringCreditInputV2:
      allOf:
        - $ref: '#/components/schemas/RecurringCommitOrCreditInputBaseV2'
        - type: object
          properties:
            proration_rounding:
              type: object
              description: >-
                Optional rounding configuration for prorated recurring credit
                amounts.
              properties:
                access:
                  $ref: '#/components/schemas/ProrationRoundingConfigV2'
    DiscountInputV2:
      type: object
      required:
        - product_id
        - schedule
      properties:
        product_id:
          type: string
          format: uuid
        name:
          type: string
          minLength: 1
          description: displayed on invoices
        schedule:
          $ref: '#/components/schemas/SchedulePointInTimeInputV2'
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
    OverrideInputV2:
      type: object
      required:
        - starting_at
      properties:
        starting_at:
          type: string
          format: date-time
          description: >-
            RFC 3339 timestamp indicating when the override will start applying
            (inclusive)
        ending_before:
          type: string
          format: date-time
          description: >-
            RFC 3339 timestamp indicating when the override will stop applying
            (exclusive)
        entitled:
          type: boolean
        type:
          type: string
          enum:
            - OVERWRITE
            - overwrite
            - MULTIPLIER
            - multiplier
            - TIERED
            - tiered
          description: Overwrites are prioritized over multipliers and tiered overrides.
        multiplier:
          type: number
          description: Required for MULTIPLIER type. Must be >=0.
        priority:
          type: number
          description: >-
            Required for EXPLICIT multiplier prioritization scheme and all
            TIERED overrides. Under EXPLICIT prioritization, overwrites are
            prioritized first, and then tiered and multiplier overrides are
            prioritized by their priority value (lowest first). Must be > 0.
        overwrite_rate:
          $ref: '#/components/schemas/OverwriteRateInputV2'
          description: Required for OVERWRITE type.
        product_id:
          type: string
          format: uuid
          description: ID of the product whose rate is being overridden
        applicable_product_tags:
          type: array
          items:
            type: string
          description: tags identifying products whose rates are being overridden
        override_specifiers:
          type: array
          items:
            $ref: '#/components/schemas/OverrideSpecifierInputV2'
          description: >-
            Cannot be used in conjunction with product_id or
            applicable_product_tags. If provided, the override will apply to all
            products with the specified specifiers.
        tiers:
          type: array
          items:
            $ref: '#/components/schemas/OverrideTierInput'
          description: Required for TIERED type. Must have at least one tier.
        is_commit_specific:
          type: boolean
          description: >-
            Indicates whether the override should only apply to commits.
            Defaults to `false`. If `true`, you can specify relevant commits in
            `override_specifiers` by passing `commit_ids`.
        target:
          type: string
          enum:
            - COMMIT_RATE
            - commit_rate
            - LIST_RATE
            - list_rate
          description: >-
            Indicates whether the override applies to commit rates or list
            rates. Can only be used for overrides that have `is_commit_specific`
            set to `true`. Defaults to `"LIST_RATE"`.
    ScheduledChargeInputV2:
      type: object
      required:
        - product_id
        - schedule
      properties:
        product_id:
          type: string
          format: uuid
        name:
          type: string
          minLength: 1
          description: displayed on invoices
        schedule:
          $ref: '#/components/schemas/SchedulePointInTimeInputV2'
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
    ProServiceInput:
      type: object
      required:
        - product_id
        - unit_price
        - quantity
        - max_amount
      properties:
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
    ResellerRoyaltyOrUpdateInput:
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
        applicable_product_ids:
          type: array
          items:
            type: string
            format: uuid
          description: >-
            Must provide at least one of applicable_product_ids or
            applicable_product_tags.
        applicable_product_tags:
          type: array
          items:
            type: string
          description: >-
            Must provide at least one of applicable_product_ids or
            applicable_product_tags.
        starting_at:
          type: string
          format: date-time
        ending_before:
          description: >-
            Use null to indicate that the existing end timestamp should be
            removed.
          type: string
          nullable: true
          format: date-time
        reseller_contract_value:
          type: number
        aws_options:
          type: object
          properties:
            aws_account_number:
              type: string
            aws_payer_reference_id:
              type: string
            aws_offer_id:
              type: string
        gcp_options:
          type: object
          properties:
            gcp_account_id:
              type: string
            gcp_offer_id:
              type: string
    SubscriptionsInputV2:
      type: array
      description: >-
        Optional list of
        [subscriptions](https://docs.metronome.com/manage-product-access/create-subscription/)
        to add to the contract.
      items:
        $ref: '#/components/schemas/SubscriptionInputV2'
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
    BillingProviderConfigurationUpdate:
      type: object
      required:
        - billing_provider_configuration
        - schedule
      properties:
        billing_provider_configuration:
          type: object
          properties:
            billing_provider_configuration_id:
              type: string
              format: uuid
              nullable: true
            billing_provider:
              $ref: '#/components/schemas/BillingProviderType'
            delivery_method:
              $ref: '#/components/schemas/BillingProviderDeliveryMethodType'
        schedule:
          description: >-
            Indicates when the billing provider will be active on the contract.
            Any charges accrued during the schedule will be billed to the
            indicated billing provider.
          type: object
          required:
            - effective_at
          properties:
            effective_at:
              $ref: >-
                #/components/schemas/BillingProviderConfigurationUpdateEffectiveAtType
              description: When the billing provider update will take effect.
    RevenueSystemConfigurationUpdate:
      x-mint:
        groups:
          - ff:revenue-rec-configurations-enabled
      required:
        - revenue_system_configuration
        - schedule
      properties:
        revenue_system_configuration:
          type: object
          properties:
            revenue_system_configuration_id:
              type: string
              format: uuid
              nullable: true
            provider:
              $ref: '#/components/schemas/RevenueSystemProviderTypeV2'
            delivery_method:
              $ref: '#/components/schemas/BillingProviderDeliveryMethodType'
        schedule:
          type: object
          required:
            - effective_at
          properties:
            effective_at:
              $ref: >-
                #/components/schemas/RevenueSystemConfigurationUpdateEffectiveAtType
    SpendTrackerInput:
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
            $ref: '#/components/schemas/SpendTrackerApplicableSpendSpecifierInput'
    UpdateScheduledChargeInput:
      type: object
      required:
        - scheduled_charge_id
      properties:
        scheduled_charge_id:
          type: string
          format: uuid
        netsuite_sales_order_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          nullable: true
        invoice_schedule:
          $ref: '#/components/schemas/UpdateInvoiceScheduleInput'
    UpdateCommitInput:
      type: object
      required:
        - commit_id
      properties:
        commit_id:
          type: string
          format: uuid
        name:
          type: string
        description:
          type: string
        access_schedule:
          $ref: '#/components/schemas/UpdateAccessScheduleInput'
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
          $ref: '#/components/schemas/UpdateInvoiceScheduleInput'
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
        rate_type:
          type: string
          enum:
            - LIST_RATE
            - list_rate
            - COMMIT_RATE
            - commit_rate
          description: >-
            If provided, updates the commit to use the specified rate type for
            current and future invoices. Previously finalized invoices will need
            to be voided and regenerated to reflect the rate type change.
    UpdateCreditInput:
      type: object
      required:
        - credit_id
      properties:
        credit_id:
          type: string
          format: uuid
        name:
          type: string
        description:
          type: string
        access_schedule:
          $ref: '#/components/schemas/UpdateAccessScheduleInput'
        rollover_fraction:
          type: number
          nullable: true
        netsuite_sales_order_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
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
        priority:
          type: number
          nullable: true
        hierarchy_configuration:
          $ref: '#/components/schemas/CommitHierarchyConfiguration'
          description: Optional configuration for commit hierarchy access control
        rate_type:
          type: string
          enum:
            - LIST_RATE
            - list_rate
            - COMMIT_RATE
            - commit_rate
          description: >-
            If provided, updates the credit to use the specified rate type for
            current and future invoices. Previously finalized invoices will need
            to be voided and regenerated to reflect the rate type change.
    UpdateRecurringCommitInput:
      type: object
      required:
        - recurring_commit_id
      properties:
        recurring_commit_id:
          type: string
          format: uuid
        access_amount:
          type: object
          properties:
            unit_price:
              type: number
            quantity:
              type: number
        invoice_amount:
          type: object
          properties:
            unit_price:
              type: number
            quantity:
              type: number
        ending_before:
          type: string
          format: date-time
          nullable: true
        rate_type:
          type: string
          enum:
            - LIST_RATE
            - list_rate
            - COMMIT_RATE
            - commit_rate
          description: >-
            If provided, updates the recurring commit to use the specified rate
            type when generating future commits.
        proration_rounding:
          type: object
          nullable: true
          description: >-
            If provided, updates the rounding config on the recurring commit.
            Set to null to clear rounding. Omit to leave unchanged.
          properties:
            access:
              $ref: '#/components/schemas/NullableProrationRoundingConfig'
            invoice:
              $ref: '#/components/schemas/NullableProrationRoundingConfig'
    UpdateRecurringCreditInput:
      type: object
      required:
        - recurring_credit_id
      properties:
        recurring_credit_id:
          type: string
          format: uuid
        access_amount:
          type: object
          properties:
            unit_price:
              type: number
            quantity:
              type: number
        ending_before:
          type: string
          format: date-time
          nullable: true
        rate_type:
          type: string
          enum:
            - LIST_RATE
            - list_rate
            - COMMIT_RATE
            - commit_rate
          description: >-
            If provided, updates the recurring credit to use the specified rate
            type when generating future credits.
        proration_rounding:
          type: object
          nullable: true
          description: >-
            If provided, updates the rounding config on the recurring credit.
            Set to null to clear rounding. Omit to leave unchanged.
          properties:
            access:
              $ref: '#/components/schemas/NullableProrationRoundingConfig'
    UpdateSubscriptionInput:
      type: object
      required:
        - subscription_id
      properties:
        subscription_id:
          type: string
          format: uuid
        name:
          type: string
        ending_before:
          type: string
          format: date-time
          nullable: true
        quantity_management_mode_update:
          type: object
          description: >-
            Update the subscription's quantity management mode from
            QUANTITY_ONLY to SEAT_BASED with the provided seat_group_key.
          required:
            - quantity_management_mode
            - seat_config
          properties:
            quantity_management_mode:
              type: string
              enum:
                - SEAT_BASED
                - seat_based
            seat_config:
              type: object
              required:
                - seat_group_key
              properties:
                seat_group_key:
                  type: string
        quantity_updates:
          type: array
          description: >-
            Quantity changes are applied on the effective date based on the
            order which they are sent. For example, if I scheduled the quantity
            to be 12 on May 21 and then scheduled a quantity delta change of -1,
            the result from that day would be 11.
          items:
            type: object
            required:
              - starting_at
            properties:
              quantity:
                type: number
                description: >-
                  The new quantity for the subscription. Must be provided if
                  quantity_delta is not provided. Must be non-negative.
              quantity_delta:
                type: number
                description: >-
                  The delta to add to the subscription's quantity. Must be
                  provided if quantity is not provided. Can't be zero. It also
                  can't result in a negative quantity on the subscription.
              starting_at:
                type: string
                format: date-time
        seat_updates:
          $ref: '#/components/schemas/SubscriptionSeatUpdateInput'
        proration_rounding:
          $ref: '#/components/schemas/NullableProrationRoundingConfig'
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
    ScheduleDurationInputV2:
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
            - spend
            - QUANTITY
            - quantity
          description: >-
            Determines how the balance is drawn down. `SPEND` deducts the dollar
            cost of usage. `QUANTITY` deducts the number of units used. Defaults
            to `SPEND` if omitted.
        credit_type_id:
          type: string
          format: uuid
        schedule_items:
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
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
    CommitPaymentGateConfig:
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
            if you do not wish Metronome to calculate tax on your behalf.
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
            on_session_payment:
              type: boolean
              description: >-
                If true, the payment will be made assuming the customer is
                present (i.e. on session). 


                If false, the payment will be made assuming the customer is not
                present (i.e. off session). 

                For cardholders from a country with an e-mandate requirement
                (e.g. India), the payment may be declined.


                If left blank, will default to false.
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
                and denomination as the commit's invoice schedule
            tax_name:
              type: string
              description: >-
                Name of the tax to be applied. This may be used in an invoice
                line item description.
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
    SpendTrackerAttributesInput:
      type: object
      required:
        - counts_as_discounted
      properties:
        counts_as_discounted:
          type: boolean
          description: >-
            If true, this commit will be included in spend trackers with
            discounted set to DISCOUNTED_ONLY
    RecurringCommitOrCreditInputBaseV2:
      type: object
      required:
        - product_id
        - access_amount
        - priority
        - commit_duration
        - starting_at
      properties:
        name:
          type: string
          minLength: 1
          description: >-
            displayed on invoices. will be passed through to the individual
            commits
        product_id:
          type: string
          format: uuid
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
              description: >-
                This field is required unless a subscription is attached via
                `subscription_config`.
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
          description: Will be passed down to the individual commits
        temporary_id:
          type: string
          description: >-
            A temporary ID that can be used to reference the recurring commit
            for commit specific overrides.
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
          description: determines the start time for the first commit
        ending_before:
          type: string
          format: date-time
          description: >-
            Determines when the contract will stop creating recurring commits.
            optional
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
          description: >-
            Defines the length of the access schedule for each created
            commit/credit. The value represents the number of units. Unit
            defaults to "PERIODS", where the length of a period is determined by
            the recurrence_frequency.
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
          $ref: '#/components/schemas/RecurringCommitSubscriptionConfigInputV2'
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
    OverwriteRateInputV2:
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
        credit_type_id:
          type: string
          format: uuid
    OverrideSpecifierInputV2:
      type: object
      properties:
        commit_ids:
          type: array
          items:
            type: string
          description: >-
            If provided, the override will only apply to the specified commits.
            Can only be used for commit specific overrides. If not provided, the
            override will apply to all commits.
        recurring_commit_ids:
          type: array
          items:
            type: string
          description: >-
            Can only be used for commit specific overrides. Must be used in
            conjunction with one of product_id, product_tags,
            pricing_group_values, or presentation_group_values. If provided, the
            override will only apply to commits created by the specified
            recurring commit ids.
        any_commit_or_credit_ids:
          type: array
          items:
            type: string
          description: >-
            Can only be used for commit specific overrides. Must be used in
            conjunction with one of `product_id`, `product_tags`,
            `pricing_group_values`, or `presentation_group_values`. Must be used
            instead of both `commit_ids` and `recurring_commit_ids` If provided,
            the override will apply to any specified commit, credit, recurring
            commit or recurring credit IDs.
        product_id:
          type: string
          format: uuid
          description: >-
            If provided, the override will only apply to the product with the
            specified ID.
        product_tags:
          type: array
          items:
            type: string
          description: >-
            If provided, the override will only apply to products with all the
            specified tags.
        pricing_group_values:
          type: object
          description: >-
            A map of pricing group names to values. The override will only apply
            to products with the specified pricing group values.
          additionalProperties:
            type: string
        presentation_group_values:
          type: object
          description: >-
            A map of group names to values. The override will only apply to line
            items with the specified presentation group values. Can only be used
            for multiplier overrides.
          additionalProperties:
            type: string
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
    OverrideTierInput:
      type: object
      required:
        - multiplier
      properties:
        size:
          type: number
        multiplier:
          type: number
    ResellerType:
      type: string
      enum:
        - AWS
        - AWS_PRO_SERVICE
        - GCP
        - GCP_PRO_SERVICE
    SubscriptionInputV2:
      required:
        - subscription_rate
        - collection_schedule
        - proration
      type: object
      properties:
        subscription_rate:
          $ref: '#/components/schemas/SubscriptionRateInput'
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
          $ref: '#/components/schemas/SubscriptionProrationInputV2'
        initial_quantity:
          type: number
          description: >-
            The initial quantity for the subscription. It must be non-negative
            value. Required if quantity_management_mode is QUANTITY_ONLY.
        starting_at:
          type: string
          format: date-time
          description: >-
            Inclusive start time for the subscription. If not provided, defaults
            to contract start date
        ending_before:
          type: string
          format: date-time
          description: >-
            Exclusive end time for the subscription. If not provided,
            subscription inherits contract end date.
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: subscription
        temporary_id:
          type: string
          description: >-
            A temporary ID used to reference the subscription in recurring
            commit/credit subscription configs created within the same payload.
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
          $ref: '#/components/schemas/SubscriptionSeatConfigInput'
        billing_cycle_config:
          $ref: '#/components/schemas/SubscriptionBillingCycleConfigInput'
        payment_gate_config:
          $ref: '#/components/schemas/SubscriptionPaymentGateConfigInput'
          x-stainless-skip: true
          x-mint:
            groups:
              - ff:payment-gated-subscriptions-enabled
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
    BillingProviderConfigurationUpdateEffectiveAtType:
      type: string
      enum:
        - START_OF_CURRENT_PERIOD
        - START_OF_NEXT_PERIOD
    RevenueSystemProviderTypeV2:
      type: string
      enum:
        - netsuite
      description: The revenue system provider type.
    RevenueSystemConfigurationUpdateEffectiveAtType:
      type: string
      x-mint:
        groups:
          - ff:revenue-rec-configurations-enabled
      enum:
        - START_OF_CURRENT_PERIOD
        - START_OF_NEXT_PERIOD
      description: When the revenue system configuration update will take effect.
    SpendTrackerApplicableSpendSpecifierInput:
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
          description: >-
            Filter by whether the spend was discounted. Defaults to ANY if
            omitted.
    UpdateInvoiceScheduleInput:
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
    UpdateAccessScheduleInput:
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
              ending_before:
                type: string
                format: date-time
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
              ending_before:
                type: string
                format: date-time
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
    NullableProrationRoundingConfig:
      type: object
      nullable: true
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
    UpdateSpendThresholdCommit:
      type: object
      allOf:
        - $ref: '#/components/schemas/UpdateBaseThresholdCommit'
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
    UpdatePrepaidBalanceThresholdCommit:
      type: object
      allOf:
        - $ref: '#/components/schemas/UpdateBaseThresholdCommit'
        - $ref: '#/components/schemas/OptionalThresholdCommitFieldsUpdate'
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
    RecurringCommitSubscriptionConfigInputV2:
      type: object
      required:
        - apply_seat_increase_config
        - subscription_id
      properties:
        allocation:
          $ref: '#/components/schemas/SubscriptionConfigAllocationInputV2'
        apply_seat_increase_config:
          $ref: '#/components/schemas/ApplySeatIncreaseConfigForRecurringCommit'
        subscription_id:
          type: string
          description: ID of the subscription to configure on the recurring commit/credit.
        access_policy:
          x-stainless-skip: true
          type: string
          enum:
            - BILLING_PERIOD_PAID
            - INITIAL_BILLING_PERIOD_PAID_ONLY
          x-mint:
            groups:
              - ff:payment-gated-subscriptions-enabled
          description: >-
            Controls when a customer can access recurring commit or credit child
            balances when the attached subscription is payment-gated.
            `BILLING_PERIOD_PAID` releases each balance after payment for its
            billing period. `INITIAL_BILLING_PERIOD_PAID_ONLY` releases all
            balances after the first payment.
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
    SubscriptionRateInput:
      type: object
      required:
        - billing_frequency
        - product_id
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
          description: >-
            Frequency to bill subscription with. Together with product_id, must
            match existing rate on the rate card.
        product_id:
          type: string
          format: uuid
          description: Must be subscription type product
    SubscriptionProrationInputV2:
      type: object
      properties:
        is_prorated:
          type: boolean
          description: >-
            Indicates if the partial period will be prorated or charged a full
            amount.
        invoice_behavior:
          type: string
          enum:
            - BILL_IMMEDIATELY
            - BILL_ON_NEXT_COLLECTION_DATE
            - bill_immediately
            - bill_on_next_collection_date
          description: >
            Indicates how mid-period quantity adjustments are invoiced.

            **BILL_IMMEDIATELY**: Only available when collection schedule is
            `ADVANCE`. The quantity increase will be billed immediately on the
            scheduled date.

            **BILL_ON_NEXT_COLLECTION_DATE**: The quantity increase will be
            billed for in-arrears at the end of the period.
        rounding:
          $ref: '#/components/schemas/ProrationRoundingConfigV2'
    SubscriptionSeatConfigInput:
      type: object
      required:
        - seat_group_key
        - initial_seat_ids
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
        initial_seat_ids:
          type: array
          items:
            type: string
          description: The initial assigned seats on this subscription.
        initial_unassigned_seats:
          type: number
          description: The initial amount of unassigned seats on this subscription.
    SubscriptionBillingCycleConfigInput:
      type: object
      properties:
        anchor_date:
          type: string
          format: date-time
          description: >-
            The date to anchor the billing cycle to. If omitted, defaults to the
            contract's usage invoice billing cycle anchor date.
        invoice_placement:
          type: string
          enum:
            - ON_SCHEDULED_INVOICE
            - ON_USAGE_INVOICE
            - on_scheduled_invoice
            - on_usage_invoice
          description: >-
            Controls whether this subscription consolidates onto usage invoices
            or gets its own scheduled invoice. Defaults to ON_USAGE_INVOICE if
            omitted.
    SubscriptionPaymentGateConfigInput:
      type: object
      x-stainless-skip: true
      x-mint:
        groups:
          - ff:payment-gated-subscriptions-enabled
      required:
        - payment_gate_type
      properties:
        payment_gate_type:
          type: string
          enum:
            - STRIPE
            - stripe
          description: >-
            Gate access to the subscription based on successful collection of
            payment. Select STRIPE for Metronome to facilitate payment via
            Stripe.
        tax_type:
          type: string
          enum:
            - NONE
            - STRIPE
            - none
            - stripe
          description: >-
            Stripe tax is only supported for Stripe payment gateway. Select NONE
            if you do not wish Metronome to calculate tax on your behalf.
            Leaving this field blank will default to NONE.
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
    ExcludeThresholdBalanceSpecifierV2:
      type: object
      required:
        - custom_field_filters
      properties:
        custom_field_filters:
          type: array
          items:
            $ref: '#/components/schemas/BalanceCustomFieldFilterType'
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
    SubscriptionConfigAllocationInputV2:
      type: string
      enum:
        - POOLED
        - INDIVIDUAL
      description: >-
        If set to POOLED, allocation added per seat is pooled across the
        account. If set to INDIVIDUAL, each seat in the subscription will have
        its own allocation.
    ApplySeatIncreaseConfigForRecurringCommit:
      type: object
      required:
        - is_prorated
      properties:
        is_prorated:
          type: boolean
          description: Indicates whether a mid-period seat increase should be prorated.
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
    SubscriptionConfigAllocation:
      type: string
      enum:
        - INDIVIDUAL
        - POOLED
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
