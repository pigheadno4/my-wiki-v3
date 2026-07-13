<!-- Source URL: https://docs.metronome.com/api-reference/credits-and-commits/create-a-commit.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a commit

> Creates customer-level commits that establish spending commitments for customers across their Metronome usage. Commits represent contracted spending obligations that can be either prepaid (paid upfront) or postpaid (billed later). 

Note: In most cases, you should add commitments directly to customer contracts using the contract/create or contract/edit APIs.

### Use this endpoint to:
Use this endpoint when you need to establish customer-level spending commitments that can be applied across multiple contracts or scoped to specific contracts. Customer-level commits are ideal for:
- Enterprise-wide minimum spending agreements that span multiple contracts
- Multi-contract volume commitments with shared spending pools
- Cross-contract discount tiers based on aggregate usage

#### Commit type Requirements: 
- You must specify either "prepaid" or "postpaid" as the commit type:
- Prepaid commits: Customer pays upfront; invoice_schedule is optional (if omitted, creates a commit without an invoice)
- Postpaid commits: Customer pays when the commitment expires (the end of the access_schedule); invoice_schedule is required and must match access_schedule totals. 

#### Billing configuration:
- invoice_contract_id is required for postpaid commits and for prepaid commits with billing (only optional for free prepaid commits) unless do_not_invoice is set to true
- For postpaid commits: access_schedule and invoice_schedule must have matching amounts
- For postpaid commits: only one schedule item is allowed in both schedules.

#### Scoping flexibility:
Customer-level commits can be configured in a few ways:
- Contract-specific: Use the `applicable_contract_ids` field to limit the commit to specific contracts
- Cross-contract: Leave `applicable_contract_ids` empty to allow the commit to be used across all of the customer's contracts

#### Product targeting:
Commits can be scoped to specific products using applicable_product_ids, applicable_product_tags, or specifiers, or left unrestricted to apply to all products.

#### Priority considerations:
When multiple commits are applicable, the one with the lower priority value will be consumed first. If there is a tie, contract level commits and credits will be applied before customer level commits and credits. Plan your priority scheme carefully to ensure commits are applied in the desired order.

### Usage guidelines:
⚠️ Preferred Alternative: In most cases, you should add commits directly to contracts using the create contract or edit contract APIs instead of creating customer-level commits. Contract-level commits provide better organization and are the recommended approach for standard use cases.




## OpenAPI

````yaml /openapi.json post /v1/contracts/customerCommits/create
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
  /v1/contracts/customerCommits/create:
    post:
      tags:
        - Credits and commits
      summary: Create a commit
      description: >
        Creates customer-level commits that establish spending commitments for
        customers across their Metronome usage. Commits represent contracted
        spending obligations that can be either prepaid (paid upfront) or
        postpaid (billed later). 


        Note: In most cases, you should add commitments directly to customer
        contracts using the contract/create or contract/edit APIs.


        ### Use this endpoint to:

        Use this endpoint when you need to establish customer-level spending
        commitments that can be applied across multiple contracts or scoped to
        specific contracts. Customer-level commits are ideal for:

        - Enterprise-wide minimum spending agreements that span multiple
        contracts

        - Multi-contract volume commitments with shared spending pools

        - Cross-contract discount tiers based on aggregate usage


        #### Commit type Requirements: 

        - You must specify either "prepaid" or "postpaid" as the commit type:

        - Prepaid commits: Customer pays upfront; invoice_schedule is optional
        (if omitted, creates a commit without an invoice)

        - Postpaid commits: Customer pays when the commitment expires (the end
        of the access_schedule); invoice_schedule is required and must match
        access_schedule totals. 


        #### Billing configuration:

        - invoice_contract_id is required for postpaid commits and for prepaid
        commits with billing (only optional for free prepaid commits) unless
        do_not_invoice is set to true

        - For postpaid commits: access_schedule and invoice_schedule must have
        matching amounts

        - For postpaid commits: only one schedule item is allowed in both
        schedules.


        #### Scoping flexibility:

        Customer-level commits can be configured in a few ways:

        - Contract-specific: Use the `applicable_contract_ids` field to limit
        the commit to specific contracts

        - Cross-contract: Leave `applicable_contract_ids` empty to allow the
        commit to be used across all of the customer's contracts


        #### Product targeting:

        Commits can be scoped to specific products using applicable_product_ids,
        applicable_product_tags, or specifiers, or left unrestricted to apply to
        all products.


        #### Priority considerations:

        When multiple commits are applicable, the one with the lower priority
        value will be consumed first. If there is a tie, contract level commits
        and credits will be applied before customer level commits and credits.
        Plan your priority scheme carefully to ensure commits are applied in the
        desired order.


        ### Usage guidelines:

        ⚠️ Preferred Alternative: In most cases, you should add commits directly
        to contracts using the create contract or edit contract APIs instead of
        creating customer-level commits. Contract-level commits provide better
        organization and are the recommended approach for standard use cases.
      operationId: createCustomerCommit-v1
      requestBody:
        description: Create a commit
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateCustomerCommitPayload'
            example:
              customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
              type: prepaid
              name: My Commit
              priority: 100
              product_id: f14d6729-6a44-4b13-9908-9387f1918790
              invoice_contract_id: e57d6929-c2f1-4796-a9a8-63cedefe848d
              access_schedule:
                credit_type_id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                schedule_items:
                  - amount: 1000
                    starting_at: '2020-01-01T00:00:00.000Z'
                    ending_before: '2020-02-01T00:00:00.000Z'
              invoice_schedule:
                credit_type_id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                schedule_items:
                  - unit_price: 10000000
                    quantity: 1
                    timestamp: '2020-03-01T00:00:00.000Z'
                do_not_invoice: false
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
                  id: 6162d87b-e5db-4a33-b7f2-76ce6ead4e85
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
    CreateCustomerCommitPayload:
      type: object
      required:
        - customer_id
        - type
        - priority
        - product_id
        - access_schedule
      properties:
        customer_id:
          type: string
          format: uuid
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
        description:
          type: string
          description: Used only in UI/API. It is not exposed to end customers.
        priority:
          type: number
          description: >-
            If multiple credits or commits are applicable, the one with the
            lower priority will apply first.
        product_id:
          type: string
          format: uuid
          description: >-
            ID of the fixed product associated with the commit. This is required
            because products are used to invoice the commit amount.
        access_schedule:
          $ref: '#/components/schemas/ScheduleDurationInput'
          description: >-
            Schedule for distributing the commit to the customer. For "POSTPAID"
            commits only one schedule item is allowed and amount must match
            invoice_schedule total.
        invoice_schedule:
          $ref: '#/components/schemas/SchedulePointInTimeInput'
          description: >-
            Required for "POSTPAID" commits: the true up invoice will be
            generated at this time and only one schedule item is allowed; the
            total must match accesss_schedule amount. Optional for "PREPAID"
            commits: if not provided, this will be a "complimentary" commit with
            no invoice.
        invoice_contract_id:
          type: string
          format: uuid
          description: >-
            The contract that this commit will be billed on. This is required
            for "POSTPAID" commits and for "PREPAID" commits unless there is no
            invoice schedule above (i.e., the commit is 'free'), or if
            do_not_invoice is set to true.
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
        applicable_contract_ids:
          type: array
          items:
            type: string
          description: >-
            Which contract the commit applies to. If not provided, the commit
            applies to all contracts.
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
        salesforce_opportunity_id:
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
        uniqueness_key:
          $ref: '#/components/schemas/UniquenessKeyForCommitsAndCredits'
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
