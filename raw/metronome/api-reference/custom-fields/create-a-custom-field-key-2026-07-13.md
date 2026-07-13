<!-- Source URL: https://docs.metronome.com/api-reference/custom-fields/create-a-custom-field-key.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a custom field key

> Creates a new custom field key for a given entity (e.g. billable metric, contract, alert).

Custom fields are properties that you can add to Metronome objects to store metadata like foreign keys or other descriptors. This metadata can get transferred to or accessed by other systems to contextualize Metronome data and power business processes. For example, to service workflows like revenue recognition, reconciliation, and invoicing, custom fields help Metronome know the relationship between entities in the platform and third-party systems.

### Use this endpoint to:
- Create a new custom field key for Customer objects in Metronome. You can then use the Set Custom Field Values endpoint to set the value of this key for a specific customer. 
- Specify whether the key should enforce uniqueness. If the key is set to enforce uniqueness and you attempt to set a custom field value for the key that already exists, it will fail. 

### Usage guidelines:
- Custom fields set on commits, credits, and contracts can be used to scope alert evaluation. For example, you can create a spend threshold alert that only considers spend associated with contracts with custom field key `contract_type` and value `paygo`
- Custom fields set on products can be used in the Stripe integration to set metadata on invoices.
- Custom fields for customers, contracts, invoices, products, commits, scheduled charges, and subscriptions are passed down to the invoice.




## OpenAPI

````yaml /openapi.json post /v1/customFields/addKey
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
  /v1/customFields/addKey:
    post:
      tags:
        - Custom fields
      summary: Create a custom field key
      description: >
        Creates a new custom field key for a given entity (e.g. billable metric,
        contract, alert).


        Custom fields are properties that you can add to Metronome objects to
        store metadata like foreign keys or other descriptors. This metadata can
        get transferred to or accessed by other systems to contextualize
        Metronome data and power business processes. For example, to service
        workflows like revenue recognition, reconciliation, and invoicing,
        custom fields help Metronome know the relationship between entities in
        the platform and third-party systems.


        ### Use this endpoint to:

        - Create a new custom field key for Customer objects in Metronome. You
        can then use the Set Custom Field Values endpoint to set the value of
        this key for a specific customer. 

        - Specify whether the key should enforce uniqueness. If the key is set
        to enforce uniqueness and you attempt to set a custom field value for
        the key that already exists, it will fail. 


        ### Usage guidelines:

        - Custom fields set on commits, credits, and contracts can be used to
        scope alert evaluation. For example, you can create a spend threshold
        alert that only considers spend associated with contracts with custom
        field key `contract_type` and value `paygo`

        - Custom fields set on products can be used in the Stripe integration to
        set metadata on invoices.

        - Custom fields for customers, contracts, invoices, products, commits,
        scheduled charges, and subscriptions are passed down to the invoice.
      operationId: addCustomFieldKey-v1
      requestBody:
        description: Add a key to the allow list for an entity
        content:
          application/json:
            schema:
              type: object
              required:
                - entity
                - key
                - enforce_uniqueness
              properties:
                entity:
                  $ref: '#/components/schemas/ManagedEntity'
                key:
                  type: string
                enforce_uniqueness:
                  type: boolean
            example:
              entity: customer
              key: x_account_id
              enforce_uniqueness: true
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
