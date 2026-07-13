<!-- Source URL: https://docs.metronome.com/api-reference/settings/set-up-account-level-billing-provider.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up account-level billing provider

> Set up account-level configuration for a billing provider. Once configured, individual contracts across customers can be mapped to this configuration using the returned delivery_method_id.




## OpenAPI

````yaml /openapi.json post /v1/setUpBillingProvider
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
  /v1/setUpBillingProvider:
    post:
      tags:
        - Settings
      summary: Set up account-level billing provider
      description: >
        Set up account-level configuration for a billing provider. Once
        configured, individual contracts across customers can be mapped to this
        configuration using the returned delivery_method_id.
      operationId: setUpBillingProvider-v1
      requestBody:
        description: Billing provider, delivery method and configuration to insert
        content:
          application/json:
            schema:
              type: object
              required:
                - billing_provider
                - delivery_method
                - configuration
              properties:
                billing_provider:
                  $ref: '#/components/schemas/GABillingProviderType'
                  description: The billing provider set for this configuration.
                delivery_method:
                  $ref: '#/components/schemas/GABillingProviderDeliveryMethodType'
                  description: >-
                    The method to use for delivering invoices for this
                    configuration.
                configuration:
                  type: object
                  additionalProperties: true
                  description: >-
                    Account-level configuration for the billing provider. The
                    structure of this object is specific to the billing provider
                    and delivery provider combination. See examples below.
            examples:
              aws:
                value:
                  billing_provider: aws_marketplace
                  delivery_method: direct_to_billing_provider
                  configuration:
                    aws_external_id: 47b4f6b7-e297-42e8-b175-331d933b402c
                    aws_iam_role_arn: arn:aws:iam::test
              azure:
                value:
                  billing_provider: azure_marketplace
                  delivery_method: direct_to_billing_provider
                  configuration:
                    azure_client_id: client_id
                    raw_azure_client_secret: secret
                    azure_tenant_id: tenant_id
              gcp:
                value:
                  billing_provider: gcp_marketplace
                  delivery_method: direct_to_billing_provider
                  configuration:
                    gcp_provider_id: provider_id
                    raw_gcp_workload_identity_federation_config: '{"wif": "config"}'
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
                    type: object
                    required:
                      - delivery_method_id
                    properties:
                      delivery_method_id:
                        type: string
                        format: uuid
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '409':
          description: Conflict error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    GABillingProviderType:
      type: string
      enum:
        - aws_marketplace
        - azure_marketplace
        - gcp_marketplace
    GABillingProviderDeliveryMethodType:
      type: string
      enum:
        - direct_to_billing_provider
        - aws_sqs
        - aws_sns
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
