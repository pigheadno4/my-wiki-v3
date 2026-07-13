<!-- Source URL: https://docs.metronome.com/api-reference/packages/get-a-package.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a package

> Gets the details for a specific package, including name, aliases, duration, and terms. Use this endpoint to understand a package’s alias schedule, or display a specific package’s details to end customers.




## OpenAPI

````yaml /openapi.json post /v1/packages/get
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
  /v1/packages/get:
    post:
      tags:
        - Packages
      summary: Get a package
      description: >
        Gets the details for a specific package, including name, aliases,
        duration, and terms. Use this endpoint to understand a package’s alias
        schedule, or display a specific package’s details to end customers.
      operationId: getPackage-v1
      requestBody:
        description: Package ID
        content:
          application/json:
            schema:
              type: object
              required:
                - package_id
              properties:
                package_id:
                  type: string
                  format: uuid
            example:
              package_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
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
                    $ref: '#/components/schemas/Package'
              example:
                data:
                  id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                  name: Basic Package
                  usage_statement_schedule:
                    frequency: MONTHLY
                  created_at: '2019-12-31T14:23:55.234Z'
                  created_by: Alice
                  commits:
                    - id: 62c0cb84-bf3f-48b9-9bcf-a8ddf8c1cf35
                      type: PREPAID
                      name: My test commit
                      description: My test commit description
                      product:
                        id: 2e30f074-d04c-412e-a134-851ebfa5ceb2
                        name: My product A
                      applicable_product_ids:
                        - 13a2179b-f0cb-460b-85a1-cd42964ca533
                      access_schedule:
                        credit_type:
                          id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                          name: USD (cents)
                        schedule_items:
                          - id: 2d45952c-5a6e-43a9-8aab-f61ee21be81a
                            amount: 10000000
                            starting_at_offset:
                              unit: MONTHS
                              value: 1
                            duration:
                              unit: MONTHS
                              value: 3
                      invoice_schedule:
                        credit_type:
                          id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                          name: USD (cents)
                        schedule_items:
                          - id: f15e4e23-f74e-4de4-9b3a-8b07434116c4
                            unit_price: 10000000
                            quantity: 1
                            date_offset:
                              unit: MONTHS
                              value: 4
                        do_not_invoice: false
                  overrides:
                    - id: 6cf3292a-e85c-4be6-822c-e25ba9d19757
                      starting_at_offset:
                        unit: MONTHS
                        value: 1
                      type: MULTIPLIER
                      multiplier: 0.1
                      override_specifiers:
                        - product_id: eae8903b-693b-41a7-8c0b-f23748c9a9c8
                  scheduled_charges:
                    - id: 04dbca69-0bc2-45c6-ba22-a53934353b10
                      name: Test Scheduled Charge
                      description: Test Scheduled Charge Description
                      product:
                        id: eae8903b-693b-41a7-8c0b-f23748c9a9c8
                        name: My product B
                      schedule:
                        credit_type:
                          id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                          name: USD (cents)
                        schedule_items:
                          - id: f15e4e23-f74e-4de4-9b3a-8b07434116c4
                            unit_price: 10000000
                            quantity: 1
                            date_offset:
                              unit: MONTHS
                              value: 4
        '404':
          $ref: '#/components/responses/NotFound'
