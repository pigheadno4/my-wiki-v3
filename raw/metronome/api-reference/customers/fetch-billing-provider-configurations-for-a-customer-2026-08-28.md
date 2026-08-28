<!-- Source URL: https://docs.metronome.com/api-reference/customers/fetch-billing-provider-configurations-for-a-customer.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Fetch billing provider configurations for a customer

> Returns all billing configurations previously set for the customer. Use during the contract provisioning process to fetch the `billing_provider_configuration_id` needed to set the contract billing configuration.




## OpenAPI

````yaml /openapi.json post /v1/getCustomerBillingProviderConfigurations
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
  /v1/getCustomerBillingProviderConfigurations:
    post:
      tags:
        - Customers
      summary: Fetch billing provider configurations for a customer
      description: >
        Returns all billing configurations previously set for the customer. Use
        during the contract provisioning process to fetch the
        `billing_provider_configuration_id` needed to set the contract billing
        configuration.
      operationId: getCustomerBillingProviderConfigurations-v1
      requestBody:
        description: The customer id for which to fetch billing provider configurations
        content:
          application/json:
            schema:
              type: object
              required:
                - customer_id
              properties:
                customer_id:
                  type: string
                  format: uuid
                include_archived:
                  type: boolean
            example:
              customer_id: 6a37bb88-8538-48c5-b37b-a41c836328bd
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
                        #/components/schemas/CustomerBillingProviderConfiguration
              example:
                data:
                  - id: e045c62b-65e7-4e84-a924-3f06f8b621d0
                    billing_provider: stripe
                    customer_id: 6a37bb88-8538-48c5-b37b-a41c836328bd
                    configuration:
                      stripe_customer_id: cus_SB7Rq5UAkSmrR3
                      stripe_collection_method: charge_automatically
                    delivery_method: direct_to_billing_provider
                    delivery_method_configuration:
                      stripe_account_id: acct_1P6FywIkTQSg6Mm3
                      leave_invoices_in_draft: false
                      skip_zero_dollar_invoices: false
                      export_invoice_sub_line_items: false
                      include_zero_quantity_sub_line_items: true
                      stripe_invoice_quantity_always_string: false
                      set_effective_at_date_to_inclusive_period_end: false
                    archived_at: null
                    delivery_method_id: 4422e46f-b374-4159-97e3-300208cdb2e2
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
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
        unbillable_invoices_configuration:
          x-mint:
            metadata:
              tag: Beta
          type: array
          items:
            $ref: '#/components/schemas/UnbillableInvoiceRule'
          description: >-
            Rules that stop matching invoices from being sent to the billing
            provider. Only supported for Stripe billing provider configurations.
            When omitted, every invoice is sent to the billing provider.
          example:
            - invoice_type: usage
              fiat_credit_type_id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
              max_amount: 1000
            - invoice_type: usage
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
    BillingProviderDeliveryMethodType:
      type: string
      enum:
        - direct_to_billing_provider
        - aws_sqs
        - tackle
        - aws_sns
    UnbillableInvoiceRule:
      type: object
      description: >-
        An individual rule that, when evaluated to true, indicates that any
        invoices for this billing provider will not be sent to its associated
        destination for the associated contract. Rules only apply to the
        specified `invoice_type` (or all invoices if omitted) and
        `fiat_credit_type_id` (or all invoices if omitted). Rule precedence is
        evaluated from more specific to less specific. This method will fail
        with a 400 if multiple rules with the same specificity are included.
      required:
        - invoice_type
      properties:
        invoice_type:
          type: string
          enum:
            - usage
            - scheduled
          description: The type of invoice this rule applies to.
        fiat_credit_type_id:
          type: string
          format: uuid
          description: >-
            Restricts the rule to invoices in this fiat currency. Omit for a
            catch-all rule that applies to every currency of the `invoice_type`.
            Required when `max_amount` is set.
        max_amount:
          type: number
          description: >-
            A positive decimal, in the units of `fiat_credit_type_id`. Only
            invoices whose total is at or below this amount are suppressed; a
            higher total is still sent to the billing provider. When omitted,
            every matching invoice is suppressed regardless of amount.
      example:
        invoice_type: usage
        fiat_credit_type_id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
        max_amount: 1000
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
