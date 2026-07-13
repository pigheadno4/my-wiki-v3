<!-- Source URL: https://docs.metronome.com/api-reference/contracts/set-a-contract-usage-filter.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set a contract usage filter

> If a customer has multiple contracts with overlapping rates, the usage filter routes usage to the appropriate contract based on a predefined group key. 

As an example, imagine you have a customer associated with two projects. Each project is associated with its own contract. You can create a usage filter with group key `project_id`
on each contract, and route usage for `project_1` to the first contract and `project_2` to the second contract. 

### Use this endpoint to:
- Support enterprise contracting scenarios where multiple contracts are associated to the same customer with the same rates.
- Update the usage filter associated with the contract over time. 

### Usage guidelines:
To use usage filters, the `group_key` must be defined on the billable metrics underlying the rate card on the contracts.




## OpenAPI

````yaml /openapi.json post /v1/contracts/setUsageFilter
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
  /v1/contracts/setUsageFilter:
    post:
      tags:
        - Contracts
      summary: Set a contract usage filter
      description: >
        If a customer has multiple contracts with overlapping rates, the usage
        filter routes usage to the appropriate contract based on a predefined
        group key. 


        As an example, imagine you have a customer associated with two projects.
        Each project is associated with its own contract. You can create a usage
        filter with group key `project_id`

        on each contract, and route usage for `project_1` to the first contract
        and `project_2` to the second contract. 


        ### Use this endpoint to:

        - Support enterprise contracting scenarios where multiple contracts are
        associated to the same customer with the same rates.

        - Update the usage filter associated with the contract over time. 


        ### Usage guidelines:

        To use usage filters, the `group_key` must be defined on the billable
        metrics underlying the rate card on the contracts.
      operationId: setUsageFilter-v1
      requestBody:
        description: Set usage filter for contract
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SetUsageFilterPayload'
            example:
              customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
              contract_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
              group_key: business_subscription_id
              group_values:
                - ID-1
                - ID-2
              starting_at: '2020-01-01T00:00:00.000Z'
      responses:
        '200':
          description: Success
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
    SetUsageFilterPayload:
      type: object
      required:
        - customer_id
        - contract_id
        - group_key
        - group_values
        - starting_at
      properties:
        customer_id:
          type: string
          format: uuid
        contract_id:
          type: string
          format: uuid
        group_key:
          type: string
        group_values:
          type: array
          items:
            type: string
        starting_at:
          type: string
          format: date-time
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
