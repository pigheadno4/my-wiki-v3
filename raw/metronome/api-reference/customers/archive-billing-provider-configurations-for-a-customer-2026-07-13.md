<!-- Source URL: https://docs.metronome.com/api-reference/customers/archive-billing-provider-configurations-for-a-customer.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Archive billing provider configurations for a customer

> Deprecate an existing billing configuration for a customer to handle churn or billing and collection preference changes. Archiving a billing configuration takes effect immediately. If there are active contracts using the configuration, Metronome will archive the configuration on the contract and immediately stop metering to downstream systems.

### Use this endpoint to:
- Remove billing provider customer data and configurations when no longer needed
- Clean up test or deprecated billing provider configurations
- Free up uniqueness keys for reuse with new billing provider configurations
- Disable threshold recharge configurations associated with archived billing providers

### Key response fields:
A successful response returns:
- `success`: Boolean indicating the operation completed successfully
- `error`: Null on success, error message on failure

### Usage guidelines:
- Archiving a contract configuration during a grace period will result in the invoice not being sent to the customer
- Automatically disables both spend-based and credit-based threshold recharge configurations for contracts using the archived billing provider        
- You can archive multiple configurations for a single customer in a single request, but any validation failures for an individual configuration will prevent the entire operation from succeeding




## OpenAPI

````yaml /openapi.json post /v1/archiveCustomerBillingProviderConfigurations
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
  /v1/archiveCustomerBillingProviderConfigurations:
    post:
      tags:
        - Customers
      summary: Archive billing provider configurations for a customer
      description: >
        Deprecate an existing billing configuration for a customer to handle
        churn or billing and collection preference changes. Archiving a billing
        configuration takes effect immediately. If there are active contracts
        using the configuration, Metronome will archive the configuration on the
        contract and immediately stop metering to downstream systems.


        ### Use this endpoint to:

        - Remove billing provider customer data and configurations when no
        longer needed

        - Clean up test or deprecated billing provider configurations

        - Free up uniqueness keys for reuse with new billing provider
        configurations

        - Disable threshold recharge configurations associated with archived
        billing providers


        ### Key response fields:

        A successful response returns:

        - `success`: Boolean indicating the operation completed successfully

        - `error`: Null on success, error message on failure


        ### Usage guidelines:

        - Archiving a contract configuration during a grace period will result
        in the invoice not being sent to the customer

        - Automatically disables both spend-based and credit-based threshold
        recharge configurations for contracts using the archived billing
        provider        

        - You can archive multiple configurations for a single customer in a
        single request, but any validation failures for an individual
        configuration will prevent the entire operation from succeeding
      operationId: archiveCustomerBillingProviderConfigurations-v1
      requestBody:
        description: The ids of the billing provider configurations to archive
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CustomerBillingProviderArchivePayload'
            example:
              customer_billing_provider_configuration_ids:
                - 4db51251-61de-4bfe-b9ce-495e244f3491
                - 4db51251-61de-4bfe-b9ce-495e244f3491
              customer_id: 20a060d1-aa80-41d4-8bb2-4f3091b93903
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
                    $ref: '#/components/schemas/CustomerBillingProviderArchivePayload'
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
    CustomerBillingProviderArchivePayload:
      type: object
      required:
        - customer_billing_provider_configuration_ids
        - customer_id
      properties:
        customer_billing_provider_configuration_ids:
          type: array
          items:
            type: string
            format: uuid
          description: Array of billing provider configuration IDs to archive
        customer_id:
          type: string
          format: uuid
          description: The customer ID the billing provider configurations belong to
    Error:
      required:
        - message
      type: object
      properties:
        message:
          type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
