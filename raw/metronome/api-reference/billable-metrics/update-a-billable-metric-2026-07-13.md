<!-- Source URL: https://docs.metronome.com/api-reference/billable-metrics/update-a-billable-metric.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a billable metric

> Updates only the display name of an existing billable metric. Use this to correct mistakes or apply standardized naming conventions across all billable metrics. Returns the billable metric ID to confirm the update. 

Important: Only the name can be modified via this endpoint; configurations cannot be changed after creation. 

#### Example workflow:
If you need to make changes to a streaming billable metric, for example, Metronome supports easily rolling out these changes using a simple workflow:
1. Duplicate the billable metric
2. Make required changes
3. Save the metric
4. Navigate to the product you have associated with the incorrect metric
5. Schedule the product to reference the newly created metric on the appropriate date




## OpenAPI

````yaml /openapi.json put /v1/billable-metrics/{billable_metric_id}
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
  /v1/billable-metrics/{billable_metric_id}:
    put:
      tags:
        - Billable metrics
      summary: Update a billable metric
      description: >
        Updates only the display name of an existing billable metric. Use this
        to correct mistakes or apply standardized naming conventions across all
        billable metrics. Returns the billable metric ID to confirm the update. 


        Important: Only the name can be modified via this endpoint;
        configurations cannot be changed after creation. 


        #### Example workflow:

        If you need to make changes to a streaming billable metric, for example,
        Metronome supports easily rolling out these changes using a simple
        workflow:

        1. Duplicate the billable metric

        2. Make required changes

        3. Save the metric

        4. Navigate to the product you have associated with the incorrect metric

        5. Schedule the product to reference the newly created metric on the
        appropriate date
      operationId: updateBillableMetric-v1
      parameters:
        - $ref: '#/components/parameters/BillableMetricId'
      requestBody:
        description: The billable metric to update
        content:
          application/json:
            schema:
              type: object
              required:
                - name
              properties:
                name:
                  type: string
                  description: The new name of the metric
            example:
              name: CPU hours
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
components:
  parameters:
    BillableMetricId:
      name: billable_metric_id
      in: path
      required: true
      schema:
        type: string
        format: uuid
      example: 13117714-3f05-48e5-a6e9-a66093f13b4d
  schemas:
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
