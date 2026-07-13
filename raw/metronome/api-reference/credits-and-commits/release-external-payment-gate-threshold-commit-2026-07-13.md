<!-- Source URL: https://docs.metronome.com/api-reference/credits-and-commits/release-external-payment-gate-threshold-commit.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Release external payment gate threshold commit

> If using threshold billing with an external payment gateway, Metronome does not facilitate the payment gating process on behalf of the client. As a result, clients must facilitate the transaction themselves. This end-point is used to either release or cancel the commit pending on the outcome of the external payment attempt.

To release the commit, you must pass the `workflow_id` provided in the `payment_gate.external_initiate` webhook.

### Use this endpoint to:
Facilitate payment gating workflows for threshold billing if using a payment gateway Metronome does not support today.

### Usage guidelines:
Ensure that you are set up to consume the `payment_gate.external_initiate` webhook and save the `workflow_id`.




## OpenAPI

````yaml /openapi.json post /v1/contracts/commits/threshold-billing/release
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
  /v1/contracts/commits/threshold-billing/release:
    post:
      tags:
        - Credits and commits
      summary: Release external payment gate threshold commit
      description: >
        If using threshold billing with an external payment gateway, Metronome
        does not facilitate the payment gating process on behalf of the client.
        As a result, clients must facilitate the transaction themselves. This
        end-point is used to either release or cancel the commit pending on the
        outcome of the external payment attempt.


        To release the commit, you must pass the `workflow_id` provided in the
        `payment_gate.external_initiate` webhook.


        ### Use this endpoint to:

        Facilitate payment gating workflows for threshold billing if using a
        payment gateway Metronome does not support today.


        ### Usage guidelines:

        Ensure that you are set up to consume the
        `payment_gate.external_initiate` webhook and save the `workflow_id`.
      operationId: releaseExternalPaymentGateThresholdCommit-v1
      requestBody:
        description: >-
          Information to identify the workflow that is in progress to release
          the commit, and what action we should take to complete the workflow.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ExternalPaymentGateThresholdCommitPayload'
            example:
              workflow_id: 5576ba1f-4a33-b473-3f05-6162d87b4a33
              outcome: paid
      responses:
        '200':
          description: Success
components:
  schemas:
    ExternalPaymentGateThresholdCommitPayload:
      type: object
      required:
        - workflow_id
        - outcome
      properties:
        workflow_id:
          type: string
          format: uuid
          description: ID of the workflow to continue
        outcome:
          type: string
          enum:
            - paid
            - PAID
            - failed
            - FAILED
          description: The outcome of the external payment gate
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
