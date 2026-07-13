<!-- Source URL: https://docs.metronome.com/api-reference/customers/create-a-customer.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a customer

> Create a new customer in Metronome and optionally the billing configuration (recommended) which dictates where invoices for the customer will be sent or where payment will be collected. 

### Use this endpoint to:
Execute your customer provisioning workflows for either PLG motions, where customers originate in your platform, or SLG motions, where customers originate in your sales system.

### Key response fields: 
This end-point returns the `customer_id` created by the request. This id can be used to fetch relevant billing configurations and create contracts.

### Example workflow:
- Generally, Metronome recommends first creating the customer in the downstream payment / ERP system when payment method is collected and then creating the customer in Metronome using the response (i.e. `customer_id`) from the downstream system. If you do not create a billing configuration on customer creation, you can add it later.        
- Once a customer is created, you can then create a contract for the customer. In the contract creation process, you will need to add the customer billing configuration to the contract to ensure Metronome invoices the customer correctly. This is because a customer can have multiple configurations.
- As part of the customer creation process, set the ingest alias for the customer which will ensure usage is accurately mapped to the customer. Ingest aliases can be added or changed after the creation process as well.

### Usage guidelines:
For details on different billing configurations for different systems, review the `/setCustomerBillingConfiguration` end-point.




## OpenAPI

````yaml /openapi.json post /v1/customers
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
  /v1/customers:
    post:
      tags:
        - Customers
      summary: Create a customer
      description: >
        Create a new customer in Metronome and optionally the billing
        configuration (recommended) which dictates where invoices for the
        customer will be sent or where payment will be collected. 


        ### Use this endpoint to:

        Execute your customer provisioning workflows for either PLG motions,
        where customers originate in your platform, or SLG motions, where
        customers originate in your sales system.


        ### Key response fields: 

        This end-point returns the `customer_id` created by the request. This id
        can be used to fetch relevant billing configurations and create
        contracts.


        ### Example workflow:

        - Generally, Metronome recommends first creating the customer in the
        downstream payment / ERP system when payment method is collected and
        then creating the customer in Metronome using the response (i.e.
        `customer_id`) from the downstream system. If you do not create a
        billing configuration on customer creation, you can add it
        later.        

        - Once a customer is created, you can then create a contract for the
        customer. In the contract creation process, you will need to add the
        customer billing configuration to the contract to ensure Metronome
        invoices the customer correctly. This is because a customer can have
        multiple configurations.

        - As part of the customer creation process, set the ingest alias for the
        customer which will ensure usage is accurately mapped to the customer.
        Ingest aliases can be added or changed after the creation process as
        well.


        ### Usage guidelines:

        For details on different billing configurations for different systems,
        review the `/setCustomerBillingConfiguration` end-point.
      operationId: createCustomer-v1
      requestBody:
        description: The customer to create
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LegacyCreateCustomerPayload'
            example:
              ingest_aliases:
                - team@example.com
              name: Example, Inc.
              customer_billing_provider_configurations:
                - billing_provider: stripe
                  delivery_method: direct_to_billing_provider
                  configuration:
                    stripe_customer_id: cus_123
                    stripe_collection_method: charge_automatically
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
                    $ref: '#/components/schemas/Customer'
              example:
                data:
                  id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                  external_id: team@example.com
                  ingest_aliases:
                    - team@example.com
                  name: Aperture, Inc.
        '409':
          description: A customer with this ID already exists
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
components:
  schemas:
    LegacyCreateCustomerPayload:
      required:
        - name
      type: object
      properties:
        ingest_aliases:
          type: array
          description: Aliases that can be used to refer to this customer in usage events
          items:
            type: string
            minLength: 1
            maxLength: 128
          maxItems: 2000
        external_id:
          type: string
          minLength: 1
          maxLength: 128
          description: >-
            (deprecated, use ingest_aliases instead) an alias that can be used
            to refer to this customer in usage events
        name:
          type: string
          description: >-
            This will be truncated to 160 characters if the provided name is
            longer.
        customer_billing_provider_configurations:
          type: array
          items:
            $ref: >-
              #/components/schemas/CustomerBillingProviderConfigurationCreateCustomerInput
        customer_revenue_system_configurations:
          x-mint:
            groups:
              - ff:revenue-rec-configurations-enabled
          type: array
          items:
            $ref: >-
              #/components/schemas/CustomerRevenueSystemConfigurationCreateCustomerInput
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: customer
    Customer:
      required:
        - external_id
        - ingest_aliases
        - id
        - name
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: the Metronome ID of the customer
        external_id:
          type: string
          description: >-
            (deprecated, use ingest_aliases instead) the first ID (Metronome or
            ingest alias) that can be used in usage events
        ingest_aliases:
          type: array
          description: >-
            aliases for this customer that can be used instead of the Metronome
            customer ID in usage events
          items:
            type: string
        name:
          type: string
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: customer
    CustomerBillingProviderConfigurationCreateCustomerInput:
      type: object
      properties:
        billing_provider:
          $ref: '#/components/schemas/ContractsBillingProviderType'
          description: The billing provider set for this configuration.
        tax_provider:
          $ref: '#/components/schemas/TaxProviderType'
          description: >-
            Specifies which tax provider Metronome should use for tax
            calculation when billing through Stripe. This is only supported for
            Stripe billing provider configurations with
            auto_charge_payment_intent or manual_charge_payment_intent
            collection methods.
        configuration:
          type: object
          additionalProperties: true
          description: >-
            Configuration for the billing provider. The structure of this object
            is specific to the billing provider and delivery provider
            combination. Defaults to an empty object, however, for most billing
            provider + delivery method combinations, it will not be a valid
            configuration.
          example:
            - aws_customer_id: cust_1234
              aws_product_code: my_product
              aws_region: us-west-1
              aws_is_subscription_product: false
            - azure_subscription_id: my_subscription
            - gcp_entitlement_id: my_entitlement
              gcp_service_name: my_service
            - stripe_collection_method: charge_automatically
              leave_stripe_invoices_in_draft: true
            - netsuite_customer_id: '12345'
        delivery_method_id:
          type: string
          format: uuid
          description: >-
            ID of the delivery method to use for this customer. If not provided,
            the `delivery_method` must be provided.
        delivery_method:
          $ref: '#/components/schemas/BillingProviderDeliveryMethodType'
          description: >-
            The method to use for delivering invoices to this customer. If not
            provided, the `delivery_method_id` must be provided.
      required:
        - billing_provider
    CustomerRevenueSystemConfigurationCreateCustomerInput:
      x-mint:
        groups:
          - ff:revenue-rec-configurations-enabled
      type: object
      properties:
        provider:
          $ref: '#/components/schemas/RevenueSystemProviderType'
          description: The revenue system provider set for this configuration.
        configuration:
          type: object
          additionalProperties: true
          description: >-
            Configuration for the revenue system provider. The structure of this
            object is specific to the revenue system provider. For NetSuite,
            this should contain `netsuite_customer_id`.
        delivery_method_id:
          type: string
          format: uuid
          description: >-
            ID of the delivery method to use for this customer. If not provided,
            the `delivery_method` must be provided.
        delivery_method:
          $ref: '#/components/schemas/RevenueSystemDeliveryMethodType'
          description: >-
            The method to use for delivering invoices to this customer. If not
            provided, the `delivery_method_id` must be provided.
      required:
        - provider
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
    ContractsBillingProviderType:
      type: string
      enum:
        - aws_marketplace
        - azure_marketplace
        - gcp_marketplace
        - stripe
        - netsuite
    TaxProviderType:
      type: string
      enum:
        - anrok
        - avalara
        - stripe
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
