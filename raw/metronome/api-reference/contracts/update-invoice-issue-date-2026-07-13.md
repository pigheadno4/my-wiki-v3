<!-- Source URL: https://docs.metronome.com/api-reference/contracts/update-invoice-issue-date.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update invoice issue date

> Updates the issue date of a specific DRAFT invoice within a contract. Use this endpoint to reschedule when an invoice should be issued without affecting future billing cycles or the underlying contract terms. Only works with invoices still in DRAFT status, and the new issue date cannot be later than the contract's end date. 

### Usage guidelines:
This only changes the individual invoice's issue date - it does not modify the recurring invoice schedule of associated charges or commits. To update both the issue date and future billing schedule, use the 'edit contract' or 'edit commit' endpoints instead.




## OpenAPI

````yaml /openapi.json post /v1/contracts/updateInvoiceIssueDate
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
  /v1/contracts/updateInvoiceIssueDate:
    post:
      tags:
        - Contracts
      summary: Update invoice issue date
      description: >
        Updates the issue date of a specific DRAFT invoice within a contract.
        Use this endpoint to reschedule when an invoice should be issued without
        affecting future billing cycles or the underlying contract terms. Only
        works with invoices still in DRAFT status, and the new issue date cannot
        be later than the contract's end date. 


        ### Usage guidelines:

        This only changes the individual invoice's issue date - it does not
        modify the recurring invoice schedule of associated charges or commits.
        To update both the issue date and future billing schedule, use the 'edit
        contract' or 'edit commit' endpoints instead.
      operationId: updateInvoiceIssueDate-v1
      requestBody:
        description: The invoice_id and new issue_date
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateInvoiceIssueDatePayload'
            example:
              invoice_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
              issue_date: '2020-01-01T00:00:00.000Z'
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
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '404':
          $ref: '#/components/responses/NotFound'
components:
  schemas:
    UpdateInvoiceIssueDatePayload:
      type: object
      required:
        - invoice_id
        - issue_date
      properties:
        invoice_id:
          type: string
          format: uuid
          description: >-
            ID of the invoice to update. The invoice must still be in DRAFT
            status.
        issue_date:
          type: string
          format: date-time
          description: >-
            RFC 3339 timestamp. This will be the new issue date of the invoice.
            It must not be after the end date of the contract.
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
