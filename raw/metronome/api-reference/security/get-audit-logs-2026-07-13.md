<!-- Source URL: https://docs.metronome.com/api-reference/security/get-audit-logs.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get audit logs

> Get a comprehensive audit trail of all operations performed in your Metronome account, whether initiated through the API, web interface, or automated processes. This endpoint provides detailed logs of who did what and when, enabling compliance reporting, security monitoring, and operational troubleshooting across all interaction channels.

### Use this endpoint to:
- Monitor all account activity for security and compliance purposes
- Track configuration changes regardless of source (API, UI, or system)
- Investigate issues by reviewing historical operations

### Key response fields: 
An array of AuditLog objects containing:
- id: Unique identifier for the audit log entry
- timestamp: When the action occurred (RFC 3339 format)
- actor: Information about who performed the action
- request: Details including request ID, IP address, and user agent
- `resource_type`: The type of resource affected (e.g., customer, contract, invoice)
- `resource_id`: The specific resource identifier
- `action`: The operation performed
- `next_page`: Cursor for continuous log retrieval

### Usage guidelines:
- Continuous retrieval: The next_page token enables uninterrupted log streaming—save it between requests to ensure no logs are missed
- Empty responses: An empty data array means no new logs yet; continue polling with the same next_page token
- Date filtering:
    - `starting_on`: Earliest logs to return (inclusive)
    - `ending_before`: Latest logs to return (exclusive)
    - Cannot be used with `next_page`
- Resource filtering: Must specify both `resource_type` and `resource_id` together
- Sort order: Default is `date_asc`; use `date_desc` for newest first




## OpenAPI

````yaml /openapi.json get /v1/auditLogs
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
  /v1/auditLogs:
    get:
      tags:
        - Security
      summary: Get audit logs
      description: >
        Get a comprehensive audit trail of all operations performed in your
        Metronome account, whether initiated through the API, web interface, or
        automated processes. This endpoint provides detailed logs of who did
        what and when, enabling compliance reporting, security monitoring, and
        operational troubleshooting across all interaction channels.


        ### Use this endpoint to:

        - Monitor all account activity for security and compliance purposes

        - Track configuration changes regardless of source (API, UI, or system)

        - Investigate issues by reviewing historical operations


        ### Key response fields: 

        An array of AuditLog objects containing:

        - id: Unique identifier for the audit log entry

        - timestamp: When the action occurred (RFC 3339 format)

        - actor: Information about who performed the action

        - request: Details including request ID, IP address, and user agent

        - `resource_type`: The type of resource affected (e.g., customer,
        contract, invoice)

        - `resource_id`: The specific resource identifier

        - `action`: The operation performed

        - `next_page`: Cursor for continuous log retrieval


        ### Usage guidelines:

        - Continuous retrieval: The next_page token enables uninterrupted log
        streaming—save it between requests to ensure no logs are missed

        - Empty responses: An empty data array means no new logs yet; continue
        polling with the same next_page token

        - Date filtering:
            - `starting_on`: Earliest logs to return (inclusive)
            - `ending_before`: Latest logs to return (exclusive)
            - Cannot be used with `next_page`
        - Resource filtering: Must specify both `resource_type` and
        `resource_id` together

        - Sort order: Default is `date_asc`; use `date_desc` for newest first
      operationId: getAuditLogs-v1
      parameters:
        - $ref: '#/components/parameters/PageLimit'
        - $ref: '#/components/parameters/NextPage'
        - name: starting_on
          in: query
          description: >-
            RFC 3339 timestamp of the earliest audit log to return. Cannot be
            used with 'next_page'.
          required: false
          schema:
            type: string
            format: date-time
        - name: ending_before
          in: query
          description: RFC 3339 timestamp (exclusive). Cannot be used with 'next_page'.
          required: false
          schema:
            type: string
            format: date-time
        - name: sort
          in: query
          description: >-
            Sort order by timestamp, e.g. date_asc or date_desc. Defaults to
            date_asc.
          required: false
          schema:
            type: string
            enum:
              - date_asc
              - date_desc
        - name: resource_id
          in: query
          description: >-
            Optional parameter that can be used to filter which audit logs are
            returned. If you specify resource_id, you must also specify
            resource_type.
          required: false
          schema:
            type: string
        - name: resource_type
          in: query
          description: >-
            Optional parameter that can be used to filter which audit logs are
            returned. If you specify resource_type, you must also specify
            resource_id.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                required:
                  - data
                  - next_page
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/AuditLog'
                  next_page:
                    type: string
                    description: >-
                      The next_page parameter is always returned to support
                      ongoing log retrieval. It enables continuous querying,
                      even when some requests return no new data. Save the
                      next_page token from each response and use it for future
                      requests to ensure no logs are missed. This setup is ideal
                      for regular updates via automated processes, like cron
                      jobs, to fetch logs continuously as they become available.
                      When you receive an empty data array, it indicates a
                      temporary absence of new logs, but subsequent requests
                      might return new data.
                    nullable: true
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
    AuditLog:
      type: object
      required:
        - id
        - timestamp
        - request
      properties:
        id:
          type: string
        timestamp:
          type: string
          format: date-time
        actor:
          $ref: '#/components/schemas/Actor'
        request:
          type: object
          required:
            - id
          properties:
            id:
              type: string
            ip:
              type: string
            user_agent:
              type: string
        resource_type:
          type: string
        resource_id:
          type: string
        action:
          type: string
        status:
          type: string
          enum:
            - success
            - failure
            - pending
        description:
          type: string
    Actor:
      type: object
      required:
        - id
        - name
      properties:
        id:
          type: string
        email:
          type: string
        name:
          type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
