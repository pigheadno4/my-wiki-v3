<!-- Source URL: https://docs.metronome.com/api-reference/contracts/create-a-package.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a package

> Create a package that defines a set of reusable, time-relative contract terms that can be used across cohorts of customers. Packages provide an abstraction layer on top of rate cards to provide an easy way to provision customers with standard pricing. 

### **Use this endpoint to:**
- Model standard pay-as-you-go pricing packages that can be easily reused across customers
- Define standardized contract terms and discounting for sales-led motions
- Set aliases for the package to facilitate easy package transition. Aliases are human-readable names that you can use in the place of the id of the package when provisioning a customer’s contract. By using an alias, you can easily create a contract and provision a customer by choosing the “Starter Plan” package, without storing the package ID in your internal systems. This is helpful when launching terms for a package, as you can create a new package with the “Starter Plan” alias scheduled to be assigned without updating your provisioning code.

### Key input fields:
- `starting_at_offset`: Starting date relative to contract start. Generates the `starting_at` date when a contract is provisioned using a package.
- `duration`: Duration starting from `starting_at_offset`. Generates the `ending_before` date when a contract is provisioned using a package.
- `date_offset`: Date relative to contract start. Used for point-in-time dates without a duration.
- `aliases`: Human-readable name to use when provisioning contracts with a package.

### Usage guidelines:
- Use packages for standard self-serve use cases where customers have consistent terms. For customers with negotiated custom contract terms, use the `createContract` endpoint for maximum flexibility.
- Billing provider configuration can be set when creating a package by using `billing_provider` and `delivery_method`. To provision a customer successfully with a package, the customer must have one and only one billing provider configuration that matches the billing provider configuration set on the package.
- A package alias can only be used by one package at a time. If you create a new package with an alias that is already in use by another package, the original package’s alias schedule will be updated. The alias will reference the package to which it was most recently assigned.
- Terms can only be specified using times relative to the contract start date. Supported granularities are: `days`, `weeks`, `months`, `years`
- Packages cannot be edited once created. Use the rate card to easily add new rates across all of your customers or make direct edits to a contract after provisioning with a package. Edited contracts will still be associated with the package used during provisioning.




## OpenAPI

````yaml /openapi.json post /v1/packages/create
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
  /v1/packages/create:
    post:
      tags:
        - Contracts
      summary: Create a package
      description: >
        Create a package that defines a set of reusable, time-relative contract
        terms that can be used across cohorts of customers. Packages provide an
        abstraction layer on top of rate cards to provide an easy way to
        provision customers with standard pricing. 


        ### **Use this endpoint to:**

        - Model standard pay-as-you-go pricing packages that can be easily
        reused across customers

        - Define standardized contract terms and discounting for sales-led
        motions

        - Set aliases for the package to facilitate easy package transition.
        Aliases are human-readable names that you can use in the place of the id
        of the package when provisioning a customer’s contract. By using an
        alias, you can easily create a contract and provision a customer by
        choosing the “Starter Plan” package, without storing the package ID in
        your internal systems. This is helpful when launching terms for a
        package, as you can create a new package with the “Starter Plan” alias
        scheduled to be assigned without updating your provisioning code.


        ### Key input fields:

        - `starting_at_offset`: Starting date relative to contract start.
        Generates the `starting_at` date when a contract is provisioned using a
        package.

        - `duration`: Duration starting from `starting_at_offset`. Generates the
        `ending_before` date when a contract is provisioned using a package.

        - `date_offset`: Date relative to contract start. Used for point-in-time
        dates without a duration.

        - `aliases`: Human-readable name to use when provisioning contracts with
        a package.


        ### Usage guidelines:

        - Use packages for standard self-serve use cases where customers have
        consistent terms. For customers with negotiated custom contract terms,
        use the `createContract` endpoint for maximum flexibility.

        - Billing provider configuration can be set when creating a package by
        using `billing_provider` and `delivery_method`. To provision a customer
        successfully with a package, the customer must have one and only one
        billing provider configuration that matches the billing provider
        configuration set on the package.

        - A package alias can only be used by one package at a time. If you
        create a new package with an alias that is already in use by another
        package, the original package’s alias schedule will be updated. The
        alias will reference the package to which it was most recently assigned.

        - Terms can only be specified using times relative to the contract start
        date. Supported granularities are: `days`, `weeks`, `months`, `years`

        - Packages cannot be edited once created. Use the rate card to easily
        add new rates across all of your customers or make direct edits to a
        contract after provisioning with a package. Edited contracts will still
        be associated with the package used during provisioning.
      operationId: createPackage-v1
      requestBody:
        description: Create a new package
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreatePackagePayload'
            example:
              name: My package
              rate_card_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
              billing_provider: stripe
              delivery_method: direct_to_billing_provider
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
                  id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '404':
          $ref: '#/components/responses/NotFound'
