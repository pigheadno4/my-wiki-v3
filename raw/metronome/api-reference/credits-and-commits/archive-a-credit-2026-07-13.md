<!-- Source URL: https://docs.metronome.com/api-reference/credits-and-commits/archive-a-credit.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Archive a credit

> Archive a contract-level or customer-level credit. Use this endpoint to deactivate a credit while preserving historical records. You will not be able to archive a credit until all of the finalized invoices the credit has been applied to are voided. 

Example workflow: 
The customer was granted a free credit erroneously. It was applied to their most recent finalized invoice.
- First, void the finalized invoice that the credit was applied to. 
- Then, use the archiveCredit endpoint to deactivate the credit. 
- Finally, regenerate the voided invoice. The invoice will be regenerated without the application of the credit, which has now been archived. 

### Usage guidelines:
- Once a credit has been archived, it will no longer appear by default on the endpoints `listCustomerCredits` or `listCustomerBalances`. Use the `include_archived` parameter to choose to fetch the details. 
- Once a credit has been archived, it has a null ledger and 0 remaining balance. 
- Archiving a credit fully deactivates the entire access schedule. If you want to reduce the amount granted in a credit, consider editing the access schedule using the `editCredit` endpoint, or adding a manual ledger entry using the `addManualBalanceLedgerEntry` endpoint.




## OpenAPI

````yaml /openapi.json post /v2/contracts/credits/archive
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
  /v2/contracts/credits/archive:
    post:
      tags:
        - Credits and commits
      summary: Archive a credit
      description: >
        Archive a contract-level or customer-level credit. Use this endpoint to
        deactivate a credit while preserving historical records. You will not be
        able to archive a credit until all of the finalized invoices the credit
        has been applied to are voided. 


        Example workflow: 

        The customer was granted a free credit erroneously. It was applied to
        their most recent finalized invoice.

        - First, void the finalized invoice that the credit was applied to. 

        - Then, use the archiveCredit endpoint to deactivate the credit. 

        - Finally, regenerate the voided invoice. The invoice will be
        regenerated without the application of the credit, which has now been
        archived. 


        ### Usage guidelines:

        - Once a credit has been archived, it will no longer appear by default
        on the endpoints `listCustomerCredits` or `listCustomerBalances`. Use
        the `include_archived` parameter to choose to fetch the details. 

        - Once a credit has been archived, it has a null ledger and 0 remaining
        balance. 

        - Archiving a credit fully deactivates the entire access schedule. If
        you want to reduce the amount granted in a credit, consider editing the
        access schedule using the `editCredit` endpoint, or adding a manual
        ledger entry using the `addManualBalanceLedgerEntry` endpoint.
      operationId: archiveCredit-v2
      requestBody:
        description: Customer ID and Credit ID to archive
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ArchiveCreditPayload'
            example:
              customer_id: 4c91c473-fc12-445a-9c38-40421d47023f
              credit_id: 5e7e82cf-ccb7-428c-a96f-a8e4f67af822
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
                  id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
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
                      - CustomerNotFound
                  message:
                    type: string
components:
  schemas:
    ArchiveCreditPayload:
      type: object
      required:
        - customer_id
        - credit_id
      properties:
        customer_id:
          type: string
          format: uuid
          description: ID of the customer whose credit is being archived
        credit_id:
          type: string
          format: uuid
          description: ID of the credit to archive
    Id:
      required:
        - id
      type: object
      properties:
        id:
          type: string
          format: uuid
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
