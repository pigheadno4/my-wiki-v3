<!-- Source URL: https://docs.metronome.com/api-reference/invoices/regenerate-an-invoice.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Regenerate an invoice

> This endpoint regenerates a voided invoice and recalculates the invoice based on up-to-date rates, available balances, and other fees regardless of the billing period.

### Use this endpoint to:
Recalculate an invoice with updated rate terms, available balance, and fees to correct billing disputes or discrepancies

### Key response fields:
The regenerated invoice id, which is distinct from the previously voided invoice.

### Usage guidelines:
If an invoice is attached to a contract with a billing provider on it, the regenerated invoice will be distributed based on the configuration.




## OpenAPI

````yaml /openapi.json post /v1/invoices/regenerate
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
  /v1/invoices/regenerate:
    post:
      tags:
        - Invoices
      summary: Regenerate an invoice
      description: >
        This endpoint regenerates a voided invoice and recalculates the invoice
        based on up-to-date rates, available balances, and other fees regardless
        of the billing period.


        ### Use this endpoint to:

        Recalculate an invoice with updated rate terms, available balance, and
        fees to correct billing disputes or discrepancies


        ### Key response fields:

        The regenerated invoice id, which is distinct from the previously voided
        invoice.


        ### Usage guidelines:

        If an invoice is attached to a contract with a billing provider on it,
        the regenerated invoice will be distributed based on the configuration.
      operationId: regenerateInvoice-v1
      requestBody:
        description: The invoice id to regenerate
        content:
          application/json:
            schema:
              type: object
              required:
                - id
              properties:
                id:
                  description: The invoice id to regenerate
                  type: string
                  format: uuid
            example:
              id: 6a37bb88-8538-48c5-b37b-a41c836328bd
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    required:
                      - id
                    properties:
                      id:
                        type: string
                        format: uuid
                        description: The new invoice id
              example:
                data:
                  id: 6a37bb88-8538-48c5-b37b-a41c836328bd
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
