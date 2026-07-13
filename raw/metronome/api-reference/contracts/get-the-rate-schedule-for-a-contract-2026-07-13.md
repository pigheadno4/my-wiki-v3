<!-- Source URL: https://docs.metronome.com/api-reference/contracts/get-the-rate-schedule-for-a-contract.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get the rate schedule for a contract

> For a specific customer and contract, get the rates at a specific point in time. This endpoint takes the contract's rate card into consideration, including scheduled changes. It also takes into account overrides on the contract. 

For example, if you want to show your customer a summary of the prices they are paying, inclusive of any negotiated discounts or promotions, use this endpoint. This endpoint only returns rates that are entitled.




## OpenAPI

````yaml /openapi.json post /v1/contracts/getContractRateSchedule
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
  /v1/contracts/getContractRateSchedule:
    post:
      tags:
        - Contracts
      summary: Get the rate schedule for a contract
      description: >
        For a specific customer and contract, get the rates at a specific point
        in time. This endpoint takes the contract's rate card into
        consideration, including scheduled changes. It also takes into account
        overrides on the contract. 


        For example, if you want to show your customer a summary of the prices
        they are paying, inclusive of any negotiated discounts or promotions,
        use this endpoint. This endpoint only returns rates that are entitled.
      operationId: getContractRateSchedule-v1
      parameters:
        - $ref: '#/components/parameters/PageLimit'
        - $ref: '#/components/parameters/NextPage'
      requestBody:
        description: Contract rate schedule filter options.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GetContractRateSchedulePayload'
            example:
              customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
              contract_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
              at: '2020-01-01T00:00:00.000Z'
              selectors:
                - product_id: d6300dbb-882e-4d2d-8dec-5125d16b65d0
                  partial_pricing_group_values:
                    region: us-west-2
                    cloud: aws
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
                  next_page:
                    type: string
                    nullable: true
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/ContractRateSchedule'
components:
  parameters:
    PageLimit:
      name: limit
      in: query
      description: Max number of results that should be returned
      required: false
      schema:
        type: integer
        minimum: 1
        maximum: 100
    NextPage:
      name: next_page
      in: query
      description: Cursor that indicates where the next page of results should start.
      required: false
      schema:
        type: string
  schemas:
    GetContractRateSchedulePayload:
      type: object
      required:
        - customer_id
        - contract_id
      properties:
        customer_id:
          type: string
          format: uuid
          description: ID of the customer for whose contract to get the rate schedule for.
        contract_id:
          type: string
          format: uuid
          description: ID of the contract to get the rate schedule for.
        at:
          type: string
          format: date-time
          description: >-
            optional timestamp which overlaps with the returned rate schedule
            segments. When not specified, the current timestamp will be used.
        selectors:
          description: >-
            List of rate selectors, rates matching ANY of the selectors will be
            included in the response. Passing no selectors will result in all
            rates being returned.
          type: array
          items:
            $ref: '#/components/schemas/RateSelectorWithProductTags'
    ContractRateSchedule:
      type: object
      required:
        - rate_card_id
        - product_id
        - product_name
        - product_tags
        - product_custom_fields
        - starting_at
        - entitled
        - list_rate
      properties:
        rate_card_id:
          type: string
          format: uuid
        product_id:
          type: string
          format: uuid
        product_name:
          type: string
        product_tags:
          type: array
          items:
            type: string
        product_custom_fields:
          $ref: '#/components/schemas/CustomField'
        starting_at:
          type: string
          format: date-time
        ending_before:
          type: string
          format: date-time
        entitled:
          type: boolean
        pricing_group_values:
          type: object
          additionalProperties:
            type: string
        list_rate:
          $ref: '#/components/schemas/Rate'
        override_rate:
          $ref: '#/components/schemas/Rate'
        commit_rate:
          $ref: '#/components/schemas/CommitRate'
        billing_frequency:
          type: string
          enum:
            - MONTHLY
            - QUARTERLY
            - ANNUAL
            - WEEKLY
    RateSelectorWithProductTags:
      type: object
      properties:
        billing_frequency:
          description: >-
            Subscription rates matching the billing frequency will be included
            in the response.
          type: string
          enum:
            - MONTHLY
            - Monthly
            - monthly
            - QUARTERLY
            - Quarterly
            - quarterly
            - ANNUAL
            - Annual
            - annual
            - WEEKLY
            - Weekly
            - weekly
        product_id:
          description: Rates matching the product id will be included in the response.
          type: string
          format: uuid
        product_tags:
          description: >-
            List of product tags, rates matching any of the tags will be
            included in the response.
          type: array
          items:
            type: string
        pricing_group_values:
          description: >-
            List of pricing group key value pairs, rates matching all of the key
            / value pairs will be included in the response.
          type: object
          additionalProperties:
            type: string
        partial_pricing_group_values:
          description: >-
            List of pricing group key value pairs, rates containing the matching
            key / value pairs will be included in the response.
          type: object
          additionalProperties:
            type: string
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
    Rate:
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
            - CUSTOM
            - custom
            - TIERED
            - tiered
            - TIERED_PERCENTAGE
            - tiered_percentage
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
          x-mint:
            groups:
              - client_id:5b9e3072-415b-4842-94f0-0b6700c8b6be
              - client_id:179e395f-5349-4fe2-bf12-64ab4e5bc560
              - client_id:f157d376-0781-4ef3-9db9-775a9052148e
              - client_id:7dd2f652-7629-4925-9069-77f5c5d3db37
              - client_id:c0ce3dc0-6d3e-4f6b-aadf-dfb90f2bf9f5
              - client_id:cf874b25-ca3b-460b-b6fe-5f33b3c2ea33
              - client_id:97c07a0c-70db-448a-a1d4-adcd2b8bd1c7
        price:
          type: number
          description: >-
            Default price. For FLAT rate_type, this must be >=0. For PERCENTAGE
            rate_type, this is a decimal fraction, e.g. use 0.1 for 10%; this
            must be >=0 and <=1.
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
        pricing_group_values:
          type: object
          description: >-
            if pricing groups are used, this will contain the values used to
            calculate the price
          additionalProperties:
            type: string
        credit_type:
          $ref: '#/components/schemas/CreditType'
    CommitRate:
      type: object
      description: >-
        A distinct rate on the rate card. You can choose to use this rate rather
        than list rate when consuming a credit or commit.
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
              - client_id:11db091c-975b-4908-9f67-b1ceb126acdf
            subscription:
              - client_id:11db091c-975b-4908-9f67-b1ceb126acdf
            percentage:
              - client_id:11db091c-975b-4908-9f67-b1ceb126acdf
            PERCENTAGE:
              - client_id:11db091c-975b-4908-9f67-b1ceb126acdf
            TIERED_PERCENTAGE:
              - ff:support-charge-ga
            tiered_percentage:
              - ff:support-charge-ga
        price:
          type: number
          description: >-
            Commit rate price. For FLAT rate_type, this must be >=0. For
            PERCENTAGE rate_type, this is a decimal fraction, e.g. use 0.1 for
            10%; this must be >=0 and <=1.
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