components:
  schemas:
    Package:
      type: object
      required:
        - id
        - commits
        - overrides
        - scheduled_charges
        - created_at
        - created_by
        - usage_statement_schedule
      properties:
        id:
          type: string
          format: uuid
        uniqueness_key:
          $ref: '#/components/schemas/UniquenessKey'
        name:
          type: string
        rate_card_id:
          type: string
          format: uuid
        aliases:
          type: array
          items:
            $ref: '#/components/schemas/PackageAlias'
        duration:
          $ref: '#/components/schemas/RelativeDate'
        commits:
          type: array
          items:
            $ref: '#/components/schemas/CommitTemplate'
        credits:
          type: array
          items:
            $ref: '#/components/schemas/CreditTemplate'
        overrides:
          type: array
          items:
            $ref: '#/components/schemas/OverrideTemplate'
        scheduled_charges:
          type: array
          items:
            $ref: '#/components/schemas/ScheduledChargeTemplate'
        scheduled_charges_on_usage_invoices:
          $ref: '#/components/schemas/ScheduledChargesOnUsageInvoices'
        created_at:
          type: string
          format: date-time
        created_by:
          type: string
        net_payment_terms_days:
          type: number
        usage_statement_schedule:
          $ref: '#/components/schemas/UsageStatementScheduleTemplate'
        multiplier_override_prioritization:
          type: string
          enum:
            - LOWEST_MULTIPLIER
            - EXPLICIT
          description: >-
            Defaults to LOWEST_MULTIPLIER, which applies the greatest discount
            to list prices automatically. EXPLICIT prioritization requires
            specifying priorities for each multiplier; the one with the lowest
            priority value will be prioritized first.
        billing_provider:
          $ref: '#/components/schemas/BillingProviderType'
        delivery_method:
          $ref: '#/components/schemas/BillingProviderDeliveryMethodType'
        recurring_commits:
          type: array
          items:
            $ref: '#/components/schemas/RecurringCommitTemplate'
        recurring_credits:
          type: array
          items:
            $ref: '#/components/schemas/RecurringCreditTemplate'
        spend_threshold_configuration:
          $ref: '#/components/schemas/SpendThresholdConfiguration'
        prepaid_balance_threshold_configuration:
          $ref: '#/components/schemas/PrepaidBalanceThresholdConfiguration'
        spend_trackers:
          type: array
          x-mint:
            groups:
              - ff:tb-spend-trackers
          items:
            $ref: '#/components/schemas/SpendTrackerTemplate'
        subscriptions:
          type: array
          items:
            $ref: '#/components/schemas/SubscriptionTemplate'
        contract_name:
          type: string
          description: The name to use for contracts created from this package.
        archived_at:
          type: string
          format: date-time
    UniquenessKey:
      type: string
      minLength: 1
      maxLength: 128
      description: >-
        Prevents the creation of duplicates. If a request to create a record is
        made with a previously used uniqueness key, a new record will not be
        created and the request will fail with a 409 error.
    PackageAlias:
      type: object
      required:
        - name
      properties:
        name:
          type: string
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
    CommitTemplate:
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
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: package_commit
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
          $ref: '#/components/schemas/RelativeScheduleDuration'
          description: >-
            The schedule that the customer will gain access to the credits
            purposed with this commit.
        invoice_schedule:
          allOf:
            - $ref: '#/components/schemas/RelativeSchedulePointInTime'
            - type: object
              required:
                - do_not_invoice
              properties:
                do_not_invoice:
                  type: boolean
                  description: If true, this schedule will not generate an invoice.
                  default: false
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
    CreditTemplate:
      type: object
      required:
        - id
        - type
        - product
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        description:
          type: string
        priority:
          type: number
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: package_credit
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
        access_schedule:
          $ref: '#/components/schemas/RelativeScheduleDuration'
        rate_type:
          type: string
          enum:
            - COMMIT_RATE
            - LIST_RATE
    OverrideTemplate:
      type: object
      required:
        - id
        - starting_at_offset
        - override_specifiers
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
        applicable_product_tags:
          type: array
          items:
            type: string
        override_specifiers:
          type: array
          items:
            $ref: '#/components/schemas/OverrideSpecifierTemplate'
        starting_at_offset:
          $ref: '#/components/schemas/RelativeDate'
        duration:
          $ref: '#/components/schemas/RelativeDate'
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
          $ref: '#/components/schemas/OverwriteRate'
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
    ScheduledChargeTemplate:
      type: object
      required:
        - id
        - product
        - schedule
      properties:
        id:
          type: string
          format: uuid
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: package_scheduled_charge
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
          $ref: '#/components/schemas/RelativeSchedulePointInTime'
        name:
          type: string
        description:
          type: string
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
    UsageStatementScheduleTemplate:
      type: object
      required:
        - frequency
      properties:
        frequency:
          type: string
          enum:
            - MONTHLY
            - QUARTERLY
            - ANNUAL
            - WEEKLY
        day:
          type: string
          enum:
            - FIRST_OF_MONTH
            - CONTRACT_START
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
    RecurringCommitTemplate:
      allOf:
        - $ref: '#/components/schemas/RecurringCommitOrCreditTemplateBase'
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
              description: The amount the customer should be billed for the commit.
            proration_rounding:
              type: object
              nullable: true
              description: Rounding configuration for prorated recurring commit amounts.
              properties:
                access:
                  $ref: '#/components/schemas/ProrationRoundingConfig'
                invoice:
                  $ref: '#/components/schemas/ProrationRoundingConfig'
    RecurringCreditTemplate:
      allOf:
        - $ref: '#/components/schemas/RecurringCommitOrCreditTemplateBase'
        - type: object
          properties:
            proration_rounding:
              type: object
              nullable: true
              description: Rounding configuration for prorated recurring credit amounts.
              properties:
                access:
                  $ref: '#/components/schemas/ProrationRoundingConfig'
    SpendThresholdConfiguration:
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
          $ref: '#/components/schemas/PaymentGateConfig'
        discount_configuration:
          $ref: '#/components/schemas/DiscountConfiguration'
          x-mint:
            groups:
              - ff:threshold-billing-discounts
    PrepaidBalanceThresholdConfiguration:
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
            contract's prepaid balance lowers to this amount, a threshold charge
            will be initiated.
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
          $ref: '#/components/schemas/PrepaidBalanceThresholdCommit'
        payment_gate_config:
          $ref: '#/components/schemas/PaymentGateConfig'
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
            $ref: '#/components/schemas/ThresholdBalanceSpecifier'
    SpendTrackerTemplate:
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
    SubscriptionTemplate:
      type: object
      required:
        - subscription_rate
        - collection_schedule
        - proration
      properties:
        id:
          type: string
          format: uuid
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: package_subscription
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
          $ref: '#/components/schemas/SubscriptionProration'
        initial_quantity:
          type: number
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
            the quantity. You must use a SEAT_BASED subscription to use a linked
            recurring credit with an allocation per seat. `seat_config` must be
            provided with this option.
        seat_config:
          $ref: '#/components/schemas/SubscriptionSeatConfig'
        starting_at_offset:
          $ref: '#/components/schemas/RelativeDate'
        duration:
          $ref: '#/components/schemas/RelativeDate'
        fiat_credit_type_id:
          type: string
          format: uuid
        billing_cycle_config:
          $ref: '#/components/schemas/SubscriptionBillingCycleConfigTemplate'
    Error:
      required:
        - message
      type: object
      properties:
        message:
          type: string
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
    RelativeScheduleDuration:
      type: object
      required:
        - credit_type
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
              - starting_at_offset
              - duration
              - amount
            properties:
              id:
                type: string
                format: uuid
              starting_at_offset:
                $ref: '#/components/schemas/RelativeDate'
              duration:
                $ref: '#/components/schemas/RelativeDate'
              amount:
                type: number
    RelativeSchedulePointInTime:
      type: object
      required:
        - credit_type
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
              - unit_price
              - quantity
              - date_offset
            properties:
              id:
                type: string
                format: uuid
              unit_price:
                type: number
              quantity:
                type: number
              date_offset:
                $ref: '#/components/schemas/RelativeDate'
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
    OverrideSpecifierTemplate:
      type: object
      properties:
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
        commit_template_ids:
          type: array
          items:
            type: string
        recurring_commit_template_ids:
          type: array
          items:
            type: string
        any_commit_or_credit_template_ids:
          type: array
          items:
            type: string
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
    OverwriteRate:
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
            SUBSCRIPTION:
              - ff:legacy-subscriptions-enabled
            subscription:
              - ff:legacy-subscriptions-enabled
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
          x-mint:
            groups:
              - ff:legacy-subscriptions-enabled
          description: Default quantity. For SUBSCRIPTION rate_type, this must be >=0.
        is_prorated:
          type: boolean
          x-mint:
            groups:
              - ff:legacy-subscriptions-enabled
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
    RecurringCommitOrCreditTemplateBase:
      type: object
      required:
        - id
        - product
        - access_amount
        - priority
        - commit_duration
        - starting_at_offset
        - rate_type
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
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
        rollover_fraction:
          type: number
          description: >-
            Will be passed down to the individual commits. This controls how
            much of an individual unexpired commit will roll over upon contract
            transition. Must be between 0 and 1.
        priority:
          type: number
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
        rate_type:
          type: string
          enum:
            - COMMIT_RATE
            - LIST_RATE
          description: Whether the created commits will use the commit rate or list rate
        starting_at_offset:
          $ref: '#/components/schemas/RelativeDate'
          description: >-
            Offset relative to the contract start date that determines the start
            time for the first commit
        duration:
          $ref: '#/components/schemas/RelativeDate'
          description: >-
            Offset relative to the recurring credit start that determines when
            the contract will stop creating recurring commits. optional
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
                - PERIODS
          description: The amount of time each of the created commits will be valid for
        recurrence_frequency:
          type: string
          enum:
            - MONTHLY
            - QUARTERLY
            - ANNUAL
            - WEEKLY
            - DAILY
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
            - FIRST
            - LAST
            - FIRST_AND_LAST
          description: >-
            Determines whether the first and last commit will be prorated.  If
            not provided, the default is FIRST_AND_LAST (i.e. prorate both the
            first and last commits).
        subscription_config:
          $ref: '#/components/schemas/RecurringCommitSubscriptionConfigTemplate'
          description: Attach a subscription to the recurring commit/credit.
    ProrationRoundingConfig:
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
            (e.g., -2 rounds to nearest 100 in the stored unit. For USD, this
            means rounding to the nearest dollar).
    SpendThresholdCommit:
      type: object
      allOf:
        - $ref: '#/components/schemas/BaseThresholdCommit'
    PaymentGateConfig:
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
          description: Only applicable if using STRIPE as your payment gate type.
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
    PrepaidBalanceThresholdCommit:
      type: object
      allOf:
        - $ref: '#/components/schemas/BaseThresholdCommit'
        - type: object
          properties:
            applicable_product_ids:
              type: array
              items:
                type: string
                format: uuid
              description: >-
                Which products the threshold commit applies to. If
                applicable_product_ids, applicable_product_tags or specifiers
                are not provided, the commit applies to all products.
            applicable_product_tags:
              type: array
              items:
                type: string
              description: >-
                Which tags the threshold commit applies to. If
                applicable_product_ids, applicable_product_tags or specifiers
                are not provided, the commit applies to all products.
            specifiers:
              x-mint:
                groups:
                  - ff:commit-specifiers
              type: array
              description: >-
                List of filters that determine what kind of customer usage draws
                down a commit or credit. A customer's usage needs to meet the
                condition of at least one of the specifiers to contribute to a
                commit's or credit's drawdown. This field cannot be used
                together with `applicable_product_ids` or
                `applicable_product_tags`.
              items:
                $ref: '#/components/schemas/CommitSpecifierInput'
    ThresholdBalanceSpecifier:
      type: object
      required:
        - exclude
      properties:
        exclude:
          type: array
          description: >-
            If any of the exclude specifier is met, the balance is not
            considered when evaluating threshold billing
          items:
            $ref: '#/components/schemas/ExcludeThresholdBalanceSpecifier'
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
    SubscriptionProration:
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
          $ref: '#/components/schemas/ProrationRoundingConfig'
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
    SubscriptionBillingCycleConfigTemplate:
      type: object
      properties:
        invoice_placement:
          type: string
          enum:
            - ON_SCHEDULED_INVOICE
            - ON_USAGE_INVOICE
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
    RecurringCommitSubscriptionConfigTemplate:
      type: object
      required:
        - allocation
        - apply_seat_increase_config
        - subscription_template_id
      properties:
        allocation:
          $ref: '#/components/schemas/SubscriptionConfigAllocation'
        apply_seat_increase_config:
          $ref: '#/components/schemas/ApplySeatIncreaseConfigForRecurringCommit'
        subscription_template_id:
          type: string
          format: uuid
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
    ExcludeThresholdBalanceSpecifier:
      type: object
      required:
        - custom_field_filters
      properties:
        custom_field_filters:
          type: array
          description: >-
            If provided, balances with all the custom fields will not be
            considered when evaluating threshold billing
          items:
            $ref: '#/components/schemas/BalanceCustomFieldFilterType'
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
