<!-- Source URL: https://docs.metronome.com/api-reference/contracts/amend-a-contract.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Amend a contract

> Amendments will be replaced by Contract editing. New clients should implement using the `editContract` endpoint. Read more about the migration to contract editing [here](/guides/implement-metronome/migrate-amendments-to-edits/) and contact us via the [Metronome support portal](https://support.metronome.com/) for more details. Once contract editing is enabled, access to this endpoint will be removed.




## OpenAPI

````yaml /openapi.json post /v1/contracts/amend
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
  /v1/contracts/amend:
    post:
      tags:
        - Contracts
      summary: Amend a contract
      description: >
        Amendments will be replaced by Contract editing. New clients should
        implement using the `editContract` endpoint. Read more about the
        migration to contract editing
        [here](/guides/implement-metronome/migrate-amendments-to-edits/) and
        contact us via the [Metronome support
        portal](https://support.metronome.com/) for more details. Once contract
        editing is enabled, access to this endpoint will be removed.
      operationId: amendContract-v1
      requestBody:
        description: Amend a contract
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AmendContractPayload'
            example:
              customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
              contract_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
              starting_at: '2020-01-01T00:00:00.000Z'
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
    AmendContractPayload:
      type: object
      required:
        - customer_id
        - contract_id
        - starting_at
      properties:
        customer_id:
          type: string
          format: uuid
          description: ID of the customer whose contract is to be amended
        contract_id:
          type: string
          format: uuid
          description: ID of the contract to amend
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
          description: inclusive start time for the amendment
        commits:
          type: array
          items:
            $ref: '#/components/schemas/CommitInput'
        credits:
          type: array
          items:
            $ref: '#/components/schemas/CreditInput'
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
            $ref: '#/components/schemas/ResellerRoyaltyOrUpdateInput'
        scheduled_charges:
          type: array
          items:
            $ref: '#/components/schemas/ScheduledChargeInput'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: contract
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
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
    ScheduleDurationInput:
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
