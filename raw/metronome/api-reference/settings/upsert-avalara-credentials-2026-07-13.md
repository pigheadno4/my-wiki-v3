<!-- Source URL: https://docs.metronome.com/api-reference/settings/upsert-avalara-credentials.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upsert Avalara credentials

> Set the Avalara credentials for some specified `delivery_method_ids`, which can be found in the `/listConfiguredBillingProviders` response. This maps the Avalara credentials to the appropriate billing entity. These credentials are only used for PLG Invoicing today.




## OpenAPI

````yaml /openapi.json post /v1/upsertAvalaraCredentials
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
  /v1/upsertAvalaraCredentials:
    post:
      tags:
        - Settings
      summary: Upsert Avalara credentials
      description: >
        Set the Avalara credentials for some specified `delivery_method_ids`,
        which can be found in the `/listConfiguredBillingProviders` response.
        This maps the Avalara credentials to the appropriate billing entity.
        These credentials are only used for PLG Invoicing today.
      operationId: upsertAvalaraCredentials-v1
      requestBody:
        description: Set the Avalara credentials for some specified `delivery_method_ids`
        content:
          application/json:
            schema:
              type: object
              required:
                - delivery_method_ids
                - avalara_environment
                - avalara_username
                - avalara_password
              properties:
                delivery_method_ids:
                  type: array
                  items:
                    type: string
                  format: uuid
                  description: >-
                    The delivery method IDs of the billing provider
                    configurations to update, can be found in the response of
                    the `/listConfiguredBillingProviders` endpoint.
                avalara_environment:
                  type: string
                  enum:
                    - PRODUCTION
                    - SANDBOX
                  description: The Avalara environment to use (SANDBOX or PRODUCTION).
                avalara_username:
                  type: string
                  description: The username for the Avalara account.
                avalara_password:
                  type: string
                  description: The password for the Avalara account.
                commit_transactions:
                  type: boolean
                  description: >-
                    Commit transactions if you want Metronome tax calculations
                    used for reporting and tax filings.
            example:
              delivery_method_ids:
                - 9a906ebb-fbc7-42e8-8e29-53bfd2db3aca
              avalara_environment: PRODUCTION
              avalara_username: test@metronome.com
              avalara_password: my_password_123
              commit_transactions: true
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                x-stainless-empty-object: true
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
    Error:
      required:
        - message
      type: object
      properties:
        message:
          type: string
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
