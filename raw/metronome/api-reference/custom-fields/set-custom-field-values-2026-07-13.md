<!-- Source URL: https://docs.metronome.com/api-reference/custom-fields/set-custom-field-values.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set custom field values

> Sets custom field values on a specific Metronome entity instance. Overwrites existing values for matching keys while preserving other fields. All updates are transactional—either all values are set or none are. Custom field values are limited to 200 characters each.




## OpenAPI

````yaml /openapi.json post /v1/customFields/setValues
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
  /v1/customFields/setValues:
    post:
      tags:
        - Custom fields
      summary: Set custom field values
      description: >
        Sets custom field values on a specific Metronome entity instance.
        Overwrites existing values for matching keys while preserving other
        fields. All updates are transactional—either all values are set or none
        are. Custom field values are limited to 200 characters each.
      operationId: setCustomFields-v1
      requestBody:
        description: The custom field values to set
        content:
          application/json:
            schema:
              type: object
              required:
                - entity
                - entity_id
                - custom_fields
              properties:
                entity:
                  $ref: '#/components/schemas/ManagedEntity'
                entity_id:
                  type: string
                  format: uuid
                custom_fields:
                  $ref: '#/components/schemas/CustomField'
            example:
              entity: customer
              entity_id: 99594816-e8a5-4bca-be21-8d1de0f45120
              custom_fields:
                x_account_id: KyVnHhSBWl7eY2bl
      responses:
        '200':
          description: Success
components:
  schemas:
    ManagedEntity:
      type: string
      enum:
        - alert
        - billable_metric
        - charge
        - commit
        - contract_credit
        - contract_product
        - contract
        - customer
        - discount
        - invoice
        - professional_service
        - product
        - rate_card
        - scheduled_charge
        - subscription
        - package_commit
        - package_credit
        - package_subscription
        - package_scheduled_charge
      x-mint-enum:
        professional_service:
          - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
