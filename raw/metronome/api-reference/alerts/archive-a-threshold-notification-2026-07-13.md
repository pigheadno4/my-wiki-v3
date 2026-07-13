<!-- Source URL: https://docs.metronome.com/api-reference/alerts/archive-a-threshold-notification.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Archive a threshold notification

> Permanently disable a threshold notification and remove it from active monitoring across all customers. Archived threshold notifications stop evaluating immediately and can optionally release their uniqueness key for reuse in future threshold notification configurations.

### Use this endpoint to:
- Decommission threshold notifications that are no longer needed
- Clean up test or deprecated threshold notification configurations
- Free up uniqueness keys for reuse with new threshold notifications
- Stop threshold notification evaluations without losing historical configuration data
- Disable outdated monitoring rules during pricing model transitions

### Key response fields:
- data: Object containing the archived threshold notification's ID

### Usage guidelines:
- Irreversible for evaluation: Archived threshold notifications cannot be re-enabled; create a new threshold notification to resume monitoring
- Uniqueness key handling: Set `release_uniqueness_key` : `true` to reuse the key in future threshold notifications
- Immediate effect: Threshold notification evaluation stops instantly across all customers
- Historical preservation: Archive operation maintains threshold notification history and configuration for compliance and auditing




## OpenAPI

````yaml /openapi.json post /v1/alerts/archive
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
  /v1/alerts/archive:
    post:
      tags:
        - Alerts
      summary: Archive a threshold notification
      description: >
        Permanently disable a threshold notification and remove it from active
        monitoring across all customers. Archived threshold notifications stop
        evaluating immediately and can optionally release their uniqueness key
        for reuse in future threshold notification configurations.


        ### Use this endpoint to:

        - Decommission threshold notifications that are no longer needed

        - Clean up test or deprecated threshold notification configurations

        - Free up uniqueness keys for reuse with new threshold notifications

        - Stop threshold notification evaluations without losing historical
        configuration data

        - Disable outdated monitoring rules during pricing model transitions


        ### Key response fields:

        - data: Object containing the archived threshold notification's ID


        ### Usage guidelines:

        - Irreversible for evaluation: Archived threshold notifications cannot
        be re-enabled; create a new threshold notification to resume monitoring

        - Uniqueness key handling: Set `release_uniqueness_key` : `true` to
        reuse the key in future threshold notifications

        - Immediate effect: Threshold notification evaluation stops instantly
        across all customers

        - Historical preservation: Archive operation maintains threshold
        notification history and configuration for compliance and auditing
      operationId: archiveAlert-v1
      requestBody:
        description: The ID of the threshold notification to archive
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ArchiveAlertPayload'
            example:
              id: 8deed800-1b7a-495d-a207-6c52bac54dc9
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
        '404':
          $ref: '#/components/responses/NotFound'
components:
  schemas:
    ArchiveAlertPayload:
      required:
        - id
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: The Metronome ID of the threshold notification
        release_uniqueness_key:
          type: boolean
          description: >-
            If true, resets the uniqueness key on this threshold notification so
            it can be re-used
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
