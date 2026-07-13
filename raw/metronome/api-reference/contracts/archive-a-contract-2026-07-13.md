<!-- Source URL: https://docs.metronome.com/api-reference/contracts/archive-a-contract.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Archive a contract

> Permanently end and archive a contract along with all its terms. Any draft invoices will be canceled, and all upcoming scheduled invoices will be voided–also all finalized invoices can optionally be voided. Use this in the event a contract was incorrectly created and needed to be removed from a customer.

#### Impact on commits and credits:
When archiving a contract, all associated commits and credits are also archived. For prepaid commits with active segments, Metronome automatically generates expiration ledger entries to close out any remaining balances, ensuring accurate accounting of unused prepaid amounts. These ledger entries will appear in the commit's transaction history with type `PREPAID_COMMIT_EXPIRATION`.

#### Archived contract visibility: 
Archived contracts remain accessible for historical reporting and audit purposes. They can be retrieved using the `ListContracts` endpoint by setting the `include_archived` parameter to `true` or in the Metronome UI when the "Show archived" option is enabled.




## OpenAPI

````yaml /openapi.json post /v1/contracts/archive
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
  /v1/contracts/archive:
    post:
      tags:
        - Contracts
      summary: Archive a contract
      description: >
        Permanently end and archive a contract along with all its terms. Any
        draft invoices will be canceled, and all upcoming scheduled invoices
        will be voided–also all finalized invoices can optionally be voided. Use
        this in the event a contract was incorrectly created and needed to be
        removed from a customer.


        #### Impact on commits and credits:

        When archiving a contract, all associated commits and credits are also
        archived. For prepaid commits with active segments, Metronome
        automatically generates expiration ledger entries to close out any
        remaining balances, ensuring accurate accounting of unused prepaid
        amounts. These ledger entries will appear in the commit's transaction
        history with type `PREPAID_COMMIT_EXPIRATION`.


        #### Archived contract visibility: 

        Archived contracts remain accessible for historical reporting and audit
        purposes. They can be retrieved using the `ListContracts` endpoint by
        setting the `include_archived` parameter to `true` or in the Metronome
        UI when the "Show archived" option is enabled.
      operationId: archiveContract-v1
      requestBody:
        description: >
          Permanently end and archive a contract along with all its terms. Any
          draft invoices will be canceled, and all upcoming scheduled invoices
          will be voided–also all finalized invoices can optionally be voided.
          Use this in the event a contract was incorrectly created and needed to
          be removed from a customer.


          Impact on commits and credits: 

          When archiving a contract, all associated commits and credits are also
          archived. For prepaid commits with active segments, Metronome
          automatically generates expiration ledger entries to close out any
          remaining balances, ensuring accurate accounting of unused prepaid
          amounts. These ledger entries will appear in the commit's transaction
          history with type PREPAID_COMMIT_EXPIRATION.


          Archived contract visibility: 

          Archived contracts remain accessible for historical reporting and
          audit purposes. They can be retrieved using the `ListContracts`
          endpoint by setting the `include_archived` parameter to `true` or in
          the Metronome UI when the "Show archived" option is enabled.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ArchiveContractPayload'
            example:
              customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
              contract_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
              void_invoices: true
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
                  id: 8deed800-1b7a-495d-a207-6c52bac54dc9
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
    ArchiveContractPayload:
      type: object
      required:
        - customer_id
        - contract_id
        - void_invoices
      properties:
        customer_id:
          type: string
          format: uuid
          description: ID of the customer whose contract is to be archived
        contract_id:
          type: string
          format: uuid
          description: ID of the contract to archive
        void_invoices:
          type: boolean
          description: >-
            If false, the existing finalized invoices will remain after the
            contract is archived.
    Id:
      required:
        - id
      type: object
      properties:
        id:
          type: string
          format: uuid
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
