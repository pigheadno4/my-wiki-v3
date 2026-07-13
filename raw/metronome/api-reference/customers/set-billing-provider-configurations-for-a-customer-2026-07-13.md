<!-- Source URL: https://docs.metronome.com/api-reference/customers/set-billing-provider-configurations-for-a-customer.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set billing provider configurations for a customer

> Create a billing configuration for a customer. Once created, these configurations are available to associate to a contract and dictates which downstream system to collect payment in or send the invoice to. You can create multiple configurations per customer. The configuration formats are distinct for each downstream provider.

### Use this endpoint to:
- Add the initial configuration to an existing customer. Once created, the billing configuration can then be associated to the customer's contract.
- Add a new configuration to an existing customer. This might be used as part of an upgrade or downgrade workflow where the customer was previously billed through system A (e.g. Stripe) but will now be billed through system B (e.g. AWS). Once created, the new configuration can then be associated to the customer's contract.
- Multiple configurations can be added per destination. For example, you can create two Stripe billing configurations for a Metronome customer that each have a distinct `collection_method`.

### Delivery method options:
- `direct_to_billing_provider`: Use when Metronome should send invoices directly to the billing provider's API (e.g., Stripe, NetSuite). This is the most common method for automated billing workflows.
- `tackle`: Use specifically for AWS Marketplace transactions that require Tackle's co-selling platform for partner attribution and commission tracking.
- `aws_sqs`: Use when you want invoice data delivered to an AWS SQS queue for custom processing before sending to your billing system.
- `aws_sns`: Use when you want invoice notifications published to an AWS SNS topic for event-driven billing workflows.

### Key response fields: 
The id for the customer billing configuration. This id can be used to associate the billing configuration to a contract.

### Usage guidelines:
Must use the `delivery_method_id` if you have multiple Stripe accounts connected to Metronome.




## OpenAPI

````yaml /openapi.json post /v1/setCustomerBillingProviderConfigurations
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
  /v1/setCustomerBillingProviderConfigurations:
    post:
      tags:
        - Customers
      summary: Set billing provider configurations for a customer
      description: >
        Create a billing configuration for a customer. Once created, these
        configurations are available to associate to a contract and dictates
        which downstream system to collect payment in or send the invoice to.
        You can create multiple configurations per customer. The configuration
        formats are distinct for each downstream provider.


        ### Use this endpoint to:

        - Add the initial configuration to an existing customer. Once created,
        the billing configuration can then be associated to the customer's
        contract.

        - Add a new configuration to an existing customer. This might be used as
        part of an upgrade or downgrade workflow where the customer was
        previously billed through system A (e.g. Stripe) but will now be billed
        through system B (e.g. AWS). Once created, the new configuration can
        then be associated to the customer's contract.

        - Multiple configurations can be added per destination. For example, you
        can create two Stripe billing configurations for a Metronome customer
        that each have a distinct `collection_method`.


        ### Delivery method options:

        - `direct_to_billing_provider`: Use when Metronome should send invoices
        directly to the billing provider's API (e.g., Stripe, NetSuite). This is
        the most common method for automated billing workflows.

        - `tackle`: Use specifically for AWS Marketplace transactions that
        require Tackle's co-selling platform for partner attribution and
        commission tracking.

        - `aws_sqs`: Use when you want invoice data delivered to an AWS SQS
        queue for custom processing before sending to your billing system.

        - `aws_sns`: Use when you want invoice notifications published to an AWS
        SNS topic for event-driven billing workflows.


        ### Key response fields: 

        The id for the customer billing configuration. This id can be used to
        associate the billing configuration to a contract.


        ### Usage guidelines:

        Must use the `delivery_method_id` if you have multiple Stripe accounts
        connected to Metronome.
      operationId: setCustomerBillingProviderConfigurations-v1
      requestBody:
        description: The details of the billing provider configurations to insert
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
                    $ref: >-
                      #/components/schemas/CustomerBillingProviderConfigurationInput
            example:
              data:
                - customer_id: 4db51251-61de-4bfe-b9ce-495e244f3491
                  billing_provider: stripe
                  configuration:
                    stripe_customer_id: cus_1234
                    stripe_collection_method: charge_automatically
                    leave_stripe_invoices_in_draft: true
                  delivery_method: direct_to_billing_provider
                - customer_id: 4db51251-61de-4bfe-b9ce-495e244f3491
                  billing_provider: aws_marketplace
                  configuration:
                    aws_customer_id: ABC123ABC12
                    aws_product_code: my_product
                    aws_region: us-west-1
                  delivery_method: direct_to_billing_provider
                - customer_id: 4db51251-61de-4bfe-b9ce-495e244f3491
                  billing_provider: azure_marketplace
                  configuration:
                    azure_subscription_id: my_subscription
                  delivery_method_id: 5b9e3072-415b-4842-94f0-0b6700c8b6be
                - customer_id: 4db51251-61de-4bfe-b9ce-495e244f3491
                  billing_provider: aws_marketplace
                  configuration:
                    aws_customer_id: ABC123ABC12
                    aws_product_code: my_product
                    aws_region: us-west-1
                    aws_is_subscription_product: true
                  delivery_method: direct_to_billing_provider
                - customer_id: 4db51251-61de-4bfe-b9ce-495e244f3491
                  billing_provider: gcp_marketplace
                  configuration:
                    gcp_entitlement_id: my_entitlement
                    gcp_service_name: my.service.endpoint.goog
                  delivery_method: direct_to_billing_provider
                - customer_id: 4db51251-61de-4bfe-b9ce-495e244f3491
                  billing_provider: netsuite
                  configuration:
                    netsuite_customer_id: '12345'
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
                    type: array
                    items:
                      $ref: >-
                        #/components/schemas/CustomerBillingProviderConfigurationOutput
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    CustomerBillingProviderConfigurationInput:
      type: object
      properties:
        billing_provider:
          $ref: '#/components/schemas/BillingProviderType'
          description: The billing provider set for this configuration.
        customer_id:
          type: string
          format: uuid
        tax_provider:
          $ref: '#/components/schemas/TaxProviderType'
          x-mint:
            metadata:
              tag: Beta
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
            is specific to the billing provider and delivery method combination.
            Defaults to an empty object, however, for most billing provider +
            delivery method combinations, it will not be a valid configuration. 
            For AWS marketplace configurations, the aws_is_subscription_product
            flag can be used to indicate a product with usage-based pricing. 
            More information can be found
            [here](https://docs.metronome.com/invoice-customers/solutions/marketplaces/invoice-aws/#provision-aws-marketplace-customers-in-metronome).
          example:
            - aws_customer_id: cust_1234
              aws_product_code: my_product
              aws_region: us-west-1
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
        - customer_id
    CustomerBillingProviderConfigurationOutput:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: ID of the created configuration
        billing_provider:
          $ref: '#/components/schemas/BillingProviderType'
          type: string
          description: The billing provider set for this configuration.
        customer_id:
          type: string
          format: uuid
          description: ID of the customer this configuration is associated with.
        configuration:
          type: object
          additionalProperties: true
          description: >-
            Configuration for the billing provider. The structure of this object
            is specific to the billing provider and delivery method combination.
        delivery_method_id:
          type: string
          format: uuid
          description: ID of the delivery method used for this customer configuration.
        tax_provider:
          $ref: '#/components/schemas/TaxProviderType'
          description: The tax provider set for this configuration.
    Error:
      required:
        - message
      type: object
      properties:
        message:
          type: string
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
