<!-- Source URL: https://docs.metronome.com/api-reference/notifications/create-an-offset-lifecycle-event-notification-configuration.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an offset lifecycle event notification configuration

> Create an offset lifecycle event notification configuration. The lifecycle event type is inferred from the policy.type field.




## OpenAPI

````yaml /openapi.json post /v2/notifications/create
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
  /v2/notifications/create:
    post:
      tags:
        - Notifications
      summary: Create an offset lifecycle event notification configuration
      description: >
        Create an offset lifecycle event notification configuration. The
        lifecycle event type is inferred from the policy.type field.
      operationId: createNotificationConfig-v2
      requestBody:
        description: Notification configuration details
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateNotificationConfigPayload'
            example:
              name: +1 day after contract starts
              policy:
                type: contract.start
                offset: P1D
              uniqueness_key: contract-start-notification-823j7fqzo1
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
                    $ref: >-
                      #/components/schemas/LifecycleEventOffsetNotificationConfig
              example:
                data:
                  id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                  name: +1 day after contract starts
                  type: OFFSET_LIFECYCLE_EVENT
                  policy:
                    type: contract.start
                    offset: P1D
                  environment_type: PRODUCTION
                  created_at: '2024-01-15T10:30:00Z'
                  created_by: Martins Seyi
                  archived_at: null
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
                      - BadRequest
                  message:
                    type: string
components:
  schemas:
    CreateNotificationConfigPayload:
      type: object
      required:
        - name
        - policy
      properties:
        name:
          type: string
          description: |
            The name for this offset notification configuration.
        policy:
          $ref: '#/components/schemas/LifecycleEventOffsetPolicy'
          description: >
            The offset lifecycle event policy that defines when and how this
            notification should be triggered. The lifecycle event type is
            inferred from the policy.type field.
        uniqueness_key:
          $ref: '#/components/schemas/UniquenessKey'
          description: >
            Optional uniqueness key to prevent duplicate notification
            configurations.
    LifecycleEventOffsetNotificationConfig:
      type: object
      required:
        - id
        - name
        - type
        - policy
        - environment_type
        - created_at
        - created_by
        - archived_at
      properties:
        id:
          type: string
          format: uuid
          description: ID for this offset notification configuration
        name:
          type: string
          description: |
            The name for this offset notification configuration.
        type:
          type: string
          description: Indicates this is an offset lifecycle event notification
        policy:
          $ref: '#/components/schemas/LifecycleEventOffsetPolicy'
        environment_type:
          type: string
          description: >
            The environment type where this notification configuration was
            created.
        created_at:
          type: string
          format: date-time
          description: |
            RFC 3339 timestamp when this notification configuration was created.
        created_by:
          type: string
          description: Who created this notification configuration
        archived_at:
          type: string
          format: date-time
          nullable: true
          description: When this notification configuration was archived
    LifecycleEventOffsetPolicy:
      type: object
      required:
        - type
        - offset
      properties:
        type:
          type: string
          description: |
            The type of lifecycle event that this offset is based on.
        offset:
          type: string
          description: >
            ISO-8601 duration string indicating how much time before or after
            the base event this notification should be sent. Positive values
            indicate notifications after the event, negative values indicate
            notifications before the event. Examples: "P1D" (1 day after),
            "-PT2H" (2 hours before)
          example: P1D
    UniquenessKey:
      type: string
      minLength: 1
      maxLength: 128
      description: >-
        Prevents the creation of duplicates. If a request to create a record is
        made with a previously used uniqueness key, a new record will not be
        created and the request will fail with a 409 error.
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
