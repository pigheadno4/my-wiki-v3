<!-- Source URL: https://docs.metronome.com/api-reference/customers/get-an-embeddable-customer-dashboard.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get an embeddable customer dashboard

> Generate secure, embeddable dashboard URLs that allow you to seamlessly integrate Metronome's billing visualizations directly into your application. This endpoint creates authenticated iframe-ready URLs for customer-specific dashboards, providing a white-labeled billing experience without building custom UI.

### Use this endpoint to:
- Embed billing dashboards directly in your customer portal or admin interface
- Provide self-service access to invoices, usage data, and credit balances
- Build white-labeled billing experiences with minimal development effort

### Key response fields:
- A secure, time-limited URL that can be embedded in an iframe
- The URL includes authentication tokens and configuration parameters
- URLs are customer-specific and respect your security settings

### Usage guidelines:
- Dashboard types: Choose from `invoices`, `usage`, or `commits_and_credits`
- Customization options:
    - `dashboard_options`: Configure dashboard behavior. Supported for the invoices dashboard only. Available keys include: `show_zero_usage_line_items` ("true"/"false"), `contract_id` (UUID, filters invoices by contract), `invoice_type` ("USAGE" or "SCHEDULED", filters by invoice type), and `invoice_status_filter` ("VOID", "FINALIZED", "DRAFT", "FINALIZED_AND_DRAFT", or "ALL")
    - `color_overrides`: Match your brand's color palette
- Iframe implementation: Embed the returned URL directly in an iframe element
- Responsive design: Dashboards automatically adapt to container dimensions




## OpenAPI

````yaml /openapi.json post /v1/dashboards/getEmbeddableUrl
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
  /v1/dashboards/getEmbeddableUrl:
    post:
      tags:
        - Customers
      summary: Get an embeddable customer dashboard
      description: >
        Generate secure, embeddable dashboard URLs that allow you to seamlessly
        integrate Metronome's billing visualizations directly into your
        application. This endpoint creates authenticated iframe-ready URLs for
        customer-specific dashboards, providing a white-labeled billing
        experience without building custom UI.


        ### Use this endpoint to:

        - Embed billing dashboards directly in your customer portal or admin
        interface

        - Provide self-service access to invoices, usage data, and credit
        balances

        - Build white-labeled billing experiences with minimal development
        effort


        ### Key response fields:

        - A secure, time-limited URL that can be embedded in an iframe

        - The URL includes authentication tokens and configuration parameters

        - URLs are customer-specific and respect your security settings


        ### Usage guidelines:

        - Dashboard types: Choose from `invoices`, `usage`, or
        `commits_and_credits`

        - Customization options:
            - `dashboard_options`: Configure dashboard behavior. Supported for the invoices dashboard only. Available keys include: `show_zero_usage_line_items` ("true"/"false"), `contract_id` (UUID, filters invoices by contract), `invoice_type` ("USAGE" or "SCHEDULED", filters by invoice type), and `invoice_status_filter` ("VOID", "FINALIZED", "DRAFT", "FINALIZED_AND_DRAFT", or "ALL")
            - `color_overrides`: Match your brand's color palette
        - Iframe implementation: Embed the returned URL directly in an iframe
        element

        - Responsive design: Dashboards automatically adapt to container
        dimensions
      operationId: embeddableDashboard-v1
      requestBody:
        description: The details of the dashboard to retrieve
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EmbeddableDashboardPayload'
            example:
              customer_id: 4db51251-61de-4bfe-b9ce-495e244f3491
              dashboard: invoices
              dashboard_options:
                - key: show_zero_usage_line_items
                  value: 'false'
                - key: invoice_status_filter
                  value: FINALIZED
              color_overrides:
                - name: Gray_dark
                  value: '#ff0000'
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
                    type: object
                    properties:
                      url:
                        type: string
              example:
                data:
                  url: >-
                    https://embeddable-dashboards.metronome.com/customers/invoices/v1?...
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    EmbeddableDashboardPayload:
      required:
        - customer_id
        - dashboard
      type: object
      properties:
        customer_id:
          type: string
          format: uuid
        dashboard:
          type: string
          enum:
            - invoices
            - usage
            - commits_and_credits
          description: The type of dashboard to retrieve.
        dashboard_options:
          type: array
          description: Optional dashboard specific options
          items:
            type: object
            required:
              - key
              - value
            properties:
              key:
                type: string
                description: The option key name
                enum:
                  - show_zero_usage_line_items
                  - contract_id
                  - invoice_type
                  - invoice_status_filter
                  - hide_voided_invoices
                  - billable_status_filter
                x-mint-enum:
                  billable_status_filter:
                    - client_id:11db091c-975b-4908-9f67-b1ceb126acdf
              value:
                type: string
                description: >-
                  The option value. For show_zero_usage_line_items: "true" or
                  "false" (default "false"). For contract_id: a UUID filtering
                  invoices to a specific contract. For invoice_type: "USAGE" or
                  "SCHEDULED". For invoice_status_filter: "VOID", "FINALIZED",
                  "DRAFT", "FINALIZED_AND_DRAFT", or "ALL". For
                  hide_voided_invoices (deprecated): "true" or "false".
        color_overrides:
          type: array
          description: Optional list of colors to override
          items:
            type: object
            properties:
              name:
                type: string
                description: The color to override
                enum:
                  - Gray_dark
                  - Gray_medium
                  - Gray_light
                  - Gray_extralight
                  - White
                  - Primary_medium
                  - Primary_light
                  - UsageLine_0
                  - UsageLine_1
                  - UsageLine_2
                  - UsageLine_3
                  - UsageLine_4
                  - UsageLine_5
                  - UsageLine_6
                  - UsageLine_7
                  - UsageLine_8
                  - UsageLine_9
                  - Primary_green
                  - Primary_red
                  - Progress_bar
                  - Progress_bar_background
                  - Action
                  - Action_hover
              value:
                type: string
                description: Hex value representation of the color
    Error:
      required:
        - message
      type: object
      properties:
        message:
          type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
