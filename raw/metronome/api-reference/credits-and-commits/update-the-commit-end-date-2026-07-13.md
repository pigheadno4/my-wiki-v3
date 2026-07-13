<!-- Source URL: https://docs.metronome.com/api-reference/credits-and-commits/update-the-commit-end-date.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update the commit end date

> Shortens the end date of a prepaid commit to terminate it earlier than originally scheduled. Use this endpoint when you need to cancel or reduce the duration of an existing prepaid commit. Only works with prepaid commit types and can only move the end date forward (earlier), not extend it. 

### Usage guidelines:
To extend commit end dates or make other comprehensive edits, use the 'edit commit' endpoint instead.




## OpenAPI

````yaml /openapi.json post /v1/contracts/customerCommits/updateEndDate
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
  /v1/contracts/customerCommits/updateEndDate:
    post:
      tags:
        - Credits and commits
      summary: Update the commit end date
      description: >
        Shortens the end date of a prepaid commit to terminate it earlier than
        originally scheduled. Use this endpoint when you need to cancel or
        reduce the duration of an existing prepaid commit. Only works with
        prepaid commit types and can only move the end date forward (earlier),
        not extend it. 


        ### Usage guidelines:

        To extend commit end dates or make other comprehensive edits, use the
        'edit commit' endpoint instead.
      operationId: updateCommitEndDate-v1
      requestBody:
        description: Update the access or invoice end date of a commit
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateCommitEndDatePayload'
            example:
              customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
              commit_id: 6162d87b-e5db-4a33-b7f2-76ce6ead4e85
              access_ending_before: '2020-01-01T00:00:00.000Z'
              invoices_ending_before: '2020-01-01T00:00:00.000Z'
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
                  id: 6162d87b-e5db-4a33-b7f2-76ce6ead4e85
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
    UpdateCommitEndDatePayload:
      type: object
      required:
        - customer_id
        - commit_id
      properties:
        customer_id:
          type: string
          format: uuid
          description: ID of the customer whose commit is to be updated
        commit_id:
          type: string
          format: uuid
          description: ID of the commit to update. Only supports "PREPAID" commits.
        access_ending_before:
          type: string
          format: date-time
          description: >-
            RFC 3339 timestamp indicating when access to the commit will end and
            it will no longer be possible to draw it down (exclusive). If not
            provided, the access will not be updated.
        invoices_ending_before:
          type: string
          format: date-time
          description: >-
            RFC 3339 timestamp indicating when the commit will stop being
            invoiced (exclusive). If not provided, the invoice schedule will not
            be updated.
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
