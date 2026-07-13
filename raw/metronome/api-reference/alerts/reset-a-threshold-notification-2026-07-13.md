<!-- Source URL: https://docs.metronome.com/api-reference/alerts/reset-a-threshold-notification.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reset a threshold notification

> Force an immediate re-evaluation of a specific threshold notification for a customer, clearing any previous state and triggering a fresh assessment against current thresholds. This endpoint ensures threshold notification accuracy after configuration changes or data corrections.

### Use this endpoint to:
- Clear false positive threshold notifications after fixing data issues
- Re-evaluate threshold notifications after adjusting customer balances or credits
- Test threshold notification behavior during development and debugging
- Resolve stuck threshold notification that may be in an incorrect state
- Trigger immediate evaluation after threshold modifications

### Key response fields: 
- 200 Success: Confirmation that the threshold notification has been reset and re-evaluation initiated
- No response body is returned - the operation completes asynchronously

### Usage guidelines:
- Immediate effect: Triggers re-evaluation instantly, which may result in new webhook notifications if thresholds are breached
- State clearing: Removes any cached evaluation state, ensuring a fresh assessment
- Use sparingly: Intended for exceptional cases, not routine operations
- Asynchronous processing: The reset completes immediately, but re-evaluation happens in the background




## OpenAPI

````yaml /openapi.json post /v1/customer-alerts/reset
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
  /v1/customer-alerts/reset:
    post:
      tags:
        - Alerts
      summary: Reset a threshold notification
      description: >
        Force an immediate re-evaluation of a specific threshold notification
        for a customer, clearing any previous state and triggering a fresh
        assessment against current thresholds. This endpoint ensures threshold
        notification accuracy after configuration changes or data corrections.


        ### Use this endpoint to:

        - Clear false positive threshold notifications after fixing data issues

        - Re-evaluate threshold notifications after adjusting customer balances
        or credits

        - Test threshold notification behavior during development and debugging

        - Resolve stuck threshold notification that may be in an incorrect state

        - Trigger immediate evaluation after threshold modifications


        ### Key response fields: 

        - 200 Success: Confirmation that the threshold notification has been
        reset and re-evaluation initiated

        - No response body is returned - the operation completes asynchronously


        ### Usage guidelines:

        - Immediate effect: Triggers re-evaluation instantly, which may result
        in new webhook notifications if thresholds are breached

        - State clearing: Removes any cached evaluation state, ensuring a fresh
        assessment

        - Use sparingly: Intended for exceptional cases, not routine operations

        - Asynchronous processing: The reset completes immediately, but
        re-evaluation happens in the background
      operationId: resetCustomerAlerts-v1
      requestBody:
        description: >-
          The customer ID and notification ID of the threshold notification to
          reset
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ResetCustomerAlertsPayload'
            example:
              alert_id: 5e8691bf-b22a-4672-922d-f80eee940f01
              customer_id: 4c83caf3-8af4-44e2-9aeb-e290531726d9
      responses:
        '200':
          description: Success
components:
  schemas:
    ResetCustomerAlertsPayload:
      required:
        - customer_id
        - alert_id
      type: object
      properties:
        customer_id:
          type: string
          format: uuid
          description: The Metronome ID of the customer
        alert_id:
          type: string
          format: uuid
          description: The Metronome ID of the threshold notification
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
