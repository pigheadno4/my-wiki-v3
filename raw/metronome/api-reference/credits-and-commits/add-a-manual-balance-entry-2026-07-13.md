<!-- Source URL: https://docs.metronome.com/api-reference/credits-and-commits/add-a-manual-balance-entry.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a manual balance entry

> Manually adjust the available balance on a commit or credit. This entry is appended to the commit ledger as a new event. Optionally include a description that provides the reasoning for the entry.

### Use this endpoint to:
- Address incorrect usage burn-down caused by malformed usage or invalid config
- Decrease available balance to account for outages where usage may have not been tracked or sent to Metronome
- Issue credits to customers in the form of increased balance on existing commit or credit

### Usage guidelines:
Manual ledger entries can be extremely useful for resolving discrepancies in Metronome. However, most corrections to inaccurate billings can be modified upstream of the commit, whether that is via contract editing, rate editing, or other actions that cause an invoice to be recalculated.




## OpenAPI

````yaml /openapi.json post /v1/contracts/addManualBalanceLedgerEntry
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
  /v1/contracts/addManualBalanceLedgerEntry:
    post:
      tags:
        - Credits and commits
      summary: Add a manual balance entry
      description: >
        Manually adjust the available balance on a commit or credit. This entry
        is appended to the commit ledger as a new event. Optionally include a
        description that provides the reasoning for the entry.


        ### Use this endpoint to:

        - Address incorrect usage burn-down caused by malformed usage or invalid
        config

        - Decrease available balance to account for outages where usage may have
        not been tracked or sent to Metronome

        - Issue credits to customers in the form of increased balance on
        existing commit or credit


        ### Usage guidelines:

        Manual ledger entries can be extremely useful for resolving
        discrepancies in Metronome. However, most corrections to inaccurate
        billings can be modified upstream of the commit, whether that is via
        contract editing, rate editing, or other actions that cause an invoice
        to be recalculated.
      operationId: addManualBalanceLedgerEntry-v1
      requestBody:
        description: Add a manual ledger entry to a balance
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AddManualBalanceLedgerEntryPayload'
            example:
              customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
              contract_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
              id: 6162d87b-e5db-4a33-b7f2-76ce6ead4e85
              segment_id: 66368e29-3f97-4d15-a6e9-120897f0070a
              amount: -1000
              reason: Reason for entry
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
    AddManualBalanceLedgerEntryPayload:
      type: object
      required:
        - customer_id
        - id
        - segment_id
        - amount
        - reason
      properties:
        customer_id:
          type: string
          format: uuid
          description: ID of the customer whose balance is to be updated.
        contract_id:
          type: string
          format: uuid
          description: >-
            ID of the contract to update. Leave blank to update a customer level
            balance.
        id:
          type: string
          format: uuid
          description: ID of the balance (commit or credit) to update.
        segment_id:
          type: string
          format: uuid
          description: ID of the segment to update.
        amount:
          type: number
          description: >-
            Amount to add to the segment. A negative number will draw down from
            the balance.
        per_group_amounts:
          type: object
          additionalProperties:
            type: number
          description: >-
            If using individually configured commits/credits attached to seat
            managed subscriptions, the amount to add for each seat. Must sum to
            total amount.
        reason:
          type: string
          description: >-
            Reason for the manual adjustment. This will be displayed in the
            ledger.
        timestamp:
          type: string
          format: date-time
          description: >-
            RFC 3339 timestamp indicating when the manual adjustment takes
            place. If not provided, it will default to the start of the segment.
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
