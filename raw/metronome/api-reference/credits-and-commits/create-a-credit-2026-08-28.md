<!-- Source URL: https://docs.metronome.com/api-reference/credits-and-commits/create-a-credit.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a credit

> ⚠️ For most contract amendments, use `contracts/edit` directly. Use this endpoint only for cross-contract or enterprise-wide commits.

Creates customer-level credits that provide spending allowances or free credit balances for customers across their Metronome usage. Note: In most cases, you should add credits directly to customer contracts using the contract/create or contract/edit APIs.

### Use this endpoint to:
Use this endpoint when you need to provision credits directly at the customer level that can be applied across multiple contracts or scoped to specific contracts. Customer-level credits are ideal for:
- Customer onboarding incentives that apply globally
- Flexible spending allowances that aren't tied to a single contract
- Migration scenarios where you need to preserve existing customer balances

#### Scoping flexibility: 
Customer-level credits can be configured in two ways:
- Contract-specific: Use the applicable_contract_ids field to limit the credit to specific contracts
- Cross-contract: Leave applicable_contract_ids empty to allow the credit to be used across all of the customer's contracts

#### Product Targeting: 
Credits can be scoped to specific products using `applicable_product_ids` or `applicable_product_tags`, or left unrestricted to apply to all products.

#### Priority considerations: 
When multiple credits are applicable, the one with the lower priority value will be consumed first. If there is a tie, contract level commits and credits will be applied before customer level commits and credits. Plan your priority scheme carefully to ensure credits are applied in the desired order.

#### Access Schedule Required: 
You must provide an `access_schedule` that defines when and how much credit becomes available to the customer over time. This usually is aligned to the contract schedule or starts immediately and is set to expire in the future.

### Usage Guidelines:
⚠️ Preferred Alternative: In most cases, you should add credits directly to contracts using the contract/create or contract/edit APIs instead of creating customer-level credits. Contract-level credits provide better organization, and are easier for finance teams to recognize revenue, and are the recommended approach for most use cases.




## OpenAPI

````yaml /openapi.json post /v1/contracts/customerCredits/create
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
  /v1/contracts/customerCredits/create:
    post:
      tags:
        - Credits and commits
      summary: Create a credit
      description: >
        ⚠️ For most contract amendments, use `contracts/edit` directly. Use this
        endpoint only for cross-contract or enterprise-wide commits.


        Creates customer-level credits that provide spending allowances or free
        credit balances for customers across their Metronome usage. Note: In
        most cases, you should add credits directly to customer contracts using
        the contract/create or contract/edit APIs.


        ### Use this endpoint to:

        Use this endpoint when you need to provision credits directly at the
        customer level that can be applied across multiple contracts or scoped
        to specific contracts. Customer-level credits are ideal for:

        - Customer onboarding incentives that apply globally

        - Flexible spending allowances that aren't tied to a single contract

        - Migration scenarios where you need to preserve existing customer
        balances


        #### Scoping flexibility: 

        Customer-level credits can be configured in two ways:

        - Contract-specific: Use the applicable_contract_ids field to limit the
        credit to specific contracts

        - Cross-contract: Leave applicable_contract_ids empty to allow the
        credit to be used across all of the customer's contracts


        #### Product Targeting: 

        Credits can be scoped to specific products using
        `applicable_product_ids` or `applicable_product_tags`, or left
        unrestricted to apply to all products.


        #### Priority considerations: 

        When multiple credits are applicable, the one with the lower priority
        value will be consumed first. If there is a tie, contract level commits
        and credits will be applied before customer level commits and credits.
        Plan your priority scheme carefully to ensure credits are applied in the
        desired order.


        #### Access Schedule Required: 

        You must provide an `access_schedule` that defines when and how much
        credit becomes available to the customer over time. This usually is
        aligned to the contract schedule or starts immediately and is set to
        expire in the future.


        ### Usage Guidelines:

        ⚠️ Preferred Alternative: In most cases, you should add credits directly
        to contracts using the contract/create or contract/edit APIs instead of
        creating customer-level credits. Contract-level credits provide better
        organization, and are easier for finance teams to recognize revenue, and
        are the recommended approach for most use cases.
      operationId: createCustomerCredit-v1
      requestBody:
        description: Create a credit
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateCustomerCreditPayload'
            example:
              customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
              name: My Credit
              priority: 100
              product_id: f14d6729-6a44-4b13-9908-9387f1918790
              access_schedule:
                credit_type_id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                schedule_items:
                  - amount: 1000
                    starting_at: '2020-01-01T00:00:00.000Z'
                    ending_before: '2020-02-01T00:00:00.000Z'
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
    CreateCustomerCreditPayload:
      type: object
      required:
        - customer_id
        - priority
        - product_id
        - access_schedule
      properties:
        customer_id:
          type: string
          format: uuid
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
        access_schedule:
          $ref: '#/components/schemas/ScheduleDurationInput'
          description: Schedule for distributing the credit to the customer.
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
        applicable_contract_ids:
          type: array
          items:
            type: string
          description: >-
            Which contract the credit applies to. If not provided, the credit
            applies to all contracts.
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
          x-cf-entity: contract_credit
        rate_type:
          type: string
          enum:
            - COMMIT_RATE
            - commit_rate
            - LIST_RATE
            - list_rate
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