components:
  schemas:
    CreatePackagePayload:
      type: object
      required:
        - name
      properties:
        name:
          type: string
        contract_name:
          type: string
        uniqueness_key:
          $ref: '#/components/schemas/UniquenessKey'
        net_payment_terms_days:
          type: number
        rate_card_id:
          type: string
          format: uuid
        rate_card_alias:
          type: string
          description: >-
            Selects the rate card linked to the specified alias as of the
            contract's start date.
        aliases:
          type: array
          items:
            $ref: '#/components/schemas/PackageAlias'
          description: >-
            Reference this alias when creating a contract. If the same alias is
            assigned to multiple packages, it will reference the package to
            which it was most recently assigned. It is not exposed to end
            customers.
        duration:
          $ref: '#/components/schemas/RelativeDate'
        commits:
          type: array
          items:
            $ref: '#/components/schemas/CommitTemplateInput'
        credits:
          type: array
          items:
            $ref: '#/components/schemas/CreditTemplateInput'
        recurring_commits:
          type: array
          items:
            $ref: '#/components/schemas/RecurringCommitTemplateInput'
        recurring_credits:
          type: array
          items:
            $ref: '#/components/schemas/RecurringCreditTemplateInput'
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
            priority value will be prioritized first. If tiered overrides are
            used, prioritization must be explicit.
        overrides:
          type: array
          items:
            $ref: '#/components/schemas/OverrideTemplateInput'
        scheduled_charges:
          type: array
          items:
            $ref: '#/components/schemas/ScheduledChargeTemplateInput'
        scheduled_charges_on_usage_invoices:
          $ref: '#/components/schemas/ScheduledChargesOnUsageInvoices'
        usage_statement_schedule:
          $ref: '#/components/schemas/UsageStatementScheduleTemplateInput'
        billing_provider:
          $ref: '#/components/schemas/ContractsBillingProviderType'
        delivery_method:
          $ref: '#/components/schemas/BillingProviderDeliveryMethodType'
        spend_threshold_configuration:
          $ref: '#/components/schemas/SpendThresholdConfiguration'
        prepaid_balance_threshold_configuration:
          $ref: '#/components/schemas/PrepaidBalanceThresholdConfiguration'
        spend_trackers:
          type: array
          items:
            $ref: '#/components/schemas/SpendTrackerInput'
          x-mint:
            groups:
              - ff:tb-spend-trackers
        subscriptions:
          type: array
          items:
            $ref: '#/components/schemas/SubscriptionTemplateInput'
    Id:
      required:
        - id
      type: object
      properties:
        id:
          type: string
          format: uuid
    Error:
      required:
        - message
      type: object
      properties:
        message:
          type: string
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
    CommitTemplateInput:
      type: object
      required:
        - type
        - product_id
        - access_schedule
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
          $ref: '#/components/schemas/RelativeScheduleDurationInput'
          description: >-
            Required: Schedule for distributing the commit to the customer. For
            "POSTPAID" commits only one schedule item is allowed and amount must
            match invoice_schedule total.
        invoice_schedule:
          allOf:
            - $ref: '#/components/schemas/RelativeSchedulePointInTimeInput'
            - type: object
              properties:
                do_not_invoice:
                  type: boolean
                  description: If true, this schedule will not generate an invoice.
                  default: false
          description: >-
            Required for "POSTPAID" commits: the true up invoice will be
            generated at this time and only one schedule item is allowed; the
            total must match access_schedule amount. Optional for "PREPAID"
            commits: if not provided, this will be a "complimentary" commit with
            no invoice.
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
            with `applicable_product_ids` or `applicable_product_tags`.
          items:
            $ref: '#/components/schemas/CommitSpecifierInput'
        temporary_id:
          type: string
          description: >-
            A temporary ID for the commit that can be used to reference the
            commit for commit specific overrides.
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: package_commit
    CreditTemplateInput:
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
          $ref: '#/components/schemas/RelativeScheduleDurationInput'
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
            with `applicable_product_ids` or `applicable_product_tags`.
          items:
            $ref: '#/components/schemas/CommitSpecifierInput'
        priority:
          type: number
          description: >-
            If multiple credits are applicable, the one with the lower priority
            will apply first.
        rate_type:
          type: string
          enum:
            - COMMIT_RATE
            - commit_rate
            - LIST_RATE
            - list_rate
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: package_credit
    RecurringCommitTemplateInput:
      allOf:
        - $ref: '#/components/schemas/RecurringCommitOrCreditTemplateInputBase'
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
                  $ref: '#/components/schemas/ProrationRoundingConfig'
                invoice:
                  $ref: '#/components/schemas/ProrationRoundingConfig'
    RecurringCreditTemplateInput:
      allOf:
        - $ref: '#/components/schemas/RecurringCommitOrCreditTemplateInputBase'
        - type: object
          properties:
            proration_rounding:
              type: object
              description: >-
                Optional rounding configuration for prorated recurring credit
                amounts.
              properties:
                access:
                  $ref: '#/components/schemas/ProrationRoundingConfig'
    OverrideTemplateInput:
      type: object
      required:
        - starting_at_offset
        - override_specifiers
      properties:
        starting_at_offset:
          $ref: '#/components/schemas/RelativeDate'
          description: >-
            Offset relative to contract start date indicating when the override
            will start applying (inclusive)
        duration:
          $ref: '#/components/schemas/RelativeDate'
          description: >-
            Offset relative to override start indicating when the override will
            stop applying (exclusive)
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
          $ref: '#/components/schemas/OverwriteRateInput'
          description: Required for OVERWRITE type.
        override_specifiers:
          type: array
          items:
            $ref: '#/components/schemas/OverrideSpecifierInput'
          description: Specifies which products the override will apply to.
        tiers:
          type: array
          items:
            $ref: '#/components/schemas/OverrideTierInput'
          description: Required for TIERED type. Must have at least one tier.
        is_commit_specific:
          type: boolean
          description: >-
            Indicates whether the override should only apply to commits.
            Defaults to `false`. If `true` you can specify relevant commits in
            `override_specifiers` by passing `commit_ids`,
            `recurring_commit_ids`, or `any_commit_or_credit_ids`.  If you do
            not specify any of these fields, the override will apply when
            consuming any prepaid commit, postpaid commit, or credit
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
    ScheduledChargeTemplateInput:
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
          $ref: '#/components/schemas/RelativeSchedulePointInTimeInput'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: package_scheduled_charge
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
    UsageStatementScheduleTemplateInput:
      type: object
      required:
        - frequency
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
        day:
          type: string
          description: If not provided, defaults to the first day of the month.
          enum:
            - FIRST_OF_MONTH
            - first_of_month
            - CONTRACT_START
            - contract_start
        invoice_generation_starting_at_offset:
          $ref: '#/components/schemas/RelativeDate'
          description: >-
            The offset at which Metronome should start generating usage
            invoices, relative to the contract start date.  If unspecified,
            contract start date will be used. This is useful to set if you want
            to import historical invoices via our 'Create Historical Invoices'
            API rather than having Metronome automatically generate them.
    ContractsBillingProviderType:
      type: string
      enum:
        - aws_marketplace
        - azure_marketplace
        - gcp_marketplace
        - stripe
        - netsuite
    BillingProviderDeliveryMethodType:
      type: string
      enum:
        - direct_to_billing_provider
        - aws_sqs
        - tackle
        - aws_sns
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
    SubscriptionTemplateInput:
      type: object
      required:
        - subscription_rate
        - collection_schedule
        - proration
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
          $ref: '#/components/schemas/SubscriptionProrationInput'
        initial_quantity:
          type: number
          description: >-
            The initial quantity for the subscription. It must be non-negative
            value. Required if quantity_management_mode is QUANTITY_ONLY.
        starting_at_offset:
          $ref: '#/components/schemas/RelativeDate'
          description: >-
            Relative date from contract start date corresponding to the
            inclusive start time for the subscription. If not provided, defaults
            to contract start date
        duration:
          $ref: '#/components/schemas/RelativeDate'
          description: >-
            Lifetime of the subscription from its start. If not provided,
            subscription inherits contract end date.
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
          $ref: '#/components/schemas/SubscriptionSeatConfigTemplateInput'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: package_subscription
        billing_cycle_config:
          $ref: '#/components/schemas/SubscriptionBillingCycleConfigTemplateInput'
    RelativeScheduleDurationInput:
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
          description: Defaults to USD (cents) if not passed
        schedule_items:
          type: array
          items:
            type: object
            required:
              - amount
              - starting_at_offset
              - duration
            properties:
              amount:
                type: number
              starting_at_offset:
                $ref: '#/components/schemas/RelativeDate'
                description: >-
                  Date relative to the contract start date indicating the start
                  of this schedule segment.
              duration:
                $ref: '#/components/schemas/RelativeDate'
                description: >-
                  Offset relative to the start of this segment indicating when
                  it should end.
    RelativeSchedulePointInTimeInput:
      type: object
      description: Must provide schedule_items.
      required:
        - schedule_items
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
              - unit_price
              - quantity
              - date_offset
            properties:
              unit_price:
                type: number
                description: >-
                  Unit price for the charge. Will be multiplied by quantity to
                  determine the amount.
              quantity:
                type: number
                description: >-
                  Quantity for the charge. Will be multiplied by unit_price to
                  determine the amount.
              date_offset:
                $ref: '#/components/schemas/RelativeDate'
                description: Date relative to the contract start date.
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
    RecurringCommitOrCreditTemplateInputBase:
      type: object
      required:
        - product_id
        - access_amount
        - priority
        - commit_duration
        - starting_at_offset
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
            with `applicable_product_ids` or `applicable_product_tags`.
          items:
            $ref: '#/components/schemas/CommitSpecifierInput'
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
            Determines whether the first and last commit will be prorated.  If
            not provided, the default is FIRST_AND_LAST (i.e. prorate both the
            first and last commits).
        subscription_config:
          $ref: '#/components/schemas/RecurringCommitSubscriptionConfigInput'
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
    OverwriteRateInput:
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
        credit_type_id:
          type: string
          format: uuid
    OverrideSpecifierInput:
      type: object
      properties:
        commit_ids:
          type: array
          items:
            type: string
          description: >-
            Can only be used for commit specific overrides. Must be used in
            conjunction with one of `product_id`, `product_tags`,
            `pricing_group_values`, or `presentation_group_values`. If provided,
            the override will only apply to the specified commits. If not
            provided, the override will apply to all commits.
        recurring_commit_ids:
          type: array
          items:
            type: string
          description: >-
            Can only be used for commit specific overrides. Must be used in
            conjunction with one of `product_id`, `product_tags`,
            `pricing_group_values`, or `presentation_group_values`. If provided,
            the override will only apply to commits created by the specified
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
            items with the specified presentation group values.
          additionalProperties:
            type: string
        billing_frequency:
          type: string
          enum:
            - MONTHLY
            - QUARTERLY
            - ANNUAL
            - monthly
            - quarterly
            - annual
            - WEEKLY
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
            duration:
              $ref: '#/components/schemas/RelativeDate'
              description: >-
                The length of time the created commit will be valid, starting
                from the end of the invoice's service period. If not provided,
                defaults to one year.
            rollover_fraction:
              type: number
              description: >-
                Fraction of the created commit's unused balance that will roll
                over. Must be between 0 and 1.
            rate_type:
              type: string
              enum:
                - COMMIT_RATE
                - commit_rate
                - LIST_RATE
                - list_rate
              description: >-
                Whether the created commits will be charged at commit rate or
                list rate.
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
    SubscriptionProrationInput:
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
          $ref: '#/components/schemas/ProrationRoundingConfig'
    SubscriptionSeatConfigTemplateInput:
      type: object
      required:
        - seat_group_key
      properties:
        seat_group_key:
          type: string
          description: >-
            The property name, sent on usage events, that identifies the seat ID
            associated with the usage event. For example, the property name
            might be seat_id or user_id. The property must be set as a group key
            on billable metrics and a presentation/pricing group key on contract
            products. This allows linked recurring credits with an allocation
            per seat to be consumed by only one seat's usage.
        initial_unassigned_seats:
          type: number
          description: The initial amount of unassigned seats on this subscription.
    SubscriptionBillingCycleConfigTemplateInput:
      type: object
      properties:
        invoice_placement:
          type: string
          enum:
            - ON_SCHEDULED_INVOICE
            - ON_USAGE_INVOICE
            - on_scheduled_invoice
            - on_usage_invoice
          description: >-
            Controls whether subscriptions consolidate onto usage invoices.
            Defaults to ON_USAGE_INVOICE if omitted.
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
    RecurringCommitSubscriptionConfigInput:
      type: object
      required:
        - apply_seat_increase_config
        - subscription_id
      properties:
        allocation:
          $ref: '#/components/schemas/SubscriptionConfigAllocationInput'
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
            balances when the subscription is payment-gated.
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
    SubscriptionConfigAllocationInput:
      type: string
      enum:
        - INDIVIDUAL
        - POOLED
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
