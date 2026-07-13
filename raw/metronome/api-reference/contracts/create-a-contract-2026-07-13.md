<!-- Source URL: https://docs.metronome.com/api-reference/contracts/create-a-contract.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a contract

> Contracts define a customer's products, pricing, discounts, access duration, and billing configuration. Contracts serve as the central billing agreement for both PLG and Enterprise customers. You can automatically grant customers access to your products and services directly from your product or CRM.

### Use this endpoint to:
- PLG onboarding: Automatically provision new self-serve customers with contracts when they sign up.
- Enterprise sales: Push negotiated contracts from Salesforce with custom pricing and commitments
- Promotional pricing: Implement time-limited discounts and free trials through overrides

### Key components:
#### Contract Term and Billing Schedule
- Set contract duration using `starting_at` and `ending_before` fields. PLG contracts typically use perpetual agreements (no end date), while Enterprise contracts have fixed end dates which can be edited over time in the case of co-term upsells.

#### Rate Card
If you are offering usage based pricing, you can set a rate card for the contract to reference through `rate_card_id` or `rate_card_alias`. The rate card is a store of all of your usage based products and their centralized pricing. Any new products or price changes on the rate card can be set to automatically propagate to all associated contracts - this ensures consistent pricing and product launches flow to contracts without manual updates and migrations. The `usage_statement_schedule` determines the cadence on which Metronome will finalize a usage invoice for the customer. This defaults to monthly on the 1st, with options for custom dates, quarterly, or annual cadences. Note: Most usage based billing companies align usage statements to be evaluated aligned to the first of the month.
Read more about [Rate Cards](https://docs.metronome.com/pricing-packaging/create-manage-rate-cards/).

#### Overrides and discounts
Customize pricing on the contract through time-bounded overrides that can target specific products, product families, or complex usage scenarios. Overrides enable two key capabilities:
- Discounts: Apply percentage discounts, fixed rate reductions, or quantity-based pricing tiers
- Entitlements: Provide special pricing or access to specific products for negotiated deals

Read more about [Contract Overrides](https://docs.metronome.com/manage-product-access/add-contract-override/).

#### Commits and Credits
Using commits, configure prepaid or postpaid spending commitments where customers promise to spend a certain amount over the contract period paid in advance or in arrears. Use credits to provide free spending allowances. Under the hood these are the same mechanisms, however, credits are typically offered for free (SLA or promotional) or as a part of an allotment associated with a Subscription.

In Metronome, you can set commits and credits to only be applicable for a subset of usage. Use `applicable_product_ids` or `applicable_product_tags` to create product or product-family specific commits or credits, or you can build complex boolean logic specifiers to target usage based on pricing  and presentation group values using `override_specifiers`.

These objects can also also be configured to have a recurrence schedule to easily model customer packaging which includes recurring monthly or quarterly allotments.

Commits support rollover settings (`rollover_fraction`) to transfer unused balances between contract periods, either entirely or as a percentage.

Read more about [Credits and Commits](https://docs.metronome.com/pricing-packaging/apply-credits-commits/).

#### Subscriptions
You can add a fixed recurring charge to a contract, like monthly licenses or seat-based fees, using the subscription charge. Subscription charges are defined on your rate card and you can select which subscription is applicable to add to each contract.         When you add a subscription to a contract you need to:
- Define whether the subscription is paid for in-advance or in-arrears (`collection_schedule`)
- Define the proration behavior (`proration`)
- Specify an initial quantity (`initial_quantity`)
- Define which subscription rate on the rate card should be used (`subscription_rate`)

Read more about [Subscriptions](https://docs.metronome.com/manage-product-access/create-subscription/).

#### Scheduled Charges
Set up one-time, recurring, or entirely custom charges that occur on specific dates, separate from usage-based billing or commitments. These can be used to model non-recurring platform charges or professional services.

#### Threshold Billing
Metronome allows you to configure automatic billing triggers when customers reach spending thresholds to prevent fraud and manage risk. You can use `spend_threshold_configuration` to trigger an invoice to cover current charges whenever the threshold is reached or you can ensure the customer maintains a minimum prepaid balance using the `prepaid_balance_configuration`.

Read more about [Spend Threshold](https://docs.metronome.com/manage-product-access/spend-thresholds/) and [Prepaid Balance Thresholds](https://docs.metronome.com/manage-product-access/prepaid-balance-thresholds/).

### Usage guidelines:
- You can always [Edit Contracts](https://docs.metronome.com/manage-product-access/edit-contract/) after it has been created, using the `editContract` endpoint. Metronome keeps track of all edits, both in the audit log and over the `getEditHistory` endpoint.
- Customers in Metronome can have multiple concurrent contracts at one time. Use `usage_filters` to route the correct usage to each contract. [Read more about usage filters](https://docs.metronome.com/manage-product-access/provision-customer/#create-a-usage-filter).




## OpenAPI

````yaml /openapi.json post /v1/contracts/create
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
  /v1/contracts/create:
    post:
      tags:
        - Contracts
      summary: Create a contract
      description: >
        Contracts define a customer's products, pricing, discounts, access
        duration, and billing configuration. Contracts serve as the central
        billing agreement for both PLG and Enterprise customers. You can
        automatically grant customers access to your products and services
        directly from your product or CRM.


        ### Use this endpoint to:

        - PLG onboarding: Automatically provision new self-serve customers with
        contracts when they sign up.

        - Enterprise sales: Push negotiated contracts from Salesforce with
        custom pricing and commitments

        - Promotional pricing: Implement time-limited discounts and free trials
        through overrides


        ### Key components:

        #### Contract Term and Billing Schedule

        - Set contract duration using `starting_at` and `ending_before` fields.
        PLG contracts typically use perpetual agreements (no end date), while
        Enterprise contracts have fixed end dates which can be edited over time
        in the case of co-term upsells.


        #### Rate Card

        If you are offering usage based pricing, you can set a rate card for the
        contract to reference through `rate_card_id` or `rate_card_alias`. The
        rate card is a store of all of your usage based products and their
        centralized pricing. Any new products or price changes on the rate card
        can be set to automatically propagate to all associated contracts - this
        ensures consistent pricing and product launches flow to contracts
        without manual updates and migrations. The `usage_statement_schedule`
        determines the cadence on which Metronome will finalize a usage invoice
        for the customer. This defaults to monthly on the 1st, with options for
        custom dates, quarterly, or annual cadences. Note: Most usage based
        billing companies align usage statements to be evaluated aligned to the
        first of the month.

        Read more about [Rate
        Cards](https://docs.metronome.com/pricing-packaging/create-manage-rate-cards/).


        #### Overrides and discounts

        Customize pricing on the contract through time-bounded overrides that
        can target specific products, product families, or complex usage
        scenarios. Overrides enable two key capabilities:

        - Discounts: Apply percentage discounts, fixed rate reductions, or
        quantity-based pricing tiers

        - Entitlements: Provide special pricing or access to specific products
        for negotiated deals


        Read more about [Contract
        Overrides](https://docs.metronome.com/manage-product-access/add-contract-override/).


        #### Commits and Credits

        Using commits, configure prepaid or postpaid spending commitments where
        customers promise to spend a certain amount over the contract period
        paid in advance or in arrears. Use credits to provide free spending
        allowances. Under the hood these are the same mechanisms, however,
        credits are typically offered for free (SLA or promotional) or as a part
        of an allotment associated with a Subscription.


        In Metronome, you can set commits and credits to only be applicable for
        a subset of usage. Use `applicable_product_ids` or
        `applicable_product_tags` to create product or product-family specific
        commits or credits, or you can build complex boolean logic specifiers to
        target usage based on pricing  and presentation group values using
        `override_specifiers`.


        These objects can also also be configured to have a recurrence schedule
        to easily model customer packaging which includes recurring monthly or
        quarterly allotments.


        Commits support rollover settings (`rollover_fraction`) to transfer
        unused balances between contract periods, either entirely or as a
        percentage.


        Read more about [Credits and
        Commits](https://docs.metronome.com/pricing-packaging/apply-credits-commits/).


        #### Subscriptions

        You can add a fixed recurring charge to a contract, like monthly
        licenses or seat-based fees, using the subscription charge. Subscription
        charges are defined on your rate card and you can select which
        subscription is applicable to add to each contract.         When you add
        a subscription to a contract you need to:

        - Define whether the subscription is paid for in-advance or in-arrears
        (`collection_schedule`)

        - Define the proration behavior (`proration`)

        - Specify an initial quantity (`initial_quantity`)

        - Define which subscription rate on the rate card should be used
        (`subscription_rate`)


        Read more about
        [Subscriptions](https://docs.metronome.com/manage-product-access/create-subscription/).


        #### Scheduled Charges

        Set up one-time, recurring, or entirely custom charges that occur on
        specific dates, separate from usage-based billing or commitments. These
        can be used to model non-recurring platform charges or professional
        services.


        #### Threshold Billing

        Metronome allows you to configure automatic billing triggers when
        customers reach spending thresholds to prevent fraud and manage risk.
        You can use `spend_threshold_configuration` to trigger an invoice to
        cover current charges whenever the threshold is reached or you can
        ensure the customer maintains a minimum prepaid balance using the
        `prepaid_balance_configuration`.


        Read more about [Spend
        Threshold](https://docs.metronome.com/manage-product-access/spend-thresholds/)
        and [Prepaid Balance
        Thresholds](https://docs.metronome.com/manage-product-access/prepaid-balance-thresholds/).


        ### Usage guidelines:

        - You can always [Edit
        Contracts](https://docs.metronome.com/manage-product-access/edit-contract/)
        after it has been created, using the `editContract` endpoint. Metronome
        keeps track of all edits, both in the audit log and over the
        `getEditHistory` endpoint.

        - Customers in Metronome can have multiple concurrent contracts at one
        time. Use `usage_filters` to route the correct usage to each contract.
        [Read more about usage
        filters](https://docs.metronome.com/manage-product-access/provision-customer/#create-a-usage-filter).
      operationId: createContract-v1
      requestBody:
        description: Create a new contract
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateContractPayload'
            example:
              customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
              rate_card_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
              starting_at: '2020-01-01T00:00:00.000Z'
              billing_provider_configuration:
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
                    $ref: '#/components/schemas/CreateContractResponse'
              example:
                data:
                  id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                  contract:
                    id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                    customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
                    starting_at: '2020-01-01T00:00:00.000Z'
                    commits: []
                    credits: []
                    overrides: []
                    scheduled_charges: []
                    transitions: []
                    subscriptions: []
                    recurring_commits: []
                    recurring_credits: []
                    created_at: '2020-01-01T00:00:00.000Z'
                    created_by: system
                    usage_statement_schedule:
                      frequency: MONTHLY
                      billing_anchor_date: '2020-01-01T00:00:00.000Z'
                    usage_filter: []
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
    CreateContractPayload:
      type: object
      required:
        - customer_id
        - starting_at
      properties:
        customer_id:
          type: string
          format: uuid
        package_id:
          type: string
          format: uuid
          description: >-
            If provided, provisions a customer on a package instead of creating
            a traditional contract. When specified, only customer_id,
            starting_at, package_id, uniqueness_key, transition, and
            custom_fields are allowed.
        package_alias:
          type: string
          description: >-
            Selects the package linked to the specified alias as of the
            contract's start date. Mutually exclusive with package_id.
        name:
          type: string
        uniqueness_key:
          $ref: '#/components/schemas/UniquenessKey'
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
        total_contract_value:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: number
          description: >-
            This field's availability is dependent on your client's
            configuration.
        starting_at:
          type: string
          format: date-time
          description: inclusive contract start time
        ending_before:
          type: string
          format: date-time
          description: exclusive contract end time
        commits:
          type: array
          items:
            $ref: '#/components/schemas/CommitInput'
        credits:
          type: array
          items:
            $ref: '#/components/schemas/CreditInput'
        recurring_commits:
          type: array
          items:
            $ref: '#/components/schemas/RecurringCommitInput'
        recurring_credits:
          type: array
          items:
            $ref: '#/components/schemas/RecurringCreditInput'
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
            $ref: '#/components/schemas/OverrideInput'
        discounts:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: array
          description: >-
            This field's availability is dependent on your client's
            configuration.
          items:
            $ref: '#/components/schemas/DiscountInput'
        professional_services:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: array
          description: >-
            This field's availability is dependent on your client's
            configuration.
          items:
            $ref: '#/components/schemas/ProServiceInput'
        reseller_royalties:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: array
          description: >-
            This field's availability is dependent on your client's
            configuration.
          items:
            $ref: '#/components/schemas/ResellerRoyaltyInput'
        scheduled_charges:
          type: array
          items:
            $ref: '#/components/schemas/ScheduledChargeInput'
        scheduled_charges_on_usage_invoices:
          $ref: '#/components/schemas/ScheduledChargesOnUsageInvoices'
        transition:
          $ref: '#/components/schemas/ContractTransitionInput'
        usage_filter:
          $ref: '#/components/schemas/BaseUsageFilter'
        usage_statement_schedule:
          $ref: '#/components/schemas/UsageStatementScheduleInput'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: contract
        billing_provider_configuration:
          $ref: '#/components/schemas/CustomerBillingProviderConfigurationLookup'
        revenue_system_configuration:
          $ref: '#/components/schemas/CustomerRevenueSystemConfigurationLookup'
          x-mint:
            groups:
              - ff:revenue-rec-configurations-enabled
        spend_threshold_configuration:
          $ref: '#/components/schemas/SpendThresholdConfiguration'
        prepaid_balance_threshold_configuration:
          $ref: '#/components/schemas/PrepaidBalanceThresholdConfiguration'
        spend_trackers:
          x-mint:
            groups:
              - ff:tb-spend-trackers
          type: array
          items:
            $ref: '#/components/schemas/SpendTrackerInput'
          description: >-
            Spend trackers to attach to this contract. Aliases must be unique
            within a contract.
        subscriptions:
          $ref: '#/components/schemas/SubscriptionsInput'
        hierarchy_configuration:
          $ref: '#/components/schemas/ContractHierarchyConfigurationInput'
    CreateContractResponse:
      type: object
      required:
        - id
      properties:
        id:
          type: string
          format: uuid
        contract:
          type: object
          description: The created contract.
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
            created_at:
              type: string
              format: date-time
            created_by:
              type: string
            name:
              type: string
            package_id:
              type: string
              format: uuid
              description: ID of the package this contract was created from, if applicable.
            uniqueness_key:
              $ref: '#/components/schemas/UniquenessKey'
              description: Optional uniqueness key to prevent duplicate contract creations.
            rate_card_id:
              type: string
              format: uuid
            starting_at:
              type: string
              format: date-time
            ending_before:
              type: string
              format: date-time
            net_payment_terms_days:
              type: number
            multiplier_override_prioritization:
              type: string
              enum:
                - LOWEST_MULTIPLIER
                - lowest_multiplier
                - EXPLICIT
                - explicit
              description: >-
                Defaults to LOWEST_MULTIPLIER, which applies the greatest
                discount to list prices automatically. EXPLICIT prioritization
                requires specifying priorities for each multiplier; the one with
                the lowest priority value will be prioritized first.
            scheduled_charges_on_usage_invoices:
              $ref: '#/components/schemas/ScheduledChargesOnUsageInvoices'
            custom_fields:
              $ref: '#/components/schemas/CustomField'
              x-cf-entity: contract
            usage_statement_schedule:
              $ref: '#/components/schemas/UsageStatementSchedule'
            usage_filter:
              type: array
              items:
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
                    type: string
                    format: date-time
                  ending_before:
                    type: string
                    format: date-time
            commits:
              type: array
              items:
                $ref: '#/components/schemas/Commit'
            credits:
              type: array
              items:
                $ref: '#/components/schemas/Credit'
            has_more:
              $ref: '#/components/schemas/HasMore'
            recurring_commits:
              type: array
              items:
                $ref: '#/components/schemas/RecurringCommit'
            recurring_credits:
              type: array
              items:
                $ref: '#/components/schemas/RecurringCredit'
            overrides:
              type: array
              items:
                $ref: '#/components/schemas/Override'
            scheduled_charges:
              type: array
              items:
                $ref: '#/components/schemas/ScheduledCharge'
            transitions:
              type: array
              items:
                $ref: '#/components/schemas/ContractTransition'
            subscriptions:
              $ref: '#/components/schemas/Subscriptions'
            customer_billing_provider_configuration:
              $ref: '#/components/schemas/CustomerBillingProviderConfiguration'
            spend_threshold_configuration:
              $ref: '#/components/schemas/SpendThresholdConfiguration'
            prepaid_balance_threshold_configuration:
              $ref: '#/components/schemas/PrepaidBalanceThresholdConfiguration'
            hierarchy_configuration:
              $ref: '#/components/schemas/HierarchyConfiguration'
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
    CommitInput:
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
          $ref: '#/components/schemas/ScheduleDurationInput'
          description: >-
            Required: Schedule for distributing the commit to the customer. For
            "POSTPAID" commits only one schedule item is allowed and amount must
            match invoice_schedule total.
        invoice_schedule:
          $ref: '#/components/schemas/SchedulePointInTimeInput'
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
            with `applicable_product_ids` or `applicable_product_tags`.
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
    CreditInput:
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
          $ref: '#/components/schemas/ScheduleDurationInput'
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
    RecurringCommitInput:
      allOf:
        - $ref: '#/components/schemas/RecurringCommitOrCreditInputBase'
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
    RecurringCreditInput:
      allOf:
        - $ref: '#/components/schemas/RecurringCommitOrCreditInputBase'
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
    OverrideInput:
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
          $ref: '#/components/schemas/OverwriteRateInput'
          description: Required for OVERWRITE type.
        product_id:
          type: string
          format: uuid
          description: >-
            ID of the product whose rate is being overridden. Cannot be used in
            conjunction with override_specifiers.
        applicable_product_tags:
          type: array
          items:
            type: string
          description: >-
            tags identifying products whose rates are being overridden. Cannot
            be used in conjunction with override_specifiers.
        override_specifiers:
          type: array
          items:
            $ref: '#/components/schemas/OverrideSpecifierInput'
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
    DiscountInput:
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
          $ref: '#/components/schemas/SchedulePointInTimeInput'
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
    ResellerRoyaltyInput:
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
          type: string
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
    ScheduledChargeInput:
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
          $ref: '#/components/schemas/SchedulePointInTimeInput'
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
    ContractTransitionInput:
      type: object
      required:
        - type
        - from_contract_id
      properties:
        type:
          type: string
          enum:
            - RENEWAL
            - renewal
          description: >-
            This field's available values may vary based on your client's
            configuration.
        from_contract_id:
          type: string
          format: uuid
        future_invoice_behavior:
          type: object
          properties:
            trueup:
              type: string
              enum:
                - remove
                - as_is
                - REMOVE
                - AS_IS
              nullable: true
              description: >-
                Controls whether future trueup invoices are billed or removed.
                Default behavior is AS_IS if not specified.
    BaseUsageFilter:
      type: object
      required:
        - group_key
        - group_values
      properties:
        group_key:
          type: string
        group_values:
          type: array
          items:
            type: string
        starting_at:
          type: string
          format: date-time
    UsageStatementScheduleInput:
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
            - CUSTOM_DATE
            - custom_date
        billing_anchor_date:
          type: string
          format: date-time
          description: >-
            Required when using CUSTOM_DATE. This option lets you set a
            historical billing anchor date, aligning future billing cycles with
            a chosen cadence. For example, if a contract starts on 2024-09-15
            and you set the anchor date to 2024-09-10 with a MONTHLY frequency,
            the first usage statement will cover 09-15 to 10-10. Subsequent
            statements will follow the 10th of each month.
        invoice_generation_starting_at:
          type: string
          format: date-time
          description: >-
            The date Metronome should start generating usage invoices. If
            unspecified, contract start date will be used. This is useful to set
            if you want to import historical invoices via our 'Create Historical
            Invoices' API rather than having Metronome automatically generate
            them.
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
    CustomerBillingProviderConfigurationLookup:
      type: object
      description: >-
        The billing provider configuration associated with a contract. Provide
        either an ID or the provider and delivery method.
      properties:
        billing_provider_configuration_id:
          type: string
          format: uuid
          description: >-
            The Metronome ID of the billing provider configuration. Use when a
            customer has multiple configurations with the same billing provider
            and delivery method. Otherwise, specify the billing_provider and
            delivery_method.
        billing_provider:
          $ref: '#/components/schemas/ContractsBillingProviderType'
          description: Do not specify if using billing_provider_configuration_id.
        delivery_method:
          $ref: '#/components/schemas/BillingProviderDeliveryMethodType'
          description: Do not specify if using billing_provider_configuration_id.
    CustomerRevenueSystemConfigurationLookup:
      x-mint:
        groups:
          - ff:revenue-rec-configurations-enabled
      type: object
      description: >-
        The revenue system configuration associated with a contract. Provide
        either an ID or the provider and delivery method.
      properties:
        revenue_system_configuration_id:
          type: string
          format: uuid
          description: >-
            The Metronome ID of the revenue system configuration. Use when a
            customer has multiple configurations with the same provider and
            delivery method. Otherwise, specify the provider and
            delivery_method.
        provider:
          $ref: '#/components/schemas/RevenueSystemProviderType'
          description: >-
            The system that is providing services for revenue recognition. Do
            not specify if using revenue_system_configuration_id.
        delivery_method:
          $ref: '#/components/schemas/RevenueSystemDeliveryMethodType'
          description: >-
            How revenue recognition records should be delivered to the revenue
            system. Do not specify if using revenue_system_configuration_id.
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
    SubscriptionsInput:
      type: array
      description: >-
        Optional list of
        [subscriptions](https://docs.metronome.com/manage-product-access/create-subscription/)
        to add to the contract.
      items:
        $ref: '#/components/schemas/SubscriptionInput'
    ContractHierarchyConfigurationInput:
      type: object
      properties:
        parent:
          $ref: '#/components/schemas/ContractParentHierarchyConfigurationInput'
        payer:
          type: string
          enum:
            - SELF
            - PARENT
            - self
            - parent
          description: |-
            Indicates which customer should pay for the child's invoice charges

            **SELF**: The child pays for its own invoice charges

            **PARENT**: The parent pays for the child's invoice charges
        usage_statement_behavior:
          type: string
          enum:
            - CONSOLIDATE
            - SEPARATE
            - consolidate
            - separate
          description: >-
            Indicates the behavior of the child's invoice statements on the
            parent's invoices.


            **CONSOLIDATE**: Child's invoice statements will be added to
            parent's consolidated invoices


            **SEPARATE**: Child's invoice statements will appear not appear on
            parent's consolidated invoices
        parent_behavior:
          type: object
          properties:
            invoice_consolidation_type:
              type: string
              enum:
                - CONCATENATE
                - NONE
                - concatenate
                - none
              description: >-
                Indicates the desired behavior of consolidated invoices
                generated by the parent in a customer hierarchy


                **CONCATENATE**: Statements on the invoices of child customers
                will be appended to the consolidated invoice


                **NONE**: Do not generate consolidated invoices
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
    RecurringCommit:
      allOf:
        - $ref: '#/components/schemas/RecurringCommitOrCreditBase'
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
                  $ref: '#/components/schemas/ProrationRoundingConfig'
                invoice:
                  $ref: '#/components/schemas/ProrationRoundingConfig'
    RecurringCredit:
      allOf:
        - $ref: '#/components/schemas/RecurringCommitOrCreditBase'
        - type: object
          properties:
            proration_rounding:
              type: object
              nullable: true
              description: Rounding configuration for prorated recurring credit amounts.
              properties:
                access:
                  $ref: '#/components/schemas/ProrationRoundingConfig'
    Override:
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
            $ref: '#/components/schemas/OverrideSpecifier'
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
        value:
          type: object
          additionalProperties: true
          description: >-
            Only set for CUSTOM rate_type. This field is interpreted by custom
            rate processors.
        credit_type:
          $ref: '#/components/schemas/CreditType'
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
    Subscriptions:
      type: array
      description: List of subscriptions on the contract.
      items:
        $ref: '#/components/schemas/Subscription'
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
    HierarchyConfiguration:
      oneOf:
        - $ref: '#/components/schemas/ParentHierarchyConfiguration'
        - $ref: '#/components/schemas/ChildHierarchyConfiguration'
      description: >
        Either a **parent** configuration with a list of children or a **child**
        configuration with a single parent.
    ScheduleDurationInput:
      type: object
      required:
        - schedule_items
      properties:
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
    SchedulePointInTimeInput:
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
              $ref: '#/components/schemas/RecurringScheduleFrequency'
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
    RecurringCommitOrCreditInputBase:
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
            with `applicable_product_ids` or `applicable_product_tags`.
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
            Determines whether the first and last commit will be prorated.  If
            not provided, the default is FIRST_AND_LAST (i.e. prorate both the
            first and last commits).
        subscription_config:
          $ref: '#/components/schemas/RecurringCommitSubscriptionConfigInput'
          description: Attach a subscription to the recurring commit/credit.
        hierarchy_configuration:
          $ref: '#/components/schemas/CommitHierarchyConfiguration'
          description: >-
            Optional configuration for recurring commit/credit hierarchy access
            control
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
    ResellerType:
      type: string
      enum:
        - AWS
        - AWS_PRO_SERVICE
        - GCP
        - GCP_PRO_SERVICE
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
    RevenueSystemProviderType:
      x-mint:
        groups:
          - ff:revenue-rec-configurations-enabled
      type: string
      enum:
        - netsuite
    RevenueSystemDeliveryMethodType:
      description: >-
        How revenue recognition records should be delivered to the revenue
        system.
      x-mint:
        groups:
          - ff:revenue-rec-configurations-enabled
      type: string
      enum:
        - direct_to_billing_provider
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
    SubscriptionInput:
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
          $ref: '#/components/schemas/SubscriptionProrationInput'
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
    ContractParentHierarchyConfigurationInput:
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
    UniquenessKeyForCommitsAndCredits:
      type: string
      minLength: 1
      maxLength: 128
      description: >-
        Prevents the creation of duplicates. If a request to create a commit or
        credit is made with a uniqueness key that was previously used to create
        a commit or credit, a new record will not be created and the request
        will fail with a 409 error.
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
    RecurringCommitOrCreditBase:
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
            Determines whether the first and last commit will be prorated.  If
            not provided, the default is FIRST_AND_LAST (i.e. prorate both the
            first and last commits).
        subscription_config:
          $ref: '#/components/schemas/RecurringCommitSubscriptionConfig'
          description: Attach a subscription to the recurring commit/credit.
        hierarchy_configuration:
          $ref: '#/components/schemas/CommitHierarchyConfiguration'
          description: >-
            Optional configuration for recurring commit/credit hierarchy access
            control
    OverrideSpecifier:
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
    Tier:
      type: object
      required:
        - price
      properties:
        size:
          type: number
        price:
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
    Subscription:
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
          $ref: '#/components/schemas/SubscriptionProration'
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
    ChildHierarchyConfiguration:
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
          description: |-
            Indicates which customer should pay for the child's invoice charges

            **SELF**: The child pays for its own invoice charges

            **PARENT**: The parent pays for the child's invoice charges
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
    RecurringScheduleFrequency:
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
    SubscriptionConfigAllocationInput:
      type: string
      enum:
        - INDIVIDUAL
        - POOLED
      description: >-
        If set to POOLED, allocation added per seat is pooled across the
        account. If set to INDIVIDUAL, each seat in the subscription will have
        its own allocation.
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
