<!-- Source URL: https://docs.metronome.com/api-reference/contracts/list-contracts-associated-with-a-package.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List contracts associated with a package

> For a given package, returns all contract IDs and customer IDs associated with the package over a specific time period. 

### Use this endpoint to:
- Understand which customers are provisioned on a package at any given time for internal cohort management
- Manage customer migrations to a new package. For example, to migrate all active customers to a new package, call this endpoint, end contracts, and provision customers on a new package.

### **Usage guidelines:**
Use the **`starting_at`**, **`covering_date`**, and **`include_archived`** parameters to filter the list of returned contracts. For example, to list only currently active contracts, pass **`covering_date`** equal to the current time.




## OpenAPI

````yaml /openapi.json post /v1/packages/listContractsOnPackage
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
  /v1/packages/listContractsOnPackage:
    post:
      tags:
        - Contracts
      summary: List contracts associated with a package
      description: >
        For a given package, returns all contract IDs and customer IDs
        associated with the package over a specific time period. 


        ### Use this endpoint to:

        - Understand which customers are provisioned on a package at any given
        time for internal cohort management

        - Manage customer migrations to a new package. For example, to migrate
        all active customers to a new package, call this endpoint, end
        contracts, and provision customers on a new package.


        ### **Usage guidelines:**

        Use the **`starting_at`**, **`covering_date`**, and
        **`include_archived`** parameters to filter the list of returned
        contracts. For example, to list only currently active contracts, pass
        **`covering_date`** equal to the current time.
      operationId: listContractsOnPackage-v1
      parameters:
        - $ref: '#/components/parameters/PageLimit'
        - $ref: '#/components/parameters/NextPage'
      requestBody:
        description: Package ID and optional filters
        content:
          application/json:
            schema:
              type: object
              required:
                - package_id
              properties:
                package_id:
                  type: string
                  format: uuid
                starting_at:
                  type: string
                  format: date-time
                  description: >-
                    Optional RFC 3339 timestamp. Only include contracts that
                    started on or after this date. This cannot be provided if
                    covering_date filter is provided.
                covering_date:
                  type: string
                  format: date-time
                  description: >-
                    Optional RFC 3339 timestamp. Only include contracts active
                    on the provided date. This cannot be provided if starting_at
                    filter is provided.
                include_archived:
                  type: boolean
                  description: >-
                    Default false. Determines whether to include archived
                    contracts in the results
            example:
              package_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
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
                      $ref: '#/components/schemas/ContractProjectionSummary'
                  next_page:
                    type: string
                    nullable: true
              example:
                data:
                  - contract_id: 63798fdb-6883-4e53-8365-74d42a3e1f09
                    customer_id: f0b78a5e-01d1-4ed1-96da-05bc225963ec
                    starting_at: '2024-01-01T00:00:00Z'
                next_page: eyJvZmZzZXQiOjF9
        '400':
          description: Error
          content:
            application/json:
              schema:
                type: object
                required:
                  - code
                  - message
                properties:
                  code:
                    type: string
                    enum:
                      - PackageNotFound
                  message:
                    type: string
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
    ContractProjectionSummary:
      type: object
      required:
        - customer_id
        - contract_id
        - starting_at
      properties:
        customer_id:
          type: string
          format: uuid
        contract_id:
          type: string
          format: uuid
        starting_at:
          type: string
          format: date-time
        ending_before:
          type: string
          format: date-time
        archived_at:
          type: string
          format: date-time
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
